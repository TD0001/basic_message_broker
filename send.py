

#Python client recommended by the RabbitMQ team
import pika
message = input("Enter your message: ") #Message muon gui di



connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
#khai bao queue,

q = input("enter your queue: ")
channel.queue_declare(queue=q)


#gui message den queue.
# boi vi trong rabbitMQ, message khong duoc gui truc tiep vao queue ma thong qua exchange, khai bao default exchange = empty string
#queue khai bao o tren duoc cho vao routing key
channel.basic_publish(exchange='',
                      routing_key=q,
                      body=message)


print("Sent your message successfully")


connection.close()
