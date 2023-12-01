from day1.main import execute


def test_main():
    assert execute("test_input.txt") == 142


def test_part_2():
    assert execute("test_2_input.txt") == 281
