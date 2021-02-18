from fastapi import FastAPI
from lib.logger import init_log
from pydantic import BaseModel

app = FastAPI()

init_log()

from modular.hand_view import function_manager

class EchoArgs(BaseModel):
    msg:str
    arg:dict = {} # 其他参数

@app.post("/msg")
async def func_hand(*,arg:EchoArgs):
    res = function_manager.func_dc[arg.msg](**arg.arg)
    return {
        "res":res
        }