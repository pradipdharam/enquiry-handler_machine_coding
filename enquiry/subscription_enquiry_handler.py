from typing import Final

from data.enquiry_type import EnquiryType
from enquiry.enquiry_handler import EnquiryHandler


class SubscriptionEnquiryHandler(EnquiryHandler):
    __next_handler: Final[EnquiryHandler]

    def __init__(self, next_handler: EnquiryHandler):
        self.__next_handler = next_handler

    def handle(self, enquiry: str) -> EnquiryType:
        print("Inside SubscriptionEnquiryHandler")
        if "Upgrade" in enquiry or "payment" in enquiry:
            return EnquiryType.SUBSCRIPTION
        return self.__next_handler.handle(enquiry)
