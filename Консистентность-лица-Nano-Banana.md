# Консистентность лица в Nano Banana

Этот файл используется для портретов, fashion, beauty, image editing, reference image и любых задач, где важно сохранить лицо или сделать его живым.

## Главное ограничение

Nano Banana не гарантирует 100% одинаковое лицо между разными генерациями. Даже хороший prompt не заменяет качественный reference image.

Если нужно сохранить конкретного человека, всегда лучше использовать референс.

## Лучшие референсы

Хороший референс:

- разрешение 1024x1024 или выше
- лицо хорошо видно
- лицо занимает заметную часть кадра
- ровный фронтальный или мягкий свет
- глаза, нос, рот и линия челюсти не закрыты
- нейтральное выражение или легкая естественная улыбка
- ракурс анфас или 3/4 до 45 градусов
- без очков, рук у лица, сильных теней, волос поверх глаз

Для лучшей стабильности лица полезно иметь 2-3 референса:

- анфас
- 3/4
- легкая улыбка или другой близкий ракурс

## Базовый блок сохранения лица

Для image-to-image и задач с референсом добавляй:

Preserve the exact facial structure, eye shape, eyelid shape, nose bridge, lip shape, jawline, cheekbone height, chin shape, skin tone, and natural skin texture from the reference image.

This must be the same person as in the reference image. Do not alter the face geometry, identity, facial proportions, or recognizable features.

## Если лицо становится широким или пухлым

Добавляй в позитивный prompt:

- natural facial proportions
- defined jawline
- realistic bone structure
- natural cheekbone definition
- face shape matching the reference image

Добавляй в ограничения:

- avoid puffy cheeks
- avoid bloated face
- avoid widened jaw
- avoid double chin
- avoid swollen facial features

Не используй эти ограничения, если пользователь специально просит пухлое/круглое лицо.

## Если кожа пластиковая

Добавляй:

- realistic skin texture
- visible pores
- subtle skin imperfections
- natural micro-details
- natural skin tone variation

Ограничения:

- no plastic skin
- no waxy appearance
- no airbrushed skin
- no over-retouched beauty look
- no overly smooth skin

## Если глаза плоские или неживые

Добавляй:

- sharp clear eyes
- natural catchlights
- wet eye reflections
- detailed irises
- alive gaze
- soft light reflected in the eyes

Ограничения:

- no flat eyes
- no empty gaze
- no doll-like expression
- no lifeless eyes

## Фиксируй ракурс

Если нужно несколько похожих изображений одной модели, не меняй ракурс слишком резко.

Хорошая стабильная формула:

3/4 portrait shot, eye-level camera angle, medium close-up, 85mm portrait lens equivalent.

Для портретов без референса тоже полезно фиксировать:

- same camera angle
- same face orientation
- same lighting direction
- same crop

## Многоэтапный рабочий процесс

Для сложных портретов не пытайся получить идеал за один раз.

1. Сначала получить хорошую композицию.
2. Выбрать вариант, где лицо ближе всего к нужному.
3. Использовать лучший результат как новый референс.
4. Отдельно улучшить лицо:

Refine the face only. Improve skin texture realism, sharpen the eyes, preserve exact facial structure, maintain identity, keep background, clothing, body position, and lighting unchanged.

5. Если нужно, отдельно исправить руки или волосы.

## Когда пользователь жалуется на лицо

Если пользователь говорит:

- лицо не похоже
- лицо стало широким
- лицо пластиковое
- глаза мертвые
- не живое
- слишком ретушированное
- лицо другое
- лицо поплыло

Проект должен:

1. Выбрать теги, обычно #face #identity и при необходимости #lighting или #editing.
2. Записать короткий урок в `Журнал-экспериментов.md`.
3. Сделать v2 с блоком face preservation или face realism.
4. Если есть референс, усилить сохранение identity.
5. Если референса нет, честно улучшить реализм, но не обещать 100% одинаковость.
