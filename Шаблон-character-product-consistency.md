# Шаблон — Консистентность персонажа / продукта

**Когда использовать:** вариации одного персонажа, маскота, бренд-героя или продукта — с сохранением идентичности при смене позы, эмоции, окружения. Уровень 4.

**Дополнительно:** `Reference-Consistency-Protocol.md`, `Консистентность-лица-Nano-Banana.md`

---

## Система приоритетов референсов

| Приоритет | Изображение | Роль |
|-----------|------------|------|
| 1 (строгий) | Image A | Только identity: лицо, структура, тон кожи |
| 2 | Image B | Поза / одежда / стиль — НЕ identity |
| 3 | Image C | Освещение и цветовая гамма |

**Критически важно:** "Image B is NOT an identity reference. Ignore face, head, hair, skin tone from Image B."

---

## Character Lock (что фиксируется)

```
— Структура лица: форма костей, расположение глаз, нос, подбородок
— Тон кожи и этнические черты
— Пропорции тела
— При смене эмоции — меняется только выражение, геометрия лица неизменна
```

## Product Lock (что фиксируется)

```
— Точная форма и пропорции
— Геометрия упаковки
— Размещение логотипа
— Отделка материала и цвет
— Запрет редизайна или структурных изменений
```

---

## Формат промпта

**Русский:**
```
[Image A] — строгий identity-референс: сохранить точную структуру лица — форму костей, глаза, нос, тон кожи.
[Image B] — только поза и одежда. НЕ identity-референс. Игнорировать лицо, голову, волосы, тон кожи из Image B.
[Image C] — освещение и цветовая гамма.

Создать [описание сцены]: [действие], [ракурс], [среда].
Что меняется: [перечисление]. Что неизменно: [перечисление].
Без дрейфа личности, без смешения черт лица из разных референсов.
```

**English:**
```
[Image A] is the strict identity reference: preserve exact facial structure —
bone geometry, eye shape, nose, skin tone. Do not blend features from other images.
[Image B] provides pose and outfit only. NOT an identity reference.
Ignore face, head, hair, skin tone from Image B.
[Image C] sets lighting and color mood.

Create [scene description]: [action], [angle], [environment].
What changes: [list]. What stays fixed: [list].
No identity drift, no facial feature blending from multiple references.
```

---

## Пример (рейтинг 9/10)

**Задача:** три варианта одного персонажа (fashion-модель) в разных образах, без потери черт лица

**Русский prompt:**
Image A — строгий identity-референс: сохранить точно — структуру скул, форму миндалевидных глаз, прямой нос, тёмно-оливковый тон кожи. Это единственный источник черт лица.

Image B — только вдохновение для позы и наряда. НЕ identity. Игнорировать всё от лица, головы, волос и тона кожи из Image B.

Image C — освещение: мягкий студийный свет, тёплая цветовая гамма.

Создать fashion-портрет: модель в современном минималистичном наряде, уверенная поза, нейтральный фон. Что меняется: наряд, аксессуары, поза. Что неизменно: структура лица, тон кожи, пропорции. Без дрейфа личности, без смешения черт.

**English prompt:**
```text
Image A is the strict identity reference: preserve exactly — cheekbone structure, almond eye shape, straight nose, dark olive skin tone. This is the sole source of facial features.

Image B provides pose and outfit inspiration only. NOT identity. Ignore all face, head, hair, and skin tone from Image B.

Image C sets lighting: soft studio light, warm color palette.

Create fashion portrait: model in contemporary minimalist outfit, confident pose, neutral background. What changes: outfit, accessories, pose. What stays fixed: facial structure, skin tone, body proportions. No identity drift, no facial feature blending.
```

**Ключевой принцип:** Явный запрет "игнорировать лицо из Image B" + перечисление конкретных черт для сохранения — предотвращает смешение identity из разных референсов.
