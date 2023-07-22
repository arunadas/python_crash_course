languages = ['hindi','english']
languages[0] = 'spain'
languages.insert(0,'hindi')
languages.append('sanskrit')
languages.append('french')
languages.append('korian')
languages.append('veitnamise')
print(languages)
del languages[0]
popped_language = languages.pop()
print(popped_language)

popped_language = languages.pop(2)
print(popped_language)

languages.remove('french')
print(languages)

print(sorted(languages))


print(sorted(languages, reverse=True))


languages.reverse()
print(languages)

languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)
print(languages[12])