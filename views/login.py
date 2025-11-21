import flet as ft
from utils.user_manager import UserManager

def login_view(page: ft.Page) -> ft.View:
    # --- CONSTANTS ---
    NEON_GREEN = "#CCFF00"
    BLACK_BG = "#000000"
    
    db = UserManager()

    # References to read inputs
    username_ref = ft.Ref[ft.TextField]()
    password_ref = ft.Ref[ft.TextField]()
    
    error_ref = ft.Ref[ft.Text]()

    # Helper to clear the error when typing
    def clear_error():
        if error_ref.current.value:
            error_ref.current.value = ""
            error_ref.current.update()

    # --- INPUT HELPER ---
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
                # Clear error automatically when typing
                on_change=lambda e: clear_error()
            )
        )

    # --- LOGIN LOGIC ---
    def on_login_click(e):
        user = username_ref.current.value
        pwd = password_ref.current.value

        # Clear previous messages
        error_ref.current.value = ""
        page.update()

        if not user or not pwd:
            error_ref.current.value = "Please enter username and password"
            error_ref.current.update()
            return

        # Call the database
        success, data = db.login_user(user, pwd)

        if success:
            # Save session
            page.session.set("user", data)
            
            page.snack_bar = ft.SnackBar(ft.Text(f"Welcome back, {data['full_name']}!"), bgcolor=ft.colors.GREEN)
            page.snack_bar.open = True
            page.update()
            
            page.go("/home")
        else:
            # Show error in red on the card
            error_ref.current.value = "Incorrect username or password"
            error_ref.current.update()

    # --- HOVER LOGIC FOR THE BUTTON ---
    def button_hover(e):
        # Change to Dark Gray (#333333) on mouse over, and back to Black on mouse out
        e.control.bgcolor = "#333333" if e.data == "true" else ft.Colors.BLACK
        e.control.scale = 1.05 if e.data == "true" else 1.0
        e.control.update()

    def create_login_button():
        return ft.Container(
            content=ft.Text("Login", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            width=140,
            height=45,
            bgcolor=ft.Colors.BLACK, # Base black color
            border_radius=25,
            alignment=ft.alignment.center,
            ink=True,
            on_click=on_login_click,
            on_hover=button_hover, # Connect the new hover
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT), # Color animation
            animate_scale=ft.Animation(200, ft.AnimationCurve.EASE_OUT) # Scale animation
        )

    # --- MAIN CARD ---
    login_card = ft.Container(
        width=350,
        bgcolor=NEON_GREEN,
        border_radius=30,
        padding=ft.padding.all(40),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15, # A little less space so the error fits
            controls=[
                ft.Icon(name=ft.icons.MOVIE_CREATION_OUTLINED, size=80, color=ft.colors.BLACK),
                ft.Container(height=5),
                
                create_input_field("Username", ref=username_ref),
                create_input_field("Password", ref=password_ref, is_password=True),
                
                # --- SPACE FOR ERROR ---
                ft.Container(
                    content=ft.Text(
                        ref=error_ref, 
                        value="", 
                        color="red", 
                        size=13, 
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),
                    alignment=ft.alignment.center,
                    height=20 
                ),
                
                create_login_button()
            ],
            tight=True
        ),
        shadow=ft.BoxShadow(blur_radius=20, color=ft.colors.with_opacity(0.5, NEON_GREEN)),
    )

    return ft.View(
        route="/login",
        controls=[
            ft.Container(
                expand=True,
                bgcolor=BLACK_BG,
                alignment=ft.alignment.center,
                content=login_card,
                padding=20
            )
        ],
        padding=0,
        bgcolor=BLACK_BG
    )