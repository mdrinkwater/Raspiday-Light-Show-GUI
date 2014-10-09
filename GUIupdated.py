#############################################################################################################################################
#############################################################################################################################################
###                 Raspiday Light Show GUI----------------------                                                                         ###
###                                                                                                                                       ###
###                                          Written by:                                                                                  ###
###                                                     Mike Drinkwater                                                                   ###
###---------------------------------------------------------------------------------------------------------------------------------------###
### Rev. 1                                                                                                                      Oct. 2014 ###
###                                                                                                                                       ###
#############################################################################################################################################
#############################################################################################################################################


# Import the modules and libraries we need
#--------------------------------------------------------------------------------------------------------------------------------------------#

from Tkinter import *
from ttk import *
import ttk
import shutil
import os

# Global Variables
#--------------------------------------------------------------------------------------------------------------------------------------------#
  
songspath = "/home/mike/Raspi/home/pi/music/"       #Path to the /Music directory
playlistpath = "/home/mike/Raspi/etc/cron.d/"       #Path to the Playlists
addsonglistbox1 = "Current Songs in Active Playlist"#Label variable depending on specific choices
addsonglistbox2 = "Add Songs"                       #Label for New playlist to add songs
playlistedit1 = "Active Playlist"                   #Label for existing playlist
playlistedit2 = "New Playlist"                      #Label for a new playlist
dir1 = os.listdir(songspath)                        #Set up to find the current songs in /Music
dir2 = os.listdir(playlistpath)                     #Set up to find the current playlists in /etc/cron.d
xd = 0


# We define functions here
#--------------------------------------------------------------------------------------------------------------------------------------------#

def playlistaction(*args):                        #This function gets the active member in the listbox of playlist
    lbeditplaylist.delete(0, END)                 #This clears the listbox when the playlist focus changes
    lbaddsongs.delete(0, END)                     #This clears the listbox when the playlist focus changes         
    name = lbplaylist.get(ACTIVE)                 #This gets the active selection in the playlist list box
    playlistsongs = playlistpath + name           #This sets up the path to the songs
    s = 0                                         #Just a counting variable
    songs = open(playlistsongs)                   #This opens the files
    data = songs.readline()                       #This reads the file
    while data:                                   #Sets up the loop
        data = songs.readline()                   #This continues the loop function
        s = s + 1                                 #Increments the counter
        
        
def editplaylistaction(*args):                    #This function gets the active member in the listbox of playlist         
    nameselect = lbeditplaylist.get(ACTIVE)       #This gets the active selection in the playlist list box
    print nameselect                              #For debugging

    
    
def populate(*args):
    name = lbplaylist.get(ACTIVE)                 #This gets the active selection in the playlist list box
    playlistsongs = playlistpath + name           #This sets up the path to the songs
    lbeditplaylist.insert(0 ,name)                #This puts the selected playlist in the edit box
    lbplaylist.delete(ACTIVE)
    s = 0                                         #Just a counting variable
    songs = open(playlistsongs)                   #This opens the files
    data = songs.readline()                       #This reads the file
    while data:                                   #Sets up the loop
        print data                                #For debugging(need to reduce to just .mp3)
        lbaddsongs.insert(s, data)                #This inserts the song data into the listbox
        data = songs.readline()                   #This continues the loop function
        s = s + 1                                 #Increments the counter
    addsonglabel1.grid(column = 3, row = 3)       #This adds the label to the listbox
    remplaylist1.grid(column = 3, row = 1)        #This adds the label to the listbox
    
    
    
def deleteplaylist(*args):                        #This defines the function for the delete button
    nameselect = lbeditplaylist.get(ACTIVE)       #This should get the Active playlist in the edit box
    path = playlistpath + nameselect              #This defines the path to the file we are deleting
    destination = '/home/mike/Raspi/home/pi/Trash'#This is the path to the Trash folder 
    shutil.move(path, destination)                #This should move the file
    lbeditplaylist.delete(0, END)                 #This should clear the Active playlist box
    lbplaylist.delete(0, END)                     #This should clear the playlist box for reload without deleted list
    lbaddsongs.delete(0, END)                     #This should remove the songs in the Active playlist song listbox
    xd = 0                                        #Reset Variable to 0
    for nplist in dir2:                           #This should query cron.d for the existing playlists
        selection = StringVar(value = nplist)     #This line should populate the listbox variable for later function calls
        lbplaylist.insert(xd, nplist)             #This inserts the playlists into the listbox for viewing
        print selection                           #For debugging
        print nplist                              #For debugging
        xd = xd + 1                               #This will count the files up
        lbplaylist.grid(column = 0, row = 2)      #This sets the listbox to view available playlists
    
    
        
    
    
# This sets up the root screen
#--------------------------------------------------------------------------------------------------------------------------------------------#

root = Tk()
root.geometry('1200x700+0+0')
root.title('Raspiday Music & Lights')
content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth = 5, relief = 'sunken', width = 1200, height = 700)

# This sets up the tabs
#--------------------------------------------------------------------------------------------------------------------------------------------#

tab = ttk.Notebook(root, width=1175, height=675)
music = ttk.Frame(tab);
playlist = ttk.Frame(tab);
shows = ttk.Frame(tab);
help = ttk.Frame(tab);
tab.add(music, text="Music")
tab.add(playlist, text="Playlist")
tab.add(shows, text="Shows")
tab.add(help, text="Help")
tab.grid(column=0, row=0)

# Set known variables for the Playlist Tab
#--------------------------------------------------------------------------------------------------------------------------------------------#

nameedit = StringVar()                                                #This is for the user input text box
tabtitle = ttk.Label(playlist, text ="Create/Edit Playlist")          #This is the main label for the tab
addsonglabel1 = ttk.Label(playlist, text=addsonglistbox1)             #This is the listbox label called CURRENT SONGS IN %playlist
addsonglabel2 = ttk.Label(playlist, text=addsonglistbox2)             #This is the listbox label called ADD SONGS
remplaylist1 = ttk.Label(playlist, text =playlistedit1)               #This is the listbox label called EDIT/REMOVE
remplaylist2 = ttk.Label(playlist, text=playlistedit2)                #This is the listbox label called NEW
curplaylist = ttk.Label(playlist, text="Current Playlists")           #This is the static label for the listbox that shows 
                                                                      #the current playlists
availsongs = ttk.Label(playlist, text ="Current songs available")     #Label for the available songs listbox
entername = ttk.Label(playlist, text = "Playlist Name:")              #This creates the label for the playlist text box
nametextbox = ttk.Entry(playlist, textvariable = nameedit)            #This is the textbox to enter new playlist names
x = 0                                                                 #Variable to count files when we populate playlists
sl = 0                                                                #Variable to count files when we populate current songs
selection = StringVar()                                               #We need to set the 'selection' variable so we can call it later




#These are TabTip entries
tipbox = ttk.Labelframe(playlist, text="Tab Tip")
tip = ttk.Label(tipbox, text="1. Removing a Playlist does not remove songs from the /Music Directory\n2. Creating a playlist also requires adding it in the Show tab for it to play\n3. You can add the same song multiple times to a playlist\n4. Music removed under the Songs tab, will no longer play in the configured playlists")


# Create the Buttons
#--------------------------------------------------------------------------------------------------------------------------------------------#

addplaylistbutton = ttk.Button(playlist, text = ">>")   #This button is to move selected playlist to the remove/edit listbox
ok = ttk.Button(playlist, text = "Commit")              #This is the 'Commit' button, it should write the files/ remove files, 
                                                        #etc..completes all screen selections
addsongbutton = ttk.Button(playlist, text = ">>")       #This is the button is used to add songs to a playlist from the songs listbox
delete = ttk.Button(playlist, text = "Delete")          #This is the Delete button
delete2 = ttk.Button(playlist, text = "Delete")         #This is the Delete button



# Creates the Listboxes we will need
#--------------------------------------------------------------------------------------------------------------------------------------------#

lbplaylist = Listbox(playlist, height = 10, width = 51)                              #This is the playlist list box
lbeditplaylist = Listbox(playlist, listvariable = selection, height = 10, width = 51)#This is the list box you add the playlist to, 
                                                                                     #and should then list the songs on that playlist 
                                                                                     #in the songs box
lbcurrentmusic = Listbox(playlist, height = 10, width = 51)                          #This listbox list currently available music in 
                                                                                     #the /Music directory
lbaddsongs = Listbox(playlist, height = 10, width = 51)                              #Listbox for the available songs


# Get the initial listbox populations for the listboxs
#--------------------------------------------------------------------------------------------------------------------------------------------#
for plist in dir2:                          #This should query cron.d for the existing playlists
    selection = StringVar(value = plist)    #This line should populate the listbox variable for later function calls
    lbplaylist.insert(x, plist)             #This inserts the playlists into the listbox for viewing
    x = x + 1                               #This will count the files up
    
    
for songlist in dir1:                             #This will query /Music for existing .mp3 files
    if songlist.endswith('.mp3'):                 #This verifies we are only pulling .mp3 files
        lbcurrentmusic.insert(END, songlist)      #This inserts the songs into the listbox
        sl = sl + 1                               #This counts the files
        

# This is where we look for interactions on the Tab
#--------------------------------------------------------------------------------------------------------------------------------------------#

lbplaylist.bind('<<ListboxSelect>>', playlistaction)                          #This checks for the currently selected item in the listbox
addplaylistbutton.bind('<Button-1>', populate)                                #This defines a click on the '>>' playlist button
lbeditplaylist.bind('<<ListboxSelect>>', editplaylistaction)                  #This checks for the currently selected item in the edit box
delete.bind('<Button-1>', deleteplaylist)                                     #This defines a click on the 'DELETE' playlist button


# Set up the screen layout here, and it looks good
#--------------------------------------------------------------------------------------------------------------------------------------------#

tabtitle.grid(column = 2, row = 0, sticky = NW)                                     #This sets the main title label for the tab
curplaylist.grid(column = 0, row = 1)                                               #This sets the lable for the playlist box title
availsongs.grid(column = 0, row = 3, sticky = S)                                    #This sets the title for the available songs box
lbplaylist.grid(column = 0, row = 2)                                                #This sets the listbox to view available playlists
lbcurrentmusic.grid(column = 0, row = 4)                                            #This sets the listbox to view available music
lbeditplaylist.grid(column = 3, row = 2)                                            #This sets the listbox to add remove playlists
lbaddsongs.grid(column = 3, row = 4)                                                #This sets the listbox to add/remove music
delete.grid(column = 4, row = 2, sticky = SW)                                       #This sets the DELETE playlist button
delete2.grid(column = 4, row = 4, sticky = SW)                                      #This sets the DELETE song button
tipbox.grid(column = 0, row = 8, columnspan = 4, rowspan = 2)                       #This sets the TabTip frame
tip.grid(column = 0, row = 1, columnspan = 4)                                       #This sets the tips in the TabTip frame
addplaylistbutton.grid(column = 1, row = 2)                                         #This sets the playlist selection button
addsongbutton.grid(column = 1, row = 4)                                             #This sets the song selection button
nametextbox.grid(column = 1, row = 6, columnspan = 3, sticky = W)                   #This sets the box for user input
entername.grid(column = 0, row = 6, sticky = E)                                     #This sets the label for the user input box



# This runs the GUI loop
#--------------------------------------------------------------------------------------------------------------------------------------------#

lbeditplaylist.selection_set(0)
root.mainloop()
