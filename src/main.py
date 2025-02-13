from pathlib import Path


def print_field(content: str, field_numbers: list, delimiter: str) -> str:
    lines = content.splitlines()
    field_output = []

    for line in lines:
        characters = line.split(delimiter)
        selected_fields = []

        for number in field_numbers:
            if number <= len(characters):
                selected_fields.append(characters[number - 1])

        field_output.append(delimiter.join(selected_fields))

    return "\n".join(field_output)


def _cli():
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file", nargs="?", default="-", help="Input file (or - for stdin)"
    )
    parser.add_argument(
        "-f", "--field", type=str, nargs="+", default="1", help="Fields to extract"
    )
    parser.add_argument(
        "-d", "--delimiter", type=str, default="\t", help="Field delimiter"
    )

    args = parser.parse_args()
    delimiter = args.delimiter.encode(encoding="utf-8").decode("unicode_escape")

    if isinstance(args.file, Path):
        content = args.file.read_text(encoding="utf-8")
    else:
        content = sys.stdin.read()

    fields = []
    for item in args.field:
        fields.extend(map(int, item.split(",")))

    print(print_field(content, fields, delimiter))


if __name__ == "__main__":
    _cli()
