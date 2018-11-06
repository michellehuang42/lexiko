import pymongo
client = pymongo.MongoClient()
db = client.test
webmd_causes = db.webmd_diseases

sections = webmd_causes.find_one({"name": "A1AT Deficiency"})['sections']
content = []
for section in sections:
	if section['name'] == 'Causes':
		content = section['content']
		break

print content

# Get Causes in terminal
# db.getCollection('webmd_diseases').find({"name":"A1AT Deficiency"}, {"sections": {$elemMatch: {"name": "Causes"}}})