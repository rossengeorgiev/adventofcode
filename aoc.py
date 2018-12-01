import os
import requests

try:
    _input = raw_input
except:
    _input = input


def aoc_web_session():
    session = requests.Session()

    print("This solution automatically fetches your input from https://adventofcode.com")

    if 'AOC_COOKIE' not in os.environ:
        print("Log-in and use the browser dev tools grab the value of the 'session' cookie")
        print("(you can use the AOC_COOKIE environment variable)")

    while True:
        if 'AOC_COOKIE' in os.environ:
            val = os.environ['AOC_COOKIE']
        else:
            val = _input("Enter session cookie: ")

        session.cookies.set('session', val, domain='adventofcode.com', secure=True)

        resp = session.get('https://adventofcode.com/')
        resp.raise_for_status()

        if '[Log Out]' in resp.text:
            break
        else:
            print("Failed to login with cookie")

            if 'AOC_COOKIE' in os.environ:
                raise RuntimeError("Invalid AOC_COOKIE")

    return session
