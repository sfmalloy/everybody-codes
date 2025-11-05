# Everybody Codes 2025 Solutions

These are my solutions to Everybody Codes 2025. It uses a library based on [my Advent of Code solutions from 2024](https://github.com/sfmalloy/advent-of-code/tree/main/2024).

## Running

### Initial Setup
First install dependencies and setup the project using [uv](https://docs.astral.sh/uv/).
```bash
uv sync
```

Then setup your `.env` file with the `everybody-codes` session token (named `EC_SESSION`) if you would like to have automatically downloaded inputs. Also populate the year you want to run (for this repo `EC_EVENT` should be `2025`).

### Running Solutions
```bash
uv run src/main.py -q <QUEST> -p <PART>
```
Both "QUEST" and "PART" are required...(for now until I implement multi-part running)
