
class Ponto:
    def __init__(self, x, y):# __init__ para criar um objeto / self permite que os métodos (def) acessem os atributos específicos de cada instância da classe
        self.x = x
        self.y = y

class Retangulo:
    def __init__(self, largura, altura, ponto_inicial):
        self.largura = largura
        self.altura = altura
        self.ponto_inicial = ponto_inicial

    def encontrar_centro(self): #Aqui é feito o cálculo das coordenadas do centro do retângulo , sem atributos, somente a referencia self
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y) #Retornado o resultado

def imprimir_valores_ponto(ponto):
    print(f"Coordenadas do ponto: ({ponto.x}, {ponto.y})")

def obter_valores():
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    x = float(input("Digite a coordenada x do vértice inferior esquerdo: "))
    y = float(input("Digite a coordenada y do vértice inferior esquerdo: "))
    ponto_inicial = Ponto(x, y) #cria o objeto ponto, pegando o valor de x e y como atributo
    return largura, altura, ponto_inicial

def main(): #Aqui começa a colocar pra rodar as funções
    largura, altura, ponto_inicial = obter_valores() #obtem os valores do retângulo.
    retangulo = Retangulo(largura=largura, altura=altura, ponto_inicial=ponto_inicial) # Cria o objeto retângulo
    centro = retangulo.encontrar_centro() #Faz as continhas
    imprimir_valores_ponto(centro) #Apresenta os resultados.

if __name__ == "__main__": # função main é chamada, sem isso não roda.
    main()
