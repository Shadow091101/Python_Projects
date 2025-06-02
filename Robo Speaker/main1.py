import os

if __name__=='__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Manav")
    while(True):
        x=input("Enter what do you want me to pronounce : ")
        command=f""
        os.system(f'PowerShell -Command "Add-Type –AssemblyName System.Speech; '
            f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
            f'$speak.Speak(\'{x}\')"')
    pass