import emoji

# Виведення смайлика по короткому коду
print(emoji.emojize("Python is :thumbs_up:"))

# Перевірка, чи є емодзі в тексті
print(emoji.is_emoji("🐍"))

# Заміна смайликів на їхні коди
text = "I love 🐍 and ☕"
print(emoji.demojize(text))
