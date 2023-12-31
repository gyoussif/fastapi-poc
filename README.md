# fastapi-poc
## Create virtual environment
```
pip install virtualenv
virtualenv .venv
.venv\Scripts\activate
```

## Package and dependency management
```
pip install poetry
poetry init
poetry install
```

## Create fastapi project
```
poetry add fastapi uvicorn[standard]
uvicorn src.main:app --reload
```

## Project Structure
```
fastapi-poc
├── scripts
│   ├── coverage.py  # script to run linting and coverage check
├── src
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── cart.py  # API controller for the cart
│   ├── config.py  # global configs
│   ├── constants.py  # global constants
│   ├── logger.py  # logging middleware
│   ├── models.py  # global models
│   ├── schemas.py  # global schemas using pydantic
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── schemas.py
│   ├── database.py  # db connection related stuff
│   ├──main.py #root of the project, which inits the FastAPI app
├── tests/
│   ├── __init__.py
│   ├── cart_tests.py  # unittest for the cart APIs
├── .env
├── .gitignore
├── poetry.lock
├── pyproject.toml
├── README.md
```

## Coverage

```
bash scripts/coverage.sh
```

## Done
- virtual env
- Package and dependency management
- Basic Structure
- Model
- CRUD Operations
- Sql alchemy: ORM
- Pydantic: Data parsing and validation
- Docs Swagger works with VPN or we can host the static files locally following this documentation https://fastapi.tiangolo.com/advanced/extending-openapi/?h=#self-hosting-javascript-and-css-for-docs
- Unit test
- Script
- Logging Middleware
- env variables
- Routing

## TODO
- JWT auth
- Docker
- Queue messages (kafka)
- Caching (redis)
- Monitoring (elk) 
