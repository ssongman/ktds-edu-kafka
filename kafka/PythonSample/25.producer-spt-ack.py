################################################################
# ack에 따른 성능측정
################################################################

import sys
from kafka import KafkaProducer
import configparser
from time import sleep
import time

config  = configparser.ConfigParser()  ## 클래스 객체 생성
config.read('./config.ini', encoding='utf-8')

def producer(topic_name, range_cnt=10000, ackValue='0'):
    bootstrap_servers=config["KAFKAINFO"]["bootstrap_servers"]
    sasl_plain_username=config["KAFKAINFO"]["sasl_plain_username"]
    sasl_plain_password=config["KAFKAINFO"]["sasl_plain_password"]
    topic_name=topic_name
    """
    ex) topic_name : edu-topic01
    """


    print(f"KafkaProducer...")
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                            security_protocol="SASL_PLAINTEXT",
                            sasl_mechanism='SCRAM-SHA-512',
                            ssl_check_hostname=True,
                            sasl_plain_username=sasl_plain_username,
                            sasl_plain_password=sasl_plain_password,
                            acks=ackValue)

    # 30000건 테스트
    print(f"topicName[{topic_name}] range_cnt[{range_cnt}] ack[{ackValue}] Producing...")
    start_time = time.time() # 시작시간
    for i in range(range_cnt):
        # print(i)
        producer.send(topic_name, b'{"eventName":"a","num":%d,"title":"a", "writeId":"", "writeName": "", "writeDate":"" }' % i)

    end_time = time.time() # 종료시간
    print("duration time :", end_time - start_time)  # 현재시각 - 시작시간 = 실행 시간

        
if __name__ == '__main__':
    # 타픽명을 아규먼트 로 입력 받는다.
    producer(sys.argv[1], int(sys.argv[2]), sys.argv[3])
    # producer()

