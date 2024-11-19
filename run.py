from app import create_app
import signal


def handle_shutdown(signal, frame):
    print("Shutting down server")
    exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_shutdown)
    app = create_app()
    app.run(debug=True)
