import pytest

from stack_calculator.stack import Stack, StackUnderflow


def test_peek_returns_top_stack():
    stack = Stack([0, 1])
    result = stack.peek()
    assert result == 1


def test_peek_raises_underflow():
    stack = Stack()
    with pytest.raises(StackUnderflow):
        stack.peek()


def test_peek_doesnt_mutate_stack():
    stack = Stack([1, 2])
    stack.peek()
    assert stack.data == [1, 2]


def test_pop_removes_top_item():
    stack = Stack([1, 2])
    stack.pop()
    assert stack.data == [1]


def test_pop_returns_top_item():
    stack = Stack([1, 2])
    result = stack.pop()
    assert result == 2


def test_pop_raises_underflow():
    stack = Stack()
    with pytest.raises(StackUnderflow):
        stack.pop()
        assert stack.data == []


def test_push_adds_top_item():
    stack = Stack([1])
    stack.push(2)
    assert stack.data == [1, 2]


def test_push_returns_top_item():
    stack = Stack()
    result = stack.push(1)
    assert result == 1


def test_add_replaces_top_2_items_with_sum():
    stack = Stack([1, 2])
    stack.add()
    assert stack.data == [3]


def test_add_returns_top_item():
    stack = Stack([1, 2])
    result = stack.add()
    assert result == 3


def test_add_raises_underflow():
    stack = Stack([1])
    with pytest.raises(StackUnderflow):
        stack.add()
        assert stack.data == [1]


def test_subtract_replaces_top_2_items_with_subtraction():
    stack = Stack([5, 1])
    stack.subtract()
    assert stack.data == [4]


def test_subtract_returns_top_item():
    stack = Stack([5, 1])
    result = stack.subtract()
    assert result == 4


def test_subtract_raises_underflow():
    stack = Stack([1])
    with pytest.raises(StackUnderflow):
        stack.subtract()
        assert stack.data == [1]


def test_multiply_replaces_top_2_items_with_multiplication():
    stack = Stack([5, 2])
    stack.multiply()
    assert stack.data == [10]


def test_multiply_returns_top_item():
    stack = Stack([5, 2])
    result = stack.multiply()
    assert result == 10


def test_multiply_raises_underflow():
    stack = Stack([1])
    with pytest.raises(StackUnderflow):
        stack.multiply()
        assert stack.data == [1]


def test_divide_replaces_top_2_items_with_division():
    stack = Stack([10, 2])
    stack.divide()
    assert stack.data == [5]


def test_divide_returns_top_item():
    stack = Stack([10, 2])
    result = stack.divide()
    assert result == 5


def test_divide_raises_underflow():
    stack = Stack([1])
    with pytest.raises(StackUnderflow):
        stack.divide()
        assert stack.data == [1]


def test_divide_raises_zero_division():
    stack = Stack([10, 0])
    with pytest.raises(ZeroDivisionError):
        stack.divide()
        assert stack.data == [10, 0]
