import os

print("Hello world")
print(os.getcwd())

filepath = sys.argv[1]
p = os.getcwd()+'/'+filepath
head, filename = os.path.split(p)
os.chdir(head)
f1p = filepath
a1 = yaml_loader(f1p)
print(a1)
