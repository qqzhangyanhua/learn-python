import httpx

# 创建http2客户端
client = httpx.Client(http2=True)
