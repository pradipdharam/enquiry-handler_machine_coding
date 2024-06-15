from enquiry.enquiry_handler_factory import EnquiryHandlerFactory


class HandleEnquiryApi:
    def handle_enquiry(self, enquiry: str):
        EnquiryHandlerFactory.get_enquiry_handler().handle(enquiry)
        return None


if __name__ == "__main__":
    EnquiryHandlerFactory.get_enquiry_handler().handle(
        "I want to take 1 month Upgrade"
    )
