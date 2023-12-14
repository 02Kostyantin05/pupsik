def parne_ili_net(nomer):
    return nomer % 2 == 0
user_input = input("Введіть число: ")
nomer_to_check = int(user_input)

if parne_ili_net(nomer_to_check):
    print(f"{nomer_to_check} є парним числом.")
else:
    print(f"{nomer_to_check} є непарним числом.")