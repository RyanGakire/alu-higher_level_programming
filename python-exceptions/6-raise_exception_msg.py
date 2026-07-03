#!/usr/bin/python3
def raise_exception_msg(message=""):
    """Raise a NameError exception with a message.

    Args:
        message (str): the message to attach to the exception.

    Raises:
        NameError: always raised, with the given message.
    """
    raise NameError(message)
