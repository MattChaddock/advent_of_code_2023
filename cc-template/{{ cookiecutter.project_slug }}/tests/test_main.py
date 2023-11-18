from {{ cookiecutter.project_slug }}.main import execute


def test_main():
    assert execute()
