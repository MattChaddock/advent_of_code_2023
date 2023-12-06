from Day_6.main import execute


def test_example():
    assert execute("test_input.txt") == (288, 71503)


def test_main():
    assert execute("input.txt") == (741000, 38220708)
