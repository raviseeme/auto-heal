import logging
import azure.functions as func
import azure.durable_functions as df

from orchestrators.incident_orchestrator import app as orchestrator_bp
from activities.store_incident import app as store_incident_bp
from activities.find_known_fix import app as find_known_fix_bp
from activities.request_approval import app as request_approval_bp
from activities.execute_remediation import app as execute_remediation_bp
from activities.update_incident import app as update_incident_bp

app = df.DFApp(http_auth_level=func.AuthLevel.FUNCTION)

app.register_functions(orchestrator_bp)
app.register_functions(store_incident_bp)
app.register_functions(find_known_fix_bp)
app.register_functions(request_approval_bp)
app.register_functions(execute_remediation_bp)
app.register_functions(update_incident_bp)

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