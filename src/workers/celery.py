""" Distributed Task Queue for Python """

from celery import Celery


app = Celery("python_cli_example", broker="http://localhost:6379/0")


@app.task
def example():
    """
    This is a task. Ideally, you would call this function from somewhere else in
    your code and it will run in the background:

    from {{Name}}.workers.celery import example
    example.delay()

    Returns:
        str: output
    """
    return "Hello, world!"


if __name__ == "__main__":
    app.start()
