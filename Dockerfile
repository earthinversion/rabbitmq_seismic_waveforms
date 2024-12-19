# Use the official RabbitMQ image as the base
FROM rabbitmq:3.11-management

# Expose RabbitMQ ports
# 5672: Main RabbitMQ messaging port
# 15672: Management UI port
EXPOSE 5672 15672

# Enable RabbitMQ management plugin (included in the base image)
RUN rabbitmq-plugins enable --offline rabbitmq_management

# Optional: Copy custom RabbitMQ configuration file (if needed)
# Uncomment and provide a config file if required
# COPY rabbitmq.conf /etc/rabbitmq/rabbitmq.conf

# Optional: Set default user and password (replace with your credentials)
ENV RABBITMQ_DEFAULT_USER=admin
ENV RABBITMQ_DEFAULT_PASS=admin123

# Set up an entry point to start RabbitMQ server
CMD ["rabbitmq-server"]
