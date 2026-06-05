# file_path = "data/sample.txt"
#
# with open(file_path, "r", encoding="utf-8") as file:
#     content = file.read()
#
# print(content)
#
#
# output_path = "output/result.txt"
#
# text = """今天学习了 Python 文件处理。
# 我学会了读取 TXT 文件。
# 我也学会了写入 TXT 文件。
# """
#
# with open(output_path, "w", encoding="utf-8") as file:
#     file.write(text)
#
# print("写入完成！")
#
# import json
#
# file_path = "data/qa_data.json"
#
# with open(file_path, "r", encoding="utf-8") as file:
#     qa_list = json.load(file)
#
# print(qa_list)
#
# for item in qa_list:
#     print("问题：", item["question"])
#     print("回答：", item["answer"])
#     print()
#

#
# import json
#
# student = {
#     "name": "Lingersofe",
#     "grade": "大一",
#     "direction": "AI Agent / RAG",
#     "skills": ["Python", "Git", "Markdown"]
# }
#
# with open("output/student.json", "w", encoding="utf-8") as file:
#     json.dump(student, file, ensure_ascii=False, indent=4)
#
# print("JSON 写入完成！")


import csv

file_path = "data/students.csv"

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["grade"], row["direction"])