from re import search
from typer import secho

# Open the words file, read the contents, and filter out words
# that are not 5 letters long.
def read_words():
    with open("words.txt") as f:
        words = f.read().splitlines()
    return [word for word in words if len(word) == 5]

VALID_WORDS = read_words()

def main():
    while True:
        inpt = input("> ")
        pattern = inpt.lower()

        matches = [word for word in VALID_WORDS if search(pattern, word) is not None]
        if matches:
            secho(f"Found {len(matches)} matches:", fg="green")
            for match in matches:
                secho(match)
        else:
            secho("No matches found", fg="red")

if __name__ == "__main__":
    main()
