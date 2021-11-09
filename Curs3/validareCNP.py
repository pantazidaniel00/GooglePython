import datetime

def verif_lungime(cnp):
    msg = "Lungimea CNP-ului nu este valida"
    if len(cnp) == 13:
        print("Lungimea este valida")
    else:
        return msg

def verif_S(cnp):
    msg = 'CNP-ul nu este valid'
    if cnp[0] not in '1 2 3 4 5 6 7 8 9':
        print(msg)
    if cnp[0] in '2 4 6 8':
        print("Sexul este feminin")
    else:
        print("Sexul este masculin")

def data_nastere(cnp):
    centuries = {
        '1': 1900, '2': 1900, '3': 1800, '4': 1800, '5': 2000, '6': 2000,
    }
    year = int(cnp[1:3]) + centuries.get(cnp[0], 1900)
    month = int(cnp[3:5])
    day = int(cnp[5:7])
    try:
        print(datetime.date(year, month, day))
    except ValueError:
        print("Data nasterii invalida")

def verif_judet(cnp):
    judet = {'01': 'Alba',
             '02': 'Arad',
             '03': 'Argeș',
             '04': 'Bacău',
             '05': 'Bihor',
             '06': 'Bistrița-Năsăud',
             '07': 'Botoșani',
             '08': 'Brașov',
             '09': 'Brăila',
             '10': 'Buzău',
             '11': 'Caraș-Severin',
             '12': 'Cluj',
             '13': 'Constanța',
             '14': 'Covasna',
             '15': 'Dâmbovița',
             '16': 'Dolj',
             '17': 'Galați',
             '18': 'Gorj',
             '19': 'Harghita',
             '20': 'Hunedoara',
             '21': 'Ialomița',
             '22': 'Iași',
             '23': 'Ilfov',
             '24': 'Maramureș',
             '25': 'Mehedinți',
             '26': 'Mureș',
             '27': 'Neamț',
             '28': 'Olt',
             '29': 'Prahova',
             '30': 'Satu Mare',
             '31': 'Sălaj',
             '32': 'Sibiu',
             '33': 'Suceava',
             '34': 'Teleorman',
             '35': 'Timiș',
             '36': 'Tulcea',
             '37': 'Vaslui',
             '38': 'Vâlcea',
             '39': 'Vrancea',
             '40': 'București',
             '41': 'București - Sector 1',
             '42': 'București - Sector 2',
             '43': 'București - Sector 3',
             '44': 'București - Sector 4',
             '45': 'București - Sector 5',
             '46': 'București - Sector 6',
             '51': 'Călărași',
             '52': 'Giurgiu',
             '47': 'Bucuresti - Sector 7 (desfiintat)',
             '48': 'Bucuresti - Sector 8 (desfiintat)'
             }
    if cnp[7:9] not in judet:
        print("CNP invalid")
    print(judet[cnp[7:9]])

def verif_NNN(cnp):
    if int(cnp[10:13]) > 0 and int(cnp[10:13]) < 1000:
        print("Corect")

def calc_check_digit(cnp):
    weights = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
    check = sum(w * int(n) for w, n in zip(weights, cnp)) % 11
    if check == cnp[-1]:
        print("Corect")
    return '1' if check == 10 else str(check)

cnp = input()
verif_lungime(cnp)
data_nastere(cnp)
verif_S(cnp)
verif_judet(cnp)
verif_NNN(cnp)
print(calc_check_digit(cnp))