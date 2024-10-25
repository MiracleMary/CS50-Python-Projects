import emoji

user = input(" ").strip()
text = emoji.emojize(user, language="alias")

print(text)
