import os
from flask_apscheduler import APScheduler

from core.api import create_app
from core.api.container.logic import sample_services_config

app = create_app()
scheduler = APScheduler()


def run_application():
    """
    Runs the flask application with some custom configurations.
    """
    debug = os.environ.get("APP_DEBUG", True)  # False
    host = os.environ.get("APP_HOST", '0.0.0.0')  # 0.0.0.0
    port = int(os.environ.get('APP_PORT', 5000))

    app.run(debug=debug, host=host, port=port, use_reloader=False)


def schedule_operations(id, func, trigger='interval', seconds=15):
    """
    Schedule an operation to be performed every 'X' seconds.

    Args:
        id (str): name/ID of the task.
        func (Function): a function to occur every 'X' seconds.
        trigger (str): type of the trigger.
        seconds (int): each 'X' seconds that this function will occur.
    """
    scheduler.add_job(id=id, func=func, trigger=trigger, seconds=seconds)
    scheduler.start()


if __name__ == '__main__':
    schedule_operations(id='Sample Services Config', func=sample_services_config)
    run_application()
