from tkinter import *
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')

# Fetch une citation au hasard a parti de l'api Quotes et modifie la bulle de text de l'oracle
def get_quote():
    api_url = 'https://api.api-ninjas.com/v1/quotes'
    response = requests.get(url=api_url,headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        quote = response.json()[0]['quote']
        canvas.itemconfig(quote_text,text=quote)
    else:
        print("Error :",response.status_code,response.text)


# ----- : UI SETUP : ----- #

window = Tk()
window.title("L'oracle à dit...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="The oracle said ...", width=250, font=("Arial", 12, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="philosopher.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()