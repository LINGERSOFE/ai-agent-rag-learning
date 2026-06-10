# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     def introduce(self):
#         print(f"我是{self.name}，现在是{self.grade}学生。")
#
#
# student1 = Student("Lingersofe", "大一")
# student1.introduce()

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