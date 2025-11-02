from guizero import App, TextBox, PushButton, Box


app = App(title="Máy tính Casio", width=300, height=350)


input_box = TextBox(app, text="", width=24)
text_size = 16

def press(key):
    if key == "=":
        maytinh()
    elif key == "C":
        input_box.value = ""
    else:
        input_box.value += "/" if key == ":" else key

def maytinh():
    try:
        result = eval(input_box.value)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        input_box.value = str(result)
    except:
        input_box.value = "Error"



button_box = Box(app, layout="grid")
buttons =[
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", ".", "=", ":"],
    ["C"]]


for r, row in enumerate(buttons):
    for c, label in enumerate(row):
        PushButton(button_box, text=label, width=6, height=2, grid=[c, r], command=press, args=[label])

app.display()
