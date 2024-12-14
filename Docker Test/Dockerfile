# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./mock /app

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for the container to listen on
EXPOSE 8080

# Command to run the Python server when the container starts
CMD ["python", "server.py"]
