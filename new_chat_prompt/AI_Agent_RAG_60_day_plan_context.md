# AI Agent / RAG 实习冲刺计划交接文件

> 用途：如果开启新的 ChatGPT 对话，请直接上传本文件，并告诉 ChatGPT：“请先阅读这个文件，继续指导我完成 AI Agent / RAG 学习计划。”
>
> 目标：让新对话中的助手快速理解我当前的背景、目标、学习路线、当前进度，并继续按计划推进。

---

## 1. 我的基本背景

我是一名大一学生，希望未来进入大公司工作并获得较高薪资。目前对 AI 方向知识比较薄弱，但希望利用暑假系统提升自己，重点围绕：

- AI Agent
- RAG 知识库
- 大模型应用开发
- Prompt 工程
- Python 后端
- GitHub 项目展示
- 技术文档与 README

我的目标不是两个月内成为训练大模型的算法专家，而是：

```text
从“对 AI 感兴趣但没有作品”
变成“能独立做出 AI Agent / RAG Demo，并能讲清楚原理、代码、优化思路和踩坑过程”
```

---

## 2. 目标岗位理解

我看到的实习岗位大致属于：

```text
AI Agent 应用开发 / RAG 知识库工程 / Prompt 工程 / 工具调用与流程编排实习岗
```

岗位重点不是训练大模型，而是更偏向：

- 基于大模型 API 做应用开发
- 搭建企业知识库问答系统
- 使用 RAG 技术减少模型幻觉
- 编写和优化 Prompt
- 构建 AI Agent，让模型能够调用工具
- 使用 LangChain、LlamaIndex、Dify 等框架
- 写技术文档、测试样例、排查问题
- 把项目整理成 GitHub 作品集

---

## 3. 需要掌握的核心能力

### 3.1 Python 基础与工程能力

需要掌握：

- Python 基础语法
- 函数、类、异常处理
- 文件读取与写入
- JSON、CSV、Markdown 基础处理
- `requests`
- `python-dotenv`
- `pandas`
- 虚拟环境 `.venv`
- `pip`
- `requirements.txt`
- Git / GitHub
- README 编写

最低目标：

```text
能独立写出：
读取文件 → 调用模型 API → 处理返回结果 → 保存结果 → 做成接口或简单网页
```

---

### 3.2 大模型基础

需要理解：

- LLM 是什么
- Token 是什么
- 上下文窗口是什么
- Temperature / Top-p 的作用
- Embedding 是什么
- 向量相似度搜索是什么
- 大模型为什么会出现幻觉
- RAG 为什么能减少幻觉

核心理解：

```text
大模型本身不一定知道企业内部文档，
所以需要先从知识库中检索相关内容，
再把检索结果放进 Prompt，
让模型基于资料回答。
```

---

### 3.3 Prompt 工程

需要掌握：

- 角色设定
- 任务拆解
- 输出格式控制
- Few-shot 示例
- 防止模型胡编
- 约束模型引用资料
- 让模型在不知道时回答“不知道”
- Prompt 版本迭代

示例 Prompt：

```text
你是一个严谨的企业知识库助手。
请只根据下方资料回答问题。
如果资料中没有答案，请回答“根据当前知识库无法确定”。
回答时请列出依据。
```

---

### 3.4 RAG 知识库搭建

需要掌握完整流程：

```text
文档收集
→ 文档解析
→ 文本切分
→ 向量化 Embedding
→ 存入向量数据库
→ 用户提问
→ 相似度检索
→ 召回相关片段
→ 拼接 Prompt
→ 调用大模型回答
→ 评估答案是否准确
```

需要了解的工具：

| 工具 | 作用 |
|---|---|
| Chroma | 本地向量数据库，适合学习和 Demo |
| FAISS | 本地向量检索 |
| Milvus | 更偏企业级向量数据库 |
| LangChain | Agent、工具调用、RAG 流程编排 |
| LlamaIndex | 文档索引、知识库、RAG 应用 |
| Dify | 低代码搭建 Agent、知识库和工作流 |

---

### 3.5 Agent 开发与工具调用

需要理解 Agent 的基本流程：

```text
用户目标
→ Agent 分析任务
→ 决定调用哪些工具
→ 执行工具
→ 根据工具结果继续推理
→ 给出最终答案
```

目标项目：

```text
一个可以调用天气 API、计算器、本地知识库等工具的 AI Agent。
```

---

### 3.6 测试、排查与技术文档

企业更看重的不只是“代码跑通”，还包括：

- 是否能复现问题
- 是否能定位错误
- 是否能写清楚原因
- 是否能记录解决方案
- 是否能对比优化前后效果
- 是否能写 README 和技术文档

项目文档至少包括：

```text
1. 项目背景
2. 功能介绍
3. 技术栈
4. 系统架构图
5. RAG 流程
6. 安装运行方法
7. 核心代码说明
8. 测试样例
9. 已知问题
10. 后续优化方向
```

---

## 4. 两个月结束时的成果目标

两个月结束时，最好拥有以下成果：

1. GitHub 项目 1：个人资料 / 课程资料 RAG 助手
   - 支持上传 PDF / Markdown / TXT
   - 支持问答
   - 能返回引用来源
   - 能处理知识库中没有答案的问题

2. GitHub 项目 2：AI Agent 工具助手
   - 支持调用计算器、天气、搜索或本地知识库工具
   - 能根据用户问题自动选择工具
   - 能展示 Agent 的任务拆解过程

3. 技术文档 / 博客
   - 例如：《从零搭建一个基于 LangChain + Chroma 的 RAG 知识库助手》

4. 一份面向 AI Agent / RAG 实习的简历项目经历
   - 不能只写“熟悉 LangChain”
   - 要写清楚项目功能、技术栈、优化思路和测试方式

---

## 5. 56 天详细学习计划

说明：原计划按每天 5–7 小时设计。如果每天只有 3 小时，可以把每天任务拆成两天完成。

---

# 第 1 周：Python 工程基础 + GitHub

## 本周目标

能独立写 Python 脚本、调用 API、管理项目结构，并把代码上传 GitHub。

### Day 1：环境搭建

任务：

- 安装 Python
- 安装 VS Code
- 安装 PyCharm
- 学会创建虚拟环境 `.venv`
- 学会 `pip install`
- 学会 `.env` 管理 API Key
- 创建 GitHub 账号和第一个仓库

已完成内容：

- 已安装 Python
- 已安装 VS Code
- 已学习 PyCharm 安装和虚拟环境
- 已学习 `pip install` 和 `python -m pip`
- 已学习 `.env`
- 已学习 `.gitignore`
- 已学习 GitHub 仓库上传流程
- 已整理 Day 01 Markdown 笔记
- 已生成修改后的 Markdown 文件：`day01_python_env_notes_revised.md`

Day 1 学到的重点：

```text
创建项目
→ 创建虚拟环境
→ pip 安装依赖
→ .env 管理密钥
→ .gitignore 保护敏感文件
→ requirements.txt 记录依赖
→ GitHub 保存项目
```

### Day 2：Python 基础语法

学习内容：

- 变量
- 列表
- 字典
- 循环
- 条件判断
- 函数

练习任务：

```text
读取一个 txt 文件，统计其中出现最多的 10 个词。
```

产出：

- 一个 Python 小脚本
- 一份学习笔记
- 一次 GitHub commit

### Day 3：文件处理

学习内容：

- 读写 TXT
- 读写 JSON
- 读写 CSV
- 异常处理

练习任务：

```text
读取一个 JSON 文件，把其中的问题和答案整理成 Markdown。
```

产出：

- `json_to_markdown.py`
- 示例输入文件
- 示例输出文件
- README 说明

### Day 4：面向对象基础

学习内容：

- 类
- 对象
- 构造函数
- 方法

练习任务：

```text
写一个 DocumentLoader 类，负责读取不同类型的文本文件。
```

产出：

- `document_loader.py`
- 支持读取 `.txt` 和 `.md`
- 尝试设计类和方法

### Day 5：API 调用

学习内容：

- `requests`
- GET / POST
- JSON 请求体
- API Key

练习任务：

```text
调用一个公开 API，获取数据并格式化输出。
```

产出：

- `api_demo.py`
- 能读取 `.env` 中的 API Key
- 能处理请求失败的情况

### Day 6：FastAPI 入门

学习内容：

- 创建 FastAPI 项目
- 写 `/hello`
- 写 `/chat`
- 启动服务

练习任务：

```text
做一个简单接口：用户输入问题，接口返回固定回答。
```

产出：

- `main.py`
- `/hello`
- `/chat`
- README 中写清楚启动方式

### Day 7：整理与复盘

任务：

- 把本周代码上传 GitHub
- 写 README
- 总结 10 个踩坑点
- 录一个 1 分钟项目演示视频

产出：

- 第一个完整 GitHub 小项目
- 第 1 周学习总结

---

# 第 2 周：Prompt 工程 + 大模型 API

## 本周目标

能调用大模型，并写出稳定、可控、结构化输出的 Prompt。

### Day 8：理解 LLM 基础

掌握：

- Token
- 上下文
- 系统提示词
- 用户提示词
- 模型参数

输出：

```text
写一篇 800 字笔记：大模型为什么会胡说？
```

### Day 9：Prompt 基础

练习 5 类 Prompt：

- 总结
- 分类
- 信息抽取
- 改写
- 问答

任务：

```text
让模型把一段招聘信息提取成 JSON。
```

### Day 10：结构化输出

练习让模型稳定输出 JSON：

```json
{
  "岗位名称": "",
  "技能要求": [],
  "学习建议": [],
  "匹配度评分": ""
}
```

目标：

- 让模型稳定输出 JSON
- 处理格式错误

### Day 11：Prompt 迭代

同一个任务写 5 版 Prompt：

1. 普通版
2. 角色版
3. 约束版
4. 示例版
5. 防幻觉版

比较输出质量。

### Day 12：做一个“简历分析助手”

功能：

```text
输入岗位 JD + 我的简历
输出：
1. 匹配度
2. 缺失技能
3. 学习建议
4. 简历修改建议
```

### Day 13：加上 FastAPI

把简历分析助手封装成接口：

```text
POST /analyze_resume
```

### Day 14：整理项目

产出：

- GitHub 仓库
- README
- 示例截图
- Prompt 模板
- 技术总结

---

# 第 3 周：RAG 基础

## 本周目标

真正理解并跑通一个最小 RAG 系统。

### Day 15：理解 RAG 流程

画出流程图：

```text
文档 → 切分 → Embedding → 向量库 → 检索 → Prompt → 回答
```

写笔记：

```text
为什么 RAG 比直接问大模型更适合企业知识库？
```

### Day 16：文档切分

学习：

- chunk size
- chunk overlap
- 按字符切分
- 按段落切分

练习：

```text
把一篇 Markdown 文档切成多个 chunk。
```

### Day 17：Embedding

学习：

- 什么是向量
- 什么是语义相似度
- 为什么“苹果手机”和“iPhone”能被检索到

练习：

```text
把 10 句话转成向量，并计算相似度。
```

### Day 18：Chroma 入门

任务：

- 安装 Chroma
- 创建本地向量库
- 存入文档 chunk
- 查询相似文本

### Day 19：LangChain RAG

任务：

- 按照 LangChain 官方 RAG 教程做一遍
- 重点理解每一步，而不是只复制代码

### Day 20：做第一个知识库问答助手

项目：

```text
校园课程资料问答助手
```

功能：

- 上传课程资料
- 提问
- 返回答案
- 返回引用片段

### Day 21：复盘

输出：

- RAG 流程图
- README
- 3 个成功案例
- 3 个失败案例
- 失败原因分析

---

# 第 4 周：RAG 优化

## 本周目标

从“能跑”变成“回答更准”。

### Day 22：检索质量问题

学习常见问题：

- 检索不到
- 检索错
- chunk 太大
- chunk 太小
- overlap 不合适
- Prompt 没有限制

### Day 23：调整 chunk 参数

实验：

```text
chunk_size = 300 / 500 / 800 / 1000
chunk_overlap = 50 / 100 / 150
```

记录不同结果。

### Day 24：加引用来源

要求回答格式：

```text
回答：
依据：
来源片段：
无法确定的部分：
```

### Day 25：加入 Query Rewrite

例如用户问：

```text
这个怎么报销？
```

系统先改写为：

```text
根据公司报销制度，员工差旅费用如何报销？
```

再去检索。

### Day 26：加入多轮对话

支持：

```text
用户：报销需要什么材料？
AI：……
用户：那打车呢？
```

系统能理解“那”指的是报销场景。

### Day 27：加入测试集

准备 20 个问题：

- 10 个知识库中有答案
- 5 个部分有答案
- 5 个没有答案

统计：

```text
回答准确率
是否引用正确
是否胡编
```

### Day 28：项目整理

产出第一个正式项目：

```text
Project 1：基于 LangChain + Chroma 的课程资料 RAG 问答助手
```

简历写法：

```text
基于 LangChain 与 Chroma 构建课程资料 RAG 问答助手，实现文档解析、文本切分、Embedding 入库、相似度检索、Prompt 约束回答与来源引用；通过调整 chunk size、overlap 和检索 Top-K 优化回答准确性，并构建 20 条测试集评估问答效果。
```

---

# 第 5 周：Dify + 低代码 Agent

## 本周目标

会用 Dify 快速搭建 Agent 和知识库应用。

### Day 29：认识 Dify

学习：

- 应用
- 知识库
- 工作流
- Agent
- 工具

### Day 30：搭建 Dify 知识库

任务：

- 上传 3 篇文档
- 配置切分方式
- 创建知识库问答应用

### Day 31：优化 Dify Prompt

要求：

- 只基于知识库回答
- 不知道就说不知道
- 输出结构化答案
- 引用资料依据

### Day 32：Dify 工作流

做一个流程：

```text
用户输入问题
→ 判断问题类型
→ 检索知识库
→ 生成答案
→ 输出建议
```

### Day 33：Dify Agent 工具调用

做一个 Agent：

```text
用户输入任务
→ Agent 判断是否查知识库
→ 判断是否调用工具
→ 输出答案
```

### Day 34：复现一个企业场景 Demo

建议做：

```text
企业员工制度问答 Agent
```

功能：

- 问请假制度
- 问报销流程
- 问入职材料
- 问找不到答案时提醒联系 HR

### Day 35：写技术文档

文档标题：

```text
基于 Dify 的企业制度知识库 Agent 搭建与优化
```

---

# 第 6 周：LangChain / LlamaIndex Agent

## 本周目标

用代码实现一个简单 Agent，而不只是会用低代码平台。

### Day 36：理解 Agent 架构

掌握：

```text
LLM
Tool
Memory
Planner
Executor
Observation
```

### Day 37：工具调用

写 3 个工具：

```text
calculator_tool
weather_tool
knowledge_search_tool
```

### Day 38：让 Agent 自动选择工具

示例：

```text
用户：3 个苹果每个 5 元，一共多少钱？
Agent 调用 calculator_tool
```

```text
用户：学校奖学金怎么申请？
Agent 调用 knowledge_search_tool
```

### Day 39：学习 Hugging Face Agents Course

重点看：

- Agent 概念
- Agent 实践
- 工具调用
- 框架实践

### Day 40：LlamaIndex 入门

做一个：

```text
PDF 文档问答助手
```

### Day 41：整合 Agent + RAG

项目：

```text
学习规划 Agent
```

功能：

- 读取课程资料
- 回答知识点
- 制定复习计划
- 调用计算器安排时间

### Day 42：整理项目

产出：

```text
Project 2：AI 学习规划 Agent
```

简历写法：

```text
基于 LangChain / LlamaIndex 实现 AI 学习规划 Agent，集成本地知识库检索、计算工具和任务规划能力，支持根据用户目标自动拆解学习任务、调用工具并生成阶段计划。
```

---

# 第 7 周：项目工程化与部署

## 本周目标

让项目看起来像“能交付”的作品，而不是课程作业。

### Day 43：整理项目结构

标准结构：

```text
ai-agent-project/
├── app/
│   ├── main.py
│   ├── rag.py
│   ├── agent.py
│   ├── tools.py
│   └── config.py
├── data/
├── tests/
├── README.md
├── requirements.txt
└── .env.example
```

### Day 44：FastAPI 封装

接口：

```text
POST /upload
POST /chat
POST /query
GET /health
```

### Day 45：简单前端

可以使用：

- Gradio
- Streamlit
- 简单 HTML
- Dify 页面

目标：

```text
让面试官能直接试用项目。
```

### Day 46：错误处理

加入：

- 文件为空提示
- API Key 缺失提示
- 检索不到答案提示
- 模型调用失败提示

### Day 47：日志系统

记录：

```text
用户问题
检索到的 chunk
模型回答
耗时
错误信息
```

### Day 48：部署

可以选择：

- 本地运行
- Hugging Face Spaces
- Render
- Railway
- 自己的 VPS

### Day 49：写完整 README

README 必须包括：

```text
项目简介
功能特点
技术架构
安装方式
运行截图
接口说明
测试样例
优化思路
未来计划
```

---

# 第 8 周：简历、面试、投递

## 本周目标

把学习成果转化为实习竞争力。

### Day 50：整理简历

错误写法：

```text
熟悉 LangChain、Dify、RAG。
```

正确写法：

```text
基于 LangChain + Chroma 构建 RAG 知识库问答系统，实现文档切分、向量入库、语义检索、Prompt 约束回答和来源引用；通过构建 20 条测试集，对比不同 chunk size、Top-K 参数对回答准确性的影响。
```

### Day 51：准备项目讲解稿

每个项目准备 3 分钟讲解：

```text
1. 为什么做这个项目？
2. 用了什么技术？
3. 核心流程是什么？
4. 遇到什么问题？
5. 如何优化？
6. 还能怎么改进？
```

### Day 52：准备面试问题

必须能回答：

- 什么是 RAG？
- RAG 为什么能减少幻觉？
- chunk size 怎么选？
- Embedding 是什么？
- 向量数据库有什么用？
- LangChain 和 LlamaIndex 区别是什么？
- Agent 和普通 Chatbot 有什么区别？
- 如何评估 RAG 效果？
- 如果回答不准确，你怎么排查？

### Day 53：模拟面试

要求：

- 不能只背概念
- 必须结合自己的项目回答

### Day 54：投递实习

投递方向：

- AI Agent 实习生
- 大模型应用开发实习生
- RAG 工程实习生
- Prompt 工程实习生
- AI 产品技术实习生
- Python 后端实习生

### Day 55：优化 GitHub

检查：

- README 是否清楚
- 是否有运行截图
- 是否有 `.env.example`
- 是否有 `requirements.txt`
- 是否有测试样例
- 是否有项目演示视频

### Day 56：总结与复盘

输出一篇文章：

```text
大一学生两个月从零搭建 AI Agent/RAG 项目的学习总结
```

可以发布到：

- GitHub
- CSDN
- 掘金
- 个人博客
- 简历链接

---

## 6. 每天固定学习节奏

建议暑假每天这样安排：

| 时间 | 内容 |
|---|---|
| 08:30–09:00 | 复盘昨天内容 |
| 09:00–11:30 | 学习新知识 |
| 14:00–17:00 | 写代码做项目 |
| 19:30–20:30 | 整理笔记 |
| 20:30–21:30 | 改 README / 写博客 / 总结踩坑 |
| 21:30–22:00 | 明天任务拆解 |

每天必须完成三件事：

```text
写代码
写文档
提交 GitHub
```

---

## 7. 推荐学习资料

新对话中如果需要实时链接，请重新联网搜索确认最新地址。

### Python / 工程基础

- Python 官方教程
- FastAPI 官方教程
- GitHub 官方文档
- pip 官方文档
- python-dotenv 文档

### Prompt / 大模型应用

- DeepLearning.AI：ChatGPT Prompt Engineering for Developers
- DeepLearning.AI：Retrieval Augmented Generation

### RAG / 知识库

- LangChain 官方 RAG 教程
- LlamaIndex 官方 RAG 文档
- Chroma 文档
- Milvus 官方 RAG 教程

### Agent / 工作流

- Hugging Face AI Agents Course
- Dify 官方文档
- LangChain Agent / LangGraph 相关文档
- LlamaIndex Agent 相关文档

---

## 8. 剩余大学三年大致规划

### 大二：打牢计算机基础 + 做 AI 应用项目

大二上学期重点：

- 数据结构
- 算法基础
- Python
- C/C++
- Git
- Linux
- 数据库
- 计算机网络基础

项目方向：

```text
1. 校园资料 RAG 助手
2. 简历优化 Agent
3. 课程问答机器人
4. 学习计划 Agent
```

目标：

- GitHub 至少 3 个完整项目
- 至少写 10 篇技术博客
- 参加 1–2 个校内项目或比赛

大二下学期重点：

- 机器学习基础
- 深度学习基础
- PyTorch
- NLP 基础
- Transformer 基础

项目方向：

```text
1. 基于 RAG 的论文阅读助手
2. 多文档问答系统
3. AI 客服 Agent
4. 微信/网页知识库机器人
```

目标：

- 找第一段小厂或实验室实习
- 或加入老师的科研项目
- 简历上有 2 个 AI 相关项目

---

### 大三：冲大厂实习

大三上学期重点：

- 刷算法题
- 深入后端开发
- 学习 Docker
- 学习云服务器部署
- 学习 LangGraph / LlamaIndex / Dify / Milvus
- 学习 RAG 评估与优化

项目升级方向：

```text
从 Demo 变成系统：
用户登录
文件上传
权限管理
知识库管理
检索日志
答案评估
后台管理
```

目标：

- 投递日常实习
- 准备大厂提前批
- 简历项目要有“工程复杂度”

大三下学期重点：

- 大厂暑期实习投递
- 算法题保持训练
- 深挖一个方向

可选主方向：

| 方向 | 适合内容 |
|---|---|
| AI Agent 应用开发 | LangChain、Dify、RAG、工具调用 |
| 大模型后端工程 | Python、FastAPI、数据库、Docker |
| 机器学习算法 | 数学、PyTorch、论文、模型训练 |
| AI 产品技术 | Prompt、工作流、业务理解、Demo 搭建 |

当前更推荐路线：

```text
AI Agent 应用开发 + Python 后端 + RAG 工程
```

---

### 大四：确定就业方向 + 拿 Offer

如果选择就业：

大四上学期：

- 集中秋招
- 完善简历
- 准备项目讲解
- 准备算法和八股
- 投 AI 应用开发、后端开发、大模型应用岗

大四下学期：

- 做毕业设计
- 实习转正
- 补齐工程能力

毕业设计方向建议：

```text
基于大模型与 RAG 的高校课程智能问答系统设计与实现
```

---

## 9. 后续新对话应该如何继续

如果在新对话中上传本文件，希望 ChatGPT 按下面方式继续指导：

1. 先确认当前处于第几天学习。
2. 询问或判断我今天已经完成了哪些内容。
3. 不要重新讲完整 56 天计划，除非我要求。
4. 直接给出当天的学习任务、代码练习、笔记模板和检查清单。
5. 对我上传的代码、Markdown 笔记、README、报错截图进行具体修改和解释。
6. 每天结束时帮我整理：
   - 今日学习总结
   - 今日 GitHub commit 建议
   - 明日任务
7. 回答时尽量适合大一学生理解，但要逐渐提高工程化要求。
8. 始终围绕最终目标：两个月内完成 AI Agent / RAG 项目作品集。

---

## 10. 当前进度记录

截至本文件生成时，当前处于：

```text
第 1 周 Day 1 结束阶段
```

已经完成：

- Python 安装
- VS Code 安装
- PyCharm 安装学习
- 虚拟环境 `.venv` 学习
- `pip install` 与 `python -m pip` 学习
- `.env` 管理 API Key 学习
- `.gitignore` 学习
- GitHub 仓库创建与上传流程学习
- Markdown 基础笔记整理
- Day 1 Markdown 笔记润色

下一步建议进入：

```text
第 1 周 Day 2：Python 基础语法
```

Day 2 应重点完成：

- 变量
- 字符串
- 列表
- 字典
- 条件判断
- 循环
- 函数
- 一个文本词频统计小练习
- 对应 Markdown 学习笔记
- GitHub commit
