### Hexlet tests and linter status:
[![Actions Status](https://github.com/MysterGoN/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/MysterGoN/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/d6ffd03e47fba288890c/maintainability)](https://codeclimate.com/github/MysterGoN/python-project-49/maintainability)

# Installing and running the app
## Project requirements
- python: 3.11+
- poetry: latest

## Installation
### Installing Poetry
Command:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Setup poetry venv creation in project:
```bash
poetry config virtualenvs.in-project true --local
```
Remove --local for global settings.

Details on installing and using the **Poetry** package are available in [official documentation](https://python-poetry.org/docs/).

### Cloning the repository and installing dependencies
```bash
git clone https://github.com/MysterGoN/python-project-49.git brain-games
cd brain-games
```

Installing dependencies:
```bash
make install
```

### Build and install games
Commands:
```bash
make build
make package-install
```

### Video instruction
[![asciicast](https://asciinema.org/a/0lgcjHROo0dtP3QKia70p1MSA.svg)](https://asciinema.org/a/0lgcjHROo0dtP3QKia70p1MSA)


## Gameplay
### Even
```bash
brain-even
```
[![asciicast](https://asciinema.org/a/c7StrXPNyEcGPh9wNVknynIdI.svg)](https://asciinema.org/a/c7StrXPNyEcGPh9wNVknynIdI)

### Calc
```bash
brain-calc
```
[![asciicast](https://asciinema.org/a/gITqjGs6vkCwKpbUBbZR044po.svg)](https://asciinema.org/a/gITqjGs6vkCwKpbUBbZR044po)

### GCD
```bash
brain-gcd
```
[![asciicast](https://asciinema.org/a/Op7tqeYVf8qUZNutxPM5KwadM.svg)](https://asciinema.org/a/Op7tqeYVf8qUZNutxPM5KwadM)

### Progression
```bash
brain-progression
```
[![asciicast](https://asciinema.org/a/981WKvFLPjHbun0ESEJvcgbsW.svg)](https://asciinema.org/a/981WKvFLPjHbun0ESEJvcgbsW)

### Prime
```bash
brain-prime
```
[![asciicast](https://asciinema.org/a/r9cRCHoedWPJFMM0MBs58zwI3.svg)](https://asciinema.org/a/r9cRCHoedWPJFMM0MBs58zwI3)
