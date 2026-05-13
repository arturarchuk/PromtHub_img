# INDEX PromptHub

Этот файл - короткая карта проекта. Используй его, чтобы не читать все файлы подряд.

## Минимальный набор для обычного prompt

1. `AGENTS.md`
2. `Архитектура-PromptHub.md`
3. `Уровни-промпта.md` - выбрать нужную глубину prompt
4. `Production-Prompt-Blueprint.md`
5. быстрый memory check по похожим задачам:
   - `Журнал-экспериментов.md`
   - `Мои-удачные-промты.md`
6. один подходящий шаблон:
   - `Шаблон-портрет.md`
   - `Шаблон-товар.md`
   - `Шаблон-постер.md`
   - `Шаблон-сцена.md`
   - `Шаблон-редактирование-фото.md`
   - `Шаблон-beauty-editorial.md`
   - `Шаблон-food.md`
   - `Шаблон-интерьер-архитектура.md`
   - `Шаблон-инфографика.md`
   - `Шаблон-storyboard-серия.md`
   - `Шаблон-character-product-consistency.md`

## Подключай только по ситуации

Если запрос мутный или противоречивый:
`Уточняющие-вопросы.md`

Если пользователь дал обратную связь:
`Правила-обратной-связи.md`
`Журнал-экспериментов.md`

Если нужен v2/v3:
`Протокол-улучшения-v2-v3.md`

Если есть лицо, персонаж, портрет или identity:
`Консистентность-лица-Nano-Banana.md`

Если есть референсы, серия, storyboard или несколько изображений:
`Scene-Consistency-и-Reference-Roles.md`
`Reference-Priority-Protocol.md`

Если есть риск типичной ошибки или prompt начинает звучать слишком общо:
`Анти-паттерны-и-ошибки.md`

Если нужен формат, платформа или aspect ratio:
`Форматы-и-соотношения.md`

Если нужен текст на изображении, диаграмма, инфографика или официальная логика Nano Banana:
`Google-Cloud-Nano-Banana-Guide.md`
`Официальные-принципы-Nano-Banana.md`

Если нужно проверить финальное качество:
`Чеклист-качества-промпта.md`

Если нужен примерный стиль из реальных промптов:
`Prompt-Corpus-Index.md`
`Nano Banana Pro Prompts - www.promptgather.io - nano-banana-pro.md`

Если результат хороший и пользователь хочет сохранить:
`Мои-удачные-промты.md`

Основной рабочий сценарий через веб-Gemini по подписке:
`Gemini-Web-Workflow.md`
`Web-Gemini-Checklist.md`

Если пользователь прислал результат генерации:
`Feedback-Form.md`
`Quality-Score-Rubric.md`

Если работа идет в несколько версий:
`Prompt-Versioning.md`

Если нужно проверить систему после изменений:
`Тестовые-сценарии.md`

Если пользователь явно хочет подключить Google AI Studio / Gemini API / Nano Banana API:
`Nano-Banana-API-Workflow.md`
`API-Test-Quickstart.md`

Если добавляешь новые записи в память:
`Memory-Tags.md`

## Memory check

Перед созданием нового prompt быстро проверь память, если задача похожа на прошлые:

- `Журнал-экспериментов.md` - чтобы не повторять ошибки
- `Мои-удачные-промты.md` - чтобы повторять удачные формулы
- `Memory-Tags.md` - чтобы искать не весь журнал, а релевантные теги

Не читай и не пересказывай всю память пользователю.

Используй только релевантные уроки:

- если новый prompt про лицо/портрет - ищи #face #identity #hands #lighting
- если prompt про товар - ищи #product #lighting #composition
- если prompt про постер/текст - ищи #poster-text #text-rendering #format
- если prompt про editing - ищи #editing #local-edit #identity
- если prompt про референсы - ищи #reference #reference-conflict #identity
- если prompt про ночную сцену - ищи #scene #lighting #composition
- если prompt про серию - ищи #series #reference #composition
- если prompt про food/interior/beauty - ищи #lighting #composition и профильный шаблон

Если релевантной памяти нет, работай по обычному pipeline.

## Что НЕ делать

- Не читать весь prompt corpus при каждом запросе.
- Не подключать все файлы сразу.
- Не делать каждый prompt огромным.
- Не задавать вопросы, если можно безопасно достроить детали.
- Не продолжать бесконечно v2/v3, если качество деградирует; лучше сделать clean restart prompt.

## Быстрый маршрут

Обычная идея -> Architecture -> prompt level -> memory check -> Blueprint -> relevant template -> final RU/EN prompt -> web-Gemini next step.

Сложная/неясная идея -> Clarification -> user answer -> Blueprint -> final RU/EN prompt.

Плохой результат -> Feedback rules -> Memory tags -> Journal -> v2/v3 protocol -> final RU/EN prompt.

Несколько референсов -> Reference roles -> Reference priority -> Blueprint -> final RU/EN prompt.

Основной цикл -> PromptHub пишет prompt -> пользователь генерирует в веб-Gemini -> пользователь присылает результат и обратную связь -> PromptHub делает разбор/v2.
