from DP_function import maxpoint

# Inputs: transactions
transactions = {
"T01": {"date": "2021-05-01", "merchant_code" : "sportcheck", "amount_cents": 21000},
"T02": {"date": "2021-05-02", "merchant_code" : "sportcheck", "amount_cents": 8700},
"T03": {"date": "2021-05-03", "merchant_code" : "tim_hortons", "amount_cents": 323},
"T04": {"date": "2021-05-04", "merchant_code" : "tim_hortons", "amount_cents": 1267},
"T05": {"date": "2021-05-05", "merchant_code" : "tim_hortons", "amount_cents": 2116},
"T06": {"date": "2021-05-06", "merchant_code" : "tim_hortons", "amount_cents": 2211},
"T07": {"date": "2021-05-07", "merchant_code" : "subway", "amount_cents": 1853},
"T08": {"date": "2021-05-08", "merchant_code" : "subway", "amount_cents": 2153},
"T09": {"date": "2021-05-09", "merchant_code" : "sportcheck", "amount_cents": 7326},
"T10": {"date": "2021-05-10", "merchant_code" : "tim_hortons", "amount_cents": 1321}
}

# Calculate points for a single transaction
max_single_points = 0
for key in transactions:
    Spo_single_trans = 0  # transactions
    Tim_single_trans = 0
    Sub_single_trans = 0
    if transactions[key]["merchant_code"] == "sportcheck":
        Spo_single_trans += transactions[key]["amount_cents"]
    elif transactions[key]["merchant_code"] == "tim_hortons":
        Tim_single_trans += transactions[key]["amount_cents"]
    else:
        Sub_single_trans += transactions[key]["amount_cents"]
    max_single_points = max(max_single_points, maxpoint(Spo_single_trans // 100, Tim_single_trans // 100, Sub_single_trans // 100))
print("The max points for a single transaction: ", max_single_points)


# Calculate points for all transaction
Spo_amount_cents = 0
Tim_amount_cents = 0
Sub_amount_cents = 0
for key in transactions:  # Accumulate the amount cents of three parts
    if transactions[key]["merchant_code"] == "sportcheck":
        Spo_amount_cents += transactions[key]["amount_cents"]
    elif transactions[key]["merchant_code"] == "tim_hortons":
        Tim_amount_cents += transactions[key]["amount_cents"]
    else:
        Sub_amount_cents += transactions[key]["amount_cents"]
print("The max points for all transaction: ", maxpoint(Spo_amount_cents // 100, Tim_amount_cents // 100, Sub_amount_cents // 100))

