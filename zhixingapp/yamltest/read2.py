#读取t1.yaml中的配置
import yaml
import os
curpath = os.path.dirname(os.path.realpath(__file__))
ymalPtah = os.path.join(curpath,"t2.yaml")
f = open(ymalPtah,'r',encoding='utf-8')
cfg = f.read()
print(cfg)
print(type(cfg))
s = yaml.load(cfg,Loader=yaml.FullLoader)
print(s)
print(type(s))
