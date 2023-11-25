'''
MariaDB indicator variables

Indicator values are used in executemany() method of cursor class to
indicate special values.
'''


class MrdbIndicator():
    indicator = 0

    def __init__(self, indicator):
        self.indicator = indicator


NULL = MrdbIndicator(1)
DEFAULT = MrdbIndicator(2)
IGNORE = MrdbIndicator(3)
IGNORE_ROW = MrdbIndicator(4)
