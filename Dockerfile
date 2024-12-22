# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /BajaCloudBackend

# Copy the current directory contents into the container at /app
COPY ./InterviewBooking /BajaCloudBackend/InterviewBooking
# Copy the main file to the working directory
COPY main.py /BajaCloudBackend

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the container to listen on
EXPOSE 8000

# Command to run the Python server when the container starts
#CMD ["fastapi", "run" "main.py"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]

