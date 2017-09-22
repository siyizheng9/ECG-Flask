
import os

COLLECTION = 'kafkatopic'


def getPath(name):
    '''return path to the named file
    name -- string, file name withou suffix
    '''
    path = os.path.join(os.path.dirname(__file__), 'data')
    return os.path.join(path, name)


def download_data(db, client_id):
    '''download data from db and save it to .csv file
    db -- mongo.db connection
    client_id -- string, client_id to retrive data
    '''
    print("dowloading", client_id)
    collection = db[COLLECTION]
    msglist = collection.find({'client_id': client_id})
    msglen = msglist.count()
    print("msg count:", msglen)

    data = []
    iterator = iter(msglist)
    for i in range(20 if 20 < msglen else msglen):
        obj = next(iterator)
        data.append(obj['mMessage'])
    # print(data)
    write_to_file(data, COLLECTION + '_' + client_id)
    return data


def write_to_file(data, filename):
    ''' write data to csv file
    data -- list, mMessage list
    filename -- string, target file name, default to save as csv file
    '''
    file = open(getPath(filename) + '.csv', 'w')
    for item in data:
        file.write(item)
        file.write("\n")
    file.close
