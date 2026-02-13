# engine/evaluator.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.stats import spearmanr

def compute_daily_ic(factor: pd.Series, returns: pd.Series) -> pd.Series:
    """对齐后按日分组计算 IC"""
    df = pd.concat([factor, returns], axis=1).dropna()
    df.columns = ['factor', 'return']
    grouped = df.groupby('date').apply(lambda g: spearmanr(g['factor'], g['return'])[0])
    return grouped

def compute_ir(ic_series: pd.Series) -> float:
    """IC 的 IR"""
    return ic_series.mean() / ic_series.std() * np.sqrt(250)