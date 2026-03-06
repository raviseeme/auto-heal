import azure.durable_functions as df

app = df.Blueprint()

@app.activity_trigger(input_name="result")
def update_incident(result: dict):
    return result
