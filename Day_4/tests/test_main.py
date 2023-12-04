from Day_4.main import execute


def test_example():
    assert execute("test_input.txt") == (13, 30)


def test_main():
    assert execute("input.txt") == (23941, 5571760)
