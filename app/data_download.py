
def download_data(db, collection_name):
    print("dowloading", collection_name)
    collection = db[collection_name]
    print("record count:", collection.count())

    data = []
    iterator = iter(collection.find())
    for i in range(20):
        obj = next(iterator)
        data.append(obj['mMessage'])
    print(data)
    return data
