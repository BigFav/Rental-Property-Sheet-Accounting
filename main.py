import csv
from argparse import ArgumentParser
from enum import Enum


class CATEGORY(Enum):
    RENT = 1
    UTILITIES = 2
    MANAGEMENT = 3
    MORTGAGE = 4
    MAINTENANCE = 5
    SECURITY_DEPOSIT = 6
    REPAIR_IMPROVEMENT = 7
    GOVERNMENT_FEE = 8
    TAXES = 8
    INSURANCE = 9


class SOURCE(Enum):
    CASH_APP = 1
    APP_FOLIO = 2
    WELLS_BANK = 3
    BLUEVINE_BANK = 4
    CITI_CREDIT_CARD = 5


class TAX_DEMARCATION(Enum):
    REPAIR = 1
    IMPROVEMENT = 2


FILENAME = "test.csv"

# Looking to have rows with the following columns:
# Date,Category,Address,Unit#,DollarAmount,Notes,Source,TaxDemarcation

# The input reader should convert the input into a "request" object, with
# appropriate defaults. From there various helpers can simply operate on that
# object.


def add_transaction():
    with open(FILENAME, "w") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")


parser = ArgumentParser(description="Process transaction information, and persist it.")
parser.add_argument(
    "--add",
    type=bool,
    help="When present, will add the transaction defined by the other arguments.",
)
parser.add_argument(
    "-d", "--date", type=str, help="The date of the transaction. Format month/day/year."
)
parser.add_argument("-c", "--category", type=CATEGORY, help="Category to bucket the transaction.")
parser.add_argument("-a", "--address", type=str, help="Address of the property.")
parser.add_argument(
    "-u", "--unit", type=str, help="The specific unit relevant to the transaction."
)
parser.add_argument(
    "-da", "--dollar", "--dollars", "-am", "--amount", type=float, help="Address of the property."
)
parser.add_argument(
    "-n", "--notes", "--description", type=str, help="A note describing the transaction."
)
parser.add_argument("-s", "--source", type=SOURCE, help="Where this transaction can be found.")
parser.add_argument(
    "-t",
    "--tax",
    type=TAX_DEMARCATION,
    help="For expenses only. Is this transaction an improvement or repair? A capital improvement "
    "would include major work such as refurbishing the kitchen converting a room or attaching "
    "a conservatory. A repair on the other hand is general maintenance, for example, "
    "repairing a tap, repainting surfaces, fixing the air conditioning, or maintenance on "
    "appliances.",
)
args = parser.parse_args()
