from stack import *

def test_push():
    print("test: push")
    colors = Stack()
    colors.push("Red")
    colors.push("Blue")

    print("Pass push test")

def test_pop():
    print("test: pop")
    colors = Stack()
    colors.push("Red")
    assert colors.pop() == "Red"
    assert colors.pop() == None
    colors.push("Red")
    colors.push("Blue")
    colors.push("Yellow")
    assert colors.pop() == "Yellow"
    assert colors.pop() == "Blue"
    assert colors.pop() == "Red"
    assert colors.pop() == None
    print("Pass pop test")

def test_first():
    print("test: top")
    colors = Stack()
    colors.push("Red")
    assert colors.first() == "Red"
    colors.push("Blue")
    assert colors.first() == "Blue"
    colors.pop()
    assert colors.first() == "Red"
    colors.pop()
    assert colors.first() == None
    print("Pass first test")

test_push()
test_pop()
test_first()
