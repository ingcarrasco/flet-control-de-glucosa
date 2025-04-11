import flet as ft
import datetime


def main(page: ft.Page):
    page.title = "💉🩸 Control de glucosa 🩸💉"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.theme_mode = "DARK"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    

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
            ft.TextField(label="Glucemia (mg/dL)",hint_text="mg/dL", border_radius=20,input_filter=(ft.InputFilter(regex_string=r'^[0-9]*\.?[0-9]*$', allow=True))),
            ft.TextField(label="Metformina (Capsulas)",hint_text="Capsulas", border_radius=20,input_filter=(ft.InputFilter(regex_string=r'^[0-9]*\.?[0-9]*$', allow=True))),
            ft.TextField(label="Insulina (Unidades)",hint_text="Unidades", border_radius=20,input_filter=(ft.InputFilter(regex_string=r'^[0-9]*\.?[0-9]*$', allow=True))),
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
            ft.NavigationBarDestination(icon=ft.Icons.HOME_ROUNDED, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD, label="Agregar muestra"),
            ft.NavigationBarDestination(icon=ft.Icons.BOOK_ROUNDED, label="Reportes"),
        ],
        bgcolor=ft.Colors.BLUE_GREY_900,
        indicator_color=ft.Colors.AMBER
    )



    page.add(
        navigation_bar
    )
    show_home()

ft.app(main)
