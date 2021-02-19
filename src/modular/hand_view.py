from loguru import logger

class FunctionManager:
    
    def __init__(self):
        logger.info("初始化回调")
        self.func_dc = {}

    def __call__(self, func_name, *args, **kwargs):
        def register(cls):
            self.func_dc[func_name] = cls
            return cls
        return register


function_manager = FunctionManager()

@function_manager(func_name="hand_test")
def hand_test(**kwargs):
    print(kwargs)
    return kwargs


@function_manager(func_name="comd")
def comd(ip,port,pas,name = "",**kwargs):
    if name == "":
        pass
    return "1"

@function_manager(func_name="connect")
def connect(ip="",port=0,name="",save=0,**kwargs):
    pass