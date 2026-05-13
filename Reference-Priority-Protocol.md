# Reference Priority Protocol

Этот файл используется, когда есть один или несколько референсов.

## Главный принцип

Никогда не пиши просто "use references". У каждого изображения должна быть роль, приоритет и список того, что из него нельзя брать.

## Базовая схема

1. Назначь роль каждому изображению.
2. Определи главный приоритет.
3. Укажи, что сохранить.
4. Укажи, что изменить.
5. Запрети влияние лишних частей референса.

## Типовые роли

- Image A = strict identity reference
- Image B = outfit reference only
- Image C = pose reference only
- Image D = lighting and color mood reference only
- Image E = background reference only
- Image F = exact product reference
- Image G = texture/material reference only

## Priority order

Если референсы конфликтуют, порядок должен быть явным:

Identity reference overrides all other references for face and body identity.
Product reference overrides style reference for shape, logo, packaging, proportions, and material.
Composition reference controls layout only, not identity or style.
Style reference controls color, lighting, and mood only, not object shape or face.

## Когда референс содержит лишнее лицо

Если референс нужен для одежды, позы или стиля, но в нем есть лицо другого человека, добавляй:

Image B is not an identity reference. Ignore the face, head, hair, skin tone, age, facial features, expression, and body identity from Image B. Use Image B only for [outfit/pose/style].

Лучше, если пользователь может обрезать такой референс до нужной детали.

## Когда референс содержит товар

Для товара добавляй:

Use Image A as the exact product reference. Preserve the exact product shape, proportions, logo placement, packaging geometry, color, material finish, and key design details. Do not redesign, simplify, duplicate, stretch, or warp the product.

## Когда нужно сохранить лицо

Для лица добавляй:

Use Image A as the strict identity reference. Preserve the exact facial structure, eye shape, eyelid shape, nose bridge, lip shape, jawline, cheekbone height, chin shape, skin tone, and natural skin texture. This must remain the same person.

## Когда нужно изменить выражение лица

Разделяй эмоцию и identity:

Keep the same face geometry and identity from Image A. Change only the expression to [desired expression]. Do not change the eye shape, nose, lips, jawline, cheekbones, face width, head angle, or facial proportions.

## Когда нужно локальное редактирование

Для точечной правки добавляй:

Edit only [target area]. Preserve all pixels outside this area as much as possible. Keep the original composition, lighting, perspective, image quality, face, body, clothing, background, and color grade unchanged.

## Reference conflict checklist

Перед финальным prompt проверь:

- Есть ли роль у каждого референса?
- Есть ли главный identity/product reference?
- Есть ли priority order?
- Запрещено ли брать лицо из не-identity референса?
- Запрещено ли менять форму товара из product reference?
- Понятно ли, что менять и что сохранять?
