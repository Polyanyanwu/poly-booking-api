# **POLY BOOKING API**

The Poly Booking API is a website designed to demonstrate hosting a hotel booking API component and using it to save, update, delete and render list of available hotels to the user.

![Poly Booking API](/docs/images/poly_booking_api.png)

## Live Site

[Poly Booking API Live](https://poly-booking-api.herokuapp.com)

- [**POLY BOOKING API**](#poly-booking-api)
  - [Live Site](#live-site)
  - [**Objectives of the Site**](#objectives-of-the-site)
  - [**User Experience Design**](#user-experience-design)
    - [**Design Features**](#design-features)
  - [**User Stories**](#user-stories)
    - [**Wireframes**](#wireframes)
  - [Database](#database)
  - [API End Points](#api-end-points)
    - [Authorization Token](#authorization-token)

## **Objectives of the Site**

The site has objective of providing API component that enables the creation, fetching, updating and deletion of list of hotels, available rooms and necessary details for the hotel and rooms. The site will also use the API to enable user interaction via a Frontend to be developed with Bootstrap, Django and JavaScript tools.

## **User Experience Design**

### **Design Features**

The project has very limited time, therefore the initial design will aim at the following:

1. Create API for display getting list of hotels matching the criteria of city location.
2. Create API for fetching details of a selected hotel.
3. Create APIs for the update, delete, creation of hotels and room amenity details.
4. A frontend for rendering the list of hotels and data describing the Hotel like, Images, Price, Promotions, Ratings, facilities, etc.

The facility codes and room types shall be general and maintained by the site owner. The codes shall be used in forming the API data.

If time permits, the update, delete and create functions shall be done by only privileged users.

## **User Stories**

### **Wireframes**

Wireframes were designed at the onset of the project and guided the development of the application. The full wireframes are ![provided HERE](/docs/wireframe.md)

## Database

The application will use the Postgres Database and initial entity diagram is given below:

![Database Entity Diagram](/docs/poly_booking_ed.png)

## API End Points

### Authorization Token

To obtain authorization token by registered users to be able to post data, you need to send a POST request to:
  ```https://poly-booking-api.herokuapp.com/api-token-auth/```
in the body of the POST message add your username and password as follows:

```
{
    "username": "xxx",
    "password": "xxxx"
}
```
You will be provided with a response like this:

```{
    "token": "13ecc0xxxfa6286485924f97abaa11105dca2385"
}```

For your POST requests to be authenticated, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:

Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b


### API URL

**1. Get list of all hotels: **
  GET method end point: ```https://poly-booking-api.herokuapp.com/api/hotels```

**2. Post Hotel Data, include hotel rooms and hotel general facilities:**
  POST method end point: ```https://poly-booking-api.herokuapp.com/api/hotels```

```

    {
        "name": "xxStation",
        "brief_description": "Travel xx",
        "full_description": "Located in Nagaoka,xx",
        "rating": 4.00,
        "address": "string ",
        "city": "string",
        "contact_email": "gmail",
        "contact_name": string",
        "contact_phone": "string",
        "image_url": "https://t-cfurl",
        "free_cancel_limit": hours in numbers,
        "prepayment_needed": true or false,
        "hotel_rooms": [
            {
              "room_type": code number,
                "price": decimal,
                "on_sale": true or false,
                "quantity": integer,
                "sale_price": decimal,
                "breakfast_included": true or false
            },
             {
               "room_type": code number, 
                "price": decimal,
                "on_sale": true or false,
                "quantity": integer,
                "sale_price": decimal,
                "breakfast_included": true or false
            }
        ],
        "hotel_general_facility": [
            {
                "facility": code number
            },
            {
                "facility": code number
            }
        ]
    }

```

Note that Authorization token is required for the POST method.

**3. Update Hotel Data, include hotel rooms and hotel general facilities:**
PUT method end point: ```https://poly-booking-api.herokuapp.com/api/hotels/<hotel id>/```
The JSON structure for the body is same as in the POST but the request end point has to include the hotel id to be updated.
Also the user is validated to enure you are updating your won hotels.

**4. Get details of a specific hotel.**
GET method end point: ```https://poly-booking-api.herokuapp.com/api/hotels/<hotel id>/```

**5. Delete a specific hotel**
DELETE method end point: ```https://poly-booking-api.herokuapp.com/api/hotels/<hotel id>/```
Authorization is required and validation of the user is done.

6. Get lis of hotel rooms
GET method end point: ```https://poly-booking-api.herokuapp.com/api/hotel-room/<hotel id>/```

7. Create new Hotel Room record:
POST method end point ```https://poly-booking-api.herokuapp.com/api/hotel-room/<hotel id>/```
Expects list of hotel rooms:

```
  [
    {
      "hotel_id":id number,
      "room_type": room type code,
      "price": decimal,
      "on_sale": true,
      "quantity": number,
      "sale_price": decimal,
      "breakfast_included": true/false
    },
    {
      "hotel_id": 1,
      "room_type": 5,
      "price": "90.00",
      "on_sale": true,
      "quantity": 3,
      "sale_price": "60.00",
      "breakfast_included": true
    }
  ]

```
8. Update Hotel Room details:

PUT method end point: ```https://poly-booking-api.herokuapp.com/api/hotel-room/<hotel id>/<room_id>/```

```
    {
      "price": decimal,
      "on_sale": true,
      "quantity": number,
      "sale_price": decimal,
      "breakfast_included": true/false
    }
```

Although room type could be added as a field to be updated, however care should be taken as same room type for the same hotel is not permitted to be added more than once.

9. Delete a specific hotel room:
DELETE method end point: ```https://poly-booking-api.herokuapp.com/api/hotel-room/<hotel id>/<room_id>/```
Authorization is required and validation of the user is done.

10. Get lis of hotel room type facilities
GET method end point: ```https://poly-booking-api.herokuapp.com/api/room-facility/<hotel id>/<room type>/```

11. Add new facility to hotel room type:
POST method end point ```https://poly-booking-api.herokuapp.com/api/room-facility/<hotel id>/<room type>/```
Expects list of facility codes in the body of the request:

```
    [
      {
        "facility": 14
      },
      {
        "facility": 3
      },
        
        {
        "facility": 10
      }
    ]
```
Response is given as list of all created records.
Validation is done and error messages are displayed where appropriate.
