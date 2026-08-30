FROM python:3.9-slim

#Set the working directory inside the container
WORKDIR/app

#Copy all files from current directory to the containers working directory
COPY . .

# Install dependencies from the requireents file without using cashe ro reduce image size
RUN pip install --no-cache-dir --upgrade -r requiements.txt

# Define the command to start the application using Gunicorn with 4 worker processes
# - `-w 4`: Uses 4 worker processes for handling requests
# - `-b 0.0.0:7860`: Binds the server to port 7860 on all network interfaces
# - `app:app`: Runs the Flask app (assuming `app.py' contains the Flask instance named `app`)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0:7860", "Learner_predictor_api:Learner_predictor_api"]
