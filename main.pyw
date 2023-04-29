#pip install pillow
#pip install requests


import tkinter as tk
import requests
from PIL import Image, ImageTk

root = tk.Tk()

root.title("Your Weather App")
root.geometry("600x500")
root.minsize(600,500)
root.maxsize(600,500)
root.iconbitmap("favicon.ico")


# API KEY = 3b1f9647f2793d70b9bb7c58aceaa5c0
#API URL = https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

def city_response(weather):
    try:
        city = weather['name']
        final_city = '%s'%(city)
    except:
        final_city = "ERROR"
    return final_city


def temperature_response(weather):
    try:
        temp = weather['main']['temp']
        final_temp = '%s°F'%(temp)
    except:
        final_temp = "ERROR"
    return final_temp


def desc_response(weather):
    try:
        desc = weather['weather'][0]['description']
        final_desc = '%s'%(desc)
    except:
        final_desc = "ERROR"
    return final_desc


def open_icon(icon):
    size=int(root.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open("./img/"+icon+'.png').resize((55, 55)))
    icon_lbl.delete('all')
    icon_lbl.create_image(0,0, anchor='nw', image=img)
    icon_lbl.image=img


def get_weather(city):
    weather_key = '3b1f9647f2793d70b9bb7c58aceaa5c0'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID' : weather_key, 'q':city, 'units':'imperial'}

    response = requests.get(url, params)
    weather = response.json()

    icon_name = weather['weather'][0]['icon']
    open_icon(icon_name)
    # print(response.json())
    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])

    city_name_lbl['text']=city_response(weather)
    temperature_lbl['text'] = temperature_response(weather)
    desc_lbl['text'] = desc_response(weather)



img = Image.open('image/bg.jpg')
img = img.resize((600, 500), Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)


bg_lbl = tk.Label(root, image = img_photo)
bg_lbl.place(x=-1, y=0)



txt_box = tk.Entry(root, font=("montserrat", 15), width=17, foreground='white', bg="#0c1e4c", relief='flat')
txt_box.place(x=130, y = 153, width = 285, height=30)


search_img = Image.open('image/search_btn_icon.png')
search_img = search_img.resize((35, 35), Image.ANTIALIAS)
search_img_btn = ImageTk.PhotoImage(search_img)


search_btn = tk.Button(root, font=("montserrat bold", 15), background="#0c1e4c", foreground='white', image=search_img_btn, relief="flat", activebackground="#0c1e4c", borderwidth='2', command=lambda: get_weather(txt_box.get()))
search_btn.place(x=444, y = 148)

city_name_lbl = tk.Label(root, bg='#393a57', fg="white", font=("montserrat", 20))
city_name_lbl.place(x=275, y=290, width=200, height=35)

temperature_lbl = tk.Label(root, bg='#191d22', fg="#ffae00", font=("foldit", 25))
temperature_lbl.place(x=75, y=305, width=130, height=122)

desc_lbl = tk.Label(root, bg='#1a1b36', fg="white", font=("foldit", 15))
desc_lbl.place(x=275, y=388, width=145, height=45)

icon_lbl = tk.Canvas(root, bg="#e9eaed", bd=0, highlightthickness=0)
icon_lbl.place(x=485, y=391, width=63, height=63)





root.mainloop()