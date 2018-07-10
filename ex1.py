#!/usr/bin/env python

import jinja2

mytemplate = """
router ospf {{ process_id }}
  network {{ network }} {{ wildcard }} area {{ area }}
  
"""

vars = {
    'process_id': 40,
    'network': '10.220.88.0',
    'wildcard': '0.0.0.255',
    'area': 0
}

template = jinja2.Template(mytemplate)
output = template.render(vars)
# same as - output = template.render(**vars)
print(output)
