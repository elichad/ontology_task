from ontology_data import get_simple_ontology_data_by_id
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch data about an ontology using its ID."
    )
    parser.add_argument(
        "ontology_id",
        metavar="id",
        type=str,
        help="The ontology ID",
    )
    args = parser.parse_args()

    data = get_simple_ontology_data_by_id(args.ontology_id)

    for k, v in data.items():
        print(f"{k}: {v}")
