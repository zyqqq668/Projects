import numpy as np

student_names = []
student_scores = np.array([])

def show_menu():
    """打印系统主菜单"""
    print("成绩分析系统")
    print("1. 输入成绩数据")
    print("2. 查看成绩统计")
    print("3. 查看成绩排名")
    print("4. 查看成绩分布")
    print("5. 查询学生成绩")
    print("6. 退出系统")

def input_scores():
    """功能1"""
    global student_names, student_scores
    student_names.clear()
    student_scores = np.array([])

    while True:
        try:
            count = int(input("请输入学生人数："))
            if count <= 0:
                print("人数必须大于0，请重新输入！")
                continue
            break
        except ValueError:
            print("输入非法，请输入数字！")

    score_list = []
    for i in range(1, count + 1):
        name = input(f"\n请输入第{i}个学生姓名：").strip()
        while True:
            try:
                score = float(input("请输入成绩："))
                if 0 <= score <= 100:
                    break
                else:
                    print("成绩范围为0-100，请重新输入！")
            except ValueError:
                print("成绩必须是数字，请重新输入！")
        student_names.append(name)
        score_list.append(score)
    student_scores = np.array(score_list)
    print("\n 成绩录入完成！返回菜单...")

def score_statistics():
    """功能2"""
    if len(student_scores) == 0:
        print(" 暂无成绩数据，请先录入！")
        return
    print("\n========== 成绩统计结果 ==========")
    print(f"学生总数：{len(student_scores)}")
    print(f"平均分：{np.mean(student_scores):.2f}")
    print(f"最高分：{np.max(student_scores):.2f}")
    print(f"最低分：{np.min(student_scores):.2f}")
    print(f"中位数：{np.median(student_scores):.2f}")
    print(f"标准差：{np.std(student_scores):.2f}")

def score_ranking():
    """功能3"""
    if len(student_scores) == 0:
        print(" 暂无成绩数据，请先录入！")
        return
    stu_data = list(zip(student_names, student_scores))
    stu_data.sort(key=lambda x: x[1], reverse=True)
    print("\n========== 成绩排名（从高到低） ==========")
    print(f"{'排名':<6}{'姓名':<8}{'分数':<6}")
    for idx, (name, score) in enumerate(stu_data, start=1):
        print(f"{idx:<6}{name:<8}{score:<6.1f}")

def score_distribution():
    """功能4"""
    if len(student_scores) == 0:
        print(" 暂无成绩数据，请先录入！")
        return
    scores = student_scores
    excellent = np.sum((scores >= 90) & (scores <= 100))
    good = np.sum((scores >= 80) & (scores < 90))
    medium = np.sum((scores >= 60) & (scores < 80))
    poor = np.sum((scores >= 0) & (scores < 60))
    total = len(scores)

    print("\n========== 成绩等级分布 ==========")
    print(f"优秀(90~100)：{excellent}人，占比{excellent/total*100:.1f}%")
    print(f"良好(80~89) ：{good}人，占比{good/total*100:.1f}%")
    print(f"中等(60~79) ：{medium}人，占比{medium/total*100:.1f}%")
    print(f"不及格(0~59)：{poor}人，占比{poor/total*100:.1f}%")

def search_student():
    """功能5"""
    if len(student_scores) == 0:
        print(" 暂无成绩数据，请先录入！")
        return
    target = input("请输入要查询的学生姓名：").strip()
    found = False
    print("\n查询结果：")
    for name, score in zip(student_names, student_scores):
        if target == name:
            print(f"学生：{name}，成绩：{score:.1f}")
            found = True
    if not found:
        print(f"未找到名为【{target}】的学生！")

def main():
    """程序主循环"""
    while True:
        show_menu()
        choice = input("请选择：").strip()
        if choice == "1":
            input_scores()
        elif choice == "2":
            score_statistics()
        elif choice == "3":
            score_ranking()
        elif choice == "4":
            score_distribution()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("系统退出，再见！")
            break
        else:
            print("输入错误，请选择1-6之间的数字！")
        input("\n按回车键返回菜单...")

if __name__ == "__main__":
    main()