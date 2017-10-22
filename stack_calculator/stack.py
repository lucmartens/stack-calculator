from functools import wraps


def check_errors(fn):
    """Decorator that translates lua error strings to python errors."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if result == b"stack-underflow":
            raise StackUnderflow()
        if result == b"divide-by-zero":
            raise ZeroDivisionError()
        return result
    return wrapper


class Stack(object):
    def __init__(self, redis_store, stack_id):
        self.redis_store = redis_store
        self.stack_id = stack_id

    @check_errors
    def push(self, n):
        push = self.redis_store.register_script(lua_push)
        return push(keys=[self.stack_id], args=[n])

    @check_errors
    def pop(self):
        pop = self.redis_store.register_script(lua_pop)
        return pop(keys=[self.stack_id])

    @check_errors
    def peek(self):
        peek = self.redis_store.register_script(lua_peek)
        return peek(keys=[self.stack_id])

    @check_errors
    def add(self):
        add = self.redis_store.register_script(lua_add)
        return add(keys=[self.stack_id])

    @check_errors
    def subtract(self):
        subtract = self.redis_store.register_script(lua_subtract)
        return subtract(keys=[self.stack_id])

    @check_errors
    def multiply(self):
        multiply = self.redis_store.register_script(lua_multiply)
        return multiply(keys=[self.stack_id])

    @check_errors
    def divide(self):
        divide = self.redis_store.register_script(lua_divide)
        return divide(keys=[self.stack_id])


class StackUnderflow(Exception):
    pass


lua_push = """
    local n = tonumber(ARGV[1])
    redis.call("LPUSH", KEYS[1], n)
    return n
"""


lua_pop = """
    if redis.call("LLEN", KEYS[1]) < 1 then
        return "stack-underflow"
    end

    local n = redis.call("LPOP", KEYS[1])
    return tonumber(n)
"""

lua_peek = """
    if redis.call("LLEN", KEYS[1]) < 1 then
        return "stack-underflow"
    end

    local n = redis.call("LINDEX", KEYS[1], 0)
    return tonumber(n)
"""


lua_add = """
    if redis.call("LLEN", KEYS[1]) < 2 then
        return "stack-underflow"
    end

    local n1 = redis.call("LPOP", KEYS[1])
    local n2 = redis.call("LPOP", KEYS[1])
    local n = n2 + n1

    redis.call("LPUSH", KEYS[1], n)
    return n
"""


lua_subtract = """
    if redis.call("LLEN", KEYS[1]) < 2 then
        return "stack-underflow"
    end

    local n1 = redis.call("LPOP", KEYS[1])
    local n2 = redis.call("LPOP", KEYS[1])
    local n = n2 - n1

    redis.call("LPUSH", KEYS[1], n)
    return n
"""


lua_multiply = """
    if redis.call("LLEN", KEYS[1]) < 2 then
        return "stack-underflow"
    end

    local n1 = redis.call("LPOP", KEYS[1])
    local n2 = redis.call("LPOP", KEYS[1])
    local n = n2 * n1

    redis.call("LPUSH", KEYS[1], n)
    return n
"""


lua_divide = """
    if redis.call("LLEN", KEYS[1]) < 2 then
        return "stack-underflow"
    end

    if redis.call("LINDEX", KEYS[1], 0) == "0" then
        return "divide-by-zero"
    end

    local n1 = redis.call("LPOP", KEYS[1])
    local n2 = redis.call("LPOP", KEYS[1])
    local n = n2 / n1

    redis.call("LPUSH", KEYS[1], n)
    return n
"""
