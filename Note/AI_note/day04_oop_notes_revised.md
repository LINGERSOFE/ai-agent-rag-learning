# Day 04：Python 面向对象基础 OOP

## 今日学习目标

今天主要学习 Python 面向对象基础，也就是 OOP（Object-Oriented Programming）。

本次学习内容包括：

- 理解类 `class`
- 理解对象 `object`
- 理解 `self`
- 理解 `__init__` 构造函数
- 理解实例属性和实例方法
- 理解封装思想
- 完成 `DocumentLoader` 文档加载器小项目
- 进行进阶训练：支持 JSON、读取文件信息、统计文本长度

---

## 一、类和对象的基本概念

类可以理解为“图纸”，对象可以理解为“根据图纸造出来的具体东西”。

例如：

```text
类：学生
对象：student1、student2、student3
```

类可以规定对象具有哪些数据和行为。

例如学生可以有：

```text
数据：姓名、年级、专业
行为：自我介绍、学习、提交作业
```

### 示例代码

```python
class Student:
    def introduce(self):
        print("我是一名学生。")


student1 = Student()
student1.introduce()
```

### 输出结果

```text
我是一名学生。
```

### 代码说明

| 代码 | 作用 |
|---|---|
| `class Student:` | 定义一个 `Student` 类 |
| `def introduce(self):` | 定义类中的方法 |
| `student1 = Student()` | 创建一个 `Student` 对象 |
| `student1.introduce()` | 调用对象的方法 |

---

## 二、`self` 是什么

先看这段代码：

```python
class Student:
    def introduce(self):
        print("我是一名学生。")


student1 = Student()
student1.introduce()
```

其中：

```python
def introduce(self):
```

里面的 `self` 可以理解为：

```text
当前这个对象自己。
```

当执行：

```python
student1.introduce()
```

时，`self` 就代表 `student1`。

初学阶段只需要记住：

```text
在类里面定义实例方法时，第一个参数通常都要写 self。
```

注意：调用方法时不需要手动传入 `self`，Python 会自动传。

也就是说：

```python
student1.introduce()
```

并不需要写成：

```python
student1.introduce(student1)
```

---

## 三、`__init__` 构造函数

如果希望每个学生对象都有自己的名字和年级，就可以使用 `__init__` 构造函数。

### 示例代码

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print(f"我是{self.name}，现在是{self.grade}学生。")


student1 = Student("Lingersofe", "大一")
student1.introduce()
```

### 输出结果

```text
我是Lingersofe，现在是大一学生。
```

### 代码说明

```python
def __init__(self, name, grade):
```

`__init__` 是构造函数，创建对象时会自动执行。

例如：

```python
student1 = Student("Lingersofe", "大一")
```

这行代码创建对象时，会自动把：

```text
name = "Lingersofe"
grade = "大一"
```

传给 `__init__`。

然后：

```python
self.name = name
self.grade = grade
```

表示把传进来的 `name` 和 `grade` 保存到当前对象身上。

因此，`student1` 拥有了：

```python
student1.name
student1.grade
```

可以这样访问：

```python
print(student1.name)
print(student1.grade)
```

---

## 四、实例属性和实例方法

### 1. 实例属性

实例属性就是对象自己的数据。

在下面这段代码中：

```python
self.name = name
self.grade = grade
```

`self.name` 和 `self.grade` 就是实例属性。

不同对象可以有不同的属性值。

```python
student1 = Student("Lingersofe", "大一")
student2 = Student("Tom", "大二")

student1.introduce()
student2.introduce()
```

输出：

```text
我是Lingersofe，现在是大一学生。
我是Tom，现在是大二学生。
```

### 2. 实例方法

实例方法就是对象可以执行的行为。

例如：

```python
def introduce(self):
    print(f"我是{self.name}，现在是{self.grade}学生。")
```

这个方法可以使用对象自己的属性：

```python
self.name
self.grade
```

### 3. 一句话总结

```text
属性：对象有什么。
方法：对象能做什么。
```

例如：

```text
学生对象：
属性：姓名、年级
方法：自我介绍
```

---

## 五、为什么要使用类

之前写文件读取时，可以使用普通函数：

```python
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
```

这种写法没有问题，适合简单任务。

但是以后如果要处理很多类型的文档，例如：

```text
TXT
Markdown
JSON
CSV
PDF
Word
```

并且每种文件有不同的读取方式，如果全部用普通函数，代码会越来越乱。

这时可以用类来封装文档读取逻辑：

```python
loader = DocumentLoader("data/sample.txt")
content = loader.load()
```

这样就更像是：

```text
一个文档加载器对象，负责读取某个文件。
```

---

## 六、面向对象的核心思想：封装

今天最重要的不是背代码，而是理解“封装”。

之前可能这样写：

```python
content = read_file("data/sample.txt")
```

现在可以这样写：

```python
loader = DocumentLoader("data/sample.txt")
content = loader.load()
```

区别是：

```text
普通函数：适合简单任务。
类：适合把一组相关的数据和行为封装到一起。
```

在 `DocumentLoader` 中：

```text
数据：file_path
行为：check_exists、get_suffix、load、_load_text
```

面向对象最核心的思想可以概括为：

```text
对象 = 数据 + 行为
```

---

## 七、今日综合小项目：DocumentLoader 文档加载器

### 1. 项目目标

完成一个 `DocumentLoader` 类，用来读取 `.txt` 和 `.md` 文件。

项目效果：

```python
loader = DocumentLoader("data/sample.txt")
content = loader.load()
print(content)
```

### 2. 创建示例文件

在 `data` 文件夹中新建：

```text
sample.txt
```

写入：

```text
Python is useful for AI Agent.
RAG needs document processing.
This is a txt file.
```

再新建：

```text
note.md
```

写入：

```markdown
# Day 04 Note

This is a markdown file.

Python can read markdown as plain text.
```

### 3. 创建 `document_loader.py`

```python
from pathlib import Path


class DocumentLoader:
    """文档加载器：用于读取 txt 和 md 文件"""

    def __init__(self, file_path):
        """初始化方法，保存文件路径"""
        self.file_path = Path(file_path)

    def check_exists(self):
        """检查文件是否存在"""
        return self.file_path.exists()

    def get_suffix(self):
        """获取文件后缀名"""
        return self.file_path.suffix.lower()

    def load(self):
        """根据文件类型读取文件内容"""
        if not self.check_exists():
            raise FileNotFoundError(f"文件不存在：{self.file_path}")

        suffix = self.get_suffix()

        if suffix == ".txt":
            return self._load_text()

        if suffix == ".md":
            return self._load_text()

        raise ValueError(f"暂不支持该文件类型：{suffix}")

    def _load_text(self):
        """读取文本类文件"""
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.read()
```

### 4. 创建 `main.py`

```python
from document_loader import DocumentLoader


def main():
    file_paths = [
        "data/sample.txt",
        "data/note.md",
        "data/not_exist.pdf"
    ]

    for file_path in file_paths:
        print("=" * 50)
        print(f"正在读取：{file_path}")

        try:
            loader = DocumentLoader(file_path)
            content = loader.load()

            print("读取成功！")
            print("文件内容：")
            print(content)

        except FileNotFoundError as error:
            print("读取失败：文件不存在。")
            print("具体错误：", error)

        except ValueError as error:
            print("读取失败：文件类型不支持。")
            print("具体错误：", error)


if __name__ == "__main__":
    main()
```

### 5. 运行结果

运行 `main.py` 后，可能会出现：

```text
==================================================
正在读取：data/sample.txt
读取成功！
文件内容：
Python is useful for AI Agent.
RAG needs document processing.
This is a txt file.

==================================================
正在读取：data/note.md
读取成功！
文件内容：
# Day 04 Note

This is a markdown file.

Python can read markdown as plain text.

==================================================
正在读取：data/not_exist.pdf
读取失败：文件不存在。
具体错误： 文件不存在：data\not_exist.pdf
```

---

## 八、重点解释 `DocumentLoader`

### 1. `__init__`

```python
def __init__(self, file_path):
    """初始化方法，保存文件路径"""
    self.file_path = Path(file_path)
```

`__init__` 会在创建对象时自动执行。

例如：

```python
loader = DocumentLoader("data/sample.txt")
```

这行代码会自动调用 `__init__`，并把 `"data/sample.txt"` 传给 `file_path`。

```python
self.file_path = Path(file_path)
```

表示把路径保存到对象上。

`Path(file_path)` 来自：

```python
from pathlib import Path
```

`Path` 比普通字符串路径更方便，比如可以：

- 检查文件是否存在
- 获取文件后缀名
- 拼接路径

### 2. `check_exists()`

```python
def check_exists(self):
    """检查文件是否存在"""
    return self.file_path.exists()
```

作用是检查文件是否存在。

如果文件存在，返回：

```python
True
```

如果文件不存在，返回：

```python
False
```

注意：Python 中布尔值首字母要大写，应该写 `True` 和 `False`，不能写 `true` 和 `false`。

### 3. `get_suffix()`

```python
def get_suffix(self):
    """获取文件后缀名"""
    return self.file_path.suffix.lower()
```

作用是获取文件后缀名，并统一转成小写。

例如：

```text
data/sample.txt → .txt
data/note.md → .md
data/test.PDF → .pdf
```

其中：

```python
.lower()
```

可以避免 `.TXT`、`.Md`、`.PDF` 这类大小写不统一的问题。

### 4. `load()`

```python
def load(self):
    """根据文件类型读取文件内容"""
    if not self.check_exists():
        raise FileNotFoundError(f"文件不存在：{self.file_path}")

    suffix = self.get_suffix()

    if suffix == ".txt":
        return self._load_text()

    if suffix == ".md":
        return self._load_text()

    raise ValueError(f"暂不支持该文件类型：{suffix}")
```

执行逻辑：

```text
先检查文件是否存在
→ 如果不存在，主动抛出 FileNotFoundError
→ 如果存在，获取文件后缀
→ 如果是 .txt，按文本读取
→ 如果是 .md，也按文本读取
→ 其他类型，主动抛出 ValueError
```

### 5. `raise` 的作用

```python
raise FileNotFoundError(f"文件不存在：{self.file_path}")
```

和：

```python
raise ValueError(f"暂不支持该文件类型：{suffix}")
```

`raise` 的意思是：

```text
主动抛出一个错误。
```

为什么要主动抛出错误？

因为当文件不存在或文件类型不支持时，程序不应该假装正常，而应该明确告诉外部：

```text
这里出问题了，需要处理。
```

然后在 `main.py` 里用 `try-except` 捕获：

```python
except FileNotFoundError as error:
    print("读取失败：文件不存在。")
    print("具体错误：", error)
```

这样程序不会直接崩溃，而是输出更友好的提示。

### 6. `_load_text()`

```python
def _load_text(self):
    """读取文本类文件"""
    with open(self.file_path, "r", encoding="utf-8") as file:
        return file.read()
```

这个方法负责真正读取文本内容。

方法名前面加下划线 `_`：

```python
_load_text
```

表示它更像是类内部使用的辅助方法，不建议外部直接调用。

推荐这样用：

```python
loader.load()
```

不推荐这样用：

```python
loader._load_text()
```

---

## 九、进阶训练

### 1. 支持 `.json`

在 `document_loader.py` 顶部添加：

```python
import json
```

然后在类中增加方法：

```python
def _load_json(self):
    """读取 JSON 文件"""
    with open(self.file_path, "r", encoding="utf-8") as file:
        return json.load(file)
```

在 `load()` 中添加：

```python
if suffix == ".json":
    return self._load_json()
```

### 2. 支持读取文件基本信息

在类中添加方法：

```python
def get_info(self):
    """获取文件基本信息"""
    return {
        "file_path": str(self.file_path),
        "suffix": self.get_suffix(),
        "exists": self.check_exists()
    }
```

在 `main.py` 中调用：

```python
print(loader.get_info())
```

### 3. 统计文本长度

在类中添加方法：

```python
def count_characters(self):
    """统计文件字符数"""
    content = self.load()
    return len(content)
```

然后在 `main.py` 中输出：

```python
print("字符数：", loader.count_characters())
```

注意：这个方法适合统计 `.txt` 和 `.md` 读取出来的字符串长度。如果读取的是 JSON，`self.load()` 返回的可能是字典或列表，`len(content)` 表示元素数量，不一定是字符数。

---

## 十、今日学习总结

今天学习了 Python 面向对象基础，包括：

- 类 `class`
- 对象 `object`
- `self`
- `__init__` 构造函数
- 实例属性
- 实例方法
- 封装思想
- `raise` 主动抛出异常
- 使用类封装文件读取逻辑

今天完成了一个 `DocumentLoader` 文档加载器，用类的方式封装了文件路径、文件是否存在检查、文件后缀判断和文本读取逻辑。

这为后续学习 RAG 文档解析打下了基础，因为以后可以继续扩展这个类，让它支持：

```text
TXT
Markdown
JSON
CSV
PDF
Word
```

---

## 十一、今日检查清单

- [x] 理解类 `class`
- [x] 理解对象 `object`
- [x] 理解 `self`
- [x] 理解 `__init__`
- [x] 理解实例属性
- [x] 理解实例方法
- [x] 理解封装思想
- [x] 完成 `Student` 示例
- [x] 完成 `DocumentLoader` 类
- [x] 能读取 `.txt` 文件
- [x] 能读取 `.md` 文件
- [x] 理解 `Path(file_path)`
- [x] 理解 `raise`
- [x] 理解 `_load_text()` 前面下划线的含义
- [x] 完成进阶训练思路整理
