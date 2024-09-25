import PySimpleGUI as sg


tamaño = (7, 3)
jugador1 = "X"
jugador2= "O"
current_ply = jugador1
winer = "el ganador es: {}" .format(current_ply)
deck = [0, 0, 0,
        0, 0, 0, 
        0, 0, 0]
winer_plays = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
               [0, 3, 6], [1, 4, 7], [2, 5, 8],
               [0, 4, 8], [2, 4, 6]]
layout = [
            [sg.Button("", key="-0-", size=(tamaño)),
             sg.Button("", key="-1-",size=(tamaño)),
             sg.Button("", key="-2-",size=(tamaño))],

            [sg.Button("", key="-3-", size=(tamaño)),
            sg.Button("", key="-4-",size=(tamaño)),
            sg.Button("", key="-5-", size=(tamaño))],

            [sg.Button("", key="-6-", size=(tamaño)),
             sg.Button("", key="-7-",size=(tamaño)),
             sg.Button("", key="-8-", size=(tamaño))],

            [sg.Button("He terminado", size=(7,2), key= "ok"), 
            sg.Text("kkk", key="winer", size=(7,2))]
        ]


window = sg.Window("random", layout)
game_over = False
while True:
    event, values = window.Read()
    print(event)


    if event == sg.WIN_CLOSED or event == "ok":
        break

    if window.Element(event).ButtonText == "" and not game_over:
        index = int(event.replace( "-", ""))
        deck[index] = current_ply
        window.Element(event).Update(text= current_ply)
        
        for winer_play in winer_plays:
            if deck[winer_play[0]] == deck[winer_play[1]] == deck[winer_play[2]] != 0:
                if deck[winer_play[0]] == jugador1:
                    #window.Element("winer").Update(text= winer)
                    print(winer)

                else:
                    #window.Element("winer").Update(text = winer)
                    print(winer)
                
                game_over = True

       
        if 0 not in deck:
            print("game over")

        gamer_over = True
        

    if current_ply == jugador1:
        current_ply = jugador2
    else:
        current_ply = jugador1
        
window.close()