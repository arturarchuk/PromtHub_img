# Scene Consistency и роли референсов

Этот файл помогает сохранять стабильность сцены, персонажей, товаров и стиля между итерациями.

## Когда использовать

Используй этот файл, если пользователь:

- загружает референс
- хочет того же персонажа в новой сцене
- хочет сохранить лицо, одежду, товар, логотип или позу
- делает серию изображений
- просит storyboard, комикс, несколько кадров, кампанию или набор постов
- жалуется, что результат "поплыл", "не похож", "стиль другой", "товар изменился"

## Назначай роли референсам

Если есть несколько изображений, не пиши просто "use references".

Всегда задавай роль:

- Image A = identity reference
- Image B = pose reference
- Image C = outfit reference
- Image D = style reference
- Image E = background / environment reference
- Image F = product reference
- Image G = texture / material reference

Пример:

Use Image A as the identity reference for the model's face. Use Image B only as the outfit reference. Use Image C as the lighting and color mood reference. Preserve the face from Image A and the product shape from Image B.

## Lock-лист для стабильности

Для персонажа:

- same facial structure
- same eye shape
- same jawline
- same skin tone
- same hairstyle if requested
- same body proportions
- same character identity

Для товара:

- exact product shape
- exact proportions
- exact material finish
- logo placement unchanged
- packaging geometry unchanged
- no redesign

Для сцены:

- same camera angle
- same lighting direction
- same color palette
- same environment logic
- same composition hierarchy

## Не меняй все сразу

Для стабильного результата лучше менять один главный параметр за раз:

- сначала фон
- потом свет
- потом одежду
- потом кадрирование
- потом мелкие детали

Если пользователь просит много изменений сразу, можно сделать prompt, но стоит структурировать его по блокам: Preserve / Change / Style / Constraints.

## Когда пора перезапускать цепочку

После многих итерационных правок качество может деградировать: накапливаются мелкие артефакты, стиль съезжает, лицо меняется, детали становятся грязнее.

Если после 3-5 правок результат ухудшается, лучше не продолжать бесконечно.

Сделай consolidated restart prompt:

1. Возьми лучший текущий результат как новый референс.
2. Сформулируй полный clean prompt заново.
3. Укажи, что нужно сохранить.
4. Укажи только главные изменения.
5. Убери старые противоречивые инструкции.

## Формула restart prompt

Using the best current image as the new reference, recreate the scene cleanly with the same subject identity, composition, lighting direction, and main visual style. Preserve [locked details]. Improve [specific issues]. Avoid accumulated artifacts, over-processing, distorted anatomy, changed identity, and messy background details.

## Storyboard / серия кадров

Для серии кадров назначай постоянные якоря:

- character name
- outfit
- face/identity
- color palette
- camera language
- location logic

Пример:

Character lock: "Maya" is the same woman in every frame, with the same face, hair, body proportions, and outfit. Each panel changes only the action and camera angle.
