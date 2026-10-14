raw_phones = [
    "08031234567",
    "+2348031234567",
    "2348031234567",
    "8031234567",
    "0805 111 2233",
    "07012",
    "abc",
    "",
    "08051112233",
    "0803123456x",
    "12345678901",
]


def normalize_phones(raw):
    raw = raw.replace(" ", "").removeprefix("+")

    if raw.startswith("234"):
        raw = raw.replace("234", "0", 1)

    if len(raw) == 10 and not raw.startswith("0"):
        raw = "0" + raw

    if len(raw) != 11 or not raw.startswith("0") or not raw.isdigit():
        return (None, "Invalid number")

    return (raw, None)


invalid = 0
seen = []
duplicates = 0

for r in raw_phones:
    number, err = normalize_phones(r)

    if err is None:
        if number in seen:
            duplicates += 1
        else:
            seen.append(number)
        print(number)
    else:
        invalid += 1


print(f"{invalid} invalid, {len(seen)} unique, {duplicates} duplicates")
