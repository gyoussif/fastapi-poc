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
uvicorn main:app --reload
```