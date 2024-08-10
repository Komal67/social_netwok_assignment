# social_netwok_assignment


# Project Overview
This project is a RESTful API built using Django Rest Framework for a social networking application. It includes functionalities for user authentication (signup, login, logout), user search, sending and managing friend requests, listing friends, and viewing pending friend requests. The application also includes rate limiting to prevent spamming friend requests.

## Features
- User Signup & Login: Simple user registration and login with email and password.
- Search Users: Search other users by email or name, with pagination.
- Friend Request Management: Send, accept, or reject friend requests.
- List Friends: List all friends of the authenticated user.
- Pending Friend Requests: View all pending friend requests received.
- Rate Limiting: Users cannot send more than 3 friend requests per minute.

## Requirements
- Python 3.x
- Django 4.x
- Django Rest Framework 3.x
- Django REST Framework Token Authentication
- Django Ratelimit
- Docker
- Postgres
- Postman (for API testing)

## Setup Instructions

1. Clone the Repository

```sh
git clone https://github.com/Komal67/social_netwok_assignment.git
cd social_network_assignment
```

2. Set Up Virtual Environment
```sh
python -m venv venv
source venv/bin/activate   
```
> On Windows use `venv\Scripts\activate`

3. Install Dependencies
```sh
pip install -r requirements.txt
```

4. Run Migrations
```sh
python manage.py makemigrations api
python manage.py migrate
```
5. Run the Server
```sh
python manage.py runserver
```

6. Access the API
- The API can be accessed at http://127.0.0.1:8000/.
- Use the Django admin at http://127.0.0.1:8000/admin/ to manage users and other models.

## API Endpoints
- Signup: POST `/api/signup/`
- Login: POST `/api/login/`
- Logout: POST `/api/logout/`
- Search Users: GET `/api/users/?search=<keyword>`
- Send Friend Request: POST `/api/friend-request/<recipient_id>/`
- Accept/Reject Friend Request: POST `/api/friend-request/<friend_request_id>?action=accept|reject`
- List Friends: GET `/api/friends/`
- Pending Friend Requests: GET `/api/pending-requests/`


## Docker Setup
To containerize this application, ensure you have Docker installed and then use the provided Dockerfile and docker-compose.yaml to build and run the application.
1. Build the Docker Image
```sh
docker build .
```
2. Run the Docker Container
```sh 
docker compose up
```
The application should now be running in a containerized environment.

### Docker Compose Services
- social_network: This service runs the Django application.
- database: This service runs a PostgreSQL database instance.

### Environment Variables
- DATABASE_NAME: The name of the PostgreSQL database.
- DATABASE_USER: The PostgreSQL database user.
- DATABASE_PASSWORD: The password for the PostgreSQL database user.
- DATABASE_HOST: The hostname of the PostgreSQL database (the database service).
- DATABASE_PORT: The port on which the PostgreSQL database is running (default: 5432).

### Docker Health Check
The database service includes a health check that ensures the PostgreSQL server is ready before the social_networkservice attempts to connect.

## High-Level Design (HLD) Overview

### Explanation
- User Management: Handles user registration, login, and authentication.
- Friend Requests: Manages sending, accepting, and rejecting friend requests between users.
- Friends List: Displays the list of users who are friends with the authenticated user.
- Search: Allows users to search for other users by email or name.
- Django Backend: The core of the application, handling requests and serving the API.
- PostgreSQL Database: Stores user data, friend requests, and relationships.

```
  +-------------------+                +--------------------+
  |                   |                |                    |
  |   User Interface  |   HTTP(S) API  |   Django Views &   |
  |     (Clients)     +---------------->+   Serializers     |
  |                   |                |                    |
  +-------------------+                +--------------------+
                                              |
                                              v
                                      +-------------------+
                                      |                   |
                                      |   Business Logic  |
                                      |   (Services &     |
                                      |    Models)        |
                                      |                   |
                                      +-------------------+
                                              |
                                              v
                                      +-------------------+
                                      |                   |
                                      |   Data Layer      |
                                      |   (Database &     |
                                      |    ORM)           |
                                      |                   |
                                      +-------------------+
                                              |
                                              v
                                      +-------------------+
                                      |                   |
                                      |   Infrastructure  |
                                      |   (Docker &       |
                                      |    Docker Compose)|
                                      |                   |
                                      +-------------------+

```
Docker:
<img width="1728" alt="Screenshot 2024-08-10 at 2 27 03 PM" src="https://github.com/user-attachments/assets/1181989f-beda-4466-a230-ed453127af3b">

Sign-up API :
<img width="1656" alt="Screenshot 2024-08-10 at 2 10 01 PM" src="https://github.com/user-attachments/assets/873608f1-186c-410b-bd55-0c13a8465931">

Login API:
<img width="1659" alt="Screenshot 2024-08-10 at 2 17 53 PM" src="https://github.com/user-attachments/assets/7c9b09be-5616-48da-a6c3-86dbf001aba9">

Logout API:
<img width="1662" alt="Screenshot 2024-08-10 at 2 18 29 PM" src="https://github.com/user-attachments/assets/3f9feae6-87b9-4a03-acbf-f6c520ec8d6b">

Add Friend API:
<img width="1658" alt="Screenshot 2024-08-10 at 2 21 45 PM" src="https://github.com/user-attachments/assets/e5aa4cdf-b77e-47b9-b318-886f48d2d7b6">

Pending Friend Request:
<img width="1658" alt="Screenshot 2024-08-10 at 2 23 39 PM" src="https://github.com/user-attachments/assets/c197b2c3-3926-4f51-84e4-111060e4d0ab">

Action on friend request:
<img width="1656" alt="Screenshot 2024-08-10 at 2 24 28 PM" src="https://github.com/user-attachments/assets/dd79ef5e-4b53-435c-9b69-221c293b4012">

List all Friend:
<img width="1658" alt="Screenshot 2024-08-10 at 2 25 00 PM" src="https://github.com/user-attachments/assets/675d55b5-a6ea-4369-9e16-b5e93022aa61">

Search User:
<img width="1659" alt="Screenshot 2024-08-10 at 2 25 39 PM" src="https://github.com/user-attachments/assets/113c5d71-b7d9-42c5-8f7d-42206470ca4b">

