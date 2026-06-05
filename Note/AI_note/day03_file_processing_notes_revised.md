# Day 03：Python 文件处理

## 今日学习目标

今天主要学习 Python 文件处理能力，包括读取文件、写入文件、处理 JSON / CSV / Markdown，并理解异常处理 `try-except`。

这部分内容是后续学习 RAG 知识库和 AI Agent 项目的基础，因为 RAG 的第一步通常就是：

```text
读取文档
→ 解析内容
→ 清洗文本
→ 转换格式
→ 存入知识库
```

---

## 一、创建项目

### 1. 创建项目目录

在 PyCharm 中创建 Day 03 项目，项目名称可以设置为：

```text
day03_file_processing
```

建议项目结构如下：

```text
day03_file_processing/
├── data/
│   ├── sample.txt
│   ├── qa_data.json
│   └── students.csv
├── output/
│   ├── result.txt
│   ├── student.json
│   └── qa_notes.md
├── main.py
├── json_to_markdown.py
├── README.md
└── requirements.txt
```

其中：

| 文件夹 | 作用 |
|---|---|
| `data/` | 存放输入文件 |
| `output/` | 存放程序生成的输出文件 |

---

## 二、读取 TXT 文件

### 1. 创建示例文件

在 `data` 文件夹中新建：

```text
sample.txt
```

写入以下内容：

```text
Python is useful for AI Agent.
RAG needs document processing.
File processing is the first step of building a knowledge base.
```

---

### 2. 读取整个 TXT 文件

在 `main.py` 中写入：

```python
file_path = "data/sample.txt"

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

### 代码说明

| 部分 | 作用 |
|---|---|
| `open()` | 打开文件 |
| `"r"` | read，读取模式 |
| `encoding="utf-8"` | 按 UTF-8 编码读取，避免中文乱码 |
| `with` | 自动关闭文件，不需要手动调用 `file.close()` |
| `file.read()` | 一次性读取文件全部内容 |

---

### 3. 逐行读取文件

有时文件很长，不适合一次性全部读取，可以逐行读取：

```python
file_path = "data/sample.txt"

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

### 说明

`line.strip()` 的作用是去掉每一行前后的空格和换行符。

注意：这里是 `line.strip()`，需要加括号，因为它是一个方法调用。

---

## 三、写入 TXT 文件

在 `main.py` 中写入：

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

运行后，程序会在 `output` 文件夹中创建 `result.txt` 文件。

---

### 文件打开模式

| 模式 | 作用 |
|---|---|
| `"r"` | 读取文件 |
| `"w"` | 写入文件，如果文件已存在，会覆盖原内容 |
| `"a"` | 追加写入，不会覆盖原内容 |

---

### 追加写入示例

```python
with open("output/result.txt", "a", encoding="utf-8") as file:
    file.write("\n这是追加写入的新内容。")
```

说明：

```text
\n 表示换行。
```

---

## 四、读取 JSON 文件

JSON 是后面调用 API、处理大模型返回结果时非常常见的数据格式。

---

### 1. 创建 JSON 文件

在 `data` 文件夹中新建：

```text
qa_data.json
```

写入以下内容：

```json
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

---

### 2. 使用 Python 读取 JSON

在 `main.py` 中写入：

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

---

### 3. `json.load(file)` 的作用

`json.load(file)` 的意思是：

```text
从 JSON 文件中读取内容，并转换成 Python 可以处理的数据。
```

在这个例子中：

- JSON 最外层是 `[]`，所以读出来是 Python 列表 `list`。
- 每一条问答是 `{}`，所以每条问答读出来是 Python 字典 `dict`。

也就是：

```text
JSON 数组 []  → Python 列表 list
JSON 对象 {}  → Python 字典 dict
```

---

### 4. JSON 常见格式要求

JSON 格式比较严格，需要注意：

| 规则 | 说明 |
|---|---|
| 字符串必须使用英文双引号 | `"question"` 正确，`'question'` 错误 |
| 每个键值对之间要有英文逗号 | `,` |
| 不能使用中文逗号 | `，` 是错误的 |
| 最后一项后面不要多加逗号 | JSON 不允许尾随逗号 |
| 文件不能为空 | 空 JSON 文件会解析失败 |

---

## 五、写入 JSON 文件

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

---

### 重点参数说明

```python
ensure_ascii=False
```

作用是让中文正常显示，而不是变成 Unicode 编码。

```python
indent=4
```

作用是让 JSON 文件格式更清晰、更容易阅读。

---

## 六、读取 CSV 文件

CSV 类似表格文件，常用于保存结构化数据。

---

### 1. 创建 CSV 文件

在 `data` 文件夹中新建：

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

---

### 2. 使用 Python 读取 CSV

在 `main.py` 中写入：

```python
import csv

file_path = "data/students.csv"

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["grade"], row["direction"])
```

---

### 3. `csv.DictReader()` 的作用

`csv.DictReader()` 会把每一行转换成字典。

例如：

```python
{
    "name": "Lingersofe",
    "grade": "大一",
    "direction": "AI Agent"
}
```

这样就可以通过字段名读取数据：

```python
row["name"]
row["grade"]
row["direction"]
```

---

## 七、异常处理 `try-except`

实际开发中，文件可能不存在，路径可能写错，JSON 格式可能错误，所以需要学会异常处理。

`try-except` 的作用是：

```text
当程序可能出错时，不让程序直接崩溃，而是捕获错误，并给出可控的处理方式。
```

---

### 1. 基本格式

```python
try:
    可能出错的代码
except 错误类型:
    出错后的处理代码
```

说明：

- `try` 中放可能出错的代码。
- `except` 中放出错后的处理方式。
- 一旦 `try` 中某一行出错，后面的 `try` 代码不会继续执行，而是跳到对应的 `except`。

---

### 2. 文件不存在异常

```python
file_path = "data/not_exist.txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("文件不存在，请检查文件路径。")
```

---

### 3. JSON 格式错误异常

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

---

### 4. 常见异常类型

| 场景 | 可能出现的问题 | 常见异常 |
|---|---|---|
| 读取文件 | 文件不存在、路径写错 | `FileNotFoundError` |
| 读取 JSON | JSON 文件为空、格式错误 | `json.JSONDecodeError` |
| 读取用户输入 | 用户输入了不合法内容 | `ValueError` |
| 处理字典 | 缺少某个字段 | `KeyError` |
| 数学计算 | 除数为 0 | `ZeroDivisionError` |

---

### 5. 完整结构：`try-except-else-finally`

`try-except` 还有更完整的写法：

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

含义：

| 结构 | 含义 |
|---|---|
| `try` | 尝试执行 |
| `except` | 出错时执行 |
| `else` | 没有出错时执行 |
| `finally` | 无论是否出错都会执行 |

---

### 6. 不建议滥用 `except Exception`

`except Exception` 可以捕获几乎所有异常，但初学阶段不建议经常这样写。

原因是它可能掩盖真正的问题。

不推荐写法：

```python
try:
    ...
except Exception:
    print("出错了")
```

更推荐写法：

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

这样可以更清楚地知道程序到底哪里出了问题。

---

## 八、今日综合小项目：JSON 问答转 Markdown

### 1. 项目目标

今天最重要的小项目是：

```text
读取 qa_data.json
→ 提取 question 和 answer
→ 生成 qa_notes.md
```

这个练习非常贴近后面的 RAG 文档处理。

---

### 2. 创建 `json_to_markdown.py`

```python
import json


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

    except FileNotFoundError:
        print("文件不存在，请检查 data/qa_data.json 是否存在。")

    except json.JSONDecodeError as error:
        print("JSON 格式错误，请检查 qa_data.json。")
        print("具体错误：", error)

    except KeyError as error:
        print(f"JSON 数据缺少字段：{error}")

    else:
        print(f"转换完成，文件已保存到：{output_path}")

    finally:
        print("程序运行结束。")


if __name__ == "__main__":
    main()
```

---

### 3. 运行程序

```powershell
python json_to_markdown.py
```

运行成功后，会在 `output` 文件夹中生成：

```text
qa_notes.md
```

---

## 九、小项目代码理解

### 1. `enumerate()` 的作用

```python
for index, item in enumerate(qa_list, start=1):
    question = item["question"]
    answer = item["answer"]
```

`enumerate()` 的作用是：

```text
遍历列表时，同时获得编号和元素。
```

其中：

```python
start=1
```

表示编号从 1 开始。如果没有 `start=1`，默认编号从 0 开始。

---

### 2. `lines.append()` 的作用

```python
lines.append("# Python 学习问答笔记")
```

`append()` 的作用是往列表末尾添加一个元素。

在这里，`lines` 是一个列表，用来一行一行保存 Markdown 内容。

---

### 3. `join()` 的作用

```python
"\n".join(lines)
```

`join()` 可以把列表里的字符串拼接起来。

例如：

```python
lines = ["第一行", "第二行", "第三行"]

content = "\n".join(lines)

print(content)
```

输出：

```text
第一行
第二行
第三行
```

`"\n".join(lines)` 的意思是：

```text
用换行符把 lines 里面的每一行连接起来。
```

---

### 4. `write_markdown()` 的作用

```python
def write_markdown(file_path, content):
    """写入 Markdown 文件"""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
```

这个函数的作用是：

```text
把生成好的 Markdown 文本写入 .md 文件。
```

其中：

- `file_path` 表示输出路径。
- `content` 表示要写入的 Markdown 文本。
- `"w"` 表示写入模式，如果文件已存在，会覆盖原内容。

---

## 十、今日学习总结

今天学习了 Python 文件处理，包括：

- 读取 TXT 文件
- 写入 TXT 文件
- 逐行读取文件
- 读取 JSON 文件
- 写入 JSON 文件
- 读取 CSV 文件
- 使用 `try-except` 处理异常
- 将 JSON 问答数据转换成 Markdown 文件

今天最重要的收获是理解了：

```text
外部文件可以通过 Python 读取进程序，
转换成字符串、列表、字典等数据结构，
再经过处理后输出成新的文件。
```

这个过程和后续 RAG 的学习非常相关：

```text
Day 03 文件处理：
读取文件 → 解析数据 → 转换格式 → 输出文件

后续 RAG 项目：
读取文档 → 清洗文本 → 文本切分 → 向量化 → 检索 → 生成回答
```

---

## 十一、今日检查清单

- [x] 创建 `day03_file_processing` 项目
- [x] 创建 `data/` 文件夹
- [x] 创建 `output/` 文件夹
- [x] 学会读取 TXT 文件
- [x] 学会逐行读取 TXT 文件
- [x] 学会写入 TXT 文件
- [x] 学会追加写入 TXT 文件
- [x] 学会读取 JSON 文件
- [x] 学会写入 JSON 文件
- [x] 学会读取 CSV 文件
- [x] 理解 `try-except`
- [x] 理解 `else` 和 `finally`
- [x] 完成 JSON 问答转 Markdown 小项目
- [x] 理解 `enumerate()` 和 `join()`
