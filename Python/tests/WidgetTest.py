from Test import Test
from Widget import Widget, Category

class WidgetTest(Test):
    def evaluate(self, expected, actual):
        if expected is actual:
            print("PASS")
        elif expected == actual:
            print("PASS")
        else:
            print(str(expected), str(actual))
            print(hex(id(expected)), hex(id(actual)))
            print("FAIL")

    def init_test(self, name: str, category: Category):
        """
        Test to check widget init
        """
        return Widget(name, category)

    def test_attr(self, widget: Widget):
        expected_str1 = "facebook: SOCIAL"
        expected_str2 = "facebook"
        expected_str3 = "SOCIAL"
        expected_val = 3

        self.evaluate(expected_str1, str(widget))
        self.evaluate(expected_str2, widget.name)
        self.evaluate(expected_str3, widget.category)
        self.evaluate(expected_val, widget.category_value)

    def test_open_func(self, widget):
        widget.open()
        widget.show_usage_time()

    def test(self):
        widget = self.init_test("Facebook", Category.SOCIAL)
        if widget is not None:
            print("PASS")
        else:
            print("FAIL")
        self.test_attr(widget)
        self.test_open_func(widget)
