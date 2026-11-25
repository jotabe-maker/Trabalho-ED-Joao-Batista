
# Estruturas de Dados 2 - Arvore Binaria de Busca
# Aluno: Joao Batista

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBST:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if no is None:
            return No(valor)

        if valor < no.valor:
            no.esquerda = self._inserir(
                no.esquerda, valor
            )
        elif valor > no.valor:
            no.direita = self._inserir(
                no.direita, valor
            )

        return no

    def buscar(self, valor):
        atual = self.raiz

        while atual is not None:
            if valor == atual.valor:
                return True
            elif valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return False

    def remover(self, valor):
        self.raiz = self._remover(self.raiz, valor)

    def _remover(self, no, valor):
        if no is None:
            return None

        if valor < no.valor:
            no.esquerda = self._remover(
                no.esquerda, valor
            )
        elif valor > no.valor:
            no.direita = self._remover(
                no.direita, valor
            )
        else:
            if no.esquerda is None:
                return no.direita

            if no.direita is None:
                return no.esquerda

            sucessor = no.direita

            while sucessor.esquerda is not None:
                sucessor = sucessor.esquerda

            no.valor = sucessor.valor
            no.direita = self._remover(
                no.direita, sucessor.valor
            )

        return no

    def em_ordem(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado

    def _em_ordem(self, no, resultado):
        if no is not None:
            self._em_ordem(no.esquerda, resultado)
            resultado.append(no.valor)
            self._em_ordem(no.direita, resultado)

    def pre_ordem(self):
        resultado = []
        self._pre_ordem(self.raiz, resultado)
        return resultado

    def _pre_ordem(self, no, resultado):
        if no is not None:
            resultado.append(no.valor)
            self._pre_ordem(no.esquerda, resultado)
            self._pre_ordem(no.direita, resultado)

    def pos_ordem(self):
        resultado = []
        self._pos_ordem(self.raiz, resultado)
        return resultado

    def _pos_ordem(self, no, resultado):
        if no is not None:
            self._pos_ordem(no.esquerda, resultado)
            self._pos_ordem(no.direita, resultado)
            resultado.append(no.valor)


def main():
    arvore = ArvoreBST()

    valores = [50, 30, 70, 20, 40, 60, 80]

    print("TRABALHO - ESTRUTURAS DE DADOS 2")
    print("Aluno: Joao Batista")

    for valor in valores:
        arvore.inserir(valor)

    print("\nArvore criada!")
    print("Em ordem:", arvore.em_ordem())
    print("Pre-ordem:", arvore.pre_ordem())
    print("Pos-ordem:", arvore.pos_ordem())

    print("\nBuscando o numero 40:")
    print("Encontrado:", arvore.buscar(40))

    print("\nBuscando o numero 90:")
    print("Encontrado:", arvore.buscar(90))

    print("\nRemovendo o numero 30:")
    arvore.remover(30)

    print("Arvore apos remocao:")
    print(arvore.em_ordem())


if __name__ == "__main__":
    main()
