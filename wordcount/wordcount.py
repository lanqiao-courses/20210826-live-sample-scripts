import os
import string
import argparse
from rich import print
from rich.table import Table


class CountMarkdownWords:
    """统计指定文件夹中文档的字符数量"""

    def __init__(self, path) -> None:
        self.path = path

    def __walk_course_dir(self) -> dict:
        """遍历指定课程文件夹，返回文件名称"""
        for root, dirs, files in os.walk(self.path):
            lab_names = []
            for lab_name in sorted(files):
                lab_names.append(lab_name)
        return lab_names

    def __words_count(self, contents: str) -> None:
        """统计文件内容中的字符数量

        Args:
            contents ([str]): 文本

        Returns:
            [type]: [全部字符数量，中文字符数量，英文字符数量，空格数量，数字数量，特殊符号数量]
        """

        count_en = count_dg = count_sp = count_zh = count_pu = 0
        s_len = len(contents)
        for c in contents:
            # 统计英文
            if c in string.ascii_letters:
                count_en += 1
            # 统计数字
            elif c.isdigit():
                count_dg += 1
            # 统计空格
            elif c.isspace():
                count_sp += 1
            # 统计中文
            elif c.isalpha():
                count_zh += 1
            # 统计特殊字符
            else:
                count_pu += 1
        return s_len, count_zh, count_en, count_sp, count_dg, count_pu

    def count(self) -> None:
        lab_names = self.__walk_course_dir()
        table = Table("文件名", "全部", "中文", "英文", "空格", "数字", "符号")
        sum_len = sum_en = sum_dg = sum_sp = sum_zh = sum_pu = 0
        for lab_name in lab_names[:-1]:
            with open(os.path.join(self.path, lab_name), "r", encoding="utf-8") as f:
                contents = f.read()
            # 统计字数
            (
                s_len,
                count_zh,
                count_en,
                count_sp,
                count_dg,
                count_pu,
            ) = self.__words_count(contents)
            # 增加总数
            sum_len += s_len
            sum_en += count_en
            sum_dg += count_dg
            sum_sp += count_sp
            sum_zh += count_zh
            sum_pu += count_pu
            # 添加表格行
            table.add_row(
                lab_name,
                str(s_len),
                str(count_zh),
                str(count_en),
                str(count_sp),
                str(count_dg),
                str(count_pu),
            )

        table.add_row(
            "总计",
            str(sum_len),
            str(sum_zh),
            str(sum_en),
            str(sum_sp),
            str(sum_dg),
            str(sum_pu),
        )
        print(table)
        print(f"→ 中英文字符数量：{sum_zh+sum_en}")


parser = argparse.ArgumentParser(description="统计指定文件夹中文档的字符数量")
parser.add_argument(
    "-p",
    "--path",
    type=str,
    help="指定文件夹路径",
    metavar="PATH",
    nargs="?",
    default=os.getcwd(),
)
args = parser.parse_args()
path = args.path
if not os.path.exists(path):
    print(f"{path} 不存在")
    exit(1)
if not os.path.isdir(path):
    print(f"{path} 不是文件夹")
    exit(1)
count_markdown_words = CountMarkdownWords(path)
count_markdown_words.count()
