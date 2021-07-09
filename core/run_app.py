import os


from core.api import create_app

app = create_app()


def run_application():
    debug = os.environ.get("APP_DEBUG", True)  # False
    host = os.environ.get("APP_HOST", '0.0.0.0')  # 0.0.0.0
    port = int(os.environ.get('APP_PORT', 5000))

    app.run(debug=debug, host=host, port=port)


if __name__ == '__main__':
    run_application()