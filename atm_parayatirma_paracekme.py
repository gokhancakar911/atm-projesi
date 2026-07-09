print ("===CAKARBANK ATMSINE HOSGELDİNİZ===")

bakiye=5000
miray=100
öyküm=100
melike=100

while True:
    print("*"*50)
    print("Hangi işlemi yapacaksınız?")
    print("1. Çekme")
    print("2. Yatırma")
    print("3. Transfer")
    print("4. Çıkış")
    print("5. Bakiye Görüntüle")

    islem=input("işlem seçinizi (1/2/3/4/5):")
    print("*"*50)

    if islem=="4":
        print("Çıkış yaptınız.")
        break

    elif islem=="5":
        print(f"Güncel bakiyeniz {bakiye} TL dir.")
        continue

    miktar=int(input("Tutar giriniz:"))

    if miktar <= 0:
        print("Geçersiz tutar.")
        continue

    if islem=="1":
        if miktar > bakiye:
            print("Yetersiz bakiye.")
            continue

        bakiye -= miktar
        print(f"{miktar} TL çekim yaptınız. Bakiyeniz {bakiye} TL dir.")

    elif islem=="2":
        bakiye=bakiye+miktar
        print(f"{miktar} TL yatırım yaptınız. Bakiyeniz {bakiye} TL dir.")

    elif islem=="3":
        while True:

            if miktar > bakiye:
                print("Yetersiz bakiye.")
                break

            print("Kişi seçiniz.")
            print("1. Miray")
            print("2. Öyküm")
            print("3. Melike")

            kisi = input("Kişi seçiniz (1/2/3):")
            print("="*50)

            if kisi=="1":
                bakiye -= miktar
                miray += miktar
                print("Miray kişisini seçtiniz.")
                print(f"{miktar} TL transfer yaptınız. Bakiyeniz {bakiye} TL dir.")
                print(f"Miray'ın bakiyesi: {miray} TL")
                break

            elif kisi =="2":
                bakiye -= miktar
                öyküm += miktar
                print("Öyküm kişisini seçtiniz.")
                print(f"{miktar} TL transfer yaptınız. Bakiyeniz {bakiye} TL dir.")
                print(f"Öyküm'ün bakiyesi: {öyküm} TL")
                break

            elif kisi == "3":
                bakiye -= miktar
                melike += miktar
                print("Melike kişisini seçtiniz.")
                print(f"{miktar} TL transfer yaptınız. Bakiyeniz {bakiye} TL dir.")
                print(f"Melike'nin bakiyesi: {melike} TL")
                break

            else:
                print("Geçersiz seçim")