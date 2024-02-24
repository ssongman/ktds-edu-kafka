
import sys
from kafka import KafkaConsumer


def consumer(topicName):
    bootstrap_servers='my-cluster.kafka.43.203.62.69.nip.io:32100'
    sasl_plain_username='edu-user'
    sasl_plain_password='oXTjENLJMvdKV6CbQmU2NX0e87Rezxhc'
    topic_name=topicName                    # <-- 본인 topic명으로 지정
    group_id='edu-group' + topicName[-2:]   # topicName에서 마지막 두자리만 이용하여 groupName 으로 사용한다.


    print(f"KafkaConsumer...")
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
    consumer(sys.argv[1])
