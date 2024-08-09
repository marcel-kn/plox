from abc import ABC, abstractmethod

from ltoken import Token

class Expr(ABC):
	@abstractmethod
	def accept(self, visitor: "Visitor"):
		pass

class Visitor(ABC):
	@abstractmethod
	def visit_Binary(self, expr: "Binary"):
		pass

	@abstractmethod
	def visit_Grouping(self, expr: "Grouping"):
		pass

	@abstractmethod
	def visit_Literal(self, expr: "Literal"):
		pass

	@abstractmethod
	def visit_Unary(self, expr: "Unary"):
		pass


class Binary(Expr):
	def __init__(self, left: Expr, operator: Token, right: Expr):
		self.left = left
		self.operator = operator
		self.right = right

	def accept(self, visitor: Visitor):
		pass

class Grouping(Expr):
	def __init__(self, expression: Expr):
		self.expression = expression

	def accept(self, visitor: Visitor):
		pass

class Literal(Expr):
	def __init__(self, value):
		self.value = value

	def accept(self, visitor: Visitor):
		pass

class Unary(Expr):
	def __init__(self, operator: Token, right: Expr):
		self.operator = operator
		self.right = right

	def accept(self, visitor: Visitor):
		pass
