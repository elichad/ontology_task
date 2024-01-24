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

Run the program to fetch data about an ontology:

```bash
cd ontology_data
python main.py <id>
```

For example, to fetch the ontology with ID "agro":

```bash
python main.py agro
```

Run tests:

```bash
python -m unittest
```
