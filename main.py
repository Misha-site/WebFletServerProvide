import flet as ft
from parser import parse_site_get, parse_site_post, parse_site_post_delete

def main(page: ft.Page):
    page.title = "WebFletParser"
    page.window.height = 900
    page.window.width = 1500
    page.window.resizable = False
    page.window.maximizable = False
    page.window.center()
    page.bgcolor = "#000000"

    def get_waiting_values(e):
        waiting_values_int = int(e.control.value)
        for i in range(waiting_values_int):
            info_key_ = ft.TextField(width=200, border_color="white", color="white", text_style=ft.TextStyle(size=24))
            info_value_ = ft.TextField(width=500, border_color="white", color="white", text_style=ft.TextStyle(size=24))

            left_column.controls.append(ft.Text(f"Информация-{i+1} (ключ):", color="white", size=20))
            left_column.controls.append(info_key_)
            left_column.controls.append(ft.Text(f"Информация-{i+1} (значение):", color="white", size=20))
            left_column.controls.append(info_value_)

            waiting_values_key_field.append(info_key_)
            waiting_values_value_field.append(info_value_)
        page.update()

    site_url = ft.TextField(width=500, border_color="white", color="white", text_style=ft.TextStyle(size=24))
    element = ft.TextField(width=200, border_color="white", color="white", text_style=ft.TextStyle(size=24))
    class_ = ft.TextField(width=200,border_color="white",color="white",text_style=ft.TextStyle(size=24))
    id_ = ft.TextField(width=200,border_color="white",color="white",text_style=ft.TextStyle(size=24))
    headers_key = ft.TextField(width=300,border_color="white",color="white",text_style=ft.TextStyle(size=24))
    headers_value = ft.TextField(width=300,border_color="white",color="white",text_style=ft.TextStyle(size=24))

    waiting_values = ft.TextField(width=100, on_change=get_waiting_values ,border_color="white", color="white", text_style=ft.TextStyle(size=24))

    waiting_values_key_field = []
    waiting_values_value_field = []

    result_column = ft.Column(
        controls=[],
        scroll="auto",
        expand=True,
        spacing=10
    )
    left_column = ft.Column(
        controls=[],
        scroll="auto",
        expand=True,
        spacing=10
    )

    def app_req_get(e):
        page.clean()
        page.add(
            ft.Row(
                controls=[
                    # Левая колонка: поля ввода
                    ft.Column(
                        controls=[
                            ft.ElevatedButton("Назад", on_click=go_to_main_menu,style=ft.ButtonStyle(padding=ft.Padding(20, 10, 20, 10),
                                                                   text_style=ft.TextStyle(size=35))),
                            ft.Text("URL сайта:", color="white", size=20), site_url,
                            ft.Text("HTML-элемент:", color="white", size=20), element,
                            ft.Text("Класс элемента:", color="white", size=20), class_,
                            ft.Text("ID элемента:", color="white", size=20), id_,
                            ft.Text("Заголовки (ключ):", color="white", size=20), headers_key,
                            ft.Text("Заголовки (значение):", color="white", size=20), headers_value,
                            ft.ElevatedButton("Парсить", on_click=new_parse_window,
                                              style=ft.ButtonStyle(padding=ft.Padding(20, 10, 20, 10),
                                                                   text_style=ft.TextStyle(size=35)))

                        ],
                        width=600,
                        spacing=10,
                        expand=True,
                        scroll="auto",
                    ),
                    # Правая колонка: вывод результата
                    ft.Column(
                        controls=[ft.Text("Результаты парсинга:", size=25, color="white", text_align=ft.TextAlign.RIGHT),
                                  result_column],
                        expand=True,
                        scroll="auto",
                        spacing=10
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.START
            )
        )

    def app_req_post(e):
        page.clean()
        page.add(
            ft.Row(
                controls=[
                    # Левая колонка: поля ввода с прокруткой
                    ft.Container(
                        width=600,
                        height=800,  # фиксированная высота
                        content=ft.Column(
                            scroll="auto",
                            controls=[
                                ft.ElevatedButton("Назад", on_click=go_to_main_menu,
                                                  style=ft.ButtonStyle(
                                                      padding=ft.Padding(20, 10, 20, 10),
                                                      text_style=ft.TextStyle(size=35))),
                                ft.Text("URL сервера:", color="white", size=20), site_url,
                                ft.Text("Кол-во ожидаемых переменных:", color="white", size=20), waiting_values,
                                left_column,
                                ft.Text("Заголовки (ключ):", color="white", size=20), headers_key,
                                ft.Text("Заголовки (значение):", color="white", size=20), headers_value,
                                ft.ElevatedButton("Парсить", on_click=new_post_req,
                                                  style=ft.ButtonStyle(
                                                      padding=ft.Padding(20, 10, 20, 10),
                                                      text_style=ft.TextStyle(size=35)))
                            ],
                            spacing=10
                        )
                    ),
                    # Правая колонка: вывод результата
                    ft.Column(
                        controls=[
                            ft.Text("Результаты парсинга:", size=25, color="white", text_align=ft.TextAlign.RIGHT),
                            result_column
                        ],
                        expand=True,
                        scroll="auto",
                        spacing=10
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.START
            )
        )

    def new_delete_post(e):
        result_column.controls.clear()

        response = parse_site_post_delete(
            site=site_url.value,
            headers_key=headers_key.value,
            headers_value=headers_value.value
        )

        for item in response:
            result_column.controls.append(ft.Text(item, color="white", size=20))

        page.update()

    def app_req_clear(e):
        page.clean()
        page.add(
            ft.Row(
                controls=[
                    # Левая колонка: поля ввода с прокруткой
                    ft.Container(
                        width=600,
                        height=800,  # фиксированная высота
                        content=ft.Column(
                            scroll="auto",
                            controls=[
                                ft.ElevatedButton("Назад", on_click=go_to_main_menu,
                                                  style=ft.ButtonStyle(
                                                      padding=ft.Padding(20, 10, 20, 10),
                                                      text_style=ft.TextStyle(size=35))),
                                ft.Text("URL сервера:", color="white", size=20), site_url,
                                ft.Text("Заголовки (ключ):", color="white", size=20), headers_key,
                                ft.Text("Заголовки (значение):", color="white", size=20), headers_value,
                                ft.ElevatedButton("Парсить", on_click=new_delete_post,
                                                  style=ft.ButtonStyle(
                                                      padding=ft.Padding(20, 10, 20, 10),
                                                      text_style=ft.TextStyle(size=35)))
                            ],
                            spacing=10
                        )
                    ),
                    # Правая колонка: вывод результата
                    ft.Column(
                        controls=[
                            ft.Text("Результаты парсинга:", size=25, color="white", text_align=ft.TextAlign.RIGHT),
                            result_column
                        ],
                        expand=True,
                        scroll="auto",
                        spacing=10
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.START
            )
        )

    main_menu = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        expand=True,
                        content=ft.Text("FletAppParser | Главная", text_align=ft.TextAlign.CENTER, size=35,
                                        color="white")
                    )
                ]
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        margin=ft.Margin(0, 100, 0, 0),
                        expand=True,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.ElevatedButton(
                                    text="GET парсинг",
                                    on_click=app_req_get,
                                    style=ft.ButtonStyle(
                                        padding=ft.Padding(20, 10, 20, 10),
                                        text_style=ft.TextStyle(size=45)
                                    )
                                ),
                                ft.ElevatedButton(
                                    text="POST запрос",
                                    on_click=app_req_post,
                                    style=ft.ButtonStyle(
                                        padding=ft.Padding(20, 10, 20, 10),
                                        text_style=ft.TextStyle(size=45)
                                    )
                                ),
                                ft.ElevatedButton(
                                    text="DELETE парсинг (бд)",
                                    on_click=app_req_clear,
                                    style=ft.ButtonStyle(
                                        padding=ft.Padding(20, 10, 20, 10),
                                        text_style=ft.TextStyle(size=45)
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        ]
    )

    def go_to_main_menu(e):
        page.clean()
        page.add(main_menu)

    def new_parse_window(e):
        result_column.controls.clear()

        response = parse_site_get(
            site=site_url.value,
            html_elem=element.value,
            id_elem=id_.value,
            class_elem=class_.value,
            headers_key=headers_key.value,
            headers_value=headers_value.value
        )

        for item in response:
            result_column.controls.append(ft.Text(item, color="white", size=20))

        page.update()

    def new_post_req(e):
        result_column.controls.clear()

        keys = [field.value for field in waiting_values_key_field]
        values = [field.value for field in waiting_values_value_field]

        response = parse_site_post(
            site=site_url.value,
            info_keys=keys,
            info_vales=values,
            headers_key=headers_key.value,
            headers_value=headers_value.value
        )

        for item in response:
            result_column.controls.append(ft.Text(item, color="white", size=20))

        page.update()



    # Главное меню
    page.add(main_menu)

# , view=ft.AppView.WEB_BROWSER
ft.app(target=main, view=ft.AppView.WEB_BROWSER)