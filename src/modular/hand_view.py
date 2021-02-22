from loguru import logger
from sqlalchemy.sql.functions import func
from modular.alone_server import manager
from lib.ssh_client import SShClient

class FunctionManager:
    
    def __init__(self):
        logger.info("初始化回调")
        self.func_dc = {}
        self.func_explain = {}

    def __call__(self, func_name,func_explain="", *args, **kwargs):
        def register(cls):
            self.func_dc[func_name] = cls
            self.func_explain[func_name] = func_explain
            return cls
        return register


function_manager = FunctionManager()

@function_manager(func_name="hand_test",func_explain="测试")
def hand_test(**kwargs):
    print(kwargs)
    return kwargs


@function_manager(func_name="comd")
def comd(command,ip = "",port = 22,password = "",user_name = "root",name = "",save=0,**kwargs):
    res = "err"
    sc = SShClient()
    if ip != "":
        status,msg =sc.ssh_login(ip, port,user_name,password)
        if status != 1000:
            return msg
        if int(save) == 1:
            res = manager.save_server(ip,port,password,user_name,name)
    elif name != "":
        # 通过别名连接
        s,data = manager.get_server(name)
        if s != 1000:
            return data
        status,msg =sc.ssh_login(data.ip, data.port,data.user_name,data.password)
        if status != 1000:
            return msg
    else:
        return res
    _, stdout, _ = sc.exec_command(command)
    res = stdout.read()
    sc.close()
    return res


@function_manager(func_name="get_server",func_explain="获取服务器列表")
def server_all(name = "",group="",**kwargs):
    return manager.get_all_server(name,group)


@function_manager(func_name="get_cpu",func_explain="获取服务器cpu负载")
def get_top(**kwargs):
    return manager.get_top()


@function_manager(func_name="get_memory",func_explain="获取内存")
def get_memory(**kwargs):
    return manager.get_memory()
