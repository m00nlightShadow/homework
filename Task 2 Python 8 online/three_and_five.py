# Перевірити, чи є число не парним, ділиться чи на три і на п'ять одночасно, але так, щоб не ділитися на 10.
# Всі числа, які діляться на 10 є парними

number = int(input('Введіть число: '))
if number %2 !=0 and number %3 == 0 and number %5 == 0:
    print ('Не парне, ділиться на 3 і на 5 одночасно')
else:
    print ("Спробуй інше")