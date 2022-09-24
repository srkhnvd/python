import os
create = "C:/arts/PYTHON"
os.mkdir(create)
dir = "C:/arts/PYTHON"
dir2 = "C:/arts/PYTHON2"
os.rename(dir,dir2)
res = []
for path in os.listdir(dir2):
    if os.path.isfile(os.path.join(dir2, path)):
        res.append(path)
print(res)
os.rmdir(dir2)