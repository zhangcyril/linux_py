#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-

class Calculator:
    name = 'Good calculator'
    price = 17
    def add(self,x,y):
        print(self.name)
        result = x + y
        print(result)
    def minus(self,x,y):
        result = x - y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)


