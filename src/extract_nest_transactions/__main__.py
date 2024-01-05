from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from datetime import datetime

from bs4 import BeautifulSoup


def main(args: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("html_file", nargs="+", type=Path)
    parsed_args = parser.parse_args(args)
    html_paths: list[Path] = parsed_args.html_file
    rows = []

    for html_path in html_paths:
        soup = BeautifulSoup(html_path.read_text(), features="html.parser")
        for table in soup.find_all("table", class_="sec_table_wrapper"):
            info_table = table.find("table", class_="info_table")
            date = info_table.tbody.find_all("tr")[1].find("label").string
            date = datetime.strptime(date, "%d %B %Y").strftime("%Y-%m-%d")

            info_row = table.find("tr", class_="table3_body")
            data = [element.string for element in info_row.find_all("td")]
            assert len(data) == 4
            fund_name, number_unit, unit_price, cash_value = (
                data[0],
                # Replace decimal point with comma because my other app is German.
                str(float(data[1])).replace(".", ","),
                str(float(data[2])).replace(".", ","),
                str(float(data[3])).replace(".", ","),
            )

            rows.append((date, fund_name, number_unit, unit_price, cash_value))

    # Sort by date
    rows.sort(key=lambda row: row[0])

    writer = csv.writer(sys.stdout)
    writer.writerow(("date", "fund_name", "number_unit", "unit_price", "cash_value"))
    writer.writerows(rows)


if __name__ == "__main__":
    main()
