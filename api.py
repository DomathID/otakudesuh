import requests
import json

logo = '''

 .--. .-----. .--. .-..-..-..-..---.  .--.  .--. .-..-.
: ,. :`-. .-': .; :: :' ;: :: :: .  :: .--': .--': :: :
: :: :  : :  :    ::   ' : :: :: :: :: `;  `. `. : :: :
: :; :  : :  : :: :: :.`.: :; :: :; :: :__  _`, :: :; :
`.__.'  :_;  :_;:_;:_;:_;`.__.':___.'`.__.'`.__.'`.__.'
                                                       
fb.me/bangdomath.id
'''
print(logo)

nama = input("Anime: ")
response = requests.get("https://anime.kaedenoki.net/api/anime/" + nama)
data = response.json()
print(f'Title: {data["japanase"]}')
print(f'Score: {data["score"]}')
print(f'Status: {data["status"]}')
print(f'Total Eps: {data["total_episode"]}')
print(f'Sinopsis: {data["synopsis"]}')
print(f'Link: {data["batch_link"], ["link"]}')
