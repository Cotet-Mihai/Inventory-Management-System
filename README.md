# Inventory Management System (IVM)

## Project Overview

The **Inventory Management System (IVM)** is a web-based application designed to streamline warehouse management. It enables users to track product availability across multiple warehouses, manage inventory levels, and facilitate the transfer of products between warehouses. This system provides a comprehensive solution for efficient inventory tracking and data management.

---

## Key Features

- **Warehouse Management**  
  Add, view, and manage multiple warehouses with their locations and names.
  
- **Product Management**  
  Manage product details (name, quantity, etc.) for each warehouse.

- **Product Transfers**  
  Record product transfers between warehouses, including source, destination, and quantities.

- **User Authentication**  
  Secure login and access management to ensure proper data handling.

---

## Technologies Used

- **Backend**: [Flask](https://flask.palletsprojects.com/) - A Python web framework for building the server-side application.
- **Database**: [MySQL](https://www.mysql.com/) - Relational database management system for storing warehouse and product data.
- **Frontend**:  
  - **HTML** for structure
  - **CSS** for styling
  - **JavaScript** for dynamic behavior
  
---

## Database Structure

The project uses a MySQL database with the following four tables:

### 1. `users` Table

This table stores user credentials for the application.

| Field     | Type          | Null | Key | Default | Extra            |
|-----------|---------------|------|-----|---------|------------------|
| `id`      | `int`         | NO   | PRI | NULL    | `auto_increment` |
| `username`| `varchar(255)`| YES  |     | NULL    |                  |
| `password`| `varchar(255)`| YES  |     | NULL    |                  |

- **`id`**: Unique identifier for each user.
- **`username`**: The username for login purposes.
- **`password`**: The encrypted password for authentication.

---

### 2. `items` Table

This table stores information about the items in the inventory.

| Field     | Type          | Null | Key | Default | Extra            |
|-----------|---------------|------|-----|---------|------------------|
| `id`      | `int`         | NO   | PRI | NULL    | `auto_increment` |
| `category`| `varchar(255)`| NO   |     | NULL    |                  |
| `name`    | `varchar(255)`| NO   |     | NULL    |                  |
| `price`   | `decimal(10,2)`| YES |     | NULL    |                  |

- **`id`**: Unique identifier for each item.
- **`category`**: The category of the item.
- **`name`**: The name of the item.
- **`price`**: The price of the item.

---

### 3. `warehouses` Table

This table stores the warehouse details.

| Field     | Type          | Null | Key | Default | Extra            |
|-----------|---------------|------|-----|---------|------------------|
| `id`      | `int`         | NO   | PRI | NULL    | `auto_increment` |
| `name`    | `varchar(255)`| NO   |     | NULL    |                  |
| `address` | `varchar(255)`| NO   |     | NULL    |                  |

- **`id`**: Unique identifier for each warehouse.
- **`name`**: The name of the warehouse.
- **`address`**: The address of the warehouse.

---

### 4. `item_transfer` Table

This table stores information about the transfers of items between warehouses.

| Field              | Type          | Null | Key | Default | Extra            |
|--------------------|---------------|------|-----|---------|------------------|
| `transfer_id`      | `int`         | NO   | PRI | NULL    | `auto_increment` |
| `item_id`          | `int`         | NO   | MUL | NULL    |                  |
| `warehouse_id`     | `int`         | NO   | MUL | NULL    |                  |
| `user_id`          | `int`         | NO   | MUL | NULL    |                  |
| `transfer_datetime`| `datetime`    | NO   |     | NULL    |                  |
| `transfer_type`    | `varchar(255)`| NO   |     | NULL    |                  |

- **`transfer_id`**: Unique identifier for each transfer.
- **`item_id`**: The ID of the item being transferred (foreign key referencing `items`).
- **`warehouse_id`**: The ID of the warehouse involved in the transfer (foreign key referencing `warehouses`).
- **`user_id`**: The ID of the user performing the transfer (foreign key referencing `users`).
- **`transfer_datetime`**: The date and time of the transfer.
- **`transfer_type`**: Type of the transfer (e.g., inbound or outbound).

---

This structure allows for efficient tracking of items across different warehouses and the management of product transfers between them.

