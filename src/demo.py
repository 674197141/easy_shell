import sys,logging
from paramiko.client import SSHClient, AutoAddPolicy
from paramiko import AuthenticationException
from paramiko.ssh_exception import NoValidConnectionsError
 
class SshClient(SSHClient):
 
    def ssh_login(self, host_ip, username, password,port=22):
        try:
            # 设置允许连接known_hosts文件中的主机（默认连接不在known_hosts文件中的主机会拒绝连接抛出SSHException）
            self.set_missing_host_key_policy(AutoAddPolicy())
            self.connect(host_ip, port, username=username, password=password)
        except AuthenticationException:
            logging.warning('username or password error')
            return 1001
        except NoValidConnectionsError:
            logging.warning('connect time out')
            return 1002
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return 1003
        return 1000
 
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

if __name__ == "__main__":
    command = "ls\n"       # 自己使用ssh时，命令怎么敲的command参数就怎么写
    ssh = SshClient()
    if ssh.ssh_login(host_ip="192.168.0.130", username="root", password="123456") == 1000:
        ssh.execute_some_command(command)
        ssh.open()
        ssh.ssh_logout()