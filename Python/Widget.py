from enum import Enum
from datetime import datetime as dt

class Category(Enum):
    ENTERTAINMENT = 1
    EDUCATIONAL = 2
    SOCIAL = 3
    INFO = 4

class Widget:
    def __init__(self, name: str, category: Category):
        self.__name = name.lower()
        self.__category = category
        self.__usage_times = []
    
    def __str__(self):
        return "{}: {}".format(self.__name, self.__category.name)

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category.name

    @property
    def category_value(self):
        return self.__category.value

    def open(self):
        self.__usage_times.append(dt.now())

    def show_usage_time(self):
        print(self.__usage_times)
