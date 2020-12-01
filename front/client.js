import {models, service} from './otus_graphql'

const booksClient = new service.BooksServiceClient('http://localhost:8080', null, null);
const req = new models.Empty();

const booksStream = booksClient.getBooks(req, {});

booksStream.on('data', (response) => {
    console.log(response);
});
