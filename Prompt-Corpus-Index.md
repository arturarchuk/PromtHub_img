# Prompt Corpus Index

Этот файл - быстрый индекс к разбитому корпусу в папке `corpus/`.

Не читай весь corpus для обычного prompt. Используй этот индекс как карту паттернов, а конкретные файлы открывай только при необходимости.

## Что есть в corpus

Корпус содержит примеры Nano Banana Pro prompts в двух основных формах:

- обычный text prompt
- structured / JSON-style prompt

Полезен не для копирования, а для изучения:

- структуры сцен
- reference wording
- lighting language
- constraints
- product/fashion/cinematic композиции
- text rendering
- JSON-style группировки

## Файлы корпуса

| Категория | Файл |
|-----------|------|
| Portrait / fashion / identity | `corpus/portrait.md` → части `corpus/portrait-01.md` ... `corpus/portrait-04.md` |
| Product / commercial | `corpus/product.md` |
| Cinematic / scene / environment | `corpus/scene.md` |
| Poster / text / infographic | `corpus/poster.md` |
| Food / beverage | `corpus/food.md` |

## Основные категории

### Portrait / fashion / identity

Паттерны:

- subject as main focus
- identity preservation from reference
- outfit and pose as separate blocks
- face clarity and natural skin texture
- background softly blurred

Используй для:

- портретов
- fashion-съемки
- influencer visuals
- identity reference задач

Не копируй:

- конкретные лица, имена, уникальные описания людей
- чрезмерные promises вроде 1000% identical

### Product / commercial

Паттерны:

- exact product shape
- material finish
- surface reflections
- controlled studio lighting
- clean commercial background

Используй для:

- косметики
- часов
- упаковки
- gadgets
- рекламных карточек

Добавляй:

- no warped product shape
- no redesign
- no duplicated product
- logo placement unchanged if reference exists

### Cinematic / scene

Паттерны:

- clear narrative moment
- foreground / midground / background
- weather and atmosphere
- color grading
- camera angle

Используй для:

- городских сцен
- исторических сцен
- sci-fi / fantasy
- luxury lifestyle

Осторожно:

- не добавляй cinematic language в товар, схему или чистый постер без причины

### Poster / thumbnail / text rendering

Паттерны:

- exact text in quotes
- typography hierarchy
- high contrast
- clean negative space
- readable layout

Используй для:

- афиш
- YouTube thumbnail
- баннеров
- карточек

Добавляй:

- no extra letters
- no misspelled words
- no random text
- clean readable typography

### Reference composition

Паттерны:

- Image A as identity reference
- Image B as outfit/product/style reference
- preserve critical details
- blend with consistent perspective, lighting and scale

Используй вместе с:

- `Reference-Consistency-Protocol.md`

### Infographic / diagram

Паттерны:

- labels must be exact
- sections/nodes count
- clean spacing
- informational hierarchy
- no decorative clutter

Используй вместе с:

- `API-Guide.md`
- `Production-Prompt-Blueprint.md`

## Useful structural patterns

### Text prompt pattern

Create an image of [subject] [action/context]. Composition: [framing/angle]. Style: [visual medium]. Lighting: [source/mood]. Details: [materials/textures]. Constraints: [relevant guards]. Aspect ratio: [ratio].

### JSON-style pattern

Используй только для сложных задач:

```text
{
  "Objective": "...",
  "Subject": "...",
  "Reference_Roles": "...",
  "Composition": "...",
  "Lighting": "...",
  "Materials": "...",
  "Constraints": "..."
}
```

JSON-style полезен, когда много требований, но для простых prompt он слишком тяжелый.

## Corpus rules

- Не копировать full prompt из corpus без запроса.
- Не имитировать один пример слишком близко.
- Не брать уникальные имена, тексты, бренды или сцены без причины.
- Использовать только reusable pattern.
- Для обычной работы достаточно этого индекса.
