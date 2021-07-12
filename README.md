# ContainerApi

Docker version 20.10.7, build f0df350

docker-compose version 1.29.2

Installation guide:

1) clone this repo
2) install docker on the machine that this server will be running on.
3) build a python virtual enviroment
4) activate virtual enviroment using 'source venv/bin/activate'
5) pip install -r requirements.txt
6) make sure when running it that the intrepeter is pointed correctly and you have all of the dependencies installed.
7) the file that should be run is core/run_app.py - if you try to use 'python run_app.py' - you will get module not found error because of some relative import issue.
so the best way is to run it through the pycharm with a correct interperter that points out to the virtual enviroment interpreter that you created.
7) the functions are pretty documented so if there is something you don't understand let me know
8) there is a configuration file that is based on docker-compose. its important to keep it in its path and not to change it. feel free to change the file it self but not the its path. 
9) feel free to ask me any question.


Note:

if you will change the docker-compose file, the server should recognize it and run/remove/update containers with whatever configurations docker-compose allow you.
so if for example i have this docker compose file:

version: "3.9"
services:
  nginx1:
    image: nginx
    ports:
      - "50001:50001"
  nginx2:
    image: nginx
    ports:
      - "50001:50001"
      

and i decide to remove one of the nginx services then we should expect seeing only one container in 'docker ps' output instead of two.

version: "3.9"
services:
  nginx1:
    image: nginx
    ports:
      - "50001:50001"
