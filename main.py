from webserver import keep_alive
import requests

channelID = 1112029891878191104
headers = {
    "authorization":
    "ODUyODU0OTIxODI0MDQzMDM4.Gqkp-1.7IXHGVKwiTgAZ_anP0lShvkRqsWvIO3Ov4MGek"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
