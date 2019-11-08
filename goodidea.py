#!/usr/bin/python3

import random

ragok  = ["-ébe", "-ében", "-éből", "-én", "-ére", "-éről", "-énél", "-éhez", "-étől", "-éig", "-ének", "-ért", "-ként"]
igek   = list(open('dic_verb.txt'))
mnevek = list(open('dic_adj.txt' ))
igenevek=list(open('dic_mi.txt'  ))
fonevek= list(open('dic_noun.txt'))

def gen_alany():
    jelzo1 = random.choice(mnevek).rstrip()
    alany  = random.choice(fonevek).rstrip() + random.choice(fonevek).rstrip() + "(k)"
    jelzo2 = random.choice(igenevek).rstrip()
    hatarozo = random.choice(fonevek).rstrip() + random.choice(ragok)
    return jelzo1 + " " + alany + " " + jelzo2 + " " + hatarozo

def gen_allitmany():
    ige_ve = random.choice(igek).rstrip() + "-ve"
    jelzo3 = random.choice(igenevek).rstrip()
    targy  = random.choice(fonevek).rstrip() + "-t"
    ige    = random.choice(igek).rstrip()
    return ige_ve + " " + jelzo3 + " " + targy + " " + ige + "(ik)"

for x in range(5):
    print(gen_alany() + " " + gen_allitmany())
