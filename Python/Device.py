from LinkedList import LinkedList
from ApplicationPane import ApplicationPane

class Device:
    def __init__(self, id_: int, widget_matrix: list):
        self.device_id = id_
        self.app_panes = LinkedList()
        self.__create_app_panes(widget_matrix)

    def __create_app_panes(self, widget_matrix: list):
        for widgets in widget_matrix:
            self.app_panes.addNewNode(ApplicationPane(widgets))

    def __str__(self):
        try:
            while True:
                self.app_panes.goBack()
        except ValueError:
            pass

        print("Device: {}\n\n".format(self.device_id))
        out_str, counter = "", 0
        try:
            while True:
                out_str += "Application pane {}:\n".format(counter)
                counter += 1
                out_str += str(self.app_panes.head.val) + "\n\n"
                self.app_panes.goNext()
        except ValueError:
            out_str += "Done\n\n" 
        return out_str

    def open_app_widget(self, widget_name: str):
        if self.app_panes.head.next is None:
            try:
                while True:
                    widget = self.app_panes.head.val.names.get(widget_name, None)
                    if widget is None:
                        self.app_panes.goBack()
                    else:
                        self.app_panes.head.val.open_widget(widget_name)
                        widget.show_usage_time()
                        break
            except ValueError:
                pass
        else:
            try:
                while True:
                    widget = self.app_panes.head.val.names.get(widget_name, None)
                    if widget is None:
                        self.app_panes.goNext()
                    else:
                        self.app_panes.head.val.open_widget(widget_name)
                        widget.show_usage_time()
                        break
            except ValueError:
                pass
