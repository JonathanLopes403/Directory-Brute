#!/usr/bin/python3
# Created by: Jonathan Lopes

from threading import Thread
import requests
from sys import argv

alvo = argv[1]
wordlist = argv[2]
cookie = ""
useragent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"

try:
    headers = {'Cookie': cookie, 'User-Agent': useragent}
except:
    pass

def brute(lista):
    global alvo
    for diretorio in lista:
        r = requests.get(f'{alvo}/{diretorio}')
        resposta =  r.status_code
        if resposta != 404:
            print (f'{alvo}/{diretorio} ({resposta})')
      
def attack(num):
    global wordlist
    arq = open(wordlist, 'r')
    linhas = arq.read().splitlines()

    n = num
    splited = [linhas[i::n] for i in range(n)]
    
    for i in range(n):
        #print (f'Thread {i}: {splited[i]}')
        t1 = Thread(target=brute, args=[splited[i]])
        t1.start()

attack(int(argv[3]))
