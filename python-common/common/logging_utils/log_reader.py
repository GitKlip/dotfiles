
import datetime as datetime_
import re
from dataclasses import dataclass
from typing import List
from typing import Optional


def bracket(pattern):
    return r'\[' + pattern + r'\]'


@dataclass
class LogLine:
    _DATE_RE = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
    _TIME_RE = r'(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2}),(?P<millisecond>\d+)'
    _LOG_TYPE = r'(?P<log_level>\w+)\s*'
    _FILE_FUNCTION = r'(?P<filename>[^:]+):(?P<line_number>[^:]+):(?P<function>[^:]+)'
    _MESSAGE = r'\s*(?P<message>.*)'
    _INT_FIELDS = ['year', 'month', 'day', 'hour', 'minute', 'second', 'millisecond', 'line_number']
    _DATETIME_FIELDS = ['year', 'month', 'day', 'hour', 'minute', 'second']

    LOG_LINE = bracket(_DATE_RE + r'\s+' + _TIME_RE) + bracket(_LOG_TYPE) + bracket(_FILE_FUNCTION) + _MESSAGE

    LOG_LINE_RE = re.compile(LOG_LINE)
    EQUALITY_ATTRIBUTES = ['datetime', 'log_level', 'filename', 'line_number', 'function', 'message']

    datetime: datetime_.datetime
    log_level: Optional[str] = None
    filename: Optional[str] = None
    line_number: Optional[str] = None
    function: Optional[str] = None
    message: Optional[str] = None
    next_log_line: Optional[object] = None
    previous_log_line: Optional[object] = None

    @classmethod
    def from_line(cls, line):
        """ If the line is a log line, will return a Log object, else None. """
        match = cls.LOG_LINE_RE.match(line)
        if not match:
            return None
        data = match.groupdict()
        for field in cls._INT_FIELDS:
            data[field] = int(data[field])

        datetime_kwargs = {field: data[field] for field in cls._DATETIME_FIELDS}
        datetime = datetime_.datetime(**datetime_kwargs, microsecond=data['millisecond'] * 1000)
        return cls(
            datetime=datetime,
            log_level=data['log_level'],
            filename=data['filename'],
            line_number=data['line_number'],
            function=data['function'],
            message=data['message'] + "\n",
        )

    @property
    def seconds_until_next(self):
        if self.next_log_line:
            return (self.next_log_line.datetime - self.datetime).total_seconds()

    @property
    def seconds_since_previous(self):
        if self.previous_log_line:
            return (self.datetime - self.previous_log_line.datetime).total_seconds()

    @property
    def is_error(self):
        """ Returns True if log_level == 'ERROR', else False. """
        return self.log_level == 'ERROR'

    @property
    def is_warning(self):
        """ Returns True if log_level == 'WARNING', else False. """
        return self.log_level == 'WARNING'

    @property
    def is_info(self):
        """ Returns True if log_level == 'INFO', else False. """
        return self.log_level == 'INFO'

    def __eq__(self, other):
        if other is None or not isinstance(other, self.__class__):
            return False
        self_values = [getattr(self, att) for att in self.EQUALITY_ATTRIBUTES]
        other_values = [getattr(other, att) for att in self.EQUALITY_ATTRIBUTES]
        return self_values == other_values

    def __repr__(self):
        data = {att: getattr(self, att) for att in self.EQUALITY_ATTRIBUTES}
        data['message'] = data['message'][0:30] + " ..."
        return f"LogLine({data})"

    __str__ = __repr__


@dataclass
class LogFile:

    filename: str
    log_lines: Optional[List[LogLine]]
    prologue: str = ''
    # log_time_diffs: Optional[List[LogTimeDiff]]

    def __init__(self, filename=None):
        self.filename = filename
        if self.filename:
            with open(self.filename) as infile:
                self.prologue, self.log_lines = self.read(infile)

    @staticmethod
    def read(infile):
        past_first_log_line = False
        prologue = ''
        log_lines = []
        for line in infile:
            log_line = LogLine.from_line(line)
            if log_lines and log_line:
                log_lines[-1].next_log_line = log_line
                log_line.previous_log_line = log_lines[-1]

            if log_line:
                log_lines.append(log_line)
                past_first_log_line = True

            if past_first_log_line:
                if log_line is None:
                    log_lines[-1].message += line
            else:
                prologue += line

        return prologue, log_lines
