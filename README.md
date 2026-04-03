# JSONPlaceholder CLI Client

A simple Python command-line application for working with a REST API using the `requests` library.

This project connects to the public [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API and demonstrates how to send `GET` and `POST` requests, handle responses, and display data in a clear CLI format.

## Features

- Get user information by ID
- Get post title by ID
- Create a new post
- Display all users in a numbered list
- Show comment emails for a selected post

## Tech Stack

- Python 3
- Requests
- JSONPlaceholder API

## Installation

Install the required dependency:

```bash
pip install requests
```

## Usage

Run the application:

```bash
python "API project.py"
```

Then choose an option from the menu:

```text
1. Get user
2. Get post
3. Create post
4. Get all users
5. Get comments by post id
6. Exit
```

## Example

```text
4. Get all users
1. Leanne Graham
2. Ervin Howell
3. Clementine Bauch
```

## Project Goal

The main goal of this project is to practice:

- working with external APIs
- using the `requests` library
- handling JSON data
- building a simple interactive CLI application

## Note

JSONPlaceholder is a fake online REST API for testing and learning. Data created with `POST` requests is not permanently saved on the server.
