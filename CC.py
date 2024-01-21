from currency_converter import CurrencyConverter
import tkinter as tk

c = CurrencyConverter()

window = tk.Tk()
window.geometry("512x384")
window.title("CC")

def clicked():
    amount = int(entry1.get())
    currency1 = entry2.get()
    currency2 = entry3.get()
    data = c.convert(amount, currency1, currency2)
    Converted_Label = tk.Label(window, text = data, font = "Times 16 bold").place(x = 175, y = 325)

Label = tk.Label(window, text = "Currency Converter", font = "Times 20 italic").place(x =140, y = 50)

Label1 = tk.Label(window, text = "Enter amount here: ", font = "Times 16 bold").place(x = 50, y = 100)
entry1 = tk.Entry(window)

Label2 = tk.Label(window, text = "Enter currency here: ", font = "Times 16 bold").place(x = 50, y = 150)
entry2 = tk.Entry(window)

Label3 = tk.Label(window, text = "Enter your currency here: ", font = "Times 16 bold").place(x = 50, y = 200)
entry3 = tk.Entry(window)

button = tk.Button(window, text = "Click", font ="Times 14 bold", command = clicked).place(x = 225, y = 250)

entry1.place(x = 325, y = 105)
entry2.place(x = 325, y = 155)
entry3.place(x = 325, y = 205)

window.mainloop()