# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.8

# Environment variables
ENV APP_HOME /app

# Expose port
EXPOSE 8080

# Copy local code to the container image.
WORKDIR $APP_HOME
COPY . .

# Install dependencies.
RUN pip install -r requirements.txt

# Run the web service on container startup.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]