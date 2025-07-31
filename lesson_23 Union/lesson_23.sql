CREATE TABLE fashists
(
    id         SERIAL PRIMARY KEY,
    fash_name  VARCHAR(50),
    is_punched BOOLEAN
);

-- Найти свою таблицу которую я фиг пойми куда выложил
SELECT *
FROM information_schema.tables
WHERE table_name = 'fashists';

CREATE TABLE punched_fashists
(
    id        SERIAL PRIMARY KEY,
    fash_name VARCHAR(50)
);

INSERT INTO fashists(fash_name, is_punched)
SELECT 'Vladimir Putin', FALSE
UNION
SELECT 'Vladimir zelenski', FALSE
UNION
SELECT 'Netanyahu', FALSE
UNION
SELECT 'Edrogan', FALSE
UNION
SELECT 'Orban', FALSE
UNION
SELECT 'Trump', FALSE;

INSERT INTO fashists(fash_name, is_punched)
VALUES ('TEST_FASHIST', FALSE);

INSERT INTO fashists(fash_name, is_punched)
SELECT 'test FASHIST 2', FALSE;

SELECT DISTINCT fash_name, is_punched
FROM fashists;

UPDATE fashists
SET fash_name = 'Adolf Hitler'
WHERE id = 7;
UPDATE fashists
SET is_punched = TRUE
WHERE id = 7;

UPDATE fashists
SET fash_name = 'Mousolini'
WHERE fash_name = 'test FASHIST 2';
UPDATE fashists
SET is_punched = TRUE
WHERE fash_name = 'test FASHIST 2';

UPDATE fashists
SET is_punched = TRUE
WHERE id = 11;

UPDATE fashists
SET fash_name = 'Pinochet'
WHERE fash_name = 'TEST_FASHIST'
  AND is_punched = TRUE;

UPDATE fashists
SET is_punched = TRUE
WHERE fash_name = 'Mousolini';

DELETE
FROM fashists
WHERE fash_name = 'TEST_FASHIST';

BEGIN;

INSERT INTO punched_fashists(fash_name)
SELECT fash_name
FROM fashists
WHERE is_punched = TRUE;

DELETE
FROM fashists
WHERE is_punched = TRUE;

COMMIT;

INSERT INTO fashists(fash_name, is_punched)
SELECT 'Francisko Franko', FALSE;


BEGIN;

UPDATE fashists
SET is_punched = TRUE
WHERE fash_name = 'Francisko Franko';

INSERT INTO punched_fashists(fash_name)
SELECT fash_name
FROM fashists
WHERE is_punched = TRUE;

DELETE
FROM fashists
WHERE is_punched = TRUE;

COMMIT;