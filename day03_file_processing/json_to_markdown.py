import json
from pathlib import Path


def read_json(file_path):
    """读取 JSON 文件"""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def build_markdown(qa_list):
    """把问答列表转换成 Markdown 文本"""
    lines = []

    lines.append("# Python 学习问答笔记")
    lines.append("")
    lines.append("> 本文档由 Python 脚本自动生成。")
    lines.append("")

    for index, item in enumerate(qa_list, start=1):
        question = item["question"]
        answer = item["answer"]

        lines.append(f"## {index}. {question}")
        lines.append("")
        lines.append(answer)
        lines.append("")

    return "\n".join(lines)


def write_markdown(file_path, content):
    """写入 Markdown 文件"""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def main():
    input_path = "data/qa_data.json"
    output_path = "output/qa_notes.md"

    try:
        qa_list = read_json(input_path)
        markdown_content = build_markdown(qa_list)
        write_markdown(output_path, markdown_content)

        print(f"转换完成，文件已保存到：{output_path}")

    except FileNotFoundError:
        print("文件不存在，请检查 data/qa_data.json 是否存在。")

    except json.JSONDecodeError:
        print("JSON 格式错误，请检查 qa_data.json。")

    except KeyError as error:
        print(f"JSON 数据缺少字段：{error}")


if __name__ == "__main__":
    main()