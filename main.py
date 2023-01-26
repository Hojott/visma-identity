#!/bin/python

class VismaIdentity:
    def __init__(self, uri: str):
        schemeplit: list = uri.split("://")
        pathsplit: list = schemesplit[1].split("?")

        scheme: str = schemesplit[0]
        self.path: str = pathsplit[0]
        parameters: str = pathsplit[1]

        if self.path == "login":
            source: str = parameters.split("=")[1]
            self.parameters: dict = {
                "source": source
            }

        if self.path == "confirm":
            parameters: list = parameters.split("&")
            source: str = parameters[0].split("=")[1]
            number: int = int(parameters[1].split("=")[1])
            self.parameters: dict = {
                "source": source,
                "payment number": number
            }
        if self.path == "sign":
            parameters: list = parameters.split("&")
            source: str = parameters[0].split("=")[1]
            documentid: str = parameters[1].split("=")[1]
            self.parameters: dict = {
                "source": source,
                "documentid": documentid
            }
        else:
            self.parameters: dict = {
                "Error": "Error"
            }
