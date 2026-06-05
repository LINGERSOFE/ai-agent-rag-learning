# Day 02：Python 基础语法

## 今日学习目标

今天主要复习和巩固 Python 基础语法，为后续学习文件处理、API 调用、RAG 文档解析和 AI Agent 开发打基础。

本次学习内容包括：

- 查看变量类型
- 字符串 `str`
- 列表 `list`
- 字典 `dict`
- 条件判断 `if`
- 循环 `for` / `while`
- 函数 `function`
- 词频统计小项目

---

## 一、查看变量类型

Python 中可以使用 `type()` 查看变量的数据类型。

### 示例代码

```python
name = "Lingersofe"
print(type(name))
```

### 输出结果

```text
<class 'str'>
```

### 说明

这里的 `str` 表示字符串类型。

常见基础类型如下：

| 类型 | 示例 | 说明 |
|---|---|---|
| `str` | `"Python"` | 字符串 |
| `int` | `18` | 整数 |
| `float` | `3.14` | 小数 |
| `bool` | `True` / `False` | 布尔值 |

---

## 二、字符串 `str`

字符串是 Python 中非常重要的数据类型。以后做 AI Agent、RAG 和 Prompt 工程时，经常要处理大量文本，因此字符串操作是基础能力。

---

### 1. 字符串基本操作

### 示例代码

```python
text = "Python is useful for AI Agent"

print(text)
print(len(text))
print(text.lower())
print(text.upper())
print(text.replace("Python", "Java"))
```

### 输出结果

```text
Python is useful for AI Agent
29
python is useful for ai agent
PYTHON IS USEFUL FOR AI AGENT
Java is useful for AI Agent
```

### 常用方法

| 写法 | 作用 |
|---|---|
| `len(text)` | 获取字符串长度 |
| `text.lower()` | 将字符串转成小写 |
| `text.upper()` | 将字符串转成大写 |
| `text.replace(a, b)` | 将字符串中的 `a` 替换成 `b` |

---

### 2. 字符串切分

### 示例代码

```python
sentence = "Python is useful for AI Agent"
words = sentence.split()

print(words)
```

### 输出结果

```text
['Python', 'is', 'useful', 'for', 'AI', 'Agent']
```

### 说明

`split()` 默认按照空格、换行等空白字符切分字符串。

这个方法在词频统计、文本清洗、RAG 文档切分中都会用到。

例如：

```python
text = "Python is useful"
words = text.split()
print(words)
```

输出：

```text
['Python', 'is', 'useful']
```

---

### 3. f-string 格式化

推荐优先使用 f-string 进行字符串格式化。

### 示例代码

```python
name = "Lingersofe"
direction = "AI Agent"

print(f"我是{name}，我正在学习{direction}。")
```

### 输出结果

```text
我是Lingersofe，我正在学习AI Agent。
```

相比字符串拼接：

```python
print("我是" + name + "，我正在学习" + direction + "。")
```

f-string 更清晰，也更适合以后写复杂输出。

---

## 三、列表 `list`

列表用于保存一组有顺序的数据。

例如，今天要学习的内容可以保存为一个列表：

```python
tasks = ["变量", "字符串", "列表", "字典", "条件判断", "循环", "函数"]
```

列表中的元素可以通过下标访问。

```python
print(tasks[0])
print(tasks[1])
print(tasks[-1])
```

输出：

```text
变量
字符串
函数
```

注意：

```text
Python 的下标从 0 开始。
```

---

### 1. 添加元素

使用 `append()` 可以在列表末尾添加元素。

```python
tasks = ["变量", "字符串", "列表"]

tasks.append("字典")

print(tasks)
```

输出：

```text
['变量', '字符串', '列表', '字典']
```

---

### 2. 删除元素

使用 `remove()` 可以删除指定元素。

```python
tasks = ["变量", "字符串", "列表", "字典"]

tasks.remove("字符串")

print(tasks)
```

输出：

```text
['变量', '列表', '字典']
```

注意：如果要删除的元素不存在，程序会报错。

---

### 3. 遍历列表

使用 `for` 循环可以遍历列表中的每个元素。

```python
tasks = ["变量", "字符串", "列表", "字典"]

for task in tasks:
    print("今天要学习：", task)
```

输出：

```text
今天要学习： 变量
今天要学习： 字符串
今天要学习： 列表
今天要学习： 字典
```

---

### 4. 带编号遍历列表

使用 `enumerate()` 可以同时获得编号和元素。

```python
tasks = ["变量", "字符串", "列表", "字典"]

for index, task in enumerate(tasks, start=1):
    print(f"第 {index} 个任务：{task}")
```

输出：

```text
第 1 个任务：变量
第 2 个任务：字符串
第 3 个任务：列表
第 4 个任务：字典
```

---

## 四、字典 `dict`

字典用于保存“键值对”数据，非常适合保存结构化信息。

### 示例代码

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

### 输出结果

```text
{'name': 'Lingersofe', 'grade': '大一', 'target': 'AI Agent 实习', 'language': 'Python'}
Lingersofe
AI Agent 实习
```

---

### 1. 添加和修改字典内容

```python
student = {
    "name": "Lingersofe",
    "grade": "大一"
}

student["target"] = "进入大公司实习"
student["grade"] = "大一暑假"

print(student)
```

输出：

```text
{'name': 'Lingersofe', 'grade': '大一暑假', 'target': '进入大公司实习'}
```

说明：

- 如果键不存在，就是新增。
- 如果键已经存在，就是修改。

---

### 2. 遍历字典

```python
student = {
    "name": "Lingersofe",
    "grade": "大一",
    "target": "AI Agent 实习"
}

for key, value in student.items():
    print(key, ":", value)
```

输出：

```text
name : Lingersofe
grade : 大一
target : AI Agent 实习
```

---

### 3. 字典在 AI 项目中的作用

以后处理 API 返回结果、模型输出 JSON、RAG 检索结果时，经常会用到字典。

例如：

```python
job_info = {
    "岗位名称": "AI Agent 实习生",
    "技能要求": ["Python", "RAG", "Prompt", "LangChain"],
    "学习建议": "先做一个知识库问答项目"
}

print(job_info["技能要求"])
```

---

## 五、条件判断 `if`

条件判断可以让程序根据不同情况执行不同代码。

### 示例代码

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

### 输出结果

```text
及格
```

### 说明

| 写法 | 作用 |
|---|---|
| `if` | 如果条件成立，就执行 |
| `elif` | 否则如果另一个条件成立，就执行 |
| `else` | 以上条件都不成立时执行 |

---

### 判断列表中是否包含某个元素

```python
skills = ["Python", "Git", "Markdown"]

if "Python" in skills:
    print("已经开始学习 Python")
else:
    print("还需要补 Python")
```

输出：

```text
已经开始学习 Python
```

---

## 六、循环

循环用于重复执行一段代码。

---

### 1. `for` 循环

`for` 循环适合遍历列表、字符串、字典等数据。

```python
tasks = ["变量", "字符串", "列表"]

for task in tasks:
    print(task)
```

输出：

```text
变量
字符串
列表
```

---

### 2. `range()`

`range()` 常用于生成数字序列。

```python
for i in range(5):
    print(i)
```

输出：

```text
0
1
2
3
4
```

注意：

```text
range(5) 生成的是 0 到 4，不包括 5。
```

---

### 3. `while` 循环

`while` 循环会在条件成立时一直执行。

```python
count = 1

while count <= 5:
    print("当前次数：", count)
    count += 1
```

输出：

```text
当前次数： 1
当前次数： 2
当前次数： 3
当前次数： 4
当前次数： 5
```

初学阶段可以先重点掌握 `for` 循环。

---

## 七、函数 `function`

函数可以把一段代码封装起来，方便重复使用。

---

### 1. 最简单的函数

```python
def say_hello():
    print("你好，今天开始学习 Python 基础语法！")

say_hello()
```

输出：

```text
你好，今天开始学习 Python 基础语法！
```

---

### 2. 带参数的函数

```python
def greet(name):
    print(f"你好，{name}！")

greet("Lingersofe")
```

输出：

```text
你好，Lingersofe！
```

---

### 3. 带返回值的函数

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

输出：

```text
8
```

---

### 4. 函数的意义

函数的作用是：

```text
把一段重复使用的逻辑封装起来，让代码更清晰、更容易维护。
```

例如词频统计小项目中，可以把程序拆成：

```text
读取文件
→ 清洗文本
→ 统计词频
→ 排序输出
```

每一步都写成一个函数。

---

## 八、词频统计小项目

### 项目目标

读取 `sample.txt` 文件，统计每个单词出现的次数，并输出出现次数最多的前 10 个词。

---

### 项目流程

```text
读取文本
→ 清洗文本
→ 切分单词
→ 统计词频
→ 排序输出
```

---

### 示例代码

```python
def read_file(file_path):
    """读取文本文件内容"""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def clean_text(text):
    """清洗文本，把大写转小写，并去掉常见标点"""
    text = text.lower()

    punctuation = [".", ",", "!", "?", ":", ";"]
    for symbol in punctuation:
        text = text.replace(symbol, "")

    return text


def count_words(text):
    """统计单词出现次数"""
    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def show_top_words(word_count, top_n=10):
    """输出出现次数最多的单词"""
    sorted_words = sorted(
        word_count.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print(f"出现次数最多的前 {top_n} 个词：")

    for word, count in sorted_words[:top_n]:
        print(f"{word}: {count}")


def main():
    file_path = "sample.txt"

    text = read_file(file_path)
    cleaned_text = clean_text(text)
    word_count = count_words(cleaned_text)

    show_top_words(word_count, top_n=10)


if __name__ == "__main__":
    main()
```

---

### 核心理解

这段代码的数据变化过程是：

```text
sample.txt 文件内容
→ read_file() 读成字符串
→ clean_text() 转小写、去标点
→ split() 切成单词列表
→ count_words() 用字典统计次数
→ sorted() 按次数排序
→ show_top_words() 输出前 10 个
```

最核心的一段是：

```python
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
```

它的意思是：

```text
如果单词已经出现过，次数加 1；
如果单词第一次出现，就把次数设为 1。
```

---

## 九、今日学习总结

今天复习并整理了 Python 基础语法，包括变量类型、字符串、列表、字典、条件判断、循环和函数。

其中最重要的内容是：

- 字符串适合处理文本。
- 列表适合保存一组有顺序的数据。
- 字典适合保存键值对，也非常适合做统计。
- 条件判断可以让程序根据不同情况执行不同逻辑。
- 循环可以重复处理数据。
- 函数可以把代码拆分成更清晰的模块。
- 词频统计小项目综合使用了文件读取、字符串处理、列表、字典、循环和函数。

今天的小项目虽然简单，但它和后续 RAG 学习有联系：

```text
词频统计：
读取文本 → 清洗文本 → 切分文本 → 统计结果

RAG 项目：
读取文档 → 清洗文本 → 切分文本 → 向量化 → 检索 → 回答问题
```

---

## 十、今日检查清单

- [x] 学会使用 `type()` 查看变量类型
- [x] 学会字符串常用方法
- [x] 学会使用 `split()` 切分字符串
- [x] 学会 f-string 格式化
- [x] 学会列表的添加、删除和遍历
- [x] 学会字典的创建、修改和遍历
- [x] 理解条件判断 `if / elif / else`
- [x] 理解 `for` 循环和 `while` 循环
- [x] 理解函数的基本写法
- [x] 完成词频统计小项目
