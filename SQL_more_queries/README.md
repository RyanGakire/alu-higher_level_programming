# MySQL - More queries

This project goes further with MySQL. It covers users and privileges, table
constraints like `NOT NULL`, `DEFAULT`, `UNIQUE`, primary keys and foreign
keys, and finally subqueries and joins across several tables.

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
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
```

Most scripts work inside one database, so the database name goes at the end:

```
cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
```

Tasks 10 to 16 need the `hbtn_0d_tvshows` dump. Import it once:

```
cat hbtn_0d_tvshows.sql | mysql -hlocalhost -uroot -p
```

## Files

| File | What it does |
| --- | --- |
| `0-privileges.sql` | Lists the privileges of `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates `hbtn_0d_2` and a user that can only read it |
| `3-force_name.sql` | Creates `force_name`, where `name` cannot be null |
| `4-never_empty.sql` | Creates `id_not_null`, where `id` defaults to 1 |
| `5-unique_id.sql` | Creates `unique_id`, where `id` cannot be used twice |
| `6-states.sql` | Creates `hbtn_0d_usa` and the table `states` |
| `7-cities.sql` | Creates the table `cities`, linked to `states` |
| `8-cities_of_california_subquery.sql` | Lists the cities of California, without `JOIN` |
| `9-cities_by_state_join.sql` | Lists every city with the name of its state |
| `10-genre_id_by_show.sql` | Lists the shows that have at least one genre |
| `11-genre_id_all_shows.sql` | Lists every show, with `NULL` when there is no genre |
| `12-no_genre.sql` | Lists only the shows without a genre |
| `13-count_shows_by_genre.sql` | Counts how many shows use each genre |
| `14-my_genres.sql` | Lists the genres of the show Dexter |
| `15-comedy_only.sql` | Lists the shows of the genre Comedy |
| `16-shows_by_genre.sql` | Lists every show with all its genres |

## Notes

- `CREATE USER IF NOT EXISTS` and `CREATE DATABASE IF NOT EXISTS` let the
  scripts run twice without failing.
- Task 8 is not allowed to use `JOIN`, so it uses a subquery to find the id of
  California first.
- `INNER JOIN` keeps only the rows found on both sides, so it is used when a
  link must exist. `LEFT JOIN` keeps every row of the first table, which is how
  tasks 11, 12 and 16 can show `NULL`.
- Task 13 counts through the link table only, so a genre with no show never
  appears in the result.

## Author
[RyanGakire](https://github.com/RyanGakire)
