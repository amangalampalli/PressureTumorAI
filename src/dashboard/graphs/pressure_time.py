import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import random
from src.ipc_broker.socket_init import create_subscriber
from src.ipc_broker.socket_comms import recv_array

# socket = create_subscriber(8001)

# Create figure for plotting
def graphPressure():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = []
    ys = []

    # This function is called periodically from FuncAnimation
    def animate(i, xs, ys):

        # Read temperature (Celsius) from TMP102
        temp_c = round(random.random(), 2)

        # Add x and y to lists
        xs.append(dt.datetime.now().strftime("%H:%M:%S.%f"))
        ys.append(temp_c)

        # Limit x and y lists to 20 items
        xs = xs[-20:]
        ys = ys[-20:]

        # Draw x and y lists
        ax.clear()
        ax.plot(xs, ys)

        # Format plot
        plt.xticks(rotation=45, ha="right")
        plt.subplots_adjust(bottom=0.30)
        plt.title("TMP102 Temperature over Time")
        plt.ylabel("Temperature (deg C)")

    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
    plt.show()
