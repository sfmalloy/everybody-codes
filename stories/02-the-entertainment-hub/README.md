# Story 2 Solutions

These are my solutions to Story 2 - [*The Entertainment Hub*](https://everybody.codes/story/2/quests) written in Go.

## Running

This project has a simple command-line interface to run solutions. Below are the various flags accepted.

```bash
  -p uint
        Part of this quest to run
  -q uint
        Quest to run
  -t    Whether to run input using test.txt or not
```

**NOTE**: Inputs must be saved manually to the `inputs` directory. The basic pattern for input filenames are `inputs/quest0#/part0#.txt`

### Running a Single Part of a Quest

```bash
go run main.go -q 1 -p 1
```
### Running ALL Parts of a Quest

```bash
go run main.go -q 1
```

### Running a Quest with the `test.txt` Input

```bash
go run main.go -q 1 -t
```
