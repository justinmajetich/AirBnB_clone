#!/usr/bin/python3

import re
import sys

def preloop(self):
    """Prints if isatty is false"""
    if not sys.__stdin__.isatty():
        print('{} '.format(self.prompt))


def precmd(self, line):

    no_formating_chars = not any([x in line for x in ["(", ")", "."]])
    if no_formating_chars:
        return line.split(" ")

    search_exprs = {
        "class_name": "^{}".format(
            make_regex_list(self.record_classes)
        ),
        "dot_commands": "(?=.){}".format(
            make_regex_list(self.dot_commands)
        ),
        "parenthetical_args": "(?<=\()(.*?)(?=\))",
        "extract_quote": "(?<=('|\"))(.*?)(?=('|\"))",
        "extract_args": ""
    }
    parsed_line = {
        "class": re.search(search_exprs["class_name"], line),
        "dot_command": re.search(search_exprs["dot_commands"], line),
        "args": re.search(search_exprs["parenthetical_args"], line),
        "id": re.search(search_exprs["extract_quote"], line)
    }

    if parsed_line["dot_command"] not in self.dot_commands:
        raise Exception

    parsed_args = [x.group() for x in parsed_line.values() if x]

    return parsed_args


def postcmd(self, stop, line):
    """Prints if isatty is false"""
    if not sys.__stdin__.isatty():
        print(
            '{} '.format(self.prompt),
            end=''
        )
    return stop


def convert_to_hardcode(a_list, formating, enclosure, adjust):
    """FUNCTION TO CONVERT A LIST INTO A HARDCODE STRING """
    return enclosure("".join([formating(x) for x in a_list])[:adjust * -1])


def make_regex_list(a_list):
    """SPECIFIC USE CASE OF 'convert_to_hardcode' TO DYNMICALLY GENERATE REGEX """
    return convert_to_hardcode(a_list, (lambda x: f"{x}|"), (lambda y: f"({y})"), adjust=1)