# django-emergencyfood.dev
![Status](https://github.com/gohanko/emergencyfood.dev/actions/workflows/build-and-release.yml/badge.svg)

Source code for my previous personal website. It's too much of a hassle to handle deployment, database backups and hosting costs for just a blogging site so I've decided to just use static site generators like hugo or jekyll.

## Deployment
```docker-compose -f ./infrastructure/docker/docker-compose.production.yml <build|up>```