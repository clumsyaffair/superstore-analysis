CREATE DATABASE if not EXISTS python_db;
use python_db;
CREATE TABLE superstore(
Row_ID int,
Order_ID VARCHAR(50),
Order_Date Date,
Ship_Date Date,
Ship_Mode VARCHAR(50),
Customer_ID VARCHAR(50),
Customer_Name VARCHAR(100),
Segment VARCHAR(50),
Country VARCHAR(50),
City VARCHAR(50),
State VARCHAR(50),
Postal_Code int,
Region VARCHAR(50),
Product_ID VARCHAR(50),
Category VARCHAR(50),
Sub_Category VARCHAR(50),
Product_Name VARCHAR(50),
Sales FLOAT,
Quantity int,
Discount FLOAT,
Profit FLOAT,
Ship_Duration int,
Profit_Margin FLOAT
)
