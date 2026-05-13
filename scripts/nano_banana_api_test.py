from __future__ import annotations

import os
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
DEFAULT_MODEL = "gemini-2.5-flash-image"
DEFAULT_PROMPT = (
    "Create a simple studio product photo of a single red apple on a white "
    "ceramic plate, soft natural window light, clean background, realistic "
    "texture, no text, no watermark, square 1:1 composition."
)


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def main() -> int:
    load_dotenv(ROOT / ".env")

    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Missing GOOGLE_API_KEY. Add it to .env or export it in your shell.")
        return 2

    try:
        from google import genai
    except ImportError:
        print("Missing dependency: google-genai")
        print("Install it with: python3 -m pip install google-genai pillow")
        return 2

    model = os.environ.get("NANO_BANANA_MODEL", DEFAULT_MODEL)
    prompt = os.environ.get("NANO_BANANA_TEST_PROMPT", DEFAULT_PROMPT)

    OUTPUTS.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model,
        contents=[prompt],
    )

    saved = 0
    for index, part in enumerate(response.parts):
        if getattr(part, "text", None):
            print(part.text)
            continue

        inline_data = getattr(part, "inline_data", None)
        if inline_data is None:
            continue

        image = part.as_image()
        out_path = OUTPUTS / f"nano-banana-test-{stamp}-{index}.png"
        image.save(out_path)
        saved += 1
        print(f"Saved {out_path}")

    if saved == 0:
        print("No image was returned. Check model access, billing, quota, and safety output.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
