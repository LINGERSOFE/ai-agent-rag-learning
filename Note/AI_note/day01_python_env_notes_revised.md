# Day 01：Python 开发环境与 GitHub 基础

## 今日学习目标

今天主要完成 Python 项目开发的基础环境配置，并掌握以后做 AI Agent、RAG、后端项目都会反复用到的基本流程：

1. 安装并配置 PyCharm。
2. 创建 Python 项目和虚拟环境。
3. 学会使用 `pip` 安装第三方库。
4. 学会使用 `.env` 管理 API Key。
5. 学会使用 `.gitignore` 忽略敏感文件和无关文件。
6. 学会使用 Git 和 GitHub 管理代码。
7. 了解误提交文件后的撤回方法。

---

## 一、Markdown 基础回顾

本次笔记使用 Markdown 编写。

Markdown 适合用于：

- 学习笔记
- 项目 README
- 实验记录
- 技术博客
- 项目文档

相关内容可参考：`Markdown_learning.md`

---

## 二、安装 PyCharm

由于我已经安装好了 Python 和 VS Code，所以今天直接从安装 PyCharm 开始。

PyCharm 官网：

[PyCharm 官方网站](https://www.jetbrains.com/pycharm/)

建议初学阶段安装：

> PyCharm Community Edition 社区版

原因：

- 免费
- 足够进行 Python 学习
- 支持虚拟环境
- 支持 Git
- 支持代码运行和调试

---

## 三、创建第一个 Python 项目

### 1. 创建项目

打开 PyCharm 后，选择：

```text
New Project
```

建议项目路径统一管理，例如：

```text
D:\AIStudy\day01_python_env
```

不要把项目随意放在桌面，也尽量避免路径过深或包含特殊字符。

推荐以后的学习目录结构：

```text
D:\AIStudy\
├── day01_python_env
├── day02_python_basic
├── ai_jd_analyzer
├── rag_course_assistant
└── agent_project
```

---

### 2. 创建虚拟环境

PyCharm 在创建新项目时，一般会自动创建虚拟环境。

虚拟环境通常位于项目目录下：

```text
.venv/
```

完整项目结构可能如下：

```text
day01_python_env/
├── .venv/
├── main.py
└── requirements.txt
```

---

## 四、什么是虚拟环境？

虚拟环境可以理解为：

> 给每个 Python 项目单独准备一个“独立的小房间”，这个项目需要的库都装在自己的房间里，不影响其他项目。

例如：

```text
项目 A：需要 langchain 0.2
项目 B：需要 langchain 0.3
```

如果所有库都装在全局 Python 里，就容易发生版本冲突。

如果每个项目都有自己的 `.venv`，就可以避免不同项目之间互相影响。

所以以后每做一个正式项目，都应该给它单独创建虚拟环境。

---

## 五、手动创建虚拟环境

虽然 PyCharm 可以自动创建虚拟环境，但也要学会手动创建。

### 1. 进入项目目录

在 VS Code、Windows Terminal 或 PyCharm Terminal 中输入：

```powershell
cd D:\AIStudy\day01_python_env
```

---

### 2. 创建虚拟环境

```powershell
python -m venv .venv
```

含义：

- `python`：使用当前 Python 解释器。
- `-m venv`：调用 Python 自带的虚拟环境模块。
- `.venv`：虚拟环境文件夹名称。

---

### 3. 激活虚拟环境

Windows 系统中输入：

```powershell
.venv\Scripts\activate
```

激活成功后，命令行前面通常会出现：

```text
(.venv)
```

例如：

```text
(.venv) D:\AIStudy\day01_python_env>
```

这说明当前终端已经进入项目的虚拟环境。

---

### 4. 退出虚拟环境

```powershell
deactivate
```

---

## 六、使用 pip 安装第三方库

`pip` 是 Python 的包管理工具，用来安装第三方库。

例如安装 `requests`：

```powershell
python -m pip install requests
```

查看已经安装的库：

```powershell
python -m pip list
```

---

## 七、为什么推荐使用 `python -m pip`

有时候会看到两种写法：

```powershell
pip install requests
```

和：

```powershell
python -m pip install requests
```

更推荐使用第二种：

```powershell
python -m pip install requests
```

原因是它表示：

> 用当前这个 Python 解释器自带的 pip 来安装库。

这样可以避免一个常见问题：

```text
你以为库安装到了当前项目里，
实际上却安装到了另一个 Python 环境里。
```

尤其是在电脑里存在多个 Python、多个虚拟环境、Anaconda 或 PyCharm 项目解释器时，`python -m pip` 更稳妥。

---

## 八、保存项目依赖

安装完第三方库后，可以把当前环境中的依赖保存到 `requirements.txt` 文件中：

```powershell
python -m pip freeze > requirements.txt
```

以后别人拿到你的项目后，只需要执行：

```powershell
python -m pip install -r requirements.txt
```

就可以安装相同的依赖。

---

## 九、使用 `.env` 管理 API Key

`.env` 文件专门用来保存敏感配置，例如：

```text
API Key
数据库密码
模型名称
服务地址
```

在 AI 项目中，API Key 绝对不要直接写进代码里，也不要上传到 GitHub。

---

### 1. 安装 `python-dotenv`

```powershell
python -m pip install python-dotenv
```

`python-dotenv` 的作用是读取项目中的 `.env` 文件，并把里面的键值对加载到环境变量中。

---

### 2. 创建 `.env` 文件

在项目根目录下新建文件：

```text
.env
```

写入示例内容：

```env
API_KEY=sk-xxxxxxxxxxxxxxxx
MODEL_NAME=gpt-4o-mini
```

注意：

- `.env` 中不要随便加空格。
- `.env` 中可能保存真实 API Key，不能上传到 GitHub。

推荐写法：

```env
API_KEY=sk-xxxxxxxxxxxxxxxx
MODEL_NAME=gpt-4o-mini
```

不推荐写法：

```env
API_KEY = sk-xxxxxxxxxxxxxxxx
MODEL_NAME = gpt-4o-mini
```

---

### 3. 在 `main.py` 中读取 `.env`

```python
import os
from dotenv import load_dotenv

# 读取当前项目中的 .env 文件
load_dotenv()

api_key = os.getenv("API_KEY")
model_name = os.getenv("MODEL_NAME")

print("API_KEY 是否读取成功：", api_key is not None)
print("当前模型名称：", model_name)
```

运行：

```powershell
python main.py
```

如果输出类似：

```text
API_KEY 是否读取成功： True
当前模型名称： gpt-4o-mini
```

说明 `.env` 读取成功。

---

## 十、使用 `.gitignore` 忽略不该上传的文件

`.gitignore` 是 Git 的“忽略清单”，用来告诉 Git 哪些文件或文件夹不要提交到 GitHub。

在项目根目录创建文件：

```text
.gitignore
```

推荐写入：

```gitignore
# Python virtual environment
.venv/
venv/

# Environment variables
.env

# Python cache
__pycache__/
*.pyc

# PyCharm
.idea/

# VS Code
.vscode/

# System files
.DS_Store
Thumbs.db
```

---

### 常见不应该上传的文件

| 文件或文件夹 | 不上传的原因 |
|---|---|
| `.venv/` | 虚拟环境很大，而且每个人电脑环境不同 |
| `.env` | 里面可能有 API Key、密码，上传会泄露 |
| `__pycache__/` | Python 自动生成的缓存文件，没必要上传 |
| `.idea/` | PyCharm 的个人配置，不一定适合别人 |
| `.vscode/` | VS Code 的个人配置，有时不需要上传 |

---

## 十一、创建 `.env.example`

虽然 `.env` 不能上传，但可以创建一个示例文件：

```text
.env.example
```

写入：

```env
API_KEY=your_api_key_here
MODEL_NAME=gpt-4o-mini
```

`.env.example` 可以上传到 GitHub。

这样别人看到你的项目后，就知道需要自己创建 `.env` 文件，并填写对应配置。

---

## 十二、项目推荐结构

今天的项目最终可以整理成：

```text
day01_python_env/
├── .venv/
├── .env
├── .env.example
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

其中建议上传到 GitHub 的文件：

```text
.env.example
.gitignore
main.py
README.md
requirements.txt
```

不建议上传的文件：

```text
.venv/
.env
.idea/
__pycache__/
```

---

## 十三、把本地项目上传到 GitHub

### 1. 安装 Git

如果已经安装，可以跳过。

检查 Git 是否安装成功：

```powershell
git --version
```

---

### 2. 配置 Git 用户名和邮箱

第一次使用 Git，需要设置用户名和邮箱：

```powershell
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的GitHub邮箱"
```

检查配置：

```powershell
git config --global --list
```

---

### 3. 初始化本地仓库

确保当前路径在项目目录下：

```powershell
cd D:\AIStudy\day01_python_env
```

初始化 Git 仓库：

```powershell
git init
```

查看当前文件状态：

```powershell
git status
```

如果 `.gitignore` 写对了，`.env` 和 `.venv/` 不应该出现在待提交列表中。

---

### 4. 添加并提交代码

```powershell
git add .
git commit -m "init python env practice"
```

---

### 5. 连接远程 GitHub 仓库

在 GitHub 新建仓库后，复制仓库地址，例如：

```text
https://github.com/你的用户名/day01-python-env.git
```

然后执行：

```powershell
git branch -M main
git remote add origin https://github.com/你的用户名/day01-python-env.git
git push -u origin main
```

这样就完成了本地项目到 GitHub 的上传。

---

## 十四、误提交文件后的撤回方法

如果不小心把 `.idea/`、`.env`、`.venv/` 等文件提交进 Git，需要先修改 `.gitignore`，再从 Git 追踪中移除这些文件。

---

### 1. 修改 `.gitignore`

确保 `.gitignore` 中已经包含：

```gitignore
.venv/
.env
.idea/
__pycache__/
*.pyc
```

---

### 2. 从 Git 追踪中移除 `.idea/`

```powershell
git rm -r --cached .idea
```

这条命令的意思是：

> 不再让 Git 追踪 `.idea/` 文件夹，但不会删除本地文件。

然后查看状态：

```powershell
git status
```

你应该会看到 `.idea/` 相关文件被标记为删除。

这里的“删除”是指从 Git 仓库中移除，不是从电脑本地删除。

---

### 3. 重新提交

```powershell
git add .gitignore
git commit -m "ignore pycharm config files"
```

如果还没有 push 到 GitHub，之后正常执行：

```powershell
git push
```

---

### 4. 如果误提交了 `.env`

如果 `.env` 已经被提交到 GitHub，应该立刻：

1. 删除 Git 对 `.env` 的追踪。
2. 修改 `.gitignore`。
3. 重新提交。
4. 更换已经泄露的 API Key。

命令如下：

```powershell
git rm --cached .env
git add .gitignore
git commit -m "remove env file from git tracking"
git push
```

注意：

> 如果真实 API Key 已经上传到 GitHub，仅仅删除文件还不够，应该去对应平台重新生成新的 API Key。

---

## 十五、今日常见问题记录

### 1. `pip install` 和 `python -m pip install` 有什么区别？

`pip install` 更短，但可能使用了错误环境中的 pip。

`python -m pip install` 更稳，因为它明确表示使用当前 Python 解释器对应的 pip。

推荐以后统一使用：

```powershell
python -m pip install 包名
```

---

### 2. `.gitignore` 为什么不生效？

可能原因：

- `.gitignore` 写错了。
- `.gitignore` 没放在项目根目录。
- 文件在加入 `.gitignore` 之前已经被 Git 追踪了。

如果文件已经被 Git 追踪，需要使用：

```powershell
git rm --cached 文件名
```

或者移除文件夹：

```powershell
git rm -r --cached 文件夹名
```

---

### 3. `.env` 和 `.env.example` 有什么区别？

| 文件 | 作用 | 是否上传 GitHub |
|---|---|---|
| `.env` | 保存真实 API Key 和配置 | 不上传 |
| `.env.example` | 提供配置模板 | 可以上传 |

---

## 十六、今日学习总结

今天完成了 Python 项目开发的基础配置，掌握了以下内容：

- 使用 PyCharm 创建 Python 项目。
- 理解虚拟环境 `.venv` 的作用。
- 学会手动创建和激活虚拟环境。
- 学会使用 `python -m pip install` 安装第三方库。
- 学会使用 `requirements.txt` 记录项目依赖。
- 学会使用 `.env` 管理 API Key。
- 学会使用 `.gitignore` 忽略敏感文件和无关文件。
- 学会将本地项目上传到 GitHub。
- 学会处理误提交 `.idea/`、`.env` 等文件的问题。

今天最重要的收获是理解了一个 Python 项目的基本开发流程：

```text
创建项目
→ 创建虚拟环境
→ 安装第三方库
→ 保存依赖
→ 使用 .env 管理密钥
→ 使用 .gitignore 保护敏感文件
→ 使用 Git 提交代码
→ 上传到 GitHub
```

这套流程以后在 AI Agent、RAG、Python 后端和其他项目中都会反复使用。
