# make sure to do "chmod +x run.sh" if you get a permissions error

docker image build -t flask_docker .

docker run -p 5000:5000 flask_docker