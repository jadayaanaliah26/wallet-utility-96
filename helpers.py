import re
def validate_wallet_address(address):
    if not isinstance(address, str):
        return False
    if not address.startswith("0x"):
        return False
    if len(address) != 42:
        return False
    if not re.match(r"^0x[0-9a-fA-F]{40}$", address):
        return False
    return True

def validate_amount(amount):
    if not isinstance(amount, (int, float)):
        return False
    if amount <= 0:
        return False
    return True

def process_wallet_data(data_list):
    processed = []
    for item in data_list:
        if not isinstance(item, dict):
            processed.append({"status": "invalid", "reason": "not dict"})
            continue
        address = item.get("address")
        amount = item.get("amount")
        if not validate_wallet_address(address):
            processed.append({"status": "invalid", "address": address, "reason": "bad address"})
            continue
        if not validate_amount(amount):
            processed.append({"status": "invalid", "address": address, "reason": "bad amount"})
            continue
        processed.append({"status": "success", "address": address, "amount": amount})
    return processed

if __name__ == "__main__":
    test_data = [
        {"address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e", "amount": 1.5},
        {"address": "0xinvalidaddress", "amount": 100},
        {"address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e", "amount": 0},
        {"address": "0x1234567890123456789012345678901234567890", "amount": 250},
        "not a dict",
        {"address": "0xabcdefabcdefabcdefabcdefabcdefabcdefabcd", "amount": -5}
    ]
    results = process_wallet_data(test_data)
    for result in results:
        print(result)
