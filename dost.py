def main(roixat : list):
    list = []
    for x in roixat :
        if len(x) > 4:
            list.append(x)
    return list

print(main(["mirafzal", "soms", "maya","sdfgd"]))
               