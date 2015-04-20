from MyList import MyList
import re

# default constructor
def test_default_constructor():

# copy constructor
def test_copy_constructor():

# Test string constructor
def test_string_constructor():

# Test char* constructor
def test_char_constructor():

# destructor
def test_destructor():

# push_front on empty
def test_push_front_empty():

# push_front on nonempty
def test_push_front_nonempty():

# push_back on empty
def test_push_back_empty():

# push_back on empty
def test_push_back_nonempty():

# pop_front on empty
def test_pop_front_empty():

# pop_front on empty
def test_pop_front_nonempty():

# pop_back empty
def test_pop_back_empty():

# pop_back empty
def test_pop_back_empty():

# print
def test_print(capsys):
    test_output = MyList("testoutput")
    test_output.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "testoutput"

