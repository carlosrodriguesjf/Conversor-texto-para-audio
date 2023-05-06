# PROJETO 5 - PYTONISTA AUTODIDATA - CONVERSOR DE TEXTO PARA ÁUDIO

import pyttsx4

conversor = pyttsx4.init()

# Ler o arquivo txt
with open('texto.txt','r',newline='',encoding='utf-8') as arquivo:
    for linha in arquivo:   
        conversor.say(linha)
        conversor.runAndWait()

