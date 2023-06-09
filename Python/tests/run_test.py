#!/usr/bin/python3

from WidgetTest import WidgetTest
from LinkedListTest import LinkedListTest
from ApplicationPaneTest import ApplicationPaneTest

if __name__ == "__main__":
    testobj = WidgetTest()
    testobj.test()

    testobj2 = LinkedListTest()
    testobj2.test()

    testobj3 = ApplicationPaneTest()
    testobj3.test()
