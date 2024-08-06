"""
Contains classes belonging to the AST.
For representing code in memory.
"""

from ltoken import Token


class Expr:
    """
    A Base class for expressions
    """
    pass


class Binary(Expr):
    """
    Binary operations
    """

    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right = right
