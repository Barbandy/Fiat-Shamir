﻿#! /usr/bin/python
# coding: UTF-8

import random, BigInt


def GeneratePrime(bitLen):
    p = BigInt.GenerateRandomLen(bitLen)
    while not MillerRabin(p):
        p += 1
    return p

	
# тест Миллера-Рабина
def MillerRabin(m):
    m = m.getString()
    m = int(m)
    t = m - 1
    s = BigInt.BigInt(0)
    while t % 2 == 0:
        t /= 2
        s += 1
            
    for i in range(20):
        #a = BigInt.GenerateRandomMax(m-4)+2
        a = random.randint(1, m-1)
        x = pow(a,t,m)#m.powmod(a, t, m)
        if x == 1:
            return True # составное
    i = BigInt.BigInt(0)
    while i < s - 1:
        x = (x * x) % m
        if x == m - 1:
            return True
        i = i + 1
    return x == m - 1
				
		
# генерация ключей		
def KeyGen(bitlen):
   #3-е лицо генерирует простые  p,q и вычисляет n
    p = GeneratePrime(bitlen)
    q = GeneratePrime(bitlen)
    n = p*q
	# Алиса генерирует s ивычисляет v
    s = BigInt.GenerateRandomMax(n - 1)
    v = n.powmod(s,2,n)
    pub_key = "{}\n{}\n{}".format(n, v)
    print "pub_key ",pub_key
    priv_key = "{}\n{}".format(s, p, q)
    print "priv_key ",priv_key
    return pub_key, priv_key, n, s, v

	
def main():
    print "Fiat-Shamir"
    args = getArgs()
    bitlen = 16
			
    pub_key, priv_key, n, s, v = KeyGen(bitlen)
    # Проверка Алисы Бобом может быть сделана в четыре шага
	# 1 Алиса- претендент выбирает случайное число r (r называется "обязательство")
    r = BigInt.GenerateRandomMax(n - 1)
    print "r ",r
	# затем вычисляет значение x (x называется "свидетельство")
    x = n.powmod(r,2,n)
	# 2 Алиса передает x Бобу как свидетельство
    print "x  ",x
	# 3 Боб-верификатор передает вызов c Алисе. Значение c равно или 0, или 1
    ee = random.randint(0, 1)
    e = BigInt.BigInt(e)
    print "e ",e
	# 4 Алиса вычисляет свой ответ y = rs^c. 
    y = (r * n.powmod(s,e,n) % n)
    print "y ",y
	# 5 Алиса передает ответ Бобу, чтобы показать, что она знает значение своего секретного ключа, s. Она подтверждает, что это была именно Алиса
	
	# 6 Боб вычисляет y^2 и x^c. Если эти два значения являются конгруэнтными, то для Алисы значение s означает "она честна"; или она вычислила значение y другим способом ("она нечестная"), потому что мы можем легко доказать, что y - тот же самый, как x^c по модулю n
    y *= y 
    print "y^2",y
    yy = (x * n.powmod(v,e,n) % n) 
    print "yy",yy
    			
if __name__ == "__main__":
    main()	