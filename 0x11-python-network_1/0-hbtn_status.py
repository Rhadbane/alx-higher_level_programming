#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status using urllib.

This module demonstrates how to make a GET request to a URL using
the urllib package and display the response details.
"""

import urllib.request


def fetch_status():
    """
    Fetch the status from https://alx-intranet.hbtn.io/status
    and display the response details.
    """
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))


if __name__ == "__main__":
    fetch_status()
