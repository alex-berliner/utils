from enum import IntEnum
from collections import OrderedDict
import sqlite3

class DBField():
    def __init__(self, field_name, field_type, field_primary=False):
        self.field_name = field_name
        self.field_type = field_type
        self.field_primary = field_primary

class DBTable():
    def __init__(self, table_name, fields):
        self.table_name = table_name
        self.fields = fields
        field_str = []
        FIELD_TEMPLATE = "%s %s NOT NULL"
        for field in self.fields:
            line = FIELD_TEMPLATE%(field.field_name, field.field_type)
            field_str += [line]
        primary_key_str = (", ".join([x.field_name for x in self.fields if x.field_primary == True]),)
        insert_field_str = " ".join(["%d," if (x.field_type == "INTEGER") else "'%s'," for x in self.fields]).strip(", ")
        field_str+=[""]
        DBCMD_ARGS_MAKE_REAG_TABLE=(self.table_name,) + (",\n".join(field_str),) + primary_key_str

        self.DBCMD_MAKE_TABLE =\
             """ CREATE TABLE %s (\n%s PRIMARY KEY (%s) ); """ % DBCMD_ARGS_MAKE_REAG_TABLE

        self.DBCMD_INST_ELEM =\
             """REPLACE INTO %s VALUES (%s)""" %(self.table_name, insert_field_str)

        self.DBCMD_DROP_TABLE =\
             """DROP TABLE IF EXISTS %s;"""%self.table_name

        self.DBCMD_TABLE_EXISTS =\
             """SELECT name FROM sqlite_master WHERE type= 'table' AND name= '%s';"""%(self.table_name)

        self.DBCMD_ADD_COLUMN =\
             """ALTER TABLE %s ADD %%s %%s"""%(self.table_name)

    def table_exists(self, conn):
        r=conn.execute(self.DBCMD_TABLE_EXISTS)
        return len(list(r))>0

    def drop_table(self, conn):
        input("Dropping table %s, press enter to continue"%self.table_name)
        conn.executescript(self.DBCMD_DROP_TABLE)

    def create_table(self, conn):
        # Check for updates to table fields
        # Add additional fields to end of table if any exist
        if self.table_exists(conn):
            current_cols = self.get_columns(conn)
            for field in self.fields:
                if field.field_name not in current_cols:
                    self.add_column(conn, field)
        else:
            print("Creating table %s" % self.table_name)
            conn.executescript(self.DBCMD_MAKE_TABLE)

    def get_columns(self, conn):
        get_col_exec_str="""PRAGMA table_info(%s);"""%(self.table_name)
        res = list(conn.execute(get_col_exec_str))
        return list(x[1] for x in res)

    def get_row_count(self, conn):
        count = conn.execute("""SELECT COUNT(*) FROM %s"""%self.table_name)
        return list(count)[0][0]

    def add_column(self, conn, dbfield):
        input("Adding column %s to %s, press enter to continue"%(dbfield.field_name, self.table_name))
        conn.execute(self.DBCMD_ADD_COLUMN%(dbfield.field_name, dbfield.field_type))

    def add_entry(self, conn, elem_tuple):
        conn.execute(self.DBCMD_INST_ELEM%(elem_tuple))

    def dump(self, conn):
        conts = list(conn.execute(""" SELECT * FROM %s""" % self.table_name))
        print(conts)
