class Auto:
    def __init__(self, barwa, stan, wiek):
        self.kolor = barwa
        self.ilosc_paliwa = 10
        self.kondycja = stan
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.rocznik = 2023 - wiek

    def tryb_eco(self):
        self.tryb_ekonomiczny = True
        self.spalanie_na_100 = 10

    def tryb_normal(self):
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14



auto_Kamila = Auto('zielone', 4, 12)

print(auto_Kamila.kolor)
auto_Kamila.kolor = 'niebieskie'
print(auto_Kamila.kolor)

print(f'spalanie na 100 przed zmianą {auto_Kamila.spalanie_na_100}')
auto_Kamila.tryb_eco()
print(f'spalanie na 100 po zmianie {auto_Kamila.spalanie_na_100}')