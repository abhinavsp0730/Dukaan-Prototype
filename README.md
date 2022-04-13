# Dukaan Prototype- A Production Grade Dukaan MVP 
## **Django+PostgreSQL+Redis+Nginx+Gunicorn+Docker Compose 🔥 🔥 🔥**

## Quick Introduction:
This project is a production grade MVP of [Dukaan](https://mydukaan.io/)(DIY platform to create your own E-Commerce store).\
In this project I've used Django for the backend, PostgreSQL for production database, Introduced caching(Redis) mechanism  \
for increasing the throughput of the server and used event+time driven caching invalidation mechanism for invalidating cache. \
Used Gunicorn for the production server, Nginx for revrese proxy and for serving static files. \
Then I have Dockerize my project into 4 containers. i.e Web(Django+Gunicorn), db(PostgreSQL), redis_db(Redis), nginx(Nginx). \
And finally I've used Docker Compose for running multiple containers as a single service. 

