def goster():
    
    with open("bilgiler.txt", "r", encoding = "utf-8") as file:
        for satir in file:
            print(satir)