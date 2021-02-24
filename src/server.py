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
def func_hand(*,arg:EchoArgs):
    if arg.msg.startswith("group"):
        func_name = arg.msg.replace("group","")
        res = function_manager.call_group(func_name,**arg.arg)
    else:
        res = function_manager.func_dc[arg.msg](**arg.arg)
    return {
        "res":res
        }


def run_cmd():
    while True:
        s = input(">>>")
        if s == "exit":
            print("-------- exit app --------")
            return
        if s == "":
            continue
        # 先取第一个参数是基本命令
        cmd_commd = s.split(" ")[0]
        s = s.replace(cmd_commd,"")
        s = s.strip()
        # 然后是附加参数
        kwargs_dc = {}
        cmd_args = s.split("-")
        for arg in cmd_args:
            if arg == "":
                continue
            s_l = arg.split(" ")
            kwargs_dc[s_l[0]] = s_l[1]
        res = function_manager.func_dc[cmd_commd](**kwargs_dc)
        print(res)