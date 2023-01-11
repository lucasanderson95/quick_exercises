import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.window_height = 400
    page.window_width = 600
    
    page.title = 'Counter'
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    number = ft.TextField(value='0', 
                          width=100,
                          text_align=ft.TextAlign.CENTER)
    
    def add(e):
        number.value = str(int(number.value) + 1)
        page.update()
    
    def subtract(e):
        number.value = str(int(number.value) - 1)
        page.update()
    
    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[
                ft.IconButton(icon=ft.icons.REMOVE,
                              icon_color=ft.colors.RED,
                              on_click=subtract), 
                number, 
                ft.IconButton(icon=ft.icons.ADD,
                              icon_color=ft.colors.TEAL,
                              on_click=add)
            ]
        )
    )
    
ft.app(target=main)    
#ft.app(target=main, view=ft.WEB_BROWSER)