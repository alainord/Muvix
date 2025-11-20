import flet as ft

# Flet compatibility shim (handles versions with ft.Colors/ft.Icons)
if not hasattr(ft, "colors") and hasattr(ft, "Colors"):
    ft.colors = ft.Colors  # type: ignore[attr-defined]
if not hasattr(ft, "icons") and hasattr(ft, "Icons"):
    ft.icons = ft.Icons  # type: ignore[attr-defined]

from components.app_bar import app_bar
from views.data import MOVIES


def home_section(page: ft.Page, title: str, items: list[dict[str, str]]) -> ft.Column:
    chips = []

    for i in items:
        chips.append(
            ft.Container(
                bgcolor=ft.colors.SURFACE,
                border_radius=12,
                padding=8,
                width=160,
                on_click=lambda e, movie_id=i["id"]: page.go(f"/movie/{movie_id}"),
                content=ft.Column(
                    [
                        # Imagen del poster (pequeña)
                        ft.Container(
                            height=120,
                            border_radius=12,
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            content=ft.Image(
                                src=f"assets/{i['poster']}",   # ← cambiado aquí
                                fit=ft.ImageFit.COVER,
                            ),
                        ),
                        # Título
                        ft.Text(
                            i["title"],
                            size=12,
                            color=ft.colors.WHITE70
                        ),
                    ],
                    spacing=6,
                    tight=True,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                ),
            )
        )

    return ft.Column(
        [
            ft.Row(
                [
                    ft.Text(title, size=18, weight=ft.FontWeight.W_700),
                    ft.Container(expand=True),
                    ft.TextButton("See all", data=title, on_click=lambda e: None),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            ft.Row(
                chips,
                scroll=ft.ScrollMode.ALWAYS,
                spacing=12,
            ),
        ],
        spacing=10,
    )


def banner() -> ft.Container:
    return ft.Container(
        height=180,
        border_radius=16,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.colors.DEEP_PURPLE_700, ft.colors.INDIGO_700],
        ),
        content=ft.Stack(
            [
                ft.Container(
                    padding=16,
                    content=ft.Column(
                        [
                            ft.Text("Featured", size=12, color=ft.colors.WHITE70),
                            ft.Text(
                                "Muvix Originals",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.WHITE,
                            ),
                            ft.Text(
                                "New episodes every Friday",
                                size=12,
                                color=ft.colors.WHITE70,
                            ),
                            ft.Row(
                                [
                                    ft.FilledButton("Watch now", icon=ft.Icons.PLAY_ARROW),
                                    ft.OutlinedButton("Details"),
                                ],
                                spacing=10,
                            ),
                        ],
                        spacing=8,
                        tight=True,
                    ),
                )
            ]
        ),
    )


def home_view(page: ft.Page) -> ft.View:
    # Las listas reales vienen de data.py
    movie_list = list(MOVIES.values())

    body = ft.ListView(
        controls=[
            ft.Container(height=8),
            banner(),
            ft.Container(height=16),
            home_section(page, "Trending now", movie_list),
            ft.Container(height=6),
            home_section(page, "Because you watched", movie_list),
            ft.Container(height=6),
            home_section(page, "Recommended for you", movie_list),
            ft.Container(height=16),
        ],
        spacing=0,
        auto_scroll=False,
    )

    return ft.View(
        route="/",
        controls=[
            app_bar(page, "Muvix"),
            ft.Container(padding=12, content=body, expand=True),
        ],
        padding=0,
        bgcolor=ft.colors.BACKGROUND,
    )
