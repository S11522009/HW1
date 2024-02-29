# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

variables = ['P', 'Q'] 
operations = ['and', 'or', 'not'] 

header = variables + [f'{var} not' for var in variables] + operations + [f'({var} implies {other_var})' for var in variables for other_var in variables] 
header += ['Result'] 
print("\t".join(header)) 

for p in [False, True]: 
    for q in [False, True]: 
        values = [p, q, not p, not q, p and q, p or q, not p and q, not p or q, p or not q, (not p or p) and (p or not p)] 
        result = values[0] or values[1] or values[2] or values[3] or values[4] or values[5] or values[6] or values[7] or values[8] or values[9] or values[10] 
        # 列印結果 
        row = [str(int(value)) for value in values] + [str(int(result))] 
        print("\t".join(row))
