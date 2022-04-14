from abc import ABC, abstractmethod


class PCInterface(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def show(self):
        pass