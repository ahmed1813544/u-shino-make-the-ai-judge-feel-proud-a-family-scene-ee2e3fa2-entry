"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (one or two lines, <= 280 characters)
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Stdlib only. No network, no file reads outside this repository.
Deterministic: every run writes byte-identical output.
"""

import os

SCENE = (
    "My six-year-old charges Dad one biscuit per bedtime story. "
    "Last night he paid up, then fell asleep halfway through \u2014 "
    "so she tucked him in and whispered, \u201cShh, the storyteller "
    "needs his rest.\u201d"
)


def main() -> None:
    # The gate allows 1 to 280 characters, not only whitespace, in
    # one or two lines. Refuse to write anything that would fail it.
    if not (1 <= len(SCENE) <= 280) or not SCENE.strip():
        raise ValueError("scene does not meet the 1-280 character gate")
    if SCENE.count("\n") > 1:
        raise ValueError("scene must be one or two lines")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SCENE)


if __name__ == "__main__":
    main()
