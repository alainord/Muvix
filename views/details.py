import flet as ft

# Flet compatibility shim (handles versions with ft.Colors/ft.Icons)
if not hasattr(ft, "colors") and hasattr(ft, "Colors"):
    ft.colors = ft.Colors  # type: ignore[attr-defined]
if not hasattr(ft, "icons") and hasattr(ft, "Icons"):
    ft.icons = ft.Icons  # type: ignore[attr-defined]

from components.app_bar import app_bar


def details_view(page: ft.Page, item_id: str) -> ft.View:
    return ft.View(
        route=f"/movie/{item_id}",
        controls=[
            app_bar(page, "Details", back=True),
            ft.Container(
                padding=16,
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Container(
                                    width=120,
                                    height=160,
                                    bgcolor=ft.colors.GREY_800,
                                    border_radius=12,
                                ),
                                ft.Container(width=12),
                                ft.Column(
                                    [
                                        ft.Text(
                                            f"Title #{item_id}",
                                            size=24,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        ft.Text("Action • 2024 • 2h 10m", color=ft.colors.WHITE70),
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
                                    ],
                                    spacing=8,
                                ),
                            ]
                        ),
                        ft.Container(height=12),
                        ft.Text("Synopsis", size=16, weight=ft.FontWeight.W_600),
                        ft.Text(
                            "Placeholder description for the selected title. "
                            "We’ll swap this with real content mapped from your data later.",
                            color=ft.colors.WHITE70,
                        ),
                    ],
                    expand=False,
                ),
            ),
        ],
        padding=0,
        bgcolor=ft.colors.BACKGROUND,
    )
