from enum import Enum, auto


class EnquiryType(Enum):
    ACADEMIC = auto()
    PROJECT = auto()
    SUBSCRIPTION = auto()
    UNKNOWN = auto()
