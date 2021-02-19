from sqlalchemy.sql.functions import user
from server import session
from data.db import Server

def save_server(ip,port,password,user_name,name):
    # 以ip和用户名为唯一标识
    server_data = session.query(Server).filter_by(ip=ip,user_name = user_name).first()
    if server_data is None:
        server_data = Server()
    server_data.ip = ip
    server_data.port = port
    server_data.name = name
    server_data.user_name = user_name
    server_data.password = password
    if server_data is None:
        session.add(server_data)
    session.commit()
    return "ok"


def get_server(name):
    server_data = session.query(Server).filter_by(name = name).first()
    if server_data is None:
        return 1001,f"未找到：{name}对应的数据"
    return 1000,server_data