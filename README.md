#EMT-Server

To run: docker-compose up

To run python commands: 
```
	docker-compose up
	docker ps
	docker exec -t -i (container id) bash
```
	
Temp admin:
```
	admin
	root
```

##Database Schema:

Arrays will be stringified when obtained from the database

Appened the respective ID to its API call to obtain a specific object: e.g. "COL1"
```
API Call: ":8080/DBCalls/"
```
```
Collection object:
	{
		"colID"		: String ("COL4"),
		"colName"	: String,
		"colExh"	: Array ([Exhibit Object,]),
		"colMods"	: Array ([Module Object,])
	}
```
```
API Call: ":8080/DBCalls/Exhibits/"
```
```
Exhibt Object:
	{
		"exhID"		: String ("EX3"),
		"exhName"	: String,
		"exhIMG"	: String (URL),
		"exhDesc"	: String,
		"exhMods"	: Array ([Module Object,])
	}
```
```
API Call: ":8080/DBCalls/Modules/"
```
```
Module Object:
	{
		"modID"			: String("MOD2"),
		"modName"		: String,
		"modType"		: String,
		"modQuestions"	: Array ([Question Object,])
	}
```
```
Question Object:
	{
		"qID"		: String("QUE7")
		"qTitle"	: String,
		"qType"		: String
		"qExtra"	: String
	}
```
