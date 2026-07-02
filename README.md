# MMORPG for micro:bit

Playing with [BBC micro:bit](https://microbit.org/) microcontroller.
Aspiring to build a multi-player game that uses radio to communicate between devices.

# vscode workflow

1. Install `microbit-stubs` Python package to enable syntax support in VSCode.

2. Flash [official MicroPython](https://github.com/microbit-foundation/micropython-microbit-v2/releases) with microbit support to microbit by copying the .hex file.

3. Install `mpremote` and use it to interactively run scripts from RAM on the microbit (saves flash write cycles) and copy programs (without changing the micropython runtime).


```bash
# run script in RAM
mpremote run eat_the_dot.py
# script to be main executable
mpremote fs cp eat_the_dot.py :main.py
```
