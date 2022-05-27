# freepdfapp
this is my final repo of this project


# Run this project into docker container 

# Write Dockerfile

FROM python:3.8
WORKDIR /freepdf_app
COPY requirements.txt requirements.txt
COPY . .
RUN ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Build the image

sudo docker build --tag freepdfapp/latest .

# Run the container

sudo docker run -d -p 8000:8000 freepdfapp/latest

# Open browser and type

localhost:8000/freepdf/home  "press enter"


# boom your project is hosted now
