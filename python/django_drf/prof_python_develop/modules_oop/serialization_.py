import pickle


user = {'name': 'John', 'age': 34, 'weight': 85}

# file = open('user.pickle', 'wb')
# pickle.dump(user, file)
# file.close()


with open('user.pickle', 'wb') as file:
    pickle.dump(user, file)


with open('user.pickle', 'rb') as file:
    print(pickle.load(file))
