"""
Package with which to calculate capacity scenarios.

Author: Maarten Fabré <maartenfabre@gmail.com>

License: MIT
"""
from sortedcontainers import SortedDict
import bisect


class Scenario:
    """
    defines a scenario


    """

    def __init__(self, capacities_mapping=None, **capacities):
        if capacities_mapping and capacities:
            raise ValueError(
                "define only capacities_mapping or capacities, not both"
            )
        capacities = capacities_mapping if capacities_mapping else capacities
        self._items = SortedDict(capacities)

    def __setitem__(self, key, value):
        self._items[key] = value

    def __getitem__(self, key):
        try:
            return self._items[key]
        except KeyError as exc:
            keys = list(self._items.keys())
            idx = bisect.bisect_left(keys, key) - 1
            if idx == -1:
                raise KeyError from exc
            found_key = keys[idx]
            return self._items[found_key]

    def __iter__(self):
        return iter(self._items.items())
