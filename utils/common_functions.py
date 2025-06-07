import csv
from typing import List, Dict


def read_csv_data(file_path: str) -> List[Dict[str, str]]:
    with open(file_path, newline="", encoding="UTF-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return [row for row in reader]
