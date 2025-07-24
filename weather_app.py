from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim

from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)


def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="my_weather_app_your_email@example.com")
    location = geolocator.geocode(city)
    if location is None:
        name.config(text="City not found!")
        return
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    print(result)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    # Weather API (OpenWeatherMap)
    api_key = "e6d7f5399576324d209cb16ab08ddf40"  # <-- User's OpenWeatherMap API key
    lat = location.latitude
    lon = location.longitude
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    try:
        response = requests.get(weather_url)
        data = response.json()
        print(data)
        if data.get("cod") != 200:
            name.config(text="Weather not found!")
            t.config(text="--")
            c.config(text="")
            w.config(text="--")
            h.config(text="--")
            d.config(text="--")
            p.config(text="--")
            return
        # Extract weather data
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"].title()
        wind = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]

        # Update labels
        t.config(text=f"{int(temp)}°C")
        c.config(text=condition)
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=condition)
        p.config(text=f"{pressure} hPa")
    except Exception as e:
        name.config(text="Network/API error!")
        t.config(text="--")
        c.config(text="")
        w.config(text="--")
        h.config(text="--")
        d.config(text="--")
        p.config(text="--")


#search box
search_image=PhotoImage(file="Copy of search.png")
myimage=Label(image=search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

search_icon=PhotoImage(file="Copy of search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

#logo
Logo_image=PhotoImage(file="copy of logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)


#Botton box

frame_image=PhotoImage(file="copy of box.png")
frame_myimage=Label(image=frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTON",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)


w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)

d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)

p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)




root.mainloop()
