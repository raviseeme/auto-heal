import os
import json
import uuid
from datetime import datetime, timezone

import azure.functions as func
from azure.servicebus import ServiceBusClient, ServiceBusMessage

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

SERVICEBUS_CONNECTION = os.getenv("SERVICEBUS_CONNECTION")
QUEUE_NAME = os.getenv("REMEDIATION_QUEUE_NAME", "remediation-events")


def build_event(payload: dict) -> dict:
    return {
        "eventId": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": payload.get("source", "manual"),
        "environment": payload.get("environment", "dev"),
        "resourceType": payload.get("resourceType", "vm"),
        "resourceId": payload.get("resourceId", "unknown-resource"),
        "severity": payload.get("severity", "medium"),
        "alertName": payload.get("alertName", "manual-alert"),
        "description": payload.get("description", ""),
        "correlationId": payload.get("correlationId", str(uuid.uuid4())),
        "metadata": payload.get("metadata", {})
    }


@app.route(route="ingest")
def ingest(req: func.HttpRequest) -> func.HttpResponse:
    if not SERVICEBUS_CONNECTION:
        return func.HttpResponse(
            "Missing SERVICEBUS_CONNECTION app setting.",
            status_code=500
        )

    try:
        payload = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON body.", status_code=400)

    event = build_event(payload)

    with ServiceBusClient.from_connection_string(SERVICEBUS_CONNECTION) as client:
        sender = client.get_queue_sender(queue_name=QUEUE_NAME)
        with sender:
            sender.send_messages(ServiceBusMessage(json.dumps(event)))

    return func.HttpResponse(
        json.dumps({"status": "queued", "event": event}),
        mimetype="application/json",
        status_code=202
    )
