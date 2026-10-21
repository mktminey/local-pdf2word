import sys
from pathlib import Path

import fitz  # PyMuPDF
from docx import Document
from docx.shared import Mm


def convert_to_image_docx(pdf_path: str, dpi: int = 200) -> Path:
    src = Path(pdf_path)
    if not src.exists() or src.suffix.lower() != ".pdf":
        raise SystemExit("请提供一个存在的 .pdf 文件")

    dst = src.with_name(src.stem + "_image.docx")
    if dst.exists():
        raise SystemExit(f"{dst.name} 已存在，为避免覆盖已停止")

    pdf = fitz.open(str(src))
    doc = Document()
    tmp_dir = src.parent / "_tmp_pages"
    tmp_dir.mkdir(exist_ok=True)

    try:
        for i, page in enumerate(pdf):
            # 按 PDF 页面真实大小设置 Word 页面
            width_mm = page.rect.width / 72 * 25.4
            height_mm = page.rect.height / 72 * 25.4

            if i == 0:
                section = doc.sections[0]
            else:
                section = doc.add_section()
            section.page_width = Mm(width_mm)
            section.page_height = Mm(height_mm)
            section.left_margin = section.right_margin = Mm(0)
            section.top_margin = section.bottom_margin = Mm(0)

            # 渲染成图片
            pix = page.get_pixmap(dpi=dpi)
            img_path = tmp_dir / f"page_{i + 1}.png"
            pix.save(str(img_path))

            doc.add_picture(str(img_path), width=Mm(width_mm))
            print(f"已处理第 {i + 1}/{len(pdf)} 页")

        doc.save(str(dst))
    finally:
        pdf.close()
        for f in tmp_dir.glob("*.png"):
            f.unlink()
        tmp_dir.rmdir()

    return dst


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("用法: python convert_image.py 文件.pdf")
    print("已生成:", convert_to_image_docx(sys.argv[1]))