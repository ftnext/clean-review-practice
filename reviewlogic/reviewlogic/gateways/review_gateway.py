import abc


class ReviewPort(abc.ABC):
    def __init__(self, driver):
        self.driver = driver

    @abc.abstractmethod
    def save(self, review):
        raise NotImplementedError


class ReviewGateway(ReviewPort):
    def save(self, review):
        raise NotImplementedError
