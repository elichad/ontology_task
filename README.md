# ontology_task

Coding exercise to fetch data from the Ontology Lookup Service (OLS) API.

## Installation

This project uses Python. It has been tested with Python 3.11 on Linux (Ubuntu WSL).

Clone the repository:

```bash
git clone git@github.com:elichad/ontology_task.git
cd ontology_task
```

Install dependencies:

```bash
pip install -r requirements.txt
```

(Optional) Run tests:

```bash
python -m unittest
```

## Command-line usage

In the `ontology_data` directory, run the `main.py` program to fetch data about an ontology:

```bash
cd ontology_data
python main.py <id>
```

For example, to fetch the ontology with ID "agro":

```bash
python main.py agro
```

## Docker container usage

In the root directory of the repo, build and run the container, passing the ontology ID as a command line argument in the same way as [Command-line usage](#command-line-usage):

```bash
docker build --tag ontology_task .
docker run ontology_task <id>
```

## Programmatic usage

In a Python script (if this were distributed as a package):

```python
from ontology_data.ontology_data import get_simple_ontology_data_by_id

# Get data for ontology with ID "agro"
id = "agro"
data = get_simple_ontology_data_by_id(id)
```
