#!/usr/bin/bash

sudo chmod 644 index.html
echo "Changed Permission to: index.html"

sudo chmod 755 ./image
echo "Changed Permission to dir: image"

sudo chmod 644 ./image/*
echo "Changed Permission to files in: image"


echo "Go to: http://127.0.0.1:8080/"


docker stop web

pwd=$(pwd)
sudo docker run -it --rm -d -p 8080:80 --name web -v "$(pwd)/":/usr/share/nginx/html nginx

echo "Done!"