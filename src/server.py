from fastapi import FastAPI
from lib.logger import init_log
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

init_log()

engine = create_engine('sqlite:///data/data.db?check_same_thread=False')
from data.db import DbTableBase
DbTableBase.metadata.create_all(engine)

session_maker = sessionmaker(bind=engine)
session = session_maker()

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