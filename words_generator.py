# This .py file is used to generate words used in word guess game from an .xls file

import pandas as pd

# words ref: https://www.newgeneralservicelist.org/
def extract_words_from_xls(file_path):
    # 读取 Excel 文件
    df = pd.read_excel(file_path, header=None)  # header=None 表示无列名
    # 取第一列（索引为 0）
    words = df.iloc[:, 0].dropna().astype(str).tolist()
    return words

# 文件路径
file_path = 'ngsl-101-by-band-qq9o.xls'

# 提取第一列单词
extracted_words = extract_words_from_xls(file_path)

# 写入 TXT 文件，逗号分隔
with open('words.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(','.join(extracted_words))

print("Words have been successfully extracted from .xls and written to words.txt file.")
