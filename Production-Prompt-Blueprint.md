# Production Prompt Blueprint

Этот файл задает финальную структуру production-ready prompt.

Используй его как внутренний конструктор, не обязательно показывай блоки пользователю.

## Text-to-image blueprint

Create an image of [subject] [action] in [location/context].
Composition: [shot type, angle, framing, foreground/midground/background if needed].
Style: [photo / 3D render / illustration / poster / diagram / cinematic / editorial].
Lighting: [specific light setup and mood].
Materials and texture: [visible physical details].
Color palette: [main colors and grading].
Aspect ratio: [ratio/platform].
Constraints: [only relevant constraints].

## Image editing blueprint

Using the provided image, change only [target element] to [new result].
Keep [unchanged elements] exactly the same: [face/product/pose/background/lighting/composition].
Match the original [perspective, lighting, shadows, texture, color grade].
Constraints: [do not alter identity/product/logo/anatomy/text].

## Reference composition blueprint

Use Image A as [role].
Use Image B as [role].
Use Image C as [role].
Create [new final scene].
Preserve [critical details from each reference].
Blend the elements with consistent perspective, lighting, scale, shadows, and material texture.
Constraints: [no redesign, no identity drift, no random text].

## Text rendering blueprint

Create [poster/mockup/diagram/card] with the exact text "[TEXT]".
Typography: [font style, weight, color, placement].
Hierarchy: [headline/subtitle/caption].
Layout: [grid/composition/spacing].
Constraints: no extra letters, no misspelled words, no random text, clean readable typography.

## Diagram / infographic blueprint

Create a [diagram/infographic/flowchart] about [topic].
Structure: [number of sections/nodes/steps].
Layout: [left-to-right/top-to-bottom/radial/grid].
Labels: [exact labels if known].
Style: [scientific/editorial/classroom/technical].
Accuracy: [factual constraints].
Constraints: readable labels, clean spacing, no extra nodes, no decorative clutter.

## Cinematic scene blueprint

Create a cinematic image of [subject/action] in [location].
Narrative moment: [what just happened or is about to happen].
Composition: [camera angle, shot size, foreground/midground/background].
Lighting: [source, direction, contrast, atmosphere].
Color: [grading].
Texture: [environment/material/weather].
Camera: [lens/focus only if useful].
Aspect ratio: usually 16:9, 21:9, or 9:16 depending on use.
Constraints: [avoid clutter, keep subject clear, no random text].

## Prompt length control

Short prompt:
Use when the idea is simple and low-risk.

Production prompt:
Use for serious, commercial, cinematic, product, portrait, poster, editing, or reference tasks.

Structured prompt:
Use when there are many requirements, multiple references, exact text, diagrams, or complex edits.

Do not make every prompt huge. Detail should serve control.
