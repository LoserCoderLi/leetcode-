# 使用官方 Python 运行环境作为基础镜像
FROM python:3.9-slim

# 将工作目录设置为 /app
WORKDIR /app

# 复制当前目录的内容到容器的 /app 目录下
COPY . /app

# 安装 requirements.txt 中的依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露容器的 8888 端口
EXPOSE 8888

# 设置 Flask 的环境变量，启用调试模式
ENV FLASK_ENV=development

# 当容器启动时运行 app.py
CMD ["python", "app.py"]
