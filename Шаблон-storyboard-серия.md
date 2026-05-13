# Шаблон — Storyboard / Серия / Кампания

**Когда использовать:** серия изображений с единым персонажем, продуктом или стилем — для кампаний, контента, storyboard'ов. Уровень 4.

**Дополнительно:** `Scene-Consistency-и-Reference-Roles.md`, `Reference-Priority-Protocol.md`

---

## Зафиксируй якоря перед стартом

Перед написанием промптов для серии определи и зафиксируй **неизменяемые элементы**:

- Персонаж / продукт — identity, форма
- Outfit (если нужна консистентность)
- Стиль и цветовая палитра
- Свет-логика (откуда свет в этом мире)
- Соотношение сторон

**Изменяемые между кадрами:** действие, ракурс, эмоция, детали фона, время суток

---

## Формат промпта для серии

**Русский:**
```
Серия из [N] кадров с одним [персонажем/продуктом/стилем] во всех сценах.

Якоря (не меняются):
— Персонаж/продукт: [описание]
— Outfit: [описание] / Продукт: [форма, цвет, логотип]
— Стиль: [описание]
— Палитра: [цвета]

Кадр 1: [действие] — [ракурс] — [отличительная деталь]
Кадр 2: [действие] — [ракурс] — [отличительная деталь]
Кадр N: ...

Правила консистентности: не менять лицо, не менять продукт, не менять цветовую схему,
без гардеробных несоответствий, без дрейфа личности, без редизайна продукта.
```

**English:**
```
Create a [N]-frame series with the same [character/product/style] across all frames.

Locked anchors:
— Character/product: [description]
— Outfit: [description] / Product: [shape, color, logo]
— Style: [description]
— Color palette: [colors]

Frame 1: [action] — [angle] — [distinctive detail]
Frame 2: [action] — [angle] — [distinctive detail]
Frame N: ...

Consistency rules: do not change face, do not redesign product, preserve color scheme,
no wardrobe inconsistencies, no identity drift, no product redesign.
```

---

## Правила консистентности

```
maintain character identity across all frames,
preserve product shape and logo placement unchanged,
consistent light logic (same light direction world),
no identity drift between frames,
no wardrobe changes unless specified
```

---

## Пример (рейтинг 8/10)

**Задача:** серия из 3 кадров для бренда косметики — один продукт, разные сцены использования

**Русский prompt:**
Серия из 3 кадров для beauty-бренда с одним продуктом — белый тюбик крема с золотым логотипом "AURA" — во всех сценах.

Якоря: тюбик строго без изменений (форма, цвет, логотип, пропорции), стиль — премиальный минимализм, палитра — белый / золотой / бежевый.

Кадр 1: тюбик на мраморной поверхности, утренний мягкий свет — ракурс 45°, без пропсов.
Кадр 2: женская рука держит тюбик, выдавливает крем — крупный план руки, боковой студийный свет.
Кадр 3: тюбик на фоне зелени у окна — естественный дневной свет, атмосфера природы.

Во всех кадрах: продукт читается чётко, логотип виден, без случайного текста, без деформации упаковки.

**English prompt:**
```text
3-frame series for a beauty brand featuring one product — white cream tube with gold "AURA" logo — across all frames.

Locked anchors: tube strictly unchanged (shape, color, logo, proportions), style — premium minimalism, palette — white / gold / beige.

Frame 1: tube on marble surface, soft morning light — 45-degree angle, no props.
Frame 2: female hand holding tube, applying cream — close-up of hand, side studio light.
Frame 3: tube against green foliage near window — natural daylight, nature atmosphere.

All frames: product clearly legible, logo visible, no random text, no packaging distortion.
```

**Ключевой принцип:** Явный список "якорей" в начале промпта + "без дрейфа продукта" предотвращают самопроизвольный редизайн между кадрами.
