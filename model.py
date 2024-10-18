from colorama import Fore

class Parkovka:
    def __init__(self, filial_nomi, narx, sigim):
        self.filial_nomi = filial_nomi
        self.narx = narx
        self.sigim = sigim
        self.tushum = 0
        self.mashinalart = []

    def filial_r(self):
        return self.filial_nomi
    
    def tushumlar(self):
        self.tushum += self.vaqt * self.narx
        


    def kirish(self, mashina: dict):
        vaqt = mashina['vaqt']  
        self.tushum += vaqt * self.narx
        self.mashinalart.append(mashina)
        print(f"\n{50 * "="}\n{Fore.GREEN}{mashina["mashina_nomi"]} {mashina['vaqt']} soatga , parkovkaga qo'yildi{Fore.RESET}\n{50 * "="}\n")

    def chiqish(self, mashina_raqami: str):
        for mashina in self.mashinalart:
            if mashina["mashina_raqami"] == mashina_raqami:
                self.mashinalart.remove(mashina)
                print(f"\n{50 * "="}\n{Fore.GREEN}{mashina["mashina_nomi"]} mashinagiz olib chiqishga tayyor {Fore.RESET}\n{50 * "="}\n")
                return  
        print(f"\n{50 * "="}\n{Fore.RED}{mashina_raqami} raqamli mashina topilmadi.{Fore.RESET}\n{50 * "="}\n") 

    def mashinalarni_korish(self):
        if len(self.mashinalart) == 0:
            print(f"\n{50 * "="}\n{Fore.YELLOW}{self.filial_nomi} filialda hozircha mashina yo'q\n{50 * "="}{Fore.RESET}\n")
        else:
            mashinalar_nomlari = []
            for mashina in self.mashinalart:
                mashinalar_nomlari.append(mashina["mashina_nomi"])

            if len(mashinalar_nomlari) == 1:
                print(f"\n{50 * "="}\nHozirda {self.filial_nomi} da quyidagi mashina bor: {mashinalar_nomlari[0]}\n{50 * "="}\n")
            else:
                text = f'{", ".join(mashinalar_nomlari[:-1])} va {mashinalar_nomlari[-1]}'
                print(f"\n{50 * "="}\nHozirda {self.filial_nomi} da quyidagi mashinalar bor: {text}\n{50 * "="}\n")

    def tushumlar_hisoblash(self):
     self.tushum = sum(mashina['vaqt'] * self.narx for mashina in self.mashinalart)
     print(f"\n{50 * "="}\n{Fore.GREEN}Jami tushum: {self.tushum} {Fore.RESET}\n{50 * "="}\n")
