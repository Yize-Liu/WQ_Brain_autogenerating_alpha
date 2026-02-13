# run.py
import pandas as pd
from engine.expression_parser import evaluate_expression
from engine.evaluator import compute_daily_ic, compute_ir
from engine.expression_generator import generate_expression


# 读取数据和表达式
data = pd.read_csv("data/prices.csv", parse_dates=['Date'])
data.columns = [col.lower() for col in data.columns]
data = data.rename(columns={"date": "date"})
data = data.set_index(['date', 'symbol'])

returns = data['close'].groupby('symbol').pct_change().shift(-1)  # next-day return

with open("expressions/alpha_list.txt", "r") as f:
    expressions = [generate_expression(depth=2) for _ in range(10)]

results = []
for expr in expressions:
    try:
        factor = evaluate_expression(expr, data)
        ic = compute_daily_ic(factor, returns)
        ir = compute_ir(ic)
        results.append((expr, ir))
    except Exception as e:
        print(f"❌ Failed on {expr}: {e}")

# 输出 Top 因子
results.sort(key=lambda x: x[1], reverse=True)
for expr, ir in results[:5]:
    print(f"✅ IR={ir:.3f} | {expr}")

pd.DataFrame(results, columns=["expression", "IR"]).to_csv("top_alphas.csv", index=False)