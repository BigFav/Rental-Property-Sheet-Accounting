import csv
from argparse import ArgumentParser
from enum import Enum

MAIN_FILENAME = "test.csv"


class KNOWN_ADDRESSES(Enum):
    _17_S_15TH_ST = "17 S 15TH ST"
    _513_S_SHIPPEN_ST = "513 S SHIPPEN ST"
    _36_S_13TH_ST = "36 S 13TH ST"
    _131_N_13TH_ST = "131 N 13TH ST"
    _235_MACLAY_ST = "235 MACLAY ST"
    _1011_WALNUT_ST = "1011 WALNUT ST"


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
    CARRYOVER = 10


class SOURCE(Enum):
    CASH_APP = 1
    APP_FOLIO = 2
    WELLS_BANK = 3
    BLUEVINE_BANK = 4
    CITI_CREDIT_CARD = 5
    CARRYOVER = 6
    EMAIL = 7


class TAX_DEMARCATION(Enum):
    REPAIR = 1
    IMPROVEMENT = 2


class Transaction:
    def __init__(self, args):
        self.date = args.date
        self.category = args.category
        self.address = args.address.upper()
        self.unit = args.unit
        self.dollar_amount = "${:.2f}".format(args.dollar).replace("$-", "-$")
        self.source = args.source
        self.tax_demarcation = args.tax
        if args.notes:
            self.notes = args.notes
        elif args.category in ("RENT", "MANAGEMENT", "MORTGAGE", "CARRYOVER"):
            self.notes = self.category
        else:
            raise TypeError(f"Notes are required for nontrivial category: {args.category}")


# Looking to have rows with the following columns:
# Date,Category,Address,Unit,DollarAmount,Notes,Source,TaxDemarcation

# The input reader should convert the input into a "request" object, with appropriate defaults.
# From there various helpers can simply operate on that object.


def add_transaction(transactionRow):
    transactionRowDict = transactionRow.__dict__
    with open(MAIN_FILENAME, "a+") as csvfile:
        csvwriter = csv.DictWriter(
            csvfile,
            fieldnames=[
                "date",
                "category",
                "address",
                "unit",
                "dollar_amount",
                "notes",
                "source",
                "tax_demarcation",
            ],
            delimiter=",",
        )
        csvwriter.writerow(transactionRowDict)


parser = ArgumentParser(description="Process transaction information, and persist it.")
parser.add_argument(
    "-d",
    "--date",
    type=str,
    required=True,
    help="The date of the transaction. Format month/day/year.",
)
parser.add_argument(
    "-c",
    "--category",
    required=True,
    choices=CATEGORY.__members__,
    help="Category to bucket the transaction.",
)
parser.add_argument(
    "-a",
    "--address",
    required=False,
    choices=[e.value for e in KNOWN_ADDRESSES],
    default="",
    type=str,
    help="Address of the property.",
)
parser.add_argument(
    "-u",
    "--unit",
    required=False,
    default="",
    type=str,
    help="The specific unit relevant to the transaction.",
)
parser.add_argument(
    "-da",
    "--dollar",
    "--dollars",
    "-am",
    "--amount",
    required=True,
    type=float,
    help="The dollar amount associated with the transaction.",
)
parser.add_argument(
    "-n",
    "--notes",
    "--description",
    required=False,
    type=str,
    help="A note describing the transaction.",
)
parser.add_argument(
    "-s",
    "--source",
    required=True,
    choices=SOURCE.__members__,
    help="Where this transaction can be found.",
)
parser.add_argument(
    "-t",
    "--tax",
    required=False,
    choices=TAX_DEMARCATION.__members__,
    default="",
    help="For expenses only. Is this transaction an improvement or repair? A capital improvement "
    "would include major work such as refurbishing the kitchen converting a room or attaching "
    "a conservatory. A repair on the other hand is general maintenance, for example, "
    "repairing a tap, repainting surfaces, fixing the air conditioning, or maintenance on "
    "appliances.",
)
parser.add_argument(
    "--add",
    action="store_true",
    default=False,
    help="When present, will add the transaction defined by the other arguments.",
)
args = parser.parse_args()
row = Transaction(args)

if args.add:
    add_transaction(row)
