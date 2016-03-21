from collections import Iterable


def create_constant(value):
    return Constant(value)


def create_variable(name):
    return Variable(name)


def create_operator(symbol, function):
    return Operator(symbol, function)


def create_expression(structure):
    return Expression(structure)


class Entity:
    OPERATORS = {
        '+': lambda lhs, rhs: lhs + rhs,
        '-': lambda lhs, rhs: lhs - rhs,
        '*': lambda lhs, rhs: lhs * rhs,
        '/': lambda lhs, rhs: lhs / rhs,
        '//': lambda lhs, rhs: lhs // rhs,
        '%': lambda lhs, rhs: lhs % rhs,
    }

    def __add__(self, other):
        exp_structure = (self, Operator('+', Entity.OPERATORS['+']), other)
        return Expression(exp_structure)

    def __radd__(self, other):
        exp_structure = (other, Operator('+', Entity.OPERATORS['+']), self)
        return Expression(exp_structure)

    def __sub__(self, other):
        exp_structure = (self, Operator('-', Entity.OPERATORS['-']), other)
        return Expression(exp_structure)

    def __rsub__(self, other):
        exp_structure = (other, Operator('-', Entity.OPERATORS['-']), self)
        return Expression(exp_structure)

    def __mul__(self, other):
        exp_structure = (self, Operator('*', Entity.OPERATORS['*']), other)
        return Expression(exp_structure)

    def __rmul__(self, other):
        exp_structure = (other, Operator('*', Entity.OPERATORS['*']), self)
        return Expression(exp_structure)

    def __truediv__(self, other):
        exp_structure = (self, Operator('/', Entity.OPERATORS['/']), other)
        return Expression(exp_structure)

    def __rtruediv__(self, other):
        exp_structure = (other, Operator('/', Entity.OPERATORS['/']), self)
        return Expression(exp_structure)

    def __floordiv__(self, other):
        exp_structure = (self, Operator('//', Entity.OPERATORS['//']), other)
        return Expression(exp_structure)

    def __rfloordiv__(self, other):
        exp_structure = (other, Operator('//', Entity.OPERATORS['//']), self)
        return Expression(exp_structure)

    def __mod__(self, other):
        exp_structure = (self, Operator('%', Entity.OPERATORS['%']), other)
        return Expression(exp_structure)

    def __rmod__(self, other):
        exp_structure = (other, Operator('%', Entity.OPERATORS['%']), self)
        return Expression(exp_structure)


class Constant(Entity):
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    @property
    def value(self):
        return self._value

    def evaluate(self, **variables):
        return self._value


class Variable(Entity):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return str(self._name)

    @property
    def name(self):
        return self._name

    def evaluate(self, **variables):
        return variables[self._name]


class Operator:
    def __init__(self, symbol, function):
        self._symbol = symbol
        self._function = function

    def __str__(self):
        return str(self._symbol)


class Expression(Entity):
    def __init__(self, structure):
        self._structure = structure

    def __str__(self):
        expression = Expression.flatten_string(self._structure)
        stack = '('
        for item in expression:
            stack += item
        stack += ')'
        return str(stack)

    def __iter__(self):
        return iter(self._structure)

    @staticmethod
    def flatten(structure):
        for item in structure:
            if isinstance(item, Iterable):
                for sub in Expression.flatten(item):
                    yield sub
            elif isinstance(item, Expression):
                Expression.flatten(item.structure)
            else:
                yield item

    @property
    def structure(self):
        return self._structure

    @staticmethod
    def flatten_string(structure):
        for item in structure:
            if isinstance(item, Iterable):
                yield '('
                for sub in Expression.flatten_string(item):
                    yield str(sub)
                yield ')'
            elif isinstance(item, Expression):
                Expression.flatten(item.structure)
            else:
                if isinstance(item, Operator):
                    yield ' '
                    yield str(item)
                    yield ' '
                else:
                    yield str(item)

    def evaluate(self, **variables):
        stack = str(self)
        for i in stack:
            if i in variables:
                stack = stack.replace(i, str(variables[i]))
        return eval(stack)

    @property
    def variable_names(self):
        expression = Expression.flatten(self._structure)
        variables = set()
        for item in expression:
            if isinstance(item, Variable):
                variables.add(item.name)
        return tuple(variables)
