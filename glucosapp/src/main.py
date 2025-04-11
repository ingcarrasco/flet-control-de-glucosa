import flet as ft
import datetime


def main(page: ft.Page):
    page.title = "💉🩸 Control de glucosa 🩸💉"
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.theme_mode = "DARK"

    btn_add_glucemia = ft.TextField(label="Glucemia",hint_text="mg/dL", border_radius=20),

    def add_register():
        print(btn_add_glucemia)

    def show_home ():
        page.controls.clear()
        page.add(
            navigation_bar,
            ft.Text("Inicio")
        )

    def show_add ():
        page.controls.clear()
        page.add(
            navigation_bar,
            ft.Text("ADD"),
            ft.TextField(label="Glucemia (mg/dL)",hint_text="mg/dL", border_radius=20,input_filter=(ft.InputFilter(regex_string=r'^[0-9]*\.?[0-9]*$', allow=True))),
            ft.ElevatedButton("Guardar", on_click=add_register)            
            
        )

    def show_report ():
        page.controls.clear()
        page.add(
            navigation_bar,
            ft.Text("Report")   
        )

    def on_navigation_change(e):
        selected_index = e.control.selected_index
        print(selected_index)
        if selected_index == 0 :
            show_home()
        elif selected_index == 1 :
            show_add()
        elif selected_index == 2 :
            show_report()
        page.update()


    navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=on_navigation_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME_ROUNDED, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.icons.ADD, label="Agregar muestra"),
            ft.NavigationBarDestination(icon=ft.icons.BOOK_ROUNDED, label="Reportes"),
        ],
        bgcolor=ft.colors.BLUE_GREY_900,
        indicator_color=ft.colors.AMBER
    )



    page.add(
        navigation_bar
    )
    show_home()

ft.app(main)
