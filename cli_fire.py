#!/usr/bin/env python

import fire
from mylib.logic import wiki, search_wiki, phrase

cli_wiki = wiki
cli_search = search_wiki
cli_phrase = phrase

if __name__ == "__main__":
    fire.Fire()
