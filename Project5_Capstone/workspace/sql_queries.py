import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES
staging_i94addrs_table_drop = "DROP TABLE IF EXISTS staging_i94addrs"     
staging_i94cit_res_table_drop = "DROP TABLE IF EXISTS staging_i94cit_res"         
staging_i94modes_table_drop = "DROP TABLE IF EXISTS staging_i94modes"     
staging_i94ports_table_drop = "DROP TABLE IF EXISTS staging_i94ports"     
staging_i94visas_table_drop = "DROP TABLE IF EXISTS staging_i94visas"     
staging_airports_table_drop = "DROP TABLE IF EXISTS staging_airports"     
staging_immigrations_table_drop = "DROP TABLE IF EXISTS staging_immigrations"         
staging_us_cities_demographics_table_drop = "DROP TABLE IF EXISTS staging_us_cities_demographics"   

i94addrs_table_drop = "DROP TABLE IF EXISTS i94addrs"
i94cit_res_table_drop = "DROP TABLE IF EXISTS i94cit_res"
i94modes_table_drop = "DROP TABLE IF EXISTS i94modes"
i94ports_table_drop = "DROP TABLE IF EXISTS i94ports"
i94visas_table_drop = "DROP TABLE IF EXISTS i94visas"
airports_table_drop = "DROP TABLE IF EXISTS airports"
immigrations_table_drop = "DROP TABLE IF EXISTS immigrations"
us_cities_demographics_table_drop = "DROP TABLE IF EXISTS us_cities_demographics"

# CREATE SCHEMA
schema_create = ("""
    CREATE SCHEMA IF NOT EXISTS capstone;
    SET search_path TO capstone;
""")

# STAGING TABLES
staging_i94addrs_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_i94addrs (
    i94addr_id  VARCHAR NOT NULL DISTKEY, 
    state       VARCHAR NOT NULL
);
""");

staging_i94cit_res_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_i94cit_res (
    i94cit_res_id   VARCHAR NOT NULL DISTKEY, 
    country         VARCHAR NOT NULL
);
""");

staging_i94modes_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_i94modes (
    i94mode_id   VARCHAR NOT NULL DISTKEY, 
    mode         VARCHAR NOT NULL
);
""");

staging_i94ports_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_i94ports (
    i94port_id   VARCHAR NOT NULL DISTKEY, 
    city         VARCHAR NOT NULL,
    state        VARCHAR NOT NULL SORTKEY
);
""");

staging_i94visas_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_i94visas (
    i94visa_id   VARCHAR NOT NULL DISTKEY, 
    category     VARCHAR NOT NULL
);
""");

staging_airports_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_airports (
    ident_id      VARCHAR NOT NULL DISTKEY, 
    type          VARCHAR NOT NULL,
    name          VARCHAR NOT NULL,
    continent     VARCHAR NOT NULL,
    iso_country   VARCHAR NOT NULL,
    local_code    VARCHAR NOT NULL SORTKEY,    
    latitude      VARCHAR NOT NULL,
    longitude     VARCHAR NOT NULL, 
    state         VARCHAR NOT NULL    
);
""");

staging_immigrations_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_immigrations (
    cicid      INT NOT NULL DISTKEY, 
    i94yr      INT NOT NULL,
    i94mon     INT NOT NULL,
    i94cit     INT NOT NULL,
    i94res     INT NOT NULL,    
    i94port    VARCHAR NOT NULL SORTKEY,
    arrdate    DATE NOT NULL,
    i94mode    INT NOT NULL,
    i94addr    VARCHAR NOT NULL,
    depdate    DATE NULL,    
    i94bir     INT NOT NULL,
    i94visa    INT NOT NULL, 
    count      INT NOT NULL,    
    matflag    VARCHAR NULL,
    biryear    INT NOT NULL,
    gender     VARCHAR NULL,
    insnum     VARCHAR NULL,
    airline    VARCHAR NULL,     
    admnum     FLOAT NOT NULL,
    fltno      VARCHAR NULL,
    visatype   VARCHAR NOT NULL,
    days_stay  INT NULL    
);
""");

staging_us_cities_demographics_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_us_cities_demographics (     
    city                      VARCHAR NOT NULL,
    state                     VARCHAR NOT NULL,
    state_code                VARCHAR NOT NULL SORTKEY,
    foreign_born              INTEGER NOT NULL, 
    male_population           INTEGER NOT NULL,
    average_household_size    FLOAT NOT NULL,
    total_population          INTEGER NOT NULL,
    female_population         INTEGER NOT NULL,    
    media_age                 FLOAT NOT NULL,
    number_of_veterans        INTEGER NOT NULL, 
    american_indian_and_alaska_native BIGINT NOT NULL,
    asian                     BIGINT NOT NULL,
    black_or_african_american BIGINT NOT NULL,
    hispanic_or_latino        BIGINT NOT NULL,
    white                     BIGINT NOT NULL   
);
""");

# CREATE TABLES
i94addrs_table_create = ("""
CREATE TABLE IF NOT EXISTS i94addrs (
    i94addr_id  VARCHAR NOT NULL DISTKEY, 
    state       VARCHAR NOT NULL
);
""");

i94cit_res_table_create = ("""
CREATE TABLE IF NOT EXISTS i94cit_res (
    i94cit_res_id   INTEGER NOT NULL DISTKEY, 
    country         VARCHAR NOT NULL
);
""");

i94modes_table_create = ("""
CREATE TABLE IF NOT EXISTS i94modes (
    i94mode_id   INTEGER NOT NULL DISTKEY, 
    mode         VARCHAR NOT NULL
);
""");

i94ports_table_create = ("""
CREATE TABLE IF NOT EXISTS i94ports (
    i94port_id   VARCHAR NOT NULL DISTKEY, 
    city         VARCHAR NOT NULL,
    state        VARCHAR NOT NULL SORTKEY
);
""");

i94visas_table_create = ("""
CREATE TABLE IF NOT EXISTS i94visas (
    i94visa_id   INTEGER NOT NULL DISTKEY, 
    category     VARCHAR NOT NULL
);
""");

airports_table_create = ("""
CREATE TABLE IF NOT EXISTS airports (
    ident_id      VARCHAR NOT NULL DISTKEY, 
    type          VARCHAR NOT NULL,
    name          VARCHAR NOT NULL,
    continent     VARCHAR NOT NULL,
    iso_country   VARCHAR NOT NULL,
    local_code    VARCHAR NOT NULL SORTKEY,    
    latitude      VARCHAR NOT NULL,
    longitude     VARCHAR NOT NULL, 
    state         VARCHAR NOT NULL    
);
""");

immigrations_table_create = ("""
CREATE TABLE IF NOT EXISTS immigrations (
    cic_id     INTEGER NOT NULL DISTKEY, 
    i94yr      INTEGER NOT NULL,
    i94mon     INTEGER NOT NULL,
    i94cit_id     INTEGER NOT NULL,
    i94res_id     INTEGER NOT NULL,    
    i94port_id    VARCHAR NOT NULL SORTKEY,
    arrdate    DATE NOT NULL,
    i94mode_id    INTEGER NOT NULL,
    i94addr_id    VARCHAR NOT NULL,
    depdate    DATE NULL,    
    i94bir     INTEGER NOT NULL,
    i94visa_id    INTEGER NOT NULL, 
    count      INTEGER NOT NULL,    
    matflag    VARCHAR NULL,
    biryear    INTEGER NOT NULL,
    gender     VARCHAR NULL,
    insnum     VARCHAR NULL,
    airline    VARCHAR NULL,     
    admnum     FLOAT NOT NULL,
    fltno      VARCHAR NULL,
    visatype   VARCHAR NOT NULL,
    days_stay  INTEGER NULL 
);
""");
 
us_cities_demographics_table_create = ("""
CREATE TABLE IF NOT EXISTS us_cities_demographics (
    us_cities_demographic_id  INTEGER IDENTITY(1,1) DISTKEY,     
    city                      VARCHAR NOT NULL,
    state                     VARCHAR NOT NULL,
    state_code                VARCHAR NOT NULL SORTKEY,
    foreign_born              INTEGER NOT NULL, 
    male_population           INTEGER NOT NULL,
    average_household_size    FLOAT NOT NULL,
    total_population          INTEGER NOT NULL,
    female_population         INTEGER NOT NULL,    
    media_age                 FLOAT NOT NULL,
    number_of_veterans        INTEGER NOT NULL, 
    american_indian_and_alaska_native BIGINT NOT NULL,
    asian                     BIGINT NOT NULL,
    black_or_african_american BIGINT NOT NULL,
    hispanic_or_latino        BIGINT NOT NULL,
    white                     BIGINT NOT NULL   
);
""");

# Loading data from parquet file to redshift
i94addr_copy = ("""
    COPY {}.staging_i94addrs 
    FROM 's3://{}/{}/i94addr.parquet' 
    IAM_ROLE '{}' 
    FORMAT AS PARQUET;
""").format(config["DWH"]["dwh_db_schema"], config["S3"]["bucket_name"], config["S3"]["path_input_data"], config["IAM_ROLE"]["ARN"])

i94cit_res_copy = ("""
    COPY {}.staging_i94cit_res 
    FROM 's3://{}/{}/i94cit_i94res.parquet' 
    IAM_ROLE '{}' 
    FORMAT AS PARQUET;
""").format(config["DWH"]["dwh_db_schema"], config["S3"]["bucket_name"], config["S3"]["path_input_data"], config["IAM_ROLE"]["ARN"])

i94modes_copy = ("""
    COPY {}.staging_i94modes 
    FROM 's3://{}/{}/i94mode.parquet' 
    IAM_ROLE '{}' 
    FORMAT AS PARQUET;
""").format(config["DWH"]["dwh_db_schema"], config["S3"]["bucket_name"], config["S3"]["path_input_data"], config["IAM_ROLE"]["ARN"])

i94ports_copy = ("""
    COPY {}.staging_i94ports 
    FROM 's3://{}/{}/i94port.parquet' 
    IAM_ROLE '{}' 
    FORMAT AS PARQUET;
""").format(config["DWH"]["dwh_db_schema"], config["S3"]["bucket_name"], config["S3"]["path_input_data"], config["IAM_ROLE"]["ARN"])

i94visas_copy = ("""
    COPY {}.staging_i94visas 
    FROM 's3://{}/{}/i94visa.parquet' 
    IAM_ROLE '{}' 
    FORMAT AS PARQUET;
""").format(config["DWH"]["dwh_db_schema"], config["S3"]["bucket_name"], config["S3"]["path_input_data"], config["IAM_ROLE"]["ARN"])

airports_copy = ("""
    COPY {}.staging_airports 
    FROM 's3://{}/{}/airport.parquet' 
    IAM_ROLE '{}' 
    FORMAT AS PARQUET;
""").format(config["DWH"]["dwh_db_schema"], config["S3"]["bucket_name"], config["S3"]["path_input_data"], config["IAM_ROLE"]["ARN"])

immigrations_copy = ("""
    COPY {}.staging_immigrations 
    FROM 's3://{}/{}/immigration.parquet' 
    IAM_ROLE '{}' 
    FORMAT AS PARQUET;
""").format(config["DWH"]["dwh_db_schema"], config["S3"]["bucket_name"], config["S3"]["path_input_data"], config["IAM_ROLE"]["ARN"])

us_cities_demographics_copy = ("""
    COPY {}.staging_us_cities_demographics 
    FROM 's3://{}/{}/cities_demographics.parquet' 
    IAM_ROLE '{}' 
    FORMAT AS PARQUET;
""").format(config["DWH"]["dwh_db_schema"], config["S3"]["bucket_name"], config["S3"]["path_input_data"], config["IAM_ROLE"]["ARN"])

# INSERT FINAL TABLES
i94addrs_table_insert = ("""
INSERT INTO {}.i94addrs  
SELECT DISTINCT 
    i94addr_id,
    state
FROM staging_i94addrs
WHERE i94addr_id IS NOT NULL;
""").format(config["DWH"]["dwh_db_schema"])

i94cit_res_table_insert = ("""
INSERT INTO {}.i94cit_res  
SELECT DISTINCT 
    CAST(i94cit_res_id as INT), 
    country
FROM staging_i94cit_res
WHERE i94cit_res_id IS NOT NULL;
""").format(config["DWH"]["dwh_db_schema"])

i94modes_table_insert = ("""
INSERT INTO {}.i94modes  
SELECT DISTINCT 
    CAST(i94mode_id as INT), 
    mode
FROM staging_i94modes
WHERE i94mode_id IS NOT NULL;
""").format(config["DWH"]["dwh_db_schema"])

i94ports_table_insert = ("""
INSERT INTO i94ports  
SELECT DISTINCT 
    i94port_id, 
    city,
    state
FROM staging_i94ports
WHERE i94port_id IS NOT NULL;
""")

i94visas_table_insert = ("""
INSERT INTO i94visas  
SELECT DISTINCT 
    CAST(i94visa_id as INT), 
    category
FROM staging_i94visas
WHERE i94visa_id IS NOT NULL;
""")

airports_table_insert = ("""
INSERT INTO airports  
SELECT DISTINCT 
    ident_id, 
    type,
    name,
    continent,
    iso_country,
    local_code,    
    latitude,
    longitude, 
    state
FROM staging_airports
WHERE ident_id IS NOT NULL;
""")

imigrations_table_insert = ("""
INSERT INTO immigrations  
SELECT DISTINCT 
    CAST(cicid as INT) AS cic_id, 
    CAST(i94yr as INT),
    CAST(i94mon as INT),
    CAST(i94cit as INT) AS i94cit_id ,
    CAST(i94res as INT) AS i94res_id,    
    i94port AS i94port_id,
    arrdate,
    CAST(i94mode as INT) AS i94mode_id,
    i94addr AS i94addr_id,
    depdate,    
    CAST(i94bir as INT),
    CAST(i94visa as INT) AS i94visa_id, 
    CAST(count as INT),    
    matflag,
    CAST(biryear as INT),
    gender,
    insnum,
    airline,     
    CAST(admnum as FLOAT),
    fltno,
    visatype,
    CAST(days_stay as INT) 
FROM staging_immigrations
WHERE cic_id IS NOT NULL;
""")    

us_cities_demographics_table_insert = ("""
INSERT INTO us_cities_demographics  
    (city, state, state_code, foreign_born, male_population, average_household_size, total_population, female_population, media_age, number_of_veterans, american_indian_and_alaska_native, asian, black_or_african_american,  hispanic_or_latino, white) 
SELECT DISTINCT 
    city,
    state,
    state_code,
    foreign_born,
    male_population,
    average_household_size,
    total_population,
    female_population,
    media_age,
    number_of_veterans,
    american_indian_and_alaska_native,
    asian,
    black_or_african_american, 
    hispanic_or_latino,
    white 
FROM staging_us_cities_demographics 
WHERE state_code IS NOT NULL;
""") 
    
# QUERY LISTS
create_table_queries = [schema_create, staging_i94addrs_table_create, staging_i94cit_res_table_create, staging_i94modes_table_create, staging_i94ports_table_create, staging_i94visas_table_create, staging_airports_table_create, staging_immigrations_table_create, staging_us_cities_demographics_table_create, i94addrs_table_create, i94cit_res_table_create, i94modes_table_create, i94ports_table_create, i94visas_table_create, airports_table_create, immigrations_table_create, us_cities_demographics_table_create]

drop_table_queries = [schema_create, staging_i94addrs_table_drop ,staging_i94cit_res_table_drop ,staging_i94modes_table_drop ,staging_i94ports_table_drop ,staging_i94visas_table_drop ,staging_airports_table_drop ,staging_immigrations_table_drop ,staging_us_cities_demographics_table_drop, i94addrs_table_drop, i94cit_res_table_drop, i94modes_table_drop, i94ports_table_drop, i94visas_table_drop, airports_table_drop, immigrations_table_drop, us_cities_demographics_table_drop]

copy_table_queries = [schema_create, i94addr_copy, i94cit_res_copy, i94modes_copy, i94ports_copy, i94visas_copy, airports_copy, us_cities_demographics_copy, immigrations_copy]

insert_table_queries = [schema_create, i94addrs_table_insert, i94cit_res_table_insert, i94modes_table_insert, i94ports_table_insert, i94visas_table_insert, airports_table_insert, us_cities_demographics_table_insert, imigrations_table_insert]

list_all_tables = ['us_cities_demographics', 'immigrations', 'airports', 'i94visas', 'i94ports', 'i94modes', 'i94cit_res', 'i94addrs']
