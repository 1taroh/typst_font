import json

def txt_to_json(input_file, output_file, encoding='utf-8'):
    # テキストファイルを読み込み
    with open(input_file, 'r', encoding=encoding) as f:
        lines = f.readlines()

    # JSON形式に整形
    entries = [{"name": line.strip()} for line in lines]

    # JSONファイルに書き込み
    with open(output_file, 'w', encoding=encoding) as f:
        json.dump({"entries": entries}, f, indent=4, ensure_ascii=False)

# 入力ファイルと出力ファイルを指定して実行
input_file = "fonts.txt"
output_file = "fonts.json"
txt_to_json(input_file, output_file, encoding='utf-8')  # エンコーディングを適切に指定する