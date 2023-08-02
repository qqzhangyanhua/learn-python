import execjs
import os


os.environ["NODE_PATH"] = "/usr/local/bin/node"

with open('01.js', 'r', encoding='utf-8') as f:
    js = f.read()
    # print(js)
    js = execjs.compile(js)
    signature = js.call('foo', 'hello world')
    print(signature)