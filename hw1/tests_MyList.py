from MyList import MyList
import re

# default constructor
def test_default_constructor():
    def_constructor = MyList()

# copy constructor
def test_copy_constructor():

# Test string constructor
def test_string_constructor():
    str_constructor = MyList("I am a string")
    assert str_constructor.size() == len("I am a string")


## Test char* constructor
#def test_char_constructor():

## destructor
#def test_destructor():

## push_front on empty
def test_push_front(capsys):
    test_pf = MyList("world")
    test_pf.push_front(' ')
    test_pf.push_front('o')
    test_pf.push_front('l')
    test_pf.push_front('l')
    test_pf.push_front('e')
    test_pf.push_front('h')

    test_pb.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "hello world"

# push_back on empty
def test_push_back(capsys):
    test_pb = MyList("hello")
    test_pb.push_back(' ')
    test_pb.push_back('w')
    test_pb.push_back('o')
    test_pb.push_back('r')
    test_pb.push_back('l')
    test_pb.push_back('d')

    test_pb.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "hello world"

## pop_front on empty
def test_pop_front(capsys):
    test_popf = MyList("popping")
    test_popf.pop_front()
    test_popf.pop_front()
    test_popf.pop_front()

    test_popf.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "ping"

# pop_back empty
def test_pop_back(capsys):
    test_popb = MyList("popping")
    test_popb.pop_front()
    test_popb.pop_front()
    test_popb.pop_front()

    test_popb.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "pop"

## swap valid i valid j
#def test_swap():

## insert at valid i
#def test_insert_at_pos():

# reverse
def test_reverse(capsys):
    test_rev = MyList("reverse")
    test_rev.revese()

    test_rev.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "esrever"

# size
def test_size():
    test_list_size = MyList("abcdefghij")
    assert test_list_size.size() == 10

# operator [  ]
#def test_brackets(capsys):

# print
def test_print(capsys):
    test_output = MyList("testoutput")
    test_output.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "testoutput"

