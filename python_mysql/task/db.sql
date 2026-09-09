create database inventory__db;
use inventory__db;

CREATE TABLE inventory(
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    sku VARCHAR(50) UNIQUE NOT NULL,
    category VARCHAR(50) NOT NULL,
    quantity INT DEFAULT 0,
    reorder_level INT DEFAULT 10,
    unit_price DECIMAL(10, 2) DEFAULT 0.00,
    storage_zone VARCHAR(20) DEFAULT 'Zone-A',
    status VARCHAR(20) DEFAULT 'In Stock',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from inventory;