# ContainerApi

Docker version 20.10.7, build f0df350

docker-compose version 1.29.2

Installation guide:

1) clone this repo
2) build a python virtual enviroment
3) activate virtual enviroment using 'source venv/bin/activate'
4) pip install -r requirements.txt
5) make sure when running it that the intrepeter is pointed correctly and you have all of the dependencies installed.
6) the file that should be run is core/run_app.py - if you try to use 'python run_app.py' - you will get module not found error because of some relative import issue.
so the best way is to run it through the pycharm with a correct interperter that points out to the virtual enviroment interpreter that you created.
7) the functions are pretty documented so if there is something you don't understand let me know
8) there is a configuration file that is based on docker-compose. its important to keep it in its path and not to change it. feel free to change the file it self but not the its path. 
9) feel free to ask me any question.
