DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS bugs;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    user_type VARCHAR(255)   
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE bugs (
    id SERIAL PRIMARY KEY,
    short_name VARCHAR(255),
    description VARCHAR(255),
    product_id INT NOT NULL REFERENCES products(id) ,
    first_reported VARCHAR(255)
);

CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    bug_id INT NOT NULL REFERENCES bugs(id),
    product_id INT NOT NULL REFERENCES products(id),
    date_subm VARCHAR(255), 
    user_id INT NOT NULL REFERENCES users(id),
    ticket_status VARCHAR(255)
);