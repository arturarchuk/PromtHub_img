# QUICK-REF — PromptHub One-Page Card

Открывай первым, если нужно быстро понять маршрут. Для деталей переходи в `INDEX.md`.

## 5 уровней промпта

| Level | Когда применять | Смысл |
|-------|-----------------|-------|
| 1 Quick | простая идея, низкий риск | коротко и без перегруза |
| 2 Production | портрет, товар, beauty, poster, коммерция | полный визуальный контроль |
| 3 Structured | сложная сцена, текст, несколько объектов | блоки и иерархия |
| 4 High-Risk Lock | лицо, бренд, продукт, серия, референсы | жёсткая фиксация identity/product |
| 5 Local Edit | точечная правка фото | менять только указанную область |

## Формат ответа

Русский prompt:
[готовый подробный prompt на русском языке]

English prompt:
```text
[ready-to-copy English prompt for Nano Banana 2]
```

Следующий шаг: сгенерируй изображение в web-Gemini по English prompt и пришли результат + что нравится, что не нравится, что сохранить и что изменить.

## Топ-10 constraints

| Риск | Constraint |
|------|------------|
| Пластиковое лицо | `natural realistic skin texture, visible pores, no plastic retouching` |
| Неживые глаза | `natural catchlights, relaxed eyelids, no glassy eyes` |
| Искажённое лицо | `do not distort facial structure, keep face proportions natural` |
| Плохие руки | `natural hand anatomy, no extra fingers, no distorted hands` |
| Руки не важны | `hands relaxed and partially outside the frame` |
| Товар поплыл | `preserve exact product shape, no warped geometry, no redesign` |
| Лишний текст | `no random text, no watermark, no extra letters` |
| Нужен точный текст | `exact readable text: "[TEXT]", no misspelled words` |
| Тёмный результат | `balanced exposure, visible key details, no underexposed shadows` |
| Перегруженный фон | `clean background, uncluttered composition, clear subject separation` |

## Маршрут по типу задачи

| Тип | Открыть |
|-----|---------|
| Новая генерация | `INDEX.md` → нужный `Шаблон-*.md` → `Style-Formula-Library.md` |
| Редактирование | `Шаблон-редактирование-фото.md` + Level 5 |
| Референсы / серия | `Reference-Consistency-Protocol.md` |
| V2 / V3 | `Протокол-улучшения-v2-v3.md` + `Журнал-экспериментов.md` |
| Оценка результата | `Quality-Score-Rubric.md` |
| API / web запуск | `API-Guide.md` |

## Быстрая формула prompt

`Subject + Action + Location/context + Composition + Style + Lighting + Materials/texture + Aspect ratio + Constraints`
