# 第三天：python文件处理

学会让 Python 读取文件、写入文件、处理 JSON / CSV / Markdown，并理解异常处理。

## 一.创建项目

- 同样的操作，在pycharm中创建项目
- 新建data和output两个新文件夹

---

## 二.读取txt

1. 在data文件夹中创建sample.txt，写入
```text
Python is useful for AI Agent.
RAG needs document processing.
File processing is the first step of building a knowledge base.
```

2. 在`main.py`中写入

```python
file_path = "data/sample.txt"

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```


代码理解：

| 部分                 | 作用                          |
| ------------------ | --------------------------- |
| `open()`           | 打开文件                        |
| `"r"`              | read，读取模式                   |
| `encoding="utf-8"` | 按 UTF-8 编码读取，避免中文乱码         |
| `with`             | 自动关闭文件，不需要手动 `file.close()` |

3. 逐行读取文件

- 有时文件很长，不适合一次性全部读取，可以逐行读取：

```python
file_path = "data/sample.txt"

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

- `line.strip`的作用是去掉每一行前后的空格和换行符。

## 三.写入TXT文件

在main中写

```python
output_path = "output/result.txt"

text = """今天学习了 Python 文件处理。
我学会了读取 TXT 文件。
我也学会了写入 TXT 文件。
"""

with open(output_path, "w", encoding="utf-8") as file:
    file.write(text)

print("写入完成！")
```

- 这里会直接在output文件夹中创建一个新的.txt文件

| 模式    | 作用         |
| ----- | ---------- |
| `"r"` | 读取         |
| `"w"` | 写入，会覆盖原内容  |
| `"a"` | 追加，不会覆盖原内容 |


- 追加写入示例

```python
with open("output/result.txt", "a", encoding="utf-8") as file:
    file.write("\n这是追加写入的新内容。")
```

## 四.读取JSON文件

JSON 是后面调用 API、处理大模型返回结果时非常常见的数据格式。

在data中新建`qa_data.json`

写入：

```JSON
[
  {
    "question": "什么是虚拟环境？",
    "answer": "虚拟环境是给每个 Python 项目准备的独立依赖环境。"
  },
  {
    "question": "为什么要使用 .env？",
    "answer": ".env 用来保存 API Key、数据库密码等敏感配置，避免直接写进代码。"
  },
  {
    "question": "为什么要使用 .gitignore？",
    "answer": ".gitignore 用来告诉 Git 哪些文件不需要提交，例如 .env、.venv 和 __pycache__。"
  }
]
```


在main中写

```python
import json

file_path = "data/qa_data.json"

with open(file_path, "r", encoding="utf-8") as file:
    qa_list = json.load(file)

print(qa_list)

for item in qa_list:
    print("问题：", item["question"])
    print("回答：", item["answer"])
    print()
```


其中的`json.load(file)`

意思是：从 JSON 文件中读取内容，并转换成 Python 可以处理的数据。

这个 JSON 文件最外层是 []，所以读出来是一个列表。

里面每一项是 {}，所以每条问答是一个字典。


## 五.写入JSON文件

```python
import json

student = {
    "name": "Lingersofe",
    "grade": "大一",
    "direction": "AI Agent / RAG",
    "skills": ["Python", "Git", "Markdown"]
}

with open("output/student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, ensure_ascii=False, indent=4)

print("JSON 写入完成！")
```

重点看
```python
ensure_ascii=False
```

作用是让中文正常显示，而不是变成 Unicode 编码

```python
indent=4
```

作用是让 JSON 文件格式更好看。

---

## 六.读取CSV文件

CSV 类似表格文件，常用于保存结构化数据。

在`data`中新建

```text
students.csv
```

写入：
```csv
name,grade,direction
Lingersofe,大一,AI Agent
Tom,大二,Backend
Alice,大三,Machine Learning
```

然后在main中写

```python
import csv

file_path = "data/students.csv"

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["grade"], row["direction"])
```

`csv.DictReader()` 会把每一行转换成字典，例如：

```python
    "name": "Lingersofe",
    "grade": "大一",
    "direction": "AI Agent"
```

## 七.异常处理try-except

实际开发中，文件可能不存在、路径可能写错、JSON 格式可能错误，所以你要学会处理异常。

例如：

```python
file_path = "data/not_exist.txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("文件不存在，请检查文件路径。")
```

再例如JSON格式错误
```python
import json

file_path = "data/qa_data.json"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    print(data)

except FileNotFoundError:
    print("文件不存在，请检查路径。")

except json.JSONDecodeError:
    print("JSON 文件格式错误，请检查是否缺少逗号、引号或括号。")
```

这部分非常重要，因为以后做 AI 项目时，经常会遇到：

```text
文件不存在
API Key 不存在
接口请求失败
JSON 解析失败
模型返回格式不对
```

### 有关try-except的用法

基本格式：
```python
try:
    可能出错的代码
except 错误类型:
    出错后的处理代码
```
- 这里的错误类型一般是系统报告出来的错误

- 当代码出错时，不会直接崩溃，而是会输出except里的内容

真实项目中，很多事情不是你能完全控制的

比如

| 场景      | 可能出现的问题          |
| ------- | ---------------- |
| 读取文件    | 文件不存在、路径写错、编码错误  |
| 读取 JSON | JSON 文件为空、格式错误   |
| 调用 API  | 网络失败、接口超时、返回格式错误 |
| 读取用户输入  | 用户输入了不合法内容       |
| 处理字典    | 缺少某个字段           |
| 数学计算    | 除数为 0            |


如果不用 `try-except`，只要出现一个错误，程序就停止。

如果使用 `try-except`，程序可以给出提示，甚至继续运行。

一旦 `try` 中某一行出错，后面的 `try` 代码就不会继续执行，而是直接跳到对应的 `except`。

- `try-except`还有更完整的写法

```python
try:
    可能出错的代码

except 某种错误:
    出错时执行

else:
    没有出错时执行

finally:
    无论是否出错都执行
```

- `except Exception`能捕获所有异常，但在初学阶段不建议这么做，可能会掩盖真实的问题，更推荐一个`try`后面跟多个`except`能更好的发现问题

```python
try:
    ...

except FileNotFoundError:
    print("文件不存在，请检查路径。")

except json.JSONDecodeError:
    print("JSON 格式错误，请检查文件内容。")

except KeyError as error:
    print(f"缺少字段：{error}")

```

---

## 今日综合小项目 JSON 问答转 Markdown

今天最重要的小项目是：

```text
读取 qa_data.json
→ 提取 question 和 answer
→ 生成 qa_notes.md
```

这个练习非常贴近后面的 RAG 文档处理。

1. 创建json_to_markdown.py

```python
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
```

- 对代码的重点稍作解释：

1. enumerate的作用
```python
for index, item in enumerate(qa_list, start=1):
        question = item["question"]
        answer = item["answer"]
```

其中的`enumerate`的作用是给每一个问题前加一个编号，`start`意思是从1开始

2. join() 可以把列表里的字符串拼接起来。
```python
"\n".join(lines)
```

例如：
```python
lines = ["第一行", "第二行", "第三行"]

content = "\n".join(lines)

print(content)
```

输出:
```text
第一行
第二行
第三行
```

`"\n".join(lines)`意思是用换行符把 lines 里面的每一行连接起来