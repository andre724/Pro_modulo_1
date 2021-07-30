'''
Main module
'''

from functions import mult_check


a,b,c,d = map(int, input().split())

resultados=mult_check(a,b,c,d)

print(resultados)
