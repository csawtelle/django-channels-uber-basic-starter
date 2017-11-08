#### Install prereqs

pip install django
pip install channels


wget http://download.redis.io/redis-stable.tar.gz

tar xvzf redis-stable.tar.gz

cd redis-stable

make

sudo cp src/redis-server /usr/local/bin/

#### start redis:
redi-server

#### start django
python3 manage.py runserver

#### start working
python3 manage.py poll

#### navigate to homepage and watch the ticker
