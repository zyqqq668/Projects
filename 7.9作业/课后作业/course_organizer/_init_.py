"""课程资料整理工具包"""
__all__ = ["get_file_category", "plan_organize", "execute_organize", "gen_report"]
from .rules import get_file_category
from .core import plan_organize, execute_organize, gen_report