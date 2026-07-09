from pathlib import Path

# 作业优先匹配关键字
HOMEWORK_KEYWORDS = {"作业", "练习", "实验", "任务"}

# 后缀 -> 分类目录映射
EXT_TO_FOLDER = {
    ".ppt": "slides",
    ".pptx": "slides",
    ".key": "slides",

    ".py": "code",
    ".ipynb": "code",
    ".c": "code",
    ".cpp": "code",
    ".java": "code",

    ".csv": "data",
    ".xlsx": "data",
    ".json": "data",

    ".pdf": "documents",
    ".doc": "documents",
    ".docx": "documents",
    ".txt": "documents",
    ".md": "documents",

    ".png": "images",
    ".jpg": "images",
    ".jpeg": "images",
    ".gif": "images",
}

def get_file_category(file: Path) -> str:
    """
    获取文件归属分类
    优先级：作业关键字 > 文件后缀 > others
    """
    filename = file.name
    # 优先判断作业
    for kw in HOMEWORK_KEYWORDS:
        if kw in filename:
            return "homework"
    # 按后缀匹配
    suffix = file.suffix.lower()
    return EXT_TO_FOLDER.get(suffix, "others")