'''

Adapted excerpt from Getting Started with Raspberry Pi by Matt Richardson

Modified by Rui Santos
Complete project details: http://randomnerdtutorials.com

'''

from flask import Flask, render_template, request
from servergpio_lib import GPIO

app = Flask(__name__)

# Initialize GPIO pins (0 to 27)
pins = {i: {'name': f'GPIO {i}', 'gpio': GPIO(i)} for i in range(28)}

# Configure all pins as output and set initial value to 0
for pin in pins.values():
    pin['gpio'].setmode("output")
    pin['gpio'].write(0)

@app.route("/")
def main():
    # Update pin states
    for pin in pins.values():
        pin['state'] = pin['gpio'].read() if pin['gpio'].getmode() == "input" else None

    # Pass the pin dictionary into the template
    templateData = {'pins': pins}
    return render_template('html.html', **templateData)

@app.route("/<int:changePin>/<action>")
def action(changePin, action):
    try:
        pin = pins[changePin]['gpio']
        deviceName = pins[changePin]['name']

        if action == "on":
            pin.write(1)
            message = f"Turned {deviceName} on."
        elif action == "off":
            pin.write(0)
            message = f"Turned {deviceName} off."
        else:
            message = "Invalid action."

    except KeyError:
        message = "Invalid pin number."
    except ValueError as e:
        message = str(e)

    # Update pin states
    for pin in pins.values():
        pin['state'] = pin['gpio'].read() if pin['gpio'].getmode() == "input" else None

    # Pass the pin dictionary into the template
    templateData = {
        'pins': pins,
        'message': message
    }

    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
