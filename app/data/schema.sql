drop table if exists first_pool;
create table first_pool (
    id integer primary key autoincrement,
    datetime text,
    height real
)