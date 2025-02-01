favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}

print("The following language have been mentioned:")
print(set(favorite_languages.values()))
for language in set(favorite_languages.values()):
    print(language.title())