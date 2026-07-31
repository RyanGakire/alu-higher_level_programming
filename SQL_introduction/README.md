# MySQL - Introduction

This project is a first look at relational databases with MySQL. Each file is
a small SQL script that does one thing: create or delete a database, create a
table, add rows, read them back, change them or remove them.

## Requirements

- Ubuntu 20.04 LTS with MySQL 8.0 (version 8.0.25)
- All files end with a new line
- Every file starts with a comment describing the task
- Every query has a comment just above it
- All SQL keywords are in uppercase
- Allowed editors: `vi`, `vim`, `emacs`

## How to run a script

Send the file to the `mysql` command:

```
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

Some scripts work inside one database. The database name goes at the end of
the command:

```
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## Files

| File | What it does |
| --- | --- |
| `0-list_databases.sql` | Lists all the databases of the server |
| `1-create_database_if_missing.sql` | Creates `hbtn_0c_0` without failing if it is already there |
| `2-remove_database.sql` | Deletes `hbtn_0c_0` without failing if it is missing |
| `3-list_tables.sql` | Lists all the tables of the current database |
| `4-first_table.sql` | Creates the table `first_table` with `id` and `name` |
| `5-full_table.sql` | Prints the full description of `first_table` |
| `6-list_values.sql` | Lists every row of `first_table` |
| `7-insert_value.sql` | Adds the row `89` / `Best School` to `first_table` |
| `8-count_89.sql` | Counts the rows of `first_table` with `id = 89` |
| `9-full_creation.sql` | Creates `second_table` and adds four records |
| `10-top_score.sql` | Lists score and name, best score first |
| `11-best_score.sql` | Same list, but only for a score of 10 or more |
| `12-no_cheating.sql` | Sets the score of Bob to 10, using his name |
| `13-change_class.sql` | Removes the rows with a score of 5 or less |
| `14-average.sql` | Computes the average score in a column named `average` |
| `15-groups.sql` | Counts the rows sharing the same score |
| `16-no_link.sql` | Lists score and name, skipping the rows without a name |

## Notes

- Tasks 1, 2, 4 and 9 use `IF NOT EXISTS` or `IF EXISTS` so running them twice
  never fails.
- Task 5 uses `SHOW CREATE TABLE` because `DESCRIBE` and `EXPLAIN` are not
  allowed.
- Task 12 finds the row with `WHERE name = 'Bob'`, not with an id.
- Task 16 uses `WHERE name IS NOT NULL` to drop the rows that have no name.

## Author
[RyanGakire](https://github.com/RyanGakire)
