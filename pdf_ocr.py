# from: https://qiita.com/Hagian/items/f508d5996e05f4497557

from pathlib import Path
from pdf2image import convert_from_path
import pyocr
import pyocr.builders
import sys

# 使用可能なOCRツールを探す
tools = pyocr.get_available_tools()
tool = tools[0]
if len(tools) == 0:
    print("OCR tool is not found.")
    sys.exit(1)
lan = "eng"

# 抽出したいファイル名を指定
f_name = input("Enter PDF file name you want to extract text data: ")
print("input!")

# パスを設定
pdf_path = Path(f"{f_name}.pdf")
txt_path = Path(f"{f_name}.txt")

# PDFから画像ファイルに変換
pages = convert_from_path(str(pdf_path), 300)

print("converted!")

txt = ""
for i, page in enumerate(pages):
    txt = txt + tool.image_to_string(page, lang=lan, builder=pyocr.builders.TextBuilder(tesseract_layout=6))

# テキストファイルに書き出し
with open(txt_path, mode="w") as f:
    f.write(txt)
print("Process completed!")
