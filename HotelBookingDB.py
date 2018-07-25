# python HotelBookingDB.py

import pymongo

class HotelBookingDB(object):
    URI = 'mongodb://127.0.0.1:27017'
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(HotelBookingDB.URI)
        HotelBookingDB.DATABASE = client['HotelBookingDB']

    @staticmethod
    def deleteACollection(collection):
        HotelBookingDB.DATABASE[collection].drop()

    @staticmethod
    def insert(collection, data):
        HotelBookingDB.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return HotelBookingDB.DATABASE[collection].find(query)

    @staticmethod
    def findOne(collection, query):
        return HotelBookingDB.DATABASE[collection].find_one(query)

    @staticmethod
    def deleteId(collection, bookingReferenceID):
        HotelBookingDB.DATABASE[collection].delete_one({"Booking Reference ID": bookingReferenceID})

    @staticmethod
    def checkIfCollectionExists(collectionName):
        listOfCollections = HotelBookingDB.DATABASE.list_collection_names()
        for collection in listOfCollections:
            if collection == str(collectionName):
                return True