import expr
from ltoken import Token, TokenType


class AstPrinter(expr.Visitor):
    """
    a pretty printer for a given ast
    """

    def print(self, expr: expr.Expr):
        return expr.accept(self)

    def visit_binary_expr(self, expr: expr.Binary):
        return self.parenthesize(expr.operator.lexeme,
                                 expr.left, expr.right)

    def visit_grouping_expr(self, expr: expr.Grouping):
        return self.parenthesize("group", expr.expression)

    def visit_literal_expr(self, expr: expr.Literal):
        if expr.value == None:
            return "nil"
        else:
            return str(expr.value)

    def visit_unary_expr(self, expr: expr.Unary):
        return self.parenthesize(expr.operator.lexeme,
                                 expr.right)

    def parenthesize(self, name, *exprs: expr.Expr) -> str:
        builder = "(" + name
        for expr in exprs:
            # temp. converted to string
            builder += " " + str(expr.accept(self))
        builder += ")"

        return builder


if __name__ == "__main__":
    expression: expr.Expr = expr.Binary(
        expr.Unary(Token(TokenType.MINUS, "-", None, 1),
                   expr.Literal(123)),
        Token(TokenType.STAR, "*", None, 1),
        expr.Grouping(expr.Literal(45.67)))

    print(AstPrinter().print(expression))
