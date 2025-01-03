"""This script initializes and runs a Flask server.

Imports:
    from clear import clear: Clears the terminal screen.
    from dotenv import dotenv_values as values: Loads environment variables from a .env file.
    from eventlet import listen: Listens for incoming connections.
    from eventlet.wsgi import server: Runs the WSGI server.
    from app import create_app: Imports the Flask application factory.

Functions:
    create_app: Creates and configures the Flask application.

Main Execution:
    Clears the terminal screen.
    Retrieves the port number from environment variables or defaults to 5000.
    Prints server execution details.
    Starts the WSGI server on the specified port with the Flask application.

"""

# from os import getcwd, path

# from pathlib import Path

from clear import clear
from dotenv import dotenv_values as values
from eventlet import listen
from eventlet.wsgi import server

from app import create_app

app = create_app()

if __name__ == "__main__":

    clear()
    port = int(values().get("PORT", 5000))
    print(
        f"""
=======================================================

            Executando servidor Flask
            * Porta: {int(values().get("PORT", "8000"))}

=======================================================
              """
    )

    # version_Path = Path(path.join(getcwd(), ".version"))
    # if version_Path.exists() is False:
    #     from app.misc.checkout import checkout_release_tag

    #     with open(".version", "w") as f:
    #         f.write(checkout_release_tag())

    server(listen(("localhost", port)), app, log=app.logger)
