wag = [10,15,25,8,7,5]
max =25

def podziel(wagi):
    for waga in wagi:
        if waga >max:
            raise ValueError(f"Paczka o wadze {waga} przekracza dozwoloną wagę kursu{max}")

    wag_sorted = sorted(wag,reverse=True)
    kursy = []
    for waga in wag_sorted:
        dodana = False
        for kurs in kursy:
            if sum(kurs) + waga <= max:
                kurs.append(waga)
                dodana =True
                break
        if not dodana:
            kursy.append([waga])
    return len(kursy), kursy

liczba_kursow, kursy = podziel(wag)
print(f"Liczba kursów: {liczba_kursow}")
for i, kurs in enumerate (kursy, 1):
    print(f"Kurs {i}: {kurs} - suma wag: {sum(kurs)} kg")
