<<<<<<< HEAD
/*
    Select query to see users wishlist
*/
SELECT user.user_id, user.first_name, book.book_id, book_name
FROM wishlist
INNER JOIN user
    ON wishlist.user_id = user.user_id
INNER JOIN book
    ON wishlist.book_id = book.book_id;


/*
    Select query to see WhatABook store
*/
SELECT * FROM `whatabook`.`store` LIMIT 1000;


/*
    Select query to see WhatABook lists of books
*/
SELECT * FROM `whatabook`.`book`. LIMIT 1000;


/*
    Select query to see WhatABook lists of users
*/
SELECT * FROM `whatabook`.`user` LIMIT 1000;


/*
    Select query to see WhatABook lists of users
*/
SELECT * FROM `whatabook`.`wishlist` LIMIT 1000;


/*
    Select query to see WhatABook a list of books not in the users’ wishlist
*/
SELECT book_id, book_name, author, details
FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = user_id);


""" Reference: Professor Krasso. (2020, July 16). GitHub repository. module10/whatabook_program_queries.sql """
=======

>>>>>>> aa9e3026386438188783b8466da70aa1f70964fc
