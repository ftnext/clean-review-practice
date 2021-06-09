import abc


class ReviewDriver(abc.ABC):
    @abc.abstractmethod
    def save(self, entity):
        raise NotImplementedError
