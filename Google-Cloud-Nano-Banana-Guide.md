# Google Cloud Nano Banana prompting guide

Источник: официальный Google Cloud Blog, "The ultimate Nano Banana prompting guide", 2026-03-05.

Используй этот файл как официальный каркас промптинга для Nano Banana 2 / Nano Banana Pro.

## Главные best practices

1. Будь конкретным: subject, lighting, composition.
2. Используй positive framing: описывай, что нужно получить, а не только что запретить.
3. Управляй камерой: low angle, aerial view, close-up, wide shot, macro, shallow depth of field.
4. Улучшай итерациями: follow-up prompts должны уточнять, что изменить и что оставить.
5. Начинай prompt с сильного действия: create, generate, transform, edit, remove, replace, refine.

## Framework 1: Text-to-image без референсов

Когда нет референса, пользователь фактически выступает режиссером сцены. Не пиши просто набор ключевых слов. Описывай сцену как визуальную постановку.

Формула:

[Subject] + [Action] + [Location/context] + [Composition] + [Style]

Дополнительно можно добавить:

- lighting
- color grading
- materiality and texture
- camera/lens/focus
- aspect ratio
- constraints

Пример структуры:

Create an image of [subject] [action] in [location/context]. Composition: [shot type, framing, angle]. Style: [photography/design/rendering style]. Lighting: [specific lighting]. Materials and textures: [visible details]. Aspect ratio: [ratio]. Constraints: [quality guards].

## Framework 2: Multimodal generation с референсами

Используется, когда пользователь загружает одно или несколько изображений: лицо, продукт, ткань, эскиз, стиль, объект.

Формула:

[Reference images] + [Relationship instruction] + [New scenario]

Всегда уточняй связь:

- use this image as the identity reference
- use this sketch as the composition
- use this product image as the exact object to preserve
- use this fabric sample as the texture
- use this image only as a style reference

Важно: если есть референс, явно пиши, что сохранить и что изменить.

## Framework 3: Image editing

При редактировании уже есть базовое изображение. Prompt должен фокусироваться не на полном описании всего кадра, а на двух вещах:

1. Что изменить.
2. Что оставить точно таким же.

Формула:

Edit the image by changing [target area/object] into [new result]. Keep [unchanged elements] exactly the same.

Примеры keep-секций:

- keep the face unchanged
- keep the pose unchanged
- keep the product shape unchanged
- keep the background unchanged
- keep the lighting unchanged
- keep the composition unchanged

## Framework 4: Real-time information / web-aware images

Nano Banana 2 может использовать актуальную информацию и изображения из web search.

Формула:

[Source/search request] + [Analytical task] + [Visual translation]

Пример логики:

Search for current [topic/data/event]. Use the retrieved information to create a visual representation that shows [visual concept]. Make the image [style/composition].

Используй это только когда пользователь просит актуальность: новости, погода, город сегодня, свежие события, реальные места, текущие данные.

## Framework 5: Text rendering and localization

Nano Banana 2 / Pro хорошо работают с текстом на изображениях, но prompt должен быть точным.

Правила:

- Всегда заключай нужный текст в кавычки.
- Указывай стиль шрифта: bold sans-serif, elegant serif, brush script, condensed uppercase, clean geometric font.
- Указывай расположение текста.
- Указывай иерархию: headline, subheading, small caption.
- Если нужен перевод, явно укажи целевой язык.

Пример:

Render the exact headline text "URBAN EXPLORER" in bold white uppercase sans-serif typography, centered at the top. Add the smaller subtitle "Night Edition" below it in thin condensed lettering.

Ограничения:

- no extra letters
- no misspelled words
- no random text
- clean readable typography

## Prompting like a Creative Director

Чтобы prompt был сильным, управляй сценой как арт-директор.

### 1. Свет

Задавай свет прямо:

- three-point softbox setup
- soft diffused window light
- golden hour backlighting
- chiaroscuro lighting
- warm practical restaurant lighting
- volumetric light through haze
- balanced exposure

### 2. Камера, объектив, фокус

Используй только когда уместно:

- low-angle shot
- aerial view
- eye-level camera angle
- medium close-up
- full body shot
- wide-angle lens
- macro lens
- shallow depth of field
- f/1.8 look

Не добавляй объективы в инфографику, схемы и простые графические постеры.

### 3. Цвет и film look

Используй цвет как инструмент настроения:

- muted teal tones
- warm amber highlights
- 1980s color film look
- slightly grainy analog texture
- clean high-key commercial palette
- restrained luxury color grading

### 4. Материалы и текстуры

Не пиши просто "костюм" или "броня". Пиши физически видимые материалы:

- navy blue tweed jacket
- polished black marble table
- brushed aluminum surface
- translucent glass bottle
- soft silk dress
- realistic skin pores
- wet asphalt reflections

## Aspect ratios and capabilities

Nano Banana 2 / Pro поддерживают популярные ratios:

- 1:1
- 3:2
- 2:3
- 3:4
- 4:3
- 4:5
- 5:4
- 9:16
- 16:9
- 21:9

Nano Banana 2 также может поддерживать экстремальные ratios вроде 1:4, 4:1, 1:8, 8:1.

Используй обычные ratios по умолчанию, если пользователь не просит необычный формат.

## Практическое правило

Для обычного prompt:

Create [subject/action/location] + composition + style + lighting + materiality + aspect ratio + constraints.

Для редактирования:

Edit/change [target] + keep [unchanged elements] exactly the same + constraints.

Для референсов:

Use [reference] as [identity/product/style/composition/texture] + transform into [new scenario] + preserve [critical details].
