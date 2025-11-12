import flet as ft

# Flet compatibility shim (handles versions with ft.Colors/ft.Icons)
if not hasattr(ft, "colors") and hasattr(ft, "Colors"):
    ft.colors = ft.Colors  # type: ignore[attr-defined]
if not hasattr(ft, "icons") and hasattr(ft, "Icons"):
    ft.icons = ft.Icons  # type: ignore[attr-defined]


def navigation_bar(page: ft.Page) -> ft.NavigationBar:
    # Newer flet versions expose NavigationDestination; older ones may not.
    # Provide a fallback: if NavigationDestination is available, use it;
    # otherwise return a simple row of IconButtons that replicates behavior.
    def on_change(e: ft.ControlEvent) -> None:
        idx = e.control.selected_index
        route = {0: "/", 1: "/search", 2: "/profile"}.get(idx, "/")
        page.go(route)

    current = {"/": 0, "/search": 1, "/profile": 2}.get(page.route, 0)

    if hasattr(ft, "NavigationDestination"):
        return ft.NavigationBar(
            selected_index=current,
            on_change=on_change,
            destinations=[
                ft.NavigationDestination(
                    icon=ft.Icons.HOME_OUTLINED,
                    selected_icon=ft.Icons.HOME,
                    label="Home",
                ),
                ft.NavigationDestination(icon=ft.Icons.SEARCH, label="Search"),
                ft.NavigationDestination(
                    icon=ft.Icons.PERSON_OUTLINE,
                    selected_icon=ft.Icons.PERSON,
                    label="Profile",
                ),
            ],
        )
    else:
        # Fallback UI: mimic a bottom navigation bar with IconButtons
        def make_button(icon, route, index, selected_index=current):
            return ft.IconButton(
                icon,
                tooltip=route,
                icon_color=ft.colors.WHITE if index == selected_index else ft.colors.WHITE70,
                on_click=lambda e, r=route: page.go(r),
            )

        return ft.Container(
            padding=8,
            bgcolor=getattr(ft.colors, "SURFACE", None) or "#1E1E1E",
            content=ft.Row(
                [
                    make_button(ft.Icons.HOME_OUTLINED, "/", 0),
                    make_button(ft.Icons.SEARCH, "/search", 1),
                    make_button(ft.Icons.PERSON_OUTLINE, "/profile", 2),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
        )
