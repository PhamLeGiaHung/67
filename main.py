from guizero import App, TextBox, PushButton, Box

def press(key):
    if key == "=":
        calculate()
    elif key == "C":
        input_box.value = ""
    else:
        input_box.value += "/" if key == ":" else key

def calculate():
    try:
        result = eval(input_box.value)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        input_box.value = str(result)
    except:
        input_box.value = "Error"

app = App(title="Máy tính guizero", width=300, height=400)

input_box = TextBox(app, text="", width=24)
input_box.text_size = 16

button_box = Box(app, layout="grid")
buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", ".", ":", "="],
    ["C"]
]

for r, row in enumerate(buttons):
    for c, label in enumerate(row):
        PushButton(button_box, text=label, width=6, height=2, grid=[c, r], command=press, args=[label])

app.display()