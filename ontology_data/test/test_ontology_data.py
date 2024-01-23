from requests import HTTPError
from unittest import TestCase

from ontology_data.ontology_data import (
    fetch_ontology_data_by_id,
    get_simple_ontology_data_by_id,
    print_data,
)


class TestFetchOntologyDataById(TestCase):
    def test_fetch_works_with_valid_id(self):
        id = "agro"
        result = fetch_ontology_data_by_id(id)
        self.assertEqual("agro", result["ontologyId"])
        self.assertEqual("Agronomy Ontology", result["config"]["title"])

    def test_fetch_raises_httperror_with_invalid_id(self):
        id = "invalid"

        with self.assertRaises(HTTPError) as ctx:
            fetch_ontology_data_by_id(id)

        self.assertEqual(500, ctx.exception.response.status_code)

    def test_fetch_timeout(self):
        # TODO: mock call to force a timeout
        pass


class TestGetSimpleOntologyData(TestCase):
    def test_works_with_valid_id(self):
        # Arrange
        id = "agro"
        expected = {
            "ID": "agro",
            "Title": "Agronomy Ontology",
            "Description": "AgrO is an ontlogy for representing agronomic practices, techniques, variables and related entities",
            "Number of terms": 4162,
            "Current status": "LOADED",
        }

        # Act
        result = get_simple_ontology_data_by_id(id)

        # Assert
        self.assertDictEqual(expected, result)

    def test_raises_valueerror_with_invalid_id(self):
        id = "invalid"

        with self.assertRaises(ValueError) as ctx:
            get_simple_ontology_data_by_id(id)

        self.assertEqual("No ontology found with ID 'invalid'.", str(ctx.exception))

    def test_raises_exception_with_timeout(self):
        # TODO: mock call to force a timeout
        pass
