import flask

from stack_calculator.stack import Stack


api = flask.Blueprint('calc', __name__)


@api.route('/<int:id>/peek', methods=['GET'])
def peek(id):
    stack = Stack(flask.current_app.redis, id)
    return str(stack.peek())


@api.route('/<int:id>/push/<int:n>', methods=['GET'])
def push(id, n):
    stack = Stack(flask.current_app.redis, id)
    return str(stack.push(n))


@api.route('/<int:id>/pop', methods=['GET'])
def pop(id):
    stack = Stack(flask.current_app.redis, id)
    return str(stack.pop())


@api.route('/<int:id>/add', methods=['GET'])
def add(id):
    stack = Stack(flask.current_app.redis, id)
    return str(stack.add())


@api.route('/<int:id>/subtract', methods=['GET'])
def subtract(id):
    stack = Stack(flask.current_app.redis, id)
    return str(stack.subtract())


@api.route('/<int:id>/multiply', methods=['GET'])
def multiply(id):
    stack = Stack(flask.current_app.redis, id)
    return str(stack.multiply())


@api.route('/<int:id>/divide', methods=['GET'])
def divide(id):
    stack = Stack(flask.current_app.redis, id)
    return str(stack.divide())
