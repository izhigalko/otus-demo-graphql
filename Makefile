.PHONY=schema
schema:
	python manage.py graphql_schema --out schema.graphql

venv:
	python -m venv ./venv
	./venv/bin/pip install -r requirements.txt

otus_graphql/books_pb2_grpc.py otus_graphql/books_pb2.py: venv
	./venv/bin/python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/otus_graphql/books.proto

front/otus_graphql/books_grpc_web_pb.js front/otus_graphql/books_pb.js: venv
	protoc -I./proto --js_out=import_style=commonjs:./front \
		--grpc-web_out=import_style=commonjs,mode=grpcwebtext:./front ./proto/otus_graphql/books.proto


.PHONY=get_schema
get_schema:
	grpc_cli ls localhost:50051 -l

.PHONY=get_books_req
get_books_req:
	grpc_cli call localhost:50051 GetBooks ""

.PHONY=proto
proto: otus_graphql/books_pb2_grpc.py otus_graphql/books_pb2.py front/otus_graphql/books_grpc_web_pb.js front/otus_graphql/books_pb.js

front/dist:
	@npm --prefix front i
	@mkdir ./front/dist
	./front/node_modules/.bin/webpack-cli -o ./front/dist/main.js ./front/client.js
