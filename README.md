###
Property Listings App (Django + PostgreSQL + Redis Caching)

This project is a Django-based property listing application that demonstrates how to use PostgreSQL as the database and Redis as a cache backend to optimize performance.

It covers:

Django project setup

Dockerized PostgreSQL and Redis

Response caching with @cache_page

Queryset caching with Redis (low-level cache API)

Cache invalidation with Django signals

Redis cache hit/miss metrics

Features

Create and manage property listings.

PostgreSQL as the relational database.

Redis as a caching layer for performance.

Caching strategies:

Full response caching (@cache_page).

Queryset caching (cache.set / cache.get).

Automatic cache invalidation on DB changes.

Monitoring Redis hit/miss metrics.

Tech Stack

Backend: Django (Python)

Database: PostgreSQL (Dockerized)

Cache: Redis (Dockerized, via django-redis)

Containerization: Docker & Docker Compose

###