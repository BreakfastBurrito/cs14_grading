from MyList import MyList

def test_print(capsys):
    test_output = MyList("testoutput")
    test_output.print_list()
    out = capsys.readout()
    only_chars = "".join(re.findall('([a-z]+|[A-Z]+)', out))
    assert only_chars == "testoutput"

