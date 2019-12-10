#!/usr/bin/python3
# -*- coding: Utf-8 -*
from GrandPyApp import views


"""
main page
"""


def start_program():
    views.app.run(debug=True)


if __name__ == "__main__":
    start_program()