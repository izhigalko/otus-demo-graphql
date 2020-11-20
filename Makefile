.PHONY=schema
schema:
	python manage.py graphql_schema --out schema.graphql