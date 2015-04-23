from MyList import MyList, get_MyList
import re

# default constructor
def test_default_constructor():
    def_constructor = get_MyList(MyList())
    assert len(def_constructor) == 0

# copy constructor
def test_copy_constructor_len():
    copy_from = MyList("original")
    copy_to = get_MyList(MyList(copy_from))
    copy_from = get_MyList(copy_from)
    assert len(copy_from) == 8 and len(copy_to) == 8

# copy constructor
def test_copy_constructor_diff():
    copy_from = MyList("original")
    copy_to = MyList(copy_from)
    copy_to.push_front('a')
    copy_to = get_MyList(copy_to)
    copy_from = get_MyList(copy_from)
    assert len(copy_from) == 8 and len(copy_to) == 9

# Test string constructor
def test_string_constructor():
    str_constructor = MyList("Iamastring")
    assert get_MyList(str_constructor) == "Iamastring"

## destructor
#def test_destructor():

## push_front on empty
def test_push_front_nonempty():
    test_pf = MyList("world")
    for ch in "olleh":
        test_pf.push_front(ch)
    assert get_MyList(test_pf) == "helloworld"

# push_front empty
def test_push_front_empty():
    test_pf = MyList()
    for ch in "olleh":
        test_pf.push_front(ch)
    assert get_MyList(test_pf) == "hello"

# push_back on nonempty
def test_push_back_nonempty():
    test_pb = MyList("hello")
    for ch in "world":
        test_pb.push_back(ch)
    assert get_MyList(test_pb) == "helloworld"

# push_back on empty
def test_push_back_empty():
    test_pb = MyList()
    for ch in "abc":
        test_pb.push_back(ch)
    assert get_MyList(test_pb) == "abc"

# pop_front on empty
def test_pop_front_empty():
    test_popf = MyList()
    test_popf.pop_front()
    assert get_MyList(test_popf) == ""

# pop_front on empty
def test_pop_front_nonempty():
    test_popf = MyList("popping")
    for _ in xrange(3):
        test_popf.pop_front()
    assert get_MyList(test_popf) == "ping"

# pop_back empty
def test_pop_back_empty():
    test_popb = MyList()
    test_popb.pop_back()
    assert get_MyList(test_popb) == ""

# pop_back empty
def test_pop_back_nonempty():
    test_popb = MyList("popping")
    for _ in xrange(4):
        test_popb.pop_back()
    assert get_MyList(test_popb) == "pop"

# swap valid i valid j
def test_swap_both_valid():
    swap_me = MyList("swap")
    swap_me.swap(1,2)
    assert get_MyList(swap_me) == "sawp"

# swap invalid i valid j
def test_swap_invalid_i():
    swap_me = MyList("swap")
    swap_me.swap(8,2)
    assert get_MyList(swap_me) == "swap"

# swap valid i invalid j
def test_swap_invalid_j():
    swap_me = MyList("swap")
    swap_me.swap(1,10)
    assert get_MyList(swap_me) == "swap"

# swap both invalid
def test_swap_both_invalid():
    swap_me = MyList("swap")
    swap_me.swap(-1,200)
    assert get_MyList(swap_me) == "swap"


# swap on empty list
def test_swap_on_empty():
    empty = MyList()
    empty.swap(1, 2)
    assert get_MyList(empty) == ""

## insert at valid i
def test_insert_at_pos_valid():
    my_list = MyList("testing")
    my_list.insert_at_pos(2,'a')
    assert get_MyList(my_list) == "teasting"

# reverse nonempty
def test_reverse_nonempty():
    test_rev = MyList("reverse")
    test_rev.reverse()
    assert get_MyList(test_rev) == "esrever"

# reverse empty
def test_reverse_empty():
    test_rev = MyList()
    test_rev.reverse()
    assert get_MyList(test_rev) == ""

# size
def test_size():
    test_list = get_MyList(MyList("abcdefghij"))
    assert len(test_list) == 10

def test_find_valid_char():
    test_string = MyList("teststring")
    assert test_string.find_MyList("r") == 6

def test_find_invalid_char():
    test_string = MyList("teststring")
    assert test_string.find_MyList("z") == -1

def test_find_empty_list():
    test_string = MyList()
    assert test_string.find_MyList("r") == -1


def test_find_valid_MyList():
    test_string = MyList("teststring")
    assert test_string.find_MyList(MyList("rin")) == 6 

def test_find_invalid_MyList():
    test_string = MyList("teststring")
    assert test_string.find_MyList(MyList("zoo")) == -1

def test_find_empty_list_MyList():
    test_string = MyList()
    assert test_string.find_MyList(MyList("test")) == -1

def test_equals_operator_empty():
    test_string = MyList()
    test_string.reassign(MyList("newstring"))
    test_string = get_MyList(test_string)
    assert test_string == "newstring"


def test_equals_operator_nonempty():
    test_string = MyList("test")
    test_string.reassign(MyList("newstring"))
    test_string = get_MyList(test_string)
    assert test_string == "newstring"


def test_equals_operator_nonempty_mem_check():
    test_string = MyList("test")
    test_str2   = MyList("newstring")
    test_string.reassign(test_str2)
    test_str2.pop_back()
    assert get_MyList(test_string) != get_MyList(test_str2)

def test_addition_operator_a_empty_b_empty():
    test_str  = MyList()
    test_str2 = MyList()
    test_str3 = test_str + test_str2
    assert get_MyList(test_str3) == ""

def test_addition_operator_a_empty_b_nonempty():
    test_str  = MyList()
    test_str2 = MyList("123")
    test_str3 = test_str + test_str2
    assert get_MyList(test_str3) == "123"

def test_addition_operator_a_nonempty_b_nonempty():
    test_str  = MyList("abc")
    test_str2 = MyList("def")
    test_str3 = test_str + test_str2
    assert get_MyList(test_str3) == "abcdef"

def test_addition_operator_a_nonempty_b_empty():
    test_str  = MyList("123")
    test_str2 = MyList()
    test_str3 = test_str + test_str2
    assert get_MyList(test_str3) == "123"


def test_addition_operator_mem_check():
    test_str  = MyList("abc")
    test_str2 = MyList("def")
    test_str3 = test_str + test_str2
    test_str2.pop_back()

    assert get_MyList(test_str3) == "abcdef"

# print
def test_print(capfd):
    test_output = MyList("testoutput")
    test_output.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "testoutput"

