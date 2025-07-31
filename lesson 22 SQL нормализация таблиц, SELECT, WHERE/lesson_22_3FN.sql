-- 1) Core (business) entities
CREATE TABLE d_author_3nf (
                         author_id   SERIAL    PRIMARY KEY,
                         birthdate   DATE      NOT NULL,
                         name        VARCHAR(50) NOT NULL,
                         surname     VARCHAR(50) NOT NULL
);

CREATE TABLE d_genres_3nf (
                        genre_id    SERIAL    PRIMARY KEY,
                        genre_name  VARCHAR(50) NOT NULL
);

CREATE TABLE d_ban_types_3nf (
                           ban_id       SERIAL     PRIMARY KEY,
                           ban_name     VARCHAR(50) NOT NULL,
                           law_reference VARCHAR(255)
);

CREATE TABLE d_books_3nf (
                       book_id      SERIAL     PRIMARY KEY,
                       book_name    VARCHAR(255) NOT NULL,
                       book_series  VARCHAR(100),
                       genre_id     INTEGER    NOT NULL REFERENCES d_genres_3nf(genre_id),
                       ban_id       INTEGER    REFERENCES d_ban_types_3nf(ban_id)
);

CREATE TABLE d_regions_3nf (
                         region_id   SERIAL      PRIMARY KEY,
                         region_name VARCHAR(100) NOT NULL
);

-- 2) Historization (Type-2) tables
CREATE TABLE d_author_history_3nf (
                                auth_hist_id SERIAL     PRIMARY KEY,
                                author_id    INTEGER    NOT NULL REFERENCES d_author_3nf(author_id),
                                valid_from   TIMESTAMPTZ NOT NULL,
                                valid_to     TIMESTAMPTZ NOT NULL,
                                UNIQUE (author_id, valid_from)
);

CREATE TABLE d_book_history_3nf (
                              book_hist_id SERIAL     PRIMARY KEY,
                              book_id      INTEGER    NOT NULL REFERENCES d_books_3nf(book_id),
                              valid_from   TIMESTAMPTZ NOT NULL,
                              valid_to     TIMESTAMPTZ NOT NULL,
                              UNIQUE (book_id, valid_from)
);

CREATE TABLE d_genre_history_3nf (
                               gen_hist_id  SERIAL     PRIMARY KEY,
                               genre_id     INTEGER    NOT NULL REFERENCES d_genres_3nf(genre_id),
                               valid_from   TIMESTAMPTZ NOT NULL,
                               valid_to     TIMESTAMPTZ NOT NULL,
                               UNIQUE (genre_id, valid_from)
);

CREATE TABLE d_ban_history_3nf (
                             ban_hist_id  SERIAL     PRIMARY KEY,
                             ban_id       INTEGER    NOT NULL REFERENCES d_ban_types_3nf(ban_id),
                             valid_from   TIMESTAMPTZ NOT NULL,
                             valid_to     TIMESTAMPTZ NOT NULL,
                             UNIQUE (ban_id, valid_from)
);

-- 3) Facts
CREATE TABLE f_book_sales_3nf (
                              sale_id       SERIAL      PRIMARY KEY,
                              book_id       INTEGER     NOT NULL REFERENCES d_books_3nf(book_id),
                              sale_date     DATE        NOT NULL,
                              quantity_sold INTEGER     NOT NULL,
                              revenue       NUMERIC(12,2),
                              region_id     INTEGER     REFERENCES d_regions_3nf(region_id)
);

CREATE TABLE f_book_storage_3nf (
                                storage_id    SERIAL      PRIMARY KEY,
                                book_id       INTEGER     NOT NULL REFERENCES d_books_3nf(book_id),
                                storage_count INTEGER,
                                record_date   DATE        NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE f_leaderboard_3nf (
                               rank_id       SERIAL      PRIMARY KEY,
                               book_id       INTEGER     NOT NULL REFERENCES d_books_3nf(book_id),
                               rank          INTEGER     NOT NULL,
                               rank_date     DATE        NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE f_book_authors_3nf (
                                ba_id         SERIAL      PRIMARY KEY,
                                book_id       INTEGER     NOT NULL REFERENCES d_books_3nf(book_id),
                                author_id     INTEGER     NOT NULL REFERENCES d_author_3nf(author_id)
);

DROP TABLE d_author_3nf, d_genres_3nf, d_ban_types_3nf;