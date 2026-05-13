# API Test Quickstart

Этот файл нужен для локальной проверки Nano Banana / Gemini image generation API.

## Перед тестом

Если API key был отправлен в чат, удали его в Google AI Studio и создай новый.

Не присылай новый ключ в чат.

## Настройка

1. Открой уже созданный `.env` локально и вставь новый ключ:

```bash
GOOGLE_API_KEY=PASTE_YOUR_NEW_SECRET_HERE
GOOGLE_AI_PROJECT_ID=projects/168169110837
```

2. Замени `PASTE_YOUR_NEW_SECRET_HERE` на новый ключ.

## Быстрый запуск

После вставки ключа выполни:

```bash
scripts/run_nano_banana_test.sh
```

Скрипт сам установит зависимости из `requirements.txt` и запустит тест.

## Ручная установка зависимостей

Если хочешь делать шаги вручную:

```bash
python3 -m pip install -r requirements.txt
```

## Запуск теста

```bash
python3 scripts/nano_banana_api_test.py
```

Если всё работает, изображение появится в `outputs/`.

## Смена модели

По умолчанию используется:

```bash
gemini-2.5-flash-image
```

В API обычно используются model id, а не маркетинговое имя "Nano Banana 2".

Официальные варианты для image generation:

- `gemini-2.5-flash-image` - Nano Banana / быстрый image model.
- `gemini-3-pro-image-preview` - Nano Banana Pro / Pro image model.

Если хочешь тестировать Pro-вариант, в `.env` замени:

```bash
NANO_BANANA_MODEL=gemini-2.5-flash-image
```

на:

```bash
NANO_BANANA_MODEL=gemini-3-pro-image-preview
```

Можно временно задать другую модель:

```bash
NANO_BANANA_MODEL="model-name-here" python3 scripts/nano_banana_api_test.py
```

## Смена prompt

```bash
NANO_BANANA_TEST_PROMPT="Create a clean product photo of black sunglasses on marble, no text." python3 scripts/nano_banana_api_test.py
```

## Что делать с ошибками

- `Missing GOOGLE_API_KEY` - ключ не найден в `.env` или окружении.
- `Missing dependency` - установи `google-genai pillow`.
- `API key not valid` - ключ удален, скопирован неверно или не от того аккаунта.
- `Billing required` - нужна привязка billing к Google Cloud project.
- `Model not found` - модель недоступна для аккаунта/API, проверь актуальное имя модели.
- `Quota exceeded` - закончился лимит, проверь Usage / Rate Limit / Billing.
