import ast
import array
import datetime
import time
import sys
import timeit

def x_in_y(x,y):
    try:
        return x in y
    except Exception as e:
        return e

def x_ge_y(x,y):
    try:
        return x >= y
    except Exception as e:
        return e

def x_gt_y(x,y):
    try:
        return x > y
    except Exception as e:
        return e

def x_le_y(x,y):
    try:
        return x <= y
    except Exception as e:
        return e

def x_lt_y(x,y):
    try:
        return x < y
    except Exception as e:
        return e

def x_subset_y(x,y):
    try:
        return x.issubset(y)
    except Exception as e:
        return e

def x_issuperset_y(x,y):
    try:
        return x.issuperset(y)
    except Exception as e:
        return e

def x_isdisjoint_y(x,y):
    try:
        return x.isdisjoint(y)
    except Exception as e:
        return e

def x_startswith_y(x,y):
    try:
        return x.startswith(y)
    except Exception as e:
        return e

def x_endswith_y(x,y):
    try:
        return x.endswith(y)
    except Exception as e:
        return e

def x_inrange_y(x,y):
    try:
        return y.start <= x < y.stop
    except Exception as e:
        return e

data_sample = [1,2.0,
               [],[1],[1,'a'],
               set(),{1},{'a'},
               (),(1,2),('a',2.0),
               {'key' : 'val'},dict(),
               True, not False,
              "", "key",
             range(0), range(0,5),
             b'bytes',bytes(),
             bytearray(),
             array.array('i'),
             datetime.datetime(1990,12,12),
             datetime.datetime(199,12,12,14,0,0,0),
             datetime.time(1,1,1),
             datetime.time(2,1,1),
             None]

negate_kwords = ['','!']
reverse_kwords = ['','r_']
logical_kwords = ['in:', 'gt:', 'lt:', 'ge:', 'le:', 'eq:', 'sw:', 'ew:', 'bw:', 'iss:', 'iSS:', 'idj:','ir:']

all_kword_combinations = [f'{n}{r}{l}' for n in negate_kwords
     for r in reverse_kwords
     for l in logical_kwords]

conditions_sample = [
    f'{k}{d} '
    for k in all_kword_combinations
    for d in data_sample
    ]


convol = [(x,
           y,
           type(x),
           type(y),
           x==y, 
           not x ==y, 
           x_in_y(x,y),
           x_ge_y(x,y), 
           x_gt_y(x,y), 
           x_le_y(x,y), 
           x_lt_y(x,y),
           x_subset_y(x,y),
           x_issuperset_y(x,y),
           x_isdisjoint_y(x,y),
           x_startswith_y(x,y),
           x_endswith_y(x,y),
           x_inrange_y(x,y)
           ) for x in data_sample for y in data_sample]

convol_eq = len([x for x in convol if x[4] in [True, False]])
convol_neq = len([x for x in convol if x[5] in [True, False]])
convol_in = len([x for x in convol if x[6] in [True, False]])
convol_ge = len([x for x in convol if x[7] in [True, False]])
convol_gt = len([x for x in convol if x[8] in [True, False]])
convol_le = len([x for x in convol if x[9] in [True, False]])
convol_lt = len([x for x in convol if x[10] in [True, False]])
convol_issubset = len([x for x in convol if x[11] in [True, False]])
convol_issuperset = len([x for x in convol if x[12] in [True, False]])
convol_isdisjoint = len([x for x in convol if x[13] in [True, False]])
convol_startswith = len([x for x in convol if x[14] in [True, False]])
convol_endswith = len([x for x in convol if x[15] in [True, False]])
convol_inrange = len([x for x in convol if x[16] in [True, False]])


c=sys.getsizeof(convol)
print(c)
pass
