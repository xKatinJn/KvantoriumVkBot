# KvantoriumVkBot
Описание
--------
KvantoriumVkBot - это бот, который решает задачу проведения викторины среди участников сообщества Кванториум. Весьма простенько реализован за один длительный вечер.

Функционал
---------
Может приветствовать пользователя и выдавать дальнейшие инструкции. Обрабатывает некорректный ввод данных от пользователя, уведомляя его, и просит ввести данные корректно. Записывает ID диалогов с пользователями, которые прошли викторину, тем самым ограничивая повторное прохождение викторины одним и тем же пользователем.

Настройка и запуск
-----------------
**Установка библиотек**
###
pip install requirements.txt
######
**Переменные окружения**
###
token={Токен группы в ВК}
######
group_id={ID группы в ВК}
######
form_url={Ссылка на форму для отправки результата}
######
csv_path={Путь для записи .csv файла с peer_id участников, которые прошли викторину}
######
**Формат словаря с вопросами**
###
``` python 
questions = {
    'q1': {
        'question': 'Рекурсия это...\n'+
                    'a) То, что никогда не используется\n'+
                    'б) Функция, которая вызывает сама себя и имеет условие для выхода',
        'answers': ['а', 'б'],
        'true': 1                     # Индекс правильного ответа из списка с вопросами
    },
    'q2': {
        'question': 'Что такое ардуино?',
        'answers': ['ЯП для электроники на опр. чипсетах', 'ЯП для сумасшедших', 'ЯП для создания 3Д игр', 'ЯП для всего'],
        'true': 0                     # Индекс правильного ответа из списка с вопросами
    }
}
```
Фото диалога
-------------
![screenshot of sample](https://sun9-71.userapi.com/Be8xweK7kEPlKd59MbU40dwcTTvdkKs4HKuwNg/hJNJMr3OD2E.jpg)
![screenshot of sample](https://sun9-40.userapi.com/Csa4nU9SukJTsj_CoS4V1POyVNo5tUisu_pevw/Ba72sdUjgpQ.jpg)
![screenshot of sample](https://sun9-10.userapi.com/DFjiKUCLCxo7a_fLhaNl7fN0czWC9BKzJ86TGA/z0zdzJXsr3o.jpg)
![screenshot of sample](https://sun9-34.userapi.com/RgKP8t2zBdFlRkRzEC6jWECU1Pvn6DXUwWs5Ng/ncTMTfQi9f4.jpg)
![screenshot of sample](https://sun9-33.userapi.com/MEPiVWob4VkmBe5ePMW9gLnF9vgchTXhG9-HIw/kqbpyPgpI1o.jpg)

>(На фото представлены 2 вопроса с разной реализацией ответов)
