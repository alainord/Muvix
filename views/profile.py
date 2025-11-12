import flet as ft

# Flet compatibility shim (handles versions with ft.Colors/ft.Icons)
if not hasattr(ft, "colors") and hasattr(ft, "Colors"):
    ft.colors = ft.Colors  # type: ignore[attr-defined]
if not hasattr(ft, "icons") and hasattr(ft, "Icons"):
    ft.icons = ft.Icons  # type: ignore[attr-defined]

from components.app_bar import app_bar


def profile_view(page: ft.Page) -> ft.View:
    return ft.View(
        route="/profile",
        controls=[
            app_bar(page, "Profile"),
            ft.Container(
                padding=16,
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.CircleAvatar(
                                    bgcolor=ft.colors.DEEP_PURPLE_200,
                                    content=ft.Icon(ft.Icons.PERSON, color=ft.colors.BLACK),
                                    radius=28,
                                ),
                                ft.Column(
                                    [
                                        ft.Text("Your Name", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Premium plan", size=12, color=ft.colors.WHITE70),
                                    ]
                                ),
                            ],
                            spacing=12,
                        ),
                        ft.Divider(opacity=0.3),
                        ft.ListTile(leading=ft.Icon(ft.Icons.DOWNLOAD), title=ft.Text("Downloads")),
                        ft.ListTile(leading=ft.Icon(ft.Icons.BOOKMARK), title=ft.Text("Watchlist")),
                        ft.ListTile(leading=ft.Icon(ft.Icons.SETTINGS), title=ft.Text("Settings")),
                        ft.ListTile(leading=ft.Icon(ft.Icons.LOGOUT), title=ft.Text("Sign out")),
                    ],
                    spacing=8,
                    tight=False,
                ),
                expand=True,
            ),
        ],
        padding=0,
        bgcolor=ft.colors.BACKGROUND,
    )
