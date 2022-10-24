class Carro:
    def __init__(self, peneus, banco, volante, porta, ignição):
        self.peneus = peneus
        self.banco = banco
        self.volante = volante
        self.porta = porta
        self. ignição = ignição
o_carro = Carro('80cm de peneus', 'encostado no banco', 'girando volante', 'abrindo porta', 'giro à chave')
print(o_carro.porta, o_carro.banco, o_carro.ignição, 'com meus', o_carro.peneus, 'vou pela estrada cinuosa', o_carro.volante)