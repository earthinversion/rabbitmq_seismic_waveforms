
## Install
```bash
conda activate rabbitmq

pip install pika
```

## Deploy RabbitMQ server
```bash
docker build -t container-rabbitmq . #build the image
docker run -d --name rabbitmq-server -p 5672:5672 -p 15672:15672 container-rabbitmq #run the container

```

- Open the webpage: http://localhost:15672
```
admin
admin123
```
