## Como o programa traduz os critérios do CDD para a pontuação feita aqui?

1) Os indicadores de complexidade são a parte mais fácil. A identificação é objetiva e tranquila de ser feita.
Aqui consigo pontuar o uso de branchs, acoplamentos, operador ternário e iteração.

```

indicadores_de_complexidade = [

        "if",
        "else",
        "try",
        "Autowired",
        "?",
        ":",
        "switch",
        "case",
        "forEach"

]

```

2) Funções passadas como parâmetros


Aqui faço a identificação por meio do padrão existente na sequÊncia de parênteses e pontos.
O texto é tratado como uma lista inicialmente e filtrado apenas pelos parênteses e pontos.
Após isso transformado numa string.
Depois a contagem simples por meio do padrão '.(.())' -> já que f() = '.()' .: f(f()) -> '.(.())'
Acho que esse recurso pode ser bastante utilizado, tendo em vista a facilidade de se identificar uma função por meio de '.()'


```

regex1 = r'[)(.]' 

padrao_parenteses = re.findall(regex1, classe_analisada)

padrao_parenteses_string = ''.join(padrao_parenteses)

funcoes_como_parametro = padrao_parenteses_string.count('.(.())')


```

- 3) A ideia agora é fazer uma lista com a maior variedade de casos possíveis de situações de código que geraram 
aumento de complexidade. Partindo dessa lista, a ideia é tentar ir ajustando o programa para conseguir identificar 
cada situação.

- 4) Acho que uma ideia interessante também seria começar a gerar dados estatísticos por padrão em relação à complexidade
das classes.


### Considerações sobre o contador em python


- A ideia é automatizar o processo de contagem dos pontos de complexidade em determinada classe.

- O intuito de criar esse programa foi melhorar o aproveitamento de tempo e poder me aprofundar na teoria
do Cognitive Driven Development, tendo em vista que estar desenvolvendo esse algoritmo tem me conduzido, obviamente, a estudar 
a teoria com maior profundidade.

- Talvez já exista alguma forma automatizada, mas como não sabia, resolvi desenvolver esse algorítmo.

- Ainda está em fase inicial e cheio de bugs. Então serve só como início mesmo, ainda vou aprimorar.

- Os acoplamentos são contados por meio do Autowired (ainda preciso refinar esse mecanismo de contagem).

- Utilizei as classes que fiz no desafio da Casa do Código e do Ecommerce. Mudei só o Autowired que tinha usado antes, para PersistenceContext, para evitar que o EntityManager fosse pontuado.

- Ainda falta implementar identificação de funções como parâmetro, classes tipo Dto e Form e outros casos que
ainda estou pensando como vou identificar.

- Provavelmente tem formas mais fáceis de implementar esse algoritmo com bibliotecas como Numpy. Mas como não sei usar, estou implementando desse modo mesmo, depois vou mudando e simplificando o código.

- Também falta trazer esse algoritmo mais para a Orientação à Objetos. Ficou bem procedural até agora. Mas realmente é só um início para ver se consigo a possibilidade de efetivamente contar os pontos de complexidade de forma automatizada. O que poderia gerar uma agilidade interessante na hora de refatorar projetos via CDD. Inclusive permitindo um mapeamento rápido do perfil de complexidade das classes de um determinado projeto.

- Então a ideia agora seria melhorar a precisão da contagem automática, corrigindo bugs. E, depois, adaptar os argumentos recebidos no terminal para direcionar a análise a um projeto todo, e não mais apenas analisando uma classe por vez.