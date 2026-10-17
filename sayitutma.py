import random
answer=random.randint(1,100)
#print(answer)

attempts=0
level=input("Zor mu kolay mi?").lower()


while level!="zor" and level!="kolay":
    print("Lutfen sadece 'zor' ya da 'kolay' yaz:)")
    level=input("Zor mu kolay mi?").lower()
if level=="zor":
    attempts=5
    print("Sayiyi tahmin etmek icin 5 hakkin var")
elif level=="kolay":
    attempts=10
    print("Sayiyi tahmin etmek icin 10 hakkin var")



is_game_over=False
while not is_game_over:
    user_guess = int(input("Tahmin et hangi sayiyi tuttum:)"))
    if user_guess == answer:
        print("Bravo bildin!")
        attempts=attempts - 1
        is_game_over=True
    elif user_guess < answer:
        attempts=attempts - 1
        if attempts == 0:
            is_game_over = True
            print(f"Maalesef tum haklarini tukettin:( Dogru cevap {answer} olacakti")
        else:
            print(f"Buyuk dusun biraz:) bu arada {attempts} hakkin kaldi")
    else:
        attempts=attempts - 1
        if attempts == 0:
            is_game_over = True
            print(f"Maalesef tum haklarini tukettin:( Dogru cevap {answer} olacakti")
        else:
            print(f"Cok attin, kucult biraz bu arada {attempts} hakkin kaldi")


