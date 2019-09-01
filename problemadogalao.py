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
        return self.representacao.__str__()

    
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


    def encontrarSolucao(self):  
        self.encontrouSolucao = False
        self.estadosVisitados = list([self.estadoAtual])

        #while not self.alcancaObjetivo(self.estadoAtual): 
        self.avaliar(self.estadoAtual.copy(), 1)
        print("fim")
        '''
        estadosCandidados = list()    
        estadosFilhos = self.getEstadosFilhos(
            self.estadoAtual
        )

        for estado in estadosFilhos:                
            if estado not in estadosVisitados:
                estadosCandidados.append(estado)                    

        if estadosCandidados.__len__() == 0:
            print("sem solucao")
            break

        print('%s %s' %(self.estadoAtual, self.estadoAtual.acao))
        estadosVisitados.append(estadosCandidados[0])
        self.estadoAtual = estadosCandidados[0]
        '''
        


    def avaliar(self, estadoAtual, stack):
        #print("start - " + str(stack))
        if self.alcancaObjetivo(estadoAtual):
            self.encontrouSolucao = True
            print("encontrou ----------------------------")
            return 
        
        if self.encontrouSolucao:
            #print("?")
            return

        estadosCandidados = list()    
        estadosFilhos = self.getEstadosFilhos(
            estadoAtual
        )

        for estado in estadosFilhos:                
            #if estado not in self.estadosVisitados:
                estadosCandidados.append(estado)                    

        # print(estadosCandidados.__len__())
        if estadosCandidados.__len__() == 0:
            #print("n deu - " + str(stack))
            return                    

        print('%s %s' %(estadoAtual, estadoAtual.acao))
        for i in range(estadosCandidados.__len__()):
            #print("letsgo")
            self.estadosVisitados.append(estadosCandidados[i])
            #print("biroliro")
            self.avaliar(estadosCandidados[i].copy(), stack+1)
            #print("prox")
        #print("ui")            

    #def verificarCaminho(self, estadoVerificar, estadosVisitados):



tabuleiro = Tabuleiro(
    Estado(
        #[[1, 2, 3], [8, -1, 6], [7, 4, 5]],
        #[[-1, 2], [1, 3]],
        [[3, -1], [2, 1]],
        None, 
        None, 
        0,
        0,
        #[1, 1]
        [0, 0]
    ),
    Estado(
        #[[1, 2, 3], [4, 5, 6], [7, 8, -1]]
        [[1, 2], [3, -1]]    
    )
)    

import sys
sys.setrecursionlimit(9999)
try:
    print(tabuleiro.encontrarSolucao())
except:
    print("except")

print("n deu erro")


# 3 coisas
# 1. Pq o script ta parando do nada, qual o motivo de ter parado?
# 2. pq a stack esta sendo printada linearmente e nao esta diminiindpo nos returns
# 3. Apagar os estados visitados ao dar o return, já que sao posibilidades a se visitar novamente ja que n seguiu certo caminho
# 4. Pq está printando None nas acoes dos estados?

