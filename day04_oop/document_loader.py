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