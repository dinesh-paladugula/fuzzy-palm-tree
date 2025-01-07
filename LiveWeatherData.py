from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def weather(city):
    city = city.replace(" ", "+")
    url = f'https://www.google.com/search?q={city}+weather+in+celcius'

    try:
        # Sending request to the Google search 
        res = requests.get(url, headers=headers)
        res.raise_for_status()  # Check for successful request (200 status code)
        print("Searching......\n")

        soup = BeautifulSoup(res.text, 'html.parser')

        # Extract relevant data using specific classes from the HTML
        time = soup.find('div', {'class': 'BNeawe tAd8D AP7Wnd'})  # Time of weather report
        weather = soup.find('div', {'class': 'BNeawe iBp4i AP7Wnd'})  # Temperature

        
        if time and weather:
            print(f"Temperature: {weather.get_text(strip=True)}")
            print(f"Time: {time.get_text(strip=True)}")

        else:
            print("Could not find weather information. Please try again later.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# User input
city = input("Enter the Name of Any City >> ")
weather(city)
