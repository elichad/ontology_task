from requests import ConnectionError, get, HTTPError, Timeout


def fetch_ontology_data_by_id(id: str) -> dict:
    """Fetch ontology data from the Ontology Lookup Service API.

    id (str): An ontology ID, for example "efo".

    If successful, returns a JSON representation of the ontology.
    Raises ValueError if the ontology could not be found.
    Raises HTTPError if the request returns an unknown error response.
    Raises ConnectionError or Timeout if the request fails to connect.
    """
    api = "http://www.ebi.ac.uk/ols4/api/"
    endpoint = f"ontologies/{id}"

    try:
        response = get(f"{api}{endpoint}")
        response.raise_for_status()
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

    return response.json()


def get_simple_ontology_data_by_id(id: str) -> dict:
    """Get a simple representation of an ontology using its ID.

    Wraps fetch_ontology_data_by_id to pick out desired data.
    """
    data = fetch_ontology_data_by_id(id)

    return {
        "ID": data["ontologyId"],
        "Title": data["config"]["title"],
        "Description": data["config"]["description"],
        "Number of terms": data["numberOfTerms"],
        "Current status": data["status"],
    }
