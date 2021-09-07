import os

voltagePositionRaw = "/Users/aditya/Programming/PressureTumorAI/pressuretumorai/data/raw_data.txt"
voltagePositionFiltered = "/Users/aditya/Programming/PressureTumorAI/pressuretumorai/data/pressure_metrics.csv"

file = None

def writeFile(data):
    global voltagePosition, file
    file = open(voltagePositionRaw, "a")
    file.write("\n" + str(data) + "\n")

def closeFile():
    try:
        os.remove(voltagePositionFiltered)
    except:
        pass
    with open(voltagePositionRaw, "r") as f, open(voltagePositionFiltered, "w") as out:
        for line in f:
            if not line.isspace() and not line.startswith("None"):
                out.write(line)
        f.close()
        out.close()
    os.remove(voltagePositionRaw)