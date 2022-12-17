#from asclepius import dashboard, login_screen
import dashboard, home_screen

""" login_window = login_screen.Login(
    width=450, height=350, appearance_mode="light", color_theme="green"
 )

while True:
    login_window.show_login()
    if login_window.submit:
        password, enrollment_id = login_window.get_credentials()
        break """

home_screen_window = home_screen.HomeScreen(
    width=450, height=350, appearance_mode="light", color_theme="green"
 )

while True:
    home_screen_window.show_homescreen()

#dash_board = dashboard.Dashboard(
#    width=1280,
#    height=720,
#    appearance="dark",
#    theme_color="green",
#)

#dash_board.show_dashboard()


print("Program exited successfully.")
