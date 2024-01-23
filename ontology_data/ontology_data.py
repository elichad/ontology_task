from requests import ConnectionError, get, HTTPError


def fetch_ontology_data_by_id(id: str) -> dict:
    api = "http://www.ebi.ac.uk/ols4/api/"
    endpoint = f"ontologies/{id}"

    response = get(f"{api}{endpoint}")

    response.raise_for_status()

    return response.json()


def get_simple_ontology_data_by_id(id: str) -> dict:
    try:
        data = fetch_ontology_data_by_id(id)
    except HTTPError as e:
        if e.response.status_code == 500:
            # status code 500 used to indicate no such ontology exists
            raise ValueError(f"No ontology found with ID '{id}'.")
        else:
            raise e
    except ConnectionError:
        raise ConnectionError("Failed to connect to the Ontology Lookup Service API.")

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
