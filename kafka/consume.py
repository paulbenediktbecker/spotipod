

print("consuming")    
from kafka import KafkaConsumer
consumer = KafkaConsumer("my_favorite_topic", bootstrap_servers='localhost:29092',
                             auto_offset_reset='earliest', group_id='your_consumer_group')

try:
    # Poll for new messages
    for msg in consumer:
        # Print the received message key and value
        print(f'Received message: Key={msg.key}, Value={msg.value}')
except KeyboardInterrupt:
    pass
finally:
    consumer.close()