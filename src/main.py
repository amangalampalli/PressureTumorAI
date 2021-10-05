from multiprocessing import Process

from src.dashboard.gui import dashboard

# from src.web_server.web_server import runServer
from src.localization.frame_streamer import stream_frames
import time

if __name__ == "__main__":
    # Start the frame streamer
    frame_streamer_process = Process(target=stream_frames)
    frame_streamer_process.start()

    # Delay the rendering of the GUI to allow the frame streamer to start
    time.sleep(0.1)

    # Start the GUI
    gui_process = Process(target=dashboard)
    gui_process.start()

    # Start the web server
    # web_server_process = Process(target=runServer)
    # web_server_process.start()

    # Wait for the processes to finish
    # gui_process.join()
    # web_server_process.join()
    frame_streamer_process.join()
