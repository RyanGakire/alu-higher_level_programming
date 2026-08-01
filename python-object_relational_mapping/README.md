# Python - Object-relational mapping

Two ways of talking to the same MySQL database: raw queries with
`MySQLdb`, then the same work through the `SQLAlchemy` ORM.

## MySQLdb scripts

| File | Description |
| --- | --- |
| `0-select_states.py` | Lists all the states |
| `1-filter_states.py` | Lists the states starting with an upper N |
| `2-my_filter_states.py` | Filters by name with `format` (injectable) |
| `3-my_safe_filter_states.py` | Same filter, safe from SQL injection |
| `4-cities_by_state.py` | Lists all the cities with their state |
| `5-filter_cities.py` | Lists the cities of one state |

## SQLAlchemy models and scripts

| File | Description |
| --- | --- |
| `model_state.py` | The `State` class and the `Base` instance |
| `model_city.py` | The `City` class, with a foreign key to `states.id` |
| `6-model_state.py` | Creates the `states` table |
| `7-model_state_fetch_all.py` | Lists all the states |
| `8-model_state_fetch_first.py` | Prints the first state |
| `9-model_state_filter_a.py` | Lists the states containing an `a` |
| `10-model_state_my_get.py` | Prints the id of one state |
| `11-model_state_insert.py` | Adds the state Louisiana |
| `12-model_state_update_id_2.py` | Renames the state whose id is 2 |
| `13-model_state_delete_a.py` | Deletes the states containing an `a` |
| `14-model_city_fetch_by_state.py` | Lists the cities with their state |

## Usage

```
./0-select_states.py root root hbtn_0e_0_usa
./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
```

## Environment

* Ubuntu 20.04 LTS
* python3 (version 3.8.5), MySQLdb 2.0.x, SQLAlchemy 1.4.x
* pycodestyle (version 2.7.*)
