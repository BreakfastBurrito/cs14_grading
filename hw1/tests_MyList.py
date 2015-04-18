from MyList import MyList
import re

def test_print(capfd):
    test_output = MyList("testoutput")
    test_output.print_list()
    out, err = capfd.readouterr()
    only_chars = "".join(re.findall('([a-z])', out))
    assert only_chars == "testoutput"

