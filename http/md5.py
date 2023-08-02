from hashlib import md5
obj = md5()
s = 'hello world'
obj.update(s.encode('utf-8'))
val = obj.hexdigest()
print(val)
print(len(val))