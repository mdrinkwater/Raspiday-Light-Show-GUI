from Tkinter import *
from ttk import *
import ttk
import os

playlistname = "  "

# This sets up the root screen

root = Tk()
root.geometry('1000x600+0+0')
root.title('Raspiday Music & Lights')
content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth = 2, relief = 'sunken', width = 990, height = 590)

# This sets up the tabs

tab = ttk.Notebook(root, width=950, height=550)
music = ttk.Frame(tab);
playlist = ttk.Frame(tab);
shows = ttk.Frame(tab);
help = ttk.Frame(tab);
tab.add(music, text="Music")
tab.add(playlist, text="Playlist")
tab.add(shows, text="Shows")
tab.add(help, text="Help")
tab.grid(column=0, row=0)


# Music Tab Layout

path = "/home/mike/Raspi/home/pi/music/"
dirs = os.listdir(path)
x = 0
lbmusic = Listbox(music, height = 20, width = 60)
for file in dirs:
	if file.endswith('.mp3'):
        	lbmusic.insert(x, file)
        	lbmusic.grid(column=0, row=0)
        	x = x + 1
        	lbmusic.grid(column=0, row=0)
remove = ttk.Label(music, text = "Remove")
remove.grid(column=3, row=0, sticky = N)
ok = ttk.Button(music, text = "Continue")
ok.grid(column=3, row=0, sticky = W)
add = ttk.Label(music, text ="Add Song")
add.grid(column=0, row=1, sticky = SW)
bbutton = ttk.Button(music, text="Browse")
bbutton.grid(column=0, row=2, sticky = W)
cbutton = ttk.Button(music, text="Add")
cbutton.grid(column=0, row=2, sticky = E)


# Playlist Layout


path = "/home/mike/Raspi/etc/cron.d"
myfile = '/home/mike/Raspi/etc/cron.d/'
dirs = os.listdir(path)
avaplay = ttk.Label(playlist, text="Current Playlists")
avaplay.grid(column=0, row=1)
x = 0
#for file in dirs:
    #splylst = StringVar(value = file)  ****This section needs to be worked near the top, and the fuction def() created
    #print splylst
lbplaylist = Listbox(playlist, height = 10, width = 51)
for file in dirs:
    myf = myfile + file
    splylst = StringVar(value = file) # This is to move the selection to the remove box
    f = open(myf)
    data = f.readline()
    while data:
        lbplaylist.insert(x, file +"  "+data)
        data = f.readline()
        x = x + 1
        lbplaylist.grid(column=0, row=2)
remove = ttk.Label(playlist, text = "Playlists to remove")
remove.grid(column=3, row=1, sticky = N)
plbutton = ttk.Button(playlist, text=">>")
plbutton.grid(column=2, row=2)
lbplay = Listbox(playlist, height = 10, width = 51)
lbplay.grid(column=3, row=2) # This should work off the >> button
ok = ttk.Button(playlist, text = "Continue")
paths = "/home/mike/Raspi/home/pi/music/"
dirs2 = os.listdir(paths)
x = 0
lbmusic = Listbox(playlist, height = 10, width = 51)
for file in dirs2:
	if file.endswith('.mp3'):
        	lbmusic.insert(x, file)
        	lbmusic.grid(column=0, row=4)
        	x = x + 1
        	lbmusic.grid(column=0, row=4)
ok.grid(column=2, row=7, sticky = S)
add = ttk.Label(playlist, text ="Create/Edit Playlist")
add.grid(column=2, row=0, sticky = NW)
cbutton = ttk.Button(playlist, text=">>")
cbutton.grid(column=2, row=4)
songlabel = ttk.Label(playlist, text="Songs adding to Playlist")
songlabel.grid(column=3, row=3, sticky = S)
lbsongs = Listbox(playlist, height = 10, width = 51)
lbsongs.grid(column=3, row=4)
avasong = ttk.Label(playlist, text="Available Songs")
avasong.grid(column=0, row=3, sticky = S)
plnlab = ttk.Label(playlist, text="Playlist name:")
plname = ttk.Entry(playlist, textvariable=playlistname)
plnlab.grid(column=0, row=6, sticky = E)
plname.grid(column=1, row=6, columnspan= 3, sticky = W)
tipbox = ttk.Labelframe(playlist, text="Tab Tip")
tip1 = ttk.Label(tipbox, text="1. Removing a Playlist does not remove songs from the /Music Directory")
tip2 = ttk.Label(tipbox, text="2. Creating a playlist also requires adding it in the Show tab for it to play")
tip3 = ttk.Label(tipbox, text="3. You can add the same song multiple times to a playlist")
tip4 = ttk.Label(tipbox, text="4. Songs removed under the Songs tab, will no longer play in the configured playlists")
tipbox.grid(column=0, row=8, columnspan=4, rowspan=2)
tip1.grid(column=0, row=1, columnspan=4)
tip2.grid(column=0, row=2, columnspan=4)
tip3.grid(column=0, row=3, columnspan=4)
tip4.grid(column=0, row=4, columnspan=4)



# Shows Layout

label3 = ttk.Label(shows, text="Shows")
label3.grid(column=0, row=0)


# Help Tab Layout

box = ttk.Labelframe(help, text = "Music Tab")
labelh1 = ttk.Label(box, text="Under the Music tab, you can:")
labelh2 = ttk.Label(box, text="View the current songs in the /Music directory available to add to a playlist")
labelh3 = ttk.Label(box, text="Add new songs to the /Music directory")
labelh4 = ttk.Label(box, text="Remove existing songs from the /Music directory")
pbox = ttk.Labelframe(help, text = "Playlist Tab")
labelh5 = ttk.Label(pbox, text="Under the Playlist tab, you can:")
labelh6 = ttk.Label(pbox, text="View current Playlists")
labelh7 = ttk.Label(pbox, text="Create new Playlists")
labelh8 = ttk.Label(pbox, text="Edit or Delete current Playlists")
box.grid(column=0, row=0)
labelh1.grid(column=0, row=0)
labelh2.grid(column=0, row=2)
labelh3.grid(column=0, row=3)
labelh4.grid(column=0, row=4)
pbox.grid(column=0, row=1)
labelh5.grid(column=0, row=6)
labelh6.grid(column=0, row=8)
labelh7.grid(column=0, row=9)
labelh8.grid(column=0, row=10)



# This runs the GUI loop

root.mainloop()
