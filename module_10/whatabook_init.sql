DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook. * TO 'whatabook_user'@'localhost';

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS wishlist;


CREATE TABLE store(
    store_id    INT                 NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)        NOT NULL,
    PRIMARY KEY(store_id)
);


CREATE TABLE book(
    book_id         INT             NOT NULL    AUTO_INCREMENT,
    book_name       VARCHAR(200)    NOT NULL,
    author          VARCHAR(200)    NOT NULL,
    details         VARCHAR(500),
    PRIMARY KEY(book_id)
):


CREATE TABLE user(
    user_id         INT             NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75)     NOT NULL,
    last_name       VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id)
);


CREATE TABLE wishlist(
    wishlist_id     INT     NOT NULL    AUTO_INCREMENT,
    user_id         INT     NOT NULL,
    book_id         INT     NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_user
    FOREIGN KEY(user_id)
        REFERENCES user(user_id),
    CONSTRAINT fk_book
    FOREIGN KEY(book_id)
        REFERENCES book(book_id)
);


INSERT INTO whatabook.store(store_id, locale)
    VALUES('1', '1320 Calvada' 'Las Vegas' 'Nevada');


INSERT INTO whatabook.book(book_id, book_name, author, details)
VALUES
('1', 'The Dreamer', 'Grace Yu', 'ISBN 132146141114'),
('2', 'The Puzzles', 'Jane Huss', 'ISBN 111478122111'),
('3', 'Pizza and the Cat', 'Cris Dur', 'ISBN 012389186177'),
('4', 'Mathematics', 'Lis Mye', 'ISBN 411361783241'),
('5', 'History', 'Drew Hanz', 'ISBN 811136152011'),
('6', 'Light and Energy', 'Ric Dre', 'ISBN 000132149186'),
('7', 'Solar Energy', 'John Smith', 'ISBN 111832116918'),
('8', 'Grow Your Food', 'Tim Walker', 'ISBN 911167853200'),
('9', 'How to Raise Animals', 'Dino Dy', 'ISBN 752167853211');


INSERT INTO whatabook.user(user_id, first_name, last_name)
VALUES
('11', 'Arnold', 'Green'),
('12', 'Tom', 'Roberts'),
('13', 'David', 'Jones');


INSERT INTO whatabook.wishlist(wishlist_id, user_id, book_id)
VALUES
('15', '11', '1'),
('16', '12', '4'),
('17', '13', '7');

