import abc


class ReviewPort(abc.ABC):
    @abc.abstractmethod
    def save(self, review):
        raise NotImplementedError
