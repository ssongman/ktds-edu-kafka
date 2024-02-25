
################################################################
# Consumer 기본
################################################################

from datetime import datetime
import sys
from kafka import KafkaConsumer
import configparser
import time

config  = configparser.ConfigParser()  ## 클래스 객체 생성
config.read('./kafka/PythonSample/config.ini', encoding='utf-8')


def consumer(group_id='edu-topic01-b-cg', auto_offset_reset='latest'):
    bootstrap_servers=config["KAFKAINFO"]["bootstrap_servers"]
    sasl_plain_username=config["KAFKAINFO"]["sasl_plain_username"]
    sasl_plain_password=config["KAFKAINFO"]["sasl_plain_password"]
    topic_name=config["KAFKAINFO"]["topic_name"]
    group_id=config["KAFKAINFO"]["group_id"]
    """
    ex) topic_name : edu-topic01
        group_id   : edu-topic01-cg
    """

    print(f"KafkaConsumer group_id[{group_id}] auto_offset_reset[{auto_offset_reset}]  ...")
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers,
                            security_protocol="SASL_PLAINTEXT",
                            sasl_mechanism='SCRAM-SHA-512',
                            sasl_plain_username=sasl_plain_username,
                            sasl_plain_password=sasl_plain_password,
                            ssl_check_hostname=True,
                            auto_offset_reset=auto_offset_reset,
                            enable_auto_commit=False,
                            # auto_commit_interval_ms=60000,
                            group_id=group_id,
                            max_poll_records=500, # default 500
                            max_poll_interval_ms=300000 # default 300000
                            )

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
        consumer.commit()
    # end for


    
    # # 메세지 읽기
    # print(f"Consuming...")
    # while True:
    #     message = consumer.poll()
    #     if len(message) == 0: 
    #         time.sleep(1)
    #     for topic_partition, records in message.items():
    #         kmsgs = []
    #         for record in records:
    #             msg = record.value
    #             dt_rcv = datetime.fromtimestamp(record.timestamp / 1000).strftime("%H%M%S.%f")[:-3]
    #             dt_cre = datetime.now().strftime("%H%M%S.%f")[:-3]
    #             # msg['rcvDt'] = dt_rcv
    #             # msg['creDt'] = dt_cre
    #             #db.demo.insert_one(msg)
    #             kmsgs.append(msg)

    #         print(topic_partition, len(kmsgs))
    #         # db.demo.insert_many(kmsgs)
    # # end while


if __name__ == '__main__':
    # 타픽명을 아규먼트 로 입력 받는다.
    consumer(sys.argv[1], sys.argv[2])
    # consumer()
