from {{ cookiecutter.project_slug }}.main import execute


def test_example():
    assert execute("test_input.txt")

def test_main():
    assert execute("input.txt")
