# DRF API Manual Testing

## `/auth/users/` POST (User Registration)
- Send a POST request, get a 201 response.
- Send a POST request with an existing username, get a 400 response.

## `/auth/token/login/` POST (User Login)
- Send a POST request with correct credentials, get a 200 response.
- Send a POST request with incorrect credentials, get a 400 response.

## `/posts/` POST (Create a Post)
- Send a POST request with authentication, get a 201 response.
- Send a POST request without authentication, get a 401 response.

## `/comments/` POST (Create a Comment)
- Send a POST request with authentication, get a 201 response.
- Send a POST request without authentication, get a 401 response.

## `/posts/<id>/` DELETE (Delete a Post)
- Send a DELETE request as the author with authentication, get a 204 response.
- Send a DELETE request without authentication, get a 401 response.

## `/posts/<id>/` PUT (Update a Post)
- Send a PUT request as the author with authentication, get a 200 response.
- Send a PUT request without authentication, get a 401 response.

## `/todos/<id>/` GET (Retrieve a Todo)
- Send a GET request as the author with authentication, get a 200 response.
- Send a GET request without authentication, get a 401 response.

## `/todos/<id>/` PUT (Update a Todo)
- Send a PUT request as the author with authentication, get a 200 response.
- Send a PUT request without authentication, get a 401 response.

## `/todos/<id>/` DELETE (Delete a Todo)
- Send a DELETE request as the author with authentication, get a 204 response.
- Send a DELETE request without authentication, get a 401 response.
