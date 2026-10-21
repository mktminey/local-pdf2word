# local-pdf2word

[中文](#中文) | [English](#english)

---

## 中文

一个**完全在本地运行**的 PDF 转 Word 小工具。不联网、不上传、不收费，你的文件不会离开你的电脑。

### 特点

- **隐私安全**：所有处理都在本机完成，不会上传到任何服务器
- **不覆盖原文件**：如果目标文件已存在，程序会停止并提示，而不是直接覆盖
- **两种模式**：
  - `convert.py`：**可编辑模式**，文字可以直接在 Word 里修改
  - `convert_image.py`：**保真模式**，每页渲染成高清图片，外观与原 PDF 完全一致（但文字不可编辑）

### 安装

需要 Python 3.9 或更高版本（Windows 安装时请勾选 **Add python.exe to PATH**）。

```bash
git clone https://github.com/<你的用户名>/local-pdf2word.git
cd local-pdf2word

python -m venv .venv
.venv\Scripts\activate        # Windows (cmd)
# source .venv/bin/activate   # macOS / Linux

pip install -r requirements.txt
```

> 在国内网络下如果安装很慢或报错，可以加上镜像源：
> `pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`

### 使用方法

**可编辑模式**（推荐先试这个）：

```bash
python convert.py 文件.pdf
```

输出：与原文件同目录下的 `文件.docx`

**保真模式**（页面含数学公式、分数线等细线，或需要外观完全一致时）：

```bash
python convert_image.py 文件.pdf
```

输出：同目录下的 `文件_image.docx`。如果文件太大，可以把脚本里的 `dpi` 从 200 调低到 150。

文件名含空格时请加引号：`python convert.py "my file.pdf"`

### 已知局限

- **不支持扫描版 PDF**。本工具只能转换文字可以被选中的 PDF。判断方法：用阅读器打开，试着选中文字，选不中就是扫描版。扫描版需要先做 OCR（文字识别），可以用 [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) 处理后再转换
- **数学公式中的细线可能丢失**，例如分数线。这类页面建议使用保真模式
- **复杂排版**（多栏、图文混排、复杂表格）的还原效果因文件而异
- 保真模式生成的 Word 里文字是图片，不能编辑

### 常见问题

| 报错 | 原因与解决 |
|---|---|
| `AttributeError: 'Rect' object has no attribute 'get_area'` | PyMuPDF 版本过新。运行 `pip install "pymupdf<1.26"` |
| `ValueError: check_hostname requires server_hostname` | 代理与旧版 pip 不兼容。关闭代理，或使用国内镜像源 |
| `No module named 'pdf2docx'` | 没有激活虚拟环境，或没有安装依赖 |
| `已存在，为避免覆盖已停止` | 目标 `.docx` 已存在，删除或改名后重试 |

### 开源协议

本项目采用 **AGPL-3.0** 协议，因为依赖的 PyMuPDF 使用 AGPL 协议。

### 致谢

- [pdf2docx](https://github.com/ArtifexSoftware/pdf2docx)
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF)
- [python-docx](https://github.com/python-openxml/python-docx)

---

## English

A small PDF-to-Word converter that runs **entirely on your own machine**. No internet connection, no uploads, no fees. Your files never leave your computer.

### Features

- **Private by design**: all processing happens locally; nothing is sent to any server
- **Never overwrites**: if the output file already exists, the program stops with a message instead of replacing it
- **Two modes**:
  - `convert.py`: **editable mode**, text stays editable in Word
  - `convert_image.py`: **faithful mode**, each page is rendered as a high-resolution image so the look matches the PDF exactly (text is not editable)

### Installation

Requires Python 3.9 or newer. On Windows, check **Add python.exe to PATH** during installation.

```bash
git clone https://github.com/<your-username>/local-pdf2word.git
cd local-pdf2word

python -m venv .venv
.venv\Scripts\activate        # Windows (cmd)
# source .venv/bin/activate   # macOS / Linux

pip install -r requirements.txt
```

### Usage

**Editable mode** (try this first):

```bash
python convert.py file.pdf
```

Output: `file.docx` in the same folder as the PDF.

**Faithful mode** (for pages with math formulas, fraction bars or other thin lines, or whenever the exact look matters):

```bash
python convert_image.py file.pdf
```

Output: `file_image.docx` in the same folder. If the file is too large, lower `dpi` in the script from 200 to 150.

Wrap file names containing spaces in quotes: `python convert.py "my file.pdf"`

### Known limitations

- **Scanned PDFs are not supported.** The tool only converts PDFs whose text can be selected. To check, open the PDF in a viewer and try selecting text; if you can't, it is a scan. Run OCR first, for example with [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF), then convert
- **Thin lines in math formulas may be lost**, such as fraction bars. Use faithful mode for those pages
- **Complex layouts** (multi-column, mixed text and images, complicated tables) may not be reproduced perfectly
- In faithful mode the text in the Word file is an image and cannot be edited

### Troubleshooting

| Error | Cause and fix |
|---|---|
| `AttributeError: 'Rect' object has no attribute 'get_area'` | PyMuPDF is too new. Run `pip install "pymupdf<1.26"` |
| `ValueError: check_hostname requires server_hostname` | A proxy is conflicting with an old pip. Turn off the proxy or use a mirror |
| `No module named 'pdf2docx'` | The virtual environment is not active, or dependencies are not installed |
| Output file already exists | Delete or rename the existing `.docx` and retry |

### License

Released under **AGPL-3.0**, because PyMuPDF is AGPL-licensed.

### Acknowledgements

- [pdf2docx](https://github.com/ArtifexSoftware/pdf2docx)
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF)
- [python-docx](https://github.com/python-openxml/python-docx)
