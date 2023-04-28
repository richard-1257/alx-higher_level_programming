
# Python - Network #1

In this project, I continued to practicing SQL queries, working with permissoins, joins, and constraints.

## Usage 🐋

- Scripts [3-force_name.sql](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/3-force_name.sql) forward take the database to query from as a MySQL command line argument.

`$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2`

- Tasks 10-101 query from the database [hbtn_0d_tvshows.sql](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/hbtn_0d_tvshows.sql).
- Tasks 102-103 query from the database [hbtn_0d_tvshows_rate.sql](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/hbtn_0d_tvshows_rate.sql).

## Tasks 📃
- 0. My privileges!
     - [0-privileges.sql](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/0-privileges.sql): MySQL script that lists all privileges of the users `user_0d_1` and `user_0d_2`.
     
- 1. Root user
     - [1-create_user.sql](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/1-create_user.sql): MySQL script that creates the user `user_0d_1` with all privileges and password `user_0d_1_pwd`.
   
- 2. Read user
     - [2-create_read_user.sql](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/2-create_read_user.sql): MySQL script that creates the database `hbtn_0d_2` and user `user_0d_2` with password `user_0d_2_pwd`.
     - `user_0d_2` only has SELECT privilege on the database `hbtn_0d_2`.

- 3. Always a name
     - [3-force_name.sql](https://github.com/richard-1257/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/3-force_name.sql): MySQL script that creates the table `force_name`.
     - Description:
         - `id`: INT
         - `name`: VARCHAR(256) (cannot be null)
