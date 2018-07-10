#!/usr/bin/env python

import jinja2

filename = 'ospf_config.j2'

with open(filename) as f:
    mytemplate = f.read()
    
vars = {
    'process_id': 40,
    'network': '10.220.88.0',
    'wildcard': '0.0.0.255',
    'area': 0,
    'loopback0_addr': '172.31.255.1',
    'loopback0_mask': '255.255.255.255'
}

template = jinja2.Template(mytemplate)
output = template.render(vars)
# same as - output = template.render(**vars)
print(output)
