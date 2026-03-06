import json
import azure.durable_functions as df

def incident_orchestrator(context: df.DurableOrchestrationContext):
    payload = context.get_input()
    event = json.loads(payload)

    incident = yield context.call_activity("store_incident", event)
    fix = yield context.call_activity("find_known_fix", event)

    if not fix:
        result = {
            "incidentId": incident.get("incidentId"),
            "status": "no_known_fix"
        }
        yield context.call_activity("update_incident", result)
        return result

    approval = yield context.call_activity("request_approval", {
        "incident": incident,
        "fix": fix
    })

    if not approval.get("approved", False):
        result = {
            "incidentId": incident.get("incidentId"),
            "status": "rejected"
        }
        yield context.call_activity("update_incident", result)
        return result

    execution = yield context.call_activity("execute_remediation", {
        "incident": incident,
        "fix": fix
    })

    result = {
        "incidentId": incident.get("incidentId"),
        "status": "completed" if execution.get("success") else "failed",
        "execution": execution
    }
    yield context.call_activity("update_incident", result)
    return result

app = df.Blueprint()
app.orchestration_trigger(context_name="context")(incident_orchestrator)
