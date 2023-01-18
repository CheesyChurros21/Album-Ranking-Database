import discord, mysql.connector, asyncio
from discord.ext import commands
from Album import Album


#BOT PREFIX

bot = commands.Bot(command_prefix = "|", help_command=None) #turns off default help list (its trash)


@bot.command(aliases = ["newalbum","NewAlbum","enter"])
async def newAlbum(a):


    #FUNCTIONS FOR GATHERING ALBUM INFORMATION

    circleName = await askCircleName(a)
    
    albumTitle = await askAlbumTitle(a)

    global songAmount

    songAmount = await askSongAmount(a)

    albumURL = await askAlbumURL(a)

    pictureURL = await askPictureURL(a)

    global album

    album = Album(circleName, albumTitle, songAmount, albumURL, pictureURL)

    await confirmation(a, album) #relays all inputted information back to check

    valid = 0

    while valid == 0:

        reply = await bot.wait_for('message', check=None) #checks the users next message

        if (reply.content == "kill"): #stops command if you need to
            await a.send("Command Killed")
            return

        elif ((reply.content).lower() == "yes"):
            #await albumDataStore(a, album)
            await a.send("Next")
            valid = 1

        elif ((reply.content).lower() == "no"):

            fix = 0

            while fix == 0: #THIS PART NEEDS CLEANING, PROBABLY MORE FUNCTIONS

                await a.send("What would you like to fix? (1 = Circle Name, 2 = Album Title, 3 = Song Amount, 4 = Album URL, 5 = Picture URL, 6 = Done)")
                reply = await bot.wait_for('message', check=None) #checks the users next message

                if not reply.content.isdigit(): #doesnt put number from 1-6
                    await a.send("Messed up input, try again")

                elif int(reply.content) == 1:
                    album.updateCircleName(await askCircleName(a))

                elif int(reply.content) == 2:
                    album.updateAlbumTitle(await askAlbumTitle(a))

                elif int(reply.content) == 3:
                    album.updateSongAmount(await askSongAmount(a))

                elif int(reply.content) == 4:
                    album.updateAlbumURL(await askAlbumURL(a))
                
                elif int(reply.content) == 5:
                    album.updatePictureURL(await askPictureURL(a))

                elif int(reply.content) == 6:
                    await confirmation(a, album)

                    reply = await bot.wait_for('message', check=None) #checks the users next message

                    if (reply.content == "kill"): #stops command if you need to
                        await a.send("Command Killed")
                        return

                    elif ((reply.content).lower() == "yes"):
                        #await albumDataStore(a, album)
                        await a.send("Next")
                        valid = 1
                        fix = 1

                    elif ((reply.content).lower() == "no"):
                        pass

                    else:
                        await a.send("Messed up input, try again")

        else: #messed up input
            await a.send("Messed up input, try again")
    
    await rating(a)



#HELPER FUNCTIONS



async def askCircleName(a):
    await a.send("Circle Name?")

    valid = 0

    while valid == 0:

        reply = await bot.wait_for('message', check=None) #checks the users next message

        if (reply.content == "kill"): #stops command if you need to
            await a.send("Command Killed")
            return

        else:
            valid = 1
            return (reply.content)

    return


async def askAlbumTitle(a):
    await a.send("Album Title?")

    valid = 0

    while valid == 0:

        reply = await bot.wait_for('message', check=None) #checks the users next message

        if (reply.content == "kill"): #stops command if you need to
            await a.send("Command Killed")
            return

        else:
            valid = 1
            return (reply.content)
    
    return


async def askSongAmount(a):
    await a.send("Amount of Songs? (number only)")

    valid = 0

    while valid == 0:

        reply = await bot.wait_for('message', check=None) #checks the users next message

        if (reply.content == "kill"): #stops command if you need to
            await a.send("Command Killed")
            return

        elif (reply.content).isnumeric(): #checks the message charcater (should be a number)
            valid = 1 #exits loop
            return int(reply.content)#converts message to int

        else:
            await a.send("Messed up input, try again")

    return


async def askAlbumURL(a):
    await a.send("Album URL?")

    valid = 0

    while valid == 0:

        reply = await bot.wait_for('message', check=None) #checks the users next message

        if (reply.content == "kill"): #stops command if you need to
            await a.send("Command Killed")
            return

        elif (reply.content == "Album URL?"):
            pass

        else:
            valid = 1
            return (reply.content)

    return


async def askPictureURL(a):
    await a.send("Picture URL?")

    valid = 0

    while valid == 0:

        reply = await bot.wait_for('message', check=None) #checks the users next message

        if (reply.content == "kill"): #stops command if you need to
            await a.send("Command Killed")
            return

        elif (reply.content == "Picture URL?"):
            pass

        else:
            valid = 1
            return (reply.content)

    return


async def confirmation(a, album):
    await a.send("-\nIs this correct? (Yes/No)\n\n" + album.getPictureURL())
    await a.send(album.getCircleName() + " - " + album.getAlbumTitle() + "    >>>>    Total Songs: " + str(album.getSongAmount()) + "\n" + album.getAlbumURL())
    await a.send("-")

async def rating(a):

    average1 = 0
    average2 = 0

    channel1 = discord.utils.get(a.guild.channels, name="jordan-ranking-area")
    channel2 = discord.utils.get(a.guild.channels, name="nick-ranking-area")

    songNumber = 1

    while songNumber < songAmount + 1:
        await channel1.send("Ratings for Song " + str(songNumber) + "?")
        await channel2.send("Ratings for Song " + str(songNumber) + "?")

        rating1, rating2 = await asyncio.gather(
            bot.wait_for('message', check=lambda b: b.channel == channel1),
            bot.wait_for('message', check=lambda b: b.channel == channel2)
        )

        rating1 = rating1.content
        rating2 = rating2.content

        if isfloat(rating1) == False and isfloat(rating1) == False:
            await channel1.send("Messed up input, put only numbers (no x/10)")
            await channel2.send("Messed up input, put only numbers (no x/10)")

            while isfloat(rating1) == False and isfloat(await rating2) == False:
                rating1, rating2 = await asyncio.gather(
                    bot.wait_for('message', check=lambda b: b.channel == channel1),
                    bot.wait_for('message', check=lambda b: b.channel == channel2)
                )

                rating1 = rating1.content
                rating2 = rating2.content

        if isfloat(rating1) == False:
            await channel1.send("Messed up input, put only numbers (no x/10)")

            while isfloat(rating1) == False:
                await channel1.send("Ratings for Song " + str(songNumber) + "?")
                rating1 = bot.wait_for('message', check=lambda b: b.channel == channel1)

                rating1 = rating1.content


        if isfloat(rating2) == False:
            await channel2.send("Messed up input, put only numbers (no x/10)")

            while isfloat(rating2) == False:
                await channel2.send("Ratings for Song " + str(songNumber) + "?")
                rating2 = bot.wait_for('message', check=lambda b: b.channel == channel2)

                rating2 = rating2.content

        average1 = average1 + float(rating1)
        average2 = average2 + float(rating2)

        songNumber = songNumber + 1

    await channel1.send("Subjective Rating?")
    await channel2.send("Subjective Rating?")

    subjective1, subjective2 = await asyncio.gather(
        bot.wait_for('message', check=lambda b: b.channel == channel1),
        bot.wait_for('message', check=lambda b: b.channel == channel2)
    )

    subjective1 = subjective1.content 
    subjective2 = subjective2.content

    if isfloat(subjective1) == False and isfloat(subjective2) == False:
        await channel1.send("Messed up input, put only numbers (no x/10)")
        await channel2.send("Messed up input, put only numbers (no x/10)")

        while isfloat(subjective1) == False and isfloat(subjective2) == False:
            rating1, rating2 = await asyncio.gather(
                bot.wait_for('message', check=lambda b: b.channel == channel1),
                bot.wait_for('message', check=lambda b: b.channel == channel2)
            )

            subjective1 = subjective1.content 
            subjective2 = subjective2.content

    if isfloat(subjective1) == False:
        await channel1.send("Messed up input, put only numbers (no x/10)")

        while isfloat(subjective1) == False:
            await channel1.send("Ratings for Song " + str(songNumber) + "?")
            rating1 = bot.wait_for('message', check=lambda b: b.channel == channel1)

            subjective1 = subjective1.content 

    if isfloat(subjective2) == False:
        await channel2.send("Messed up input, put only numbers (no x/10)")

        while isfloat(subjective2) == False:
            await channel2.send("Ratings for Song " + str(songNumber) + "?")
            rating2 = bot.wait_for('message', check=lambda b: b.channel == channel2)

            subjective2 = subjective2.content

    await channel1.send("Objective Rating: " + str(float(round(average1/songAmount, 4))) + "/10")
    await channel2.send("Objective Rating: " + str(float(round(average2/songAmount, 4))) + "/10")

    await channel1.send("-\n Finished Ranking Session")
    await channel2.send("-\n Finished Ranking Session")

    await toDatabase(a, album, float(subjective1), float(subjective2), float(round(average1/songAmount, 4)), float(round(average2/songAmount, 4)))

    
def isfloat(a):
    try:
        float(a)
        return True
        
    except ValueError:
        return False


async def toDatabase(a, album, subjectiveJordan, subjectiveNick, objectiveJordan, objectiveNick):
    connection = mysql.connector.connect(
    host="placeholder",
    user="placeholder",
    password="placeholder"
    )

    if connection.is_connected() == True:
        print("Successful Connection")

    else:
        print("Failed To Connect")

    c = connection.cursor()

    c.execute("CREATE DATABASE IF NOT EXISTS Benben_Tsukumo")

    connection = mysql.connector.connect(
    host="placeholder",
    user="placeholder",
    password="placeholder",
    database="placeholder"
    )

    c = connection.cursor()

    sql = """CREATE TABLE IF NOT EXISTS Albums(
        orderNumber INT(3) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        circleName VARCHAR(100) NOT NULL,
        albumTitle VARCHAR(100) NOT NULL,
        songAmount INT(2) NOT NULL,
        albumURL VARCHAR(200) NOT NULL,
        pictureURL VARCHAR(200) NOT NULL,
        subjectiveJordan DECIMAL(5, 4) NOT NULL,
        subjectiveNick DECIMAL(5, 4) NOT NULL,
        objectiveJordan DECIMAL(5, 4) NOT NULL,
        objectiveNick DECIMAL(5, 4) NOT NULL
    )"""

    c.execute(sql)

    row = (album.getCircleName(), album.getAlbumTitle(), album.getSongAmount(), album.getAlbumURL(), album.getPictureURL(), subjectiveJordan, subjectiveNick, objectiveJordan, objectiveNick)

    c.execute("""INSERT IGNORE INTO Albums (circleName, albumTitle, songAmount, albumURL, pictureURL, subjectiveJordan, subjectiveNick, objectiveJordan, objectiveNick)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", row)

    connection.commit()

    c.execute("SELECT * FROM Albums ORDER BY orderNumber DESC LIMIT 1")

    albums = c.fetchall()

    channel = discord.utils.get(a.guild.channels, name="album-history")

    for row in albums:
        await channel.send("Album Number: " + str(row[0]) + "\n\n" + str(row[5]))
        await channel.send(str(row[1]) + " - " + str(row[2]) + "    >>>>    Total Songs: " + str(row[3]) + "\n\n" + str(row[4]))
        await channel.send("-\n\nSubjective Rating:\n" + "Jordan - " + str(row[6]) + "/10\nNick - " + str(row[7]) + "/10\n\nObjective Rating:\n" + "Jordan - " + str(row[8]) + "/10\nNick - " + str(row[9]) + "/10\n\n-\n-\n-\n-")

    connection.close()

    

#IMPORTANT BOT ACTIVATING STUFF



@bot.event
async def on_ready(): #prints in terminal bot is ready to be used
    print("Benben Tsukumo is at your service")

"""
@bot.event
async def on_command_error(a, error): #for general bad inputs not already locally handled, causes entire command to be killed
    if isinstance(error, commands.CommandNotFound): #non-existant command called
        await a.send('Command does not exist, try the "help" command or check your spelling')

    elif isinstance(error, commands.MissingRequiredArgument): #when a command needs multiple inputs, but less than required is put (deprecated cause multi step commands)
        await a.send("You forgot something when putting the info after the command, check your inputs again")
"""

bot.run("Redacted Bot Token") #runs bot (inside is the bot token, replaced for privacy reasons)



#DEPRECATED STUFF

"""
@bot.command(aliases = ["list"])
async def albumList(a):

    stringo = ""

    with open("Album List.txt") as file:
        
        info = file.readlines()

        for i in info:
        
            if stringo == "":
                stringo = stringo + i

            else:
                stringo = stringo + i

    await a.send(stringo) 


@bot.command(aliases = ["rank", "rankingSession", "rankSession", "albumTime", "rankTime"])
async def ranking(a):

    await newAlbum(a)

    for i in range(1, songAmount+1):
        stringo = "" 
        stringo = stringo + str(i) + "\n"

    await a.send(stringo)


@bot.command()
async def albumSearch(a, *albumTitle):
    file = open("Album List.txt", "r")
   
    listo = file.readlines()

    specified = []

    enumList = enumerate(listo)
    for i, ii in enumList:
        if (" ".join(albumTitle)).lower() in ii.lower():
            album = [listo[i-1].strip(), ii.strip(), listo[i+1].strip(), listo[i+2].strip()]
            specified.append(album)

    if len(specified) == 0:
        await a.send("No Album Found, Check Your Spelling")
        return

    else:
        stringo = specified[0][0] + "\n" + specified[0][1] + "\n" + specified[0][2] + "\n" + specified[0][3] #NOTE extremely trash and redundant code, fix in future
        await a.send(stringo)

@bot.command()
async def circleSearch(a, *circleName):
    
    file = open("Album List.txt", "r")
   
    listo = file.readlines()

    specified = []

    enumList = enumerate(listo)
    for i, ii in enumList:
        if (" ".join(circleName)).lower() in ii.lower():
            album = [ii.strip(), listo[i+1].strip()]
            specified.append(album)


    if len(specified) == 0:
        await a.send("No Circle Found, Check Your Spelling")
        return

    else:
        stringo = ""

        for i in specified:
            if stringo == "":
                stringo = stringo + i[0] + "\n" + i[1]

            else:
                stringo = stringo + "\n\n" + i[0] + "\n" + i[1]

        await a.send(stringo)

async def albumDataStore(a, album):
    file = open("Album List.txt", "a+")
    
    file.write("\n" + album.circle + "\n")
    file.write(album.title + "\n")
    file.write(str(album.songAmount) + " songs\n")
    file.write(album.link + "\n")

    return
"""