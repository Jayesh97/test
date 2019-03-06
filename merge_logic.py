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
        yaml.dump(data,fy,default_flow_style=False)

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


def merge(a):
    filepath = os.getcwd()+'/'+a
    head, filename = os.path.split(filepath)
    os.chdir(head)
    f1p = filepath
    while(True):
        os.chdir("..")
        parent = os.listdir(".")
        if filename in parent:
            f2p = os.getcwd()+"/"+filename
            a1 = yaml_loader(f1p)
            a2 = yaml_loader(f2p)
            d = update(a2,a1)
            f1p = f2p
        else:
            break
    yaml_dump(filepath,d)
    return d

if __name__ == '__main__':
    y = merge(sys.argv[1])
    print yaml.dump(y,default_flow_style=False)
    