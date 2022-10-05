#n = []
#p = {"n":"BOM DIA!"}
#p1 = {"i":"SEMANA!"}
#n.append(p)
#n.append(p2)
#print('Na minha lista achei um..\n',(p["n"]),'\nE uma ótima:\n',(p2["i"]))



teste = {"maior":" drama","e":" mais drama",
"fazendo":" ainda mais drama",
"e":" claro mais drama"
}
for chave, textos in teste.items():
    print("O {} dos {} .".format(chave, textos))


#for chave in teste.values():
    #print(chave)
#for chave in teste.keys():
    #print(chave)

#for l in teste.items():
    #print("o grande {} não é nada além de {} e é claro {}".format(l))