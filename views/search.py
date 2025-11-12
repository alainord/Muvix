import flet as ft

# Flet compatibility shim (handles versions with ft.Colors/ft.Icons)
if not hasattr(ft, "colors") and hasattr(ft, "Colors"):
    ft.colors = ft.Colors  # type: ignore[attr-defined]
if not hasattr(ft, "icons") and hasattr(ft, "Icons"):
    ft.icons = ft.Icons  # type: ignore[attr-defined]

from components.app_bar import app_bar


def search_view(page: ft.Page) -> ft.View:
    def on_search(e: ft.ControlEvent) -> None:
        query = (search.value or "").strip().lower()
        results.controls.clear()
        if query:
            for i in range(12):
                results.controls.append(
                    ft.Container(
                        bgcolor=ft.colors.SURFACE,
                        border_radius=12,
                        content=ft.Column(
                            [
                                ft.Container(
                                    height=120,
                                    bgcolor=ft.colors.GREY_800,
                                    border_radius=12,
                                ),
                                ft.Text(f"Result {i+1}", size=12),
                            ],
                            spacing=6,
                        ),
                        padding=8,
                    )
                )
        page.update()

    search = ft.TextField(
        hint_text="Search movies, shows...",
        prefix_icon=ft.Icons.SEARCH,
        on_submit=on_search,
        filled=True,
        border_radius=12,
    )

    results = ft.GridView(
        runs_count=2,
        max_extent=None,
        child_aspect_ratio=0.75,
        spacing=12,
        run_spacing=12,
        expand=True,
    )

    return ft.View(
        route="/search",
        controls=[
            app_bar(page, "Search"),
            ft.Container(padding=12, content=ft.Column([search, results], expand=True)),
        ],
        padding=0,
        bgcolor=ft.colors.BACKGROUND,
    )
