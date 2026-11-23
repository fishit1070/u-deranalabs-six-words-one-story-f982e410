"""Six Words, One Story — make.fun entry.

A returning astronaut finds time has outlived him at home:
a complete life, and its loss, in exactly six words.
Writes the story to entry.txt in the output directory.
"""

import os

STORY = "Astronaut came home. Daughter was grandmother."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
