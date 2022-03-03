import discord
from discord.ext import tasks # needed for tasks
import datetime # for dat time objects
import os


client = discord.Client()
global Events #global variable used for storing events
Events = [] # empty list for events
TOKEN = 'OTI4NDMwMTk1NzEzNjcxMjQ5.YdYqAA.YkiTkHjKImz2lUgO2zNCnnBux5o'


@tasks.loop(seconds=10) #Excute the code below in a defined duration
async def check_events():
    current_date = datetime.date.today() # collecting current time
    print(current_date.strftime("%d-%b-%Y")) # print current date
    channel = client.get_channel(929040126103928913) # collecting the channel where the bot will send the messages
    for event in Events: #going through all the events
        date = datetime.datetime(int(event[1][2]), int(event[1][1]), int(event[1][0])) # Creates date time we are checking
        date_formatted = date.strftime("%d-%b-%Y") # formats the  datetime
        print(date_formatted)
        if date.isocalendar() == current_date.isocalendar(): #checks to see if it is the same day
            await channel.send("Reminder:: " + event[0] + " on " + date_formatted + " is happening today!!!") # confirm it is the same day
            Events.pop() #removes the event as it doesnt need to be reminded and it will be over by the next day
        elif date.isocalendar()[1] == current_date.isocalendar()[1] and date.year == current_date.year: #checks if it is the same week or year
            await channel.send("Reminder:: " + event[0] + " on " + date_formatted + " is happening this week!!!") #if it is same, send message event happens this week



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    check_events.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!addevent'):  # add add-event function
        event_name = message.content.split(":")[0][10:] # get events name from string
        date = message.content.split(":")[1] # get date from string
        date_format = date.split(".") # Splits the date into the DD/MM/YYYY list
        print(date_format)
        event = [event_name, date_format] # creating a list containing event name and date
        Events.append(event) # Appends it to the event list
        print(Events)

    if message.content.startswith("!rmevent"): # add remove-event function
        event_to_remove = message.content[9:] # gathering event name from the message
        print(event_to_remove)
        for event in Events: # going through every events
            print(event[0])
            if event[0] == event_to_remove: # compare to see if it's the same event
                Events.pop() # Removes the event it is the same

    if message.content.startswith("!viewevents"): #view events function
        for event in Events: # going through all the events
            date_format = datetime.datetime(int(event[1][2]), int(event[1][1]), int(event[1][0])) # Create a date time object from  event
            await message.channel.send("Event: " + event[0] + " Date:" + date_format.strftime("%d-%b-%Y")) # send a message about the event

client.run(TOKEN)