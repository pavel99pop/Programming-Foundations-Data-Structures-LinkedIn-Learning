user_preferences = {
    "language": "English",
    "font_size": "14px",
    "timezone": "GMT",
    "currency": "USD",
    "enable_location": False,
    "volume_level": 80,
    "date_format": "MM/DD/YYYY"
}

user_preferences['timezone'] = 'PST'
del user_preferences['font_size']
deleted_items = user_preferences.pop('volume_level', 'N/A')
print(deleted_items)

print(user_preferences)