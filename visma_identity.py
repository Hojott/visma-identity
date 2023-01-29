#!/usr/bin/env python3
from urllib.parse import urlparse, urlsplit

class VismaIdentity:
    """ Identifies path and parameters from uri request
    """
    def __init__(self, uri: str) -> None:
        
        uriparsed = urlsplit(uri)
        scheme: str = uriparsed.scheme
        self.path: str = uriparsed.netloc # urlsplit views the path as netloc
        
        parameters: list = uriparsed.query.split("&")
        self.parameters: dict = {}
        for parameter: str in parameters:
            parameter.split("=")
            self.parameters[parameter[0]] = parameter[1]

    def __dict__(self) -> dict:
        """ Whole object can be iterated like a dict
        """
        identity_dict = self.parameters
        self.parameters["path"]: str = self.path
        return identity_dict

v = VismaIdentity("visma-identity://confirm?source=netvisor&paymentnumber=102226")
