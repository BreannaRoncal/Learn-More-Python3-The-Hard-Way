"""
Automated testing for sllist.py
"""

from turtle import color
from sllist import *


def test_push():
    print("test: push")
    colors = SingleLinkedList()
    colors.push("Blue")
    assert colors.count() == 1
    colors.push("Red")
    assert colors.count() == 2
    print("pass push test")


def test_pop():
    print("test: pop")
    colors = SingleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None
    print("Pass pop test")


def test_remove():
    print("test: remove")
    colors = SingleLinkedList()
    colors.push("Cobalt")
    colors.push("White")
    colors.push("Yellow")
    colors.push("Red")
    colors.remove("Cobalt")
    colors.remove("White")
    colors.remove("Red")
    colors.remove("Yellow")
    colors.print_list()
    print("Pass remove test")


def test_first():
    print("test: first")
    colors = SingleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.first() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.first() == "Cadmium Red Light"
    colors.push("Pthalo Green")
    assert colors.first() == "Cadmium Red Light"
    print("Pass first test")

def test_last():
    print("test: last")
    colors = SingleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.last() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.last() == "Hansa Yellow"
    colors.push("Pthalo Green")
    assert colors.last() == "Pthalo Green" 
    print("Pass last test")


def test_get():
    print("test: get")
    colors = SingleLinkedList()
    colors.push("Vermillion")
    assert colors.get(0) == "Vermillion"
    colors.push("Sap Green")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    colors.push("Cadmium Yellow Light")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == "Cadmium Yellow Light"
    assert colors.pop() == "Cadmium Yellow Light"
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == None
    colors.pop()
    assert colors.get(0) == "Vermillion"
    colors.pop()
    assert colors.get(0) == None
    print("Pass get test")

test_push()
test_pop()
test_remove()
test_first()
test_last()
test_get()

