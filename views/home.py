from data.movies_mock import movies_mock
import random
import flet as ft

def get_movies_by_genre(genre: str):
    return [m for m in movies_mock if m["genre"].lower() == genre.lower()]

def random_movies(n=5):
    import random
    return random.sample(movies_mock, min(n, len(movies_mock)))

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

    # ✅ Scroll horizontal visible y funcional
    scroll_row = ft.Container(
        content=ft.Row(
            chips,
            scroll=ft.ScrollMode.HIDDEN, 
            spacing=12,
        ),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,  # aísla el scroll del navegador
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
            scroll_row,
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
    
def movie_card(movie, page: ft.Page) -> ft.Container:
    return ft.Container(
        width=140,
        bgcolor=ft.colors.SURFACE,
        border_radius=12,
        padding=4,
        on_click=lambda e, movie_id=movie["id"]: page.go(f"/movie/{movie_id}"),
        content=ft.Column(
            [
                ft.Image(
                    src=movie["poster"],
                    width=140,
                    height=200,
                    border_radius=12,
                    fit=ft.ImageFit.COVER,
                ),
                ft.Text(movie["title"], size=11, weight=ft.FontWeight.W_600, max_lines=1),
                ft.Text(movie["genre"], size=10, color=ft.colors.WHITE70),
            ],
            spacing=3,
        ),
    )


def trending_card(movie, page: ft.Page) -> ft.Container:
    return ft.Container(
        width=350,
        height=300,
        border_radius=16,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,  # fuerza el recorte
        bgcolor=None,  # asegura fondo transparente
        on_click=lambda e, movie_id=movie["id"]: page.go(f"/movie/{movie_id}"),
        content=ft.Stack(
            [
                # Imagen principal
                ft.Image(
                    src=movie["poster"],
                    width=350,
                    height=300,
                    fit=ft.ImageFit.FIT_WIDTH,
                ),

                # Capa de degradado y texto
                ft.Container(
                    bgcolor="transparent",
                    gradient=None,
                    alignment=ft.alignment.bottom_center,
                    content=ft.Container(
                        width=220,
                        height=120,
                            content=ft.Container(
                            alignment=ft.alignment.bottom_left,
                            padding=ft.padding.only(left=1, bottom=8),  
                            content=ft.Text(
                                movie["title"],
                                color=ft.colors.WHITE,
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                max_lines=2,
                                text_align=ft.TextAlign.LEFT,  
                            ),
                        ),
                    ),
                ),
            ]
        ),
    )
    
def movie_section(title: str, movies: list[dict[str, str]], page: ft.Page) -> ft.Column:
    # Si la sección es Trending, usa tarjetas grandes
    if "trending" in title.lower():
        cards = [trending_card(m, page) for m in movies]
    else:
        cards = [movie_card(m, page) for m in movies]

    return ft.Column(
        [
            ft.Text(title, size=18, weight=ft.FontWeight.W_700),
            ft.Container(
                content=ft.Row(cards, scroll=ft.ScrollMode.AUTO, spacing=12),
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
            ),
        ],
        spacing=8,
    )


def home_view(page: ft.Page) -> ft.View:
    dummy_items = [{"title": f"Movie {i+1}", "subtitle": "Action"} for i in range(12)]
    trending = [{"title": f"Show {i+1}", "subtitle": "Drama"} for i in range(10)]
    recommended = [{"title": f"Pick {i+1}", "subtitle": "Sci-Fi"} for i in range(10)]
    
    body = ft.ListView(
        controls=[
            movie_section("Trending now", random_movies(5), page),
            movie_section("Because you watched Action", get_movies_by_genre("Action"), page),
            movie_section("Recommended for you", random_movies(5), page),
            movie_section("Horror picks", get_movies_by_genre("Horror"), page),
            movie_section("Animation highlights", get_movies_by_genre("Animation"), page),
        ],
        auto_scroll=False,
        spacing=16,
    )


    return ft.View(
        route="/",
        controls=[
            app_bar(page, ft.Image(src="./images/Logo.png", width=120, height=40, fit=ft.ImageFit.CONTAIN)),
            ft.Container(padding=12, content=body, expand=True),
        ],
        padding=0,
        bgcolor=ft.colors.BACKGROUND,
    )
