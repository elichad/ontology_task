from requests import HTTPError, ConnectionError, Timeout
from unittest import TestCase
from unittest.mock import patch

from ontology_data.ontology_data import (
    fetch_ontology_data_by_id,
    get_simple_ontology_data_by_id,
)


class TestFetchOntologyDataById(TestCase):
    def test_fetch_works_with_valid_id(self):
        # Arrange
        id = "agro"

        # Act
        result = fetch_ontology_data_by_id(id)

        # Assert
        self.assertEqual("agro", result["ontologyId"])
        self.assertEqual("Agronomy Ontology", result["config"]["title"])

    def test_fetch_raises_httperror_with_invalid_id(self):
        # Arrange
        id = "invalid"

        # Act & Assert
        with self.assertRaises(ValueError) as ctx:
            fetch_ontology_data_by_id(id)

        self.assertEqual("No ontology found with ID 'invalid'.", str(ctx.exception))

    @patch("ontology_data.ontology_data.get")
    def test_fetch_connection_error(self, mock_requests_get):
        # Arrange
        id = "agro"
        mock_requests_get.side_effect = ConnectionError

        # Act & Assert
        with self.assertRaises(ConnectionError) as ctx:
            fetch_ontology_data_by_id(id)

        self.assertEqual(
            "Failed to connect to the Ontology Lookup Service API.", str(ctx.exception)
        )

    @patch("ontology_data.ontology_data.get")
    def test_fetch_timeout(self, mock_requests_get):
        # Arrange
        id = "agro"
        mock_requests_get.side_effect = Timeout

        # Act & Assert
        with self.assertRaises(Timeout) as ctx:
            fetch_ontology_data_by_id(id)

        self.assertEqual("Request timed out.", str(ctx.exception))


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
        # Arrange
        id = "invalid"

        # Act & Assert
        with self.assertRaises(ValueError) as ctx:
            get_simple_ontology_data_by_id(id)

        self.assertEqual("No ontology found with ID 'invalid'.", str(ctx.exception))
