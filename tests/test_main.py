from src.main import print_field


def test_print_field():
    content = "f0\tf1\tf2\n0\t1\t2\n3\t4\t5\n"
    assert print_field(content, [1], "\t") == "f0\n0\n3"


def test_print_field_empty_input():
    content = ""
    assert print_field(content, [3], "") == ""


def test_print_field_with_delimiter():
    content = "10000 Reasons (Bless the Lord),20 Good Reasons,\nAdore You,Africa"
    assert print_field(content, [2], ",") == "20 Good Reasons\nAfrica"


def test_print_field_with_two_parameters():
    content = "f0\tf1\tf2\n0\t1\t2\n3\t4\t5\n"
    assert print_field(content, [1, 2], "\t") == "f0\tf1\n0\t1\n3\t4"


def test_print_field_number_out_of_range():
    content = "f0\tf1\tf2\n0\t1\t2\n3\t4\t5\n"
    assert print_field(content, [1, 10], "\t") == "f0\n0\n3"
