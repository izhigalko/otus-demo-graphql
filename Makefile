.PHONY=schema
schema:
	python manage.py graphql_schema --out schema.graphql

venv:
	python -m venv ./venv
	./venv/bin/pip install -r requirements.txt

otus_graphql/books_pb2_grpc.py otus_graphql/books_pb2.py: venv
	./venv/bin/python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/otus_graphql/books.proto

.PHONY=get_schema
get_schema:
	grpc_cli ls localhost:50051 -l

.PHONY=get_books_req
get_books_req:
	grpc_cli call localhost:50051 GetBooks ""

