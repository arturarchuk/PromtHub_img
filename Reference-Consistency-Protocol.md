# Reference Consistency Protocol

Единый протокол для референсов, серий, storyboard, продуктовой консистентности и конфликтующих изображений.

## Когда использовать

Используй этот файл, если пользователь:

- загружает один или несколько референсов;
- хочет сохранить лицо, товар, логотип, одежду, позу или стиль;
- делает серию изображений, кампанию, storyboard или набор вариантов;
- жалуется, что результат "поплыл", "не похож", "товар изменился", "стиль другой";
- дает референс, где есть лишнее лицо, лишний товар или конфликтующий стиль.

## Базовая схема

| Шаг | Что сделать | Готовая формулировка |
|-----|-------------|----------------------|
| 1 | Назначить роль каждому изображению | `Use Image A as the strict identity reference. Use Image B only as the outfit reference.` |
| 2 | Указать главный приоритет | `Identity reference overrides all other references for face and body identity.` |
| 3 | Зафиксировать, что сохранить | `Preserve [face/product/pose/style] exactly.` |
| 4 | Указать, что изменить | `Change only [target] to [desired result].` |
| 5 | Запретить лишнее влияние | `Image B is not an identity reference. Ignore the face, hair, age, skin tone, and body identity from Image B.` |

## Роли референсов

| Роль | Когда применять | Формула |
|------|-----------------|---------|
| Identity | лицо, личность, модель, персонаж | `Image A = strict identity reference` |
| Product | товар, упаковка, логотип, форма | `Image A = exact product reference` |
| Outfit | одежда на другом человеке | `Image B = outfit reference only, not identity` |
| Pose | поза, жест, положение тела | `Image B = pose reference only` |
| Composition | раскладка кадра, ракурс, иерархия | `Image C = composition reference only` |
| Style | цвет, настроение, свет, обработка | `Image C = lighting and color mood reference only` |
| Environment | фон, интерьер, локация | `Image D = background / environment reference only` |
| Texture | ткань, материал, поверхность | `Image E = texture / material reference only` |

## Priority order

Если референсы конфликтуют, порядок должен быть явным:

| Конфликт | Приоритет |
|----------|-----------|
| Лицо vs одежда | Identity reference всегда важнее outfit/pose/style |
| Товар vs стиль | Product reference важнее style для формы, логотипа, пропорций, материала |
| Композиция vs identity | Composition контролирует раскладку, но не лицо и не тело |
| Стиль vs продукт | Style меняет цвет/свет/настроение, но не форму товара |
| Фон vs субъект | Environment reference не должен менять лицо, одежду или товар |

## Lock-листы

### Лицо / identity

Use Image A as the strict identity reference. Preserve the exact facial structure, eye shape, eyelid shape, nose bridge, lip shape, jawline, cheekbone height, chin shape, skin tone, natural skin texture, head proportions, and body identity. This must remain the same person.

### Товар

Use Image A as the exact product reference. Preserve the exact product shape, proportions, logo placement, packaging geometry, color, material finish, and key design details. Do not redesign, simplify, duplicate, stretch, melt, or warp the product.

### Сцена / серия

Keep the same camera language, lighting direction, color palette, environment logic, composition hierarchy, and subject scale across all frames. Change only the action, framing, or scene beat specified for each image.

### Локальное редактирование

Edit only [target area]. Preserve all pixels outside this area as much as possible. Keep the original composition, lighting, perspective, image quality, face, body, clothing, background, and color grade unchanged.

## Если референс содержит лишнее лицо

Image B is not an identity reference. Ignore the face, head, hair, skin tone, age, facial features, expression, and body identity from Image B. Use Image B only for [outfit/pose/style].

Если можно, попроси пользователя обрезать референс до нужной детали.

## Если нужно изменить выражение лица

Keep the same face geometry and identity from Image A. Change only the expression to [desired expression]. Do not change the eye shape, nose, lips, jawline, cheekbones, face width, head angle, or facial proportions.

## Серия / storyboard

Перед серией зафиксируй якоря:

| Якорь | Что записать |
|-------|--------------|
| Character lock | имя/роль, лицо, возрастной диапазон, волосы, пропорции |
| Outfit lock | одежда, аксессуары, материал, цвет |
| Product lock | форма, логотип, упаковка, масштаб |
| Style lock | палитра, свет, camera language, обработка |
| Scene logic | место, время, погода, предметы окружения |

Формула:

Character lock: "[Name]" is the same person in every frame, with the same face, hair, body proportions, and outfit. Each frame changes only the action, camera angle, and narrative beat.

## Не меняй все сразу

Для стабильного результата лучше менять один главный параметр за раз:

- фон;
- свет;
- одежду;
- кадрирование;
- мелкие детали.

Если пользователь просит много изменений сразу, структурируй prompt блоками: `Preserve / Change / Reference roles / Style / Constraints`.

## Consolidated restart

После 3-5 правок качество может деградировать: появляются артефакты, лицо или товар меняется, стиль становится грязнее.

Формула restart:

Using the best current image as the new reference, recreate the scene cleanly with the same subject identity, composition, lighting direction, and main visual style. Preserve [locked details]. Improve [specific issues]. Avoid accumulated artifacts, over-processing, distorted anatomy, changed identity, warped product shape, and messy background details.

## Финальный checklist

- У каждого референса есть роль?
- Есть главный identity/product reference?
- Есть priority order при конфликте?
- Запрещено брать лицо из не-identity референса?
- Запрещено менять форму товара из product reference?
- Понятно, что изменить и что сохранить?
- Для серии зафиксированы character/product/style anchors?
