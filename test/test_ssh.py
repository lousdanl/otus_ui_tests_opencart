import re

STDOUT_DOCKER_MARIADB = "anastasia_mariadb_1"
STDOUT_DOCKER_OPENCART = "anastasia_opencart_1"
STDUT_RESTART_MARIADB = "Restarting anastasia_mariadb_1"
STDUT_RESTART_OPENCART = "Restarting anastasia_opencart_1"
STDUT_CREATE_MARIADB = "Creating anastasia_mariadb_1"
STDOUT_CREATE_OPENCART = "Creating anastasia_opencart_1"


def docker_restart(ssh):
    stdin, stdout, stderr = ssh.client.exec_command("sudo docker-compose restart \n")
    data = stdout.read() + stderr.read()
    data = data.decode("utf-8")
    output = re.findall(r"(\w+ \w+)", data)
    assert STDUT_RESTART_MARIADB, STDUT_RESTART_OPENCART in output


def docker_up(ssh):
    stdin, stdout, stderr = ssh.client.exec_command("sudo docker-compose up -d \n")
    data = stdout.read() + stderr.read()
    data = data.decode("utf-8")
    output = re.findall(r"(\w+ \w+)", data)
    assert STDUT_CREATE_MARIADB, STDOUT_CREATE_OPENCART in output


def test_docker_restart(ssh):
    stdin, stdout, stderr = ssh.client.exec_command("sudo docker-compose ps \n")
    data = stdout.read() + stderr.read()
    data = data.decode("utf-8")
    output = re.findall(r"(\w+ )", data)
    if STDOUT_DOCKER_MARIADB and STDOUT_DOCKER_OPENCART in output:
        docker_restart(ssh)
    else:
        docker_up(ssh)
        docker_restart(ssh)
