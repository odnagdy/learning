zp = input("Введите вашу зарплату: ")
days_of_work = input("Введите кол-во рабочих дней в месяц: ")
print("Ваша зп за день: ", (int(zp) // int(days_of_work)), "Ваша зп за час: ", (int(zp) // int(days_of_work) / 8) )
