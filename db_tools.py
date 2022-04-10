import sqlite3


# INSERT INTO NPC ("ID", "HP", "MP","STR","INT") VALUES (2, 20, 5,5,5);

def get_conn():
    conn = sqlite3.connect("mydb.db")
    return conn


# def do_create_table():
#     conn = get_conn()
#     try:
#         sql1 = """
#         CREATE TABLE "NPC"
#             (
#             "ID" INTEGER NOT NULL,
#             "HP" INTEGER NOT NULL,
#             "MP" INTEGER NOT NULL,
#             "STR" INTEGER NOT NULL,
#             "INT" INTEGER NOT NULL,
#             PRIMARY KEY("ID" AUTOINCREMENT)
#             )
#             """
#         conn.execute(sql1)
#     finally:
#         conn.close()


def query_data_one(sql):
    conn = get_conn()
    c = conn.cursor()
    try:
        c.execute(sql)
        return c.fetchone()[0]
    finally:
        c.close()
        conn.close()


# def query_data(sql):
#     conn= get_conn()
#     c = conn.cursor()
#     try:
#         c.execute(sql)
#         return c.fetchall()
#     finally:
#         c.close()
#         conn.close()


# def insert_or_update_data(sql):
#     conn= get_conn()
#     c = conn.cursor()
#     try:
#         c.execute(sql)
#         conn.commit()
#     finally:
#         c.close()
#         conn.close()


if __name__ == '__main__':
    pass
