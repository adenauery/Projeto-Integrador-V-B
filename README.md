# Projeto Integrador V - B

Bem vindos ao repositório que será utilizado no PI V-B.

Após o Projeto Integrador o aluno deverá ser capaz de organizar soluções para armazenamento e disponibilização de materiais que explorem a convergência entre diferentes tipos de conteúdos. Estas soluções deverão prover diferentes perfis de acesso aos usuários, com mecanismos de seleção que empreguem recursos das diferentes mídias envolvidas, dentre os quais destacaríamos resumos textuais, miniaturas de imagens e/ou trechos dos vídeos a serem disponibilizados. Os materiais deverão poder ser recuperados pela Internet, sem restrições de local e/ou distância para acesso.

Neste **[link](https://docs.google.com/document/d/1gJrZ9nvX9VrMvw3FfVDizOWTzQQO4cLEClNY8xt7O_E/edit?usp=sharing)** está disponível o seu Plano de Execução.

### Professores Responsáveis

* Adenauer Yamin - adenauer.yamin at ucpel.edu.br
* Victoria Souto - victoria.souto at ucpel.edu.br

### Entrega Final

A Entrega Final, a qual compreende 60% da nota final, consistirá na elaboração de um Relatório em PDF referente a apropriação conceitual feita. Cada grupo de alunos irá discorrer sobre um tópico relevante no contexto das aplicações de Redes Convergentes, tendo por base o cenário das infraestruturas de comunicação modernas, as quais consideram o emprego de Redes de Longa Distância. Juntamente com o Relatório Final deverá ser também disponibilizado um vídeo que **trate do apresentado tanto no Relatório Parcial, como no Final.** Mais especificamente, no Relatório Final deverá ser incluído o link para acesso ao vídeo desenvolvido pelo grupo. O Relatório Final deverá ser entregue empregando a Plataforma A.

#### Abixo a equipe da disciplina:

* BRUNO LEMKE DOS SANTOS
* GUILHERME DE SOUZA DIAS
* HENDRIO BUTTOW PEREIRA
* MARCELO SOUZA DA ROSA
* PABLO DE SOUZA LOPES
* PAULO ARMANDO DA SILVA ALVES
* RODRIGO DOS SANTOS OLMOS
* RODRIGO VALADÃO

#### Tópicos Relevantes no Contexto das Aplicações das Redes Convergentes

Cada grupo (que pode ser de 1 ou mais integrantes) deverá selecionar um dos tópicos para trabalhar. Deverá ser gerado um texto entre 3 e 10 páginas, sendo estimulado o emprego de figuras.

* VoIP
* VoD
* OTT
* PPP 
* SLIP
* LAPB.
* L2TP
* PPTP.
* Arquitetura SIP
* Arquiteturas H.323
* RTP
* RTCP.
* MGCP
* Megaco
* MGCP.

## Programando Dispositivos na Internet das Coisas

### Embarcado que será utilizado:
* ESP32 - [Visão Geral & IoT](http://esp32.net/)
* ESP32 - [Mercado Livre](https://produto.mercadolivre.com.br/MLB-2043197044-esp32-doit-devkit-com-esp32-wroom-32d-e-certif-anatel-_JM#position=3&search_layout=grid&type=item&tracking_id=031cba6d-d510-44da-b601-1b3eb2af0e35)
* Observação sobre a pinagem da ESP3:
  * [Artigo que faz a discussão](https://blog.eletrogate.com/conhecendo-o-esp32-introducao-1/)
  * “Os Boards mais comuns encontrados aqui no Brasil , usam os módulos ESP-WROOM-32. Existem dois modelos de placas de desenvolvimento ESP32 DevKit, uma placa com 30 pinos e a outra com 38 pinos. As diferenças não são tão importantes, já que na Placa de 30 pinos não tem disponíveis os pinos para interface com o SD card ( SD0, SD1, SD2, SD3, CMD e CLK) . Não é recomendável o uso desses pinos, já que são usados pela memória Flash do módulo ESP32!”
  * Como ponto de partida, começar a desenvolver utilizando um ESP32 DevKit de 30 pinos.

### Linguagem que será utilizada:
* [MicroPython](http://olaria.ucpel.edu.br/micropython/)

### Instalando MicroPython
* [Instalando como uPyCraf](https://www.usinainfo.com.br/blog/micropython-esp32-parte-1/#:~:text=Instalando%20a%20IDE%20para%20trabalhar%20com%20Micropython%20ESP32&text=Primeiramente%2C%20acesse%20a%20p%C3%A1gina%20de,Caso%20haja%2C%20clique%20em%20atualizar)

### Ferramentas e Ambientes de Programação
* [Ambientes](http://olaria.ucpel.edu.br/micropython/doku.php?id=ferramentas). Como ponto de partida utilizar o ambiente de desenvolvimento uPyCraft

### Ambiente para Tratamento e Exibição dos Dados Coletados
* [ThingsBoard com Docker](https://thingsboard.io/docs/user-guide/install/docker/)
