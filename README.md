# ECSE 3038 - Lab 3

## Water Tank Management Exercise

This project can be used to manage a system that monitors the status of a set of electronically measured water tanks. The embedded circuit attached to each water tank will measure the height of the water in the tank and report on the tank's current stored volume as a percentage of its maximum capacity.

This RESTful API allows each IoT enabled water tank to interface with your server so that the measured values can be represented visually on a web page. The web page is designed by another member of this team.

The server is able to perform actions on a resource such as Create, Read, Update and Delete, which is done with the use of a locally stored list variable for prototyping, debugging and proof of concept.

### Tank Routes:

The server hosts at least 5 specific HTTP routes. They are:

```jsx
GET /tank
GET /tank/{id}

POST /tank

PATCH /tank/{id}

DELETE /tank/{id}
```

## Note
The input for post requests is 
```python
class Tank(BaseModel):
    id: UUID
	location: str
    latitude: float
    longitude: float
```

- id (automatically generated on post request)
- location - The Tank’s location description
- lat - The latitudinal coordinate of the tank
- long - The Longitudinal coordinate of the tank

**`GET /tank`**

This route returns a **list** of tank statuses previously made by the POST request. 

```jsx
GET /tank

// if an object has not been POSTed yet
Expected Response
[]

// if an object had been previously POSTed
Expected Response
[
    {
				"id": "0cf996c3-d9ca-4c0b-ab01-52b26c9050ec",
        "location": "Engineering department",
        "lat": "18.0051862",
        "long": "-76.7505108",
    },
		.
		.
		.
]
```
*fig. 1*

**`GET /tank/{id}`**

This route returns a **single JSON object** of  tank that is associated with the id passed as input in the route. If the API is unable to locate the object that has the id specified, the API responds with an appropriate response message and status code.  The structure of the object can be seen in *fig.2.*

```jsx
GET /tank{id}

Expected Response
{
		"id": "0cf996c3-d9ca-4c0b-ab01-52b26c9050ec",
    "location": "Engineering department",
    "lat": "18.0051862",
    "long": "-76.7505108",
}

```

*fig.2*

**`POST /tank`**

This route accepts a JSON object structured as depicted in *fig.3.* On success, the web application responds with the same JSON object that was posted with the addition of an `id` attribute. This `id` is generated by the API. 

The route also returns a status code that indicates that an object was **successfully created**.

```jsx
POST /tank

Example Request
{
    "location": "Physics department",
    "lat": 18.004741066082236,
    "long": -76.74875280426826
}

Example Response
{
		"id": "2ecc8f75-7594-4383-ac59-a24aff085cb3"
    "location": "Physics department",
    "lat": "18.004741066082236",
    "long": "-76.74875280426826"
}
```

*fig. 3*

**`PATCH /tank/{id}`**

Your server allows a client to alter the parts of one of the tanks after it has been POSTed. The server allows the requester to make a JSON body with any combination of the three attributes and update them as necessary (The client is NOT allowed to edit the `id` attribute). 

The route also returns a status code that indicates that an object was **successfully altered**.

If the API is unable to locate the object that has the id specified, the API responds with an appropriate response message and status code.

An example request and expected result can be seen in *fig.4.*

```jsx
PATCH /tank/{id}

Example Request
{
    "location": "<new location>", //optional
    "lat": "<new lat>", //optional
    "long": "<new long>", //optional
}

Expected Response
{
		"id": "<id>",
    "location": "<updated location>",
    "lat": "<updated lat>",
    "long": "<updated long>",
}
```

*fig. 4*

**`DELETE /tank/{id}`**

Allows the client to delete any previously POSTed object. The web application does not send back any message to the client once the objects has been deleted. There is, however, a suitable status code that indicates **success** and that an **empty response is expected**.

If the API is unable to locate the object that has the id specified, the API responds with an appropriate response message and status code.

**NOTE**

[X] A summary the expected behaviour of each function included in your code.

[X] The reason the code was written (eg. for the purpose of an assignment, etc).
```
To get a grade and the introduciton of the README as well, I suppose
```
[X] Two truths and a lie. I’ll guess which one is the lie.
```
I am apart of a swimming team
I was a previous member of Jamaica National Robotics Team
I enjoy Solo Leveling somewhat
```