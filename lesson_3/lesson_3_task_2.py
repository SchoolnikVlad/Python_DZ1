from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "iPhone 15", "+79111111111")
phone2 = Smartphone("Samsung", "Galaxy S23", "+79222222222")
phone3 = Smartphone("Google", "Pixel 9", "+79333333333")
phone4 = Smartphone("OnePlus", "8 Pro", "+79444444444")
phone5 = Smartphone("Xiaomi", "Mi 13", "+79555555555")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(phone.brand, phone.model, phone.phone_number)