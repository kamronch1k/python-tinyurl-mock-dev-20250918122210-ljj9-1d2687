import hashlib
s='devmini'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
