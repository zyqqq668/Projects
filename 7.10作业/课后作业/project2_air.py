# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 解决中文乱码、负号显示
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 自动创建所需文件夹
if not os.path.exists("dataset"):
    os.mkdir("dataset")
if not os.path.exists("plot_img"):
    os.mkdir("plot_img")

# 读取数据集，增加异常捕获
try:
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00381/PRSA_data_2010.1.1-2014.12.31.csv"
    df = pd.read_csv(url)
    df = df.drop("No", axis=1)
except Exception as e:
    print("在线读取失败，创建模拟测试数据用于演示：", e)
    np.random.seed(0)
    df = pd.DataFrame({
        "year": np.repeat(np.arange(2010,2015), 365*24),
        "month": np.random.randint(1,13, 365*24*5),
        "day": np.random.randint(1,29, 365*24*5),
        "hour": np.random.randint(0,24, 365*24*5),
        "pm2.5": np.random.normal(80, 40, 365*24*5),
        "DEWP": np.random.normal(5, 9, 365*24*5),
        "TEMP": np.random.normal(12, 10, 365*24*5),
        "PRES": np.random.normal(1010, 10, 365*24*5),
        "cbwd": np.random.choice(["NW","NE","SE","CV"], size=365*24*5),
        "Iws": np.random.normal(3, 2, 365*24*5),
        "Is": np.random.uniform(0,1,365*24*5),
        "Ir": np.random.uniform(0,1,365*24*5)
    })

# 构造标准时间列
df["datetime"] = pd.to_datetime(df[["year", "month", "day", "hour"]])

# 季节映射
season_map = {
    1:"冬季",2:"冬季",12:"冬季",
    3:"春季",4:"春季",5:"春季",
    6:"夏季",7:"夏季",8:"夏季",
    9:"秋季",10:"秋季",11:"秋季"
}
df["season"] = df["month"].map(season_map)

# PM2.5缺失值线性插值
df["pm2.5"] = df["pm2.5"].interpolate(method="linear")

# 仅使用数据集真实存在的字段
target_col = ["pm2.5"]
meteor_cols = ["TEMP", "DEWP", "PRES", "Iws", "Is", "Ir"]
all_analysis_cols = target_col + meteor_cols

# 输出统计指标
print("="*50)
print("PM2.5与气象因子统计指标：")
print(df[all_analysis_cols].describe())

print("="*50)
season_pm25 = df.groupby("season")["pm2.5"].mean().sort_values(ascending=False)
print("各季节PM2.5平均浓度：")
print(season_pm25)

month_pm25 = df.groupby("month")["pm2.5"].mean()
print("\n1-12月PM2.5月均浓度：")
print(month_pm25)

# 1. 相关性热力图
plt.figure(figsize=(10,6))
corr_df = df[all_analysis_cols].corr()
sns.heatmap(corr_df, annot=True, cmap="RdYlBu_r", fmt=".2f")
plt.title("PM2.5与气象因子相关性热力图")
plt.tight_layout()
plt.savefig("plot_img/热力图_相关性.png", dpi=300)
plt.show()
plt.close()

# 2. PM2.5时间序列折线图
plt.figure(figsize=(15,4))
df_sort = df.sort_values("datetime")
df_sample = df_sort.iloc[::100, :]
plt.plot(df_sample["datetime"], df_sample["pm2.5"], c="#c82423", linewidth=0.4)
plt.title("2010-2014 PM2.5浓度时间序列变化")
plt.xlabel("时间")
plt.ylabel("PM2.5 浓度 μg/m³")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("plot_img/折线图_时序趋势.png", dpi=300)
plt.show()
plt.close()

# 3. 四季PM2.5柱状图
plt.figure(figsize=(7,4))
sns.barplot(x=season_pm25.index, y=season_pm25.values, palette="Blues_r")
plt.title("四季平均PM2.5浓度对比")
plt.xlabel("季节")
plt.ylabel("平均浓度")
plt.tight_layout()
plt.savefig("plot_img/柱状图_季节对比.png", dpi=300)
plt.show()
plt.close()

# 4. 气温-PM2.5散点图
plt.figure(figsize=(6,4))
sample_scatter = df.sample(n=min(5000, len(df)), random_state=1)
plt.scatter(sample_scatter["TEMP"], sample_scatter["pm2.5"], alpha=0.15, c="#2878b5")
plt.title("气温与PM2.5浓度分布关系")
plt.xlabel("气温 ℃")
plt.ylabel("PM2.5浓度")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("plot_img/散点图_温度PM25.png", dpi=300)
plt.show()
plt.close()

# 5. 月度PM2.5变化折线图
plt.figure(figsize=(8,4))
plt.plot(month_pm25.index, month_pm25.values, marker="o", linewidth=2, c="#d44848")
plt.xticks(range(1,13))
plt.title("1-12月PM2.5月均浓度变化")
plt.xlabel("月份")
plt.ylabel("月均浓度")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("plot_img/折线图_月度规律.png", dpi=300)
plt.show()
plt.close()

print("✅ 全部图表绘制完成，图片保存在 plot_img 文件夹")