from requests import ConnectionError, get, HTTPError, Timeout


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
            # API returns status code 500 when no ontology exists for the id
            raise ValueError(f"No ontology found with ID '{id}'.")
        else:
            raise e
    except ConnectionError:
        raise ConnectionError("Failed to connect to the Ontology Lookup Service API.")
    except Timeout:
        raise Timeout("Request timed out.")

    return {
        "ID": data["ontologyId"],
        "Title": data["config"]["title"],
        "Description": data["config"]["description"],
        "Number of terms": data["numberOfTerms"],
        "Current status": data["status"],
    }
