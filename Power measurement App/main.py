import tkinter as tk
from tkinter import messagebox
import subprocess
import re
import psutil
import platform
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time

OS_TYPE = platform.system()

# Data storage for graph
timestamps = []
power_values = []

def get_power_usage():
    """Return current power usage in Watts (Linux only)."""
    if OS_TYPE == "Linux":
        try:
            result = subprocess.run(
                ["upower", "-i", "/org/freedesktop/UPower/devices/battery_BAT0"],
                stdout=subprocess.PIPE, text=True
            )
            output = result.stdout
            match = re.search(r"energy-rate:\s+([\d.]+)\s+W", output)
            return float(match.group(1)) if match else None
        except Exception:
            return None
    else:
        return None  # Windows: No direct wattage info

def get_battery_info():
    """Battery percentage and status using psutil."""
    battery = psutil.sensors_battery()
    if battery:
        status = "Plugged In" if battery.power_plugged else "On Battery"
        return battery.percent, status
    return None, "Unknown"

def get_temperature():
    """Get temperature for Linux using psutil or Windows using WMI."""
    if platform.system() == "Linux":
        if hasattr(psutil, "sensors_temperatures"):
            temps = psutil.sensors_temperatures()
            if temps:
                for name, entries in temps.items():
                    if entries:
                        return entries[0].current
    elif platform.system() == "Windows":
        try:
            import wmi
            w = wmi.WMI(namespace="root\\wmi")
            temperature_info = w.MSAcpi_ThermalZoneTemperature()
            if temperature_info:
                # Convert from tenths of Kelvin to Celsius
                temp_c = (temperature_info[0].CurrentTemperature / 10.0) - 273.15
                return round(temp_c, 1)
        except:
            return None
    return None

def get_health_tip(percent, status, temp):
    """Generate battery health tips."""
    if temp and temp > 75:
        return "Warning: High temperature! Keep the laptop cool."
    if status == "Plugged In":
        if percent >= 95:
            return "Tip: Enable battery saver mode or unplug to prevent heat."
        else:
            return "Good: Charging normally. Avoid overheating."
    else:
        if percent < 20:
            return "Warning: Battery low. Plug in soon."
        else:
            return "Good: Keep charge between 40-80% for best health."

def update_info():
    # Collect data
    power = get_power_usage()  # Linux only
    percent, status = get_battery_info()
    temp = get_temperature()
    cpu_usage = psutil.cpu_percent(interval=None)  # Cross-platform CPU usage
    tip = get_health_tip(percent, status, temp)

    # Update labels
    power_text = f"{power:.2f} W" if power else "Not Available"
    label_power.config(text=f"Power Usage: {power_text}")
    label_battery.config(text=f"Battery: {percent}% ({status})")
    label_cpu.config(text=f"CPU Usage: {cpu_usage}%")
    label_temp.config(text=f"Temperature: {temp}°C" if temp else "Temperature: N/A")
    label_tip.config(text=f"Health Tip: {tip}")

    # Add CPU usage to graph
    timestamps.append(time.strftime("%H:%M:%S"))
    power_values.append(cpu_usage)
    if len(timestamps) > 20:
        timestamps.pop(0)
        power_values.pop(0)
    update_graph()

    # Alerts
    if temp and temp > 80:
        messagebox.showwarning("Overheat Alert", "Laptop temperature is too high!")

    root.after(5000, update_info)


def update_graph():
    ax.clear()
    ax.plot(timestamps, power_values, marker="o", color="green", linewidth=2)
    ax.set_title("CPU Usage Over Time", fontsize=12)
    ax.set_ylabel("CPU %", fontsize=10)
    ax.set_xlabel("Time", fontsize=10)
    ax.set_ylim(0, 100)  # CPU % range
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.tick_params(axis="x", rotation=45)
    canvas.draw()



# Tkinter GUI
root = tk.Tk()
root.title("Cross-Platform Laptop Power Monitor")
root.geometry("600x500")

label_power = tk.Label(root, text="Power Usage: --", font=("Helvetica", 14))
label_power.pack(pady=5)

label_battery = tk.Label(root, text="Battery: --", font=("Helvetica", 14))
label_battery.pack(pady=5)

label_temp = tk.Label(root, text="Temperature: --", font=("Helvetica", 14))
label_temp.pack(pady=5)

label_tip = tk.Label(root, text="Health Tip: --", font=("Helvetica", 12), wraplength=550, justify="center")
label_tip.pack(pady=10)

label_cpu = tk.Label(root, text="CPU Usage: --", font=("Helvetica", 14))
label_cpu.pack(pady=5)


# Matplotlib figure with padding
fig = Figure(figsize=(5, 2.5), dpi=100)
fig.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.25)  # Add padding
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=20, padx=20)  # Add padding in Tkinter layout


update_info()
root.mainloop()
