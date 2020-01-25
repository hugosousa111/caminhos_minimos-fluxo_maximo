import math # bib para usar o valor infinito 
import numpy as np # bib para facilitar no uso de matrizes 

def calcArestas():
  arquivo = open("grafos.txt","r")    
  texto = arquivo.readlines()
  arquivo.close()
  arestas = texto[2:]
  return arestas
	

def matrizPesos():
	# pega o arquivo de entrada e transforma em uma matriz de adjacencia
  arquivo = open("grafos.txt","r")    
  texto = arquivo.readlines()
  arquivo.close()
  nVertices = int(texto[0].split()[0])
  arestas = texto[2:]

  w = np.zeros( (nVertices,nVertices) )
  for i in range(0,nVertices):
    for j in range(0,nVertices):
      if i != j:
        w[i,j] = math.inf
       
  for i in arestas:
    j = i.split()
    w[int(j[0]),int(j[1])] = float(j[2])

  return w


def raiz():
  arquivo = open("grafos.txt","r")    
  texto = arquivo.readlines()
  arquivo.close()
  vPai = int(texto[1].split()[0])
  return vPai


def fonte_sorvedouro():
  arquivo = open("grafos.txt","r")    
  texto = arquivo.readlines()
  arquivo.close()
  f = int(texto[1].split()[0])
  s = int(texto[1].split()[1])
  return f, s
	
###############################################

def floydWarshall(w):
  d = np.copy(w)
  n = len(w)

  for k in range(n):
    for i in range(n):
      for j in range(n):
        if (d[i,j] > (d[i,k] + d[k,j])):
          d[i,j] = d[i,k] + d[k,j]

  print(d)
	
###############################################

def calcSTP(w,i,j,m):
  if i == j: return 0
  if m == 1: return w[i,j]

  c = math.inf

  for k in range(len(w)):
    if c > (calcSTP(w,i,k,m-1) + w[k,j]):
      c = calcSTP(w,i,k,m-1) + w[k,j]
  return c


def menorRecSTP(w):
  l = np.copy(w)
  for i in range(len(w)):
    for j in range(len(w)):
      l[i,j] = calcSTP(np.copy(w),i,j,len(w))
  
  print(l)
  #return l

####################################################

def STP(l):
  nVertices = len(l)
  l2 = np.zeros((nVertices,nVertices))
  
  for i in range(0,nVertices):
    for j in range(0,nVertices):
      if i != j:
        l2[i,j] = math.inf

  for i in range(nVertices):
    for j in range(nVertices):
      c = l[i,j]
      for k in range(nVertices):
        if c > (l[i,k] + l[k,j]):
          c = l[i,k] + l[k,j]
      l[i,j] = c

  return l 

def mainSTP(w):
  l = np.copy(w)
  for i in range(1, len(w)):
    l = STP(l)
  print(l)

###############################################

def inicializa(w):
	# funcao inicializa do bellman-ford
  G = np.copy(w)
  n = len(G)
  for i in range(0,n):
    for j in range(0,n):
      if i != j:
        G[i,j] = math.inf
  return G


def relax(s, u, v, g2, w, pai): 
  if (g2[s, v] > (g2[s, u] + w[u,v])):
    g2[s, v] = g2[s, u] + w[u,v]
    pai[v] = u
    return 1
  return 0


def bellmanFord(w, raiz):
  g2 = inicializa(w)
  arestas = calcArestas()

  pai = np.zeros(len(w))
  pai_v = np.copy(pai)

  for i in range(0,len(w)):
    pai[i] = -1
  pai[raiz] = raiz


  for v in range(len(g2)):
    for i in range(len(g2) - 1):
      for row in arestas:
        j = row.split()
        relax(v, int(j[0]), int(j[1]), g2, w, pai)

    for row in arestas:
      j = row.split()
      if relax(v,int(j[0]), int(j[1]),g2,w,pai) == 1:
        print("Tem Ciclo Negativo!")
        return False
    
    if v == raiz:
      pai_v = np.copy(pai)

    pai = np.zeros(len(w))
    for i in range(0,len(w)):
      pai[i] = -1
    pai[raiz] = raiz
    
  print(g2)
  print("\nCaminhos Mínimos: ")
  exibeCaminhos(g2, pai_v, raiz)
  return True


def exibeCaminhos(g2, pai_v, raiz):
  for v in range(1, len(g2)):
    path = []
    pai_atual = -1
    path.append(v)

    while(pai_atual != raiz): 
      path.append(int(pai_v[v]))
      pai_atual = pai_v[v]
      v = int(pai_atual)
    

    pathInv = path[::-1]
    print(pathInv[0],end="")
    for i in pathInv[1:]:   
      print("->",end="")
      print(i, end="")
      
    print("")

###############################################
def inicializa_max(w):
	# funcao inicializa do bellman-ford
  G = np.copy(w)
  n = len(G)
  for i in range(0,n):
    for j in range(0,n):
      if i != j:
        G[i,j] = -1 #######
  return G

def relax_inv(s, u, v, g2, w, pai): 
  if (g2[s, v] < (g2[s, u] + w[u,v])): #########
    g2[s, v] = g2[s, u] + w[u,v]
    pai[v] = u
    return 1
  return 0

def exibeCaminhos_max(g2, pai_v, raiz, s):
  for v in range(0, len(g2)):
    path = []
    pai_atual = -1
    path.append(v)

    while(pai_atual != raiz): 
      path.append(int(pai_v[v]))
      pai_atual = pai_v[v]
      v = int(pai_atual)

    pathInv = path[::-1]
    
    if pathInv[-1] == s:
      return pathInv

def bellmanFord_Max(w3, raiz, s):
  
  g2 = inicializa_max(w3)
  
  pai = np.zeros(len(w3))
  for i in range(0,len(w3)):
    pai[i] = -1
  pai[raiz] = raiz

  pai_v = np.zeros(len(w3))

  for v in range(len(g2)):
    for l in range(len(w3)):
      for c in range(len(w3)):
        if w3[l,c] != math.inf and w3[l,c] != 0:
          relax_inv(v, l, c, g2, w3, pai)	  

    if v == raiz:
      pai_v = np.copy(pai)

    pai = np.zeros(len(w3))
    for i in range(0,len(w3)):
      pai[i] = -1
    pai[raiz] = raiz
  
  #print("w3")
  #print(w3)

  #print("g2[f,:]")  
  #print(g2[f,:])
  p = exibeCaminhos_max(g2, pai_v, raiz, s)
  
  return p
			
def fordFurkelson(w,f,s):
  w2 = np.copy(w)

  fluxo = 0
  
  while(True):
    
    path = bellmanFord_Max(w2, f, s)
    #print("path")
    #print(path)
    
    arestas_path = []
    for i in range(len(path)-1):
      arestas_path.append(w2[path[i],path[i+1]])
    minimo = min(arestas_path)
    fluxo += minimo
    for i in range(len(path)-1):
      w2[path[i],path[i+1]] -= minimo
    
    if any(i == -1 for i in path):
      break
    
    #print("w2")
    #print(w2)
    #print("fluxo")
    #print(fluxo)	

  print("\nGrafo Residuo")
  print(w2)
  print("\nFluxo Max")
  print(fluxo)	

###############################################

def inicializaPR(w,f): 
  h = np.zeros(len(w))
  e = np.zeros(len(w))
  
  c = np.copy(w)
  flu = np.copy(w)
  for l in range(len(w)):
    for j in range(len(w)):
      flu[l,j] = 0

  for l in range(len(w)):
    for j in range(len(w)):
      if w[l,j] == math.inf:
        c[l,j] = 0        
  
  h[f] = len(w)
  e[f] = math.inf
  
  for l in range(len(w)):
    if c[f,l] != 0:# or c[l,f] != 0:
      flu[f,l] = c[f,l]
      flu[l,f] = -c[f,l] ####### estranho
      #flu[l,f] -= c[f,l] ####### estranho
      e[l] = c[f,l]
      e[f] = e[f] - c[f,l]
  
  return h, e, flu, c

def push(u,v,e,c,flu):
  # cf[u,v] > 0 
  cf = c[u,v] - flu[u,v]
  d = min(e[u],cf)
  flu[u,v] = flu[u,v] + d
  flu[v,u] = -flu[u,v] ######### estranho
  #flu[v,u] -= d ######### estranho
  e[u] = e[u] - d
  e[v] = e[v] + d

def relabel(u,c,flu,h,w):
  m = math.inf 
	# descobrindo o mínimo
  for i in range(len(w)):
    cf = c[u,i] - flu[u,i]
    if cf>0:
      if h[i]<m:
        m = h[i]

  h[u] = 1 + m
	
def push_relabel(w,f,s):
  h, e, flu, c = inicializaPR(w,f)
  for j in range(len(w)*len(w)):
    for u in range(len(w)):
      if e[u]>0 and u!=f and u!=s:
        relabel(u,c,flu,h,w)
        for v in range(len(w)): 
          cf = c[u,v] - flu[u,v]
          if cf != 0:
            if h[u] == h[v]+1:
              #if w[u,v] != math.inf:
              push(u,v,e,c,flu)

  print("\nflu")
  print(flu)
  print("\nc - flu")
  print(c - flu)

  fluxo = 0
  for i in range(len(w)):
      fluxo += flu[i,s]
	
  print("\nFluxo Máximo: ")
  print(fluxo)

###############################################
w = matrizPesos()
print("Matriz de pesos (Grafo)")
print(w)

try: 
  
  f,s = fonte_sorvedouro()
  print(f,s)
  print("\n**** Parte 2 -> Fluxo Maximo ****")
  
  print("\n** Ford Fulkerson **")
  fordFurkelson(w,f,s)  

  print("\n** Push-Relabel **")
  push_relabel(w,f,s)  
  
except IndexError: 

  print("\n**** Parte 01 Caminhos Mínimos ****")

  print("\n** Bellman-Ford **")
  if bellmanFord(w, raiz()):
  
    print("\n** Floyd Warshall **")
    floydWarshall(w)

    print("\n** Shortest-Path **\n(Versão: Menor Rec)")
    menorRecSTP(w)

    print("\n** Shortest-Path **")
    mainSTP(w)