import pytest

from stack_calculator.stack import Stack, StackUnderflow


def test_push_adds_item_to_top(redis):
    stack = Stack(redis, 1)
    stack.push(5)
    stack.push(6)
    assert redis.lpop(1) == b'6'


def test_push_returns_item(redis):
    stack = Stack(redis, 1)
    assert stack.push(5) == 5


def test_peek_returns_top_item(redis):
    stack = Stack(redis, 1)
    stack.push(5)
    stack.push(6)
    assert stack.peek() == 6


def test_peek_raises_underflow(redis):
    stack = Stack(redis, 1)
    with pytest.raises(StackUnderflow):
        stack.peek()


def test_pop_removes_top_item(redis):
    stack = Stack(redis, 1)
    stack.push(5)
    stack.push(6)
    stack.pop()
    assert stack.peek() == 5


def test_pop_returns_top_item(redis):
    stack = Stack(redis, 1)
    stack.push(5)
    stack.push(6)
    assert stack.pop() == 6


def test_pop_raises_underflow(redis):
    stack = Stack(redis, 1)
    with pytest.raises(StackUnderflow):
        stack.pop()


def test_add_replaces_top_2_items_with_sum(redis):
    stack = Stack(redis, 1)
    stack.push(5)
    stack.push(6)
    stack.add()
    assert redis.llen(1) == 1
    assert stack.peek() == 11


def test_add_returns_result(redis):
    stack = Stack(redis, 1)
    stack.push(5)
    stack.push(6)
    assert stack.add() == 11


def test_add_raises_underflow(redis):
    stack = Stack(redis, 1)
    with pytest.raises(StackUnderflow):
        stack.add()


def test_subtract_replaces_top_2_items_with_subtraction(redis):
    stack = Stack(redis, 1)
    stack.push(5)
    stack.push(6)
    stack.subtract()
    assert redis.llen(1) == 1
    assert stack.peek() == -1


def test_subtract_returns_result(redis):
    stack = Stack(redis, 1)
    stack.push(5)
    stack.push(6)
    assert stack.subtract() == -1


def test_subtract_raises_underflow(redis):
    stack = Stack(redis, 1)
    with pytest.raises(StackUnderflow):
        stack.subtract()


def test_multiply_replaces_top_2_items_with_multiplication(redis):
    stack = Stack(redis, 1)
    stack.push(5)
    stack.push(6)
    stack.multiply()
    assert redis.llen(1) == 1
    assert stack.peek() == 30


def test_multiply_returns_result(redis):
    stack = Stack(redis, 1)
    stack.push(5)
    stack.push(6)
    assert stack.multiply() == 30


def test_multiply_raises_underflow(redis):
    stack = Stack(redis, 1)
    with pytest.raises(StackUnderflow):
        stack.multiply()


def test_divide_replaces_top_2_items_with_division(redis):
    stack = Stack(redis, 1)
    stack.push(10)
    stack.push(2)
    stack.divide()
    assert redis.llen(1) == 1
    assert stack.peek() == 5


def test_divide_returns_result(redis):
    stack = Stack(redis, 1)
    stack.push(10)
    stack.push(2)
    assert stack.divide() == 5


def test_divide_raises_underflow(redis):
    stack = Stack(redis, 1)
    with pytest.raises(StackUnderflow):
        stack.divide()


def test_divide_raises_zero_division(redis):
    stack = Stack(redis, 1)
    stack.push(10)
    stack.push(0)
    with pytest.raises(ZeroDivisionError):
        stack.divide()
