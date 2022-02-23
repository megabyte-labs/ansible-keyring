""" sh allows you to call any unix program as if it were a function """

from sh import ls, ifconfig, touch, rm

def examples():
    # ls -la
    print(ls("-la"))

    # ifconfig eth0
    print(ifconfig("eth0"))

    # touch foo.bar
    print(touch("./foo.bar"))

    # rm foo.bar
    print(rm("./foo.bar"))
