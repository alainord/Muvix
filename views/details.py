import flet as ft
from data.movies_mock import movies_mock
from components.app_bar import app_bar


def details_view(page: ft.Page, item_id: str) -> ft.View:
    # Convertir ID (viene como str)
    item_id = int(item_id)

    movie = next((m for m in movies_mock if m["id"] == item_id), None)

    if not movie:
        return ft.View(
            route=f"/movie/{item_id}",
            controls=[
                app_bar(page, "Not found", back=True),
                ft.Container(padding=16, content=ft.Text("Movie not found")),
            ],
            padding=0,
            bgcolor=ft.colors.BACKGROUND,
        )

    # ---------------------------------------------------
    #  PANTALLA DE DETALLES – IMAGEN DE FONDO + TEXTO
    # ---------------------------------------------------
    return ft.View(
        route=f"/movie/{item_id}",
        padding=0,
        bgcolor=ft.colors.BLACK,
        controls=[
            ft.Stack(
                [
                    # 1️⃣ Imagen FULLSCREEN detrás
                    ft.Image(
                        src=movie['backdrop'],
                        fit=ft.ImageFit.COVER,
                        width=page.width,
                        height=page.height,
                        opacity=1.0,
                    ),

                    # 2️⃣ Capa de degradado para que se lea bien el texto
                    ft.Container(
                        width=page.width,
                        height=page.height,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[
                                ft.colors.TRANSPARENT,
                                ft.colors.BLACK45,
                                ft.colors.BLACK87,
                            ],
                        ),
                    ),

                    # 3️⃣ Contenido encima del fondo
                   ft.Container(
                        width=600,
                        alignment=ft.alignment.bottom_center,
                        padding=50,
                        content=ft.Column(
                            [
                                ft.Text(
                                    movie["title"],
                                    size=50,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.colors.WHITE,
                                ),
                                ft.Text(
                                    movie["genre"],
                                    size=24,
                                    color=ft.colors.WHITE70,
                                ),

                                ft.Container(height=10),
                                
                                  ft.FilledButton(
                                    "Play",
                                    icon=ft.icons.PLAY_ARROW,
                                    height=42,      # MÁS FINO
                                    width=150,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=6),
                                        color=ft.colors.BLACK,
                                        bgcolor=ft.colors.WHITE,
                                        padding=ft.Padding(10, 5, 10, 5),
                                    ),
                                ),

                                ft.Text(
                                    movie.get("description", ""),
                                    size=20,
                                    color=ft.colors.WHITE,
                                    max_lines=4,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                ),

                                ft.Container(height=20),

                                # 4️⃣ Botón Play estrecho

                                ft.Container(height=20),
                            ],
                            spacing=4,
                        ),
                    ),

                    # 5️⃣ Botón BACK arriba (pero sin mover el contenido)
                    ft.Container(
                        padding=16,
                        alignment=ft.alignment.top_left,
                        content=ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            icon_color=ft.colors.WHITE,
                            on_click=lambda e: page.go("/")
                        )
                    ),
                ]
            )
        ]
    )
