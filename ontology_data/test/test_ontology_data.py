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

    # TODO: test invalid IDs


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

    # TODO: test invalid IDs
