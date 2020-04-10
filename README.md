# django-api-template
    Template to build DRF APIs


# Notes
    "*" represents `required`


# Getting Started Part 1: Overview & File Structure

    I built this API as a template for creating a Django
    backend service for social media applications.

    Anyone cloning this repository can convert this application
    into a standalone API without authentication, however, I
    included the Authentication app and User model to provide
    some sample structure as well!


# Getting Started Part 2: Migrations

TODO


# Getting Started Part 3:

TODO

# Authentication App

    Authentication: a provided API View for authenticating users.


    GET: Login
    Route: /api/auth/
    Description: The GET request is used to
    login users. When successful, this request
    returns the requested user account.
    Programmagically, to login, you are GETting
    the user account with which you logged
    in successfully.
    When unsuccessful, you receive an array
    of the broken fields. Display that error
    however you choose.

    Future:
        - [ ] Provide clarity on broken fields.
        - [ ] Two factor authentication

    ```js
        {
            "username": String (One required),
            "email": String (One required),
            *"password": String,
        }

        The GET/Login request must include a password field and
        one of the "One Required" fields to authenticate
        users. Users with phone numbers will receive two
        factor authentication.

        {response
            "first_name": String,
            "last_name": String,
            "username": String,
            "email": String,
        }
    ```


    POST: Sign Up
    Route: /api/auth
    Description: The POST request is used to
    create user accounts. When successful, this
    request returns the newly created user
    account.
    To sign up, programmagically, you are POSTing
    a compatible user object to save/authenticate
    into the database.

    Future: ?

    ```js
        {request
            *"first_name": String,
            *"last_name": String,
            #"username": String,
            #"email": String,
            *"password": String,
        }

        The POST/Sign Up request must include a first name,
        last name, usernane, email, password.

        {response
            "first_name": String,
            "last_name": String,
            "username": String,
            "email": String,
        }
    ```


    PUT: Misc
    Route: /api/auth
    Description: The PUT request is used to
    handle two factor auth and other misc tasks.

    Future: ?

    ```js
        {request
            *"first_name": String,
            *"last_name": String,
            *"username": String,
            *"phone": String,
            *"password": String,
        }

        The POST/Sign Up request must include a first name,
        last name, and password.

        {response
            "first_name": String,
            "last_name": String,
            "username": String,
            "email": String,
        }
    ```


# User Model

    Every model extends the Base Model which includes two
    very important fields. The first field, `guid` is used
    as a secondary primary key for each model.

    Utilizing the `guid` key feasibly unlocks the secret
    door with you make need to reference/open.

    The second field is the active key. The active key
    works as a soft delete for objects, so that we can
    reference them later if needed. Set active to false
    when you don't want that object to be returned by
    the API, delete the object when you wish it no longer
    existed.

    The User model provides most of the attributes users
    would have in an application.
    ```js
        {
            *first_name:     CharField
            *last_name:      CharField
            *username:       CharField
            email:          EmailField
            *password:       CharField
            phone:          CharField
            date_joined:    DateField
            online:         BooleanField
        }
    ```