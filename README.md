# Sanctuary
The private bot for the LeoHartUK Discord guild

### Requirements

* Python 3.5 or above
* PostgreSQL

The database name is specified in the `Config/Bot.json` file. The tables in the database must be as follows, at minimum:

```sql
CREATE TABLE available_roles (
	id BIGINT,
	PRIMARY KEY (id)
);
```
