data_list = [i for i in range(1, 100) if (i >= 10 and i <= 20 and i % 2 == 0) or (i >= 90 and i <= 100 and i % 2 != 0)]

print("<<<      LATIHAN 1    >>>")
print("Berikut akan tampil list dengan kondisi:")
print("1. range(1,100)")
print("Hanya value/item : genap (i >=10 dan i <=20)")
print("Hanya value/item : ganjil (i >=90 dan i <=100)\n")

print(data_list)

print("-"*30, "Latihan 2", "-"*30)

note_list = ["Do", "Re", "Mi", "Fa", "So", "La", "Ti"]

new_order = note_list[2:3] + note_list[:1] + note_list[3:] + note_list[1:2]

print(new_order)

print("-"*30, "Latihan 3", "-"*30)

data = "IgNatIus"

result = [char for char in data if char.isupper()]

print(result)