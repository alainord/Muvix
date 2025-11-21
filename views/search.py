import flet as ft

# Flet compatibility shim (handles versions with ft.Colors/ft.Icons)
if not hasattr(ft, "colors") and hasattr(ft, "Colors"):
    ft.colors = ft.Colors  # type: ignore[attr-defined]
if not hasattr(ft, "icons") and hasattr(ft.Icons):
    ft.icons = ft.Icons  # type: ignore[attr-defined]

from components.app_bar import app_bar
from data.movies_mock import movies_mock


def search_view(page: ft.Page) -> ft.View:

    # -------------------------
    #   FUNCIÓN DE BÚSQUEDA
    # -------------------------
    def on_search(e: ft.ControlEvent):
        query = (search.value or "").strip().lower()
        results.controls.clear()

        if query:
            filtered = [
                m for m in movies_mock
                if query in m["title"].lower()
            ]

            for movie in filtered:
                results.controls.append(
                    ft.Container(
                        bgcolor=ft.colors.SURFACE,
                        border_radius=12,
                        padding=8,
                        on_click=lambda e, mid=movie["id"]: page.go(f"/movie/{mid}"),
                        content=ft.Column(
                            [
                                ft.Container(
                                    height=160,
                                    border_radius=12,
                                    content=ft.Image(
                                        src=movie["poster"],
                                        fit=ft.ImageFit.COVER,
                                        border_radius=12,
                                    ),
                                ),
                                ft.Text(movie["title"], size=12, weight=ft.FontWeight.BOLD),
                                ft.Text(movie["genre"], size=11, color=ft.colors.WHITE70),
                            ],
                            spacing=4,
                        ),
                    )
                )

        page.update()

    # -------------------------
    #   CAMPO DE BÚSQUEDA
    # -------------------------
    search = ft.TextField(
        hint_text="Search movies, shows...",
        prefix_icon=ft.Icons.SEARCH,
        on_submit=on_search,
        filled=True,
        border_radius=12,
    )

    # -------------------------
    #   GRID DE RESULTADOS
    # -------------------------
    results = ft.GridView(
        max_extent=180,
        child_aspect_ratio=0.65,
        spacing=12,
        run_spacing=12,
        expand=True,     # importante
    )

    # 1. Creamos la barra y la guardamos en una variable
    my_bar = app_bar(page, "Search", back=True)

    # 2. Sobrescribimos la acción del botón de atrás para ir a /home
    if my_bar.leading:
        my_bar.leading.on_click = lambda _: page.go("/home")

    # -------------------------
    #   VIEW COMPLETA
    # -------------------------
    return ft.View(
        route="/search",
        controls=[
            my_bar,

            ft.Column(
                [
                    search,

                    # El contenedor expandible es lo que habilita el scroll interno
                    ft.Container(
                        expand=True,
                        content=results
                    ),
                ],
                expand=True,
            ),
        ],
        padding=0,
        bgcolor=ft.colors.BACKGROUND,
        scroll=None,   # evita que el View bloquee el scroll interno
    )
