# Memory Tags

Этот файл задает теги для `Журнал-экспериментов.md` и `Мои-удачные-промты.md`.

## Зачем нужны теги

Память должна быстро находиться по типу риска. Если журнал растет без тегов, memory check становится медленным и неточным.

## Формат строки тегов

Добавляй к новым записям строку:

Теги:
#face #identity #lighting

Используй 2-5 тегов. Не ставь все подряд.

## Основные теги

#face
Лицо, кожа, глаза, выражение, живость, сходство.

#identity
Сохранение конкретного человека или персонажа.

#hands
Руки, пальцы, жесты, hand choreography.

#product
Товар, упаковка, форма, материал, логотип.

#poster-text
Текст на изображении, типографика, постер, баннер, thumbnail.

#reference
Любая задача с референсами.

#reference-conflict
Несколько референсов, конфликт ролей, одежда с чужим лицом, style vs identity.

#editing
Правка существующего изображения.

#local-edit
Точечная правка области, аксессуаров, фона, деталей.

#lighting
Свет, экспозиция, тени, плоскость, драматичность.

#composition
Кадрирование, ракурс, дистанция, главный объект, перегруз кадра.

#format
Aspect ratio, платформа, сторис, пост, thumbnail, баннер.

#ethno-history
Этническая, историческая, культурная точность костюма, типажа, материала.

#scene
Кинематографичная сцена, окружение, атмосфера, сюжет.

#series
Серия кадров, storyboard, consistency между изображениями.

#text-rendering
Точный текст, читаемость, отсутствие лишних букв.

#beauty
Beauty, skincare, editorial portrait, кожа, косметика, premium cover.

#food
Еда, напитки, ресторан, сервировка, food photography.

#interior
Интерьер, архитектура, пространство, ресторан, отель, квартира.

#versioning
v1/v2/v3, clean restart, сравнение версий.

## Как выбирать теги

Выбирай теги по причине риска, а не только по теме картинки.

Пример:
Портрет в ресторане, лицо пластиковое и темно.

Теги:
#face #lighting #scene

Пример:
Платье взяли из Image B, но лицо тоже смешалось с Image B.

Теги:
#identity #reference #reference-conflict

Пример:
Серьги стали огромными при локальном редактировании.

Теги:
#editing #local-edit #composition

## Правило для memory check

Перед новым prompt ищи не весь журнал, а релевантные теги:

- портрет -> #face #identity #lighting
- товар -> #product #lighting
- постер -> #poster-text #text-rendering #format
- редактирование -> #editing #local-edit #identity
- несколько референсов -> #reference #reference-conflict #identity
- серия -> #series #reference #composition
- исторический образ -> #ethno-history #identity #reference
- beauty -> #beauty #face #lighting
- food -> #food #lighting #composition
- interior -> #interior #lighting #composition
- версии -> #versioning #feedback
