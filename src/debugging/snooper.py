"""
PySnooper is a python debugging tool that needs little to no setup.

Just add the @pysnooper.snoop() decorator to any function or method you'd like
to debug.
"""
import pysnooper


@pysnooper.snoop()
def backwards_hello_world():
    """
    Should return "!dlrow ,olleh" but instead returns "world! hello,".

    Returns:
        str: backwards "hello, world!" string
    """
    hello_world = "hello, world!"

    result = []
    for c in hello_world.split(" "):
        result.append(c)

    return result.join(" ")


backwards_hello_world()
