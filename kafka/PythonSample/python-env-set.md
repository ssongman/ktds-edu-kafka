

# 1. python env



## 1) venv

### (1) venv 환경 생성

```sh
$ cd <프로젝트 디렉터리>
$ python -m venv .venv
$ ls -a
.     ..    .venv


$ echo '.venv' >> .gitignore

# activate
$ Scripts\activate.bat
(.venv) $



# deactivate
(.venv) $ Scripts\deactivate.bat
```







# 2. python dockerizing



## 1) docker run

```sh
# bastion Server 에서
## docker 실행이 안되었을 경우만 ....
$ docker run --name python --user root -d python:3.9 sleep 365d


# python 확인
$ docker ps -a
CONTAINER ID  IMAGE                         COMMAND     CREATED        STATUS            PORTS       NAMES
fb231e23f9f1  docker.io/library/python:3.9  sleep 365d  2 seconds ago  Up 2 seconds ago              python


# 1) python Container 내부로 진입( bash 명령 수행)
$ docker exec -it python bash
root@a225dc4c3dd7:/#           <-- 이런 prompt 가 표기 되어야 정상

```



## 2) githubrepo 셋팅

```sh
$ mkdir -p ~/githubrepo
  cd ~/githubrepo

$ git clone https://github.com/ssongman/ktds-edu-kafka.git
    
$ cd ~/githubrepo/ktds-edu-kafka

$ git pull
    
```



## 3) tool 설치



설치

```

apt update

apt install vim

apt install netcat

.bashrc 셋팅


```





## 4) pip install



### (1) 패키지 목록 추출

```sh
$ pip freeze > requirements.txt

```



requirements.txt

```
aiohttp==3.8.6
aiosignal==1.3.1
async-timeout==4.0.3
attrs==23.1.0
certifi==2023.7.22
charset-normalizer==3.3.1
frozenlist==1.4.0
idna==3.4
multidict==6.0.4
numpy==1.26.1
pandas==2.1.2
PyJWT==2.8.0
python-dateutil==2.8.2
pytz==2023.3.post1
pyupbit==0.2.33
redis==5.0.1
requests==2.31.0
six==1.16.0
telepot==12.7
tzdata==2023.3
urllib3==2.0.7
websockets==12.0
yarl==1.9.2

```



```sh
$ cd ~/githubrepo/ktds-edu-kafka

$ cd ~/githubrepo/ktds-edu-kafka/kafka/PythonSample

$ pip install -r requirements.txt

```







## 5) docker commit and push



```sh


$ docker ps
CONTAINER ID   IMAGE                             COMMAND        CREATED        STATUS        PORTS     NAMES
eed489be3084   confluentinc/cp-kafkacat:latest   "sleep 365d"   16 hours ago   Up 16 hours             kafkacat
11507f330c58   python:3.9                        "sleep 365d"   19 hours ago   Up 19 hours             python


$ docker commit python ssongman/ktds-edu-kafka-python:v1.0


$ docker push ssongman/ktds-edu-kafka-python:v1.0
push 안됨


```





# 2. python 배포



## 1) 배포준비



### (1) 최종 library 목록

```sh
$ pip install pyupbit


# 사용 - python 3.9.0 에서 사용가능
$ pip install telepot
# docker pull python:3.12.0   <-- 실패
# docker pull python:3.9.0   <-- 성공


#  - python 3.9.0 이상에서 사용가능
$ pip install python-telegram-bot
$ pip install python-telegram-bot --upgrade



$ pip install PyJWT

$ pip install requests



$ pip install redis


```





### (2) 패키지 목록 추출

```sh
$ pip freeze > requirements.txt

```



requirements.txt

```
aiohttp==3.8.6
aiosignal==1.3.1
async-timeout==4.0.3
attrs==23.1.0
certifi==2023.7.22
charset-normalizer==3.3.1
frozenlist==1.4.0
idna==3.4
multidict==6.0.4
numpy==1.26.1
pandas==2.1.2
PyJWT==2.8.0
python-dateutil==2.8.2
pytz==2023.3.post1
pyupbit==0.2.33
redis==5.0.1
requests==2.31.0
six==1.16.0
telepot==12.7
tzdata==2023.3
urllib3==2.0.7
websockets==12.0
yarl==1.9.2

```



```sh
$ pip install -r requirements.txt

```



