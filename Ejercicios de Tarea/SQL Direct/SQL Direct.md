# Ejercicios de tarea

## Descripcion

Connect to this PostgreSQL server and find the flag! `psql -h saturn.picoctf.net -p 60315 -U postgres pico` Password is `postgres`

## Pistas (Si hay)



## Solución

``` Bash

┌──(kali㉿kali)-[~]
└─$ psql -h saturn.picoctf.net -p 60315 -U postgres pico
Password for user postgres: 
psql (14.4 (Debian 14.4-1+b1), server 14.2 (Debian 14.2-1.pgdg110+1))
Type "help" for help.

pico=# ls -la
pico-# ls 
pico-# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 pico      | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(4 rows)

pico-# \d pico
Did not find any relation named "pico".
pico-# \dt
         List of relations
 Schema | Name  | Type  |  Owner   
--------+-------+-------+----------
 public | flags | table | postgres
(1 row)

pico-# \d flags
                        Table "public.flags"
  Column   |          Type          | Collation | Nullable | Default 
-----------+------------------------+-----------+----------+---------
 id        | integer                |           | not null | 
 firstname | character varying(255) |           |          | 
 lastname  | character varying(255) |           |          | 
 address   | character varying(255) |           |          | 
Indexes:
    "flags_pkey" PRIMARY KEY, btree (id)

pico-# \s

zsh: suspended  psql -h saturn.picoctf.net -p 60315 -U postgres pico
                                                                                                                   
┌──(kali㉿kali)-[~]
└─$ psql -h saturn.picoctf.net -p 60315 -U postgres pico
Password for user postgres: 
psql (14.4 (Debian 14.4-1+b1), server 14.2 (Debian 14.2-1.pgdg110+1))
Type "help" for help.

pico=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 pico      | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(4 rows)

pico=# \c pico
psql (14.4 (Debian 14.4-1+b1), server 14.2 (Debian 14.2-1.pgdg110+1))
You are now connected to database "pico" as user "postgres".
pico=# \dt
         List of relations
 Schema | Name  | Type  |  Owner   
--------+-------+-------+----------
 public | flags | table | postgres
(1 row)

pico=# SELECT * FROM flags;
 id | firstname | lastname  |                address                 
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_21c94904}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 rows)

pico=# 


```

## Referencias