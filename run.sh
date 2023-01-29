#!/bin/bash
MAIN_FILENAME="test.csv"
BACKUP_FILENAME="backup.csv"
cp $MAIN_FILENAME $BACKUP_FILENAME

# Insert inputs here.
python3 main.py -d '8/24/2022' -c RENT -a "test" -u "1F" -da 12.12 -n "test" -s "CASH_APP" --add
