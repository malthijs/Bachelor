"""
Auteur: Matthijs de Vries
"""
import psycopg2
from psycopg2._psycopg import cursor


def verwijder_tabellen(cursor: psycopg2.extensions.cursor):
    """
    :return:
    """
    sql = """
    DROP TABLE IF EXISTS county CASCADE;
    DROP TABLE IF EXISTS taxonomy CASCADE;
    DROP TABLE IF EXISTS subtax CASCADE;
    DROP TABLE IF EXISTS status CASCADE;
    DROP TABLE IF EXISTS biological_entity CASCADE;
    DROP TABLE IF EXISTS sighting CASCADE;"""
    cursor.execute(sql)


def maak_tabellen(cursor: psycopg2.extensions.cursor):
    """
    :return:
    """
    sql = """
    CREATE TABLE county(
    county_name VARCHAR(50) PRIMARY KEY
    );

    CREATE TABLE taxonomy(
    tax_name VARCHAR(50) PRIMARY KEY
    );

    CREATE TABLE subtax(
    subtax_name VARCHAR(50) PRIMARY KEY,
    tax_name VARCHAR(50) REFERENCES taxonomy(tax_name)
    );

    CREATE TABLE status(
    description VARCHAR(50) PRIMARY KEY
    );

    CREATE TABLE biological_entity(
    scientific_name VARCHAR(50) PRIMARY KEY,
    common_name VARCHAR(50),
    subtax_name VARCHAR(50) REFERENCES subtax(subtax_name),
    description VARCHAR(50) REFERENCES status(description)
    );

    CREATE TABLE sighting(
    county_name VARCHAR(50) REFERENCES county(county_name),
    scientific_name VARCHAR(50) REFERENCES biological_entity(scientific_name),
    year DATE,
    PRIMARY KEY(county_name, scientific_name));"""
    cursor.execute(sql)


def county_tabel(cursor: psycopg2.extensions.cursor,
                 info: list[int | str]):
    """
    :return: 
    """""
    sql = """INSERT INTO county(county_name)
    VALUES (%s)
    ON CONFLICT DO NOTHING;"""
    data = [info[0]]
    cursor.execute(sql, data)


def taxonomy_tabel(cursor: psycopg2.extensions.cursor,
                   info: list[int | str]):
    """
    :return:
    """
    sql = """INSERT INTO taxonomy(tax_name)
    VALUES (%s)
    ON CONFLICT DO NOTHING;"""
    data = [info[5]]
    cursor.execute(sql, data)


def subtax_tabel(cursor: psycopg2.extensions.cursor,
                 info: list[int | str]):
    """
    :return:
    """
    sql = """INSERT INTO subtax(subtax_name, tax_name)
    VALUES (%s, %s)
    ON CONFLICT DO NOTHING;"""
    data = [info[4], info[5]]
    cursor.execute(sql, data)


def status_tabel(cursor: psycopg2.extensions.cursor,
                 info: list[int | str]):
    """
    :return:
    """
    sql = """INSERT INTO status(description)
    VALUES (%s)
    ON CONFLICT DO NOTHING;"""
    data = [info[6]]
    cursor.execute(sql, data)


def biological_entity_tabel(cursor: psycopg2.extensions.cursor,
                            info: list[int | str]):
    """
    :return:
    """
    sql = """INSERT INTO biological_entity(scientific_name, common_name, subtax_name, description)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT DO NOTHING;"""
    data = [info[1], info[2], info[4], info[6]]
    cursor.execute(sql, data)


def sighting_tabel(cursor: psycopg2.extensions.cursor,
                   info: list[int | str | None]):
    """
    :return:
    """
    sql = """INSERT INTO sighting(county_name, scientific_name, year)
    VALUES (%s, %s, %s)
    ON CONFLICT DO NOTHING;"""
    if info[3] == "NA":
        info[3] = None
    else:
        info[3] += "-01-01"
    data = [info[0], info[1], info[3]]
    cursor.execute(sql, data)


def main():
    """
    :return:
    """
    conn = psycopg2.connect(host='145.97.18.240',
                            dbname='s1128088_db',
                            user='s1128088',
                            password='s1128088')
    cursor = conn.cursor()
    try:
        verwijder_tabellen(cursor)
        maak_tabellen(cursor)
        with open("biodiversity.tsv") as file:
            _ = file.readline()
            lines = file.readlines()
        for line in lines:
            info = line.strip("\n").split("\t")
            county_tabel(cursor, info)
            taxonomy_tabel(cursor, info)
            subtax_tabel(cursor, info)
            status_tabel(cursor, info)
            biological_entity_tabel(cursor, info)
            sighting_tabel(cursor, info)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        conn.close()


if __name__ == "__main__":
    main()
