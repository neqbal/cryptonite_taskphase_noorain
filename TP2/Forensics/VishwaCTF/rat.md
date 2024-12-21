The number 789-012-3456

CREATE TABLE instructors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    bio TEXT
)

CREATE TABLE classes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    instructor_id INT,
    start_time DATETIME,
    end_time DATETIME,
    CONSTRAINT fk_instructor
        FOREIGN KEY (instructor_id)
        REFERENCES instructors(id)
        ON DELETE SET NULL
)

CREATE TABLE schedule (
    id INT AUTO_INCREMENT PRIMARY KEY,
    class_id INT,
    day_of_week VARCHAR(20),
    start_time TIME,
    end_time TIME,
    CONSTRAINT fk_class
        FOREIGN KEY (class_id)
        REFERENCES classes(id)
        ON DELETE CASCADE
)
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    email VARCHAR(100),
    phone_number VARCHAR(15),
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20)
)
CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    account_type ENUM('Checking', 'Savings', 'Loan'),
    balance DECIMAL(15, 2),
    open_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    transaction_type ENUM('Deposit', 'Withdrawal', 'Transfer'),
    amount DECIMAL(15, 2),
    transaction_date DATETIME,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
)
CREATE TABLE loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    loan_amount DECIMAL(15, 2),
    interest_rate DECIMAL(5, 2),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
CREATE TABLE cards (
    card_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    card_type ENUM('Debit', 'Credit'),
    card_number VARCHAR(20),
    expiry_date DATE,
    cvv VARCHAR(5),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
CREATE TABLE branches (
    branch_id INT AUTO_INCREMENT PRIMARY KEY,
    branch_name VARCHAR(100),
    branch_address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20)
)
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    email VARCHAR(100),
    phone_number VARCHAR(15),
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    branch_id INT,
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
)
CREATE TABLE maintainers (
    maintainer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone_number VARCHAR(15),
    department VARCHAR(100),
    role VARCHAR(50),
    in_time TIME,
    out_time TIME
)

INSERT INTO `bank`.`maintainers`
### SET
###   @1=7
###   @2='Matthew'
###   @3='Miller'
###   @4='matthew.miller@example.com'
###   @5='789-012-3456'
###   @6='Database Administrator'
###   @7='DBA'
###   @8='12:00:00'
###   @9='14:00:00'

There are some transactions that appear shady 
These transactions happened on some other date but were inserted into the database at a later data


