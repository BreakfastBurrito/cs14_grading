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

def test_find_valid_char():
    test_string = MyList("test string")
    assert test_string.find_MyList("r") == 7

def test_find_invalid_char():
    test_string = MyList("test string")
    assert test_string.find_MyList("r") == -1

def test_find_empty_list():
    test_string = MyList()
    assert test_string.find_MyList("r") == -1


def test_find_valid_MyList():
    test_string = MyList("test string")
    assert test_string.find_MyList(MyList("rin")) == 7

def test_find_invalid_MyList():
    test_string = MyList("test string")
    assert test_string.find_MyList(MyList("zoo")) == -1

def test_find_empty_list_MyList():
    test_string = MyList()
    assert test_string.find_MyList(MyList("test")) == -1

def test_equals_operator_empty(capfd):
    test_string = MyList()
    test_string.reassign(MyList("new string"))
    test_string.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "newstring"


def test_equals_operator_nonempty(capfd):
    test_string = MyList("test")
    test_string.reassign(MyList("new string"))
    test_string.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "newstring"


def test_equals_operator_nonempty_mem_check(capfd):
    test_string = MyList("test")
    test_str2   = MyList("new string")
    test_string.reassign(test_str2)
    test_str2.pop_back()
    test_string.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "newstring"

def test_addition_operator_a_empty_b_empty():
    test_str  = MyList()
    test_str2 = MyList()
    test_str3 = test_str + test_str2
    assert test_str.size() == 0

def test_addition_operator_a_empty_b_nonempty():
    test_str  = MyList()
    test_str2 = MyList("123")
    test_str3 = test_str + test_str2
    assert test_str.size() == 3

def test_addition_operator_a_nonempty_b_nonempty(capfd):
    test_str  = MyList("abc")
    test_str2 = MyList("def")
    test_str3 = test_str + test_str2
    test_str3.print_list()

    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))

    assert only_chars == "abcdef"

def test_addition_operator_a_nonempty_b_empty():
    test_str  = MyList("123")
    test_str2 = MyList()
    test_str3 = test_str + test_str2
    assert test_str.size() == 3

def test_addition_operator_mem_check():
    test_str  = MyList("abc")
    test_str2 = MyList("def")
    test_str3 = test_str + test_str2

    test_str2.pop_back()

    test_str3.print_list()

    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))

    assert only_chars == "abcdef"


# print
def test_print(capfd):
    test_output = MyList("testoutput")
    test_output.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "testoutput"

