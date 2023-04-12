import speech_recognition as sr
import pyautogui

r = sr.Recognizer()
mic = sr.Microphone()

def mouse_control():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Diga um comando:")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='pt-BR')
        if 'cima' in command:
            pyautogui.move(0, -30)
        elif 'baixo' in command:
            pyautogui.move(0, 30)
        elif 'esquerda' in command:
            pyautogui.move(-30, 0)
        elif 'direita' in command:
            pyautogui.move(30, 0)
        elif 'clique' in command:
            pyautogui.click()
        elif 'duplo clique' in command:
            pyautogui.doubleClick()
        elif 'botão direito' in command:
            pyautogui.rightClick()
        print(command)
    except:
        pass

while True:
    mouse_control()
