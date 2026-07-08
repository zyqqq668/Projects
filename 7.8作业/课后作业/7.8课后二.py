import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]

# 生成200个交易日随机模拟股价
np.random.seed(0)
days = 200
start_price = 100
#生成随机日波动
daily_change = np.random.normal(0, 0.018, days)
prices = start_price * np.exp(np.cumsum(daily_change))
prices = np.insert(prices, 0, start_price)

#对数收益率、年化波动率
log_returns = np.log(prices[1:] / prices[:-1])
annual_vol = np.std(log_returns) * np.sqrt(252)
print("年化波动率：", round(annual_vol, 3))

#5日、20日移动平均线
def ma_calc(data, window):
    kernel = np.ones(window) / window
    return np.convolve(data, kernel, mode="valid")

ma5 = ma_calc(prices, 5)
ma20 = ma_calc(prices, 20)

#投资组合风险：3只股票收益率、协方差矩阵
stock_num = 3
stock_rets = np.random.normal(0, 0.02, (stock_num, days))
cov_mat = np.cov(stock_rets)
corr_mat = np.corrcoef(stock_rets)
print("\n股票协方差矩阵：\n", np.round(cov_mat, 4))

#等权重组合波动率
weight = np.array([1/3, 1/3, 1/3])
port_var = weight @ cov_mat @ weight.T
port_vol = np.sqrt(port_var * 252)
print("投资组合年化波动率：", round(port_vol, 3))

#可视化股价+均线
plt.figure(figsize=(10,5))
plt.plot(prices, label="股票价格", c="#4472c4")
plt.plot(np.arange(4, len(prices)), ma5, label="MA5", c="#ed7d31")
plt.plot(np.arange(19, len(prices)), ma20, label="MA20", c="#70ad47")
plt.title("模拟股价与移动平均线")
plt.legend()
plt.grid(alpha=0.3)
plt.show()