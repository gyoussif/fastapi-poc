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
├── src
│   ├──main.py #root of the project, which inits the FastAPI app
├── tests/
├── .env
├── .gitignore
├── poetry.lock
├── pyproject.toml
├── README.md
```