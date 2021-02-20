import sys,logging
from paramiko.client import SSHClient, AutoAddPolicy
from paramiko import AuthenticationException
from paramiko.ssh_exception import NoValidConnectionsError
 
class SShClient(SSHClient):
 
    def ssh_login(self, host_ip,port=22, username="root", password=""):
        try:
            # 设置允许连接known_hosts文件中的主机（默认连接不在known_hosts文件中的主机会拒绝连接抛出SSHException）
            self.set_missing_host_key_policy(AutoAddPolicy())
            self.connect(host_ip, port, username=username, password=password)
        except AuthenticationException:
            logging.warning('username or password error')
            return 1001,'username or password error'
        except NoValidConnectionsError:
            logging.warning('connect time out')
            return 1002,'connect time out'
        except:
            err_str = "Unexpected error: " + str(sys.exc_info()[0])
            logging.error(err_str)
            return 1003,err_str
        return 1000,"ok"
 
    def execute_some_command(self, command):
        stdin, stdout, stderr = self.exec_command(command)
        print(stdout.readline())

    def ssh_logout(self):
        self.close()

    def open(self):
        shell = self.invoke_shell()
        shell.settimeout(1)
        command = input()
        shell.send(command)
        while True:
            try:
                recv = shell.recv(512).decode()
                if recv:
                    print(recv)
                else:
                    continue
            except:
                command = input() +"\n"
                if "exit" in command:
                    break
                shell.send(command)