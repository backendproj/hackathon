def sozlar(gap):
    list =[] 
    gaplar = gap.split()

    for x in range(1,10):
       for soz in gaplar: 
        if str(x) in soz:
          list.append(soz)
    print(" ".join(list))      
      
sozlar("Me1ning ho3vlim bor4 kat2ta")

