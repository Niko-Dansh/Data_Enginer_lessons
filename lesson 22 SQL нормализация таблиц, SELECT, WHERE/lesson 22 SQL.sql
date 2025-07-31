-- 1) Core (business) entities
CREATE TABLE authors (
                         author_id   SERIAL    PRIMARY KEY,
                         birthdate   DATE      NOT NULL,
                         name        VARCHAR(50) NOT NULL,
                         surname     VARCHAR(50) NOT NULL
);

CREATE TABLE genres (
                        genre_id    SERIAL    PRIMARY KEY,
                        genre_name  VARCHAR(50) NOT NULL
);

CREATE TABLE ban_types (
                           ban_id       SERIAL     PRIMARY KEY,
                           ban_name     VARCHAR(50) NOT NULL,
                           law_reference VARCHAR(255)
);

CREATE TABLE books (
                       book_id      SERIAL     PRIMARY KEY,
                       book_name    VARCHAR(255) NOT NULL,
                       book_series  VARCHAR(100),
                       genre_id     INTEGER    NOT NULL REFERENCES genres(genre_id),
                       ban_id       INTEGER    REFERENCES ban_types(ban_id)
);

CREATE TABLE regions (
                         region_id   SERIAL      PRIMARY KEY,
                         region_name VARCHAR(100) NOT NULL
);

-- 2) Historization (Type-2) tables
CREATE TABLE author_history (
                                auth_hist_id SERIAL     PRIMARY KEY,
                                author_id    INTEGER    NOT NULL REFERENCES authors(author_id),
                                valid_from   TIMESTAMPTZ NOT NULL,
                                valid_to     TIMESTAMPTZ NOT NULL,
                                UNIQUE (author_id, valid_from)
);

CREATE TABLE book_history (
                              book_hist_id SERIAL     PRIMARY KEY,
                              book_id      INTEGER    NOT NULL REFERENCES books(book_id),
                              valid_from   TIMESTAMPTZ NOT NULL,
                              valid_to     TIMESTAMPTZ NOT NULL,
                              UNIQUE (book_id, valid_from)
);

CREATE TABLE genre_history (
                               gen_hist_id  SERIAL     PRIMARY KEY,
                               genre_id     INTEGER    NOT NULL REFERENCES genres(genre_id),
                               valid_from   TIMESTAMPTZ NOT NULL,
                               valid_to     TIMESTAMPTZ NOT NULL,
                               UNIQUE (genre_id, valid_from)
);

CREATE TABLE ban_history (
                             ban_hist_id  SERIAL     PRIMARY KEY,
                             ban_id       INTEGER    NOT NULL REFERENCES ban_types(ban_id),
                             valid_from   TIMESTAMPTZ NOT NULL,
                             valid_to     TIMESTAMPTZ NOT NULL,
                             UNIQUE (ban_id, valid_from)
);

-- 3) Facts
CREATE TABLE f_book_sales (
                              sale_id       SERIAL      PRIMARY KEY,
                              book_id       INTEGER     NOT NULL REFERENCES books(book_id),
                              sale_date     DATE        NOT NULL,
                              quantity_sold INTEGER     NOT NULL,
                              revenue       NUMERIC(12,2),
                              region_id     INTEGER     REFERENCES regions(region_id),
                              region INT NOT NULL
);

CREATE TABLE f_book_storage (
                                storage_id    SERIAL      PRIMARY KEY,
                                book_id       INTEGER     NOT NULL REFERENCES books(book_id),
                                storage_count INTEGER,
                                record_date   DATE        NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE f_leaderboard (
                               rank_id       SERIAL      PRIMARY KEY,
                               book_id       INTEGER     NOT NULL REFERENCES books(book_id),
                               rank          INTEGER     NOT NULL,
                               rank_date     DATE        NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE f_book_authors (
                                ba_id         SERIAL      PRIMARY KEY,
                                book_id       INTEGER     NOT NULL REFERENCES books(book_id),
                                author_id     INTEGER     NOT NULL REFERENCES authors(author_id)
);


DROP TABLE d_ban_types_3nf, d_book_history_3nf, d_genre_history_3nf, f_book_sales_3nf CASCADE ;

SELECT *
FROM d_authors
WHERE d_authors.name ILIKE '%а%';

SELECT *
FROM d_ban_types
WHERE ban_name ILIKE '%запрет%';

SELECT *
FROM d_ban_types
WHERE ban_name LIKE 'З%';

SELECT * FROM d_books WHERE book_series LIKE 'Огненный%';

SELECT *
FROM d_books
WHERE book_series ILIKE 'Мир на краю';

SELECT *
FROM d_books
WHERE book_series LIKE '%сумрака';

SELECT *
FROM d_genres
WHERE genre_name ILIKE '%ф_н%';

SELECT *
FROM d_genres
WHERE genre_name LIKE 'Р___н';

SELECT *
FROM f_book_sales
WHERE region LIKE 'Новосибирск';

-- Пописать запросы с SELECT и несколькими условиями - через AND, OR.
-- Написать по 10 запросов с AND и 10 запросов с OR.
SELECT *
FROM f_book_sales
WHERE region LIKE 'Москва' OR region LIKE 'Санкт-Петербург';

SELECT *
FROM f_leaderboard
WHERE rank <= 3;

SELECT *
FROM f_leaderboard
WHERE rank > 3;

SELECT *
FROM f_book_sales
WHERE revenue > 15000;

SELECT *
FROM f_book_sales
WHERE revenue < 10000;

SELECT *
FROM d_books
WHERE id_ban IS NULL;

SELECT *
FROM d_books
WHERE id_ban IS NOT NULL;

SELECT *
FROM d_books
WHERE id_ban IS NULL
   OR id_ban = 1;

SELECT *
FROM d_books
WHERE id_genre = 2
  AND id_ban IS NULL;


SELECT *
FROM d_ban_types
WHERE ban_name ILIKE '%Запрет%'
   OR ban_name ILIKE '%изъятие%';

SELECT *
FROM d_authors
WHERE age > 35
  AND (name LIKE 'А%' OR name LIKE 'Л%');

SELECT *
FROM d_ban_types
WHERE ban_name LIKE 'Запрет%'
  AND law_reference ILIKE '%закон%';

SELECT *
FROM d_books
WHERE id_ban IS NULL
   OR book_series IS NULL;

SELECT *
FROM d_books
WHERE id_ban IS NULL
  AND book_series IS NULL;

SELECT *
FROM d_genres
WHERE genre_name = 'Фэнтези'
   OR genre_name = 'Роман';

SELECT *
FROM d_genres
WHERE genre_name LIKE '% %';

SELECT *
FROM d_genres
WHERE genre_name like 'Прикл%';

SELECT *
FROM d_genres
WHERE genre_name LIKE 'Фэн%'
   OR genre_name LIKE 'Ро%';

SELECT *
FROM f_book_authors
WHERE book_id = 1
   OR author_id = 1;


SELECT *
FROM f_book_sales
WHERE (region = 'Москва' OR region = 'Санкт-Петербург')
  AND revenue > 10000;