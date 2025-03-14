import requests

# 目标 IPTV TXT 地址（这里替换为你的目标地址）
iptv_source_url = "https://raw.githubusercontent.com/q1017673817/iptvz/refs/heads/main/iptv.txt"

# 读取 TXT 文件
response = requests.get(iptv_source_url)
if response.status_code == 200:
    with open("iptv.txt", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("IPTV 频道更新成功！")
else:
    print("获取 IPTV 数据失败！")
