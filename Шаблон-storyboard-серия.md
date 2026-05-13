# Шаблон: storyboard / серия / кампания

Используй для серии изображений, storyboard, набора постов, кампании, нескольких кадров одного персонажа или товара.

## Что нужно зафиксировать

Постоянные якоря:
- персонаж / товар
- identity
- outfit
- стиль
- палитра
- локация или логика мира
- camera language

Что может меняться:
- действие
- ракурс
- эмоция
- кадрирование
- фон, если задано
- время суток, если нужно

## Формат серии

Для каждого кадра укажи:

Frame 1:
- action
- composition
- key detail

Frame 2:
- action
- composition
- key detail

Frame 3:
- action
- composition
- key detail

## Ограничения

- same character identity in every frame
- same product shape in every frame
- consistent color palette
- consistent lighting logic
- no random outfit changes
- no identity drift
- no product redesign

## Рабочий формат

Русский prompt:
Серия из [количество] кадров: постоянные якоря [персонаж/товар/стиль], кадр 1 [действие], кадр 2 [действие], кадр 3 [действие], [ограничения consistency].

English prompt:
Create a [number]-frame series with the same [character/product/style] across all frames. Character/product lock: [anchors]. Frame 1: [action/composition]. Frame 2: [action/composition]. Frame 3: [action/composition]. Constraints: consistent identity, style, palette, lighting, no drift.
