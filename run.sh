#!/bin/bash
MAIN_FILENAME="test.csv"
BACKUP_FILENAME="backup.csv"
cp $MAIN_FILENAME $BACKUP_FILENAME

# Insert inputs here.
python3 main.py -a "131 N 13TH ST" -u "1" -da 552 -d "1/31/2023" -c "RENT" -s "APP_FOLIO" --add
