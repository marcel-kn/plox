from expr import *


class AstPrinter(Visitor):
    def print(self, expr: Expr):
        return expr.accept(self)
