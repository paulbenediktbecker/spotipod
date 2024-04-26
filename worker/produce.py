
print("sending...")


from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:29092')
for _ in range(1):
    try:
        # Produce a message to the specified topic
        producer.send("my_favorite_topic", key=b'key', value=b'your_message')
        producer.flush()  # Wait for any outstanding messages to be delivered
        print('Message sent successfully.')
    except Exception as e:
        print(f'Error producing message: {str(e)}')
    finally:
        producer.close()
    print("sent")

