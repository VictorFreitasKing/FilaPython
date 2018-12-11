class Fila():
    def __init__(self):
        self.primeiro = None
        self.último = None
        self.__tamanho = 0
        self.__iterando = None

    class Nó():
        def __init__(self, conteúdo):
            self.conteúdo = conteúdo
            self.próximo = None

    def __len__(self):
        return self.__tamanho

    def __getitem__(self, i):
        atual = self.primeiro

        _índice_atual = 0
        while atual is not None:
            if _índice_atual == i:
                # encontrou o elemento desejado
                return atual.conteúdo

            # indo para o próximo elemento
            atual = atual.próximo
            _índice_atual += 1

        raise IndexError("list index out of range")

    def __setitem__(self, i, value):
        atual = self.primeiro

        _índice_atual = 0
        while atual is not None:
            if _índice_atual == i:
                # encontrou o elemento desejado
                atual.conteúdo = value
                return

            # indo para o próximo elemento
            atual = atual.próximo
            _índice_atual += 1

        raise IndexError("list index out of range")

    # Usado para proximas funcoes funcionarem
    def __iter__(self):
        return self

    # Percorre a lista com o auxilio da variavel self.__iternado, quando nao eh vazio retorna o valor
    def __next__(self):
        # vai percorrer utilizando o conceito de lazy evaluating
        if self.__iterando is None:  # começando início / começando a iterar
            self.__iterando = self.primeiro
        else:
            self.__iterando = self.__iterando.próximo

        if self.__iterando is not None:
            return self.__iterando.conteúdo

        raise StopIteration

    def __str__(self):
        retorno = '['
        for i, e in enumerate(self):
            retorno += e.__repr__()

            if i < len(self) - 1:
                retorno += ', '

        retorno += ']'

        return retorno

    def __repr__(self):
        return self.__str__()

    def enqueue (self, x):

        novo = self.Nó(x)

        # se não existem elementos na fila
        if self.primeiro is None:
            #o elemento inserido vai ser o unico na fila
            self.primeiro = novo
            self.último = novo

        else:
            # o que era último vai apontar para o novo
            self.último.próximo = novo

            # e o novo torna-se o último
            self.último = novo

        self.__iterando = None
        self.__tamanho += 1

    def denqueue (self):
        if self.__tamanho == 0:
            raise IndexError("Não existem elementos na fila")

        temp = self.primeiro
        if self.__tamanho >1:
            self.primeiro = self.primeiro.próximo
        if self.__tamanho == 1:
            self.primeiro = self.último = None
        self.__tamanho -= 1

        return temp
