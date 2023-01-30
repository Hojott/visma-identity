#!/usr/bin/env python3
from urllib.parse import urlparse, urlsplit

class VismaIdentityURIParser:
    """ Identifies path and parameters from uri request. Returns uri path and parameters
    """
    def __init__(self, uri: str) -> None:
        uriparsed = urlsplit(uri)
        self._scheme: str = uriparsed.scheme
        self.path: str = uriparsed.netloc # urlsplit views the path as netloc
        
        parameters: list = uriparsed.query.split("&")
        self.parameters: dict = {}
        for parameter in parameters:
            valuepair = parameter.split("=")
            if valuepair[0] == "paymentnumber":
                self.parameters[valuepair[0]]: int = int(valuepair[1])
            else:
                self.parameters[valuepair[0]]: str = valuepair[1]

    def __getitem__(self, item) -> dict:
        """ Whole object can be treated like a dict
        """
        identity_dict: dict = self.parameters
        self.parameters["path"]: str = self.path
        return identity_dict[item]

    def __iter__(self) -> tuple:
        """ Object can also be iterated
        """
        yield self.path
        yield self.parameters
