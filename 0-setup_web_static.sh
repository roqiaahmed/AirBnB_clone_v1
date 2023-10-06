#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
SRC="/etc/nginx/sites-available/default"
STATIC="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Holberton School" | sudo tee "/data/web_static/releases/test/index.html"
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start

# #!/usr/bin/env bash
# # sets up the web servers for the deployment of web_static

# sudo apt-get -y update
# sudo apt-get -y install nginx
# sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
# echo "<html>
#   <head>
#   </head>
#   <body>
#     Holberton School
#   </body>
# </html>" > /data/web_static/releases/test/index.html
# sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# sudo chown -R ubuntu:ubuntu /data/
# sed -i "61i\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default
# sudo service nginx restart
