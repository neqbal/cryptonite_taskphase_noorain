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
 SET
   @1=7
   @2='Matthew'
   @3='Miller'
   @4='matthew.miller@example.com'
   @5='789-012-3456'
   @6='Database Administrator'
   @7='DBA'
   @8='12:00:00'
   @9='14:00:00'

There are some transactions that appear shady 
These transactions happened on some other date but were inserted into the database at a later data

I read all the querry that manipulated the employees table and i found this

UPDATE `bank`.`employees`
WHERE
  @1=1
  @2='John'
  @3='Smith'
  @4='1985:05:15'
  @5='john.smith@example.com'
  @6='1234567890'
  @7='123 Main St'
  @8='Mumbai'
  @9='Maharashtra'
  @10='400001'
  @11=1
SET
  @1=1
  @2='John'
  @3='Darwin'
  @4='1990:01:01'
  @5='johndoe@example.com'
  @6='+1234567890'
  @7='123 Main St'
  @8='Anytown'
  @9='Anystate'
  @10='12345'
  @11=1
at 80520
#240227 15:31:29 server id 1  end_log_pos 80551 CRC32 0xebf8ef83 	Xid = 2928

This looks fishy. The name was changed and address was also changed to nowhere \
This also happened during the working hours of the traiter Matthew \
Therefore Jhon darwin could be the outsider

I dont know what the flag format is and i cannot find anything else in this log file
