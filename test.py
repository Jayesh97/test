import os
import yaml
import sys
import re

def yaml_loader(filepath):
    with open(filepath,'r+') as fy:
        data = yaml.load(fy)
    return data



filepath = sys.argv[1]
p = re.compile('(.*)/(.*.yaml)')
m = p.match(filepath)
head = m.group(1)
fname = m.group(2)
os.chdir(head)
print(os.getcwd())
a1 = yaml_loader(filepath)
print(a1)