import pymongo

# Let's make a client.
# What is a client?
# mongo. What role are they in the 7/11 analogy? 
# They're the customer.
# The first step to talking to a mongoDB server (the 7/11) is making a customer.
# This customer is the person that can talk to the mongoDB server. The person running the
# mongoDB server (the 7/11) only speaks a certain language. The client (customer) is the only person
# speaks/understands this language.
# MAKE SURE THAT "mongod" IS RUNNING WHEN YOU RUN THIS
# Q: Why?
# A: So that the 7/11 is open so that there can be a customer

client = pymongo.MongoClient()

# Let's connect to a database
db = client.test

# Let''s connect to the cupcake collection :)
cupcake = db.cupcake

# Let's see what our cupcake collect has inside :)
print(cupcake.find_one({}))