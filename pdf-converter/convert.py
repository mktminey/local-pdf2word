import sys
from pathlib import Path
from pdf2docx import Converter


def convert(pdf_path: str) -> Path:
    src = Path(pdf_path)
    if not src.exists() or src.suffix.lower() != ".pdf":
        raise SystemExit("请提供一个存在的 .pdf 文件")

    dst = src.with_suffix(".docx")
    if dst.exists():
        raise SystemExit(f"{dst.name} 已存在，为避免覆盖已停止")

    cv = Converter(str(src))
    try:
        cv.convert(str(dst), line_overlap_threshold=0.5, line_merging_threshold=2.0)
    finally:
        cv.close()
    return dst


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("用法: python convert.py 文件.pdf")
    print("已生成:", convert(sys.argv[1]))