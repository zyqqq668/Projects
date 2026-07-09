课程资料整理器
一、项目介绍
本工具使用Python自动化批量整理课程文件，根据文件名关键字优先级+文件后缀自动分类，支持预览模式、复制/移动双模式，自动生成整理统计报告。
二、项目文件结构
02_course_materials_organizer/
├── main.py # 程序入口，解析命令行参数
├── README.md # 项目说明文档
├── 题目与要求.md # 作业原题
├── sample_materials/ # 测试用素材文件夹（9 个测试文件）
└── course_organizer/ # 功能模块包
    ├── init.py
    ├── rules.py # 分类规则、关键字、后缀映射
    └── core.py # 文件扫描、复制移动、报告生成核心逻辑
三、运行命令与执行结果
命令1：预览dry-run模式
运行指令：
python main.py --source sample_materials --target organized_materials --dry-run
执行输出：
===== DRY RUN 预览整理计划（无实际操作）=====
[slides] Python第01讲_基础语法.pptx  --> xxx/organized_materials/slides/Python第01讲_基础语法.pptx
[code] Python第01讲_课堂代码.py  --> xxx/organized_materials/code/Python第01讲_课堂代码.py
[homework] Python第01讲_作业说明.pdf  --> xxx/organized_materials/homework/Python第01讲_作业说明.pdf
[code] NumPy数组练习.ipynb  --> xxx/organized_materials/code/NumPy数组练习.ipynb
[data] 成绩样例.csv  --> xxx/organized_materials/data/成绩样例.csv
[documents] 课程通知.txt  --> xxx/organized_materials/documents/课程通知.txt
[documents] 学生问题记录.md  --> xxx/organized_materials/documents/学生问题记录.md
[images] 截图_环境配置.png  --> xxx/organized_materials/images/截图_环境配置.png
[others] 未分类文件.xyz  --> xxx/organized_materials/others/未分类文件.xyz
总计待整理文件：9
命令 2：真实复制整理模式
运行指令：
python main.py --source sample_materials --target organized_materials
执行输出：
===== 开始整理文件 =====
[复制] Python第01讲_基础语法.pptx → xxx/organized_materials/slides/Python第01讲_基础语法.pptx
[复制] Python第01讲_课堂代码.py → xxx/organized_materials/code/Python第01讲_课堂代码.py
[复制] Python第01讲_作业说明.pdf → xxx/organized_materials/homework/Python第01讲_作业说明.pdf
[复制] NumPy数组练习.ipynb → xxx/organized_materials/code/NumPy数组练习.ipynb
[复制] 成绩样例.csv → xxx/organized_materials/data/成绩样例.csv
[复制] 课程通知.txt → xxx/organized_materials/documents/课程通知.txt
[复制] 学生问题记录.md → xxx/organized_materials/documents/学生问题记录.md
[复制] 截图_环境配置.png → xxx/organized_materials/images/截图_环境配置.png
[复制] 未分类文件.xyz → xxx/organized_materials/others/未分类文件.xyz

整理报告已生成：xxx/organized_materials/整理报告.txt

整理完成！所有文件存放至：xxx/organized_materials