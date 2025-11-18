# Series Printer

A simple Python program that generates a series of numbers starting from 100 and decreasing with a dynamic difference. The program takes an integer input and generates a series of numbers where the initial value is 100, and each subsequent number is reduced by an incrementing difference.

## How It Works

1. The program starts with a value of 100.
2. It appends this value to the result list.
3. Then, the value is decreased by an incrementing difference, starting from 1.
4. The program continues this process until the value is no longer greater than the provided integer `n`.
5. The series of numbers are returned as a comma-separated string.

## Requirements

- Python 3.x
- No external libraries are required for this script.

## Usage

To run this script, pass an integer `n` as a command-line argument. The script will generate the series of numbers starting from 100, decreasing with an increasing difference, until the number is no longer greater than `n`.
