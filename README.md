TRABALHO N1 TÉCNICAS DE PROGRAMAÇÃO - UNIVERSIDADE ANHEMBI MORUMBI (UAM)

Trabalho realizado pelo aluno Vinícius Rodrigues Martin RA: 21458710

------------------------------------------------------------------------------------------------------------------------------------------------------------------

CONTEXTO:

Muitos jogos de RPG são baseados em explorar dungeons, ou seja, explorar cavernas, calabouços, florestas e todo tipo de lugar desconhecido.

Hoje você será o líder de uma guilda de heróis! 

As regras para a travessia do labirinto são bastante simples. Toda a guilda começará na sala 1 e a partir dela pode-se escolher 2 opções diferentes:

•	1 – Caminho vermelho (ou direita);

•	2 – Caminho preto (ou esquerda);

Você precisará criar a lógica para fazer com que por meio de interações com o usuário seja possível avançar pelos caminhos do labirinto. 

O caminho preto da sala 8 leva à um local desconhecido, isso porque esta dungeon é controlada por criaturas místicas que dominam o tempo-espaço e criaram um portal! 
Toda vez que os personagens escolherem o caminho preto estando na sala 8 é preciso sortear o seu destino, podendo ser qualquer sala entre 1, 2, 3, 4 ou 5.

O seu programa deve fazer com que a guilda inicie na sala 1 e possa escolher entre o caminho vermelho e preto na estrutura indicada anteriormente. 

Ele deverá funcionar todo em console, não é preciso criar nenhum tipo de gráfico.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

REGRAS:

	Os heróis vencem ao chegar na Sala 9;

	A sala 6 tem realmente uma única possibilidade;

	Os heróis perdem se levarem 7 ou mais interações para chegarem na sala 9;

	Cada vez que os heróis escolhem um caminho é considerado 1 interação

	Você precisa utilizar um laço de repetição, podendo ser o comando “while”;

	Dentro do laço de repetição você poderá incluir somente UM BLOCO de comando “if” (com direito a um elif e um else, mas sem outros ifs internos) e NENHUM comando “switch-case” (os demais comandos não possuem limitação);

	Não pode usar nenhum if disfarçado de while.

	Fora do laço de repetição você poderá utilizar quantos comandos precisar.
