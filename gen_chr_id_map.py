#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:11:48 2019

@author: jonahcullen
"""

id_map = {
    'NC_009144.3':'chr1',  'NC_009145.3':'chr2',  'NC_009146.3':'chr3',
    'NC_009147.3':'chr4',  'NC_009148.3':'chr5',  'NC_009149.3':'chr6',
    'NC_009150.3':'chr7',  'NC_009151.3':'chr8',  'NC_009152.3':'chr9',
    'NC_009153.3':'chr10', 'NC_009154.3':'chr11', 'NC_009155.3':'chr12',
    'NC_009156.3':'chr13', 'NC_009157.3':'chr14', 'NC_009158.3':'chr15',
    'NC_009159.3':'chr16', 'NC_009160.3':'chr17', 'NC_009161.3':'chr18',
    'NC_009162.3':'chr19', 'NC_009163.3':'chr20', 'NC_009164.3':'chr21',
    'NC_009165.3':'chr22', 'NC_009166.3':'chr23', 'NC_009167.3':'chr24',
    'NC_009168.3':'chr25', 'NC_009169.3':'chr26', 'NC_009170.3':'chr27',
    'NC_009171.3':'chr28', 'NC_009172.3':'chr29', 'NC_009173.3':'chr30',
    'NC_009174.3':'chr31', 'NC_009175.3':'chrX',  'NC_001640.1':'chrMt'
}



ensem_id_map = {}

def inc_range(start, end):
    return range(start, end+1)

for i in inc_range(1,31):
    ensem_id_map[str(i)] = 'chr' + str(i)
    
    if 'MT' or 'X' not in ensem_id_map:
        ensem_id_map['MT'] = 'chrMt'
        ensem_id_map['X'] = 'chrX'


def gen_ensem_id_map():
    
    ensem_id_map = {}
    
    def inc_range(start, end):
        return range(start, end+1)
    
    for i in inc_range(1,31):
        ensem_id_map[str(i)] = 'chr' + str(i)
        
        if 'MT' or 'X' not in ensem_id_map:
            ensem_id_map['MT'] = 'chrMt'
            ensem_id_map['X'] = 'chrX'
       
    return ensem_id_map        

test = gen_ensem_id_map()
