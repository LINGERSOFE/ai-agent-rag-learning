# 此文档记录我在学习过程中遇到问题

## 一.有时调取终端时，powershell和cmd是有区别的
- 有些时候会要使用powershell，有时要用cmd，这里先留下一个坑，等我之后学完再来补上

---

## 有关GitHub仓库的文件夹上有箭头的问题

![如图](https://chatgpt.com/backend-api/estuary/content?id=file_0000000020807230a919727c3b36a8c4&fn=fc71a7f9-36c1-4948-9120-e7a9818460e3.png&cd=attachment&ts=494600&p=fs&cid=1&sig=c71c421bb444a3bff403085d655a0e987f6b0b30034f489b80897b13c8d53669&v=0)

那个箭头图标表示：文件被 GitHub 识别成了一个 Git 子模块 submodule。

简单说就是：你的文件夹里面大概率还保留着它自己原来的 .git 文件夹。于是当你把它放进总仓库时，Git 没有把它当成普通文件夹，而是当成了“另一个 Git 仓库的引用”。

- 对初学者来说，submodule 管理比较麻烦。这里同样学到后面再填坑

步骤：
1. 在powershell中跳转到根目录
2. 删除 day1 里面自己的 .git 

注意：这里删除的是 day1 子文件夹内部的 Git 记录，不是删除你的代码文件。

执行
```powershell
删除 day1 里面自己的 .git
```

3. 从总仓库中移除 submodule 记录

执行
```powershell
git rm --cached day1_python_env
```

这一步是把“子模块引用”从 Git 暂存区移除，但不会删除你本地的 day1_python_env 文件夹内容

4. 重新把 day1 当普通文件夹加入

```powershell
git add day1_python_env
git commit -m "fix day1 folder from submodule to normal directory"
git push
```

顺带一提，提交文件时有一般格式

```powershell
git add .
git commit -m "提交说明"
git push
```

提交说明能让你很好的追溯，git伟大无需多言

## 每天学完的固定流程

将新建的文件提交到GitHub


```powershell
cd D:\AIStudy\ai-agent-rag-learning
git status
git add .
git commit -m "提交说明"
git push
```