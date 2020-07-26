#读取t1.yaml中的配置
import yaml
import os
curpath = os.path.dirname(os.path.realpath(__file__))
ymalPtah = os.path.join(curpath,"t1.yaml")
f = open(ymalPtah,'r',encoding='utf-8')
cfg = f.read()
print(cfg)
print(type(cfg))
#因为读出来的是个str类型，要转成字典就用yaml.load,加了这个Loader=yaml.FullLoader不会有警告

f.close()
s = yaml.load(cfg,Loader=yaml.FullLoader)
print(s)
print(type(s))