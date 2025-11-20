from views.data import MOVIES
import flet as ft
from components.app_bar import app_bar


def details_view(page: ft.Page, item_id: str) -> ft.View:
    movie = MOVIES.get(item_id)

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

    return ft.View(
        route=f"/movie/{item_id}",
        padding=0,
        bgcolor=ft.colors.BACKGROUND,
        controls=[
            app_bar(page, movie["title"], back=True),

            # --- Backdrop grande ---
            ft.Container(
                height=260,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                content=ft.Stack(
                    [
                        # Imagen horizontal grande
                        ft.Image(
                            src=f"assets/{movie['backdrop']}",
                            fit=ft.ImageFit.COVER,
                            width=float("inf"),
                        ),

                        # Degradado para legibilidad (opcional)
                        ft.Container(
                            gradient=ft.LinearGradient(
                                begin=ft.Alignment(0, -1),
                                end=ft.Alignment(0, 1),
                                colors=[
                                    ft.colors.with_opacity(0.0, ft.colors.BLACK),
                                    ft.colors.with_opacity(0.8, ft.colors.BLACK),
                                ],
                            )
                        )
                    ]
                )
            ),

            # --- Contenido principal ---
            ft.Container(
                padding=16,
                content=ft.Column(
                    [
                        ft.Text(
                            movie["title"],
                            size=28,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(
                            f"{movie['genre']} • {movie['year']} • {movie['runtime']}",
                            size=14,
                            color=ft.colors.WHITE70,
                        ),
                        ft.Container(height=12),

                        ft.Row(
                            [
                                ft.FilledButton("Play", icon=ft.Icons.PLAY_ARROW),
                                ft.OutlinedButton(
                                    "Add to list",
                                    icon=ft.Icons.BOOKMARK_ADD_OUTLINED,
                                ),
                            ],
                            spacing=10,
                        ),

                        ft.Container(height=16),

                        ft.Text(
                            movie["description"],
                            size=14,
                            color=ft.colors.WHITE70,
                        ),
                    ],
                    spacing=8,
                ),
            ),
        ],
    )
