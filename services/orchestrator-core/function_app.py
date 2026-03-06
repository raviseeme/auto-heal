import logging
import azure.functions as func
import azure.durable_functions as df

app = df.DFApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.service_bus_queue_trigger(
    arg_name="msg",
    queue_name="%REMEDIATION_QUEUE_NAME%",
    connection="SERVICEBUS_CONNECTION"
)
@app.durable_client_input(client_name="client")
async def servicebus_starter(msg: func.ServiceBusMessage, client):
    payload = msg.get_body().decode("utf-8")
    instance_id = await client.start_new("incident_orchestrator", None, payload)
    logging.info("Started orchestration with ID = %s", instance_id)
