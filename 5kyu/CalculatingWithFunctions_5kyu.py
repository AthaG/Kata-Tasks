'''This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five()))  # must return 35
four(plus(nine()))  # must return 13
eight(minus(three()))  # must return 5
six(divided_by(two()))  # must return 3

Requirements:

    There must be a function for each number from 0 ("zero") to 9 ("nine")
    There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy(divided_by in Ruby and Python)
    Each calculation consist of exactly one operation and two numbers
    The most outer function represents the left operand, the most inner function represents the right operand
    Division should be integer division. For example, this should return 2, not 2.666666...:

eight(divided_by(three()))'''


def zero(x=0): return 0 if not x else eval('0' + x)
def one(x=0): return 1 if not x else eval('1' + x)
def two(x=0): return 2 if not x else eval('2' + x)
def three(x=0): return 3 if not x else eval('3' + x)
def four(x=0): return 4 if not x else eval('4' + x)
def five(x=0): return 5 if not x else eval('5' + x)
def six(x=0): return 6 if not x else eval('6' + x)
def seven(x=0): return 7 if not x else eval('7' + x)
def eight(x=0): return 8 if not x else eval('8' + x)
def nine(x=0): return 9 if not x else eval('9' + x)


def plus(x): return '+' + str(x)
def minus(x): return '-' + str(x)
def times(x): return '*' + str(x)
def divided_by(x): return '//' + str(x)
