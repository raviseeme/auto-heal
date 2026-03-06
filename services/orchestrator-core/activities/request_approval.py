import azure.durable_functions as df

app = df.Blueprint()

@app.activity_trigger(input_name="request_data")
def request_approval(request_data: dict):
    # Phase 1 placeholder.
    # Replace later with Logic App / Teams approval call.
    return {"approved": True, "approvedBy": "phase1-default"}
