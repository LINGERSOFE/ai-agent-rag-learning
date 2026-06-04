# 学习第一天
- Markdown 的基础用法
详情参见Markdown_learning.md

## 安装必备软件
- 鉴于我已经安装了 python 和 VS code,于是便直接从pycharm开始

    [pycharm官网](https://www.jetbrains.com/help/pycharm/creating-empty-project.html?utm_source=chatgpt.com)

## 创建一个新项目

- 页面左上角点击文件，新建项目，pycharm会自动创建虚拟环境
- 建议养成好习惯，对于项目管理，文件夹管理
- .venv 就是这个项目自己的虚拟环境。

### 虚拟环境介绍
- 给每个 Python 项目单独准备一个“独立的小房间”，这个项目需要的库都装在自己的房间里，不影响其他项目。以后每做一个正式项目，都应该有自己的虚拟环境：

## 虚拟环境安装包
- pip install用于下载库
- pip list 用于检查已安装的库

## 学会自己创建虚拟环境
1. 在 VS Code、Windows Terminal 或 PyCharm Terminal 中进入项目目录

```bash
cd D:\AIstudy\day01_python_env
```

2. 创建虚拟环境：

```bash
python -m venv .venv
```

3. 激活虚拟环境

```bash
.venv\Scripts\activate
```

- 激活成功后，命令行前面通常会出现：

```bash
(.venv)
```

例如：
```bash
(.venv) D:\AIStudy\day01_python_env>
```
4. 然后安装库
```bash
pip install requests
```
5. 退出虚拟环境
```bash
deactivate
```
### 注意事项
- 不要把 .venv 上传到 GitHub

以后如果你用 GitHub，需要新建 .gitignore 文件，写入：

```markdown
.venv/
__pycache__/
.env
```

`.venv` 很大，而且每个人电脑环境不同，不应该上传。

- 在使用pip时，要注意最好再前面加上`python -m`，这是基于当前python环境下载包文件

换句话说
```markdown
用当前这个 Python 自带的 pip 来安装
```

避免了一个常见问题:

```markdown
你以为装到了当前项目里，
实际上装到了另一个 Python 环境里。
```


## 安装完第三方库后
- 将依赖保存到`.txt`文件中，这里使用`freeze`
```markdown
python -m pip freeze > requirements.txt
```
- 以后别人拿到你的项目后，只需要执行：
```markdown
python -m pip install -r requirements.txt
```
就能安装你的项目依赖

---

## 学会 `.env` 管理 API Key

`.env` 文件专门用来保存敏感配置，比如：
```markdown
API Key
数据库密码
模型名称
服务地址
```
`python-dotenv` 的作用是读取项目里的 `.env` 文件，把里面的键值对加入到环境变量中，然后你就可以用 `os.getenv()` 读取。

1. 创建`.env`文件

在项目根目录下新建文件
```markdown
.env
```
写入
```markdown
API_KEY=sk-xxxxxxxxxxxxxxxx
MODEL_NAME=gpt-4o-mini
```

2. 安装`python-dotenv`

    已经安装不再赘述
3. 在 `main.py` 中读取 `.env`
打开`main.py`，写入：
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

4. 绝对不要把 `.env `上传到 GitHub

- 在项目根目录创建：`.gitignore`（Git 的“忽略清单”，不要被提交到 GitHub。）
- 写入
```markdown
.venv/
.env
__pycache__/
*.pyc
```
- 为什么不上传

| 文件 | 原因 |
|---|---|
| `.venv` | 虚拟环境很大，而且每个人电脑环境不同|
| `.env` | 里面可能有 API Key、密码，上传会泄露 |
| `__pycache__/` |Python 自动生成的缓存文件，没必要上传 |
| `.idea/` |PyCharm 的个人配置，不一定适合别人 |
| `.vscode/` |VS Code 的个人配置，有时不需要上传 |

- **做 AI 项目，API Key 永远不要直接写在代码里，也不要上传 GitHub。**

5. 创建 `.env.example`

- 虽然 `.env` 不能上传，但你可以在项目根目录创建一个示例文件：
```markdown
.env.example
```
写入
```markdown
API_KEY=your_api_key_here
MODEL_NAME=gpt-4o-mini
```
这个文件可以上传 GitHub，别人看到后就知道应该自己创建 `.env。`

---

## 把本地项目上传到 GitHub
1. 安装git（已装略过）
2. 配置 Git 用户名和邮箱

- 第一次用 Git，需要设置：
```markdown
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的GitHub邮箱"
```
检查配置：
```markdown
git config --global --list
```
3. 初始化本地仓库

- 首先确保你在项目目录下：
```markdown
cd D:\AIStudy\day01_python_env
```
- 初始化Git
```markdown
git init
```
- 查看当前文件状态：
```markdown
git status
```
你应该能看到 `main.py`、`.gitignore`、`.env.example`、`requirements.txt` 等文件。

注意：如果 `.gitignore` 写对了，`.env` 和 `.venv/` 不应该出现在待提交列表里。

4. 添加并提交代码 
```markdown
git add .
git commit -m "init python env practice"
```
5. 远程连接Github仓库

- 在 GitHub 新建仓库后，页面会给你一个地址

- 执行
```markdown
git branch -M main
git remote add origin https://github.com/你的用户名/day01-python-env.git
git push -u origin main
```
**这样你就完成了文件的上传**

## 当你把不必要的文件或者敏感文件已经传到Git的撤回操作
1. 修改.gitignore将不必要的文件加入忽略目录

2. 从 Git 追踪中移除 `.idea`

执行
```bash
git rm -r --cached .idea
```
这条命令的意思是：

不再让 Git 追踪 .idea 文件夹，但本地文件不会被删除。

然后执行
```bash
git status
```
你应该会看到 `.idea` 相关文件被标记为删除，但这只是从 Git 仓库中移除，不是从你电脑里删掉

3. 重新提交
```bash
git add .gitignore
git commit -m "ignore pycharm config files"
```
如果你还没有 push 到 GitHub，再正常 push 就行：
```bash
git push
```
