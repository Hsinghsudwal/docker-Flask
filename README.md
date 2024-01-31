# setup environment

# install dependencies

# run python app if it work

# setup dockerfile

# see how many images on docker

docker ps

docker images

# build docker

docker build -t myapp .

# run the image and keep it running in the background (detached)

# -p port mapping

docker run -d -p myapp

# to check container

docker ps #you will get a container ID, use that to inspect

# docker stop

docker stop <container_id> #stop the container

# docker remove

docker image rm -f <container_id> #remove the container. If you want to remove and save
