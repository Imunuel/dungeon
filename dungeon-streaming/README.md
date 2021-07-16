# Dungeon of Python (Streaming)

A service for monitoring progress of a user by appointed mentor. 
Streaming service also provides main features of the game to a user.   

## Configuration
Configuration located in `envs/.env`, for examples see `envs/.env.ci`

## Linting

```sh
$ flake8
$ isort .
```

## Docker

### Containers management

#### Formatted output
```shell
$ docker ps -a --format "{{.ID}}: {{.Image}} {{.Names}} {{.Size}}"
```
### Building

```bash
$ docker-compose -f local.yml up
```

or 
```bash
$ docker-compose -f local.yml build ...
```
if you want to rebuild specific container.
