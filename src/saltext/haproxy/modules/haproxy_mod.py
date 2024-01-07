"""
Salt execution module
"""
import logging

log = logging.getLogger(__name__)

__virtualname__ = "haproxy"


def __virtual__():
    # To force a module not to load return something like:
    #   return (False, "The haproxy execution module is not implemented yet")
    return __virtualname__


def example_function(text):
    """
    This example function should be replaced

    CLI Example:

    .. code-block:: bash

        salt '*' haproxy.example_function text="foo bar"
    """
    return __salt__["test.echo"](text)
