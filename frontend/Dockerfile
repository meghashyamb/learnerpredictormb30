# Use a minimal base image with Python 3.9 installed
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy all files from current directory on the host to the container's /app directory
COPY . .

# Install python dependencies from the requirements.txt file
RUN pip3 install -r requirements.txt

# Define the command to run the Streamlit app on port 8501 and make it accessible externally
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address=0.0.0.0", "--server.enableXsrfProtection=false"]

# Note: XSRF protection disbaled for easier external access in order to make batch predictions
