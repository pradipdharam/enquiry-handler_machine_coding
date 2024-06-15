from enquiry.academic_enquiry_handler import AcademicEnquiryHandler
from enquiry.enquiry_handler import EnquiryHandler
from enquiry.idle_handler import IdleHandler
from enquiry.log_handler import LogHandler
from enquiry.project_enquiry_handler1 import ProjectEnquiryHandler
from enquiry.subscription_enquiry_handler import SubscriptionEnquiryHandler


class EnquiryHandlerFactory:
    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def get_enquiry_handler() -> EnquiryHandler:
        return LogHandler(
            AcademicEnquiryHandler(
                ProjectEnquiryHandler(
                    SubscriptionEnquiryHandler(IdleHandler())
                )
            ))
