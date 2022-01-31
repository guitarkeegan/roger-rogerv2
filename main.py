from playsound import playsound  # simplest way to play audio I could find.
import morse_code as mc  # links to another document with a dictionary
import time

playsound("long.mp3")
playsound("short.mp3")

on = True
while on:
    message = str(input("Type in your message to hear it in Morse code: ")).lower().replace(" ", "_")
    if message == "quit_code":
        on = False
        continue
    for letter in message:
        code = mc.mc[letter]
        for char in code:
            if char == "-":
                playsound("long.mp3")  # I made the mp3s in Garage Band
            elif char == ".":
                playsound("short.mp3")
            elif char == "!":
                print("next word...")
                time.sleep(1)

print("Have a great day!")
playsound("long.mp3")
playsound("short.mp3")
