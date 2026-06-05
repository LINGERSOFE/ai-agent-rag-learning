# 第二天学习（python基础语法）
鉴于之前已经有点python基础，便制作一点零散的知识点

---

## 一.查看变量类型
输入
```python
name="Lingersofe"
print(type(name))
```
输出
```text
<class 'str'>
```
---

## 字符串 str

1. 基本操作

- 输入

```python
text = "Python is useful for AI Agent"

print(text)
print(len(text))
print(text.lower())
print(text.upper())
print(text.replace("Python", "Java"))
```

- 输出

```text
Python is useful for AI Agent
29
python is useful for ai agent
PYTHON IS USEFUL FOR AI AGENT
Java is useful for AI Agent
```

| 写法                   | 作用      |
| -------------------- | ------- |
| `len(text)`          | 获取字符串长度 |
| `text.lower()`       | 转成小写    |
| `text.upper()`       | 转成大写    |
| `text.replace(a, b)` | 替换内容（前旧后新）    |

2. 字符串切分

- 输入
```python
sentence = "Python is useful for AI Agent"
words = sentence.split()

print(words)
```

- 输出

```text
['Python', 'is', 'useful', 'for', 'AI', 'Agent']
```

**`split`词频统计就会用到**


3. f-string 格式化

- 推荐优先使用f-string

```python
name = "Lingersofe"
direction = "AI Agent"

print(f"我是{name}，我正在学习{direction}。")
```

比下面这种写法更清晰：
```python
print("我是" + name + "，我正在学习" + direction + "。")
```

输出相同
```text
我是Lingersofe，我正在学习AI Agent。
```

---

## 列表 list

1. 添加元素

```python
tasks = ["变量", "字符串", "列表"]

tasks.append("字典")

print(tasks)
```

2. 删除元素

```python
tasks = ["变量", "字符串", "列表", "字典"]

tasks.remove("字符串")

print(tasks)
```

3. 遍历列表

```python
tasks = ["变量", "字符串", "列表", "字典"]

for task in tasks:
    print("今天要学习：", task)
```

--- 

## 字典

字典用来保存“键值对”。非常适合保存结构化信息。
- 例如一个学生的信息
```python 
student = {
    "name": "Lingersofe",
    "grade": "大一",
    "target": "AI Agent 实习",
    "language": "Python"
}

print(student)
print(student["name"])
print(student["target"])
```

1. 添加和修改字典内容
```python
student = {
    "name": "Lingersofe",
    "grade": "大一"
}

student["target"] = "进入大公司实习"
student["grade"] = "大一暑假"

print(student)
```

2. 遍历字典
```python
student = {
    "name": "Lingersofe",
    "grade": "大一",
    "target": "AI Agent 实习"
}

for key, value in student.items():
    print(key, ":", value)
```


3. 字典再AI项目中的作用
- 做 Prompt 输出 JSON、处理 API 返回结果时，字典会非常常见
```python
job_info = {
    "岗位名称": "AI Agent 实习生",
    "技能要求": ["Python", "RAG", "Prompt", "LangChain"],
    "学习建议": "先做一个知识库问答项目"
}

print(job_info["技能要求"])
```

---

## 条件判断if
1.  `if` `elif` `else`

2. 判断列表中是否包含某个元素
```python
skills = ["Python", "Git", "Markdown"]

if "Python" in skills:
    print("已经开始学习 Python")
else:
    print("还需要补 Python")
```

---

## 循环 `for` `while`
1. `for`循环和`range()`
```python
tasks = ["变量", "字符串", "列表"]

for task in tasks:
    print(task)


for i in range(5):
    print(i)

```

2. `while `循环
```python
count = 1

while count <= 5:
    print("当前次数：", count)
    count += 1
```

## 函数
- 函数名后可加参数，最后可以返回一个值。
```python
def functionname()
pass
```

## 小项目：读取文档中文字并进行词频统计

1. 创建 `sample.txt`
2. 创建` word_count.py`
3. 
| 函数                 | 作用         |
| ------------------ | ---------- |
| `read_file()`      | 读取文本文件     |
| `clean_text()`     | 清洗文本       |
| `count_words()`    | 统计词频       |
| `show_top_words()` | 展示前 N 个高频词 |
| `main()`           | 组织整个程序流程   |

- 以后做 RAG 时，也会经历类似流程：
```text
读取文档
→ 清洗文本
→ 切分文本
→ 统计或向量化
→ 检索
→ 输出结果
```