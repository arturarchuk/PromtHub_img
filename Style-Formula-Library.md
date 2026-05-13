# Style Formula Library

Быстрая библиотека проверенных формул для света, стиля, материалов и отрицательных constraints. Используй как набор фрагментов, а не как обязательный список для каждого prompt.

## Свет по категориям

| Категория | Когда использовать | Formula fragment |
|-----------|--------------------|------------------|
| Портрет | реалистичный lifestyle / fashion | `soft directional key light, gentle fill light, natural catchlights in the eyes, realistic skin texture, balanced exposure` |
| Портрет ночью | ресторан, авто, город | `warm practical ambient light, soft highlights on the face, visible eye detail, restrained night contrast, no crushed shadows` |
| Beauty | skincare, close-up, editorial | `large diffused beauty light, soft sculpting shadows, luminous but natural skin, clean catchlights, no plastic smoothing` |
| Продукт | clean commercial | `controlled studio softbox lighting, clean reflections, crisp edge highlights, accurate material finish, no harsh glare` |
| Премиальный товар | luxury, watches, perfume | `low-key luxury lighting, precise rim highlights, dark reflective surface, controlled specular accents, premium contrast` |
| Еда | ресторан / реклама | `soft appetizing side light, gentle highlights on moist textures, warm table ambience, realistic food surface detail` |
| Интерьер | вечерний ресторан / архитектура | `layered architectural lighting, warm practical lamps, visible material textures, straight vertical lines, realistic scale` |
| Сцена | cinematic / narrative | `motivated key light from [source], atmospheric depth, readable subject silhouette, balanced foreground and background detail` |
| Постер | графика / афиша | `high-contrast readable lighting, clean negative space, clear separation between subject and typography` |
| Инфографика | схема / диаграмма | `flat clean design lighting, no photographic shadows, high readability, consistent spacing` |

## Negative constraints по категориям

| Категория | Ready-to-use constraints |
|-----------|--------------------------|
| Портрет | `no distorted face, no plastic skin, no glassy eyes, no asymmetrical facial features, no over-smoothed retouching` |
| Лицо с референсом | `do not change identity, do not alter face shape, eye shape, nose, lips, jawline, cheekbones, skin tone, or head proportions` |
| Руки | `no extra fingers, no missing fingers, no fused fingers, no distorted wrists, no duplicated hands` |
| Товар | `no warped product shape, no redesign, no duplicated product, no melted edges, no incorrect logo placement` |
| Логотип / упаковка | `logo placement unchanged, packaging geometry unchanged, no fake labels, no random text, no stretched typography` |
| Постер / текст | `no extra letters, no misspelled words, no random text, no watermark, clean readable typography` |
| Food | `no plastic-looking food, no fake shine, no messy sauce artifacts, no unappetizing colors, no distorted utensils` |
| Интерьер | `no warped walls, no bent vertical lines, no unrealistic scale, no cluttered furniture, no overexposed windows` |
| Сцена | `no cluttered background, no unrelated people, no inconsistent lighting, no muddy color grade, no unreadable subject` |
| Инфографика | `no decorative clutter, no tiny unreadable labels, no incorrect number of steps, no random icons` |

## Проверенные связки: стиль + свет + материал

| Задача | Style + light + material formula |
|--------|----------------------------------|
| Luxury watch | `premium product photography, black marble surface, controlled softbox reflections, crisp metal highlights, restrained black-silver palette` |
| Perfume / skincare | `high-end beauty product still life, translucent glass, soft diffused highlights, clean cream background, realistic liquid reflections` |
| Restaurant portrait | `upscale lifestyle portrait, warm practical restaurant lighting, shallow background blur, natural skin texture, elegant evening palette` |
| Beauty close-up | `beauty editorial close-up, large diffused key light, realistic skin micro-texture, subtle gloss highlights, no plastic retouching` |
| Night car lifestyle | `candid luxury lifestyle photography, low warm ambient car light, city bokeh outside windows, readable face exposure, rich dark interior` |
| Premium dessert | `restaurant dessert advertising, warm side light, glossy fruit highlights, crisp pastry texture, elegant table setting` |
| Tech poster | `modern high-contrast poster design, clean geometric typography, dark background, controlled neon accents, clear headline hierarchy` |
| Architectural interior | `editorial interior photography, layered warm practical lights, natural material texture, straight verticals, realistic depth` |
| Cinematic street scene | `photorealistic cinematic street scene, wet asphalt reflections, motivated streetlight, atmospheric depth, restrained color grade` |
| Clean infographic | `minimal editorial infographic, flat vector-like clarity, consistent grid, exact labels, generous spacing` |

## Mini-fragments для v2

| Нужно улучшить | Добавить в prompt |
|----------------|-------------------|
| Дороже | `more restrained luxury styling, fewer decorative elements, premium materials, controlled contrast` |
| Реалистичнее | `photographic realism, natural imperfections, physically plausible lighting, authentic material texture` |
| Чище | `simpler composition, cleaner background, fewer props, clear subject hierarchy` |
| Мягче | `softer diffused light, gentle tonal transitions, reduced contrast, natural color palette` |
| Контрастнее | `stronger subject separation, defined rim highlights, deeper but still readable shadows` |
| Не как CGI | `real camera photograph, natural lens behavior, no 3D render, no CGI, no plastic surfaces` |
