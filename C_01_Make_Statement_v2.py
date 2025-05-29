# Functions go here
import decoration as decoration


def make_statement(statement, decoration, lines):
    """Create headings (3 lines), subheadings (2 lines) and emphasis text / mini-headings (1 lne), Only use
    emoji for single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# Main Routine goes here
make_statement("Programming is Fun!!!", "✔", 3)
make_statement("Still Fun!!!", "🤰", 2)
make_statement("Bodhi is Freaky!!!", "😱", 1)
