import json
import tkinter as tk
import requests
API_key='1b61610e5d58db58868ed08b1d69229e'
API_key2='ac93fb48395def635c20722c7015cd02'
window=tk.Tk()
window.minsize(width=800,height=600)
window.title("Weather Forecast")

def get_weather(lat,lon):
    
    url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric'
    # url=f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_key}'
    # url=f'http://api.openweathermap.org/data/2.5/forecast/daily?lat=lat&lon=lon&appid={API_key}'
    
    response = requests.request("GET", url)
    if response.status_code == 200:
    # If the status code is 200, the request was successful
        print(response.json())  # Print the JSON response
    else:
    # If the status code is not 200, print the response content
        print(response.text)

def get_geo():
    # Retrieve the value from the Entry widget
    text_value = inputtxt.get()
    # Display the value (you can do whatever you want with it)
    url=f'http://api.openweathermap.org/geo/1.0/direct?q={text_value}&appid={API_key}'
    response = requests.request("GET", url)
    status_code = response.status_code
    
    if(status_code==200):
        try:
            result = json.loads(response.text)
            if result:
                get_weather(result[0]['lat'],result[0]['lon'])
                # return result
            else:
                erro_lbl.config(text=f"No result found for this location {text_value}")
            # print(f"latitude: {result[0]['lat']}")
            # print(f"longitude:  {result[0]['lon']}")
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
    else:
        erro_lbl.config(text=f"Failed to fetch data. Status code: {status_code}")
    
    # print(f"latitude: {result[0]['lat']}")
    # print(f"longitude:  {result[0]['lon']}")




location_lbl = tk.Label(window, text = "Location:",font=("Arial", 20) ) 
location_lbl.grid(column=0,row=0,sticky="ew",padx=100,pady=5)

inputtxt = tk.Entry(window) 
inputtxt.grid(column=1,row=0,sticky="ew",padx=10,pady=5)

searchButton = tk.Button(window, text = "Search",command=get_geo) 
searchButton.grid(column=2,row=0,sticky="ew",padx=10,pady=5)

erro_lbl=tk.Label(window,font=("Arial", 14))
erro_lbl.config(fg="red")
erro_lbl.grid(column=0,row=1,sticky="ew",padx=10,pady=5)

lbl1 = tk.Label(window, text = "Temperature: ",font=("Arial", 20) ) 
lbl1.grid(column=0,row=2,sticky="ew",padx=5,pady=40)


lbl2 = tk.Label(window, text = "Humidity: ",font=("Arial", 20) ) 
lbl2.grid(column=0,row=3,sticky="ew",padx=5,pady=20)


lbl3 = tk.Label(window, text = "Wind Speed: ",font=("Arial", 20) ) 
lbl3.grid(column=0,row=4,sticky="ew",padx=5,pady=20)


lbl4 = tk.Label(window, text = "Pressure: ",font=("Arial", 20) ) 
lbl4.grid(column=0,row=5,sticky="ew",padx=5,pady=20)


lbl5 = tk.Label(window, text = "Precipitation: ",font=("Arial", 20) ) 
lbl5.grid(column=0,row=6,sticky="ew",padx=5,pady=20)


window.mainloop()