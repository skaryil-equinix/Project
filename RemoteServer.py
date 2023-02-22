import paramiko

from FileLocation import FileLocation

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

hostname = None
username = None
password = None

class RemoteServer(FileLocation):

    def set_connection_to_database(self):
        ssh.connect(hostname=hostname, username=username, password=password)
