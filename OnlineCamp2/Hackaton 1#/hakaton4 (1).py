# 1. Узнайте какие телефоны из Kivano стоят столько же сколько и компьютеры из Sulpak.
# 2. Узнайте самую последнюю модель Iphone в магазинах.
# 3. Выведите на экран список всех ноутбуков из sulpak и только тех телефонов которые имеют одинаковую дату выхода с компьютером из таблицы kivano.########################
# 4. Выведите все китайские продукты.
# 5. Напишите запрос, который выводит продукты любого магазина в порядке их добавления.
# 6. Найдите товары, которые есть в kivano но нет в sulpak.
# 7. Найдите все товары в магазине sulpak, где компания-производитель содержит букву "m" в имени.
# 8. Найдите товары, которые есть и в kivano u sulpak.
# 9. Найдите китайские товары из kivano, которые в названии содержат "k". 
# 10. Найдите самый последний добавленный товар в таблице produsers, и поменяйте компанию на Apple, и страну на kyrgyzstan.
# 11. Нужно объеденить 2 магазина по product_name и вывести на экран имя продукта и его цену из обоих магазинов, однако не факт что в обоих магазинах будут одинаковые товары, поэтому нужно joinить по полной.
# 12. Найдите самый последний японский товар который был добавлен в produsers.
# 13. Напишите запрос, который прибавит 1000 к цене всех продуктов в sulpak.
# 14. Узнать разницу между самой высокой ценой в sulpak и самой низкой ценой товар в kivano.
# 15. Выведите на экран цены самых дешёвых телефонов из обоих магазинов.
# 16. Удалить все записи где есть NULL в product_name в обоих магазинах.
# 17. Все телефоны у которых год меньше 1998 изменить на 2000 (Выполнить с помощью psycopg2)
# 18. Acer закрыл свою фабрику в Бразилии после 2012 года и переехал в Германию, у всех записей в produsers где Acer был произведен в Brazil после 2012 поставьте Germany.
# 19. Выведите первые 16 записей без id, из kivano.
# 20. Выведите на экран все product_name которые относятся к категории laptops в kivano.
# 21. Найдите товары в sulpak, цена которых больше среднего на 2000 и меньше средний на 2000
# 22. Найдите product_company, чьи товары дороже среднего в kivano.
# 23. Найдите товар который лежит посередине в таблице sulpak.
# 24. Поменяйте страну на South Korea везде где страна Korea и компания Asus.
# 25. В producers поменяйте Nokia на Microsoft везде где у компании Nokia указана страна USA.

import psycopg2
conn = psycopg2.connect(database='markets',user='postgres',password='4567')
cur = conn.cursor()

#Task 1#
# cur.execute('select kivano.category_id,kivano.product_name as kivano_mobile,kivano.price,sulpak.category_id,sulpak.product_name as sulpak_notebook,sulpak.price from kivano join sulpak on kivano.price=sulpak.price where kivano.category_id = 1 and sulpak.category_id = 2;')
# lol = cur.fetchall()
# for i in lol:
#     print(f"mobile - {i[1]} price - {i[2]}. laptop - {i[4]} price - {i[5]}")

#Task 2
# cur.execute("select * from kivano where product_name like 'Iphone%' union select * from sulpak where product_name like 'Iphone%' and product_name like '%12' order by product_name ASC LIMIT 1;")
# answer = cur.fetchall()
# print(f'Последний айфон это - {answer[0][3]}')

#Task 3


select sulpak.*,produsers.prodused_date from sulpak join produsers on produsers.produser_id=sulpak.produser_id where category_id = 2 union all select sulpak.*,produsers.prodused_date from sulpak join produsers on produsers.produser_id = sulpak.produser_id where category_id = 1 and prodused_date in (select prodused_date from kivano join produsers on produsers.prodused_date=kivano.prodused_date);