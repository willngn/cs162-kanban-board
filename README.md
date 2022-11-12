# Kanban Board

## Introduction

This is a very ugly and basic Kanban board built in HTML, CSS for frontend and Flask for backed. It helps us:
1. Add a new task and choose its stage - to do, doing, done
2. Move tasks around - change the task status
3. Delete a task

## Project Structure
```
cs162-kanban-board
│   README.md
│   requirements.txt    
│   app.py
|
|
└───src
|   │____ templates
|       |   index.html
|
|   |____ static       
|       |   style.css
|
|   |____ __init__.py
|   |____ api.py
|   |____ kanban.db
|   |____ models.py
|
└───tests
|   │____ __init__.py
|       
|
|   |____ testing.py       
```
## Installation

Remember to be at the root director, run the following in your terminal:
### MacOS
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```
### Windows
```
python3 -m venv venv
venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3 app.py
```
## Testing
Run the following in your terminal:
```
python3 -m unittest discover test
```

Code Coverage:

```
Name                Stmts   Miss  Cover   Missing
-------------------------------------------------
src/__init__.py        12      0   100%
src/api.py             29      1    97%   36
src/models.py          12      1    92%   12
tests/__init__.py      19      1    95%   30
tests/testing.py       59      1    98%   94
-------------------------------------------------
TOTAL                 131      4    97%
```