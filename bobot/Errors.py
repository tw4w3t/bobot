"Errors module"

class RuleNameError(Exception):
    "Error in name of rule"
    pass

class ParsingError(Exception):
    "Error while parsing of message"
    pass

class ResponseFormatError(Exception):
    "Error in response format"
    pass

class ResponseMessageError(Exception):
    "Error in response message description"
    pass

class MessageTextEmptyError(Exception):
    "Exception for empty text in message"
    pass
