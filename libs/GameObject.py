import abc

class GameObject(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, display, pos_x, pos_y, size_x, size_y):
        self.display = display
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def render(self):
        pass