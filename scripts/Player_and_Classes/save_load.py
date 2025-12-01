from creation import user_data_path, user_data
import json


def save_user_data():
    with open(user_data_path, "w") as f:
        json.dump(user_data, f, indent=4)
