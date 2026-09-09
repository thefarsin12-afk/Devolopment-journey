create database inventory_db;

use inventory_db;

CREATE TABLE inventory_(
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    category VARCHAR(100),
    quantity INT not null,
    price INT not null
);

select * from inventory_;