import pytest

pytestmark = [
    pytest.mark.requires_salt_modules("haproxy.example_function"),
]


@pytest.fixture
def haproxy(modules):
    return modules.haproxy


def test_replace_this_this_with_something_meaningful(haproxy):
    echo_str = "Echoed!"
    res = haproxy.example_function(echo_str)
    assert res == echo_str
