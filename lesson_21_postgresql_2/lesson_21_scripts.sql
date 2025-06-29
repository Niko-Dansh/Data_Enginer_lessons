SELECT *
FROM information_schema.role_table_grants
WHERE grantee = CURRENT_USER;

SELECT rolname, rolsuper, rolcreatedb, rolcreaterole, rolcanlogin
FROM pg_roles
WHERE rolname = CURRENT_USER;

CREATE TABLE d_authors
(
    begin_date timestamptz DEFAULT NOW(),
    end_date   timestamptz DEFAULT '2050-01-01 00:00',
    id         INT GENERATED ALWAYS AS IDENTITY,
    birthdate  DATE,
    age        SMALLINT,
    name       VARCHAR(50),
    surname    VARCHAR(50),
    PRIMARY KEY (id, begin_date)
);


CREATE TABLE d_books
(
    begin_date  timestamptz DEFAULT NOW(),
    end_date    timestamptz DEFAULT '2050-01-01 00:00',
    id          INT GENERATED ALWAYS AS IDENTITY,
    book_name   VARCHAR(255),
    book_series VARCHAR(100),
    id_genre    INT,
    id_ban      INT,
    PRIMARY KEY (id, begin_date)
);



CREATE TABLE d_books
(
    begin_date  timestamptz DEFAULT NOW(),
    end_date    timestamptz DEFAULT '2050-01-01 00:00',
    id          INT GENERATED ALWAYS AS IDENTITY,
    id_genre    INT,
    id_ban      INT,
    book_name   VARCHAR(255),
    book_series VARCHAR(100),
    PRIMARY KEY (id, begin_date)
);

CREATE TABLE d_books -- совет чата гпт по оптимальности
(
    id          INT GENERATED ALWAYS AS IDENTITY,
    id_genre    INT NOT NULL,
    id_ban      INT,
    book_name   VARCHAR(255) NOT NULL,
    book_series VARCHAR(100),
    begin_date  timestamptz DEFAULT NOW(),
    end_date    timestamptz DEFAULT '2050-01-01 00:00',
    PRIMARY KEY (id, begin_date)
);

CREATE TABLE d_genres
(
    id          INT GENERATED ALWAYS AS IDENTITY,
    genre_name  VARCHAR(50),
    begin_date  timestamptz DEFAULT NOW(),
    end_date    timestamptz DEFAULT '2050-01-01 00:00',
    PRIMARY KEY (id, begin_date)
);

CREATE TABLE f_leaderboard
(
    id         INT GENERATED ALWAYS AS IDENTITY,
    book_id    INT,
    rank       INT,
    begin_date timestamptz DEFAULT NOW(),
    end_date   timestamptz DEFAULT '2050-01-01 00:00',
    PRIMARY KEY (id, begin_date)
);

CREATE TABLE f_book_sales
(
    id            INT GENERATED ALWAYS AS IDENTITY,
    book_id       INT  NOT NULL,
    sale_date     DATE NOT NULL,
    quantity_sold INT  NOT NULL,
    revenue       NUMERIC(12, 2),
    region        VARCHAR(100),
    begin_date    timestamptz DEFAULT NOW(),
    end_date      timestamptz DEFAULT '2050-01-01 00:00',
    PRIMARY KEY (id, begin_date)
);

CREATE TABLE f_book_storage
(
    id         INT GENERATED ALWAYS AS IDENTITY,
    book_id    INT NOT NULL ,
    storage_count INT,
    begin_date timestamptz DEFAULT NOW(),
    end_date   timestamptz DEFAULT '2050-01-01 00:00',
    PRIMARY KEY (id, begin_date)
);



INSERT INTO d_authors (begin_date, end_date, birthdate, age, name, surname)
VALUES
    ('2023-01-01 00:00', '2050-01-01 00:00', '1985-03-12', 39, 'Антон', 'Чехов'),
    ('2023-01-01 00:00', '2050-01-01 00:00', '1970-11-05', 53, 'Людмила', 'Петрушевская'),
    ('2023-01-01 00:00', '2050-01-01 00:00', '1990-06-21', 34, 'Игорь', 'Громов'),
    ('2023-01-01 00:00', '2050-01-01 00:00', '1962-04-18', 62, 'Сергей', 'Довлатов'),
    ('2023-01-01 00:00', '2050-01-01 00:00', '2000-12-01', 24, 'Мария', 'Книжная');

INSERT INTO d_books (begin_date, end_date, book_name, book_series, id_genre, id_ban)
VALUES
    ('2025-06-26 00:00:00+00', '2050-01-01 00:00:00+00', 'Пламя надежды', 'Огненный путь', 1, 1),
    ('2025-06-26 00:00:00+00', '2050-01-01 00:00:00+00', 'Звёздный рыцарь', NULL, 2, NULL),
    ('2025-06-26 00:00:00+00', '2050-01-01 00:00:00+00', 'Последний берег', 'Мир на краю', 3, NULL),
    ('2025-06-26 00:00:00+00', '2050-01-01 00:00:00+00', 'Мир теней', 'Хроники сумрака', 2, 2),
    ('2025-06-26 00:00:00+00', '2050-01-01 00:00:00+00', 'Сердце дракона', NULL, 4, NULL);


INSERT INTO d_genres (genre_name, begin_date, end_date)
VALUES
    ('Фэнтези', '2025-06-26 00:00:00+00', '2050-01-01 00:00:00+00'),
    ('Научная фантастика', '2025-06-26 00:00:00+00', '2050-01-01 00:00:00+00'),
    ('Детектив', '2025-06-26 00:00:00+00', '2050-01-01 00:00:00+00'),
    ('Роман', '2025-06-26 00:00:00+00', '2050-01-01 00:00:00+00'),
    ('Приключения', '2025-06-26 00:00:00+00', '2050-01-01 00:00:00+00');

CREATE TABLE d_ban_types
(
    id            INT GENERATED ALWAYS AS IDENTITY,
    ban_name      VARCHAR(50)                            NOT NULL,
    law_reference VARCHAR(255),
    begin_date    timestamptz DEFAULT NOW()              NOT NULL,
    end_date      timestamptz DEFAULT '2050-01-01 00:00:00' NOT NULL,
    PRIMARY KEY (id, begin_date)
);

INSERT INTO d_ban_types (ban_name, law_reference, begin_date, end_date)
VALUES ('Запрет на продажу', 'Федеральный закон №123-ФЗ от 01.01.2020', NOW(), '2050-01-01 00:00:00'),
       ('Цензура содержания', 'Постановление Правительства №456 от 15.03.2021', NOW(), '2050-01-01 00:00:00'),
       ('Запрет для несовершеннолетних', 'Закон №789-ФЗ от 20.05.2019', NOW(), '2050-01-01 00:00:00'),
       ('Изъятие из библиотек', 'Приказ Минкульта №321 от 10.09.2022', NOW(), '2050-01-01 00:00:00'),
       ('Запрет на ввоз', 'Таможенное распоряжение №654 от 25.12.2020', NOW(), '2050-01-01 00:00:00');

CREATE TABLE f_book_authors
(
    id         INT GENERATED ALWAYS AS IDENTITY,
    book_id    INT                                       NOT NULL,
    author_id  INT                                       NOT NULL,
    begin_date timestamptz DEFAULT NOW()                 NOT NULL,
    end_date   timestamptz DEFAULT '2050-01-01 00:00:00' NOT NULL,
    PRIMARY KEY (id, begin_date)
);

INSERT INTO f_book_authors (book_id, author_id)
VALUES (1, 2),
       (2, 5),
       (3, 1),
       (4, 3),
       (5, 4);



INSERT INTO f_book_sales (book_id, sale_date, quantity_sold, revenue, region)
VALUES (1, '2025-06-01', 100, 15000.00, 'Москва'),
       (2, '2025-06-02', 50, 7500.00, 'Санкт-Петербург'),
       (3, '2025-06-03', 200, 30000.00, 'Новосибирск'),
       (4, '2025-06-04', 120, 18000.00, 'Казань'),
       (5, '2025-06-05', 80, 12000.00, 'Екатеринбург');

INSERT INTO f_leaderboard (book_id, rank)
VALUES (4, 1),
       (3, 2),
       (1, 3),
       (2, 4),
       (5, 5);