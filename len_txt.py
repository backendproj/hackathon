# FUnction

# Oson

def len_txt(text):
    bolish = text.split()
    return len(bolish)

if __name__ == "__len_txt__":
    len_txt()

def test_len_txt():
    assert len_txt("Salom mening ismim Humoyun") == 4
    assert len_txt("Salom Humoyun") == 2
    assert len_txt("Salom ismi Humoyun") == 3
    
# qiyin
def len_txt(text:str):
    for i in text:
        if i == " ":
            return text.count(i)+1
    else:
        return 1
            
if __name__ == "__len_txt__":
    len_txt()

def test_len_txt():
    assert len_txt("Salom mening ismim Humoyun") == 4
    assert len_txt("Salom Humoyun") == 2
    assert len_txt("Salom ismi Humoyun") == 3


