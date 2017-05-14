import flask

from stack_calculator.stack import Stack


api = flask.Blueprint('calc', __name__)


def fetch_stack(id):
    redis = flask.current_app.redis
    data = redis.fetch_stack(id) or []
    return Stack(data)


def persist_stack(id, stack):
    redis = flask.current_app.redis
    return redis.persist_stack(id, stack.data)


@api.route('/<int:id>/peek', methods=['GET'])
def peek(id):
    stack = fetch_stack(id)
    return str(stack.peek())


@api.route('/<int:id>/push/<int:n>', methods=['GET'])
def push(id, n):
    stack = fetch_stack(id)
    result = str(stack.push(n))
    persist_stack(id, stack)
    return result


@api.route('/<int:id>/pop', methods=['GET'])
def pop(id):
    stack = fetch_stack(id)
    result = str(stack.pop())
    persist_stack(id, stack)
    return result


@api.route('/<int:id>/add', methods=['GET'])
def add(id):
    stack = fetch_stack(id)
    result = str(stack.add())
    persist_stack(id, stack)
    return result


@api.route('/<int:id>/subtract', methods=['GET'])
def subtract(id):
    stack = fetch_stack(id)
    result = str(stack.subtract())
    persist_stack(id, stack)
    return result


@api.route('/<int:id>/multiply', methods=['GET'])
def multiply(id):
    stack = fetch_stack(id)
    result = str(stack.multiply())
    persist_stack(id, stack)
    return result


@api.route('/<int:id>/divide', methods=['GET'])
def divide(id):
    stack = fetch_stack(id)
    result = str(stack.push())
    persist_stack(id, stack)
    return result
