import json

following = open('following.json', 'r')
followers = open('followers.json', 'r')
# depending on download, might need to modify the FOLLOWERS file with every new download to allow for proper parsing
# just add an extra bracket {} and rename the file to 'followers.json'


following_json = json.load(following)
followers_json = json.load(followers)

def parse_json(json_file, str_):
    current_set = set()
    for user in json_file[str_]:
        current_set.add(user['string_list_data'][0]['value'])
    return current_set

targets = parse_json(following_json, 'relationships_following') - parse_json(followers_json, 'relationships_followers')

for target in targets:
    print(target)