# -*- coding: utf-8 -*-

def h1_handler(header):
    parent_el = header.parent
    while True:
        if len(parent_el.text) > 1000:  # Add factors stoping //
            break
        else:
            parent_el = parent_el.parent
    return parent_el
