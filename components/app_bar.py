import flet as ft

# Flet compatibility shim (handles versions with ft.Colors/ft.Icons)
if not hasattr(ft, "colors") and hasattr(ft, "Colors"):
    ft.colors = ft.Colors  # type: ignore[attr-defined]
if not hasattr(ft, "icons") and hasattr(ft, "Icons"):
    ft.icons = ft.Icons  # type: ignore[attr-defined]


def app_bar(page: ft.Page, title: str, back: bool = False) -> ft.AppBar:
    actions = [
        ft.IconButton(ft.Icons.SEARCH, tooltip="Search", on_click=lambda e: page.go("/search")),
        ft.IconButton(ft.Icons.NOTIFICATIONS_OUTLINED, tooltip="Notifications"),
    ]
    leading = (
        ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/"))
        if back
        else None
    )
    return ft.AppBar(
        leading=leading,
        title=ft.Text(title),
        center_title=False,
        bgcolor=ft.colors.SURFACE,
        actions=actions if not back else None,
    )

