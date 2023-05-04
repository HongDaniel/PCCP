expression= "100-200*300-500+20"	

from itertools import permutations as P
import re

def calculate(operators,expression):
    expression = re.split(r'(\D)',expression)
    for op in operators:
        while(op in expression):
            for idx,el in enumerate(expression):
                if el == op:
                    if op == '-':
                        expression[idx] = int(expression[idx-1])-int(expression[idx+1])
                    elif op == '+':
                        expression[idx] = int(expression[idx-1])+int(expression[idx+1])
                    elif op == '*':
                        expression[idx] = int(expression[idx-1])*int(expression[idx+1])
                    expression.pop(idx-1)
                    expression.pop(idx)
                    break
    return abs(expression.pop())

def solution(expression):
    answer = []
    operators = set()
    for el in expression:
        if el in ('+','-','*'):
            operators.add(el)
    operators = list(P(operators,len(operators)))
    for case in operators:
        answer.append(calculate(case,expression))
    return max(answer)

solution(expression)