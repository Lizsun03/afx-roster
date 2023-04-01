# roster-py
revamp roster in python


## Requirements
- Docker
- Python3 and Pip3 (only used for installing dependencies and running locally)


## Backend Setup Instructions
- Make sure the Docker daemon is running 
- Optional: Run `pip install -r requirements.txt`
  - Just in case you want to test without Docker
- Run `./build_and_run.sh`
  - If you get a permissions error, run `chmod +x ./run.sh` first
  - If this command does not work, run the docker-compose commands in the build_and_run.sh file
- Send a GET request to `http://localhost:5000/`
  - You can use Insomnia or Postman to send the request, or just run the following in a terminal window: `curl --request GET \
  --url http://localhost:5000/`
