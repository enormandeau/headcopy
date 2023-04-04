# headcopy

Learn head copying morse code and help instant character recognition

Uses `cw` program to sound the morse

## Usage

Launch with `./headcopy <SPEED> <DELAY>` or add your headcopy directory to your
"$PATH" variable and launch with `headcopy <SPEED> <DELAY>`.

## Parameters

- `SPEED` is the number of words per minute (wpm)

- `DELAY` acts as a Farnsworth factor. This is the amount of extra spacing 
   added between characters, in units of 'dot lenghts'. At zero, you are 
   using full speed (20 wpm by default).

For example, at `SPEED=20` and `DELAY=26`, you are using an effective speed of
10 wpm.
