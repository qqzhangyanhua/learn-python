
# 关于加密  AES DES

from Crypto.Cipher import AES

from Crypto.Util import Padding

# 1.加密
# 1.1 准备一个key
s = '我爱你'
# 创建一个加密器
# mode 模式ECB CBC
aes = AES.new(key='9395939210@qq.com'.encode(), mode=AES.MODE_ECB)

bs =s.encode('utf-8')
bs = Padding.pad(bs, 16)
r =aes.encrypt(bs)
print(r)