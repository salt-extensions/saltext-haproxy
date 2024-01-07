import pytest

pytestmark = [
    pytest.mark.requires_salt_states("haproxy.exampled"),
]


@pytest.fixture
def haproxy(states):
    return states.haproxy


def test_replace_this_this_with_something_meaningful(haproxy):
    echo_str = "Echoed!"
    ret = haproxy.exampled(echo_str)
    assert ret.result
    assert not ret.changes
    assert echo_str in ret.comment
