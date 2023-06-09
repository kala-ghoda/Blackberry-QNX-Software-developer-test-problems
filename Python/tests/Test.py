import sys, os
from abc import ABC, abstractmethod

parent_dir = os.path.dirname(os.getcwd())
sys.path.append(parent_dir)

class Test(ABC):
    @abstractmethod
    def test(self, **kwargs):
        pass

    @abstractmethod
    def evaluate(self, expected, actual):
        pass
