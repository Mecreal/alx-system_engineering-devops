
# 0x16. API advanced

## Description
This project focuses on working with the Reddit API to perform various tasks such as retrieving subscriber counts, listing hot posts, and analyzing post titles. It aims to improve skills in API interaction, JSON parsing, and recursive API calls.

## Project Information
- **Language:** Python
- **OS:** Ubuntu 20.04 LTS
- **Style:** PEP 8

## Learning Objectives
By the end of this project, you should be able to:
- Read API documentation to find the required endpoints
- Use an API with pagination
- Parse JSON results from an API
- Make recursive API calls
- Sort a dictionary by value

## Requirements
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Libraries imported in Python files must be organized in alphabetical order
- A `README.md` file at the root of the project folder is mandatory
- Code should use the PEP 8 style
- All files must be executable
- File length will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- You must use the Requests module for sending HTTP requests to the Reddit API
- You are not allowed to import any other module

## Tasks

### 0. How many subs?
Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit.

### 1. Top Ten
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

### 2. Recurse it!
Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

### 3. Count it! (Advanced)
Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.

## Author
Hamza Abouabid

## License
This project is licensed under the terms of the MIT license.