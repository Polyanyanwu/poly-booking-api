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

## **Objectives of the Site**

The site has objective of providing API component that enables the creation, fetching, updating and deletion of list of hotels, available rooms and necessary details for the hotel and rooms. The site will also use the API to enable user interaction via a Frontend to be developed with Bootstrap, Django and JavaScript tools.

## **User Experience Design**

### **Design Features**

The project has very limited time, therefore the initial design will aim at the following:

1. Create API for display getting list of hotels matching the criteria of city location.
2. Create API for fetching details of a selected hotel.
3. Create APIs for the update, delete, creation of hotels, room details and supporting code tables.
4. A frontend for rendering the list of hotels and data describing the Hotel like, Images, Price, Promotions, Ratings, facilities, etc.

If time permits, the update, delete and create functions shall be done by only privileged users.

## **User Stories**

### **Wireframes**

Wireframes were designed at the onset of the project and guided the development of the application. The full wireframes are [provided HERE](/docs/wireframe.md)

## Database

The application will use the Postgres Database and initial entity diagram is given below:

[Database Entity Diagram](/docs/poly_booking_ed.png)
