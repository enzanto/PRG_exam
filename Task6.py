# The task is uploaded to https://github.com/enzanto/PRG_exam in case indentation or other errors occurs when uploading to Noroff


customer = {"name": "jane doe", "address": "14 main road"}
# putting items in a list future proofs it for cases with more than one item
items = [{"description": "jumping castle", "amount": 2, "cost": 2000}]
invoice_no = 12345
width = 50
divider = "-" * width
invoice_total = 0

for item in items:
    invoice_total += item["amount"] * item["cost"]


print("invoice".upper().center(width))
print()
print(
    f"{customer['name']}".ljust(30),
    "invoice no:".upper().ljust(11),
    str(invoice_no).rjust(9),
    sep="",
)
print(
    f"{customer['address']}".ljust(30),
    "amount due:".upper().ljust(11),
    f"{invoice_total:.2f}".rjust(9),
    sep="",
)
print()
print(
    "description".upper().ljust(17),
    "items".upper().center(16),
    "cost".upper().ljust(10),
    "total".upper().ljust(7),
    sep="",
)
print(divider)
for item in items:  # Using a for loop to iterate over all the items.
    print(
        item["description"].title().ljust(17),
        str(item["amount"]).center(16),
        f"{item['cost']:.2f}".ljust(10),
        f"{item['amount'] * item['cost']:.2f}".ljust(7),
        sep="",
    )
print(divider)
print("total".title().ljust(25), f"{invoice_total:.2f}".rjust(25), sep="")
print(divider)
