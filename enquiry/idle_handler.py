from data.enquiry_type import EnquiryType
from enquiry.enquiry_handler import EnquiryHandler


class IdleHandler(EnquiryHandler):
    def handle(self, enquiry: str) -> EnquiryType:
        print("Inside IdleHandler")
        return EnquiryType.UNKNOWN
