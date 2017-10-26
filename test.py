from appjar import gui
app = gui()
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)
app.addButtons(["Submit", "Cancel"], press)
app.go()
