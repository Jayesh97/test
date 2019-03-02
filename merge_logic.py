import os
import sys
import collections
import yaml

def yaml_loader(filepath):
    with open(filepath,'r+') as fy:
        data = yaml.load(fy)
    return data

def yaml_dump(filepath,data):
    with open(filepath,'r+') as fy:
        yaml.dump(data,fy)

def update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            d[k] = update(d.get(k, {}), v)
        else:
            if type(v)==list:
                x = set(d[k])- set(v)
                d[k] = v+list(x)
            else:
                d[k] = v
    return d



filepath = os.getcwd()+'/'+sys.argv[1]
head, filename = os.path.split(filepath)
os.chdir(head)
print(os.getcwd())
f1p = filepath
while(True):
    os.chdir("..")
    parent = os.listdir(".")
    if filename in parent:
        f2p = os.getcwd()+"/"+filename
        a1 = yaml_loader(f1p)
        a2 = yaml_loader(f2p)
        os.remove(f1p)
        print("File deleted - located at --------->",f1p)
        d = update(a2,a1)
        print("File merged  - located at --------->",f2p)
        yaml_dump(f2p,d)
        f1p = f1p
    else:
        break
