# Chat System

Cloud Continuous Delivery of Flask Microservices: online chatting system

## Services used

- AWS App runner
- AWS CloudFormation
- MongoDB Atlas

## Introduction

This online chatting system is designed to be straightforward and user-friendly. It is built using Flask, a popular
Python-based microservice framework, and is deployed on the AWS App Runner platform. The system leverages the power of
MongoDB Atlas, a highly scalable and reliable cloud-based database service, to store user profile and credentials. The
chat microservice is deployed using AWS CloudFormation, a tool that enables users to create, manage, and update AWS
infrastructure resources in a safe and predictable manner. This combination of powerful technologies ensures that the
online chatting system is able to handle a large number of concurrent users and provide a fast and responsive user
experience.

## Architecture

- Flask Microservice: The main application logic is implemented using the Flask framework. It is responsible for
  handling incoming requests from users, processing chat messages, and interacting with the database.

- MongoDB Atlas Database: The system uses MongoDB Atlas, a cloud-based NoSQL database service, to store chat messages
  and other data. This database is deployed on the AWS Cloud and can be easily scaled as the number of users grows.

- AWS App Runner: The Flask microservice is deployed on the AWS App Runner platform, which provides a highly available
  and scalable infrastructure for running web applications. The App Runner automatically manages the deployment,
  scaling, and monitoring of the application.

- AWS CloudFormation: The MongoDB Atlas database is deployed using AWS CloudFormation, which provides a safe and
  predictable way to manage cloud infrastructure. This allows for easy deployment and maintenance of the database and
  ensures that the infrastructure is in a known state.

- Load Balancer: To ensure high availability and scalability, the system uses an AWS load balancer to distribute
  incoming traffic across multiple instances of the Flask microservice.

## Getting started

1. Clone the repository and `cd` into the project directory
2. Install needed dependencies using `pip install -r app/requirements.txt`
3. Create a MongoDB Atlas database and add the connection string to the `MONGO_URI` environment variable in the
   `app/dao/db.py` file
4. Run the application using `gunicorn --worker-class eventlet -w 1 app.server:app` to start a production server,
   or `python app/server.py` to start a development server

## Demo

Application is deployed on [AWS](https://s2z35ykgqb.us-east-1.awsapprunner.com/)

## Done

- Create a Microservice in Flask or Fast API
- Push source code to Github
- Configure Build System to Deploy changes
- Use IaC (Infrastructure as Code) to deploy code
- Use either AWS, Azure, GCP (recommended services include Google App Engine, AWS App Runner or Azure App Services)
  Containerization is optional, but recommended

## License
[MIT License]()