#!/usr/bin/python3
def multiple_returns(sentence):
    return (len(sentence), sentence[0] if 0 < len(sentence) else None)
