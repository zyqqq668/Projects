# 完整依赖导入，解决Path、List、shutil未定义报错
from pathlib import Path
import shutil
from typing import List, Dict, Tuple
from .rules import get_file_category

# 定义计划项类型，放在最前面，提前声明
PlanItem = Tuple[Path, Path, str]


def get_safe_dst(dst_dir: Path, filename: str) -> Path:
    """生成不覆盖的目标文件名，重名自动加_1、_2"""
    dst = dst_dir / filename
    if not dst.exists():
        return dst
    stem, suffix = dst.stem, dst.suffix
    idx = 1
    while True:
        new_name = f"{stem}_{idx}{suffix}"
        new_dst = dst_dir / new_name
        if not new_dst.exists():
            return new_dst
        idx += 1


def plan_organize(source: Path, target: Path) -> List[PlanItem]:
    """
    第一步：生成整理计划（只扫描不操作）
    返回所有文件的源路径、安全目标路径、分类
    """
    plan = []
    # 遍历源目录所有文件（不递归子文件夹）
    for item in source.iterdir():
        if not item.is_file():
            continue
        cat_name = get_file_category(item)
        cat_dir = target / cat_name
        safe_dst = get_safe_dst(cat_dir, item.name)
        plan.append((item, safe_dst, cat_name))
    return plan


def execute_organize(target: Path, plan: List[PlanItem], dry_run: bool = False, mode: str = "copy") -> None:
    """
    第二步：执行整理
    dry_run=True：仅打印预览，不创建文件夹、不复制/移动
    mode: copy(默认) / move
    """
    if dry_run:
        print("===== DRY RUN 预览整理计划（无实际操作）=====")
        for src, dst, cat in plan:
            print(f"[{cat}] {src.name}  --> {dst}")
        print(f"总计待整理文件：{len(plan)}")
        return

    # 真实执行：先创建所有分类目录
    all_cats = set(cat for _, _, cat in plan)
    for cat in all_cats:
        (target / cat).mkdir(parents=True, exist_ok=True)

    print("===== 开始整理文件 =====")
    for src, dst, cat in plan:
        if mode == "copy":
            shutil.copy2(src, dst)
            op = "复制"
        else:
            shutil.move(src, dst)
            op = "移动"
        print(f"[{op}] {src.name} → {dst}")


def gen_report(target: Path, plan: List[PlanItem], mode: str = "copy") -> None:
    """生成整理报告.txt写入目标根目录"""
    report_path = target / "整理报告.txt"
    cat_count: Dict[str, int] = {}
    total = len(plan)
    op_name = "复制" if mode == "copy" else "移动"

    # 统计各类文件数量
    for _, _, cat in plan:
        cat_count[cat] = cat_count.get(cat, 0) + 1

    lines = [
        "=" * 50,
        "课程资料整理报告",
        "=" * 50,
        f"文件操作方式：{op_name}",
        f"本次整理总文件数：{total}",
        "",
        "【各类文件统计】",
    ]
    for cat, cnt in sorted(cat_count.items()):
        lines.append(f"  {cat}：{cnt} 个")
    lines.extend(["", "【文件迁移明细】"])
    for src, dst, cat in plan:
        lines.append(f"[{cat}] 源：{src}  →  目标：{dst}")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n整理报告已生成：{report_path.resolve()}")