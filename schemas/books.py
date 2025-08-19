def bookRecord(item) -> dict:
    return {
        "id": str(item["_id"]),
        "isbn": item["isbn"],
        "author": item["author"],
        "title": item["title"],
        "date": item["date"],
        "pages": item["pages"]
    }

def listOfBookRecords(item_list) -> list:
    record_list = []
    for item in item_list:
        record_list.append(bookRecord(item))
    return record_list
