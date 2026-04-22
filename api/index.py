from fastapi import FastAPI
from mangum import Mangum

# import your existing app
from backend.api import app

handler = Mangum(app)