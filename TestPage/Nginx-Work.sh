#!/usr/bin/bash

echo "Go to: http://127.0.0.1:8080/"

sudo docker run -it --rm -p 8080:80 --name MyTestPage nginx

echo "Done!"