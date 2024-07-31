# importação das bibliotecas
import tkinter as tk
from tkinter import messagebox
import requests

weather_traducoes = {
    "clear sky": "céu limpo",
    "few clouds": "poucas nuvens",
    "scattered clouds": "nuvens dispersas",
    "broken clouds": "nuvens fragmentadas",
    "overcast clouds": "nuvens encobertas",
    "shower rain": "chuva de banho",
    "rain": "chuva",
    "thunderstorm": "trovoada",
    "snow": "neve",
    "mist": "névoa"
}

def get_weather():
    city = city_entry.get()
    api_key = '7feab10321fa46638e07b56648538d35'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    result_label.config(text=f'Tempo: {weather}\nTemperatura: {temperature}°C\nHumidade: {humidity}%\nVelocidade do Vento: {wind_speed} m/s')
    
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        weather_pt = weather_traducoes.get(weather, weather)  # Traduz ou usa o original se não houver tradução
        result_label.config(text=f'Tempo: {weather}\nTemperatura: {temperature}°C')
    else:
        messagebox.showerror('Erro', 'Cidade não encontrada')


# Configuração da interface gráfica
root = tk.Tk()
root.title('App de Previsão do Tempo')

city_label = tk.Label(root, text='Cidade:')
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text='Obter Previsão', command=get_weather)
get_weather_button.pack()

result_label = tk.Label(root, text='', font=('bold', 14))
result_label.pack()

root.mainloop()
    
    