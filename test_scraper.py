import requests
from bs4 import BeautifulSoup


url = input("Enter job URL: ")

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=20
)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text(
    separator="\n",
    strip=True
)

print("\n==============================")
print("       PAGE TEXT")
print("==============================\n")

print(text[:5000])