import os
import yaml
import sys
import re

def yaml_loader(filepath):
    with open(filepath,'r+') as fy:
        data = yaml.load(fy)
    return data



filepath = sys.argv[1]
head, filename = os.path.split(filepath)
print(filepath)
os.chdir(head)
a1 = yaml_loader(filepath)
print(a1)