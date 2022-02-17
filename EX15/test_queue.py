from queue import *

def test_push():
    print("test: push")
    colors = Queue()
    assert colors.count() == 0
    colors.push("Yellow")
    assert colors.count() == 1
    colors.push("Blue")
    assert colors.count() == 2
    colors.push("Red")
    assert colors.count() == 3
    print("Pass push test")

def test_pop():
    print("test: pop")
    colors = Queue()
    assert colors.pop() == None
    colors.push("Purple")
    colors.push("Green")
    colors.push("Gray")
    assert colors.pop() == "Purple"
    assert colors.pop() == "Green"
    assert colors.pop() == "Gray"
    assert colors.pop() == None
    print("Pass pop test")

test_push()
test_pop()
