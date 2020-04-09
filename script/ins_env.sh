#!/bin/bash

[ $(id -u) != "0" ] && { echo "Error: You must be root to run this script"; exit 1; }

apt remove python -y
apt-get install -y git
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev git zip unzip
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

sed '/export PATH="\/root\/.pyenv\/bin:\$PATH"/d' -i ~/.bashrc
sed '/eval "\$(pyenv init -)"/d'  -i ~/.bashrc
sed '/eval "\$(pyenv virtualenv-init -)"/d'  -i ~/.bashrc

cat >> ~/.bashrc << EOF
export PATH="/root/.pyenv/bin:\$PATH"
eval "\$(pyenv init -)"
eval "\$(pyenv virtualenv-init -)"
EOF
source ~/.bashrc
pyenv install 3.7.1
pyenv global 3.7.1
wget -c https://github.com/rc452860/shadowsocksr/archive/master.zip
unzip master.zip
wget ssrpanel.test/api/node/config -O shadowsocksr-master/usermysql.json
pip install -r shadowsocksr-master/requestment.txt
python shadowsocksr-master/server.py
