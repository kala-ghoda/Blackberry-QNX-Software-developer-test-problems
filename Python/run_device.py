#!/usr/bin/python3

from Device import Device
from Widget import Widget, Category

if __name__ == "__main__":
    widget_matrix = [[Widget("Facebook", Category.SOCIAL), Widget("Google", Category.INFO), Widget("YouTube", Category.ENTERTAINMENT)],
                     [Widget("Whatsapp", Category.SOCIAL), Widget("COD", Category.ENTERTAINMENT), Widget("TED Talks", Category.EDUCATIONAL), Widget("Inshorts", Category.INFO)],
                     [Widget("Snapchat", Category.SOCIAL), Widget("VLC Media Player", Category.ENTERTAINMENT)]]

    device = Device(0xffd242e242ac34b, widget_matrix)
    print(str(device))
    device.open_app_widget("whatsapp")
