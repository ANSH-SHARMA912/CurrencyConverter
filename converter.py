import tkinter as tk 
from tkinter import ttk, messagebox
import requests 
import json

api_key="fb8abfc8c2b8c0403db484e8"
url=f"https://v6.exchangerate-api.com/v6/fb8abfc8c2b8c0403db484e8/latest/USD"

def get_exchangerate():
    try:
        response=requests.get(url)
        data=response.json()
        return data["conversion_rates"]
    except Exception as e:
        messagebox.showerror("error",f"failed to fetch exchange rates : {e}")
        return None
    
root=tk.Tk()
root.title("currency converter")
root.geometry("400x300")
root.resizable(False,False)


exchage_rates=get_exchangerate()
if exchage_rates is None:
    root.destroy()

currencies=list(exchage_rates.keys())

amount_label=tk.Label( root,text="Amount:",font=("Arial",12))
amount_label.pack(pady=5)

amount_entry=tk.Entry( root,font=("Arial",12))
amount_entry.pack(pady=5)

from_currency_label=tk.Label(root,text="From currency",font=("Arial",12))
from_currency_label.pack(pady=5)

from_currency=ttk.Combobox(root,values=currencies,state="readonly")
from_currency.pack(pady=5)
from_currency.set("USD")

to_currency_label=tk.Label(root,text="To currency", font=("Arial",12))
to_currency_label.pack(pady=5)

to_currency=ttk.Combobox(root,values=currencies,state="readonly")
to_currency.pack(pady=5)
to_currency.set("EUR")

def conversion():
    try:
        ammount=float(amount_entry.get())
        from_curr=from_currency.get()
        to_curr=to_currency.get()
        
        if from_curr not in exchage_rates or to_curr not in exchage_rates:
            messagebox.showerror("Error","Invalid currency selection")
            return 
        converted_amount=ammount*(exchage_rates[to_curr]/exchage_rates[from_curr])
        result_label.config(text=f"Converted Amount: {converted_amount: .2f}{to_curr}")
    except Exception as e :
        messagebox.showerror("Error", " Please enter a valid amount")

convert_button=tk.Button(root,text="Convert",command=conversion,font=("Arial",12),bg="blue",fg="white")
convert_button.pack(pady=10)

result_label=tk.Label(root,text="",font=("Arial",14,"bold"),fg="green")
result_label.pack(pady=10)

root.mainloop()