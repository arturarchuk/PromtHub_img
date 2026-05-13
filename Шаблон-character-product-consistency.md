# Шаблон: character / product consistency

Используй, когда нужно сохранить одного персонажа, лицо, товар, упаковку, бренд или объект между вариантами.

## Character lock

Фиксируй:
- same facial structure
- same eye shape
- same eyelid shape
- same nose bridge
- same lip shape
- same jawline
- same cheekbone height
- same chin shape
- same skin tone
- same hair if needed
- same body proportions

Если меняется эмоция:
Change only the expression to [emotion]. Keep the same face geometry and identity.

## Product lock

Фиксируй:
- exact product shape
- exact proportions
- packaging geometry
- logo placement
- material finish
- cap/lid shape
- label area
- color

Ограничения:
- no redesign
- no warped product shape
- no duplicated product
- no changed logo placement
- no simplified packaging

## Reference priority

Если несколько референсов:

- Image A = strict identity/product reference
- Image B = pose/outfit/style only
- Image C = lighting/color mood only

Запрет:
Image B is not an identity reference. Ignore face, head, hair, skin tone and facial features from Image B.

## Рабочий формат

Русский prompt:
Используй Image A как строгий reference для [лица/товара]. Сохрани [lock-list]. Используй Image B только для [роль]. Измени [что меняется]. Не меняй [критичные элементы].

English prompt:
Use Image A as the strict [identity/product] reference. Preserve [lock list]. Use Image B only as [role]. Change [target change]. Do not alter [critical elements].
