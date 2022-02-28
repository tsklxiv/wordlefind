from re import search
from typer import secho
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

# Open the words file, read the contents, and filter out words
# that are not 5 letters long.
def read_words():
    with open("words.txt") as f:
        words = f.read().splitlines()
    return [word for word in words if len(word) == 5]

VALID_WORDS = read_words()

session = PromptSession(
    auto_suggest=AutoSuggestFromHistory(),
    enable_history_search=True,
)

def main():
    while True:
        inpt = session.prompt("> ")
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
