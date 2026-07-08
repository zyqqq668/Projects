import math
RECORD_FILE = "record.txt"

def add(a,b):
    """加法函数"""
    answer =  a + b
    return f"{a} + {b} = {answer}", answer

def subtract(a,b):
    """减法函数"""
    answer = a - b
    return f"{a} - {b} = {answer}", answer

def multiply(a,b):
    """乘法函数"""
    answer = a * b
    return f"{a} * {b} = {answer}", answer

def divide(a,b):
    """除法函数"""
    if b == 0:
        return "除数不能为零！", None
    answer = a / b
    return f"{a} / {b} = {answer}", answer

def power(a,b):
    """幂函数"""
    answer = math.pow(a, b)
    return f"{a} ^ {b} = {answer}", answer

def square_root(a):
    """平方根函数"""
    if a < 0:
        return "不能对负数开平方！", None
    answer = math.sqrt(a)
    return f"√{a} = {answer}", answer

def save_record(record):
    """保存计算记录到文件"""
    with open(RECORD_FILE, "a", encoding="utf-8") as f:
        f.write(record + "\n")

def load_records():
    try:
        with open(RECORD_FILE, "r", encoding="utf-8") as f:
            records = f.readlines()
        if not records:
            print("没有找到计算记录。")
            return
        print("计算记录如下：")
        for record in records:
            print(record.strip())
    except FileNotFoundError:
        print("没有找到计算记录。")

def show_menu():
    """显示菜单"""
    print("欢迎使用计算器")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    print("5. 幂运算")
    print("6. 平方根")
    print("7. 查看计算记录")
    print("8. 退出")

def get_number(prompt):
    """安全获取用户输入的数字"""
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("输入无效，请重新输入。")

if __name__ == "__main__":
    while True:
        show_menu()
        try:
            choice = int(input("请输入您的选择（1-8）："))
            if choice == 1:
                a = get_number("请输入第一个数字：")
                b = get_number("请输入第二个数字：")
                record, _ = add(a, b)
                print(record)
                save_record(record)
            elif choice == 2:
                a = get_number("请输入第一个数字：")
                b = get_number("请输入第二个数字：")
                record, _ = subtract(a, b)
                print(record)
                save_record(record)
            elif choice == 3:
                a = get_number("请输入第一个数字：")
                b = get_number("请输入第二个数字：")
                record, _ = multiply(a, b)
                print(record)
                save_record(record)
            elif choice == 4:
                a = get_number("请输入第一个数字：")
                b = get_number("请输入第二个数字：")
                record, _ = divide(a, b)
                print(record)
                if _ is not None:
                    save_record(record)
            elif choice == 5:
                a = get_number("请输入底数：")
                b = get_number("请输入指数：")
                record, _ = power(a, b)
                print(record)
                save_record(record)
            elif choice == 6:
                a = get_number("请输入要开平方的数字：")
                record, _ = square_root(a)
                print(record)
                if _ is not None:
                    save_record(record)
            elif choice == 7:
                load_records()
            elif choice == 8:
                print("感谢使用计算器，再见！")
                break
            else:
                print("无效的选择，请输入1-8之间的数字。")
        except (ZeroDivisionError,ValueError) as e:
            print(f"发生错误：{e}")