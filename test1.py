
tabel = []

def user_input_fun():
    user_input = input("adauga: ")
    return user_input
def incearca(user_input, tabel):
    for a in range(3):
        tabel.append(user_input_fun())
    return

incearca(user_input=user_input_fun, tabel=tabel)
print(tabel)