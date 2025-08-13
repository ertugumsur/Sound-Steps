# importing required module
import pyaudio
import wave
import time
from pynput import keyboard
import tkinter as tk
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math

root = tk.Tk() 
root.title('Sound Steps Sound Player')  #giving the title for our window
root.geometry("1920x1080")
 
# making function 
def play_front():
    paused = False    # global to track if the audio is paused
    def on_press(key):
        global paused
        print (key)
        if key == keyboard.Key.space:
            if stream.is_stopped():     # time to play audio
                print ('play pressed')
                stream.start_stream()
                paused = False
                return False
            elif stream.is_active():   # time to pause audio
                print ('pause pressed')
                stream.stop_stream()
                paused = True
                return False
        return False


    # you audio here
    wf = wave.open('front.wav', 'rb')

    # instantiate PyAudio
    p = pyaudio.PyAudio()

    # define callback
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    # open stream using callback
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream
    stream.start_stream()

    while stream.is_active() or paused==True:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        time.sleep(0.1)

    # stop stream
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio
    p.terminate()
 
def play_behind():
    paused = False    # global to track if the audio is paused
    def on_press(key):
        global paused
        print (key)
        if key == keyboard.Key.space:
            if stream.is_stopped():     # time to play audio
                print ('play pressed')
                stream.start_stream()
                paused = False
                return False
            elif stream.is_active():   # time to pause audio
                print ('pause pressed')
                stream.stop_stream()
                paused = True
                return False
        return False


    # you audio here
    wf = wave.open('behind.wav', 'rb')

    # instantiate PyAudio
    p = pyaudio.PyAudio()

    # define callback
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    # open stream using callback
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream
    stream.start_stream()

    while stream.is_active() or paused==True:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        time.sleep(0.1)

    # stop stream
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio
    p.terminate()

def play_right():
    paused = False    # global to track if the audio is paused
    def on_press(key):
        global paused
        print (key)
        if key == keyboard.Key.space:
            if stream.is_stopped():     # time to play audio
                print ('play pressed')
                stream.start_stream()
                paused = False
                return False
            elif stream.is_active():   # time to pause audio
                print ('pause pressed')
                stream.stop_stream()
                paused = True
                return False
        return False


    # you audio here
    wf = wave.open('right.wav', 'rb')

    # instantiate PyAudio
    p = pyaudio.PyAudio()

    # define callback
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    # open stream using callback
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream
    stream.start_stream()

    while stream.is_active() or paused==True:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        time.sleep(0.1)

    # stop stream
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio
    p.terminate()

def play_left():
    paused = False    # global to track if the audio is paused
    def on_press(key):
        global paused
        print (key)
        if key == keyboard.Key.space:
            if stream.is_stopped():     # time to play audio
                print ('play pressed')
                stream.start_stream()
                paused = False
                return False
            elif stream.is_active():   # time to pause audio
                print ('pause pressed')
                stream.stop_stream()
                paused = True
                return False
        return False


    # you audio here
    wf = wave.open('left.wav', 'rb')

    # instantiate PyAudio
    p = pyaudio.PyAudio()

    # define callback
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    # open stream using callback
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream
    stream.start_stream()

    while stream.is_active() or paused==True:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        time.sleep(0.1)

    # stop stream
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio
    p.terminate()

def play_f_right():
    paused = False    # global to track if the audio is paused
    def on_press(key):
        global paused
        print (key)
        if key == keyboard.Key.space:
            if stream.is_stopped():     # time to play audio
                print ('play pressed')
                stream.start_stream()
                paused = False
                return False
            elif stream.is_active():   # time to pause audio
                print ('pause pressed')
                stream.stop_stream()
                paused = True
                return False
        return False


    # you audio here
    wf = wave.open('front_right.wav', 'rb')

    # instantiate PyAudio
    p = pyaudio.PyAudio()

    # define callback
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    # open stream using callback
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream
    stream.start_stream()

    while stream.is_active() or paused==True:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        time.sleep(0.1)

    # stop stream
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio
    p.terminate()

def play_f_left():
    paused = False    # global to track if the audio is paused
    def on_press(key):
        global paused
        print (key)
        if key == keyboard.Key.space:
            if stream.is_stopped():     # time to play audio
                print ('play pressed')
                stream.start_stream()
                paused = False
                return False
            elif stream.is_active():   # time to pause audio
                print ('pause pressed')
                stream.stop_stream()
                paused = True
                return False
        return False


    # you audio here
    wf = wave.open('front_left.wav', 'rb')

    # instantiate PyAudio
    p = pyaudio.PyAudio()

    # define callback
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    # open stream using callback
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream
    stream.start_stream()

    while stream.is_active() or paused==True:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        time.sleep(0.1)

    # stop stream
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio
    p.terminate()

def play_b_right():
    paused = False    # global to track if the audio is paused
    def on_press(key):
        global paused
        print (key)
        if key == keyboard.Key.space:
            if stream.is_stopped():     # time to play audio
                print ('play pressed')
                stream.start_stream()
                paused = False
                return False
            elif stream.is_active():   # time to pause audio
                print ('pause pressed')
                stream.stop_stream()
                paused = True
                return False
        return False


    # you audio here
    wf = wave.open('behind_right.wav', 'rb')

    # instantiate PyAudio
    p = pyaudio.PyAudio()

    # define callback
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    # open stream using callback
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream
    stream.start_stream()

    while stream.is_active() or paused==True:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        time.sleep(0.1)

    # stop stream
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio
    p.terminate()

def play_b_left():
    paused = False    # global to track if the audio is paused
    def on_press(key):
        global paused
        print (key)
        if key == keyboard.Key.space:
            if stream.is_stopped():     # time to play audio
                print ('play pressed')
                stream.start_stream()
                paused = False
                return False
            elif stream.is_active():   # time to pause audio
                print ('pause pressed')
                stream.stop_stream()
                paused = True
                return False
        return False


    # you audio here
    wf = wave.open('behind_left.wav', 'rb')

    # instantiate PyAudio
    p = pyaudio.PyAudio()

    # define callback
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    # open stream using callback
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream
    stream.start_stream()

    while stream.is_active() or paused==True:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        time.sleep(0.1)

    # stop stream
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio
    p.terminate()


# title on the screen you can modify it    
title=tk.Label(root,text="Sound Steps",bd=9,relief=tk.GROOVE,
            font=("times new roman",50,"bold"),bg="white",fg="blue") 
title.pack(side=tk.TOP,fill=tk.X) 
 
# making a button which trigger the function so sound can be playeed
play_button = tk.Button(root, text="Front", font=("Helvetica", 16),
                     relief=tk.GROOVE, command=play_front)
play_button.place(x = 450, y = 150, height = 100, width = 100)

play_button2 = tk.Button(root, text="Behind", font=("Helvetica", 16),
                     relief=tk.GROOVE, command=play_behind)
play_button2.place(x = 450, y = 650, height = 100, width = 100)

play_button3 = tk.Button(root, text="Right", font=("Helvetica", 16),
                     relief=tk.GROOVE, command=play_right)
play_button3.place(x = 700, y = 400, height = 100, width = 100) 

play_button4 = tk.Button(root, text="B_Right", font=("Helvetica", 16),
                     relief=tk.GROOVE, command=play_b_right)
play_button4.place(x = 625, y = 575, height = 100, width = 100)

play_button5 = tk.Button(root, text="B_Left", font=("Helvetica", 16),
                     relief=tk.GROOVE, command=play_b_left)
play_button5.place(x = 275, y = 575, height = 100, width = 100) 

play_button6 = tk.Button(root, text="F_Left", font=("Helvetica", 16),
                     relief=tk.GROOVE, command=play_f_left)
play_button6.place(x = 275, y = 225, height = 100, width = 100) 

play_button7 = tk.Button(root, text="F_Right", font=("Helvetica", 16),
                     relief=tk.GROOVE, command=play_f_right)
play_button7.place(x = 625, y = 225, height = 100, width = 100) 

play_button8 = tk.Button(root, text="Left", font=("Helvetica", 16),
                     relief=tk.GROOVE, command=play_left)
play_button8.place(x = 200, y = 400, height = 100, width = 100) 

v2 = tk.DoubleVar() 

def update(): 
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume_percentage = v2.get()
    volume.SetMasterVolumeLevel(34 * math.log(volume_percentage / 100, 10), None)
    
  
s2 = tk.Scale( root, variable = v2, 
           from_ = 100, to = 0, 
           orient = tk.VERTICAL)  
  
b2 = tk.Button(root, text ="Update Volume", 
            command = update, 
            bg = "purple",  
            fg = "white") 
  
s2.place(x = 80, y = 100, height = 600, width = 100)  
b2.place(x = 60, y = 720, height = 20, width = 100)

root.mainloop()