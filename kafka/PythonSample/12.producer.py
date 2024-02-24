import sys
from kafka import KafkaProducer
from time import sleep

def producer(topicName):

    # 개인환경으로 변경
    bootstrap_servers='my-cluster.kafka.43.203.62.69.nip.io:32100'
    sasl_plain_username='edu-user'
    sasl_plain_password='oXTjENLJMvdKV6CbQmU2NX0e87Rezxhc'
    topic_name=topicName     # <-- 본인 타픽명으로 지정


    print(f"KafkaProducer...")
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                            security_protocol="SASL_PLAINTEXT",
                            sasl_mechanism='SCRAM-SHA-512',
                            ssl_check_hostname=True,
                            sasl_plain_username=sasl_plain_username,
                            sasl_plain_password=sasl_plain_password)

    # 10000건을 0.5초에 한번씩 발송해보자.
    print(f"topicName[{topic_name}] subscribed!")
    print(f"Producing...")
    for i in range(10000):
        print(i)
        sleep(0.5)
        producer.send(topic_name, b'{"eventName":"a","num":%d,"title":"a", "writeId":"", "writeName": "", "writeDate":"" }' % i)

    # 테스트를 끝내려면 Ctrl + C 로 중지하자.
        
if __name__ == '__main__':
    producer(sys.argv[1])

