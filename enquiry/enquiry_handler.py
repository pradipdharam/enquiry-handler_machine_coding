import abc


class EnquiryHandler(abc.ABC):
    @abc.abstractmethod
    def handle(self, enquiry: str):
        pass
