# 我的第一篇 Markdown 笔记

## 今天学习内容

- Python 安装
- VS Code 使用
- Markdown 基础语法


## 代码示例

```python
print("Hello Markdown")
```

## 打开预览
右键点开项目名，点击预览，英文为preview

或者在 VS Code 中按：

Ctrl + Shift + V

## 基本语法


**加粗文字**

*斜体文字*

***这是加粗加斜体文字***

~~这是被删除的文字~~

- 第一项
- 第二项
- 第三项


1. 第一步
2. 第二步
3. 第三步

## 代码块的书写

- 使用三个反引号接上编程语言，再用三个反引号结尾（调取bash时也是这样书写）
```c
#include <stdio.h>

int main() {
    printf("Hello World");
    return 0;
}
```

- 行内引用
使用 `printf()` 可以输出内容。此时在预览中printf() 会变成一个单独模块


## 表格
| 名称 | 用途 |
|---|---|
| Python | 编程语言 |
| VS Code | 代码编辑器 |
| Markdown | 写文档 |

## 引用
> 这是一段引用内容。
- 多层应用
> 第一层引用
>> 第二层引用
>>> 第三层引用

## 链接
[点击访问百度](https://www.baidu.com)


## 图片（比链接前多一个！）
![图片说明](图片地址)


## 任务列表（GitHub、VS Code、Typora 等工具支持任务列表）
- [ ] 安装 Python
- [ ] 安装 VS Code
- [ ] 学习 Markdown
- [ ] 完成 README

## 数学公式
- 行内公式
一元二次方程公式为 $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$。
- 独立公式
$$
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

## 转义字符

\# 这不是标题
\*\*这不是加粗\*\*
