#!/usr/bin/env python3
from visma_identity import VismaIdentityURIParser

class VismaIdentity:
    def __init__(self, uri: str) -> None:
        uriparsed: tuple = tuple(VismaIdentityURIParser(uri))
        self.path: str = uriparsed[0]
        self.args: dict = uriparsed[1]
    
    def whoami(self) -> str:
        """ Returns information about request as string
        """
        scheme_text: str = "Scheme: visma-identity"
        path_text: str = f"Path: {self.path}"
        args_text: str = f"Args:"
        for k,v in self.args.items():
            args_text += f"\n- {k}: {str(v)}"

        text: str = f"{scheme_text}\n{path_text}\n{args_text}"
        return text

if __name__ == "__main__":
    uri: str = input()
    vi = VismaIdentity(uri)
    text: str = vi.whoami()
    print(text)
