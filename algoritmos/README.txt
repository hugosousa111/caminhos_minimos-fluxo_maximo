1. Arquivo:
Todos os algoritmos foram implementados em um mesmo arquivo em python (main.py) que se encontra dentro da pasta (trabFinalGrafos) com todos os arquivos necessários para sua execução.

2. Instalação das dependências:
	2.1 Instalar o python3 e o pip:
			Sessão "Como Instalar Python no Ubuntu" do site:  https://www.hostinger.com.br/tutoriais/como-instalar-python-ubuntu/
	2.2 Instalar biblioteca Numpy com o comando: 
			sudo pip install numpy

3. Demais instruções:
	- Abrir arquivo "grafos.txt" e adicionar o grafo desejado respeitando o modelo.
	- Para executar utilize os comandos: 
		- cd "caminho dos arquivos"
		- python main.py

4. Observações:
	- Caso tenha algum problema durante a execução, o trabalho pode ser acessado e executado através da ferramenta Repl.it pelo link <https://repl.it/@RenanCardoso/trabFinalGrafos>.
	- Se o grafo analisado for grande (por exemplo: n>8 ), o algoritmo menorRecSTP(w) apresenta uma demora maior para executar, visto que é um algoritmo com métodos recursivos. Caso haja problemas, basta comentar a linha 396 do arquivo "main.py" (utilize # para comentar).