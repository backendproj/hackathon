
def  mani():
    text = input("matni kriting : ")
    print(main(text))


def main(text):
    for  n , m in enumerate(text):
        somsa = text.count(m)
        if somsa >= 2 :
            # return 
            k = text.replace(m, "1" )
            return k



if __name__ == "__main__":
    mani()