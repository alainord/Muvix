import flet as ft

def payment_success_view(page: ft.Page) -> ft.View:
    NEON_GREEN = "#CCFF00"
    BLACK_BG = "#000000"

    def go_to_login(e):
        page.go("/login")

    # --- HOVER LOGIC ---
    def button_hover(e):
        # Change to Dark Gray (#333333) on mouse over, and back to Black on mouse out
        e.control.bgcolor = "#333333" if e.data == "true" else ft.colors.BLACK
        e.control.scale = 1.05 if e.data == "true" else 1.0
        e.control.update()

    success_card = ft.Container(
        width=350,
        bgcolor=NEON_GREEN,
        border_radius=30,
        padding=ft.padding.all(40),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Icon(name=ft.icons.CHECK_CIRCLE_OUTLINE, size=100, color=ft.colors.BLACK),
                
                ft.Text(
                    "Payment Successful!", 
                    size=24, 
                    weight=ft.FontWeight.BOLD, 
                    color=ft.colors.BLACK,
                    text_align=ft.TextAlign.CENTER
                ),
                
                ft.Text(
                    "Your account has been created correctly.", 
                    size=16, 
                    color=ft.colors.BLACK,
                    text_align=ft.TextAlign.CENTER
                ),

                ft.Container(height=20),

                ft.Container(
                    content=ft.Text("Log In", color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                    width=160,
                    height=50,
                    bgcolor=ft.colors.BLACK,
                    border_radius=25,
                    alignment=ft.alignment.center,
                    ink=True,
                    on_click=go_to_login,
                    on_hover=button_hover,
                    animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),      # Color animation
                    animate_scale=ft.Animation(200, ft.AnimationCurve.EASE_OUT) # Scale animation
                )
            ],
            tight=True
        ),
        shadow=ft.BoxShadow(blur_radius=20, color=ft.colors.with_opacity(0.5, NEON_GREEN)),
    )

    return ft.View(
        route="/payment_success",
        controls=[
            ft.Container(
                expand=True,
                bgcolor=BLACK_BG,
                alignment=ft.alignment.center,
                content=success_card,
                padding=20
            )
        ],
        padding=0,
        bgcolor=BLACK_BG
    )