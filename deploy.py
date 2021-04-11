import paramiko
import re
import time
import json


with open("./id_rsa.json", "r") as f:
    cfg = json.load(f)

port = cfg["port"]
app_name = cfg["app_name"]
id_rsa_path = cfg["id_rsa_path"]
pwd = cfg["pwd"]

start = time.time()

private_key = paramiko.RSAKey.from_private_key_file(id_rsa_path, password=pwd)

# 实例化SSHClient
client = paramiko.SSHClient()

# 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地 know_hosts 文件中记录的主机将无法连接
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接SSH服务端，以用户名和密码进行认证
client.connect(hostname='dev.teaforence.com', port=22,
               username='root', pkey=private_key)
stdin, stdout, stderr = client.exec_command(f"netstat -tunlp | grep {port}")

output = stdout.read().decode('utf-8')

if output != "":
    pid = re.findall("^.*((?<!\\d)\\d+).*$", output).pop()
    print(f"端口{port}正在占用, 已停止, 进程信息:\n {output}")
    stdin, stdout, stderr = client.exec_command(f"kill {pid}")
else:
    print("没有端口占用")

path = "cd /tea_repo/teaforence/api&&"

print(f"git正在拉取 ")
stdin, stdout, stderr = client.exec_command(f"{path}git pull", timeout=10)
print(f"git拉取完毕 {stdout.read().decode('utf-8')}")

print(f"mvn正在打包")
stdin, stdout, stderr = client.exec_command(
    f"{path}mvn clean package spring-boot:repackage")
print(f"mvn打包完成: {stdout.read().decode('utf-8')}\n")

path = "cd /tea_repo/teaforence/api/target;"

# 以下是两种可行方案
# ==============================================================================

# Add the following code
chan = client.invoke_shell()
# Execute command This method has no return value
chan.send(f"{path}nohup java -jar ./{app_name} &> ./deploy.log &\n")
time.sleep(1)

stdin, stdout, stderr = client.exec_command("ps -aux | grep java")
print(f"Java 运行:\n{stdout.read().decode('utf-8')}")

# ==============================================================================

# # Add the following code
# transport = client.get_transport()
# channel = transport.open_session()
# # Execute command This method has no return value
# channel.exec_command(f"{path}nohup java -jar ./{app_name} &> ./deploy.log &\n")

# ==============================================================================
end = time.time()

print(f"部署成功, 耗时: {end-start}s")

# 打印执行结果
# if stdout.read().decode('utf-8') != "" or stderr.read().decode('utf-8') != "":
#     print(f"stdout: {stdout.read().decode('utf-8')}")
#     print(f"stderr: {stderr.read().decode('utf-8')}")


# 关闭SSHClient
client.close()
