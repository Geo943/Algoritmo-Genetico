from math      import sqrt, log
from itertools import permutations as permutaciones
from itertools import islice as rango
from random    import randrange as aleatorio
from random    import random
from graphviz  import Digraph

metros = {}
def fact(n): return 1 if n < 2 else n * fact(n-1)
def parserarrayaristas(file):
    fcd = open(file,"r")
    datos = fcd.readlines()
    fcd.close()
    arrayaristas = []
    for i, linea in enumerate (datos):
        nums = linea.split(", ")
        arrayaristas.append(arista(i, str(nums[0]), str(nums[1]), str(nums[2]), float(nums[3]), float(nums[4]), float(nums[5]), float(nums[6]), float(nums[7]), float(nums[8])))
    return arrayaristas
class arista:
    def __init__(self, id, dir, org, dest, dist, tip, vel, trf, acc, sem):
        self.__id = id
        self.__dir = dir
        self.__org = org
        self.__dest = dest
        self.__dist = dist
        self.__tip = tip
        self.__vel = vel
        self.__trf = trf
        self.__acc = acc
        self.__sem = sem
    def __str__(self):
        return "%d" % (self.__id)
    def __del__(self):
        del self.__id
        del self.__dir
        del self.__org
        del self.__dest
        del self.__dist
        del self.__tip
        del self.__vel
        del self.__trf
        del self.__acc
        del self.__sem
    def getid(self):
        return self.__id
    def getdir(self):
        return self.__dir
    def getorg(self):
        return self.__org
    def getdest(self):
        return self.__dest
    def getdist(self):
        return self.__dist
    def gettip(self):
        return self.__tip
    def getvel(self):
        return self.__vel
    def gettrf(self):
        return self.__trf
    def getacc(self):
        return self.__acc
    def getsem(self):
        return self.__sem
class cromosoma:
    def __init__(self, arrayaristas = []):
        self.__arrayaristas = list(arrayaristas)
    def copy(self):
        return cromosoma( self.getarrayaristas())
    def __del__(self):
        while self.__arrayaristas:
            arista = self.__arrayaristas.pop()
        del arista
    def getarrayaristas(self):
        return self.__arrayaristas
    def __str__(self):
        s  = "["
        for arista in self.getarrayaristas() :
            s += " %s," % (str(arista))
        return s
    def costo(self, nd1):
        a = nd1
        key = "%d" % a.getid()
        if key in metros:
            mt = metros[key]
        else:
            d = a.getdist()
            t = a.gettip()
            tr = a.gettrf()
            ac = a.getacc()
            s = a.getsem()
            t = t*(tr+0.25*ac)+0.5*s
            v = (d/t)*0.06
            mt = v * 10
            metros[key] = mt
        return mt
    def aptitud( self ):
        apt = 0
        orig = sorted(self.getarrayaristas(), key=lambda x: x.getid(), reverse=False)
        for a in orig:
            apt += self.costo(a)
        return apt
    def __cmp__(self, otro):
        return int(self.aptitud() - otro.aptitud())
    def index( self, nodo ):
        return self.__arrayaristas.index(nodo)
    def cruzar(self, otro):
        p1, p2 = self.getarrayaristas(), otro.getarrayaristas()
        h1, h2 = list(p2), list(p1)
        idx = [0]
        i = 0
        cont = True
        while cont:
            ciudad = p2[i]
            i = p1.index(ciudad)
            idx.append(i)
            cont = not p1[0] is p2[i]

        for i in idx:
            h1[i], h2[i] = h2[i], h1[i]

        return cromosoma(h1), cromosoma(h2)
    def mutar(self):
        lista = self.getarrayaristas()
        mitad = len(lista)//2
        ini = aleatorio(0, mitad)
        fin = aleatorio(mitad, len(lista))
        a, b, c = lista[0:ini], lista[ini:fin], lista[fin:]
        b.reverse()
        del self.__arrayaristas
        self.__arrayaristas = a + b + c
        del a
        del b
        del c
def sort( self ):
	self.__arrayaristas.sort()
def desvestandar(poblacion =[]):
	tam = len(poblacion)
	aptitudes = map(cromosoma.aptitud, poblacion)
	xprom = sum(aptitudes)/tam
	desvs = sqrt(sum(map(lambda x: (x-xprom)**2, aptitudes))/ (tam - 1))
	return desvs, xprom
def mutarPoblacion( pop, pmuta ):
	for p in pop:
		if pmuta > random():
			p.mutar()
def cruzarpob( pob, pcruza ):
	padres = list( pob )
	hijos = list()

	if len(padres) % 2:
		if random() > 0.5:
			padres.pop( aleatorio(0, len(padres)))
		else:
			padres.append( padres[aleatorio(0, len(padres))] )

	while padres:
		a = padres.pop(aleatorio(0,len(padres)))
		b = padres.pop(aleatorio(0,len(padres)))

		if pcruza > random() :
			hijos.extend( a.cruzar(b) )

	return hijos
def generapob(arrayaristas, pob):
	s     = list()
	perms = permutaciones(arrayaristas)
	fin   = aleatorio( pob, fact( len(arrayaristas) ) )
	ini   = fin - pob

	Sigma = list(rango(perms, pob))

	for sigma in Sigma:
		k = list(sigma)
		s.append(cromosoma(k))

	for k in range(2):
		mutarPoblacion(s,1.0)

	return s
def imprimepob( pob ):
	n      = int( log( len(pob),10) + 1 )
	s      = " | %" + str(n) + "d | %s | %f\n"
	edge= " +" + (n + 2) * "-" + "+" + (len(str(pob[0])) + 2) * "-" + "+\n"
	strpob = edge
	for i, p in enumerate(pob):
		strpob += s % (i+1,str(p), p.aptitud() )

	return strpob + edge
def selecciona(poblacion, pobtam):
	p = list(poblacion)
	p.sort()
	return p[:pobtam]
def seleccionOE(poblacion = []):
    poblacion.sort()
    s, prom = desvestandar(poblacion)
    n = len(poblacion)
    prob = lambda r: (1-s)/(1-s**n)*(s**(r-1))
    probabilidades = map(prob, range(n))
    probacumulada  = 0
    pacumuladas    = []
    elegidos       = []
    pobtam = 20

    for probabilidad in probabilidades:
        probacumulada += probabilidad
    pacumuladas.append(probacumulada)
    print("*" *50 ,probacumulada)

    for k in range(len(poblacion)):
        cota = random()
        i = 0
        while i < len(pacumuladas) and pacumuladas[i] < cota :
            i += 1
        elegidos.append( poblacion[i] )

    return elegidos[:pobtam]
def selecciont(poblacion, tampob):
	selec = list()
	for k in [1,2]:
		participantes = list(poblacion)
		if len(participantes)%2 ==1:
			if k==1:
				participantes.pop(aleatorio(0, len(participantes)))
			else:
				participantes.append(participantes[aleatorio(0, len(participantes))])
		while participantes:
			a= participantes.pop(aleatorio(0, len(participantes)))
			b= participantes.pop(aleatorio(0, len(participantes)))
			ganador = a if str(a) < str(b) else b
			selec.append(ganador)
	sorted(str(selec))
	return selec[:tampob]
def genetico(ciudades, pobtam, pcruza, pmuta, generaciones ):
	poblacion = generapob(ciudades, pobtam)
	mejores = list()
	sorted(str(poblacion))
	mejor = poblacion[0]
	mejores.append(mejor.copy())
	selec = selecciont(poblacion, pobtam)
	continua = True
	i = 1
	while continua and i < generaciones:
		print (i, ") comenzando generacion")
		i+=1
		print (imprimepob(selec))
		hijos = cruzarpob(selec, pcruza)
		selec.extend(hijos)
		mutarPoblacion(selec, pmuta)
		selec = selecciont(selec, pobtam)
		sorted(str(selec))
		mejores.append(selec[0].copy())
		if(len(mejores)>1):
			aux=list(mejores)
			sorted(str(aux))
			n=aux.count(aux[0])
			if(len(mejores)>=10 and n>len(aux)/2):
				continua= False
	sorted(str(mejores))
	return mejores[0]
def crear(arrayaristas):
    caminos = list()
    for arista in arrayaristas:
        camino = buscar(arista, arrayaristas)
        if camino not in caminos:
            caminos.append(camino)
    return caminos
camino = []
tmpcamino = []
def buscar(aristaOriginal, arrayaristas):
    global camino
    global tmpcamino
    tmpcamino.append(aristaOriginal)
    for arista in arrayaristas:
        if aristaOriginal.getdest() == arista.getorg():
            buscar(arista, arrayaristas)
        elif aristaOriginal.getdir() == 'SALIDA':
            if len(tmpcamino) > 3:
                camino = tmpcamino
                tmpcamino = []
                break
    return camino
def eliminar(lista):
    return list(dict.fromkeys(lista))
padres = []
def buscarM(origen, arrayaristas):
    for arista in arrayaristas:
        if arista.getdest() == origen:
            padres.append(arista)
            buscarM(arista.getorg(), arrayaristas)
    return padres
def main():
    arrayaristas = parserarrayaristas("arrayaristas.txt")
    dot = Digraph(comment='Original')
    for arista in arrayaristas:
        dot.node(arista.getorg())
    for arista in arrayaristas:
        dot.edge(arista.getorg(), arista.getdest(), str(arista.gettrf()))
    dot.render('resultados/grafo.pdf', view=True)
    tamaño = 4
    cruzamiento = 0.9
    mutaciones = 0.5
    generaciones = 20
    caminos = crear(arrayaristas)
    respuestas = list()
    for camino in caminos:
        respuestas.append(genetico(eliminar(camino), tamaño, cruzamiento, mutaciones, generaciones ))
    size = len(respuestas)
    respuestaFinal = list()
    for i in range(size-1):
        if respuestas[i].aptitud() > respuestas[i+1].aptitud():
            respuestaFinal = respuestas[i+1]
        elif respuestas[i].aptitud() < respuestas[i+1].aptitud():
            respuestaFinal = respuestas[i]
    print ("Mejor camino: ")
    print (respuestaFinal, "]-- Con un costo final de ", int(respuestaFinal.aptitud()), ".")
    dot2 = Digraph(comment='Mejor camino')
    for arista in sorted(respuestaFinal.getarrayaristas(), key=lambda x: x.getid(), reverse=True):
        dot2.node(arista.getorg())
        dot2.edge(arista.getorg(), arista.getdest(), str(arista.gettrf()))
    lista = sorted(respuestaFinal.getarrayaristas(), key=lambda x: x.getid(), reverse=True)
    padre = None
    while padre is None:
        padre = buscarM(lista[0].getorg(), arrayaristas)
    if padre is not None:
        if len(padre) > 0:
            for hijo in padre:
                if hijo not in respuestaFinal.getarrayaristas():
                    dot2.node(hijo.getorg())
                    dot2.edge(hijo.getorg(), hijo.getdest(), str(hijo.gettrf()))
    dot2.body = eliminar(dot2.body)
    dot2.render('resultados/grafo.pdf', view=True)
if __name__ == "__main__":
	main()