from Widget import Widget, Category

class ApplicationPane:
    def __init__(self, widgets: list):
        self.widgets, self.names = self.__check_widget(widgets)
        self.num_widgets = len(self.widgets)
    
    def __check_widget(self, widgets: list):
        names = {}
        uniques = []
        for widget in widgets:
            if widget.name in names:
                continue
            names[widget.name.lower()] = widget
            uniques.append(widget)
        return uniques, names

    def __str__(self):
        widget_list = []
        for widget in self.widgets:
            widget_list.append(str(widget))
        pane_string = "\n".join(widget_list) + "\n"
        return pane_string

    def open_widget(self, widget_name):
        widget = self.names.get(widget_name, None)
        if widget is not None:
            print("Opening widget: {}".format(widget.name.capitalize()))
            widget.open()
        else:
            print("Widget does not exist...")
