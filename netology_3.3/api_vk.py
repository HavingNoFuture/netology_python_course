from urllib.parse import urlencode
import requests
from pprint import pprint


AUTH_URL = "https://oauth.vk.com/authorize"
APP_ID = 6610956

auth_params = {
	"client_id": APP_ID,
	"scope": "friends",
	"response_type": "token",
	"v": "5.78"
}
print("?".join((AUTH_URL, urlencode(auth_params))))

TOKEN = "f048118cfada07f9ce3ca433b52ffcd113c83c93f1be84eb6c688b76b7a40ffe9f0605af00bccc4b08c5e"

def get_mutual_friends(target_uids):
	params = {
		"access_token": TOKEN,
		"v": "5.78",
	    "target_uids": target_uids
	}

	response = requests.get('https://api.vk.com/method/friends.getMutual', params)

	response_dict = response.json()
	common_friends_list = []

	for target_uid in response_dict["response"]:
		for common_friend in target_uid["common_friends"]:
			if common_friend not in common_friends_list:
				common_friends_list.append(common_friend)

	common_friends_dict = {}
	for common_friend in common_friends_list:
		common_friends_dict[common_friend] = "https://vk.com/id{}".format(common_friend)
        return common_friends_dict


target_uids = input('Input ids users. *Format: "id_1, id_2, etc.":')
pprint(get_mutual_friends(target_uids)) # Ваши общие друзья с id_1 и id_2 без повторений
