
\! echo "
What is the sales to total production rate?
"
SELECT body_type, Sales*100/Total AS 'margin' FROM Body_data2024;

\! echo "
Which body type sales are the highest?
"
SELECT body_type FROM Body_data2024 ORDER BY Sales DESC LIMIT 1;

\! echo "
Total unsold units by body type?
"
SELECT body_type, (Total - Sales) AS unsold_units FROM Body_data2024;

\! echo "
What is the ratio of sales to unsold units for each body type?
"
SELECT body_type, Sales/(Total - Sales) AS sale_ratio FROM Body_data2024;

\! echo "
What is the total percentage of sales contributed by the top 5 OEMs?
"
SELECT SUM(a.perc_sales) AS 'Top5 percentage' FROM (SELECT Make, perc_sales FROM OEM_data ORDER BY Sales DESC LIMIT 5) AS a;

\! echo "
How many units are unsold by the top 5 OEM?
"
SELECT Make, (Total - Sales) AS 'unsold_units' FROM OEM_data ORDER BY Sales DESC LIMIT 5;

\! echo "
Total unsold units in the market in 2024?
"
SELECT SUM(Total - Sales) AS 'total_unsold' FROM OEM_data ORDER BY total_unsold ASC;

\! echo "
How many maruti cars were sold compared to Kia in 2024
"
SELECT a.Sales/b.Sales FROM OEM_data AS a WHERE Make='Maruti' INNER JOIN on='Make' FROM OEM_data AS b WHERE Make='Kia';
