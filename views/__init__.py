import flet as ft

from .details import details_view
from .home import home_view
from .profile import profile_view
from .search import search_view
from .buy_subscription import buy_subscription_view
from .register import register_view
from .payment import payment_view
from .payment_success import payment_success_view
from .login import login_view

def init_view(page: ft.Page) -> ft.View:
    page.title = "Muvix - All your entertainment in one place"
    page.padding = 0

    # Background image
    background = ft.Container(
        expand=True,  # Forces the container to fill the available space
        image=ft.DecorationImage(
            src="fondo_home.png",
            fit=ft.ImageFit.COVER,
            opacity=0.35  # The opacity is applied to the image here
        )
    )

    # Titles
    title = ft.Text(
        "All your entertainment in one place",
        size=36,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER,
    )

    subtitle = ft.Text(
        "Enjoy unlimited streaming from €5.99/month",
        size=18,
        color=ft.colors.WHITE70,
        text_align=ft.TextAlign.CENTER,
    )

    def make_hover_button(label: str, route: str):
        normal_bg = "#C6FF00"
        hover_bg = "#00C853"
        text_color = ft.colors.BLACK

        def on_hover(e):
            is_hovering = e.data == "true"
            e.control.bgcolor = hover_bg if is_hovering else normal_bg
            e.control.scale = 1.1 if is_hovering else 1.0
            e.control.shadow = ft.BoxShadow(blur_radius=15, color=hover_bg) if is_hovering else None
            e.control.update()

        def on_click(e):
            page.go(route)

        # We use ONLY Container, without external wrappers
        return ft.Container(
            content=ft.Text(
                label, 
                color=text_color, 
                weight=ft.FontWeight.BOLD,
                size=16
            ),
            width=170,
            height=54,
            bgcolor=normal_bg,
            border_radius=10,
            alignment=ft.alignment.center,
            
            # Animations
            animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
            animate_scale=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
            
            # Events
            on_click=on_click,
            on_hover=on_hover,
            
        
            ink=True  # This activates the hand cursor and click effect automatically
        )
    # Create the buttons
    signup_btn = make_hover_button("Sign up", "/signup")
    login_btn = make_hover_button("Log in", "/login")

    # Page structure
    centered_content = ft.Column(
        [
            title,
            subtitle,
            ft.Row(
                [signup_btn, ft.Container(width=50), login_btn], # Space of 50 between buttons
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=24,
        expand=True,
    )

    overlay = ft.Container(
        content=centered_content,
        alignment=ft.alignment.center,
        expand=True,
        padding=20,
    )

    layout = ft.Stack(
        [
            background,
            overlay,
        ],
        expand=True,
    )

    return ft.View(
        route="/",
        controls=[layout],
        padding=0,
        bgcolor=ft.colors.BLACK,
    )