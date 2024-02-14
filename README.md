# A Book Store Backend Case Study for E-Adam

Dear E-Adam Team,

I am thrilled to present the **finalized** documentation for the Book Store Management application, as per the assignment provided. Below is a detailed overview along with the necessary steps to proceed.

Kindly ensure the creation of a ".env" file from ".env.example" and establish the connection between the **NestJS** App and the **PostgreSQL** database.

Additionally, you have the option to utilize the **"generate_jwt.py"** file to generate **JWT_SECRET**, **JWT_AT_KEY**, and **JWT_RT_KEY** values for integration into your **".env"** configuration file.

Your cooperation in this matter is highly appreciated.

---

### Assignment Paper Details

#### Project Description:

We aim to develop a Book Store Management application. The application will consist of three roles: User, Store Manager, and Admin.

### User Role:

- Ability to view all bookstores.
- Can view the books available in each store and query which books are available in which bookstores.

### Store Manager Role:

- Can add or remove a specific quantity of a book to/from a store (from the Book table)

### Admin Role:

- Can create a new bookstore.
- Can add a new book.
- Can add or remove a specific quantity of a particular book to/from a specific bookstore.
- Adding new users and roles can only be done by the Admin.

---

### Overview of Implementation

I am pleased to announce the successful implementation of all stipulated features outlined above. Furthermore, I have extended the functionality to incorporate essential elements such as registration processes, JWT integration, and access token management to enhance the overall user experience and security measures.

Please refer to the API usage details provided below for a comprehensive understanding of the system's functionalities and their respective endpoints.

Your feedback and collaboration are eagerly awaited as we proceed further in this endeavor. Thank you for this opportunity, and I am excited about the prospect of collaborating with your esteemed team.

**Warm regards, Onur Gümüş.**

## Authentication API

This API provides endpoints for user authentication, including registration, login, and fetching current user details.

### Endpoints

#### Register User

- **URL:** `POST /api/auth/register`
- **Request:**
- **Body Parameters:**
  - `firstName` (string, required): First name of the user.
  - `lastName` (string, optional): Last name of the user.
  - `email` (string, required): Email address of the user.
  - `password` (string, required): Password for the user account (minimum length: 8 characters).
- **Response:**
- **Success Response (201 Created):**
  - Returns a SignupResponse object containing the registered user details and an access token.
- **Example Response:**
  ```json
  {
    "user": {
      "id": 5,
      "firstName": "Hamza",
      "lastName": "Hamzaoğlu",
      "email": "gms_10ur@hotmail.com",
      "role": "user",
      "createdAt": "2024-02-14T12:32:47.371Z",
      "updatedAt": "2024-02-14T12:32:47.371Z"
    },
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjUsImlhdCI6MTcwNzkxMzk2NywiZXhwIjoxNzA5MTIzNTY3fQ.X7wu4-OGczYFeFRMQBnA8ck9y1TYv0w3Eu1rfmnFbcw"
  }
  ```

#### User Login

- **URL:** `POST /api/auth/login`
- **Request:**
  - **Body Parameters:**
    - `email` (string, required): Email address of the user.
    - `password` (string, required): Password for the user account (minimum length: 8 characters).
- **Response:**
  - **Success Response (200 OK):**
    - Returns a LoginResponse object containing the logged-in user details and an access token.
- **Example Response:**
  ```json
  {
    "user": {
      "id": 5,
      "firstName": "Hamza",
      "lastName": "Hamzaoğlu",
      "email": "gms_10ur@hotmail.com",
      "role": "user",
      "createdAt": "2024-02-14T12:32:47.371Z",
      "updatedAt": "2024-02-14T12:32:47.371Z"
    },
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjUsImlhdCI6MTcwNzkxNDUzOSwiZXhwIjoxNzA5MTI0MTM5fQ.oeKcpW2-0_9vigV8DJw6N2SqBFTfZy5WQFKJgpk3niY"
  }
  ```

#### Get Current User Details

- **URL:** `GET /api/auth/me`
- **Authorization:** Bearer Token
- **Response:**
  - **Success Response (200 OK):**
    - Returns a UserResponseDto object containing details of the current authenticated user.

---

## UserController

This controller manages user operations such as creating, retrieving, and updating user information. All operations shuld done by an admin. Authorization is handled by "Bearer Token"

### Endpoints

#### Create User

- **URL:** `POST /api/user`
- **Description:** Creates a new user.
- **Authorization:** Only users with the role of admin can access this endpoint.
- **Request:**
  - **Body Parameters:**
    - `firstName` (string, required): First name of the user.
    - `lastName` (string, optional): Last name of the user.
    - `email` (string, required): Email address of the user.
    - `password` (string, required): Password for the user account.
    - `role` (Role, required): Role of the user. (Enum: ADMIN, USER)
- **Response:** Returns the newly created user information with a HTTP 200 response.
- **Example Response:**
  ```json
  {
    "firstName": "Onur",
    "lastName": "Gümüş",
    "email": "10urgumus@gmail.com",
    "password": "$argon2id$v=19$m=19456,t=2,p=1$5NAGKJ1+NuYJNC3l9v+PNA$/1zUfF405oPltZAiZGFlv6yEIX1kkHhbKuowHuRToFU",
    "role": "admin",
    "id": 1,
    "createdAt": "2024-02-14T12:49:05.654Z",
    "updatedAt": "2024-02-14T12:49:05.654Z"
  }
  ```

#### List All Users

- **URL:** `GET /api/user`
- **Description:** Retrieves a list of all users.
- **Authorization:** Only users with the role of admin can access this endpoint.
- **Response:** Returns a list of all users with a HTTP 200 response.
- **Example Response:**
  ```json
  [
    {
      "id": 1,
      "firstName": "Onur",
      "lastName": "Gümüş",
      "email": "10urgumus@gmail.com",
      "role": "admin",
      "createdAt": "2024-02-14T10:51:17.279Z",
      "updatedAt": "2024-02-14T10:51:17.279Z"
    },
    {
      "id": 5,
      "firstName": "Hamza",
      "lastName": "Hamzaoğlu",
      "email": "gms_10ur@hotmail.com",
      "role": "user",
      "createdAt": "2024-02-14T12:32:47.371Z",
      "updatedAt": "2024-02-14T12:32:47.371Z"
    },
    {
      "id": 6,
      "firstName": "Tutku",
      "lastName": "Gümüş",
      "email": "tutkukucuker1@gmail.com",
      "role": "storeManager",
      "createdAt": "2024-02-14T12:49:05.654Z",
      "updatedAt": "2024-02-14T12:49:05.654Z"
    }
  ]
  ```

#### Get User by ID

- **URL:** `GET /api/user/:id`
- **Description:** Retrieves a user by their ID.
- **Parameters:**
  - `id` (number): ID of the user.
- **Authorization:** Only users with the role of admin can access this endpoint.
- **Response:** Returns the user information corresponding to the provided ID with a HTTP 200 response.
- **Example Response:**
  ```json
  {
    "id": 5,
    "firstName": "Hamza",
    "lastName": "Hamzaoğlu",
    "email": "gms_10ur@hotmail.com",
    "password": "$argon2id$v=19$m=19456,t=2,p=1$jwqqMlxCfaZuFziFxJ85rg$hdfLDdHjRRBMSSoaNkncofs9XXHrFipJDQCBaHp10a4",
    "role": "user",
    "createdAt": "2024-02-14T12:32:47.371Z",
    "updatedAt": "2024-02-14T12:32:47.371Z"
  }
  ```

#### Update User

- **URL:** `PATCH /api/user/:id`
- **Description:** Updates user information by their ID.
- **Parameters:**
  - `id` (number): ID of the user.
- **Authorization:** Only users with the role of admin can access this endpoint.
- **Request:**
  - **Body Parameters:**
    - `firstName` (string, optional): New first name of the user.
    - `lastName` (string, optional): New last name of the user.
    - `email` (string, optional): New email address of the user.
    - `password` (string, optional): New password for the user account.
    - `role` (Role, optional): New role of the user. (Enum: ADMIN, USER)
- **Response:** Returns the updated user information with a HTTP 200 response.
- **Example Response:**
  ```json
  {
    "id": 5,
    "firstName": "Hamza",
    "lastName": "Hamzaoğlu",
    "email": "gms_10ur@hotmail.com",
    "role": "storeManager",
    "createdAt": "2024-02-14T12:32:47.371Z",
    "updatedAt": "2024-02-14T12:32:47.371Z"
  }
  ```

---

## StoreController

This controller manages store-related operations such as creating, retrieving, and updating store information.

### Endpoints

#### Create Store

- **URL:** `POST /api/store`
- **Description:** Creates a new store.
- **Authorization:** Only users with the role of admin can access this endpoint.
- **Request:**
  - **Body Parameters:**
    - `name` (string, required): Name of the store.
- **Response:** Returns the newly created store information with a HTTP 200 response.
- **Example Response:**
  ```json
  {
    "id": 3,
    "name": "Another BookStore",
    "createdAt": "2024-02-14T12:55:11.858Z",
    "updatedAt": "2024-02-14T12:55:11.858Z"
  }
  ```

#### List All Stores

- **URL:** `GET /api/store`
- **Description:** Retrieves a list of all stores.
- **Authorization:** Users with the role of admin or user can access this endpoint.
- **Response:** Returns a list of all stores with a HTTP 200 response.
- **Example Response:**
  ```json
  [
    {
      "id": 1,
      "name": "E-Adam BookStore",
      "createdAt": "2024-02-14T11:12:16.675Z",
      "updatedAt": "2024-02-14T11:12:16.675Z"
    },
    {
      "id": 2,
      "name": "Myrista BookStore",
      "createdAt": "2024-02-14T11:12:42.352Z",
      "updatedAt": "2024-02-14T11:12:42.352Z"
    },
    {
      "id": 3,
      "name": "Another BookStore",
      "createdAt": "2024-02-14T12:55:11.858Z",
      "updatedAt": "2024-02-14T12:55:11.858Z"
    }
  ]
  ```

#### Get Store by ID

- **URL:** `GET /api/store/:id`
- **Description:** Retrieves a store by its ID.
- **Parameters:**
  - `id` (number): ID of the store.
- **Authorization:** Users with the role of admin or user can access this endpoint.
- **Response:** Returns the store information corresponding to the provided ID with a HTTP 200 response.
- **Example Response:**
  ```json
  {
    "id": 1,
    "name": "E-Adam BookStore",
    "createdAt": "2024-02-14T11:12:16.675Z",
    "updatedAt": "2024-02-14T11:12:16.675Z"
  }
  ```

#### Update Store

- **URL:** `PATCH /api/store/:id`
- **Description:** Updates store information by its ID.
- **Parameters:**
  - `id` (number): ID of the store.
- **Authorization:** Only users with the role of admin can access this endpoint.
- **Request:**
  - **Body Parameters:**
    - `name` (string, required): New name of the store.
- **Response:** Returns the updated store information with a HTTP 200 response.
- **Example Response:**
  ```json
  {
    "id": 3,
    "name": "YET Another BookStore",
    "createdAt": "2024-02-14T12:55:11.858Z",
    "updatedAt": "2024-02-14T12:55:11.858Z"
  }
  ```

---

## BookController

This controller manages book-related operations such as creating, retrieving, and updating book information.

### Endpoints

#### Create Book

- **URL:** `POST /api/book`
- **Description:** Creates a new book.
- **Authorization:** Only users with the role of store manager or admin can access this endpoint.
- **Request:**
  - **Body Parameters:**
    - `name` (string, required): Name of the book.
    - `author` (string, required): Author of the book.
    - `publisher` (string, required): Publisher of the book.
    - `quantity` (number, required): Quantity of the book in stock.
    - `storeId` (number, required): ID of the store where the book is available.
- **Response:** Returns the newly created book information with a HTTP 200 response.
- **Example Response:**
  ```json
  {
    "id": 3,
    "name": "Zamanın Kısa Tarihi",
    "author": "Stephen Hawking",
    "publisher": "Alfa Yayıncılık",
    "quantity": 15,
    "store": {
      "id": 1,
      "name": "E-Adam BookStore",
      "createdAt": "2024-02-14T11:12:16.675Z",
      "updatedAt": "2024-02-14T11:12:16.675Z"
    },
    "createdAt": "2024-02-14T13:01:32.578Z",
    "updatedAt": "2024-02-14T13:01:32.578Z"
  }
  ```

#### List All Books

- **URL:** `GET /api/book`
- **Description:** Retrieves a list of all books.
- **Authorization:** Only users with the role of user can access this endpoint.
- **Query Parameters:**
  - `storeId` (number, optional): Filter books by store ID.
- **Response:** Returns a list of all books with a HTTP 200 response.
- **Example Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Steve Jobs",
      "author": "Walter Isaacson",
      "publisher": "Domingo Yayınevi",
      "quantity": 12,
      "createdAt": "2024-02-14T11:35:51.087Z",
      "updatedAt": "2024-02-14T11:35:51.087Z"
    },
    {
      "id": 2,
      "name": "İzafiyet Teorisi",
      "author": "Albert Einstein",
      "publisher": "Say Yayınları",
      "quantity": 5,
      "createdAt": "2024-02-14T11:44:05.355Z",
      "updatedAt": "2024-02-14T11:44:05.355Z"
    },
    {
      "id": 3,
      "name": "Zamanın Kısa Tarihi",
      "author": "Stephen Hawking",
      "publisher": "Mustafa Küpüşoğlu",
      "quantity": 15,
      "createdAt": "2024-02-14T13:01:32.578Z",
      "updatedAt": "2024-02-14T13:01:32.578Z"
    }
  ]
  ```

#### Get Book by ID

- **URL:** `GET /api/book/:id`
- **Description:** Retrieves a book by its ID.
- **Parameters:**
  - `id` (number): ID of the book.
- **Authorization:** Only users with the role of user can access this endpoint.
- **Response:** Returns the book information corresponding to the provided ID with a HTTP 200 response.
- **Example Response:**
  ```json
  {
    "id": 3,
    "name": "Zamanın Kısa Tarihi",
    "author": "Stephen Hawking",
    "publisher": "Mustafa Küpüşoğlu",
    "quantity": 15,
    "createdAt": "2024-02-14T13:01:32.578Z",
    "updatedAt": "2024-02-14T13:01:32.578Z"
  }
  ```

#### Update Book

- **URL:** `PATCH /api/book/:id`
- **Description:** Updates book information by its ID.
- **Parameters:**
  - `id` (number): ID of the book.
- **Authorization:** Only users with the role of store manager or admin can access this endpoint.
- **Request:**
  - **Body Parameters:**
    - `name` (string, optional): New name of the book.
    - `author` (string, optional): New author of the book.
    - `publisher` (string, optional): New publisher of the book.
    - `quantity` (number, optional): New quantity of the book in stock.
    - `storeId` (number, optional): New ID of the store where the book is available.
- **Response:** Returns the updated book information with a HTTP 200 response.
- **Example Response:**
  ```json
  {
    "id": 3,
    "name": "Zamanın Kısa Tarihi",
    "author": "Stephen Hawking",
    "publisher": "Alfa Yayıncılık",
    "quantity": 15,
    "createdAt": "2024-02-14T13:01:32.578Z",
    "updatedAt": "2024-02-14T13:01:32.578Z"
  }
  ```
