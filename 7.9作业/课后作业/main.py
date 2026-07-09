import argparse
from pathlib import Path
from course_organizer import plan_organize, execute_organize, gen_report

def main():
    parser = argparse.ArgumentParser(description="课程资料自动分类整理工具")
    parser.add_argument("--source", required=True, type=str, help="原始资料文件夹路径")
    parser.add_argument("--target", required=True, type=str, help="整理后存放的目标文件夹")
    parser.add_argument("--dry-run", action="store_true", help="仅预览计划，不实际操作文件")
    parser.add_argument("--mode", type=str, default="copy", choices=["copy", "move"], help="文件操作模式：copy复制(默认) / move移动")

    args = parser.parse_args()
    source_dir = Path(args.source).resolve()
    target_dir = Path(args.target).resolve()

    # 校验源目录存在
    if not source_dir.exists() or not source_dir.is_dir():
        print(f"错误：源目录 {source_dir} 不存在或不是文件夹！")
        return

    # 1. 生成整理计划
    plan = plan_organize(source_dir, target_dir)
    if not plan:
        print("源目录下未找到可整理的文件，程序退出")
        return

    # 2. 执行操作（dry-run仅预览）
    execute_organize(target_dir, plan, dry_run=args.dry_run, mode=args.mode)

    # 3. 非dry-run模式生成报告
    if not args.dry_run:
        gen_report(target_dir, plan, mode=args.mode)
        print(f"\n整理完成！所有文件存放至：{target_dir.resolve()}")

if __name__ == "__main__":
    main()