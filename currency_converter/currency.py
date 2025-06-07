import requests

# API Key and the base url to the currency converter website
API_KEY = 'fca_live_IFrc5Qkr3IYPFqOKO9EAdgkghOmzuntp8Hq02ikP'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

# List of currencies that can be used
CURRENCIES = ["USD", "EUR", "CAD", "AUD", "CNY", "PHP", "JPY", "MXN", "ZAR"]

# Function to fetch the currency conversion rates based on the chosen currency
def convert_currency(base):
    # Joins the list of currencies with comma seperation
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        # Makes a GET request to the API
        response = requests.get(url)
        #Converts the API response into JSON format
        data = response.json()
        # Extracts the currency conversion data
        return data["data"]
    except Exception as e:
        print(e)
        return None

#Creates an interactive loop to keep requesting currencies until the user presses 'q'
try:
    while True:
        # Prompts for the base currency or quit('q')
        base = input("What is your base currency (press q to quit) ?: ").strip().upper()

        if base == 'Q':
            print("Thanks for choosing Currento")
            break

        # Checks to make sure the currency is supported
        if base not in CURRENCIES:
            print("Sorry, that is not available currently :(")
        else:

            # Prompts to enter the amount to convert
            amount = float(input("What is your amount?: "))
            # Prompts the user for a target currency to convert to
            convert = input("What would you like to convert to?: ").strip().upper()
            print("**********************")

            # Gets the conversion data from the API
            data = convert_currency(base)

            # Loops through the conversion results and outputs the expected result
            for ticker, value in data.items():
                if ticker == convert:
                    value *= amount
                    print(f"{ticker}: {value:.2f}")
except ValueError as e:
    print(e)



