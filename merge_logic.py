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


a2 = yaml_loader(sys.argv[2]) ##present in dir3
a1 = yaml_loader(sys.argv[1]) ##present in dir4
d = update(a2,a1)
print(d)
