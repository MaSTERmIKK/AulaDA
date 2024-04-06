#creo un inventario
#la lista è composta da 3 liste: ciscuno di loro contiene tipo, prezzo, quantità disponibile
inventario=[["pasta",1,300],["cioccolato",2,500],["pane",1,400]]
#creo la lista clienti
acquisti=[]
amministratori=["francesco","giacomo"]
#divido per amministratore e cliente
#amministratore


#fare check migliore con password per amministratori 


who=input("Sei un amministratore o un cliente: ")
if who=="amministratore":
    nome=input("Inserisci il tuo nome: ")
    while nome=="giacomo" or nome=="francesco":             #verifica che sei amministratore
        while True:
            azione=int(input("Cosa vuoi fare?: (guarda inventario=1) (modifica inventario=2) (guarda acquisti=3): "))
            if azione==1:  #guardo inventario
                print(inventario)
            elif azione==2: #modifico inventario
                modifiche=int(input("cosa vuoi moficare? aggiungi prodotto(1), modifica prodotto(2) ")) #2tipi di modifiche
                if modifiche==1:                                             
                    prodotto=str(input("inserisci nome prodotto: "))       #inserisce un nuovo prodotto
                    prezzo=int(input("inserisci prezzo prodotto: "))
                    quantità=int(input("inserisci quantità prodotto: "))
                    inventario.append([prodotto,prezzo,quantità])
                else:
                    mod=int(input("quale prodotto vuoi modificare?:(1=pasta),(2=ciocc),(pane=3) "))
                    if mod==1:                                  
                        cambio_prodotto=str(input("inserisci nome prodotto: "))       
                        cambio_prezzo=int(input("inserisci prezzo prodotto: "))
                        cambio_quantità=int(input("inserisci quantità prodotto: "))  #prodotto1
                        inventario[0][0]=cambio_prodotto
                        inventario[0][1]=cambio_prezzo
                        inventario[0][2]=cambio_quantità
                    if mod==2:
                        cambio_prodotto=str(input("inserisci nome prodotto: "))       
                        cambio_prezzo=int(input("inserisci prezzo prodotto: "))
                        cambio_quantità=int(input("inserisci quantità prodotto: "))    #prodotto2
                        inventario[1][0]=cambio_prodotto
                        inventario[2][1]=cambio_prezzo
                        inventario[3][2]=cambio_quantità
                    if mod==3:
                        cambio_prodotto=str(input("inserisci nome prodotto: "))       
                        cambio_prezzo=int(input("inserisci prezzo prodotto: "))
                        cambio_quantità=int(input("inserisci quantità prodotto: "))   #prodotto3
                        inventario[2][0]=cambio_prodotto
                        inventario[2][1]=cambio_prezzo
                        inventario[2][2]=cambio_quantità


            altro=int(input("vuoi fare altro? (0 si, 1 no) "))            #vuoi fare altro
            if altro==1:
                break
            

else:
    #trasformo in tupla
    inventario=tuple(inventario)
    nome=input("Inserisci il tuo nome: ")
    password=input("inserisci una password: ")    #registro cliente
    #fare check se cliente esiste già
    #creare una lista dove mettere clienti gia registrati

    #azione1=visalizza inventario azione2=compra
    counter=True
    while counter:
        azione=int(input("Cosa vuoi fare? (visualizza inventario(1), compra(2)) ")) 
        
        if azione==1:                 #azione: visualizza inventario
            print(inventario)

        else:                          #azione acquista
            #seleziona il tipo di prodotto
            acquisto=input("seleziona cosa vuoi comprare? (pasta, cioccolato, pane)  ")
            if acquisto==inventario[0][0]:
                quantità=int(input("inserisci la quantità?: "))
                if quantità>inventario[0][2]:
                    print("La quantità scelta non è disponibile")
                    
                else: 
                    conto=quantità*inventario[0][1]
                    inventario[0][2]=inventario[0][2]-quantità #aggiorno il mio inventario
                    acquisti.append([inventario[0][0],quantità,conto]) #aggiungo alla lista degli acquisti

            elif acquisto==inventario[1][0]:
                quantità=int(input("inserisci la quantità?: "))
                if quantità>inventario[1][2]:
                    print("La quantità scelta non è disponibile")
                    
                else: 
                    conto=quantità*inventario[1][1]
                    inventario[1][2]=inventario[1][2]-quantità #aggiorno il mio inventario
                    acquisti.append([inventario[1][0],quantità,conto]) #aggiungo alla lista degli acquisti

            else:
                quantità=int(input("inserisci la quantità?: "))
                if quantità>inventario[2][2]:
                    print("La quantità scelta non è disponibile")
                else: 
                    conto=quantità*inventario[2][1]
                    inventario[2][2]=inventario[2][2]-quantità #aggiorno il mio inventario
                    acquisti.append([inventario[2][0],quantità,conto]) #aggiungo alla lista degli acquisti
            print(acquisti)
        altro=input("vuoi fare altro:?(0 si)(1=no) ")
        if altro=="no":
            counter=False

                    



