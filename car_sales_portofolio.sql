Select * From belajar.car_sales;

Select sum(Sales_in_thousands) as total_sales_in_thousands from belajar.car_sales;
Select sum(Sales_in_thousands* Price_in_thousands) as Revenue_in_thousands from belajar.car_sales;


Select Manufacturer, Model, Sales_in_thousands, Price_in_thousands,
round(sum(Sales_in_thousands * Price_in_thousands)) AS Total_revenue_in_thousands,
Case
When Sales_in_thousands >= 40 then 'Most Sales'
When Sales_in_thousands <= 20 then 'Least Sales'
else 'Follow Up'
END as Popularity,
Case
When round(sum(Sales_in_thousands * Price_in_thousands)) >= 500 then 'Most Provitable'
When round(sum(Sales_in_thousands * Price_in_thousands)) <= 200 then 'Least Provitable'
else 'Follow UP'
END as Profite
From belajar.car_sales
group by Manufacturer, Model;

UPDATE belajar.car_sales set Price_in_thousands = '3' where Model = 'CL'; 
UPDATE belajar.car_sales set Price_in_thousands = '2' where Model = 'Town & Country';

