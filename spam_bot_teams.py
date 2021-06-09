import pymsteams
import random

#The title of the message being sent.
title = ""
#The message being sent.
text = ""

while True:
    #Generates a random number and assigns a text and title depending on the number.
    n = random.randint(0, 5)

    if n == 1:
        text = "Bring your moss stuff, careful work mandatory."
        title = "Moss stuff:"
    elif n == 2:
        text = "Nothing to say"
        title = "stuff"
    elif n == 3:
        text = "Are you okay ?"
        title = "Question"
    elif n == 4:
        text = "Hi you noob"
        title = "insult !"
    # You must create the connectorcard object with the Microsoft Webhook URL, this one won't be valid.
    myTeamsMessage = pymsteams.connectorcard("https://365education.webhook.office.com/webhookb2/df28db23-6a10-45f3-ae08-749548df7544@360a0ec5-f094-45f1-a319-c6dc35602704/IncomingWebhook/a8767f199a0242b880c8fdfb4a2e711e/1e1fcaf7-4e53-4ebc-a1b9-3d88cfe4fb4b")
    myTeamsMessage.title(title)
    #The message to be sent
    myTeamsMessage.text(text)
    #Adds a color around the text.
    myTeamsMessage.color("#42f5dd")
    #Adds a button to rick-roll
    myTeamsMessage.addLinkButton("Please click, amazing !", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    # send the message.
    myTeamsMessage.printme()
    myTeamsMessage.send()
    print(random)
    
