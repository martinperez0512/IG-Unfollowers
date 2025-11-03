import json

def parse_followers_json(json_data, data_key):
    # function to parse followers
    current_set = set()
    data_list = json_data.get(data_key, json_data) 
    
    for user in data_list:
        try:
            current_set.add(user['string_list_data'][0]['value'])
        except KeyError:
            print(f"Warning: Skipping a record in followers list: {user}")
    return current_set

def parse_following_json(json_data, data_key):
    # function to parse following 
    current_set = set()
    data_list = json_data.get(data_key, json_data) 
    
    for user in data_list:
        try:
            current_set.add(user['title'])
        except KeyError:
            print(f"Warning: Skipping a record in following list: {user}")
    return current_set

# now define the followers and following lists from the downloaded info
following_file_path = '/Users/mpere/Documents/GitHub/IG-Unfollowers/following.json'
followers_file_path = '/Users/mpere/Documents/GitHub/IG-Unfollowers/followers.json'

try:
    with open(following_file_path, 'r') as f:
        following_json = json.load(f)
    
    with open(followers_file_path, 'r') as f:
        followers_json = json.load(f)

except FileNotFoundError as e:
    print(f"Error: File not found. Make sure this file exists: {e.filename}")
    exit()
except json.JSONDecodeError as e:
    print(f"Error: Could not read one of the JSON files. It might be empty or corrupted.")
    print(f"Details: {e}")
    exit()

followers = parse_followers_json(followers_json, 'relationships_followers')
following = parse_following_json(following_json, 'relationships_following')

targets = following - followers

for target in list(targets):
        print(target)
