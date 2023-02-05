import yaml
import os
c = os.environ.get('CPU')
r = os.environ.get('RAM')

fname = "deployment.yaml"

stream = open(fname, 'r')
data = yaml.load(stream, Loader=yaml.FullLoader)

data['spec']['template']['spec']['containers'][0]['resources']['requests']['memory'] = r
data['spec']['template']['spec']['containers'][0]['resources']['requests']['cpu'] = c
data['spec']['template']['spec']['containers'][0]['resources']['limits']['memory'] = r
data['spec']['template']['spec']['containers'][0]['resources']['limits']['cpu'] = c

with open(fname, 'w') as yaml_file:
    yaml_file.write( yaml.dump(data, default_flow_style=False))
