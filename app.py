import flet as ft

# Flet compatibility shim (handles versions with ft.Colors/ft.Icons)
if not hasattr(ft, "colors") and hasattr(ft, "Colors"):
    ft.colors = ft.Colors  # type: ignore[attr-defined]
if not hasattr(ft, "icons") and hasattr(ft, "Icons"):
    ft.icons = ft.Icons  # type: ignore[attr-defined]

# Ensure common color attributes exist across different flet versions.
# Some flet releases expose colors differently; create a lightweight
# wrapper with sensible fallbacks so the app can reference constants like
# BACKGROUND, SURFACE, GREY_800, WHITE70, etc., without crashing.
try:
    from types import SimpleNamespace

    # collect existing uppercase attributes from ft.colors
    existing_colors = {}
    try:
        for name in dir(ft.colors):
            if name.isupper():
                existing_colors[name] = getattr(ft.colors, name)
    except Exception:
        # ft.colors might be a mapping-like or Enum; attempt getattr on common names later
        existing_colors = {}

    # sensible defaults (dark theme oriented)
    defaults = {
        "BACKGROUND": existing_colors.get("BACKGROUND") or existing_colors.get("SURFACE") or "#121212",
        "SURFACE": existing_colors.get("SURFACE") or "#1E1E1E",
        "SURFACE_VARIANT": existing_colors.get("SURFACE_VARIANT") or existing_colors.get("SURFACE") or "#232323",
        "GREY_800": existing_colors.get("GREY_800") or "#2E2E2E",
        "WHITE70": existing_colors.get("WHITE70") or "#B3B3B3",
        "WHITE": existing_colors.get("WHITE") or "#FFFFFF",
        "BLACK": existing_colors.get("BLACK") or "#000000",
        "DEEP_PURPLE_700": existing_colors.get("DEEP_PURPLE_700") or "#5E35B1",
        "INDIGO_700": existing_colors.get("INDIGO_700") or "#3949AB",
        "DEEP_PURPLE_200": existing_colors.get("DEEP_PURPLE_200") or "#B39DDB",
    }

    # If ft.colors supports attribute assignment, just set missing ones.
    can_set = True
    try:
        setattr(ft.colors, "__test_attr__", True)
        delattr(ft.colors, "__test_attr__")
    except Exception:
        can_set = False

    if can_set:
        for k, v in defaults.items():
            if not hasattr(ft.colors, k):
                setattr(ft.colors, k, v)
    else:
        # wrap into a SimpleNamespace so we can freely add attributes
        merged = {**existing_colors, **defaults}
        ft.colors = SimpleNamespace(**merged)
except Exception:
    # If anything unexpected happens, avoid crashing here; fall back to minimal defaults.
    try:
        ft.colors = ft.colors  # type: ignore
    except Exception:
        from types import SimpleNamespace

        ft.colors = SimpleNamespace(BACKGROUND="#121212", SURFACE="#1E1E1E")

from components import navigation_bar
from components.app_bar import app_bar
from views import details_view, home_view, init_view, profile_view, search_view, buy_subscription_view, register_view, payment_view, payment_success_view, login_view


def main(page: ft.Page) -> None:
    page.title = "Muvix"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.window_maximized = True
    page.prevent_scroll_bounce = True  # evita rebote vertical (complementario)

    # 🔥 Inyectar JS para desactivar navegación por gestos horizontales
    page.html = """
    <script>
    window.addEventListener("wheel", function(e) {
        if (Math.abs(e.deltaX) > Math.abs(e.deltaY)) {
            e.preventDefault();  // bloquea gesto horizontal
        }
    }, { passive: false });
    </script>
    """

    
    def route_change(e: ft.RouteChangeEvent) -> None:
        page.views.clear()
        template = ft.TemplateRoute(page.route)

        if template.match("/"):
            page.views.append(init_view(page))
        elif template.match("/home"):
            page.views.append(home_view(page))
        elif template.match("/signup"):
            page.views.append(buy_subscription_view(page))
        elif template.match("/register"):
             page.views.append(register_view(page))
        elif template.match("/payment"):
             page.views.append(payment_view(page))
        elif template.match("/payment_success"): 
             page.views.append(payment_success_view(page))
        elif template.match("/login"):
             page.views.append(login_view(page))
        elif template.match("/search"):
            page.views.append(search_view(page))
        elif template.match("/profile"):
            page.views.append(profile_view(page))
        elif template.match("/movie/:id"):
            page.views.append(details_view(page, template.id))
        else:
            page.views.append(
                ft.View(
                    route="/404",
                    controls=[
                        app_bar(page, "Not found", back=True),
                        ft.Container(padding=16, content=ft.Text("Page not found")),
                    ],
                    padding=0,
                    bgcolor=ft.colors.BACKGROUND,
                )
            )

        page.update()

    def view_pop(e: ft.ViewPopEvent) -> None:
        if len(page.views) > 1:
            page.views.pop()
            page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route or "/")


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
