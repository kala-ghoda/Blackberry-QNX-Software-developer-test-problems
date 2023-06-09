from Test import Test
from ApplicationPane import ApplicationPane
from Widget import Widget, Category
from time import sleep

class ApplicationPaneTest(Test):
    def evaluate(self, expected, actual):
        if expected is actual:
            print("PASS")
        elif expected == actual:
            print("PASS")
        else:
            print("FAIL")

    def init_test_applpane(self, widget_list: list):
        """
        Test to check application pane init
        """
        return ApplicationPane(widget_list)

    def applpane_attr_test(self, app_pane):
        expectd_str = "facebook: SOCIAL\n\nyoutube: ENTERTAINMENT\n\ninshorts: INFO\n\n\n"
        self.evaluate(expectd_str, str(app_pane))

    def test_open_widget(self, app_pane, widget_name):
        app_pane.open_widget(widget_name)
        app_pane.names[widget_name].show_usage_time()

    def test(self):
        widget_list = [Widget("facebook", Category.SOCIAL),
                       Widget("youtube", Category.ENTERTAINMENT),
                       Widget("inshorts", Category.INFO)]
        app_pane = self.init_test_applpane(widget_list)
        if app_pane is not None:
            print("PASS")
        else:
            print("FAIL")

        self.applpane_attr_test(app_pane)
        self.test_open_widget(app_pane, "youtube")
        sleep(4)
        self.test_open_widget(app_pane, "inshorts")
        sleep(4)
        self.test_open_widget(app_pane, "youtube")
        sleep(4)
        self.test_open_widget(app_pane, "youtube")
