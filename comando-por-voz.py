print("Testando...")

import speech_recognition as sr
import os
import webbrowser

#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()

    #Usando o microfone
    with sr.Microphone() as source:

        #Chama um algoritmo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)

        #Frase para o usuário dizer algo
        print("Diga alguma coisa:")

        #Armazena o que foi dito numa variável
        audio = microfone.listen(source)

    try:

        #Passa a variavel para algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio, language='pt-BR')
        frase = frase.lower()

        if "navegador" in frase:
            os.system("start Chrome.exe")
            return False
        
        elif "excel" in frase:
           os.system("start Excel.exe")
           return False 
        
        elif "chat" in frase and "abrir" in frase:
           print("Abrindo ChatGPT")
           webbrowser.open("https://chat.openai.com")
           return False

        elif "sublime" in frase:
           os.system(r'"C:\Program Files\Sublime Text\sublime_text.exe"')
           return False
   
        elif "fechar" in frase:
           os.system("exit")
           return True


        #Retorna a frase pronunciada
        
        print("Você disse: " + frase)

    #Se não reconheceu o padrão de fala, exibe a mensagem
    except sr.UnkownValueError:
        print ("Não foi possível entender")

    return frase

while True:
    if ouvir_microfone():
        break