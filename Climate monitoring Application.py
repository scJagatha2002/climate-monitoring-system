import tkinter as tk
from tkinter import ttk
from tkinter import *
import requests


def getWeather(canvas):
    city = textfield.get()
    apilonglat = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    json_data = requests.get(apilonglat).json()
    latitude = json_data[0]['lat']
    longitude = json_data[0]['lon']

    apiforclimate = "https://api.open-meteo.com/v1/forecast?latitude=" + latitude + "&longitude=" + longitude + "&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum,precipitation_hours,windspeed_10m_max,winddirection_10m_dominant&timezone=Asia%2FSingapore"
    json_data = requests.get(apiforclimate).json()
    wind_dir = json_data['daily']['winddirection_10m_dominant']
    prep_sum = json_data['daily']['precipitation_sum']
    prep_hrs = json_data['daily']['precipitation_hours']
    wind_speed = json_data['daily']['windspeed_10m_max']
    min_temp = json_data['daily']['temperature_2m_min']
    max_temp = json_data['daily']['temperature_2m_max']
    date_time = json_data['daily']['time']
    final_info = 'Date: ' + str(date_time) + '\n' + \
                 'Wind Direction:' + str(wind_dir) + '\n' + \
                 'Precipitation Sum:' + str(prep_sum) + '\n' + \
                 'Wind Speed:' + str(wind_speed) + '\n' + \
                 'Maximum Temperature:' + str(max_temp) + '\n' + \
                 'Minimum Temperature:' + str(min_temp)
    label1.config(text=final_info)

    table['columns'] = ("date_time", 'wind_dir', 'prep_sum', 'wind_speed', 'max_temp', 'min_temp')

    table.column("#0", width=0, stretch=NO)
    table.column("date_time", anchor=CENTER, width=80)
    table.column("wind_dir", anchor=CENTER, width=80)
    table.column("prep_sum", anchor=CENTER, width=80)
    table.column("wind_speed", anchor=CENTER, width=80)
    table.column("max_temp", anchor=CENTER, width=80)
    table.column("min_temp", anchor=CENTER, width=80)

    table.heading("#0", text="", anchor=CENTER)
    table.heading("date_time", text="Date", anchor=CENTER)
    table.heading("wind_dir", text="Wind Direction", anchor=CENTER)
    table.heading("prep_sum", text="Precipitation Sum", anchor=CENTER)
    table.heading("wind_speed", text="Wind Speed", anchor=CENTER)
    table.heading("max_temp", text="Maximum Temperature", anchor=CENTER)
    table.heading("min_temp", text="Minimum Temperature", anchor=CENTER)

    for item in table.get_children():
        table.delete(item)

    table.insert(parent='', index='end', iid=0, text='',
                   values=(date_time[0], wind_dir[0], prep_sum[0], wind_speed[0], max_temp[0], min_temp[0]))
    table.insert(parent='', index='end', iid=1, text='',
                   values=(date_time[1], wind_dir[1], prep_sum[1], wind_speed[1], max_temp[1], min_temp[1]))
    table.insert(parent='', index='end', iid=2, text='',
                   values=(date_time[2], wind_dir[2], prep_sum[2], wind_speed[2], max_temp[2], min_temp[2]))
    table.insert(parent='', index='end', iid=3, text='',
                   values=(date_time[3], wind_dir[3], prep_sum[3], wind_speed[3], max_temp[3], min_temp[3]))
    table.insert(parent='', index='end', iid=4, text='',
                   values=(date_time[4], wind_dir[4], prep_sum[4], wind_speed[4], max_temp[4], min_temp[4]))
    table.insert(parent='', index='end', iid=5, text='',
                   values=(date_time[5], wind_dir[5], prep_sum[5], wind_speed[5], max_temp[5], min_temp[5]))

    table.pack()


canvas = tk.Tk()
canvas.geometry("1000x500")
canvas.title("Climate Monitoring App")

f = ("poppins", 10, "bold")
t = ("poppins", 15, "bold")

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()

table_frame = tk.Frame()
table_frame.pack()

table = ttk.Treeview(table_frame, height=6)
s = ttk.Style()
s.theme_use('clam')


canvas.mainloop()
