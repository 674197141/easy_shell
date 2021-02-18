from fastapi import FastAPI
from lib.logger import init_log

app = FastAPI()

init_log()