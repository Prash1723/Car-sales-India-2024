
# What is the sales to total production rate?
SELECT body_type, Sales*100/Total AS 'margin' FROM Body_type2024;

# Which body type sales are the highest?
SELECT body_type FROM Body_type2024 ORDER BY Sales DESC LIMIT 1;

# Total unsold units by body type?
SELECT body_type, (Total - Sales) AS unsold_units FROM Body_type2024;

# What is the ratio of sales to unsold units for each body type?
SELECT body_type, Sales/(Total - Sales) AS sale_ratio FROM Body_type2024;

# What is the total percentage of sales contributed by the top 5 OEMs?
SELECT sum(a.perc_sales) FROM (SELECT Make, perc_sales FROM OEM_data SORT BY DESC LIMIT 5) AS a;
