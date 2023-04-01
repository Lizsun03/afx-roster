FROM python:3.8-slim

# create and change to this directory
WORKDIR /python-docker

#update the container
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

# Copy our requirements file to the container and install the dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip3 install -r requirements.txt

# Copy the rest of our project files to the container
COPY . .

# tells the OS what the current flask application is
ENV FLASK_APP=roster

# treat this container as an executable
ENTRYPOINT [ "python3" ]

# pass in python+flask arguments, run on localhost
CMD ["-m" , "flask", "run", "--host=0.0.0.0"]