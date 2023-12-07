import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    api_key = "1b61610e5d58db58868ed08b1d69229e"  # Replace with your API key
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        weather_data = response.json()

        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        pressure = weather_data['main']['pressure']

        result_text = f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} km/h\nRain Chance: {rain_chance}%\nPressure: {pressure} hPa"
        result_label.config(text=result_text)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching weather data: {e}")

# GUI setup
app = tk.Tk()
app.title("Weather App")
app.geometry("400x300")  # Set the dimensions to 400x300 pixels

# Entry for city input
city_label = tk.Label(app, text="Enter City:")
city_label.pack(pady=10)

city_entry = tk.Entry(app)
city_entry.pack(pady=10)

# Button to get weather
get_weather_button = tk.Button(app, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

# Label to display weather information
result_label = tk.Label(app, text="")
result_label.pack(pady=10)

app.mainloop()
