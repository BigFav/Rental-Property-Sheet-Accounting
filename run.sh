#!/bin/bash
MAIN_FILENAME="test.csv"
BACKUP_FILENAME="backup.csv"
cp $MAIN_FILENAME $BACKUP_FILENAME

# args
# -d: The date of the transaction. Format month/day/year.
# -c: Category to bucket the transaction.
# -a: Address of the property.
# -u: The specific unit relevant to the transaction.
# -da: The dollar amount associated with the transaction.
# -n: A note describing the transaction.
# -s: Where this transaction can be found.
# -t: Tax Demarcation
# --add: When present, will add the transaction defined by the other arguments.

# Insert inputs here.
python3 main.py -a "1011 WALNUT ST" -u "1F" -da 800 -d "1/13/2023" -c "RENT" -s "EMAIL" --add
