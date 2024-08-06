user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    # updated_dict = {}
    # for item in user_preferences:
    #     if user_preferences[item] is not None:
    #         updated_dict[item] = user_preferences[item]

    # return updated_dict
  return {key: value for key, value in user_pref.items() if value is not None}


print(update_preferences(user_preferences))
