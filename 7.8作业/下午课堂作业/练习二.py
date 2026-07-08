import numpy as np
import timeit
np.random.seed(42)

#1
prices = np.array([100, 102, 105, 103, 107])
log_returns = np.log(prices[1:] / prices[:-1])

print("\n===== 对数收益率 =====")
print("股价序列：", prices)
print("每日对数收益率(保留4位小数)：", np.round(log_returns, 4))

#2
prices = np.random.uniform(50, 200, size=100)

# 方法1 np.convolve
ma5_conv = np.convolve(prices, np.ones(5)/5, mode="valid")
ma20_conv = np.convolve(prices, np.ones(20)/20, mode="valid")

# 方法2 np.cumsum前缀和
def moving_avg_cumsum(x, window):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[window:] - cumsum[:-window]) / window

ma5_cum = moving_avg_cumsum(prices, 5)
ma20_cum = moving_avg_cumsum(prices, 20)

print("\n===== 移动平均线长度 =====")
print(f"原始股价长度：{len(prices)}")
print(f"卷积MA5长度：{len(ma5_conv)} | 前缀和MA5长度：{len(ma5_cum)}")
print(f"卷积MA20长度：{len(ma20_conv)} | 前缀和MA20长度：{len(ma20_cum)}")

#3
returns = np.random.normal(0, 0.02, size=(1000, 252))

daily_std = np.std(returns, axis=1, keepdims=True)
annual_vol = daily_std * np.sqrt(252)

print("\n===== 风险分析 =====")
print("前5只股票年化波动率：")
print(np.round(annual_vol[:5].T, 3))

corr_matrix = np.corrcoef(returns)
print(f"\n相关系数矩阵shape(股票×股票)：{corr_matrix.shape}")
print("前3×3相关性矩阵：\n", np.round(corr_matrix[:3, :3], 2))