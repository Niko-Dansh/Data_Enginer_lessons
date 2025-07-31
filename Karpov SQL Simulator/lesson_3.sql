-- Задача 7.
SELECT name, SPLIT_PART(UPPER(name), ' ', 1) AS first_word, price
FROM products
ORDER BY name;

-- Задача 8.
