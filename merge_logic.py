import os
import sys
import collections
import yaml
'''
The program takes path to YAML file and recursively merges them and stores them in the orignal file(ie. child).
'''

def yaml_loader(filepath):
    with open(filepath,'r+') as fy:
        data = yaml.load(fy)
    return data

def yaml_dump(filepath,data):
    with open(filepath,'r+') as fy:
        yaml.dump(data,fy,default_flow_style=False)

#Updates dictionary 
def update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            #Dictinary keys with values as dict() merge iteratively by calling itself
            d[k] = update(d.get(k, {}), v)
        else:
            if type(v)==list: 
                #Dictinary keys with values as list merge
                x = set(d[k])- set(v)
                d[k] = v+list(x)
            else:
                #Dictinary keys with values as str,float,int merge
                d[k] = v
    return d

# Merges Yaml Files
def merge(a):
    home = os.getcwd()
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
    #updating the original input file with the modified value
    yaml_dump(filepath,d)
    os.chdir(home)
    return d

if __name__ == '__main__':
    y = merge(sys.argv[1])
    print yaml.dump(y,default_flow_style=False)

    
