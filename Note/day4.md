# 第四天笔记：Python 面向对象基础 OOP。

## 一、类的基本概念

类是图纸，对象是根据图纸造出来的具体东西。

```python
class Student:
    def introduce(self):
        print("我是一名学生。")


student1 = Student()
student1.introduce()
```

输出：
```text
我是一名学生。
```

## 二、`self`是什么

先看代码：
```python
class Student:
    def introduce(self):
        print("我是一名学生。")


student1 = Student()
student1.introduce()
```

`self`可以看成“当前这个对象自己”。

运行时，self 就代表 student1。

现在不需要把 self 想得太复杂，只要记住：

```python
类里面定义方法时，第一个参数通常都要写 self。
```

## 三、`__init__`构造函数

如果我们想让每个学生有自己的名字，就需要用 `__init__`。

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

输出：

```text
我是Lingersofe，现在是大一学生。
```

`__init__`是构造函数，创建对象时会自动执行。

在这段代码中，会把传进来的 name 和 grade 保存到当前对象身上。

使得`student1`拥有了

```python
student1.name
student1.grade
```

---

## 四、实例属性和实例方法

1. 实例属性

实例属性就是对象自己的数据。

上述代码中

```python
self.name
self.grade
```

就是实例属性

- 不同对象可以有不同属性值

2. 实例方法

实例方法就是对象可以做的事情。

比如：

```python
def introduce(self):
    print(f"我是{self.name}，现在是{self.grade}学生。")
```

这个方法可以使用对象自己的属性.

- 一句话概括：属性就是对象有什么，方法就是对象能干什么。


--- 

## 五、为什么要用类

之前写文件读取可能是这样：

```python
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
```
这没有问题

但以后要处理很多类型的的文档，比如

```text
TXT
Markdown
JSON
CSV
PDF
Word
```

并且每种文件有不同读取方式，如果全都用普通函数，代码会越来越乱。

这时可以用类来封装：

```python
loader = DocumentLoader("data/sample.txt")
content = loader.load()
```

这样看起来更像“一个文档加载器对象负责读取文件”。



## 六、今日综合小项目：DocumentLoader 文档加载器

1. 在`data`文件夹中创建

```text
sample.txt
```

写入：

```text
Python is useful for AI Agent.
RAG needs document processing.
This is a txt file.
```

再新建

```text
note.md
```

写入：

```markdown
# Day 04 Note

This is a markdown file.

Python can read markdown as plain text.
```

2. 创建 `document_loader.py`

写入：

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

3. 创建`main.py`

写入：

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

运行`main.py`，会出现：

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


## 七、重点解释 `DocumentLoader`

1. `__init__`

初始化，将路径保存到对象上，这个函数会自己执行。

`Path(file_path)` 来自：

```python
from pathlib import Path
```
它比普通字符串路径更方便，比如可以检查文件是否存在、获取后缀名


2. `check_exists`

```python
def check_exists(self):
    return self.file_path.exists()
```

检查文件是否存在，存在返回true，不存在返回false。

3. `get_suffix`

```python
def get_suffix(self):
    return self.file_path.suffix.lower()
```

作用是获取文件的后缀名。

**统一小写**


4. `load`

```python
def load(self):
    if not self.check_exists():
        raise FileNotFoundError(f"文件不存在：{self.file_path}")

    suffix = self.get_suffix()

    if suffix == ".txt":
        return self._load_text()

    if suffix == ".md":
        return self._load_text()

    raise ValueError(f"暂不支持该文件类型：{suffix}")
```

执行逻辑

```text
先检查文件是否存在
→ 如果不存在，主动抛出 FileNotFoundError
→ 如果存在，获取文件后缀
→ 如果是 .txt，按文本读取
→ 如果是 .md，也按文本读取
→ 其他类型，抛出 ValueError
```

5. `raise`的作用

意思是：主动抛出一个错误。

为什么要主动抛出错误？

因为文件不存在或文件类型不支持时，程序不应该假装正常，而应该明确告诉外部：

```text
这里出问题了，需要处理。
```


然后在`main.py` 里用 `try-except` 捕获：

```python
except FileNotFoundError as error:
    print("读取失败：文件不存在。")
```

6. `_load_text`

```python
def _load_text(self):
    with open(self.file_path, "r", encoding="utf-8") as file:
        return file.read()
```

这个方法负责真正读取文本内容。

方法名前面加 _：

```python
_load_text
```

表示它更像是类内部使用的辅助方法，不建议外部直接调用。

也就是说，更推荐这样用：

```python
loader.load()
```

而不是：

```python
loader._load_text()
```


----


## 八、核心思想

今天最重要的不是背代码，而是理解“封装”。

之前你可能这样写：

```python
content = read_file("data/sample.txt")
```

现在你可能这样写

```python
loader = DocumentLoader("data/sample.txt")
content = loader.load()
```

区别是O:

```text
普通函数：适合简单任务
类：适合把一组相关的数据和行为封装到一起
```

`DocumentLoader` 里封装了：

```text
数据：file_path
行为：check_exists、get_suffix、load、_load_text
```

这就是面向对象最核心的思想：

```text
对象 = 数据 + 行为
```

## 九、进阶训练

1. 支持`.json`

在`DocumentLoader`中添加

```python
import json
```

然后增加方法：

```python
def _load_json(self):
    """读取 JSON 文件"""
    with open(self.file_path, "r", encoding="utf-8") as file:
        return json.load(file)
```

在`load()`中添加

```python
if suffix == ".json":
    return self._load_json()
```

2. 支持读取文件基本信息

添加方法：

```python
def get_info(self):
    """获取文件基本信息"""
    return {
        "file_path": str(self.file_path),
        "suffix": self.get_suffix(),
        "exists": self.check_exists()
    }
```


在`main.py`中调用

```python
print(loader.get_info())
```

3. 统计文本长度

增加方法：

```python
def count_characters(self):
    """统计文件字符数"""
    content = self.load()
    return len(content)
```

然后在 `main.py`中输出：

```python
print("字符数：", loader.count_characters())
```

