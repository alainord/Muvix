import flet as ft
from utils.user_manager import UserManager

def register_view(page: ft.Page) -> ft.View:
    NEON_GREEN = "#CCFF00"
    BLACK_BG = "#000000"
    
    db = UserManager()

    full_name_ref = ft.Ref[ft.TextField]()
    username_ref = ft.Ref[ft.TextField]()
    password_ref = ft.Ref[ft.TextField]()

    # We use a Container to control the visibility (height) of the error
    error_container_ref = ft.Ref[ft.Container]()
    error_text_ref = ft.Ref[ft.Text]()

    def create_input_field(label: str, ref: ft.Ref, is_password: bool = False):
        return ft.Container(
            bgcolor=ft.colors.BLACK,
            border_radius=15,
            height=50,
            alignment=ft.alignment.center, 
            padding=ft.padding.only(left=20, right=10),
            content=ft.TextField(
                ref=ref,
                hint_text=label,
                password=is_password,
                can_reveal_password=is_password,
                bgcolor=ft.colors.TRANSPARENT,
                border=ft.InputBorder.NONE,
                filled=False,
                hint_style=ft.TextStyle(color=ft.colors.GREY_400, size=14),
                text_style=ft.TextStyle(color=ft.colors.WHITE),
                cursor_color=ft.colors.WHITE,
                height=50,
                content_padding=ft.padding.only(bottom=12) if not is_password else ft.padding.only(bottom=6),
                text_vertical_align=0,
                on_change=lambda e: clear_error_for_field(ref)
            )
        )
    
    def clear_error_for_field(field_ref):
        # If the user types in the username field and the error is visible, hide it
        if field_ref == username_ref and error_container_ref.current.height > 0:
            error_container_ref.current.height = 0 
            error_container_ref.current.update()

    def on_next_click(e):
        full_name = full_name_ref.current.value
        user = username_ref.current.value
        pwd = password_ref.current.value

        # 1. Empty fields check
        if not full_name or not user or not pwd:
            # Show a red bar at the bottom (SnackBar)
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Please fill in all fields", color=ft.colors.WHITE),
                bgcolor=ft.colors.RED
            )
            page.snack_bar.open = True
            page.update()
            return

        # 2. Existing user validation
        if db.username_exists(user):
            # Update the text
            error_text_ref.current.value = "Username already exists!"
            error_text_ref.current.update()
            
            error_container_ref.current.height = 20 
            error_container_ref.current.update()
            return

        # 3. If everything is fine, save and proceed
        page.session.set("temp_user_data", {
            "full_name": full_name,
            "username": user,
            "password": pwd
        })

        page.go("/payment")

    def button_hover(e):
        # Change to Dark Gray (#333333) on mouse over, and back to Black on mouse out
        e.control.bgcolor = "#333333" if e.data == "true" else ft.colors.BLACK
        e.control.scale = 1.05 if e.data == "true" else 1.0
        e.control.update()

    def create_signup_button():
        return ft.Container(
            content=ft.Text("Next", color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
            width=140,
            height=45,
            bgcolor=ft.Colors.BLACK,
            border_radius=25,
            alignment=ft.alignment.center,
            ink=True,
            on_click=on_next_click,
            on_hover=button_hover,
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT), # Color animation
            animate_scale=ft.Animation(200, ft.AnimationCurve.EASE_OUT) # Scale animation
        )

    register_card = ft.Container(
        width=350,
        bgcolor=NEON_GREEN,
        border_radius=30,
        padding=ft.padding.all(30),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            controls=[
                ft.Image(
                    src="images/Muvix_M.png", 
                    width=80, 
                    height=80, 
                    color=ft.colors.BLACK 
                ),
                ft.Container(height=10),
                
                # --- FULL NAME ---
                ft.Column(
                    spacing=0,
                    controls=[
                        create_input_field("Full name", ref=full_name_ref),
                        ft.Container(height=10)
                    ]
                ),
                
                # --- USERNAME + ERROR ---
                ft.Column(
                    spacing=0,
                    controls=[
                        create_input_field("Username", ref=username_ref),
                        
                        ft.Container(
                            ref=error_container_ref,
                            height=0, # Invisible by default
                            animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
                            content=ft.Text(
                                ref=error_text_ref,
                                value="", 
                                color="red", 
                                size=12, 
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.LEFT,
                            )
                        ),
                        
                        ft.Container(height=10)
                    ]
                ),

                # --- PASSWORD ---
                ft.Column(
                    spacing=0,
                    controls=[
                        create_input_field("Password", ref=password_ref, is_password=True),
                        ft.Container(height=50)
                    ]
                ),
            
                create_signup_button()
            ],
            tight=True
        ),
        shadow=ft.BoxShadow(blur_radius=20, color=ft.colors.with_opacity(0.5, NEON_GREEN)),
    )

    return ft.View(
        route="/register",
        controls=[
            ft.Container(
                expand=True,
                bgcolor=BLACK_BG,
                alignment=ft.alignment.center,
                content=register_card,
                padding=20
            )
        ],
        padding=0,
        bgcolor=BLACK_BG
    )