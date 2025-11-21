import flet as ft

def buy_subscription_view(page: ft.Page) -> ft.View:
    # --- CONSTANTS & COLORS ---
    NEON_GREEN = "#CCFF00"
    BLACK_BG = "#000000"
    
    # --- HELPER: FEATURE ROW ---
    def create_feature_row(icon_name: str, text: str):
        return ft.Row(
            controls=[
                ft.Icon(icon_name, color=ft.colors.BLACK, size=20),
                # WRAPPER: Ensures text wraps to new line instead of being cut off
                ft.Container(
                    content=ft.Text(
                        text, 
                        color=ft.colors.BLACK, 
                        size=14, 
                        weight=ft.FontWeight.W_500,
                    ),
                    expand=True # Takes all available space in the row
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START, 
            spacing=15,
        )

    def button_hover(e):
        # Change to Dark Gray (#333333) on mouse over, and back to Black on mouse out
        e.control.bgcolor = "#333333" if e.data == "true" else ft.colors.BLACK
        e.control.scale = 1.05 if e.data == "true" else 1.0
        e.control.update()
        
    # --- COMPONENT: BUY BUTTON ---
    def create_buy_button():
        return ft.Container(
            content=ft.Text("Buy now", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            width=180,
            height=50,
            bgcolor=ft.Colors.BLACK,
            border_radius=25,
            alignment=ft.alignment.center,
            ink=True,
            on_click=lambda _: page.go("/register"),
            on_hover=button_hover,
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT), # Color animation
            animate_scale=ft.Animation(200, ft.AnimationCurve.EASE_OUT) # Scale animation
        )

    def hover_anim(e):
        e.control.scale = 1.05 if e.data == "true" else 1.0
        e.control.update()

    # --- MAIN CARD CONTENT ---
    subscription_card = ft.Container(
        width=380,
        bgcolor=NEON_GREEN,
        border_radius=30,
        # COMPACT FIX 1: Reduced vertical padding (from 40 to 30)
        padding=ft.padding.symmetric(horizontal=30, vertical=30),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            # COMPACT FIX 2: Reduced spacing between main elements (from 25 to 20)
            spacing=20,
            controls=[
                # 1. Logo
                ft.Icon(name=ft.icons.MOVIE_CREATION_OUTLINED, size=80, color=ft.colors.BLACK),
                
                # 2. Features List
                ft.Column(
                    # COMPACT FIX 3: Reduced spacing between features (from 15 to 12)
                    spacing=12,
                    controls=[
                        create_feature_row(ft.icons.BLOCK, "Access to all the content without advertisements"),
                        create_feature_row(ft.icons.FOUR_K, "4k movies"),
                        create_feature_row(ft.icons.DOWNLOAD, "Download the content on your device"),
                    ]
                ),

                ft.Container(height=5), # Small Spacer

                # 3. Price Section
                # PRICE CUT-OFF FIX: We use CENTER alignment and padding top on the small text.
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER, 
                    controls=[
                        # Removed fixed height constraint so text isn't cut off
                        ft.Text("€ 5.99", size=40, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                        ft.Container(
                            content=ft.Text(
                                "/ Month", 
                                size=16, 
                                color=ft.colors.BLACK, 
                                weight=ft.FontWeight.W_500,
                            ),
                            # Push small text down to align visually with the big text baseline
                            padding=ft.padding.only(top=18) 
                        )
                    ]
                ),

                ft.Container(height=5), # Small Spacer

                # 4. Button
                create_buy_button()
            ],
            # This ensures the column occupies minimum required space vertically
            tight=True 
        ),
        shadow=ft.BoxShadow(blur_radius=20, color=ft.colors.with_opacity(0.5, NEON_GREEN)),
    )

    # --- VIEW LAYOUT ---
    return ft.View(
        route="/signup",
        controls=[
            ft.Container(
                expand=True,
                bgcolor=BLACK_BG,
                # Centers the card both horizontally and vertically in the page
                alignment=ft.alignment.center, 
                content=subscription_card,
                padding=20
            )
        ],
        padding=0,
        bgcolor=BLACK_BG
    )