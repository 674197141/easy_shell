from sqlalchemy.sql.functions import user
from server import session
from data.db import Server
import psutil

def save_server(ip,port,password,user_name,name):
    # 以ip和用户名为唯一标识
    server_data = session.query(Server).filter_by(ip=ip,user_name = user_name).first()
    new_server = False
    if server_data is None:
        server_data = Server()
        new_server = True
    server_data.ip = ip
    server_data.port = port
    server_data.name = name
    server_data.user_name = user_name
    server_data.password = password
    if new_server:
        session.add(server_data)
    session.commit()
    return "ok"


def get_server(name):
    server_data = session.query(Server).filter_by(name = name).first()
    if server_data is None:
        return 1001,f"未找到：{name}对应的数据"
    return 1000,server_data

def get_all_server(name = "",group = ""):
    server_query = session.query(Server)
    filter_list = []
    if name != "":
        filter_list.append(Server.name == name)
    if group != "":
        filter_list.append(Server.group == group)
    if len(filter_list)>0:
        server_query = server_query.filter(*filter_list)
    server_data = server_query.all()
    server_list = [
        "id         ip     port     name     password     group    user_name"
        ]
    for server in server_data:
        server_list.append(server.to_str())
    p_str = "\n".join(server_list)
    return p_str

def get_top():
    pass

def get_memory():
    mem = psutil.virtual_memory()
    return mem