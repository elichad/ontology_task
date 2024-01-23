import requests


def fetch_ontology_data_by_id(id: str) -> dict:
    api = "http://www.ebi.ac.uk/ols4/api/"
    endpoint = f"ontologies/{id}"

    response = requests.get(f"{api}{endpoint}")
    json = response.json()

    return json


def get_simple_ontology_data_by_id(id: str) -> dict:
    data = fetch_ontology_data_by_id(id)

    return {
        "ID": data["ontologyId"],
        "Title": data["config"]["title"],
        "Description": data["config"]["description"],
        "Number of terms": data["numberOfTerms"],
        "Current status": data["status"],
    }


def print_data(data: dict) -> None:
    for k, v in data.items():
        print(f"{k}: {v}")


info = get_simple_ontology_data_by_id("agro")
print_data(info)
