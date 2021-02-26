create table water_data(
	id SERIAL PRIMARY key,
	water_level DOUBLE precision,
	set_level DOUBLE precision,
	timestamp timestamp NOT NULL DEFAULT current_timestamp
); 
