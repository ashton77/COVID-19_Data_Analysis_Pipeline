create database covid
use covid
-- set global max_allowed_packet=67108864

-- drop table time_series_data
-- drop table countries_data
-- drop table world_data

truncate table time_series_data
truncate table countries_data
truncate table world_data
 
create table time_series_data(
	index_ts int,
    date DATE,
    Country varchar(50),
    Province varchar(50),
    Confirmed int,
    Recovered int,
    Deaths int
);

create table countries_data(
	index_ts int,
    date DATE,
    Country varchar(50),
    Confirmed int,
    Recovered int,
    Deaths int
)

create table world_data(
	index_ts int,
    date DATE,
    Confirmed int,
    Recovered int,
    Deaths int,
    Increase_rate float
)

select * from time_series_data
select * from countries_data
select * from world_data

-- select CURRENT_USER();