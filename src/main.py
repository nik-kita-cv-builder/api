from fastapi import FastAPI

app = FastAPI(swagger_ui_parameters={'TryItOutEnabled': 'true'})


@app.get('/')
def hello_world():
    return {'Hello': 'World'}
