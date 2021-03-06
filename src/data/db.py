from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

DbTableBase = declarative_base()

class Server(DbTableBase):
    # 指定本类映射到users表
    __tablename__ = 'table_server'
    
    id = Column(Integer,primary_key=True)
    ip = Column(String)
    port = Column(Integer)
    name = Column(String(20))
    password = Column(String(32))
    group = Column(String(64))
    user_name = Column(String(64))

    def __repr__(self):
        return "<Server(ip='%s', fullname='%s', password='%s')>" % (
                   self.ip, self.name, self.password)
    
    def to_str(self):
        return f"{self.id}  {self.ip}  {self.port}  {self.name}  {self.password}  {self.group}  {self.user_name}"