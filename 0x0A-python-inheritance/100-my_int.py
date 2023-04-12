#!/usr/bin/python3
"""class inheritance"""

class MyInt(int):
    """myint inherit from int"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
