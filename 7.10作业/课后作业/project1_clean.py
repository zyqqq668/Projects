# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np

# 自动创建文件夹
if not os.path.exists("dataset"):
    os.mkdir("dataset")
if not os.path.exists("clean_data"):
    os.mkdir("clean_data")

# 在线读取Titanic数据集
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("=" * 60)
print("原始数据形状：", df.shape)
print("前5行：")
print(df.head())
print("=" * 60)
print("字段信息：")
print(df.info())
print("=" * 60)
print("缺失值统计：")
print(df.isnull().sum())
print("=" * 60)
print("重复行数：", df.duplicated().sum())
print("=" * 60)
print("数值描述统计：")
print(df.describe())

# 1. 去重
df = df.drop_duplicates(keep="first")
print("\n去重后数据尺寸：", df.shape)

# 2. 三种缺失值处理
# 方案1 删除缺失
df_delete = df.dropna(subset=["Embarked"])
print(f"\n删除Embarked缺失后行数：{df_delete.shape[0]}")

# 方案2 统计填充
df_fill = df.copy()
df_fill["Age"].fillna(df_fill["Age"].median(), inplace=True)
df_fill["Fare"].fillna(df_fill["Fare"].mean(), inplace=True)
df_fill["Embarked"].fillna(df_fill["Embarked"].mode()[0], inplace=True)
df_fill["Cabin"].fillna("Unknown", inplace=True)
print(f"填充后总缺失值：{df_fill.isnull().sum().sum()}")

# 方案3 线性插值
df_interp = df.copy()
df_interp["Age"] = df_interp["Age"].interpolate(method="linear")
df_interp["Fare"] = df_interp["Fare"].interpolate(method="linear")
print(f"插值后总缺失值：{df_interp.isnull().sum().sum()}")

# 3. IQR剔除异常值
def remove_outlier(data, col):
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    low = Q1 - 1.5 * IQR
    high = Q3 + 1.5 * IQR
    return data[(data[col] >= low) & (data[col] <= high)]

df_clean = df_fill.copy()
df_clean = remove_outlier(df_clean, "Fare")
df_clean = remove_outlier(df_clean, "Age")
print(f"\n剔除异常后数据尺寸：{df_clean.shape}")

# 4. 类型转换与标准化
df_clean["Survived"] = df_clean["Survived"].astype("category")
df_clean["Pclass"] = df_clean["Pclass"].astype("category")
df_clean["Name"] = df_clean["Name"].str.strip().str.lower()
df_clean["Sex"] = df_clean["Sex"].map({"male": 0, "female": 1})
df_clean["Embarked"] = df_clean["Embarked"].map({"S": 0, "C": 1, "Q": 2})
df_clean["Fare"] = df_clean["Fare"].round(2)

print("\n" + "=" * 60)
print("清洗完成字段信息：")
print(df_clean.info())
print("\n最终缺失值：")
print(df_clean.isnull().sum())

# 保存清洗数据到 clean_data 文件夹
df_clean.to_csv("clean_data/titanic_clean.csv", index=False, encoding="utf-8-sig")
print("✅ 清洗完成，干净数据已保存至 clean_data/titanic_clean.csv")