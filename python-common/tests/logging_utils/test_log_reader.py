import datetime
from io import StringIO
from pathlib import Path

from common.logging_utils.log_reader import LogFile
from common.logging_utils.log_reader import LogLine

EXAMPLE = "[2020-05-08 22:27:21,863][WARNING][bigband.py:57:__init__]  some message"
EXAMPLE2 = "[2020-05-08 22:27:21,869][WARNING][bigband.py:59:__init__]  another message"


class TestLogLine:
    def test_from_line(self):
        expected = LogLine(
            datetime=datetime.datetime(2020, 5, 8, 22, 27, 21, 863000),
            log_level="WARNING",
            filename="bigband.py",
            line_number=57,
            function="__init__",
            message="some message\n",
            next_log_line=None,
            previous_log_line=None,
        )
        log_line = LogLine.from_line(EXAMPLE)
        assert log_line == expected

    def test_from_line_no_match(self):
        """ Should return None. """
        assert LogLine.from_line("Won't match") is None


class TestLogFile:
    def test_read(self):
        expected_prologue = "some initial stuff\nmore\n\n"

        expected_log_lines = [
            LogLine(
                datetime=datetime.datetime(2020, 5, 8, 22, 27, 21, 863000),
                log_level="WARNING",
                filename="bigband.py",
                line_number=57,
                function="__init__",
                message="some message\nafter1\nafter2\n",
            ),
            LogLine(
                datetime=datetime.datetime(2020, 5, 8, 22, 27, 21, 869000),
                log_level="WARNING",
                filename="bigband.py",
                line_number=59,
                function="__init__",
                message="another message\n",
            ),
        ]
        expected_log_lines[1].previous_log_line = expected_log_lines[0]
        expected_log_lines[0].next_log_line = expected_log_lines[1]

        filecontents = StringIO(
            f"some initial stuff\nmore\n\n{EXAMPLE}\nafter1\nafter2\n{EXAMPLE2}"
        )
        prologue, log_lines = LogFile.read(filecontents)
        assert prologue == expected_prologue
        assert log_lines == expected_log_lines


class TestReadLogFile:
    """ Test to read entire log file. """
    _DIR = Path(__file__).resolve().parent / "datafiles"
    LOG_FILE = _DIR / "big-bang-1031.log"

    def test_basic(self):
        log_file = LogFile(self.LOG_FILE)
        assert log_file.prologue == 'prologue stuff\n'
        assert len(log_file.log_lines) == 21
