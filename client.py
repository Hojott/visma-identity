#!/usr/bin/env python3
from visma_identity import VismaIdentity

if __name__ == "__main__":
    uri: str = input()
    vi = VismaIdentity(uri)
    print(tuple(vi))
