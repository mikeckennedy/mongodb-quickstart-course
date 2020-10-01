## Getting Started
### Create Admin User
```js
db.createUser({    
	user: '_username_',  
	pwd: passwordPrompt(),  
	roles: [{role: 'userAdminAnyDatabase', db:'admin'}]  
})
```
### Drop User

```js
db.dropUser('_username_');
```
### Create / Switch Database
```js
use <database_name>;
```
### db.dropDatabase( )
```js
use <database_name>
db.dropDatabase();
```
### Introspection
```js
// server level
show dbs;
show users;
show roles;
```
```js
use <database_name>
show collections;
```
### db.createCollection( )
MongoDB creates a collection implicitly when the collection is first referenced in a command, this method is used primarily for creating new collections that use specific options.
> The [`db.createCollection()`](https://docs.mongodb.com/manual/reference/method/db.createCollection/#db.createCollection "db.createCollection()") method has the following prototype form:
```js
db.createCollection('_name_',
	{
		capped: <boolean>,
		autoIndexId: <boolean>,
		size: <number>,
		max: <number>,
		storageEngine: <document>,
		validator: <document>,
		validationLevel: <string>,
		validationAction: <string>,
		indexOptionDefaults: <document>,
		viewOn: <string>,              // Added in MongoDB 3.4
		pipeline: <pipeline>,          // Added in MongoDB 3.4
		collation: <document>,         // Added in MongoDB 3.4
		writeConcern: <document>
	}
)
```
### db.collection.drop( )
MongoDB's **db.collection.drop()** is used to drop a collection from the database.
> Basic syntax of **drop()** command is as follows:
```js
db.<collection_name>.drop()
```

### db.collection.insert( )
Inserts a document or documents into a collection. If the collection does not exist, then the  [`insert()`](https://docs.mongodb.com/manual/reference/method/db.collection.insert/#db.collection.insert "db.collection.insert()")  method will create the collection.
> The [`insert()`](https://docs.mongodb.com/manual/reference/method/db.collection.insert/#db.collection.insert "db.collection.insert()") method has the following syntax:
```js
db.collection.insert(
	<document or documents array>,
	{
		writeConcern: <document>,
		ordered: <boolean>
	}
)
```
example:
```js
db.products.insert(
	[
		{ _id: 11, item: "pencil", qty: 50, type: "no.2" },
		{ item: "pen", qty: 20 },
		{ item: "eraser", qty: 25 }
	]
)
```
The operation inserted the following three documents:
```js
{ "_id" : 11, "item" : "pencil", "qty" : 50, "type" : "no.2" }
{ "_id" : ObjectId("51e0373c6f35bd826f47e9a0"), "item" : "pen", "qty" : 20 }
{ "_id" : ObjectId("51e0373c6f35bd826f47e9a1"), "item" : "eraser", "qty" : 25 }
```
#### _id  Field
If the document does not specify an [_id](https://docs.mongodb.com/manual/reference/glossary/#term-id) field, then MongoDB will add the `_id` field and assign a unique [`ObjectId`](https://docs.mongodb.com/manual/reference/method/ObjectId/#ObjectId "ObjectId") for the document before inserting. If the document contains an `_id` field, the `_id` value must be unique within the collection to avoid duplicate key error.
> ObjectId is 12 bytes hexadecimal number unique for every document in a collection. 12 bytes are divided as follows:   
```
ObjectId(4 bytes timestamp, 3 bytes machine id, 2 bytes process id, 3 bytes incrementer)`
```
### db.collection.insertOne( )
Inserts a document into a collection.
> The [`insertOne()`](https://docs.mongodb.com/manual/reference/method/db.collection.insertOne/#db.collection.insertOne "db.collection.insertOne()") method has the following syntax:
```js
db.collection.insertOne(
   <document>,
   {
	   writeConcern: <document>
   }
)
```
### db.collection.insertMany( )
Inserts multiple documents into a collection.
> The [`insertMany()`](https://docs.mongodb.com/manual/reference/method/db.collection.insertMany/#db.collection.insertMany "db.collection.insertMany()") method has the following syntax:
```js
db.collection.insertMany(
	[ <document 1> , <document 2>, ... ],
	{
		writeConcern: <document>,
		ordered: <boolean>
	}
)
```
### db.collection.update( )
Modifies an existing document or documents in a collection. The method can modify specific fields of an existing document or documents or replace an existing document entirely, depending on the  [update parameter](https://docs.mongodb.com/manual/reference/method/db.collection.update/#update-parameter).

By default, the  [`db.collection.update()`](https://docs.mongodb.com/manual/reference/method/db.collection.update/#db.collection.update "db.collection.update()")  method updates a  **single**  document. Include the option  [multi: true](https://docs.mongodb.com/manual/reference/method/db.collection.update/#multi-parameter)  to update all documents that match the query criteria.
> The [`db.collection.update()`](https://docs.mongodb.com/manual/reference/method/db.collection.update/#db.collection.update "db.collection.update()") method has the following form:
```js
db.collection.update(
   <query>,
   <update>,
	{
		upsert: <boolean>,
		multi: <boolean>,
		writeConcern: <document>,
		collation: <document>,
		arrayFilters: [ <filterdocument1>, ... ],
	    hint:  <document|string>        // Available starting in MongoDB 4.2
	}
)
```
example:
```js
db.books.update(
	{ _id: 1 },
	{
		$inc: { stock: 5 },
		$set: {
			item: "ABC123",
			"info.publisher": "2222",
			tags: [ "software" ],
			"ratings.1": { by: "xyz", rating: 3 }
		}
	}
)
```
This operation corresponds to the following SQL statement:
```sql
UPDATE books
SET    stock = stock + 5
       item = "ABC123"
       publisher = 2222
       pages = 430
       tags = "software"
       rating_authors = "ijk,xyz"
       rating_values = "4,3"
WHERE  _id = 1
```
#### Insert a New Document if No Match Exists (`Upsert`)
When you specify the option  [upsert: true](https://docs.mongodb.com/manual/reference/method/db.collection.update/#update-upsert):

-   If document(s) match the query criteria,  [`db.collection.update()`](https://docs.mongodb.com/manual/reference/method/db.collection.update/#db.collection.update "db.collection.update()")  performs an update.
-   If no document matches the query criteria,  [`db.collection.update()`](https://docs.mongodb.com/manual/reference/method/db.collection.update/#db.collection.update "db.collection.update()")  inserts a  _single_  document.
```js
db.books.update(
	{ item: "ZZZ135" },   // Query parameter
	{                     // Replacement document
		item: "ZZZ135",
		stock: 5,
		tags: [ "database" ]
	},
	{ upsert: true }      // Options
)
```
### db.collection.updateOne( )
Updates a single document within the collection based on the filter.
> The [`updateOne()`](https://docs.mongodb.com/manual/reference/method/db.collection.updateOne/#db.collection.updateOne "db.collection.updateOne()") method has the following syntax:
```js
db.collection.updateOne(
	<filter>,
    <update>,
    {
		upsert: <boolean>,
	    writeConcern: <document>,
	    collation: <document>,
	    arrayFilters: [ <filterdocument1>, ... ],
	    hint:  <document|string>        // Available starting in MongoDB 4.2.1
	}
)
```
### db.collection.updateMany( )
Updates all documents that match the specified filter for a collection.
> The  [`updateMany()`](https://docs.mongodb.com/manual/reference/method/db.collection.updateMany/#db.collection.updateMany "db.collection.updateMany()")  method has the following form:
```js
db.collection.updateMany(
	<filter>,
    <update>,
    {
		upsert: <boolean>,
	    writeConcern: <document>,
	    collation: <document>,
	    arrayFilters: [ <filterdocument1>, ... ],
	    hint:  <document|string>        // Available starting in MongoDB 4.2.1
   }
)
```
### db.collection.find( )
Selects documents in a collection or view and returns a  [cursor](https://docs.mongodb.com/manual/reference/glossary/#term-cursor) to the documents that match the `query` criteria. When the [`find()`](https://docs.mongodb.com/manual/reference/method/db.collection.find/#db.collection.find "db.collection.find()") method “returns documents,” the method is actually returning a cursor to the documents.(https://docs.mongodb.com/manual/reference/glossary/#term-cursor) to the selected documents.
> The basic syntax of **find()** method is as follows:
```js
db.<collection_name>.find()
```
#### Examples
> The examples in this section use documents from the [bios collection](https://docs.mongodb.com/manual/reference/bios-example-collection/) where the documents generally have the form:
```js
{
	"_id" : <value>,
    "name" : { "first" : <string>, "last" : <string> },       // embedded document
    "birth" : <ISODate>,
    "death" : <ISODate>,
    "contribs" : [ <string>, ... ],                           // Array of Strings
    "awards" : [
		{ "award" : <string>, year: <number>, by: <string> }  // Array of embedded documents
        ...
    ]
}
```
- Find All Documents in a Collection
```js
db.bios.find()
```
-  Query for Equality
```js
// documents in the bios collection where `_id` equals `5`
db.bios.find( { '_id': 5 } )

// documents in the bios collection where the field `last` in the `name` embedded document equals `"Hopper"`:
db.bios.find( { 'name.last': "Hopper" } )
```
> To access fields in an embedded document, use [dot notation](https://docs.mongodb.com/manual/core/document/#document-dot-notation-embedded-fields) (`"<embedded  document>.<field>"`).

- Query Using Operators
```js
// The following operation uses the `$in` operator to return documents in the bios collection where `_id` equals either `5` or `ObjectId("507c35dd8fada716c89d0013")`
db.bios.find(
	{ '_id': { $in: [ 5, ObjectId("507c35dd8fada716c89d0013") ] } }
)

// The following operation uses the `$gt` operator returns all the documents from the `bios` collection where `birth` is greater than `new  Date('1950-01-01')`
db.bios.find( 
	{ 'birth': { $gt: new Date('1950-01-01') } } 
)

// The following operation uses the `$regex` operator to return documents in the bios collection where `name.last` field starts with the letter `N` (or is `"LIKE  N%"`)
db.bios.find(
	{ 'name.last': { $regex: /^N/ } }
)
```
- Query for Ranges
```js
// Combine comparison operators to specify ranges for a field. 
// The following operation returns from the bios collection documents where `birth` is between `new  Date('1940-01-01')` and `new  Date('1960-01-01')` (exclusive)
db.bios.find( { 'birth': { $gt: new Date('1940-01-01'), $lt: new Date('1960-01-01') } } )
```
- Query for Multiple Conditions
```js
// The following operation returns all the documents from the bios collection where `birth` field is `greater  than` `new  Date('1950-01-01')` and `death` field does not exists
db.bios.find( 
	{
		'birth': { $gt: new Date('1920-01-01') },
	    'death': { $exists: false }
	} 
)
```
- Query Embedded Documents
```js
// The following operation returns documents in the bios collection where the embedded document `name` is _exactly_  `{  first:  "Yukihiro",  last:  "Matsumoto"  }`, including the order
db.bios.find(
	{ 'name': { 'first': "Yukihiro", 'last': "Matsumoto" } }
)
/* 
The `name` field must match the embedded document exactly. The query does not match documents with the following `name` fields:
	{ first: "Yukihiro", aka: "Matz", last: "Matsumoto" }
	{ last: "Matsumoto", first: "Yukihiro" }
*/

// The following operation returns documents in the bios collection where the embedded document `name` contains a field `first` with the value `"Yukihiro"` and a field `last` with the value `"Matsumoto"`.
db.bios.find(  
	{  
		'name.first': "Yukihiro",  
		'name.last': "Matsumoto"  
	}  
)
/*
The query matches the document where the `name` field contains an embedded document with the field `first` with the value `"Yukihiro"` and a field `last` with the value `"Matsumoto"`.
For instance, the query would match documents with `name` fields that held either of the following values:
	{ first: "Yukihiro", aka: "Matz", last: "Matsumoto" }
	{ last: "Matsumoto", first: "Yukihiro" }
*/
```
- Query for an Array Element
```js
// The following operation returns documents in the where the array field `contribs` contains the element "UNIX"
db.bios.find( { 'contribs': "UNIX" } )

// The following operation returns documents in the bios collection where the array field `contribs` contains the element "ALGOL" or "Lisp"
db.bios.find( 
	{ 'contribs': { $in: [ "ALGOL", "Lisp" ] } } 
)

// The following operation use the `$all` query operator to return documents in the bios collection where the array field `contribs` contains both the elements "ALGOL" and "Lisp"
db.bios.find( 
	{ 'contribs': { $all: [ "ALGOL", "Lisp" ] } } 
)

// The following operation uses the `$size` operator to return documents in the bios collection where the array size of `contribs` is 4
db.bios.find( 
	{ 'contribs': { $size: 4 } } 
)
```
- Query an Array of Documents
```js
// The following operation returns documents in the bios collection where the `awards` array contains an element with `award` field equals "Turing  Award"
db.bios.find(
	{ 'awards.award': "Turing Award" }
)

// The following operation returns documents in the bios collection where the `awards` array contains at least one element with both the `award` field equals "Turing  Award" and the `year` field greater than 1980
db.bios.find(
	{ 'awards': { $elemMatch: { award: "Turing Award", year: { $gt: 1980 } } } }
)
```
#### Projections
The [projection](https://docs.mongodb.com/manual/reference/method/db.collection.find/#find-projection) parameter specifies which fields to return. The parameter contains either include or exclude specifications, not both, unless the exclude is for the `_id` field.
> Unless the `_id` field is explicitly excluded in the projection document `_id:  0`, the `_id` field is returned.

- Specify the Fields to Return
```js
// The following operation finds all documents in the bios collection and returns only the `name` field, `contribs` field and `_id` field
db.bios.find( 
	{ }, 
	{ 'name': 1, 'contribs': 1 } 
)
```
- Explicitly Excluded Fields
```js
// The following operation queries the bios collection and returns all fields _except_ the `first` field in the `name` embedded document and the `birth` field
db.bios.find(
	{ 'contribs': "OOP" },
	{ 'name.first': 0, 'birth': 0 }
)
```
- Explicitly Exclude the  `_id`  Field
```js
// The following operation finds documents in the bios collection and returns only the `name` field and the `contribs` field
db.bios.find(
	{ },
    { 'name': 1, 'contribs': 1, '_id': 0 }
)
```
- On Arrays and Embedded Documents
```js
// The following operation queries the bios collection and returns the `last` field in the `name` embedded document and the first two elements in the `contribs` array
db.bios.find(
	{ },
	{ '_id': 0, 'name.last': 1, 'contribs': { $slice: 2 } } 
)
```
