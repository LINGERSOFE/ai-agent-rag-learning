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