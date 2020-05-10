import paramiko


class SshClient:

    def __init__(self, hostname, username, password, port):
        self.ssh_client = paramiko.SSHClient()
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname=hostname, username=username, password=password, port=port)

    @property
    def client(self):
        return self.ssh_client

    def destroy(self):
        self.ssh_client.close()
