# API Guide — Gemini / Nano Banana Workflow

Единый гайд по web-Gemini workflow, локальному Nano Banana / Gemini API, моделям, безопасности и типовым ошибкам.

Стандартный путь проекта: PromptHub пишет prompt, пользователь генерирует в web-Gemini, затем присылает результат и feedback. Локальный API используется только при явном запросе запуска или теста.

> **Безопасность:** API-ключи только в `.env`. Никогда не хранить в коде, чате или репозитории.

---

## Часть 1 — Основной web-Gemini workflow

### Перед генерацией

| Проверка | Что должно быть готово |
|----------|------------------------|
| Режим | Открыт web-Gemini / Create images, выбран доступный режим Fast / Thinking / Pro |
| Prompt | English prompt скопирован полностью |
| Формат | Aspect ratio указан в prompt, если важен |
| Текст | Нужная фраза в кавычках; если текст не нужен — есть `no text / no letters / no watermark` |
| Референсы | Все изображения загружены до отправки prompt, роли референсов понятны |
| Портрет | Лицо достаточно крупно, глаза видны, есть `natural skin texture`, если нужен реализм |
| Товар | Форма, материал и логотип закреплены; есть `no warped product shape / no redesign` |
| Постер | Есть точный текст, иерархия, место под типографику и запрет лишних букв |

### После генерации

Пользователь присылает:

1. результат изображения;
2. что нравится;
3. что не нравится;
4. что сохранить;
5. что изменить;
6. оценку близости 1-10.

Если результат почти хороший, feedback должен быть точечным: сохранить композицию/лицо/свет, исправить только руки, фон, текст или товар.

Если результат совсем не тот, нужно указать, какая цель была на самом деле: `v2`, `local edit` или `clean restart`.

---

## Часть 2 — Prompt frameworks

| Тип задачи | Формула |
|------------|---------|
| Text-to-image | `[Subject] + [Action] + [Location/context] + [Composition] + [Style] + [Lighting] + [Materials] + [Aspect ratio] + [Constraints]` |
| Reference composition | `Use [Image A] as [role]. Transform into [new scenario]. Preserve [critical details]. Ignore [irrelevant parts].` |
| Image editing | `Edit only [target] into [new result]. Keep [unchanged elements] exactly the same.` |
| Text rendering | `Render the exact text "[TEXT]" with [font style], [position], [hierarchy]. No extra letters, no misspellings.` |
| Realtime / web-aware | `Search/use current [topic]. Translate the retrieved information into [visual concept].` |

Практическое правило: пиши как creative director, а не как набор тегов. Управляй субъектом, композицией, светом, материалами и ограничениями.

---

## Часть 3 — Когда использовать API (а когда нет)

**Используй API для:**
- Локального тестирования промптов
- Автоматизации пакетной генерации
- Проверки биллинга и квот
- Разработки и отладки интеграций

**НЕ используй API для:**
- Стандартной генерации по запросу пользователя → web-Gemini
- Работы с промптами в рамках обычного workflow → web-Gemini

---

## Часть 4 — Настройка API

### 4.1 Получить API-ключ

1. Открыть [Google AI Studio](https://aistudio.google.com/)
2. Создать новый API-ключ
3. Скопировать ключ — он показывается только один раз

### 4.2 Настроить .env

Создать файл `.env` в корне проекта:

```env
GOOGLE_API_KEY=ваш_ключ_здесь
GOOGLE_AI_PROJECT_ID=projects/168169110837
```

**Обязательно:** убедись, что `.env` добавлен в `.gitignore`:
```
echo ".env" >> .gitignore
```

### 4.3 Установить зависимости

```bash
pip install -r requirements.txt
```

Или используй скрипт с автоустановкой:
```bash
bash scripts/run_nano_banana_test.sh
```

---

## Часть 5 — Доступные модели

| Модель | ID | Применение |
|--------|----|-----------|
| Standard (быстрая) | `gemini-2.5-flash-image` | Быстрое тестирование, высокий throughput |
| Pro | `gemini-3-pro-image-preview` | Максимальное качество, медленнее |

**По умолчанию** используется `gemini-2.5-flash-image`. Переключить на Pro:
```bash
NANO_BANANA_MODEL=gemini-3-pro-image-preview bash scripts/run_nano_banana_test.sh
```

---

## Часть 6 — Запуск API

### Быстрый тест

```bash
bash scripts/run_nano_banana_test.sh
```

### С кастомным промптом

```bash
NANO_BANANA_TEST_PROMPT="Portrait of a woman, natural lighting, realistic skin texture" \
  bash scripts/run_nano_banana_test.sh
```

### Результаты

Сгенерированные изображения сохраняются в папке `outputs/`.

---

## Часть 7 — Стандартный workflow с API

```
Написать промпт (AGENTS.md пайплайн)
        ↓
Запустить через scripts/run_nano_banana_test.sh
        ↓
Результат в outputs/
        ↓
Оценить → дать обратную связь
        ↓
Записать в Журнал-экспериментов.md
        ↓
Итерация v2/v3 по Протокол-улучшения-v2-v3.md
```

---

## Часть 8 — Решение проблем

| Проблема | Причина | Решение |
|----------|---------|---------|
| `INVALID_API_KEY` | Ключ неверный или истёк | Создать новый в AI Studio, обновить `.env` |
| `BILLING_REQUIRED` | Биллинг не подключён | Подключить платёжный метод в Google Cloud Console |
| `MODEL_NOT_FOUND` | Модель недоступна в регионе | Попробовать `gemini-2.5-flash-image` как fallback |
| `QUOTA_EXCEEDED` | Превышен лимит запросов | Подождать сброса квоты или повысить лимиты |
| Зависимости не установлены | pip не запускался | `pip install -r requirements.txt` вручную |
| Ключ в репозитории | Случайно закоммичен | Немедленно отозвать в AI Studio, создать новый |

---

## Часть 9 — Безопасность

**Критические правила:**
- Никогда не хранить ключи в коде, markdown-файлах или чате
- `.env` всегда в `.gitignore`
- Если ключ утёк — отозвать немедленно в [AI Studio](https://aistudio.google.com/) и создать новый
- Не передавать ключи другим участникам — каждый создаёт свой

**Если ключ появился в переписке:**
1. Немедленно отозвать в AI Studio
2. Создать новый ключ
3. Обновить `.env`
4. Убедиться, что `.gitignore` настроен

---

## Связанные файлы

- `Gemini-Web-Workflow.md` — стандартный workflow через браузер
- `requirements.txt` — зависимости Python
- `scripts/run_nano_banana_test.sh` — скрипт запуска
