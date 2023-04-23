# Арбитраж с помощью Беллмана-Форда

  С помощью алгоритма Беллмана-Форда реализована арбитражная стратегия (найден отрицательный цикл в графе, построенном из курсов
валют: вершины в этом графе представляют валюты, а ребра являются переводами из одной валюты в другую. Длина ребра соответствует
обменному курсу), подробное описание стратегии смотреть
по ссылке: https://pcnews.ru/blogs/arbitraznaa_torgovla_algoritm_bellmana__forda-974587.html#gsc.tab=0

  Разработан интерфейс, в окне которого пользователь нажимает на кнопку start для запуска алгоритма (далее кнопку next для отображения результатов и смены итерации) и кнопку stop для его завершения.
После нажатия start вводится сумма S, на которую осуществляются торги. После нажатия stop и next в консоль выводится сумма S*,
которая получена из суммы S по результатам торгов и количество процентов, на которые изменилась цена S. Также во время работы
чертится и отображается граф (вершины, по которым нужно пройти, чтобы получить арбитраж, обозначены синим цветом, остальные зелёным), который за каждую итерацию обновляется, поскольку курс валют и соотношение между ними также меняется,
считаем, что за каждую итерацию происходит обновление курса и соотношения. 

  Данные генерируются случайным образом на каждой итерации.


# Использование
- Установить `UNIX-makefiles`:
sudo apt install make # Ubuntu
- Установить зависимости и протестировать проект:
make prepare
- Запуск приложения:
make run