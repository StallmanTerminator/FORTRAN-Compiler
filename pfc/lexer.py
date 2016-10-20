from pfc import io

class Lexer:

	WHITESPACE = [' ', '\t']

	def __init__(self, line_length):
		self.line_length = line_length
		self.errors = 0
		self.tokens = dict()

	def __lineCount(self, stream):
		for index, line in enumerate(stream):
			yield index+1, line

	def __isComment(self, line):
		c = line[0]
		if c == 'C' or c == '*' or c == '!':
			return True
		return False

	def pushToken(self, token, lineno):
		if not lineno in self.tokens:
			self.tokens[lineno] = list()
		self.tokens[lineno].apppend(token)

	def lex(self, stream):
		for index, line in self.__lineCount(stream):
			if len(line) <= self.line_length:
				if self.__isComment(line):
					continue
				if line[0] not in Lexer.WHITESPACE:
					io.error(index,
						"colum 0 must be a whitespace")
					self.errors += 1
			else:
				io.error(index, "Line too long: {} > {}".format(
					len(line), self.line_length))
				self.errors += 1