import os
from dotenv import load_dotenv

# 读取当前项目中的 .env 文件
load_dotenv()

api_key = os.getenv("API_KEY")
model_name = os.getenv("MODEL_NAME")

print("API_KEY 是否读取成功：", api_key is not None)
print("当前模型名称：", model_name)