import pandas as pd #introducem biblioteca pentru manipularea si utilizarea datelor
import matplotlib.pyplot as plt #introducem biblioteca pentru a crea vizualizari si grafice
#definirea variabilelor
X = 5
Y = 10

#definirea functiei creaaza_graf
def creaza_graf(titlu, data): #functie cu titlu si set de date in format data frame, structura de date oferita de pandas
    durata = data['Durata']
    puls = data['Puls']
    max_puls = data['MaxPuls']
    calorii = data['Calorii']
    
    fig, axs = plt.subplots(2, 2, figsize=(10, 8)) #grid de 4 grafice cu size

    axs[0, 0].plot(durata, label='Durata', color='red', marker='o') #marker pt puncte pe grafic
    axs[0, 0].set_title('Durata')

    axs[0, 1].plot(puls, label='Puls', color='blue', marker='o')
    axs[0, 1].set_title('Puls')

    axs[1, 0].plot(max_puls, label='MaxPuls', color='green', marker='o')
    axs[1, 0].set_title('MaxPuls')

    axs[1, 1].plot(calorii, label='Calorii', color='purple', marker='o')
    axs[1, 1].set_title('Calorii')

    plt.suptitle(titlu)
   # plt.tight_layout()
    plt.show()  #subgraficele sunt afisate intr o fereastra

if __name__ == '__main__':
    data = pd.read_csv('data.csv')  #citirea datelor din fisierul csv
    creaza_graf('Afiseaza tot', data) #este apelata functia pentru a afisa graficele pentru toate datele

    data = pd.read_csv('data.csv', nrows=X) # afiseaza graficele pentru primele x valori
    creaza_graf('Primele ' + str(X) + ' valori', data)

    data = pd.read_csv('data.csv').tail(Y) #afiseaza graficele pentru ultiele y valori
    creaza_graf('Ultimele ' + str(Y) + ' valori', data)


