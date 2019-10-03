class Estado:
    
    def __init__(self, representacao, pai=None, acao=None, custo=None, profundidade=None, ponteiro=None):
        self.representacao = representacao
        self.pai = pai
        self.acao = acao
        self.custo = custo
        self.profundidade = profundidade
        self.ponteiro = ponteiro        


    def __repr__(self):
        return self.__str__()


    def __str__(self):
        repr  = "\t%d\t%d\t%d\t\n" % (self.representacao[0][0], self.representacao[0][1], self.representacao[0][2])
        repr += "\t%d\t%d\t%d\t\n" % (self.representacao[1][0], self.representacao[1][1], self.representacao[1][2])
        repr += "\t%d\t%d\t%d\t\n" % (self.representacao[2][0], self.representacao[2][1], self.representacao[2][2])
        repr += "\n"
        return repr


    def __eq__(self, estado):
        if self.representacao == estado.representacao:
            return True

        return False


    def __getitem__(self, position):
        return self.representacao[position[0]][position[1]]


    def __setitem__(self, position, value): 
        self.representacao[position[0]][position[1]] = value


    def copy(self, movimento=None):        
        return Estado(
            self.copyRepr(),
            self,
            movimento,
            self.custo,
            self.profundidade,
            self.ponteiro.copy()
        )


    def copyRepr(self):
        repr = list()

        for line in self.representacao:
            linha = list()
            for column in line:
                linha.append(column)

            repr.append(linha)

        return repr


class Tabuleiro:

    def __init__(self, estadoInicial, estadoFinal):
        self.estadoAtual = estadoInicial
        self.estadoInicial = estadoInicial
        self.movimentosPossiveis = list([
            self.moverAbaixo,
            self.moverAcima,
            self.moverDireita,
            self.moverEsquerda
        ])
        self.estadoFinal = estadoFinal


    def moverEsquerda(self, estado):
        try:
            novoEstado = estado.copy(self.moverEsquerda)

            ponteiro = novoEstado.ponteiro
            valorEsquerda = novoEstado[ponteiro[0], ponteiro[1] - 1]
            novoEstado[ponteiro] = valorEsquerda
            novoEstado.ponteiro = [ponteiro[0], ponteiro[1] - 1]
            novoEstado[novoEstado.ponteiro] = -1
            novoEstado.acao = self.moverEsquerda
            novoEstado.profundidade += 1
            novoEstado.custo += 1
            
            if novoEstado.ponteiro[1] < 0:
                return None

            return novoEstado
        
        except IndexError:            
            return None


    def moverDireita(self, estado):
        try:
            novoEstado = estado.copy(self.moverDireita)

            ponteiro = novoEstado.ponteiro
            valordireita = novoEstado[ponteiro[0], ponteiro[1] + 1]
            novoEstado[ponteiro] = valordireita
            novoEstado.ponteiro = [ponteiro[0], ponteiro[1] + 1]
            novoEstado[novoEstado.ponteiro] = -1
            novoEstado.acao = self.moverDireita
            novoEstado.profundidade += 1
            novoEstado.custo += 1
            
            if novoEstado.ponteiro[1] > 2:
                return None
                
            return novoEstado
        
        except IndexError:            
            return None

    
    def moverAcima(self, estado):
        try:
            novoEstado = estado.copy(self.moverAcima)

            ponteiro = novoEstado.ponteiro
            valordireita = novoEstado[ponteiro[0] - 1, ponteiro[1]]
            novoEstado[ponteiro] = valordireita
            novoEstado.ponteiro = [ponteiro[0] - 1, ponteiro[1]]
            novoEstado[novoEstado.ponteiro] = -1
            novoEstado.acao = self.moverAcima
            novoEstado.profundidade += 1
            novoEstado.custo += 1
            
            if novoEstado.ponteiro[0] < 0:
                return None
                
            return novoEstado
        
        except IndexError:            
            return None
    

    def moverAbaixo(self, estado):
        try:
            novoEstado = estado.copy(self.moverAbaixo)

            ponteiro = novoEstado.ponteiro
            novaPosicao = [ponteiro[0] + 1, ponteiro[1]]
            valordireita = novoEstado[novaPosicao]
            novoEstado[ponteiro] = valordireita
            novoEstado.ponteiro = novaPosicao
            novoEstado[novoEstado.ponteiro] = -1
            novoEstado.acao = self.moverAbaixo
            novoEstado.profundidade += 1
            novoEstado.custo += 1
            
            if novoEstado.ponteiro[0] > 2:
                return None               
            
            return novoEstado
        
        except IndexError:            
            return None


    def getEstadosFilhos(self, estado):
        estadosFilhos = list()

        for movimento in self.movimentosPossiveis:
            novoEstadoFilho = movimento(estado)
            if novoEstadoFilho is not None:
                estadosFilhos.append(novoEstadoFilho)

        return estadosFilhos


    def alcancaObjetivo(self, estado):
        if estado == self.estadoFinal:
            return True

        return False


    def buscaLargura(self):

        self.estadosVisitados = [self.estadoAtual]
        lista = [self.estadoAtual]

        while (len(lista) > 0):
            no = lista.pop(0)

            if self.alcancaObjetivo(no):
                return no

            else:
                filhos = self.getEstadosFilhos(no)
                for f in filhos:                        
                    lista.append(f)

    
    def buscaProfundidade(self):

        self.estadosVisitados = [self.estadoAtual]
        lista = [self.estadoAtual]

        while (len(lista) > 0):
            no = lista.pop()

            if self.alcancaObjetivo(no):
                return no

            else:
                filhos = self.getEstadosFilhos(no)
                for f in filhos:                        
                    lista.append(f)


    def buscaProfundidadeLimitada(self, limite):
    
        self.estadosVisitados = [self.estadoAtual]
        lista = [self.estadoAtual]

        while (len(lista) > 0):
            no = lista.pop()

            if self.alcancaObjetivo(no):
                return no

            elif no.profundidade < limite:
                filhos = self.getEstadosFilhos(no)
                for f in filhos:                        
                    lista.append(f)


    def encontrarCaminho(self):
        # estado = self.buscaAprofundamentoIterativo(self.estadoAtual)
        # estado = self.buscaLargura()
        # estado = self.buscaProfundidade(self.estadoAtual)
        # estado = self.buscaProfundidadeLimitada(self.estadoAtual)
        estado = self.buscaCustoUniforme(self.estadoAtual)

        if estado is not None:
            pilha = []

            while estado != self.estadoInicial:
                pilha.append(estado.copy())
                estado = estado.pai

            while len(pilha) > 0:
                print(pilha.pop())

    
    def buscaAprofundamentoIterativo(self, estadoInicial):
        profundidade = 0

        while True:
            self.estadoAtual = estadoInicial
            resultado = self.buscaProfundidadeLimitada(profundidade)
            profundidade += 1

            if(resultado is not None):
                return resultado
            

    def buscaCustoUniforme(self, estadoInicial):

        lista = [self.estadoAtual]

        while (len(lista) > 0):
            lista = sorted(lista, key=lambda x: x.custo)
            no = lista.pop(0)           

            if self.alcancaObjetivo(no):
                return no

            else:
                filhos = self.getEstadosFilhos(no)
                for f in filhos:                        
                    lista.append(f)
            


tabuleiro = Tabuleiro(
    Estado(
        [[1, 5, 2], [7, 4, 3], [8, 6, -1]],
        None, 
        None, 
        0,
        0,
        [2, 2]
    ),
    Estado(
        [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
    )
)    

print(tabuleiro.estadoInicial)
tabuleiro.encontrarCaminho()


