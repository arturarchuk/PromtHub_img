# Официальные принципы Nano Banana / Gemini image prompting

Этот файл - короткая выжимка практических принципов для Nano Banana 2 / Nano Banana Pro.

## Базовая формула промпта

Хороший prompt обычно отвечает на вопросы:

1. Subject - кто или что в кадре?
2. Action - что происходит?
3. Location - где это происходит?
4. Composition - как построен кадр?
5. Style - в каком визуальном стиле?
6. Lighting - какой свет?
7. Details - какие важные детали должны быть видны?
8. Constraints - чего нельзя делать?

## Простая формула

Create an image of [subject] [action] in [location], with [composition], [style], [lighting], [important details], [constraints].

## Для редактирования изображения

Пиши прямо и конкретно:

- что сохранить
- что изменить
- что убрать
- что добавить
- какие детали нельзя трогать

Пример логики:

Using the reference image, preserve the subject's identity, facial structure, pose, and proportions. Change only the background to [new background]. Keep realistic lighting and natural textures.

## Для текста на изображении

Если нужен текст, укажи его точно.

Пример:

The poster must contain the exact text: "OPEN TONIGHT"

Ограничения:

- no extra random letters
- no misspelled text
- clean readable typography
- clear hierarchy

Если текст не нужен:

- no text
- no letters
- no watermark

## Для референсов

Если пользователь использует референс, сначала реши:

- что переносим из референса
- что меняем
- что запрещено менять

Не меняй лицо, товар, логотип или форму объекта, если пользователь просит сохранить их.

## Главная мысль

Nano Banana хорошо понимает конкретные визуальные инструкции. Чем яснее объект, действие, место, композиция и ограничения, тем лучше результат.
