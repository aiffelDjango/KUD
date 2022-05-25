cd ~

curl -sL https://deb.nodesource.com/setup_16.x | sudo bash -

cat /etc/apt/sources.list.d/nodesource.list

deb https://deb.nodesource.com/node_16.x focal main

deb-src https://deb.nodesource.com/node_16.x focal main

sudo apt -y install nodejs

sudo apt -y install npm
