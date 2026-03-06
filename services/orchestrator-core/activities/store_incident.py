import uuid
import azure.durable_functions as df

app = df.Blueprint()

@app.activity_trigger(input_name="event")
def store_incident(event: dict):
    return {
        "incidentId": str(uuid.uuid4()),
        "event": event,
        "status": "received"
    }
