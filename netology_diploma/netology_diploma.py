import requests
import time
import sys
import os
import json


TOKEN = "7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099"
VERSION = 5.8


def request(TOKEN, VERSION):
    def decorator(func):
        def wrapper(method, **parameters):
            params = {
                "access_token": TOKEN,
                "v": f"{VERSION}",
                **parameters
            }
            response = requests.get(f'https://api.vk.com/method/{method}', params)
            res = func(response)
            return res
        return wrapper
    return decorator


def get_target_id():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        target_id = input("Input Target ID: ")
        if target_id.isdigit():
            return target_id
        else:
            target_id = get_id_by_screen_name("utils.resolveScreenName", screen_name=target_id)
            return target_id


@request(TOKEN, VERSION)
def get_id_by_screen_name(response):
    response_dict = response.json()
    try:
        target_id = response_dict["response"]["object_id"]
    except TypeError:
        print("Bad Screen Name!")
        quit()
    return target_id


@request(TOKEN, VERSION)
def get_friends_list(response):
    response_dict = response.json()
    return response_dict["response"]["items"]


@request(TOKEN, VERSION)
def get_group_list(response):
    return response.json()


def get_unique_group_list(friend_list, group_list):
    unique_group_list = group_list[:]
    count_friends = len(friend_list)
    for i, friend_id in enumerate(friend_list):
        print(f"Unique Communities: {len(unique_group_list)} - "
            + f"There Are Friends Left Till The End: {count_friends - i}")
        group_list_temp = get_group_list("groups.get", user_id=friend_id)
        if "error" in group_list_temp:
            if group_list_temp["error"]["error_code"] == 6:  # error: 'Too many requests per second'
                time.sleep(1)
                group_list_temp = get_group_list("groups.get", user_id=friend_id)
            if "error" in group_list_temp:  # other errors
                continue
        group_list_temp = group_list_temp["response"]["items"]
        unique_group_list = set(unique_group_list).difference(set(group_list_temp))
    print('Program Complete. Check "group.json" In The Program Directory.')
    return list(unique_group_list)


@request(TOKEN, VERSION)
def get_info_for_groups(response):
    return response.json()


def write_file(info):
    local_path = os.path.dirname(os.path.realpath(__file__))
    group_path = os.path.join(local_path, 'groups.json')
    with open(group_path, "w", encoding="utf8") as f:
        json.dump(info, f, indent=4,
                  sort_keys=True, separators=(',', ':'), ensure_ascii=False)

if __name__ == "__main__":
	target_id = get_target_id()
	friend_list = get_friends_list("friends.get", user_id=target_id)
	group_list = get_group_list("groups.get", user_id=target_id)["response"]["items"]
	unique_group_list = get_unique_group_list(friend_list, group_list)

	group_ids = map(str, unique_group_list)
	group_ids = ", ".join(group_ids)
	unique = get_info_for_groups("groups.getById", group_ids=group_ids, fields="members_count")
	write_file(unique)