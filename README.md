# 🌳 Árvores Binárias de Busca (BST)

### Trabalho Acadêmico — Estruturas de Dados 2

**Implementação e demonstração prática de uma Árvore Binária de Busca utilizando Python.**

---

## 📚 1. Informações Acadêmicas

| Informação | Descrição |
|---|---|
| Instituição | Unipê — Centro Universitário de João Pessoa |
| Disciplina | Estruturas de Dados 2 |
| Professor | Edkallenn (Ed) |
| Aluno | João Batista |
| Tema | Árvores Binárias de Busca (BST) |
| Linguagem | Python 3 |
| Tipo de projeto | Acadêmico e educativo |
| Apresentação | Vídeo de 10 minutos |

---

## 📖 2. Sobre o Projeto

Este projeto foi desenvolvido como atividade acadêmica da disciplina de **Estruturas de Dados 2**, com o objetivo de demonstrar o funcionamento das Árvores Binárias de Busca, também conhecidas como *Binary Search Trees (BST)*.

A implementação foi realizada em Python e contempla as principais operações dessa estrutura de dados, permitindo compreender como os elementos são organizados, inseridos, pesquisados, removidos e percorridos.

Além da implementação, o projeto acompanha uma apresentação educativa que demonstra os conceitos teóricos e a execução prática dos algoritmos.

## 🎯 3. Objetivos

### Objetivo geral

Compreender e demonstrar o funcionamento de uma Árvore Binária de Busca por meio de uma implementação prática em Python.

### Objetivos específicos

- Compreender os conceitos de nós, raiz, filhos e folhas.
- Implementar a inserção de elementos.
- Desenvolver um algoritmo de busca.
- Implementar a remoção de nós.
- Demonstrar os percursos em ordem, pré-ordem e pós-ordem.
- Aplicar recursividade nas operações da árvore.
- Analisar a complexidade computacional.
- Executar testes práticos para verificar o funcionamento do programa.

---

## 🌲 4. O que é uma Árvore Binária de Busca?

Uma **Árvore Binária de Busca (BST)** é uma estrutura de dados hierárquica composta por nós, em que cada nó pode possuir até dois filhos.

Sua principal característica é a organização dos valores:

- Valores menores que o nó atual são armazenados na subárvore esquerda.
- Valores maiores são armazenados na subárvore direita.
- Cada subárvore também respeita essa propriedade.

Na implementação deste projeto, valores duplicados não são inseridos.

### Exemplo de estrutura

```text
             50
           /    \
         30      70
        /  \    /  \
      20   40  60   80
```

Nessa representação:

- **50:** nó raiz.
- **30 e 70:** filhos da raiz.
- **20, 40, 60 e 80:** nós folhas.
- **Subárvore esquerda:** contém valores menores que 50.
- **Subárvore direita:** contém valores maiores que 50.

Essa organização permite realizar buscas sem necessariamente percorrer todos os elementos.

---

## ⚙️ 5. Funcionalidades Implementadas

### 5.1 Inserção de elementos

A inserção permite adicionar novos valores à árvore, respeitando suas propriedades.

O algoritmo começa pela raiz e compara o novo valor com o nó atual.

Se for menor, continua pela esquerda. Se for maior, continua pela direita.

O processo é repetido recursivamente até encontrar uma posição disponível.

**Método utilizado:** `inserir()`

### 5.2 Busca de elementos

A busca verifica se determinado valor existe na árvore.

O algoritmo começa pela raiz e utiliza comparações para determinar qual caminho seguir.

A operação retorna:

- `True`: elemento encontrado.
- `False`: elemento não encontrado.

**Método utilizado:** `buscar()`

### 5.3 Remoção de elementos

A remoção exclui um valor preservando a organização da BST.

O algoritmo considera três situações:

**Caso 1 — Nó sem filhos:** o nó é removido diretamente.

**Caso 2 — Nó com um filho:** o nó é substituído por seu filho.

**Caso 3 — Nó com dois filhos:** utiliza-se o sucessor em ordem para substituir o valor removido, mantendo as propriedades da árvore.

**Método utilizado:** `remover()`

### 5.4 Percurso em ordem

Visita os elementos na sequência:

**Esquerda → Raiz → Direita**

Resultado:

```text
20, 30, 40, 50, 60, 70, 80
```

Esse percurso apresenta os valores de uma BST em ordem crescente.

### 5.5 Percurso pré-ordem

Visita os elementos na sequência:

**Raiz → Esquerda → Direita**

Resultado:

```text
50, 30, 20, 40, 70, 60, 80
```

### 5.6 Percurso pós-ordem

Visita os elementos na sequência:

**Esquerda → Direita → Raiz**

Resultado:

```text
20, 40, 30, 60, 80, 70, 50
```

---

## 🛠️ 6. Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3 | Implementação dos algoritmos |
| Visual Studio Code | Desenvolvimento e execução |
| Git | Controle de versões |
| GitHub | Hospedagem do código-fonte |
| OBS Studio | Gravação da apresentação |
| YouTube | Hospedagem do vídeo educativo |

O projeto utiliza exclusivamente recursos da biblioteca padrão do Python, sem necessidade de instalar dependências externas.

---

## 📁 7. Estrutura do Repositório

```text
trabalho-arvore-binaria-bst/
│
├── main.py
│   └── Implementação da árvore e testes
│
└── README.md
    └── Documentação do projeto
```

### Descrição dos arquivos

**main.py**

Contém a implementação das classes `No` e `ArvoreBST`, os algoritmos de inserção, busca, remoção, percursos e os testes de execução.

**README.md**

Contém a documentação, os objetivos, as funcionalidades, as instruções de execução e as informações da apresentação.

---

## 💻 8. Como Executar o Projeto

### Pré-requisitos

Antes de executar, é necessário possuir:

- Python 3 instalado.
- Um terminal ou editor de código.
- Os arquivos deste repositório.

### Passo 1 — Obter o projeto

Faça o download dos arquivos do repositório ou utilize o comando:

```bash
git clone URL_DO_REPOSITORIO
```

Substitua `URL_DO_REPOSITORIO` pelo endereço real do projeto.

### Passo 2 — Acessar a pasta

```bash
cd trabalho-arvore-binaria-bst
```

### Passo 3 — Executar o programa

```bash
python main.py
```

No Windows, também é possível utilizar:

```bash
py main.py
```

O programa criará uma árvore, realizará as operações implementadas e apresentará os resultados no terminal.

---

## 🧪 9. Testes e Resultados Esperados

A implementação utiliza inicialmente os seguintes valores:

```python
valores = [50, 30, 70, 20, 40, 60, 80]
```

O programa executa automaticamente:

1. Inserção dos valores.
2. Percurso em ordem.
3. Percurso pré-ordem.
4. Percurso pós-ordem.
5. Busca pelo número 40.
6. Busca pelo número 90.
7. Remoção do número 30.
8. Exibição da árvore após a remoção.

### Saída esperada

```text
TRABALHO - ESTRUTURAS DE DADOS 2
Aluno: Joao Batista

Arvore criada!
Em ordem: [20, 30, 40, 50, 60, 70, 80]
Pre-ordem: [50, 30, 20, 40, 70, 60, 80]
Pos-ordem: [20, 40, 30, 60, 80, 70, 50]

Buscando o numero 40:
Encontrado: True

Buscando o numero 90:
Encontrado: False

Removendo o numero 30:
Arvore apos remocao:
[20, 40, 50, 60, 70, 80]
```

### Interpretação dos resultados

Os testes demonstram que a árvore mantém seus elementos organizados de acordo com as propriedades da BST.

A busca pelo número 40 retorna verdadeiro porque ele está presente na estrutura.

A busca pelo número 90 retorna falso porque esse elemento não foi inserido.

Após a remoção do número 30, o percurso em ordem confirma que ele não está mais presente e que os demais valores continuam organizados.

---

## 📊 10. Análise de Complexidade

A eficiência das operações depende principalmente da altura da árvore.

| Operação | Árvore balanceada | Pior caso |
|---|---|---|
| Inserção | O(log n) | O(n) |
| Busca | O(log n) | O(n) |
| Remoção | O(log n) | O(n) |
| Percurso completo | O(n) | O(n) |

### Árvore balanceada

Quando os nós estão bem distribuídos, a altura da árvore tende a crescer de forma logarítmica.

Isso permite realizar operações de busca, inserção e remoção com eficiência.

### Árvore desbalanceada

Se os elementos forem inseridos em uma sequência crescente, por exemplo:

```text
10 → 20 → 30 → 40 → 50
```

Uma BST simples pode assumir uma estrutura semelhante a uma lista encadeada.

Nesse cenário, algumas operações podem apresentar complexidade O(n).

**Observação:** a implementação apresentada não realiza balanceamento automático, como ocorre em árvores AVL.

---

## 🌍 11. Aplicações Práticas

Árvores binárias de busca são importantes no estudo e desenvolvimento de estruturas de dados utilizadas em diferentes contextos.

Entre suas aplicações e conceitos relacionados estão:

- Implementação de conjuntos e mapas ordenados.
- Organização de informações para pesquisas.
- Estruturas de indexação em memória.
- Gerenciamento de dados hierárquicos.
- Desenvolvimento de estruturas de busca balanceadas, como árvores AVL e vermelho-preto.

A BST é uma base importante para compreender estruturas de dados mais avançadas.

---

## 🎥 12. Apresentação em Vídeo

O projeto acompanha um vídeo educativo de aproximadamente 10 minutos, produzido para a disciplina de Estruturas de Dados 2.

### Conteúdo da apresentação

1. Introdução às Árvores Binárias de Busca.
2. Conceitos e propriedades fundamentais.
3. Representação visual de uma BST.
4. Explicação da estrutura e inserção de nós.
5. Demonstração do algoritmo de busca.
6. Explicação da remoção de elementos.
7. Apresentação dos três tipos de percurso.
8. Execução prática do código em Python.
9. Análise de complexidade.
10. Considerações finais.

**Link do vídeo no YouTube:** [https://youtu.be/Sb4ScbCJs_4]

---

## 📌 13. Considerações Finais

O desenvolvimento deste projeto permitiu estudar e aplicar os principais conceitos relacionados às Árvores Binárias de Busca.

Por meio da implementação em Python, foi possível demonstrar como uma estrutura hierárquica organiza os elementos e realiza operações fundamentais, como inserção, pesquisa, remoção e percursos.

A atividade também possibilitou compreender a importância da recursividade e da análise de complexidade na construção de algoritmos eficientes.

Dessa forma, o projeto contribui para o aprendizado prático dos conteúdos abordados na disciplina de Estruturas de Dados 2.

---

## 👨‍💻 14. Autor

**João Batista**

Acadêmico do Unipê — Centro Universitário de João Pessoa.

Disciplina: Estruturas de Dados 2

Professor: Edkallenn (Ed)

**Projeto desenvolvido para fins acadêmicos e educacionais.**

---

**Unipê | Estruturas de Dados 2 | Árvores Binárias de Busca (BST)**
