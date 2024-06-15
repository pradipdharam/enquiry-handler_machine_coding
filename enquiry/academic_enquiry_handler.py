from typing import Final

from data.enquiry_type import EnquiryType
from enquiry.enquiry_handler import EnquiryHandler


class AcademicEnquiryHandler(EnquiryHandler):
    __next_handler: Final[EnquiryHandler]

    def __init__(self, next_handler: EnquiryHandler):
        self.__next_handler = next_handler

    def handle(self, enquiry: str) -> EnquiryType:
        print("Inside AcademicEnquiryHandler")
        if "Ds Algo" in enquiry or "Design" in enquiry:
            return EnquiryType.ACADEMIC
        return self.__next_handler.handle(enquiry)
