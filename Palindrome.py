# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:32:53 2021

@author: John Patrick
"""

def reverse(string):
 string = "".join(reversed(string))
 return string
st = input("Enter a Word:");
revst = reverse(st);
if st.lower() == revst.lower():
    print(st,"is Palindrome");
else:
    print(st,"is not a Palindrome");