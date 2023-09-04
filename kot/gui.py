#!/usr/bin/python3
# -*- coding: utf-8 -*-
import flet as ft

from .kot import KOT_Serial
from .kot import KOT

folder = None
host = None
port = None
password = None
def database_list(page: ft.Page):
    page.scroll = "AUTO"
    global folder


    def delete_key(database, key):
        KOT_Serial(database,folder=folder).delete(key)
        page.show_snack_bar(
                    ft.SnackBar(ft.Text("Key deleted"), open=True)
                )
        get_all(database)
    
    def create_new_key(database):
        def create_new_key_submit(e):
            the_value = text_field_2.value
            try:
                the_value = float(the_value)
            except:
                pass
            KOT_Serial(database, folder=folder).set(text_field.value, the_value)
            page.show_snack_bar(
                    ft.SnackBar(ft.Text("Key created"), open=True)
                )
            get_all(database)
            text_field.value = ""
            text_field_2.value = ""
            page.remove(text_field)
            page.remove(text_field_2)

        text_field = ft.TextField(label="New Key")
        text_field_2 = ft.TextField(label="Value", on_submit=lambda e: create_new_key_submit(e))
        page.add(text_field)
        page.add(text_field_2)

    def get_all(database):
        database_list_data = KOT_Serial(database,folder=folder).get_all()
        my_table_2.rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(key)),
                            ft.DataCell(ft.Text(database_list_data[key])),
                            ft.DataCell(ft.Text("Delete"), on_tap=lambda e: delete_key(database, key)),
                        ],
                    ) for key in database_list_data]
        my_table_2.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Create or Edit Key"), on_tap=lambda e: create_new_key(database)),
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                        ], 
                    )
        )
        page.show_snack_bar(
                    ft.SnackBar(ft.Text("Database list updated"), open=True)
                )        
        page.update()



    def rename_database(old_name):
        def rename_database_submit(e):
            KOT.database_rename(old_name, text_field.value, folder=folder)
            page.show_snack_bar(
                    ft.SnackBar(ft.Text("Database renamed"), open=True)
                )
            fab_pressed(None)
            get_all(text_field.value )
            text_field.value = ""
            page.remove(text_field)

        text_field = ft.TextField(label="New Name", on_submit=lambda e: rename_database_submit(e))
        page.add(text_field)


    def create_new_db():
        def create_new_db_submit(e):
            KOT_Serial(text_field.value, folder=folder)
            page.show_snack_bar(
                    ft.SnackBar(ft.Text("Database created"), open=True)
                )
            fab_pressed(None)
            get_all(text_field.value )
            text_field.value = ""
            page.remove(text_field)

        text_field = ft.TextField(label="New DB Name", on_submit=lambda e: create_new_db_submit(e))
        page.add(text_field)

    def delete_database(database):
        KOT.database_delete(database, folder=folder)
        page.show_snack_bar(
                    ft.SnackBar(ft.Text("Database deleted"), open=True)
                )
        fab_pressed(None)
        my_table_2.rows = []
        page.update()

    def pop_database(database):
        KOT.database_pop(database, folder=folder)
        page.show_snack_bar(
                    ft.SnackBar(ft.Text("Database popped"), open=True)
                )
        fab_pressed(None)
        my_table_2.rows = []
        page.update()

    def delete_database_all():
        KOT.database_delete_all(folder=folder)
        page.show_snack_bar(
                    ft.SnackBar(ft.Text("All databases deleted"), open=True)
                )
        fab_pressed(None)
        my_table_2.rows = []
        page.update()

    def pop_database_all():
        KOT.database_pop_all(folder=folder)
        page.show_snack_bar(
                    ft.SnackBar(ft.Text("All databases popped"), open=True)
                )
        fab_pressed(None)
        my_table_2.rows = []
        page.update()

    def fab_pressed(e):
        database_list_data = KOT.database_list(folder)
        my_table.rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(database), 
                                        on_tap=lambda e, database=database: get_all(database),
                                        on_long_press=lambda e, database=database: rename_database(database)),
                            ft.DataCell(ft.Text(database_list_data[database])),
                            ft.DataCell(ft.Text("Delete"), on_tap=lambda e, database=database: delete_database(database)),
                            ft.DataCell(ft.Text("Pop"), on_tap=lambda e, database=database: pop_database(database)),
                            
                        ],
                    ) for database in database_list_data]
        my_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Create New Database"), on_tap=lambda e: create_new_db()),
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                        ],
                    )
        )
        my_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Delete All Databases"), on_tap=lambda e: delete_database_all()),
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                        ],
                    )
        )
        my_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Pop All Databases"), on_tap=lambda e: pop_database_all()),
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                        ],
                    )
        )
        page.show_snack_bar(
                    ft.SnackBar(ft.Text("Database list updated"), open=True)
                )        
        page.update()
    


    my_table = ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Name")),
                    ft.DataColumn(ft.Text("Location")),
                    ft.DataColumn(ft.Text("Delete")),
                    ft.DataColumn(ft.Text("Pop")),
                ],
            )
    my_table_2 = ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Key")),
                    ft.DataColumn(ft.Text("Value")),
                    ft.DataColumn(ft.Text("Delete")),
                ],
            )
    

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=fab_pressed, bgcolor=ft.colors.LIME_300
    )
    page.add(ft.Text("Press the + button to refresh the list."))

    def execute(e):
        result = KOT.execute(query.value)
        page.show_snack_bar(
                    ft.SnackBar(ft.Text(str(result)), open=True)
                )
        fab_pressed(None)
    query = ft.TextField(label="Query for Execution", on_submit=lambda e: execute(e))

    page.add(query)

    page.add(my_table,)
    page.add(my_table_2,)

    fab_pressed(None)
        



def login(page: ft.Page,):
    global host
    global port
    global password
    def login_submit(e):
        if password == text_field.value:
            page.show_snack_bar(
                    ft.SnackBar(ft.Text("Login successful"), open=True)
                )
            page.remove(text_field)
            database_list(page)
            
    
    text_field = ft.TextField(label="Password", on_submit=lambda e: login_submit(e))
    page.add(text_field)



def GUI(folder_data, password_data):
    global folder
    global password
    folder = folder_data
    password = password_data
    ft.app(name="KOT", target=login)

def WEB(folder_data, password_data, host_data, port_data):
    global folder
    global host
    global port
    global password
    folder = folder_data
    host = host_data
    port = port_data
    password = password_data
    ft.app(name="KOT", target=login, view=ft.AppView.WEB_BROWSER, host=host, port=port)
