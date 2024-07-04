0x10-python-network_0

This project consists of various tasks focused on HTTP requests, cURL commands, and web interactions. All Bash scripts are designed to interact with a server set up on a container.
Tasks

cURL Body Size (0-body_size.sh)

Sends a GET request to a given URL
Displays the size of the response body in bytes


cURL to the End (1-body.sh)

Sends a GET request to a given URL
Displays the response body for a 200 status code


cURL Method (2-delete.sh)

Sends a DELETE request to a given URL
Displays the response body


cURL Only Methods (3-methods.sh)

Displays all HTTP methods the server of a given URL will accept


cURL Headers (4-header.sh)

Sends a GET request to a given URL with a custom header
Header: X-HolbertonSchool-User-Id=98
Displays the response body


cURL POST Parameters (5-post_params.sh)

Sends a POST request to a given URL with specific variables
Variables: email=test.gmail.com, subject=I will always be here for PLD
Displays the response body


Find a Peak (6-peak.py, 6-peak.txt)

Python program that finds a peak in a list of unsorted integers
Includes a text file with the algorithm's complexity


Only Status Code (100-status_code.sh)

Sends a GET request to a given URL
Displays only the status code of the response
Does not use pipes, redirections, ;, or &&


cURL a JSON File (101-post_json.sh)

Sends a JSON POST request with contents from a provided file
Displays the response body


Catch Me If You Can! (102-catch_me.sh)

Sends a request to 0.0.0.0:5000/catch_me
Causes the server to respond with "You got me!" in the body



Each script is designed to demonstrate different aspects of HTTP requests and web interactions using cURL and Bash.
