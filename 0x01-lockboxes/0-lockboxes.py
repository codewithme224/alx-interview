#!/usr/bin/python3
"""method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    keys = [0]
    for key in keys:
        for newKey in boxes[key]:
            if newKey not in keys and newKey < len(boxes):
                keys.append(newKey)
    if len(keys) == len(boxes):
        return True
    return False
