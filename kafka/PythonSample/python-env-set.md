

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



