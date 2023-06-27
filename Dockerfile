# Use the official Python image as the base image


FROM python:3.9

RUN pip3 install --upgrade pip
# Set the working directory in the c/.

# Copy the application files into the working directory
COPY . /.

# Install the application dependencies
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD python3 app.py
