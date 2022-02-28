# Wordlefind - A tool for playing Wordle

`wordlefind` is a CLI tool that allows you to search up 5-letter words based on the Regex
pattern that you give to it. It is intended for helping you play Wordle (when you are stuck).

# Quick Start

0. Make sure you have `python`, `pip` and [`pipenv`](https://pipenv.pypa.io/en/latest/) installed
1. Clone this repo and go to the repo directory
2. Enable virtual environment using `pipenv`

```
pipenv shell
```

3. Install all the dependencies required:

```
pipenv install
```

4. Finally, run `main.py`:

```
pipenv run python3 main.py
```

You should, by now, have a prompt in the terminal. Press <kbd>Enter</kbd> and you should see the whole library of 5-letter words in the terminal. That means the program is working!

# Credits

This project uses [this English dictionary](https://github.com/dwyl/english-words/) for finding words. They contain words that doesn't exist in the [Wordle game](https://wordlegame.org) that I regularly played, so, pay attention!

Thanks to [`typer`](https://typer.tiangolo.com) for the cool text coloring and formatting, though using it is a bit overkill.

# License

MIT
