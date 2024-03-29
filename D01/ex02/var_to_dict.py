#!/usr/bin/python3

def my_dictionary():

    d = [
    ('Hendrix' , '1942'),
    ('Allman' , '1946'),
    ('King' , '1925'),
    ('Clapton' , '1945'),
    ('Johnson' , '1911'),
    ('Berry' , '1926'),
    ('Vaughan' , '1954'),
    ('Cooder' , '1947'),
    ('Page' , '1944'),
    ('Richards' , '1943'),
    ('Hammett' , '1962'),
    ('Cobain' , '1967'),
    ('Garcia' , '1942'),
    ('Beck' , '1944'),
    ('Santana' , '1947'),
    ('Ramone' , '1948'),
    ('White' , '1975'),
    ('Frusciante', '1970'),
    ('Thompson' , '1949'),
    ('Burton' , '1939')
    ]

    resultDictionary = dict()
    for value, key in d:
        if key_exists(key, resultDictionary) == True:
            resultDictionary[key] += " " + value
        else:
            resultDictionary[key] = value
    print('\n'.join("{} : {}".format(value, key) for value, key in resultDictionary.items()))

def key_exists(key, d):

    keys = d.keys()

    if len(d) == 0:
        return False
    for elements in keys:
        if elements == key:
            return True

if __name__ == '__main__':
    my_dictionary()