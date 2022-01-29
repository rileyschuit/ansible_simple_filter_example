#!/usr/bin/python
# https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html#developing-filter-plugins

import json
import os

def filter_unique(things):
  seen = set()
  unique_things = []

  for thing in things:
    if thing not in seen:
      seen.add(thing)
      unique_things.append(thing)

  return unique_things


class FilterModule(object):
    filter_map = {
        'unique_things': filter_unique,
    }

    def filters(self):
        return self.filter_map
