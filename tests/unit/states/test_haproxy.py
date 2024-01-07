import pytest
import salt.modules.test as testmod
import saltext.haproxy.modules.haproxy_mod as haproxy_module
import saltext.haproxy.states.haproxy_mod as haproxy_state


@pytest.fixture
def configure_loader_modules():
    return {
        haproxy_module: {
            "__salt__": {
                "test.echo": testmod.echo,
            },
        },
        haproxy_state: {
            "__salt__": {
                "haproxy.example_function": haproxy_module.example_function,
            },
        },
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    expected = {
        "name": echo_str,
        "changes": {},
        "result": True,
        "comment": f"The 'haproxy.example_function' returned: '{echo_str}'",
    }
    assert haproxy_state.exampled(echo_str) == expected
