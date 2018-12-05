import json, datetime



from bottle import route, run, request, abort

from pymongo import MongoClient

###feed data with Advanced REST client in Chrome or from cURL curl -d "<serial#>,<valueNumber>" -X PUT http://localhost:8001/documents

### http://40.124.7.95:8001/documents



## Define the MongoDB connection with URI model and access key

uri = "mongodb://<put your access key here>"

client = MongoClient(uri)

db = client.devdb





@route('/documents', method='PUT') #define a PUT route

def put_document():

    data = request.body.read()

    data = str(data) ##force to string

    data = data[1:]  ##remove leading b character

    data = data.split(",") ##csv into separate emements in list



    if not data[1] and data[0]: ##if nothing was passed, error out

        abort(400, 'No data received or malformed data')



    try:

        curTime = str(datetime.datetime.now())

        entity = {"value":"","nodeSN":"","currentTime":curTime}  ##initialize the dict and include time

        entity["value"]=data[1] ## Set the value of the input

        entity["nodeSN"]=data[0] ## Set unique identifier of whatever is being monitored

        db.devcollection.insert_one(entity) ## store in MongoDB API

    except:

        abort(400, 'cannot insert doc') ## gracefully error with 400 error and error text





@route('/documents/<_id>', method='GET')  ##return document by known _id

def get_document(_id):

    entity = client.devdocs.find_one({'_id': _id})

    if not entity:

        abort(404, 'No document with id %s' % _id)

    return entity



run(host='0.0.0.0', port=8001)  ## Answer on all interfaces port 8001


