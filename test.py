import os
import yaml
import sys


def yaml_loader(filepath):
    with open(filepath,'r+') as fy:
        data = yaml.load(fy)
    return data



filepath = sys.argv[1]
p = os.getcwd()+'/'+filepath
head, filename = os.path.split(p)
os.chdir(head)
f1p = p
a1 = yaml_loader(f1p)
print(a1)
