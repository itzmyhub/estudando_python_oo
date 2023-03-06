from collections import defaultdict
from collections import Counter

novo_dicionario = dict(Guilherme = 3, Joao = 2, Marcos = 3, Paula = 1)
print(novo_dicionario)

aparicoes = defaultdict(int)

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()
for palavra in meu_texto.split():
    aparicoes[palavra] += 1
print(aparicoes)
print(aparicoes.items())

#Testando o uso de diversas coleções

texto1 = """Ao desenvolver um projeto de programação temos que utilizar, muitas vezes, bibliotecas externas ao código feito para conseguir utilizar funcionalidades que já foram feitas por outras pessoas e que é possível utilizar, fazendo referência ao seu autor, economizando tempo de desenvolvimento.

Com o Java isso não é diferente: a linguagem usa dessas bibliotecas com pacotes inseridos em seu projeto Java, tais pacotes vêm de uma origem conhecida para que seja possível o processo de importação. Geralmente é feito o download da biblioteca e em seguida a importação dela no projeto.

Porém, a depender da complexidade do projeto, acaba sendo necessário o uso de diversas bibliotecas, que podem vir a ter problema na versão e/ou compatibilidade com o código; isso pensado em um projeto grande, passa a ser inviável realizar a importação e verificação de cada biblioteca manualmente.

Aqui entra o Maven: uma ferramenta de gerenciamento de dependências que foi feita em Java para auxiliar nos códigos feitos nesta linguagem.

Sobre o Maven (e breve história)
Ao falar da história que levou a sua criação, podemos citar duas ferramentas feitas em Java: Apache Ant e Apache Ivy.

A Apache Ant é uma ferramenta de automação de compilação no desenvolvimento de aplicações, em outras palavras, ela é quem auxilia o desenvolvedor a compilar os arquivos do projeto na ordem correta conforme dependência entre os arquivos. Este projeto é um software livre, com licença Apache.

Já a Apache Ivy é uma ferramenta de gerenciador de pacotes transitivos, Ivy é uma sub-parte do Apache Ant e possui sua funcionalidade focada em resolver as dependências de um projeto e também repositórios JAR, em especial, auxilia na integração e publicação de artefatos dos projetos que a utilizam. Também é um projeto de software livre, sob mesma licença.

O Apache Maven é uma ferramenta de gerenciamento e compreensão de projetos assim como o Apache Ant (ambas feitas em Java) porém possui conceitos e funcionalidades diferentes, em especial podemos falar da base do Maven que é o Modelo de Objeto de Projeto, este modelo organiza todas as informações do projeto em um único arquivo: o pom.xml.

Essa é a forma que o Maven realiza o Build do projeto, ou seja, conforme dependências são requisitadas, o POM é atualizado. O projeto Maven pode possuir módulos e cada módulo pode ter seu respectivo POM sem perder a organização e hierarquia do projeto principal. O Maven também auxilia na construção de relatórios e documentação.

Além disso, também é possível ter plugins que são fases individuais do projeto. O ciclo de vida de construção de um projeto também é um conceito muito importante no Maven, mas falaremos dele depois.

Instalação do Maven
A princípio temos como pré requisito a instalação do JDK, em especial na versão 1.7 ou superior. Após obter o JDK, independente do sistema operacional que esteja utilizando, podemos dar continuidade a instalação do Maven. Caso tenha dúvidas de como instalar o JDK, temos uma sugestão de leitura que pode te ajudar: Meu primeiro programa em Java.

Sobre o Maven, o próprio site sempre sugere o download da versão mais recente, porém também é possível usar versões anteriores. Em especial, é sugerido toda versão 3 em diante pois é uma versão estável desta ferramenta.

Instalando o Maven no Windows
Para instalar o Maven no Windows basta acessar este link para poder fazer o download. É possível baixar o arquivo binário ou o código fonte, conforme desejar. Neste artigo, vamos utilizar a versão 3.8.7 em seu formato binário."""

texto2 = """Quando estamos começando a fotografar, temos aquele pensamento que devemos buscar referências em outros fotógrafos da mesma área e então começamos a consumir o tempo todo apenas esse tipo de referência. É muito importante entendermos o que está sendo produzido atualmente e estudar também os grandes mestres. Essas pessoas são conhecidas por estarem fazendo com maestria seu trabalho e conseguindo comunicar suas narrativas de forma brilhante e quando estamos começando, precisamos de um ponto de partida. Nada mais justo. Mas será que essa é a única fonte de referência que podemos buscar ou corremos o risco de cair no erro de só reproduzir o que já está sendo feito?

Quando entramos no processo criativo e queremos criar imagens que nos representam, devemos lembrar que colocamos nessas imagens nossas experiências, nossa cultura, nossos gostos e aprendizados. Assim vamos criando nossa semiótica e construindo nosso inconsciente que irá transbordar na nossa fotografia. Termos noção que as nossas experiências fazem com que sejamos seres únicos no mundo é entender que ela nos ajuda a criar a nossa identidade e é o que vai trazer o nosso diferencial.

Estudando outros fotógrafos
Quando estamos começando os estudos, temos a tendência de copiar outros profissionais. Isso é normal e muitas vezes se dá por estarmos perdidos e não sabermos para onde ir e nem qual é a nossa identidade fotográfica. Queremos fazer belas fotos. Então olhe muitos trabalhos, estude esses profissionais e porque eles são considerados grandiosos. Estude os clássicos, os modernos e a partir daí você vai começar a separar o que você gosta e o que você não gosta.

Uma dica importante é: não é porque um artista é muito famoso que você precisa gostar dele ou de tudo o que ele faz. O interessante é começar a ter um olhar sobre o que você gosta dele.

Você gosta dos planos que ele trabalha?
Da iluminação que ele usa?
Da colorização das imagens?
Da produção e composição?
Das lentes que ele usa?
Vão ter infinitas particularidades e quando conseguimos separar elas, vamos criando a nossa identidade e passamos a não reproduzir mais uma cópia de outros trabalhos. Outros artistas servem para nos inspirar e ajudar a aprimorar a nossa técnica.

Procure saber o que fotógrafos de outras áreas estão produzindo. Olhar outras fontes pode trazer grandes insights e agregar novidades no seu trabalho. Fotógrafos de arquitetura podem te ensinar grandes dicas de enquadramento e perspectiva, por exemplo, se você quiser fazer selfies bacanas na sua casa.

E seguindo essa mesma linha de raciocínio, procure referências fora do eixo hegemônico. Somos bombardeados por uma estética estadunidense e européia (produzem coisas incríveis), mas você já procurou fotógrafos asiáticos, africanos e sul americanos? Vamos encontrar um mundo novo de comunicação e estética que pode abrir a sua mente para muitas possibilidades criativas.

Saindo da fotografia, podemos aprender muito com outras artes como o cinema, séries, videoclipes e pintura. Através deles podemos aprender sobre quase todas as áreas da fotografia.

Nos exemplos abaixo, temos alguns frames de filmes, séries ou clipes que nos ensinam muito sobre composição e narrativas. Vamos a eles:

O gambito da rainha"""


def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())
    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))


analisa_frequencia_de_letras(texto1)