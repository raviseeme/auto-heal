import azure.durable_functions as df

app = df.Blueprint()

@app.activity_trigger(input_name="event")
def find_known_fix(event: dict):
    alert = event.get("alertName", "").lower()

    if "service" in alert:
        return {"actionId": "restart_service", "worker": "restart-service"}

    if "agent" in alert:
        return {"actionId": "restart_agent", "worker": "restart-agent"}

    if "disk" in alert:
        return {"actionId": "cleanup_disk", "worker": "cleanup-disk"}

    return None
