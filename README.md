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
## Live Demo 
I've deployed this project in AWS EC2 instance(ubuntu server, 1 gig ram) \
Go to [http://ec2-13-233-115-87.ap-south-1.compute.amazonaws.com/](http://ec2-13-233-115-87.ap-south-1.compute.amazonaws.com/) and login via below credential(I've already populated the DB for the demo) 
```
username:
demo
password:
demo1234
```
## Web App walkthrough
(Note: While creating the project my aim was to focus enterily in the Backend part and to implement state of the art Backend Infra. \
So, I've created a very simple frontend by using just html and css. I'm able to do this by leveraging DTL and using my engineering jugadu mind) \
\
The web app is having minimal functionality of [Dukaan](https://mydukaan.io/). i.e Vendors can add their products and manage them using a dashboard. \
Then there is a unique link for each vendor which they can send to their customers. By using this unique link, customers can place the order \
by entering the neccesary details. Each placed orders then are displayed in the order's dashboard of vendor. \
Below are the snapshot of the web app. 

Signup Page (``` http://127.0.0.1:8000 #eg url for showing route ```) 👇
![Screenshot_20220413_163418](https://user-images.githubusercontent.com/43638955/163236389-9ca3a6fd-738d-49c5-a9a4-dd6afc2b1061.png)

Login Page (``` http://127.0.0.1:8000/login/ #eg url for showing route```) 👇
![Screenshot_20220413_163433](https://user-images.githubusercontent.com/43638955/163238161-c0d5ca4e-4c3b-4f0a-8495-1d510c69499b.png)

Vendor's "Your Product Dashboard" (```http://127.0.0.1:8000/your_product/ #eg url for showing route```) 👇
![Screenshot_20220413_163450](https://user-images.githubusercontent.com/43638955/163243533-a14b686f-344a-4b52-b197-f6451000ebec.png)

Vendor's Add NeW Product Form  (``` http://127.0.0.1:8000/new_product/ #eg url for showing route```) 👇
![Screenshot_20220413_163732](https://user-images.githubusercontent.com/43638955/163243670-22fa5c72-704b-4101-8b3a-68f1299abde8.png) 

Unique Link To Buy Product From vendors (```http://127.0.0.1:8000/order/demo #eg url for showing route```) 👇 
![Screenshot_20220413_163830](https://user-images.githubusercontent.com/43638955/163243921-0fd9450b-41a3-4e38-8462-19d3afac5d0e.png)

Vendor's Your Orders Dashboard (```http://127.0.0.1:8000/your_order/ #eg url for showing route```) 👇
![Screenshot_20220413_164202](https://user-images.githubusercontent.com/43638955/163244767-b4fc0925-1954-440e-9d4b-087ae108753f.png)

## Optimization using caching mechanism 
Suppose there's a sale in a particular day  in a vendor's dukaan shop. In this day the website is going to face high amount of traffic and this is gonna cause heavy load in the backend. \
When customers visits the vendor's unique link for buying products. \
Then for each visit of the client django is going to do costly query in the db and then going to generate the desired page everytime. Because of this the throughput of the \
server is gonna be decrease drastically.
Let's test throughput speed by bursting 100 requests in the vendor's unique link(I have already populated the db with dummy data) 
\
![ezgif com-gif-maker](https://user-images.githubusercontent.com/43638955/163250445-dbf53914-c072-4979-8e98-e52bf2344f74.gif) \
For completing 100 requesting it's taking around ``` 3.38 sec ```. Pretty slow right? \
\
For copinng with this problem I've implemented caching mechanism(redis). Which create a view level cache for each vendors \
```order``` view(this view is mapped to vendor's unique link).
\
Now, let's again test throughput speed by bursting 100 requests in the vendor's unique link but this time having cache enabled .
\
![ezgif com-gif-maker(1)](https://user-images.githubusercontent.com/43638955/163252685-5f4f7f4f-770a-4468-ac4e-50b7a5c78bad.gif)

Insane, this time it take only ```0.95 sec``` to process 100 requests. Which is roughly ```72%``` increase in throughput 🔥 🔥 🔥 

But what will happen when the vendor adds a new product or make the product unavailable? The customers will still get the cached page. \
For this problem we've to invalidate cache. Cache Invalidation is a crucial part in any caching mechanism system. \
I've implemented two cache Invalidation technique in this project.
1. Event based cahce invalidation.
2. Time Based cache Invalidation.

Let's see it in action and monitor what is happening underhood using ```redis-cli monitor``` command. \
When the customer first visits the unique url ```http://127.0.0.1:8000/order/demo #eg unique url``` then django will accept the request do some query in the ```Product``` model and then generate the ```order``` page\
simultaneously it **cahced** the response in the Redis Memory and then send the response back to the customer.
After that any subsequent request to the unique url will not hit the db rather it'll get the requested page from the cache which is stored\
in the Redis memory.

1. When the customer first the unique url ``` http://127.0.0.1:8000/order/demo ``` then this request hit the db do the costly query and generate the ```order``` page. \
and this page is then stored in the Redis Memory. \
You can see the ```$SETX``` redis command is executed for storing the cache. 👇 \
![r1](https://user-images.githubusercontent.com/43638955/163332657-a2887bd3-5ff9-4a99-8c71-8a7fc4bc02e5.png)
2. When we reload the page you can see that this time django is not hitting the db and hence not doing  the costly query 
but rather than it's getting the requested page from Redis Memory.\
You can see the ```$GET``` redis command is executed for sending the requested page. 👇 \
![r2](https://user-images.githubusercontent.com/43638955/163333322-f5d7f8eb-b583-4005-9eec-16799f319d7c.png)
3. Whenever the vendor is doing any modification in the ```Product``` model we're inavalidating the stored cache. 👇 \
   i) Event Based Cache Invalidation: Whenever the vendor is adding "New Product" or making the available product \
    available/unvaliable by using toogle "Yes" or "No" buttons, we're Invalidating the cache.\
   ii) Time Based Cache Invalidation: All the stored cached will automatically gets invalidated after ```15 mins```. 
 When we're making one of the product unavailable the cache are getting Invalidated.
 You can see the ```$DEL``` redis command is executed for Invalidating the cache.
![r3](https://user-images.githubusercontent.com/43638955/163333354-fec19299-23a6-4b82-880e-157abf2e4fd7.png)

## How to run this Project 
To run this project you need to install Docker and Docker Compose.\
Checkout the documentation if you don't have \
[How to install Docker](https://docs.docker.com/engine/install/)\
[How to install Docker Compose](https://docs.docker.com/compose/install/)\
After that open terminal and do,\
```$ mkdir dukaan-prototype```  
```$ cd dukaan-prototype``` 

Then clone this repo by running \
```$ git clone https://github.com/abhinavsp0730/Dukaan-Prototype ```

Update the file permissions for making ```entrypoint.sh``` executable
```
$ chmod +x app/entrypoint.sh
```
Then simply run 
``` 
# running the docker compose script to buid & spin up docker compose service. 
$ docker-compose -f docker-compose.prod.yml up -d --build 
``` 

![ezgif com-gif-maker(2)](https://user-images.githubusercontent.com/43638955/163382057-64318883-4081-4ad3-9fe1-7e0487a344db.gif) \
Then run 
```
# for doing the django migration 
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```

``` 
# copying the static files to right dir so that Nginx can serve them
$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
``` 


Now visit, \
``` http://localhost:1337/ ``` \
Yay, your production grade dukaan-protoproject has succefully up and is running 🎉 🎉 🎉 \
You can verify if it's working properly by runining and then looking the logs\
```$ docker-compose -f docker-compose.prod.yml logs -f``` \
You can spin down the docker compose service by runing \
```$ docker-compose -f docker-compose.prod.yml down -v``` 

While I was creating the project I didn't found the example of the exact tech stack in the internet. \
Also, there are lots of other thing happening in this project which I didn't cover in the ```readme.md```  intentionally.
\
So, if you want a tutorial blog for this project then send me mail at ```abhinavsp0730@gmail.com``` \
or say a hello to me in twitter ```@NeurlAP```  

## Closing Note:
I made this project for getting an internship at [Dukaan](https://mydukaan.io/) in the position of django backend intern. \
I'll update it below wheter I'm selected or not \
**Result**
```
?
```












