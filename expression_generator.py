# engine/expression_generator.py

import random

OPERATORS = ['+', '-', '*', '/']
FUNCTIONS = ['rank', 'log', 'abs']
FIELDS = ['close', 'open', 'high', 'low', 'volume']
CONSTANTS = ['1', '2', '0.5']

def generate_expression(depth=2):
    """
    简单的表达式生成器
    """
    if depth == 0:
        choice = random.choice(FIELDS + CONSTANTS)
        if random.random() < 0.3:
            func = random.choice(FUNCTIONS)
            return f"{func}({choice})"
        else:
            return choice
    else:
        left = generate_expression(depth - 1)
        right = generate_expression(depth - 1)
        op = random.choice(OPERATORS)
        return f"({left} {op} {right})"
