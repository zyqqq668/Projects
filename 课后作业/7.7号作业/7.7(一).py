student_list = []

def new_student():
    """录入学生信息"""
    name = input("请输入学生姓名：")
    id = input("请输入学生学号：")
    scores = []
    sub = int(input("请输入科目数量："))
    for i in range(sub):
        s = float(input(f"请输入第{i + 1}门科目的成绩："))
        scores.append(s)
    student = {
        "name": name,
        "id": id,
        "scores": scores
    }
    student_list.append(student)
    print(f"学生 {name} 的信息已录入成功！")

def query_student():
    """按姓名或学号查询学生信息"""
    key = input("请输入学生姓名或学号进行查询：")
    find_flag = False
    for student in student_list:
        if student["name"] == key or student["id"] == key:
            find_flag = True
            print("学生信息如下：" )
            print(f"姓名：{student['name']}") 
            print(f"学号：{student['id']}") 
            print(f"成绩：{student['scores']}")
            break
    if not find_flag:
        print("未找到该学生信息，请检查输入是否正确。")

def statistics():
    """统计整体成绩"""
    if not student_list:
        print("当前没有学生信息，请先录入学生信息。")
        return
    all_scores = []
    for student in student_list:
        all_scores.extend(student["scores"])
    average_score = sum(all_scores) / len(all_scores)
    max_score = max(all_scores)
    min_score = min(all_scores)
    print("整体成绩统计信息：")
    print(f"平均每科成绩：{average_score:.2f}")
    print(f"最高单科成绩：{max_score:.2f}")
    print(f"最低单科成绩：{min_score:.2f}")

def show_menu():
    """显示菜单"""
    print("欢迎使用学生成绩管理系统")
    print("1. 录入学生信息")
    print("2. 查询学生信息")
    print("3. 统计整体成绩")
    print("4. 退出系统")

while True:
    show_menu()
    try:
        choice = int(input("请输入您的选择（1-4）："))
        if choice == 1:
            new_student()
        elif choice == 2:
            query_student()
        elif choice == 3:
            statistics()
        elif choice == 4:
            print("感谢使用学生成绩管理系统，再见！")
            break
        else:
            print("无效的选择，请输入1-4之间的数字。")
    except ValueError:
        print("输入无效，请输入数字。")