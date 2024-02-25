
################################################################
# Consumer 기본
################################################################

import sys
from kafka import KafkaConsumer
import configparser

config  = configparser.ConfigParser()  ## 클래스 객체 생성
config.read('./kafka/PythonSample/config.ini', encoding='utf-8')


def consumer():
    bootstrap_servers=config["KAFKAINFO"]["bootstrap_servers"]
    sasl_plain_username=config["KAFKAINFO"]["sasl_plain_username"]
    sasl_plain_password=config["KAFKAINFO"]["sasl_plain_password"]
    topic_name=config["KAFKAINFO"]["topic_name"]
    group_id=config["KAFKAINFO"]["group_id"]
    """
    ex) topic_name : edu-topic01
        group_id   : edu-topic01-cg
    """

    print(f"KafkaConsumer group_id[{group_id}] ...")
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers,
                            security_protocol="SASL_PLAINTEXT",
                            sasl_mechanism='SCRAM-SHA-512',
                            sasl_plain_username=sasl_plain_username,
                            sasl_plain_password=sasl_plain_password,
                            ssl_check_hostname=True,
                            auto_offset_reset='earliest',
                            enable_auto_commit= True,
                            group_id=group_id)

    # 사용할 topic 지정(구독)
    consumer.subscribe(topic_name)
    print(f"topicName[{topic_name}] subscribed!")

    # 메세지 읽기
    print(f"Consuming...")
    for message in consumer:
        print("topic=%s partition=%d offset=%d: key=%s value=%s" %
                (message.topic,
                message.partition,
                message.offset,
                message.key,
                message.value))
        
if __name__ == '__main__':
    # 타픽명을 아규먼트 로 입력 받는다.
    #consumer(sys.argv[1])
    consumer()
