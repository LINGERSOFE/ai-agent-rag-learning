name="Lingersofe"
print(name)
print(type(name))

text = "Python is useful for AI Agent"

print(text)
print(len(text))
print(text.lower())
print(text.upper())
print(text.replace("Python", "Java"))

sentence = "Python is useful for AI Agent"
words = sentence.split()

print(words)


name = "Lingersofe"
direction = "AI Agent"

print(f"我是{name}，我正在学习{direction}。")


student = {
    "name": "Lingersofe",
    "grade": "大一",
    "target": "AI Agent 实习",
    "language": "Python"
}

print(student)
print(student["name"])
print(student["target"])


learning_plan = {
    "day": 2,
    "topic": "Python 基础语法",
    "tasks": ["变量", "字符串", "列表", "字典", "循环", "函数"],
    "goal": "完成词频统计小项目"
}

print(f"今天是第 {learning_plan['day']} 天")
print(f"学习主题：{learning_plan['topic']}")
print(f"今日目标：{learning_plan['goal']}")

for task in learning_plan["tasks"]:
    print("任务：", task)

    tasks = ["变量", "字符串", "列表"]

    for task in tasks:
        print(task)