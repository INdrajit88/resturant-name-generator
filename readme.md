# Restaurant Name Generator

A simple Streamlit app that generates a restaurant name and menu items based on a selected or custom cuisine type.

## Features

- Choose from predefined cuisines or enter your own.
- Generates a restaurant name and sample menu items using AI (via `langchain_helper`).

## Requirements

- Python 3.8+
- Streamlit
- langchain (and any dependencies required by `langchain_helper.py`)

## Installation

1. Clone this repository.
2. Install dependencies:(Add any other dependencies your `langchain_helper.py` needs.)

## Usage

Run the app with:Or, if you have issues with the command, use:## Project Structure

- `main.py` - Streamlit app code.
- `langchain_helper.py` - Helper functions for generating names and menu items.

## How it works internally

The app uses Streamlit to create a web interface where users can select or enter a cuisine type. When the "Generate Restaurant Details" button is clicked, it calls the `generate_name_and_items` function from `langchain_helper.py` to generate a restaurant name and menu items based on the chosen cuisine. The results are then displayed on the page.
