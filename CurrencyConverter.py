import tkinter as tk
import cryptocompare
from tkinter import Label, Entry, Frame, Button
from PIL import ImageTk, Image
from currency_converter import CurrencyConverter

# VARIABLES
c = CurrencyConverter()

# FUNCTIONS
def currency_conversion():
    quantity = float(enter_quantity.get())
    current_currency = entry_current_currency.get().upper()
    desired_currency = entry_desired_currency.get().upper()
    
    new_quantity = c.convert(quantity, current_currency, desired_currency)
    forex_conversion_result.config(text=f'Your {quantity} {current_currency} are equal to {new_quantity} {desired_currency}')

def crypto_conversion():
    quantity = float(enter_quantity.get())
    current_currency = entry_current_currency.get().upper()
    crypto_currency = entry_crypto_currency.get().upper()

    crypto_quantity = cryptocompare.get_price(crypto_currency, current_currency,)
    crypto_conversion_result.config(text=f'The price is {crypto_quantity}')

# Create the Pop Up window
window = tk.Tk()
window.title("Currency Converter")
window.resizable(width=False, height=False)
window.geometry("605x595")

frame = tk.Frame(master=window, width=400, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create the Image Background
img = ImageTk.PhotoImage(Image.open("Currency Converter Image.png"))    
label = Label(frame, image=img)                                         
label.pack()

# Create Buttons, Input Fields inside the Pop Up Window and Placement
quantity = Frame(window)


lbl_quantity = Label(window, text="Quantity: ",bg="green", fg="white", font=('Arial',11)).place(x=250,y=200)
enter_quantity = Entry(window, width=10)
enter_quantity.place(x=318, y=200)


lbl_current_currency = Label(window, text="Current Currency: ",bg="green", fg="white", font=('Arial',11)).place(x=192, y=250)
entry_current_currency = Entry(window, width=10)
entry_current_currency.place(x=318, y=250)


lbl_desired_currency = Label(window, text="Desired FOREX Currency: ",bg="green", fg="white", font=('Arial',11)).place(x=70, y=300)
entry_desired_currency = Entry(window, width=10)
entry_desired_currency.place(x=70, y=325)
btn_convert = Button(window,text="Convert",command=currency_conversion,bg="#00FF00",fg="black",font=('Arial',11))
btn_convert.place(x=70, y=365)


lbl_crypto_currency = Label(window, text="Desired Crypto Currency: ",bg="green", fg="white", font=('Arial',11)).place(x=340, y=300)
entry_crypto_currency = Entry(window, width = 10)
entry_crypto_currency.place(x=340, y=325)
crypto_btn_convert = Button(window,text="CryptoConvert",command=crypto_conversion,bg="#00FF00",fg="black",font=('Arial',11))
crypto_btn_convert.place(x=340, y=365)

forex_conversion_result = Label(window,text="Conversion Rate: ", bg="white", fg="green", font=('Arial',11))    
forex_conversion_result.place(x=70, y=425) 
crypto_conversion_result = Label(window,text="Conversion Rate: ", bg="white", fg="green", font=('Arial',11))
crypto_conversion_result.place(x=340, y=425)

#Run the Pop Up Window
window.mainloop()
