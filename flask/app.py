from flask import Flask, request, jsonify, render_template
import os
from collections import Counter
import time

app = Flask(__name__)
# 改成自己的文件地址
path = r"E:\Awork\python\flask_ljh\flask_filles\leetcode.md"

if not os.path.exists(path):
  with open(path, 'w') as f:
    f.write("# LeetCode\n")

# 返回一个字典，不同url的数目
def count_urls():
    # 用于存储每个 URL 出现的次数
    url_counts = Counter()

    # 读取文件内容并统计 URL 出现次数
    with open(path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        # 跳过空行和非 URL 的行
        if ">" in line:
            # 提取 URL 部分，假设 URL 在 ":" 后面
            url = line.split(">")[1].strip()
            url_counts[url] += 1
    # 使用 sorted 函数对字典进行排序，根据次数（value）降序排列
    # 并创建一个新的字典来存储排序后的结果
    sorted_url_counts = sorted(url_counts.items(), key=lambda item: item[1], reverse=True)
    print(sorted_url_counts)

    return sorted_url_counts


@app.route("/leetcode", methods=['POST', 'GET'])
def leetcode():
  if request.method == 'GET':
        return render_template('index.html')
  url = request.values.get('url')
  time_url = time.time()
  # 将时间戳转换为本地时间并格式化为指定格式
  formatted_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time_url))
  with open(path, 'a') as f:
    f.write(f"\n{formatted_time}>{url}\n")
    
  url_counts = count_urls()
  
  return jsonify({
        "message": "URL插入完成",
        "time": formatted_time,
        "url": url,
        "url_cunts":url_counts
    })

@app.route("/leetcode/summery", methods=["GET"])
def get_summery():
    url_counts = count_urls()
    
    # Calculate the red intensity for each count in Python and pass it to the template
    url_counts_with_color = []
    for url, count in url_counts:
        red_value = min(count * 10, 255)  # Ensure the red value doesn't exceed 255
        url_counts_with_color.append((url, count, red_value))
    
    return render_template('summery.html', url_counts=url_counts_with_color)

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=8888)