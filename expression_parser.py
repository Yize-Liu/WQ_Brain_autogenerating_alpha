# engine/expression_parser.py
import pandas as pd
import numpy as np

def rank(x):
    if isinstance(x, pd.Series):
        return x.groupby(level='date').rank()
    else:
        return None  # 或 raise ValueError("rank() 只接受时间序列")

def log(x):
    if isinstance(x, pd.Series):
        return np.log(x.clip(lower=1e-6))  # 防止log(0)
    else:
        return None

def abs_(x):
    if isinstance(x, pd.Series):
        return x.abs()
    else:
        return abs(x)  # 允许 abs(1) 等


def evaluate_expression(expr: str, data: pd.DataFrame) -> pd.Series:
    """
    对输入的表达式做 eval 运算, data 是 multi-index (date, symbol)
    接收一个字符串表达式,使用你给定的行情数据,执行它并返回因子值(pd.Series)
    """
    local_dict = {
        'close': data['close'],
        'open': data['open'],
        'high': data['high'],
        'low': data['low'],
        'volume': data['volume'],
        'rank': rank,
        'log': log,
        'abs': abs_,
    }

    return eval(expr, {"__builtins__": None}, local_dict)
