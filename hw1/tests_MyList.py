from MyList import MyList
import re

# default constructor
def test_default_constructor():
    def_constructor = MyList()
    assert def_constructor.size() == 0

# copy constructor
def test_copy_constructor_len():
    copy_from = MyList("original")
    copy_to = MyList(copy_from)
    assert len(copy_from) == 8 and len(copy_to) == 8

# copy constructor
def test_copy_constructor_diff():
    copy_from = MyList("original")
    copy_to = MyList(copy_from)
    copy_to.push_front('a')
    assert len(copy_from) == 9 and len(copy_to) == 8

# Test string constructor
def test_string_constructor():
    str_constructor = MyList("I am a string")
    assert str_constructor.size() == len("I am a string")

## Test char* constructor
#def test_char_constructor():

## destructor
#def test_destructor():

## push_front on empty
def test_push_front_nonempty(capfd):
    test_pf = MyList("world")
    for ch in "elloh":
        push_front(ch)

    test_pf.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "helloworld"

# push_front non empty
def test_push_front_empty(capfd):
    test_pf = MyList()
    for ch in "elloh":
        push_front(ch)

    test_pf.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "hello"

# push_back on empty
def test_push_back_nonempty(capfd):
    test_pb = MyList("hello")
    for ch in "world":
        test_pb.push_back(ch)

    test_pb.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "helloworld"

# push_back on empty
def test_push_back_empty(capfd):
    test_pb = MyList()
    for ch in "abc":
        test_pb.push_back(ch)

    test_pb.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "abc"

# pop_front on empty
def test_pop_front_empty(capfd):
    test_popf = MyList()
    test_popf.pop_front()
    assert only_chars == "ping"

# pop_front on empty
def test_pop_front_nonempty(capfd):
    test_popf = MyList("popping")
    for _ in xrange(3):
        test_popf.pop_front()

    test_popf.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "ping"

# pop_back empty
def test_pop_back_empty(capfd):
    test_popb = MyList()
    test_popb.pop_back()
    assert only_chars == "pop"

# pop_back empty
def test_pop_back_nonempty(capfd):
    test_popb = MyList("popping")
    for _ in xrange(4):
        test_popb.pop_back()

    test_popb.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "pop"

# swap valid i valid j
def test_swap_both_valid(capfd):
    swap_me = MyList("swap")
    swap_me.swap(1,2)

    test_rev.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "sawp"

# swap invalid i valid j
def test_swap_invalid_i(capfd):
    swap_me = MyList("swap")
    swap_me.swap(8,2)

    test_rev.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "swap"

# swap valid i invalid j
def test_swap_invalid_j(capfd):
    swap_me = MyList("swap")
    swap_me.swap(1,10)

    test_rev.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "swap"

# swap both invalid
def test_swap_both_invalid(capfd):
    swap_me = MyList("swap")
    swap_me.swap(-1,200)

    test_rev.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "swap"

# swap on empty list
def test_swap_on_empty(capfd):
    empty = MyList()
    empty(1, 2)

## insert at valid i
def test_insert_at_pos_valid(capfd):
    my_list = MyList("testing")
    my_list.insert_at_pos(2,'a')
    my_list.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "teasting"

# reverse nonempty
def test_reverse(capfd):
    test_rev = MyList("reverse")
    test_rev.revese()

    test_rev.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "esrever"

# reverse empty
def test_reverse(capfd):
    test_rev = MyList()
    test_rev.revese()

    test_rev.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == ""

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

