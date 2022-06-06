"""Dictionary related utility functions."""

__author__ = "730479442"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(he: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    em = {}
    for x in he:
        if N > len(he[x]):
            N = len(he[x])
        y = []
        for z in range(0, N):
            y.append(he[x][z])
        em[x] = y
    return em


def select(sel: dict[str, list[str]], li: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    em = {}
    for x in li:
        em[x] = sel[x]
    return em


def count(items: list[str]) -> dict[str, int]:
    """Return a dict with the items and how often they appear."""
    items.sort()
    blank = {}
    for x in items:
        blank[x] = 0
    for x in items:
        if x in blank:
            blank[x] += 1
    return blank