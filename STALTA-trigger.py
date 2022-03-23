from obspy.clients.seedlink.easyseedlink import create_client
from obspy.realtime import RtTrace
from collections import deque
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])

# derived from SC3's scautopick default config
sta_window = 2 # seconds
lta_window = 10 #80
ratio_window = 120
thres_on = 3
thres_off = 1.5

rt_trace = RtTrace(max_length=ratio_window)

#ratio = deque([0]*(ratio_window*100)) # assume 100Hz
ratio = np.zeros(ratio_window*100) # assume 100Hz

def append_trace_to_realtime(tr):
    global ratio

    print("Appending the following trace:")
    print(tr)
    rt_trace.append(tr)

    print("RtTrace:")
    print(rt_trace)

    print("Calculating STA/LTA")
    sta_lta = rt_trace.copy().trigger("recstalta", sta=sta_window, lta=lta_window)
    len_new_samples = len(tr.data)
    ratio = np.roll(ratio,-len_new_samples)
    ratio[-len_new_samples:] = sta_lta[-len_new_samples:]

    print()

    plt.plot(ratio)
    plt.draw()
    plt.pause(0.0001)
    plt.clf()

client = create_client("10.196.16.147", on_data=append_trace_to_realtime)
client.select_stream("AM", "RE722", "EHZ")
client.run()
