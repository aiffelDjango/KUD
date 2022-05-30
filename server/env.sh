sudo apt -y update

sudo apt -y upgrade

sudo apt install -y build-essential

sudo apt install python3-pip

sudo apt install cmake

sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev

git clone https://github.com/pyenv/pyenv.git ~/.pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashprofile

echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashprofile

echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashprofile

bash ~/.bashprofile

pyenv install 3.8.7

pyenv global 3.8.7

curl -sL https://deb.nodesource.com/setup_16.x | sudo bash -

cat /etc/apt/sources.list.d/nodesource.list

deb https://deb.nodesource.com/node_16.x focal main

deb-src https://deb.nodesource.com/node_16.x focal main

sudo apt -y install nodejs

sudo apt -y install npm
