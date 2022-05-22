# freepdfapp
this is my final repo of this project


# to run this project into docker container 

# write Dockerfile to build image

FROM python:3.8
WORKDIR /freepdf_app
COPY requirements.txt requirements.txt
COPY . .
RUN ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# After writing dockerfile build the image

sudo docker build --tag freepdfapp/latest .

# After building the image run the container to deploy the project

sudo docker run -d -p 8000:8000 freepdfapp/latest

# now goto your browser and type

localhost:8000/freepdf/home  "press enter"

# boom your project is hosted now
