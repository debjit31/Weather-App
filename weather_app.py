import tkinter as tk
from tkinter import font
import requests
HEIGHT = 500
WIDTH = 600
root = tk.Tk()

def format_response(weather):
    degrees = u"\N{DEGREE SIGN}"
    try:
        name = weather['name']
        conditions = weather['weather'][0]['description'].capitalize()
        temp = '{}{}'.format(weather['main']['temp'], degrees)
        feels = '{}{}'.format(weather['main']['feels_like'], degrees)
        return 'City :- {}\nConditions :- {}\nTemp :- {}\nFeels like {}'.format(name, conditions, temp, feels)
    except:
        return 'City or Location Not Found!!!'




def get_weather(city):
    api_key = '8e8940d777f4245501bcab9be4153fba'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'appid' : api_key, 'q' : city, 'units' : 'metric'}
    response = requests.get(url, params = params)
    weather = response.json()

    info = format_response(weather)
    det_label['text'] = info

canvas=tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

bg_img = tk.PhotoImage(file = 'landscape.png')
bg_label = tk.Label(root, image=bg_img)
bg_label.place(relheight=1, relwidth=1)



frame = tk.Frame(root , bg='#80c1ff', bd=5)
frame.place(anchor = 'n', relx = 0.5, rely=0.1, relwidth = 0.75, relheight = 0.1)


entry = tk.Entry(frame,font=('Courier', 15))
entry.place(relwidth=0.65, relheight=1)

button  = tk.Button(frame, text='Get Weather',
             font=('Courier', 12), command = lambda : get_weather(entry.get()))

button.place(relx = 0.7, relheight=1, relwidth=0.3)


low_frame = tk.Frame(root, bg = '#80c1ff', bd=10)
low_frame.place(anchor = 'n', relx = 0.5, rely = 0.25, relwidth=0.75, relheight=0.6)

det_label = tk.Label(low_frame, font=('Courier', 12), anchor = 'nw', justify = 'left', bd = 5)
det_label.place(relwidth=1, relheight=1)



root.mainloop()
