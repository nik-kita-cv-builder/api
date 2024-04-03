from fastapi import FastAPI
from config import config

app = FastAPI(swagger_ui_parameters={'TryItOutEnabled': 'true'})


@app.get('/')
def hello_world():
    return {'Hello': 'World'}
