
import os

path = os.path.join(os.path.dirname(__file__), 'data')


def getPath(name):
    return os.path.join(path, name + '.csv')


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
    write_to_file(data, collection_name)
    return data


def write_to_file(data, collection_name):
    file = open(getPath(collection_name), 'w')
    for item in data:
        file.write(item)
        file.write("\n")
    file.close
