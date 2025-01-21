'''

Adapted excerpt from Getting Started with Raspberry Pi by Matt Richardson

Modified by Rui Santos
Complete project details: http://randomnerdtutorials.com

'''

from flask import Flask, render_template, request
from servergpio_lib import GPIO

app = Flask(__name__)

# Create a dictionary called pins to store the pin number, GPIO instance, and pin state:
pins = {
   23: {'gpio': GPIO(23), 'name': 'GPIO 23'},
   24: {'gpio': GPIO(24), 'name': 'GPIO 24'}
}

# Set each pin as an output and initialize it to a low state:
for pin in pins:
    pins[pin]['gpio'].setmode("output")
    pins[pin]['gpio'].write(0)

@app.route("/")
def main():
    # For each pin, read the pin state and store it in the pins dictionary:
    for pin in pins:
        pin_obj = pins[pin]['gpio']
        pins[pin]['state'] = pin_obj.read() if pin_obj.getmode() == "input" else pin_obj.value

    # Put the pin dictionary into the template data dictionary:
    templateData = {
        'pins': pins
    }
    # Pass the template data into the template main.html and return it to the user
    return render_template('html.html', **templateData)

@app.route("/<changePin>/<action>")
def action(changePin, action):
    try:
        # Convert the pin from the URL into an integer:
        changePin = int(changePin)
        pin_obj = pins[changePin]['gpio']
        deviceName = pins[changePin]['name']

        # Perform the requested action:
        if action == "on":
            pin_obj.write(1)
            message = f"Turned {deviceName} on."
        elif action == "off":
            pin_obj.write(0)
            message = f"Turned {deviceName} off."
        else:
            raise ValueError("Invalid action")

        # Update the pin state:
        pins[changePin]['state'] = pin_obj.value

    except KeyError:
        message = "Invalid pin number."
    except ValueError as e:
        message = str(e)

    # Prepare the template data:
    templateData = {
        'pins': pins,
        'message': message
    }

    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
