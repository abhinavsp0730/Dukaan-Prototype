# Dukaan Prototype - A Production Grade Dukaan MVP 
## **Django+PostgreSQL+Redis+Nginx+Gunicorn+Docker Compose 🔥 🔥 🔥**

## Quick Introduction:
This project is a production grade MVP of [Dukaan](https://mydukaan.io/)(DIY platform to create your own E-Commerce store).\
In this project I've used Django for the backend, PostgreSQL for production database, Introduced caching(Redis) mechanism  \
for increasing the throughput of the server and used event+time driven caching invalidation mechanism for invalidating cache. \
Used Gunicorn for the production server, Nginx for revrese proxy and for serving static files. \
Then I have Dockerize my project into 4 containers. i.e Web(Django+Gunicorn), db(PostgreSQL), redis_db(Redis), nginx(Nginx). \
And finally I've used Docker Compose for running multiple containers as a single service. 

## Infrastructre Diagram of Dukaan Prototype:

![Screenshot_20220413_132548](https://user-images.githubusercontent.com/43638955/163128761-9b3b7830-f47a-41af-b9e0-bca5f602f1b9.png)

## Web App walkthrough
(Note: While creating the project my aim was to focus enterily in the Backend part and to implement state of the art Backend Infra. \
So, I've created a very simple frontend by using just html and css. I'm able to do this by leveraging DTL and using my engineering jugadu mind) \
\
The web app is having minimal functionality of [Dukaan](https://mydukaan.io/). i.e Vendors can add their products and manage them using a dashboard. \
Then there is a unique link for each vendor which they can send to their customers. By using this unique link, customers can place the order \
by entering the neccesary details. Each placed orders then are displayed in the order's dashboard of vendor. \
Below are the snapshot of the web app. \

Signup Page (``` ```)
![Screenshot_20220413_163418](https://user-images.githubusercontent.com/43638955/163236389-9ca3a6fd-738d-49c5-a9a4-dd6afc2b1061.png)

Login Page (``` ```)
![Screenshot_20220413_163433](https://user-images.githubusercontent.com/43638955/163238161-c0d5ca4e-4c3b-4f0a-8495-1d510c69499b.png)

Vendor's (``` ```)


