CREATE TABLE authors (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(100),
    author_id INT,
    publication_year INT,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE sales (
    id INT PRIMARY KEY,
    book_id INT,
    quantity INT,
    FOREIGN KEY (book_id) REFERENCES books(id)
);

INSERT INTO authors (id, first_name, last_name) VALUES
(1, 'George', 'Orwell'),
(2, 'J.K.', 'Rowling'),
(3, 'J.R.R.', 'Tolkien');

INSERT INTO books (id, title, author_id, publication_year) VALUES
(1, '1984', 1, 1949),
(2, 'Harry Potter and the Philosopher''s Stone', 2, 1997), 
(3, 'The Hobbit', 3, 1937);


INSERT INTO sales (id, book_id, quantity) VALUES
(1, 1, 5),
(2, 2, 10),
(3, 3, 8);

SELECT
    books.title,
    authors.first_name,
    authors.last_name
FROM
    books
INNER JOIN
    authors ON books.author_id = authors.id;
SELECT
    authors.first_name,
    authors.last_name,
    books.title
FROM
    authors
LEFT JOIN
    books ON authors.id = books.author_id;

SELECT
    books.title,
    authors.first_name,
    authors.last_name
FROM
    books
RIGHT JOIN
    authors ON books.author_id = authors.id;
