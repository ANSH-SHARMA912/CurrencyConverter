This is a simple currency converter application built using Python with a Tkinter-based GUI. It allows users to input an amount, select source and target currencies from dropdown menus, and quickly convert the currency using real-time exchange rates fetched from an API.
 Key Features
  - Accepts user input for **amount** to convert.
  - Dropdown menus to select **source currency** and **target currency**.
  
Conversion Logic:
  - Fetches real-time exchange rates from [ExchangeRate-API](https://www.exchangerate-api.com/) using a dummy or free-tier API key.
  - Performs conversion using this formula:
  

    converted_amount = amount × (target_currency_rate / source_currency_rate)


  Output:
  - Displays the converted amount in the selected target currency.

GUI (Tkinter-based):
  - User-friendly interface built with Tkinter.
  - Dropdown menus for selecting currencies.
  - Input field for amount.
  - "Convert" button to perform the conversion.
  - Displays the result clearly.

How It Works

1. Fetches live exchange rates using the API.
2. Displays currency codes in dropdowns for selection.
3. Takes user’s amount, source currency, and target currency.
4. Calculates the converted amount.
5. Shows the result within the GUI.

   


