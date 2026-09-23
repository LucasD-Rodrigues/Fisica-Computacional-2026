--- PROJETO 1 ---
O primeiro projeto da disciplina consiste em usar o método de Monte Carlo para aproximar o valor de pi com precisão arbitrária, 
comparando as propriedades de alguns códigos diferentes, como tempo de execução, como o erro escala com o número de entradas, 
e uma visualização gráfica do processo de sorteio de pontos.

Após utilizar sorteios aleatórios para calcular o valor de pi por meio da probabilidade de um par ordenado aleatório se encontrar dentro de um
círculo de raio 1, foi possível obter a seguinte figura como visualização desse processo

<figure align="center">
  <img src="pontos-circulo.png" width="400" alt="Sorteio de pontos via Monte Carlo">
  <figcaption>Figura 1: Visualização do sorteio de pontos no método de Monte Carlo.</figcaption>
</figure>

aqui são usadas N = 1000 pontos espalhados para estimar o valor de pi no código "lento" com laços e estruturas de decisão. O próximo objetivo é implementar uma versão "rápida" do código utilizando vetorização via NumPy e eliminar as estruturas decisórias com lógica Booleana. Feito isso, é possível identificar de que maneira o erro relativo ao valor de pi implementado no NumPy escala com o número de pontos usado para a estimativa, resultando nos painéis a seguir

<figure align="center">
  <img src="fig-erro" width="400" alt="Erros">
  <figcaption>Figura 2: Erro relativo em função do número de pontos em escalas variadas.</figcaption>
</figure>





