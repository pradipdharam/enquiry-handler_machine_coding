from data.enquiry_type import EnquiryType
from enquiry.enquiry_handler import EnquiryHandler


class IdleHandler(EnquiryHandler):
    def __init__(self, next_handler: EnquiryHandler):
        self.__next_handler = next_handler

    def handle(self, enquiry: str) -> EnquiryType:
        print("Inside IdleHandler")
        return EnquiryType.UNKNOWN
