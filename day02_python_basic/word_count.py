def read_file(file_path):
    """读取文本文件内容"""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def clean_text(text):
    """清洗文本，把大写转小写，并去掉常见标点"""
    text = text.lower()

    punctuation = [".", ",", "!", "?", ":", ";"]
    for symbol in punctuation:
        text = text.replace(symbol, "")

    return text


def count_words(text):
    """统计单词出现次数"""
    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def show_top_words(word_count, top_n=10):
    """输出出现次数最多的单词"""
    sorted_words = sorted(
        word_count.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print(f"出现次数最多的前 {top_n} 个词：")

    for word, count in sorted_words[:top_n]:
        print(f"{word}: {count}")


def main():
    file_path = "sample.txt"

    text = read_file(file_path)
    cleaned_text = clean_text(text)
    word_count = count_words(cleaned_text)

    show_top_words(word_count, top_n=10)


if __name__ == "__main__":
    main()