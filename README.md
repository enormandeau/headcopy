# headcopy

Learn head copying morse code and help instant character recognition

Uses `cw` program to sound the morse

## Usage

Launch with `./headcopy <DELAY> <SPEED>` or add your headcopy directory to your
"$PATH" variable and launch with `headcopy <DELAY> <SPEED>`.

## Parameters

- `DELAY` acts as a Farnsworth factor. At zero, you are using full speed (20
wpm by default).

- `SPEED` is the number of words per minute (wpm)

For example, at `SPEED=20` and `DELAY=26`, you are using an effective speed of
10 wpm.
