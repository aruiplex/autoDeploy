# autoDeploy
This is a tool to automatically deploy app to server. 

## App arch
In the `deploy.py` there has a demo of deploying Java Springboot.

The `id_rsa.json` is the config file of deploying. 

## Processing logic

1. check port occupied.
  1. if occuipied: stop occupy process. 
  2. if not: continue.
2. git pull
3. maven build package.



This is a example output of the app.

```bash
PS D:\aruixDAO\Code\Teaforence\tools> python .\deploy.py
端口7022正在占用, 已停止, 进程信息:
 tcp6       0      0 :::7022                 :::*                    LISTEN      147101/java

git正在拉取
git拉取完毕 Updating 69e8347..b5f6c5b
Fast-forward
 .gitignore      |  4 +--
 tools/deploy.py | 84 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 85 insertions(+), 3 deletions(-)
 create mode 100644 tools/deploy.py

mvn正在打包
mvn打包完成: [INFO] Scanning for projects...
[INFO] 
[INFO] -------------------------< com.teaforence:api >-------------------------
[INFO] Building 采茶/Teaforence 1.1.3
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] --- maven-clean-plugin:3.1.0:clean (default-clean) @ api ---
[INFO] Deleting /tea_repo/teaforence/api/target
[INFO] 
[INFO] --- maven-resources-plugin:3.1.0:resources (default-resources) @ api ---
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] Copying 1 resource
[INFO] Copying 2 resources
[INFO] 
[INFO] --- maven-compiler-plugin:3.8.1:compile (default-compile) @ api ---     
[INFO] Changes detected - recompiling the module!
[INFO] Compiling 196 source files to /tea_repo/teaforence/api/target/classes   
[INFO] /tea_repo/teaforence/api/src/main/java/com/teaforence/api/controller/tea/TeaforenceController.java: Some input files use or override a deprecated API.
[INFO] --- maven-resources-plugin:3.1.0:testResources (default-testResources) @ api ---
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] skip non existing resourceDirectory /tea_repo/teaforence/api/src/test/resources
[INFO] --- maven-compiler-plugin:3.8.1:testCompile (default-testCompile) @ api ---
[INFO] No sources to compile
[INFO]
[INFO] --- maven-surefire-plugin:2.22.2:test (default-test) @ api ---
[INFO] No tests to run.
[INFO]
[INFO] --- maven-jar-plugin:3.2.0:jar (default-jar) @ api ---
[INFO] Building jar: /tea_repo/teaforence/api/target/api-1.1.3.jar
[INFO]
[INFO] --- spring-boot-maven-plugin:2.3.3.RELEASE:repackage (repackage) @ api ---
[INFO] Replacing main artifact with repackaged archive
[INFO]
[INFO] --- spring-boot-maven-plugin:2.3.3.RELEASE:repackage (default-cli) @ api ---
[INFO] Replacing main artifact with repackaged archive
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  22.510 s
[INFO] Finished at: 2021-04-12T01:48:26+08:00
[INFO] ------------------------------------------------------------------------


Java 运行:
root      150924  102  3.2 2547628 65212 pts/0   Sl   01:48   0:01 java -jar ./api-1.1.3.jar
root      150937  0.0  0.1   9492  3236 ?        Ss   01:48   0:00 bash -c ps -aux | grep java
root      150939  0.0  0.0   8900   668 ?        S    01:48   0:00 grep java

```
