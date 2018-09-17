#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):
    return ((-b+math.sqrt(b*b-4*a*c))/(2*a)) ,((-b-math.sqrt(b*b-4*a*c))/(2*a))
    
a ,b ,c =map(int, input('please enter 3 number for ax2+bx+c=0:').split())

slv1,slv2 = quadratic(int(a),int(b),int(c))

print('the solution of \'%sx2+%sx+%s=0\' are %s and %s' %(a,b,c,slv1,slv2))

