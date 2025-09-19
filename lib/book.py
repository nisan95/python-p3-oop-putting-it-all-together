#!/usr/bin/env python3

class Book:

    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None
        self.page_count = page_count

    # Title property
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = value.strip()

    # Page count property
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

        