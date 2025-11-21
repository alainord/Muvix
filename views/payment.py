import flet as ft
from datetime import datetime
from utils.user_manager import UserManager

def payment_view(page: ft.Page) -> ft.View:
    NEON_GREEN = "#CCFF00"
    BLACK_BG = "#000000"
    
    db = UserManager()

    # References to inputs
    card_ref = ft.Ref[ft.TextField]()
    date_ref = ft.Ref[ft.TextField]()
    cvv_ref = ft.Ref[ft.TextField]()

    # References for TEXT and CONTAINER of error (to animate height) ---
    card_error_text_ref = ft.Ref[ft.Text]()
    card_error_container_ref = ft.Ref[ft.Container]()

    date_error_text_ref = ft.Ref[ft.Text]()
    date_error_container_ref = ft.Ref[ft.Container]()

    cvv_error_text_ref = ft.Ref[ft.Text]()
    cvv_error_container_ref = ft.Ref[ft.Container]()

    # --- LOGIC FOR AUTO SLASH (MM/YY) ---
    _last_date_len = [0] 

    def on_date_change(e):
        val = date_ref.current.value
        current_len = len(val)
        
        if current_len == 2 and _last_date_len[0] < 2:
            date_ref.current.value = val + "/"
            date_ref.current.update()
        
        if current_len > 5:
            date_ref.current.value = val[:5]
            date_ref.current.update()
            
        _last_date_len[0] = len(date_ref.current.value)
        
        # Clear error when typing date
        clear_field_error(date_error_container_ref)

    # Helper to clear errors (hide container)
    def clear_field_error(container_ref):
        if container_ref.current.height > 0:
            container_ref.current.height = 0
            container_ref.current.update()

    def create_input_field(label: str, ref: ft.Ref, width: int = None, expand: bool = False, on_change=None):
        def handle_change(e):
            if on_change:
                on_change(e)
            # Detect field to clear its specific error
            if ref == card_ref: clear_field_error(card_error_container_ref)
            elif ref == cvv_ref: clear_field_error(cvv_error_container_ref)

        return ft.Container(
            bgcolor=ft.colors.BLACK,
            border_radius=15,
            height=50,
            width=width,
            expand=expand,
            alignment=ft.alignment.center,
            padding=ft.padding.only(left=20, right=10),
            content=ft.TextField(
                ref=ref,
                hint_text=label,
                bgcolor=ft.colors.TRANSPARENT,
                border=ft.InputBorder.NONE,
                filled=False,
                hint_style=ft.TextStyle(color=ft.colors.GREY_400, size=14),
                text_style=ft.TextStyle(color=ft.colors.WHITE),
                cursor_color=ft.colors.WHITE,
                height=50,
                content_padding=ft.padding.only(bottom=12),
                text_vertical_align=0,
                keyboard_type=ft.KeyboardType.NUMBER,
                on_change=handle_change 
            )
        )

    def validate_date(date_str):
        try:
            if "/" not in date_str: return False
            parts = date_str.split("/")
            if len(parts) != 2: return False
            
            month = int(parts[0])
            year = int(parts[1]) + 2000 

            if month < 1 or month > 12: return False
            
            now = datetime.now()
            if year < now.year: return False
            elif year == now.year and month < now.month: return False
            return True
        except ValueError:
            return False

    def show_error(text_ref, container_ref, msg):
        text_ref.current.value = msg
        text_ref.current.update()
        container_ref.current.height = 20 # Show space
        container_ref.current.update()

    def on_pay_click(e):
        # 1. Clear previous errors (visual)
        clear_field_error(card_error_container_ref)
        clear_field_error(date_error_container_ref)
        clear_field_error(cvv_error_container_ref)
        
        card = card_ref.current.value.strip()
        date = date_ref.current.value.strip()
        cvv = cvv_ref.current.value.strip()
        
        has_error = False

        # 2. Validations
        if not card.isdigit() or len(card) != 16:
            show_error(card_error_text_ref, card_error_container_ref, "Invalid Card: Must be 16 digits")
            has_error = True

        if not validate_date(date):
            show_error(date_error_text_ref, date_error_container_ref, "Invalid Date (MM/YY)")
            has_error = True

        if not cvv.isdigit() or len(cvv) != 3:
            show_error(cvv_error_text_ref, cvv_error_container_ref, "Invalid CVV (3 digits)")
            has_error = True
            
        if has_error:
            return

        # 3. Payment process
        user_data = page.session.get("temp_user_data")
        if not user_data:
            page.snack_bar = ft.SnackBar(ft.Text("Session Error: Please register again"), bgcolor=ft.colors.RED)
            page.go("/register")
            return

        success, msg = db.register_user(
            user_data["full_name"], 
            user_data["username"], 
            user_data["password"]
        )

        if success:
            page.session.remove("temp_user_data")
            page.go("/payment_success")
        else:
             page.snack_bar = ft.SnackBar(ft.Text(f"Error: {msg}"), bgcolor=ft.colors.RED)
             page.snack_bar.open = True
             page.update()

    def button_hover(e):
        # Change to Dark Gray (#333333) on mouse over, and back to Black on mouse out
        e.control.bgcolor = "#333333" if e.data == "true" else ft.colors.BLACK
        e.control.scale = 1.05 if e.data == "true" else 1.0
        e.control.update()
        
    def create_pay_button():
        return ft.Container(
            content=ft.Text("Pay", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            width=140,
            height=45,
            bgcolor=ft.Colors.BLACK,
            border_radius=25,
            alignment=ft.alignment.center,
            ink=True,
            on_click=on_pay_click,
            on_hover=button_hover,
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT), # Color animation
            animate_scale=ft.Animation(200, ft.AnimationCurve.EASE_OUT) # Scale animation
        )
    
    # Helper to create the animated error container
    def create_error_container(text_ref, container_ref):
        return ft.Container(
            ref=container_ref,
            height=0, # Invisible by default
            animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
            content=ft.Text(
                ref=text_ref, 
                color="red", 
                size=12, 
                weight=ft.FontWeight.BOLD
            )
        )

    payment_card = ft.Container(
        width=350,
        bgcolor=NEON_GREEN,
        border_radius=30,
        padding=ft.padding.all(30),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0, # Manual spacing
            controls=[
                ft.Image(
                    src="images/Muvix_M.png", 
                    width=80, 
                    height=80, 
                    color=ft.colors.BLACK 
                ),
                ft.Container(height=10), 
                
                # --- CARD SECTION ---
                ft.Column(
                    spacing=0,
                    controls=[
                        create_input_field("Card number (16 digits)", ref=card_ref, width=290),
                        create_error_container(card_error_text_ref, card_error_container_ref),
                        ft.Container(height=10) # Fixed space
                    ]
                ),
                
                # --- DATE & CVV ROW ---
                ft.Row(
                    spacing=15,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        # Columna Fecha
                        ft.Column(
                            expand=True,
                            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                            spacing=0,
                            controls=[
                                create_input_field("MM/YY", ref=date_ref, expand=False, on_change=on_date_change),
                                create_error_container(date_error_text_ref, date_error_container_ref)
                            ]
                        ),
                        # Column CVV
                        ft.Column(
                            expand=True,
                            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                            spacing=0,
                            controls=[
                                create_input_field("CVV", ref=cvv_ref, expand=False),
                                create_error_container(cvv_error_text_ref, cvv_error_container_ref)
                            ]
                        ),
                    ]
                ),
                
                ft.Container(height=50), # Fixed space before the button
                create_pay_button()
            ],
            tight=True
        ),
        shadow=ft.BoxShadow(blur_radius=20, color=ft.colors.with_opacity(0.5, NEON_GREEN)),
    )

    return ft.View(
        route="/payment",
        controls=[
            ft.Container(
                expand=True,
                bgcolor=BLACK_BG,
                alignment=ft.alignment.center,
                content=payment_card,
                padding=20
            )
        ],
        padding=0,
        bgcolor=BLACK_BG
    )