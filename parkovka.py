from model import Parkovka
from colorama import Fore

def admin_login():
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        parol = input(f"\n{50 * '='}\nAdmin parolni kiriting: \n{50 * '='}\n ")
        if parol == '1111':
            return True
        else:
            attempts += 1
            print(f"Parol noto'g'ri. {max_attempts - attempts} ta imkonyatingiz qoldi.")
    
    print("Maksimal urinishlar tugadi. Dasturdan chiqyapsiz.")
    return False

filial1 = Parkovka(filial_nomi="Chilonzor", narx=13_000, sigim=35)

while True:
    kim_u = input(f"\n{50 * '='}\nAdmin uchun '1', \n{50 * '='}\nMijoz uchun '2',\n{50 * '='}\nChiqish uchun '0' bosing: \n{50 * '='}\n").strip()

    if kim_u == '1':
        if admin_login():
            print(f"\n{50 * '='}\n{Fore.GREEN}Admin sifatida tizimga kirdingiz\n{Fore.RESET}{50 * '='}\n")
            while True:
                print(50 * "=")
                tanlov = input(f"\n{50 * '='}\nFilialni ko'rish (1)\n{50 * '='}\nBarcha tushumni ko'rish (2)\n{50 * '='}\nChiqish uchun (0) bosing\n{50 * '='}\n")
                if tanlov == '1':
                    print(f"\n{50 * '='}\nChilonzor filialiuga kirdingiz\n{50 * '='}\n")
                    filial1.mashinalarni_korish()
                elif tanlov == "2":
                    filial1.tushumlar_hisoblash()
                elif tanlov == "0":
                    print(f"\n{50 * '='}\n\t{Fore.BLUE}Dasturdan chiqyapsiz...{Fore.RESET}\n{50 * '='}\n")
                    break
                else:  
                    print(f"{Fore.RED}Iltimos, to'g'ri raqam kiriting.{Fore.RESET}\n")
        else:
            continue  # Agar parol noto'g'ri bo'lsa, bosh sahifaga qaytadi

    elif kim_u == '2':
        while True:
            user = input(f"\n{50 * '='}\nMashina qo'yish uchun '1', \n{50 * '='}\nOlib chiqish uchun '2', \n{50 * '='}\nChiqish uchun '0' bosing: \n{50 * '='}\n").strip()
            if user == '1':
                mashina_nomi = input(f"\n{50 * '='}\nMashina nomini kiriting: \n{50 * '='}\n")
                mashina_raqami = input(f"\n{50 * '='}\nMashina raqamini kiriting: \n{50 * '='}\n")
                vaqt = float(input(f"\n{50 * '='}\nNecha soat turadi: \n{50 * '='}\n"))  
                mashina = {
                    "mashina_nomi": mashina_nomi,
                    "mashina_raqami": mashina_raqami,
                    "vaqt": vaqt
                }
                filial1.kirish(mashina=mashina)
            elif user == '2':
                mashina_raqami = input(f"\n{50 * '='}\nOlib chiqiladigan mashina raqamini kiriting: \n{50 * '='}\n")
                filial1.chiqish(mashina_raqami=mashina_raqami)  
            elif user == '0':
                print(f"\n{50 * '='}\n{Fore.BLUE}Dasturdan chiqyapsiz...{Fore.RESET}\n{50 * '='}\n")
                break  
            else:
                print(f"\n{50 * '='}\n{Fore.RED}Iltimos, to'g'ri raqam kiriting.{Fore.RESET}\n{50 * '='}\n")

    elif kim_u == '0':
        print(f"\n{50 * '='}\n\t{Fore.BLUE}Dasturdan chiqyapsiz...{Fore.RESET}\n{50 * '='}\n")
        break 
 
    else:
        print(f"\t\n\n\t{Fore.RED}Iltimos, to'g'ri raqam kiriting.{Fore.RESET}")
