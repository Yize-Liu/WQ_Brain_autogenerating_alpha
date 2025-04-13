alpha_factory/
├── expressions/
│   └── population_gen1.csv         # 记录每代因子表达式
├── data/
│   └── stock_data.feather          # 使用 yfinance 等抓取历史数据
├── engine/
│   ├── expression_parser.py        # 表达式执行器
│   ├── evaluator.py                # 计算 IC/IR 的函数
│   └── ga_core.py                  # 遗传算法逻辑模块
├── api/
│   └── worldquant_submit.py        # 可选，连接 WQ 平台
├── run.py                          # 主程序入口
└── config.yaml                     # 可配置参数（种群规模、基因池等）
