# Django Backend API Authentication Scheme

This project is a backend API authentication scheme implemented in Python using Django and Django Rest Framework. It leverages the power of `django-rest-knox` and `dj-rest-auth` to create a secure and robust token-based authentication system.

## Overview

Authentication is a critical aspect of any web application, and this project aims to provide a reliable solution for handling user authentication in your Django-based API. It utilizes `django-rest-knox` to generate and manage secure tokens for user sessions and `dj-rest-auth` to streamline authentication endpoints.

## Why Knox Instead of the Regular DRF Token Class?

When it comes to implementing token-based authentication in Django Rest Framework (DRF), the built-in `TokenAuthentication` class is a commonly used choice. However, our project has chosen to leverage `knox` authentication for several reasons, as outlined below:

1. **Multiple Tokens per User:** In DRF, tokens are limited to one per user, making it challenging to securely handle sign-ins from multiple devices. With `knox`, each client can have its unique token, which is deleted on the server side upon client logout. This provides a more flexible and secure approach, allowing users to remain logged in across various devices.

2. **Server-Side Logout:** In scenarios where a server-side logout is required (e.g., revoking all tokens for a specific user), `knox` allows for the removal of all tokens associated with a logged-in client. This feature ensures stricter control over user sessions and enhances security.

3. **Token Storage Security:** DRF tokens are stored unencrypted in the database, which poses a security risk in the event of a database breach. In contrast, `knox` tokens are only stored in an encrypted form, significantly reducing the potential impact of a security breach. Even if an attacker gains access to the database, they cannot readily use stolen credentials.

4. **Token Expiry:** While DRF tokens track their creation time, they lack an inbuilt mechanism for token expiration. `knox` tokens, on the other hand, offer the flexibility to configure token expiry in the app settings. By default, `knox` tokens expire after 10 hours, providing an additional layer of security.

In summary, the `knox` authentication scheme offers enhanced security, better session management, and improved flexibility compared to the default DRF token class. These advantages make it an excellent choice for building a secure and reliable authentication system in your Django-based API.

## Integrating Facebook Login

As part of our project's future roadmap, we plan to integrate Facebook login into the authentication scheme using dj-rest-auth's ability to integrate with Facebook. Stay tuned for updates and documentation on this exciting feature!

## Features

- Token-based authentication for user sessions.
- Seamless integration of `django-rest-knox` for secure token management.
- Easy setup and usage of authentication endpoints with `dj-rest-auth`.
- Future plans to integrate Facebook login for user convenience.

## Installation

in progress...

