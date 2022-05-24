#Modulos requeridos
import numpy as np
from math import dist as d
import matplotlib.pyplot as plt

class Coordenadas:
    #Se obtienen coordenadas de catálogo
    #Se crean coordenadas aleatorias
    def __init__(self,ruta_archivo):
        self.ruta_archivo = ruta_archivo
        
    def CoordenadasCat(ruta_archivo):
        catalogo = np.loadtxt(ruta_archivo)
        coordenadas = list(zip(np.append(catalogo[:1],catalogo[0]),np.append(catalogo[1:],catalogo[1])))
        return coordenadas
    
    def CoordenadasRand():
        coordenadas_random = 100*np.random.rand(1000,2)
        return coordenadas_random

class Distancia:
    def __init__(self,coordenadas,coordenadas_random):
        self.coordenadas = coordenadas
        self.coordenadas_random = coordenadas_random
        
    def distanciasCatalogo(coordenadas):
        #Distancias catalogo
        distancias = []
        for i in range(0,len(coordenadas)):
            for j in range(1000-i-1):
                distancias.append(d(coordenadas[i],coordenadas[i+j+1]))
        return distancias

    def distanciasRandom(coordenadas_random):
        #Distancias catalogo aleatorio
        distancias_rand = []
        for i in range(0,len(coordenadas_random)):
            for j in range(1000-i-1):
                distancias_rand.append(d(coordenadas_random[i],coordenadas_random[i+j+1]))
        return distancias_rand

    def distanciasCatRand(coordenadas,coordenadas_random):
        #Distancias catalogo x catalogo aleatorio
        distancias_cat_rand = []
        for i in range(0,1000):
            for j in range(1000-i-1):
                distancias_cat_rand.append(d(coordenadas[i],coordenadas_random[i+j+1]))
        return distancias_cat_rand

class HistogramasEstimadores:
    def __init__(self,distancias,distancias_rand,distancias_cat_rand):
        self.distancias = distancias
        self.distancias_rand = distancias_rand
        self.distancias_cat_rand = distancias_cat_rand
        
    def Histogramas_Estimadores(distancias,distancias_rand,distancias_cat_rand):
        #Histogramas
        #intervalos = [0,5,10,...,139] y color de barras
        intervalos = []
        color_barras = "#F2AB6D"
        
        for i in range(0,140,5):
            intervalos.append(i)
            
        #Impresion histograma dd(r)
        hp = []
        hp = plt.hist(distancias,bins=intervalos,color=color_barras)
        plt.title("dd(r)")
        plt.xlabel("Distancia")
        plt.ylabel("Frecuencia")
        plt.show()
        
        #Impresion histograma rr(r)
        hp_rr = []
        hp_rr = plt.hist(distancias_rand,bins=intervalos,color=color_barras)
        plt.title("rr(r)")
        plt.xlabel("Distancia")
        plt.ylabel("Frecuencia")
        plt.show()
        
        #Impresion histograma dr(rr)
        hp_dr = []
        hp_dr = plt.hist(distancias_cat_rand,bins=intervalos,color=color_barras)
        plt.title("dr(r)")
        plt.xlabel("Distancia")
        plt.ylabel("Frecuencia")
        plt.show()
        
        #####################################################################
        ################### ESTIMADORES ####################################
        ################### CON PARES ####################################
        ###################****************#############################
        pares_dd = []
        pares_dd = hp[0]
        plt.title("PARES DATA dd")
        plt.xlabel("Distancia")
        plt.ylabel("Frecuencia")
        plt.plot(pares_dd,'black')
        plt.show()
        
        pares_dr = []
        pares_dr = hp_dr[0]
        plt.title("PARES DATA_RANDOM dr")
        plt.xlabel("Distancia")
        plt.ylabel("Frecuencia")
        plt.plot(pares_dr,'black')
        plt.show()
        
        pares_rr = []
        pares_rr = hp_rr[0]
        plt.title("PARES RANDOM rr")
        plt.xlabel("Distancia")
        plt.ylabel("Frecuencia")
        plt.plot(pares_rr,'black')
        plt.show()
                
        LS = []
        ls_dd = []
        ls_dr = []
        ls_rr = []
        for i in range(len(pares_rr)):
            ls_dd.append(pares_dd[i] / 499500)
            ls_rr.append(pares_rr[i] / 499500)
            ls_dr.append((pares_dr[i] / 1000000)*2)
            LS.append((pares_dd[i] - pares_dr[i] + pares_rr[i]) / pares_rr[i])
        
        PH = []
        for i in range(len(pares_dd)):
            PH.append(pares_dd[i] / pares_rr[i] - 1)
        
        plt.title("Peebles & Hauser")
        plt.xlabel("s(h-1 Mpc)")
        plt.ylabel("ξ(s)")
        plt.plot(PH,'b')
        plt.show()
        
        plt.title("Landy & Szalay")
        plt.xlabel("s(h-1 Mpc)")
        plt.ylabel("ξ(s)")
        plt.plot(LS,'r')
        plt.show()
        
def main():
    print("                                                                               RESULTADOS Data_1")
    #********Se coloca la ruta********
    ruta = "../Servicio/Data_1.txt"
    #Se obtienen coordenadas de Data_1
    coord = Coordenadas.CoordenadasCat(ruta)
    coord_random = Coordenadas.CoordenadasRand()
    #Se obtienen distancias
    dd = Distancia.distanciasCatalogo(coord)
    rr = Distancia.distanciasRandom(coord_random)
    dr = Distancia.distanciasCatRand(coord,coord_random)
    #Histogramas
    HistogramasEstimadores.Histogramas_Estimadores(dd, rr, dr)
    
    print("                                                                               RESULTADOS Data_2")
    #Data_2
    ##********Se coloca la ruta********
    ruta2 = "../Servicio/Data_2.txt"
    #Se obtienen coordenadas de Data_2
    coord2 = Coordenadas.CoordenadasCat(ruta2)
    coord_random2 = Coordenadas.CoordenadasRand()
    #Se obtienen distancias
    dd2 = Distancia.distanciasCatalogo(coord2)
    rr2 = Distancia.distanciasRandom(coord_random2)
    dr2 = Distancia.distanciasCatRand(coord2,coord_random2)
    #Histogramas
    HistogramasEstimadores.Histogramas_Estimadores(dd2, rr2, dr2)

if __name__ == '__main__':
      main()


