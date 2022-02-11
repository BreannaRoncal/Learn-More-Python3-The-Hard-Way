from dllist import *

def test_push():
    print("test: push")
    colors = DoubleLinkedList()
    assert colors.count() == 0
    colors.push("Blue")
    colors._invariant()
    assert colors.count() == 1
    colors.push("Ultramarine")
    colors.count() == 2
    colors._invariant()
    print("Pass push test")

def test_pop():
    print("test: pop")
    colors = DoubleLinkedList()
    assert colors.pop() == None
    colors.push("Magenta")
    colors._invariant()
    colors.push("Alizarin") 
    colors.push("Van Dyke")
    colors._invariant()
    assert colors.pop() == "Van Dyke"
    colors._invariant()
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    colors._invariant()
    assert colors.pop() == None
    print("Pass pop test")

def test_remove():
    print("test: remove")
    colors = DoubleLinkedList()
    colors.push("Cobalt")
    colors.push("White")
    colors.push("Yellow")
    colors.push("Perinone")
    assert colors.remove("Cobalt") == 0
    colors._invariant()
    assert colors.remove("Perinone") == 2
    colors._invariant()
    assert colors.remove("Yellow") == 1
    colors._invariant()
    assert colors.remove("White") == 0
    colors._invariant()
    print("Pass remove test")


def test_get():
    print("test: get")
    colors = DoubleLinkedList()
    colors.push("Vermillion")
    assert colors.get(0) == "Vermillion"
    colors.push("Green")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Green"
    colors.push("Yellow")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Green"
    assert colors.get(2) == "Yellow"
    assert colors.pop() == "Yellow"
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Green"
    assert colors.get(2) == None
    colors.pop()
    assert colors.get(0) == "Vermillion"
    colors.pop()
    assert colors.get(0) == None
    print("Pass get test")


def test_first():
    print("test: first")
    colors = DoubleLinkedList()
    colors.push("Red")
    assert colors.first() == "Red"
    colors.push("Yellow")
    assert colors.first() == "Red"
    colors.remove("Red")
    assert colors.first() == "Yellow"
    print("Pass first test")

def test_last():
    print("test: last")
    colors = DoubleLinkedList()
    colors.push("Red")
    assert colors.last() == "Red"
    colors.push("Yellow")
    assert colors.last() == "Yellow"
    colors.pop()
    assert colors.last() == "Red"
    colors.pop()
    assert colors.last() == None
    print("Pass last test")

test_push()
test_pop()
test_remove()
test_get()
test_first()
test_last()
