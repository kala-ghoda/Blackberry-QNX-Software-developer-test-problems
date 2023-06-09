from Test import Test
from LinkedList import Node, LinkedList

class LinkedListTest(Test):
    def evaluate(self, expected, actual):
        if expected is actual:
            print("PASS")
        elif expected == actual:
            print("PASS")
        else:
            print("FAIL")

    def init_test_node(self, val: int):
        """
        Test to check node init
        """
        return Node(val)

    def init_linked_list(self):
        """
        Test to check linked list init
        """
        return LinkedList()

    def node_test_attr(self, node: Node):
        expected_val = 4
        self.evaluate(expected_val, node.val)
        self.evaluate(None, node.next)
        self.evaluate(None, node.prev)

    def ll_test_attr(self, linked_list: LinkedList, vals: list):
        self.evaluate(None, linked_list.head)
        try:
            self.evaluate(None, linked_list.tail)
        except AttributeError:
            print("Expected error: PASS")
        
        linked_list.addNewNode(vals[0])
        self.evaluate(1, linked_list.tail)
        self.evaluate(1, linked_list.head.val)
        self.evaluate("1", str(linked_list))

        for val in vals[1:]:
            linked_list.addNewNode(val)

        self.evaluate(90, linked_list.tail)
        self.evaluate(1, linked_list.head.val)
        self.evaluate("90 50 20 1", str(linked_list))
        self.evaluate(20, linked_list.head.next.next.prev.val)

        linked_list.goNext()
        self.evaluate(20, linked_list.head.val)
        try:
            while True:
                linked_list.goNext()
        except ValueError:
            print("Expected ValueError. PASS")

        self.evaluate(linked_list.tail, linked_list.head.val)

        try:
            while True:
                linked_list.goBack()
        except ValueError:
            print("Expected ValueError. PASS")

        self.evaluate(1, linked_list.head.val)

    def test(self):
        node = self.init_test_node(4)
        ll = self.init_linked_list()
        if node is None or ll is None:
            print("FAIL")
        else:
            print("PASS")
        self.node_test_attr(node)
        self.ll_test_attr(ll, [1, 20, 50, 90])
