# Hangman Game

A simple text-based Hangman game created in Python for the CodeAlpha internship program.

## Table of Contents
- [Overview](#overview)
- [How to Play](#how-to-play)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [About](#about)

## Overview

This is a classic Hangman game implemented in Python. The program randomly selects a word from a predefined list, and the player attempts to guess the word by suggesting letters within a limited number of attempts.

## How to Play

1. The game randomly selects a word from a predefined list
2. You guess letters one at a time to reveal the hidden word
3. You have 6 incorrect guesses before losing the game
4. Win by correctly guessing all letters in the word before running out of attempts

## Features

- Clean console-based interface
- Input validation (only accepts single letters)
- Visual feedback for correct/incorrect guesses
- Tracking of previously guessed letters
- Attempt counter showing remaining guesses
- Simple and intuitive gameplay

## Installation

1. Ensure you have Python 3 installed on your system
2. Clone this repository:
   ```bash
   git clone https://github.com/SanthoshTheodoros/CodeAlpha_HangmanGame.git

3. Navigate to the project directory:
   ```bash
     cd CodeAlpha_HangmanGame

4.Usage
Run the game with the following command:  python hangman.py

## Technologies Used
1. Python 3
2. Random module for word selection

## Project Structure
1. The main game implementation includes:
2. hangman.py - Main game file containing all logic
3. README.md - Project documentation (this file)

4. The code demonstrates:
Random word selection from a predefined list
While loop for main game flow
Conditional statements for input validation
String operations to display word progress
List operations to track guessed letters

## About
This project was completed as part of the CodeAlpha internship program to demonstrate proficiency in basic Python programming concepts.






