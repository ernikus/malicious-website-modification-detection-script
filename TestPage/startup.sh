#!/usr/bin/bash

sudo chmod 644 index.html
echo "Changed Permission to: index.html"


echo "Go to: http://127.0.0.1:8080/"


pwd=$(pwd)
sudo docker run -it --rm -d -p 8080:80 --name web -v "$(pwd)/":/usr/share/nginx/html nginx

echo "Done!"