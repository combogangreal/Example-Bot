from os.path import isfile
from sqlite3 import connect
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from typing import Any, List

DB_PATH = "./bot/data/database.db"
BUILD_PATH = "./bot/data/build.sql"
cxn = connect(DB_PATH, check_same_thread=False)
cur = cxn.cursor()


def commit():
    cxn.commit()


def with_commit(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        commit()

    return inner


class Database:
    def __init__(self) -> None:
        pass

    @with_commit
    def build(self):
        """Builds the sqlite3 database from the ./data/build.sql file."""
        if isfile(BUILD_PATH):
            self.scriptexec(BUILD_PATH)

    def autosave(self, sched: AsyncIOScheduler):
        """Schedules the database to commit any data to the database every minute.

        Args:
            sched (AsyncIOScheduler): The scheduler that is in charge
        """
        sched.add_job(commit, CronTrigger(second=0))

    def close(self):
        """Closes the connection to the database."""
        cxn.close()

    def field(self, command: str, *values: Any):
        """Executes a command with the given values and returns the first field.

        Args:
            command (str): The command to execute
            *values (Any): The values to insert into the command
        """
        cur.execute(command, tuple(values))

        if (fetch := cur.fetchone()) is not None:
            return fetch[0]

    def record(self, command: str, *values: Any):
        """Executes a command with the given values and returns the first record.

        Args:
            command (str): The command to execute
            *values (Any): The values to insert into the command
        """
        cur.execute(command, tuple(values))

        return cur.fetchone()

    def records(command: str, *values: Any):
        """Executes a command with the given values and returns all records.

        Args:
            command (str): The command to execute
            *values (Any): The values to insert into the command
        """
        cur.execute(command, tuple(values))

        return cur.fetchall()

    def column(command: str, *values: Any):
        """Executes a command with the given values and returns the first column.

        Args:
            command (str): The command to execute
            *values (Any): The values to insert into the command
        """
        cur.execute(command, tuple(values))

        return [item[0] for item in cur.fetchall()]

    def execute(self, command: str, *values: Any):
        """Executes a command with the given values.

        Args:
            command (str): The command to execute
            *values (Any): The values to insert into the command
        """
        cur.execute(command, tuple(values))

    def multiexec(self, command: str, valueset: List[Any]):
        """Executes multiple commands with the given values.

        Args:
            command (str): The command to execute
            valueset (List[Any]): The values to insert into the command
        """
        cur.executemany(command, valueset)

    def scriptexec(self, path: str):
        """Executes a script from the given path.

        Args:
            path (str): The path to the script
        """
        with open(path, "r", encoding="utf-8") as script:
            cur.executescript(script.read())
