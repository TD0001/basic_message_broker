this program is using the type of message broker: RabbitMQ

The output may result in AMQPConnectionError. Therefore, 

before running the program, we should install docker(tested on Kali Linux)
           sudo apt  install docker.io
Then run the docker
        docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management