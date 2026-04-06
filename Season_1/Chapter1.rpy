label splashscreen:
    scene black with tleaf
    with Pause(.5)
    scene ix4 with dssb
    pause
    scene black with dssr
    return



define persistent.dialogueBoxOpacity = 1.0


label start:
    define mh = Character('Miss Hill' , color="#11D7EE")
    define d = Character('[name]' , color="#85D7EE")
    define n = Character('Nami' , color="#A80808")
    define m = Character('Nojiko', color="#585858")
    define may = Character('Maja', color="#E8D41F")
    define maj = Character('Maja', color="#E8D41F")
    define u = Character('Unknown Person' , color="#482E78")
    define s = Character('Summer' , color="#19CE1F")
    define na = Character('Nadia' , color="#F46931")
    define ay = Character('Ayua' , color="#01FF71")
    define v = Character('Victoria' , color="#ffcc66")
    define dr = Character('Doctor' , color="#ecd9c6")
    define j = Character('Jeffrey' , color="#B3A7AE")
    define mi = Character('Mila' , color="#F4319B")
    define po = Character('Police Officer' , color="#4BA5D2")
    define b = Character('Bella' , color="#F7B70E")
    define t = Character('Trey' , color="#9EC8F2")
    define ma = Character('Miss Marla' , color="#6D1046")
    define ms = Character('Mister Stahl' , color="#68D7EE")
    define so = Character('Sonya' , color="#187FE6")
    define bari = Character('Barista' , color="#261293")
    define sil = Character('Silvie' , color="#261293")
    define ev = Character('Eva' , color="#11D7EE")
    define bm1 = Character('Amber' , color="#DCBE6D")
    define bm = Character('Amber' , color="#DCBE6D")
    define am = Character('Amber' , color="#DCBE6D")
    define mar = Character('Mario' , color="#4BA5D2")
    define nur = Character('Nurse' , color="#13D74E")
    define cl = Character('Claire' , color="#13D74E")
    define har = Character('Miss Harrison' , color="#13D74E")
    define emi = Character('Emilio' , color="#F46931")
    define sec = Character('Security' , color="#F46931")
    define ci = Character('Cindy' , color="#465951")
    define bari = Character('Barista' , color="#261293")
    define sil = Character('Silvie' , color="#261293")
    define cel = Character('Celina' , color="#f56f42")
    define ka = Character('Karen' , color="#abf5dc")
    define za = Character('Zara' , color="#007bff")
    define sai = Character('Sai' , color="#5e0b12")
    define nan = Character('Nancy' , color="#023f52")
    define nia = Character('Nia' , color="#f25a97")
    define rob = Character('Robin' , color="#fff79c")
    define lay = Character('Layla' , color="#465951")
    define desi = Character('Desiree' , color="#5d3bf5")
    define ow = Character('Shop Owner' , color="#c8c3db")
    define sas = Character('Sasha' , color="#c8c3db")
    define dam = Character('Damian' , color="#e3af84")
    define mh = Character('Coach Hill' , color="#731515")
    define dav = Character('Dave' , color="#731515")
    define lari = Character('Larissa' , color="#731515")
    define moll = Character('Molly' , color="#abf5dc")

    define mw = Character('Jenna' , color="#731515")
    define jen = Character('Jenna' , color="#731515")
    define sg = Character('Susan Gale' , color="#e3af84")
    define dam = Character('Damian' , color="#e3af84")
    define kel = Character('Kelly' , color="#261293")
    define rm = Character('Charlie' , color="#c8c3db")
    define adri = Character('Adrianna' , color="#c8c3db")
    define mad = Character('Madison' , color="#F46931")
    define emilia = Character('Emilia' , color="#F46931")
    define katie = Character('Katie' , color="#007bff")
    define mika = Character('Mikala' , color="#465951")
    define anna = Character('Anna' , color="#ecd9c6")
    define aliy = Character('Alyson' , color="#F7B70E")
    define pen = Character('Penelope' , color="#13D74E")
    define dg = Character('David Goggy' , color="#5d3bf5")
    define pat = Character('Patrick' , color="#261293")
    define lou = Character('Louise' , color="#e3af84")

    ######################################################

    $ messages = [] # list of all messages in the dialogue
    $ message_time = True # if True - get current time / or [hours, minutes] / or False
    $ in_history = True # add messages to history
    $ choice_number = True # default 1. choice1 / 2. choice2 / etc. / or False
    $ click_to_continue = False # if False - live mode messages
    $ time_to_send_pm = 2.0 # time to send picture message
    $ time_to_send_am = 2.0 # time to send audio message
    $ under_messenger = True # set False if you don't need a darker background under messenger

    $ typewriter = False # if False - you instantly send a message
    $ typewriter_speed = 4 # how fast you type
    $ interlocutor_name = "[name]" # interlocutor's name
    $ interlocutor_name_color = '#c4c4c4' # interlocutor's name color
    $ interlocutor_online = True # interlocutor status
    $ interlocutor_typing = True # if False - interlocutor instantly sends a message
    $ interlocutor_extra_time = 0.0 # extra writing time
    $ interlocutor_typing_speed = 0.025   # default speed 0.1 * number of letters
    $ groupchat_enable = False
    $ groupchat = GroupChat(name='GChat') # Group Chat Name
    $ groupchat.add( Interlocutor(ID=1, name='Nami', color='#f3f68f') ) # Interlocutor 1
    $ groupchat.add( Interlocutor(ID=2, name='Bella', color='#b73b87') ) # Interlocutor 2
    $ groupchat.add( Interlocutor(ID=3, name='Trey', color='#009999') ) # Interlocutor 3
    $ groupchat.add( Interlocutor(ID=4, name='Jeff', color='#d6ff60') ) # Interlocutor 4
    $ groupchat.add( Interlocutor(ID=5, name='Ayua', color='#f3f68f') ) # Interlocutor 1
    $ groupchat.add( Interlocutor(ID=6, name='Victoria', color='#b73b87') ) # Interlocutor 2
    $ groupchat.add( Interlocutor(ID=7, name='Mila', color='#009999') ) # Interlocutor 3
    #$ groupchat.add( Interlocutor(ID=8, name='Maja', color='#d6ff60') ) # Interlocutor 4
    $ groupchat.add( Interlocutor(ID=9, name='Nojiko', color='#f3f68f') ) # Interlocutor 1
    $ groupchat.add( Interlocutor(ID=10, name='Nadia', color='#b73b87') ) # Interlocutor 2
    #$ groupchat.add( Interlocutor(ID=11, name='Zara', color='#009999') ) # Interlocutor 3
    #$ groupchat.add( Interlocutor(ID=12, name='Nia', color='#d6ff60') ) # Interlocutor 4
    #$ groupchat.add( Interlocutor(ID=13, name='Amber', color='#f3f68f') ) # Interlocutor 1
    #$ groupchat.add( Interlocutor(ID=14, name='Layla', color='#b73b87') ) # Interlocutor 2
    #$ groupchat.add( Interlocutor(ID=15, name='Stefanie', color='#009999') ) # Interlocutor 3
    #$ groupchat.add( Interlocutor(ID=16, name='Sasha', color='#d6ff60') ) # Interlocutor 4
    $ active_groupchat = groupchat # Set Active Group Chat
    $ dialogue_Mila = []
    $ dialogue_one = [] #Bella
    $ dialogue_two = [] #Nami
    $ dialogue_Trey = []
    $ dialogue_GChat = [] #Groupchat1
    $ dialogue_Nojiko = []
    $ dialogue_vic = []


    ##############################################################################################


    stop music
    scene black with Dissolve(1)
    with Pause(.5)
    scene ix2 with dssb
    pause
    scene ix3 with dssa
    pause
    show screen music_player_trigger
    scene ix5 with dssa
    pause
    scene ix6 with dssa
    pause
    scene ad1983 with dssr

    pass

    $ name = renpy.input("What is your name?", default = "Nika", length = 14)
    $ name = name.strip()
    scene black with dssb
    $ play_playlist(playlist_Ch5_Nia)
    show text "A long time ago..." with dssb
    with Pause(2)
    hide text with dssb
    with Pause(.5)
    scene xx395 with dssb
    pause
    scene xx396 with dissolve
    s "Do you think it's alive?"
    d "I have no idea."
    scene xx397 with dissolve
    s "Touch it."
    d "No! You touch it."
    scene xx398 with dissolve
    s "Why is it white?"
    d "Maybe it's an albino?"
    scene xx399 with dissolve
    s "Albino spiders?"
    s "Is that a thing?"
    d "I guess? Isn't there some sort of albino of everything?"
    s "Human albinos?"
    scene xx400 with dissolve
    d "That's a thing... Like those African people that are white."
    s "Huh..."
    scene xx401
    pause
    scene xx400
    s "I think it's dead!"
    scene xx402 with vpunch
    s "*gasp* AHHH!"
    d "NOT DEAD!"
    scene xx403 with Dissolve(2)
    s "It's... looking at us!"
    d "You- albino spider!"
    scene xx404 with Dissolve(1)
    s "I think it was napping! It probably had a long day of work!"
    scene xx405 with dissolve
    d "Do you think spiders dream?"
    s "Maybe... Maybe they even have.. wet dreams."
    d "Haha, it was probably having one."
    s "And we disturbed it."
    s "No wonder it looks so angry!"
    scene xx406 with dissolve
    d "Oh look, look!"
    scene xx407 with dissolve
    s "It's super angry at us!"
    d "Careful or it will bolt!"
    scene xx408 with dissolve
    s "*gulp*"
    s "I think we should kill it."
    d "Why?"
    scene xx409 with dissolve
    s "It saw our faces! It will tell his albino friends and they will come for us!"
    d "That... sounds plausible."
    scene xx410 with dissolve
    s "Or- or we can put it into Nami's room!"
    d "That's a good idea!"
    scene xx411 with dissolve
    s "But... it could be poisonous."
    scene xx412 with dissolve
    d "Mhh- it could be some exotic thing."
    scene xx413 with vpunch
    s "Waaaah!"
    d "It's fast!"
    scene xx414 with dissolve
    s "You know what?"
    scene xx415 with dissolve
    d "We should find another animal and let them fight?"
    scene xx416 with dissolve
    s "Yes! Exactly what I thought!"
    s "Man... you just get me!"
    scene xx417 with dissolve
    pause
    scene xx418 with dissolve
    s "*soft whisper* Now let's find another animal so we can watch them fight."
    scene black with Dissolve(1.5)
    with Pause(.5)
    scene xx419 with Dissolve(2.5)
    "You and Summer search in the nearby bushes for a worthy opponent."
    scene xx420 with dissolve
    s "I got something!"
    scene xx421 with dissolve
    s "There! An orange one!"
    d "How many spiders are here?"
    scene xx422 with dissolve
    s "*worried* Oh God... What if they are already on us?"
    scene xx423 with vpunch
    d "*pointing at her shoulder and bellowing* Oh god!"
    s "ARRHGH! Get it off me! GET IT OFF!"
    scene xx424 with dissolve
    d "*Laughs*!"
    d "There is nothing on you."
    scene xx425 with dissolve
    s "You are a jerk!"
    scene xx426 with dissolve
    s "Mhhh..."
    scene xx427 with dissolve
    d "And now we should let them fight before they run away."
    scene xx428 with dissolve
    "She gives you a smile."
    with Pause(0.5)
    scene black with Dissolve(2)
    with Pause(.5)
    scene xx429 with Dissolve(2)
    s "My money is on the white one!"
    d "Mine's on the other, then!"
    scene xx430 with dissolve
    s "Ohh- I think it's happening!"
    scene xx431 with dissolve
    "You both giggle as you wait for the fight to happen."
    scene xx432 with dissolve
    pause
    scene xx433 with dissolve
    s "Wh-what are they doing?"
    d "Uh- I think they're..."
    s "Are they...?"
    d "Yep, they are doing it."
    scene xx434 with dissolve
    s "Eww! No bum bum!"
    d "Let's, uh, give them some privacy."
    scene xx435 with dissolve
    s "Ewww.. That's so gross.."
    s "Let's go to the cabin! Far away from- them!"
    d "Yes, we should hurry."
    scene black with Dissolve(2)
    with Pause(0.5)
    scene xx436 with Dissolve(3)
    pause
    s "You were right.."
    d "I told ya."
    scene xx437 with dissolve
    s "It does look a lot creepier with lights on."
    scene xx438 with dissolve
    d "It's already dark... We will never find our way home."
    scene xx439 with dissolve
    s "I think, uhm, we should sleep here?"
    scene xx438 with dissolve
    d "It's our only choice."
    scene xx440 with dissolve
    s "We should have gone back!"
    d "Yeah."
    s "Man! It's all your fault! Yours and the albino spider!"
    d "It's your fault! I told you that we should come back another time!"
    scene xx441 with dissolve
    s "Yes! But tomorrow I'll be gone on a family vacation!"
    s "I really wanted to see you before I'm gone for two weeks!"
    scene xx442 with dissolve
    d "Let's go inside."
    scene xx444 with dissolve
    d "What?"
    scene xx443 with dissolve
    s "I am scared..."
    scene xx445 with dissolve
    pause
    scene xx447 with dissolve
    d "I'll protect you."
    scene xx446 with dissolve
    s "Even if albino spider and his buddies come for me?"
    d "Of course! I will beat them up and then eat them!"
    scene xx448 with dissolve
    s "Ewww. *giggle*"
    scene xx449 with dissolve
    d "My hands are cold..."
    s "I told you to wear gloves!"
    d "Nami borrowed them."
    s "Nami is stupid!"
    scene xx450 with dissolve
    s "But I am still sad that we don't speak anymore..."
    d "I thought you didn't like her?"
    scene xx449 with dissolve
    s "I do like her! But, she... *sigh*"
    d "Nami is sad because you ditched her for me..."
    scene xx452 with dissolve
    s "I didn't!"
    s "I just really like to spend time with you... because.. I love you.."
    s "I told her that it's nothing personal! But she is so sensitive."
    scene xx453 with dissolve
    d "Enough talk about the redhead."
    scene xx452 with dissolve
    s "Why is she even red?"
    d "You asked me that a million times already..."
    scene xx454 with dissolve
    s "I can warm your hands with my gloves..."
    scene xx455 with dissolve
    "You and Summer stare each other in the eyes as she gently rubs your hands to warm them."
    d "(...You are the love of my life.)"
    scene xx457 with dssb
    pause
    scene xx458 with dissolve
    s "What is it?"
    scene xx459 with dissolve
    pause
    scene xx460 with dissolve
    "A strange glowing flower."
    scene xx461 with Dissolve(2)
    "You decide to inspect the strange, light-emitting flower."
    scene xx462 with dissolve
    pause
    scene xx463 with dssr
    s "It is soo beautiful!"
    "You hesitate for a second."
    scene xx464 with dssa
    d "...You see nothing wrong with a strange glowing flower suddenly appearing??"
    scene xx466 with dissolve
    s "No. I see them all the time! They are so cute!"
    scene xx467 with dissolve
    s "No! Don't drop it!"
    scene xx465 with dissolve
    pause
    scene xx468 with dissolve
    d "Summer?"
    scene xx469 with dissolve
    d "Look at me."
    scene xx470 with dissolve
    "A yellow-orange light emits from outside of the cabin."
    scene xx471 with Dissolve(2.5)
    "More of the strange flowers appear, but this time in yellow."
    scene xx472 with Dissolve(2.5)
    "The outside of the cabin is swarmed by these mysterious flowers in different colors."
    scene xx473 with Dissolve(2.5)
    pause
    d "...It's a dream, isn't it?"
    scene BibiEnd with dissolve
    $ renpy.pause(2.0, hard=True)
    $ play_playlist(playlist_Chapter1)
    with Pause(2)
    scene s1 with vpunch
    pause
    scene s2 with dssb
    d "(...This fucking dream...)"
    scene s3 with dssb
    pause
    scene s4 with dssb
    "Your hand is shaking."
    scene s5 with dssb
    d "(Fuck this shit.)"
    d "(Five years and it's still...)"
    scene s6 with dssa
    d "*sigh*"
    d "(Nojiko must be awake.)"
    d "(I should get up... It would be a waste of time to try to sleep in again.)"
    scene s7 with dssb
    d "(Nami's photos before she broke her camera... She wanted to cheer me up.)"
    d "(And succeeded.)"
    scene s8 with dssb
    d "(I can't help but smile a little every time I see them. I love the winter.)"
    scene black with Dissolve(2)
    with Pause(.5)
    scene s9 with dssb
    pause
    scene s10 with dssb
    d "Hey..."
    scene s11 with dssa
    m "Oh, hey! Why are you awake?"
    scene s10 with dssa
    d "You know why..."
    scene s12 with dssr
    m "Oh... You're still dreaming of it?"
    scene s13 with dssa
    m "Sit down... I'll make you some tea."
    d "No, I-... Actually, some tea sounds nice."
    scene s14 with dssb
    d "Do you need to work?"
    m "It's Tuesday."
    d "I thought it was Saturday."
    scene s15 with dssb
    m "You need to get out more."
    scene s16 with dssa
    d "We'll see."
    scene s17 with dssb
    pause
    scene s18 with dssa
    m "You know what..."
    m "Go and get some bread from the bakery."
    m "And get some bread rolls for Nami. I don't want to hear her complaining this early in the morning."
    scene s19 with dssb
    pause
    m "[name]?"
    scene s20 with dssa
    d "Mh? Wait... You were serious?"
    m "Yes."
    scene s21 with dssa
    d "*sigh* Fine."
    scene black with tleaf
    with Pause(.5)
    scene s71 with tleaf
    d "(I love the ambience that the fog in the morning provides. A gentle silence.)"
    d "(If only the world could be this silent all the time.)"
    scene s72 with dssb
    d "(But I'm surrounded by... noise.)"
    d "(Once again, I've caught myself being a misanthrope...)"
    d "(But not all of us are bad... She wasn't...)"
    scene s73 with dssb
    d "(But she's gone...)"
    d "Summer's gone."
    scene s74 with dssb
    pause
    scene s75 with dssa
    u "Where is she?"
    scene s76 with dssb
    d "I was... just speaking about the summer."
    scene s77 with dssb
    u "No, you weren't. You were talking about a person. Someone who meant something to you."
    u "You have sad eyes."
    scene s78 with dssb
    u "Excuse me. I shouldn't get involved in other people's business. It's a bad habit."
    d "(Sharing is caring so they say... But I don't want to burden anyone with it.)"
    scene s79 with dssb
    pause
    scene s80 with vpunch
    pause
    scene s82 with dssb
    pause
    scene sb1719 with dssr
    pause
    scene sb1720 with dssa
    u "It's so foggy and wet... I almost slipped leaving the house."
    scene sb1721 with dssa
    d "Don't take it the wrong way but I'd rather not talk."
    scene sb1722 with dssa
    u "Okay, sorry!"
    u "But you have a nice day and I hope you'll find her."
    scene sb1723 with dssr
    d "...You too."
    scene sb1724 with dssr
    pause
    scene sb1725 with vpunch
    stop music fadeout 3.5
    "A flash of light in your peripheral view- You burst forward and try to grab her-"
    scene sb1727 with dssr
    pause
    scene sb1728 with vpunch
    "-But the slightly wet hoody slips through your fingers..."
    scene black with Dissolve(2)
    hide screen music_player_trigger
    scene VicCH1_Cinematic with dissolve
    $ renpy.pause(4.5, hard=True)
    with Pause(60)
    $ play_playlist(playlist_Chapter1a)
    scene black with Dissolve(2)
    with Pause(.5)
    show screen music_player_trigger
    scene sb1693 with vpunch
    pause
    scene sb1694 with vpunch
    u "Oh FUCK! Oh FUCK!"
    scene sb1695 with dssb
    "She tries to assess the situation but just keeps stumbling over her words."
    u "W-what should we do?!"
    scene sb1696 with dssa
    d "*Calm voice* I'd suggest you call an ambulance."
    scene sb1697 with dssa
    d "Are you having a stroke? What are you waiting for?"
    scene sb1698 with dssr
    u "Nhhh..."
    scene sb1699 with dssa
    d "Don't move."
    d "The ambulance will arrive soon."
    scene sb1700 with dssr
    "The girl starts hyperventilating."
    d "Don't move."
    scene sb1701 with dssa
    u "M-Maja- W-where is Maja?!"
    u "I- I want Maja!"
    scene sb1702 with dssa
    d "(She lost consciousness again.)"
    scene sb1703 with dssr
    d "(I shouldn't move her in case her spine is compromised...)"
    scene sb1704 with dssa
    d "(A cop? Are you fucking kidding me?!)"
    scene sb1705 with vpunch
    d "(That stupid bitch.)"
    scene sb1706 with dssr
    d "Why did you call the police?! She needs an ambulance you fucking idiot!"
    scene sb1707 with dssa
    po "*Blurts* An ambulance is on the way."
    scene sb1708 with dssa
    pause
    scene sb1709 with dssr
    pause
    scene sb1710 with dssa
    "Gently, you move your hand over her forehead."
    scene sb1711 with dssr
    pause
    scene sb1712 with dssr
    d "...Help is on it's way."
    d "But I- I can't stay... I'm sorry."
    scene sb1713 with dssb
    pause
    scene sb1714 with dssa
    pause
    scene sb1715 with dssa
    d "(Her ID.)"
    d "(It must have been sent flying by the car.)"
    d "(Her wallet shouldn't be far.)"
    scene sb1716 with dssa
    d "(Victoria Frohn.)"
    "For a second, you consider going back to give them the ID..."
    d "(Fuck it... I don't have the energy to deal with this shit...)"
    scene sb1717 with dssa
    d "(I need to get out of here...)"
    stop music fadeout 2.0
    scene black with Dissolve(2.5)
    with Pause(.5)
    $ play_playlist(playlist_Chapter1b)
    scene s22 with dssb
    m "-and remember it Nami!"
    scene s23 with dssb
    n "I will!"
    scene s24 with dssb
    pause
    d "Move your ass, Cheeto."
    scene s25 with vpunch
    n "Hey! You address my ass with its proper title!"
    scene s26 with vpunch
    n "Shhhh... But I forgive you... I heard you went outside... Was the fresh air traumatic?"
    scene s27 with dssb
    n "Shhh... I'm here..."
    scene s28 with vpunch
    n "Wait a moment! Where are my bread rolls!?"
    scene s29 with dssa
    d "I was occupied."
    scene s30 with dssa
    n "Occupied with what, you wormy!?"
    scene s31 with dssb
    n "Noji! He forgot my rolls!"
    m "I must have some oven rolls somewhere..."
    scene s32 with dssa
    n "My day is ruined! RUINED!"
    scene s33 with dssa
    d "Stop being a baby."
    scene s34 with dssa
    m "Sorry honey. No oven rolls."
    scene s35 with dssb
    m "[name]! Why didn't you go to the bakery like I told you to?!"
    scene s36 with dssa
    d "A girl got hit by a car. I took care of her until... shortly before the ambulance arrived."
    scene s37 with dssa
    m "Is she okay?"
    scene s38 with dssa
    d "I don't know... and I... don't really care."
    scene s39 with dssa
    m "Did you put her in the recovery position? The one I showed you two?"
    scene s38 with dssa
    d "No. Her spine could've been injured."
    scene s39 with dssa
    m "Good. You've been paying attention."
    scene s40 with dssa
    d "Oh by the way... I found her wallet. It must have been sent flying by the car."
    m "And you'll give it back."
    scene s41 with dssa
    d "No."
    d "Can you do it please? I have no interest in seeing her."
    scene s42 with dssa
    m "No. You will do it!"
    scene s41 with dssa
    d "You just have to pretend you found it. 'I was walking down the street when I found this precious wallet.'"
    d "'I then tried to find the owner, and well...'"
    d "'Here I am... Victoria.'"
    scene s43 with dssb
    m "Is that her name?"
    d "Yes, according to her ID."
    scene s44 with dssb
    n "Was there money in the wallet?"
    scene s45 with dssa
    d "Nope, no money."
    d "I might go as far as waterboarding you, but I would not steal from a person who just had an accident."
    scene s46 with dssb
    n "Wow. Now I look like the jerk here..."
    d "Well... You did rent Spa-"
    scene s47 with vpunch
    n "EH, EH, EH, EH!"
    m "*sigh*."
    scene s48 with dssr
    m "I'm getting ready, and then I'm off to work. Remember, college starts in three weeks!"
    scene s49 with dssa
    m "And [name], take Victoria her wallet."
    scene s50 with dssr
    n "Asshole!"
    n "You swore, you wouldn't tell her I rented Spank Canyon 4!"
    scene s51 with dssa
    d "No? I said I'd hint at it to make you uncomfortable."
    scene s50 with dssa
    n "What did she look like?"
    scene s51 with dssa
    d "Mh?"
    scene s50 with dssa
    n "Victoria."
    scene s52 with dssa
    d "Like a girl."
    scene s53 with dssa
    "Nami stares at you. Visibly annoyed."
    scene s54 with dssa
    d "She was blonde... brown yellow eyes... I guess other people could call her visual appearance... cute."
    scene s55 with dssa
    n "Maybe she's going to reward you... For saving her life, you know."
    d "Yeah, I could use some money."
    scene s56 with dssb
    n "I wasn't talking about money."
    scene s57 with dssa
    d "I know but I chose to ignore your innuendo."
    scene s56 with dssa
    n "She must be in the Aqualia Hospital, right?"
    scene s58 with dssa
    d "...Yeah."
    scene s59 with dssa
    n "I'll come with you."
    d "*sigh*"
    scene s61 with dssa
    n "You know Nojiko. She won't let it go until you've returned it."
    d "I know... Let's just see if we can find a relative who can take it off our hands."
    scene s59 with dssa
    n "Let's do it today! I want to seeeee her!"
    d "Why?"
    scene s62 with dssb
    n "My gut tells me we should go there today! And... Wait! It's whispering something..."
    n "And it told me I should be there with you!"
    scene s63 with dssa
    d "Your gut is a weirdo."
    scene s64 with vpunch
    n "And in three weeks we're going to college!"
    scene s65 with dssr
    d "I totally forgot about that."
    scene s66 with dssa
    n "How could you forget that? Oh right.... Victoria is all you think about."
    scene s67 with dssa
    d "Oh shut up, Cheeto."
    scene black with Dissolve(2)
    with Pause(.5)
    scene s68 with dssb
    d "(I totally forgot about the fucking college...)"
    scene s69 with dssb
    d "(My parents died when I was three.)"
    scene s70 with dssb
    d "(I can't even remember their faces. But losing them didn't really affect me.)"
    d "(I guess I was too young to know what happened... but Summer... that's a different story.)"
    with Pause(0.5)
    scene black with Dissolve(2.0)
    stop music fadeout 2.0
    show text "4 hours later" with Dissolve(1.5)
    hide text with Dissolve(1.5)
    jump NamiRoomch1x0


label NamiRoomch1x0:
    $ play_playlist(playlist_Chapter1a)
    scene ad1803 with dssb
    pause
    scene ad1804 with dssa
    pause
    scene ad1805 with dssr
    pause
    scene ad1806 with dssb
    pause
    scene ad1807 with dssa
    pause
    scene ad1808 with vpunch
    "*Plop*"
    scene ad1809 with dssa
    n "Hi."
    scene ad1810 with dssa
    d "Hi."
    scene ad1811 with dssa
    pause
    d "Are we just gonna ignore the fact that you're in my room while I'm sleeping."
    scene ad1812 with dssa
    n "I think that's for the best."
    scene ad1813 with dssr
    d "Weirdo."
    scene ad1814 with dssa
    n "I think 9 out of 10 dentists would confirm that you're the weirdo."
    scene ad1813 with dssa
    d "*Sigh*"
    d "Alright Cheeto... One time offer... You go alone to the-"
    scene ad1815 with dssa
    n "No!"
    scene ad1816 with dssr
    "You sit up."
    d "God I hate you."
    n "God hates you, too."
    menu:
        "Insensitive joke":
            scene ad1817 with dssr
            d "Is that why neither you nor I have parents?"
            scene ad1818 with dssa
            n "Not cool."
        "Joke":
            scene ad1817 with dssr
            $ NTJ +=1
            d "Apparently he hates you too... Otherwise you would have more tiddies."
            scene ad1819 with vpunch
            n "WOW!"
            n "Y-you-..."
            scene ad1820 with vpunch
            n "Yeah! Fuck you God! What's that about!?"
        "Nothing":
            pass
    scene ad1821 with dssb
    d "Ugh... Let's get it done."
    n "Finally, I'm going to meet the infamous Vic!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad1822 with dssb
    pause
    scene ad1823 with dssr
    d "Aqualia Hospital... Bus or subway?"
    scene ad1824 with dssa
    n "Bus."
    n "Subway's only good if you want to go south to the beach."
    scene ad1826 with dssr
    d "Or you need low quality drugs."
    scene ad1825 with dssa
    n "Or a five dollar blowjob."
    scene ad1825 with dssa
    d "Alright, let's get this done."
    stop music fadeout 2.0
    scene black with tleaf
    with Pause(.5)
    $ play_playlist(playlist_Ch1Bus)
    scene ad1827 with tleaf
    pause
    scene ad1828 with dssa
    d "I have a headache."
    scene ad1829 with dssa
    n "From what?"
    scene ad1830 with dssa
    d "The sun... The outside."
    scene ad1829 with dssa
    n "Don't let the fresh air in too deep or you might get used to it."
    scene ad1831 with dssr
    pause
    scene ad1832 with dssa
    pause
    scene ad1833 with dssa
    d "Yo, I have no card."
    scene ad1834 with dssa
    n "He has a student ticket."
    d "I do?"
    scene ad1835 with vpunch
    n "You do! You idiot! We got it two weeks ago with our other college stuff."
    scene ad1836 with dssr
    u "I don't care. Just get in."
    scene ad1837 with dssa
    pause
    scene ad1838 with dssr
    d "Must be orange juice..."
    scene ad1839 with dssa
    n "Let's hope it is."
    scene ad1840 with dssr
    pause
    scene ad1841 with dssa
    d "Where's Obama's Kebab?"
    scene ad1842 with dssa
    n "It's been closed for like a year."
    d "Huh."
    scene ad1843 with dssr
    n "I'm excited!"
    n "What does Victoria look like?"
    scene ad1844 with dssa
    d "You saw her ID."
    scene ad1843 with dssa
    n "It's an ID. Nobody looks good on an ID."
    scene ad1845 with dssr
    d "Summer did."
    scene ad1846 with dssr
    n "Yeah... She nailed them."
    n "Back to Vic."
    scene ad1847 with dssr
    d "I told you already how she looked..."
    d "She's small... Blonde hair... Yellow/hazlenut eyes."
    scene ad1848 with dssa
    d "A cute face."
    scene ad1849 with dssr
    n "Awww... I hope she's okay."
    scene ad1850 with vpunch
    n "Yo Dave!"
    scene ad1851 with dssa
    dav "Hey Nami!"
    scene ad1852 with dssr
    n "Remember Dave?"
    scene ad1853 with dssa
    d "No."
    scene ad1852 with dssa
    n "The one that was always on Adderall."
    scene ad1854 with dssa
    d "I only know Adderall Annie."
    stop music fadeout 2.0
    scene black with dssb
    with Pause(.5)
    $ play_playlist(playlist_Chapter1a)
    scene ad1855 with dssb
    pause
    scene ad1856 with dssa
    n "Do you feel weird?"
    scene ad1857 with dssa
    d "I was never here before. Why would I?"
    scene ad1858 with dssr
    pause
    scene ad1859 with dssa
    n "You were here before."
    n "The uuuh- violent incident."
    scene ad1860 with dssa
    d "Oh."
    d "I didn't know it was... here."
    scene ad1861 with dssr
    pause
    scene ad1862 with dssr
    u "Hold the door!"
    scene ad1864 with dssr
    pause
    scene ad1865 with dssa
    pause
    scene ad1866 with vpunch
    pause
    scene ad1867 with tleaf
    n "Hello."
    scene ad1868 with dssr
    n "We're looking for Victoria Frohn."
    scene ad1869 with dssa
    u "Are you family?"
    scene ad1870 with dssa
    pause
    scene ad1871 with dssa
    n "*Lies* ...Yes."
    scene ad1872 with dssr
    n "*Lies* I'm Nami Frohn and this is [name]."
    u "She's in Room 19."
    scene ad1873 with dssa
    n "Thanks!"
    scene ad1874 with dssa
    d "What?"
    scene ad1875 with dssa
    u "What?"
    scene ad1876 with dssa
    d "Where'd you get that candy?"
    scene ad1877 with dssa
    u "It's mine! I got it for me and a friend!"
    d "I don't want yours. I just want to know if you bought it here."
    scene ad1878 with vpunch
    u "I'm not telling you!"
    scene ad1879 with dssr
    n "Come. Room 19."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    $ play_playlist(playlist_MellowMaja)
    with Pause(.5)
    scene ad1880 with dssb #ency
    pause
    scene ad1881 with dssa
    pause
    scene ad1882 with dssa
    pause
    scene ad1883 with dssr
    pause
    scene ad1884 with vpunch
    n "Hello."
    scene ad1885 with dssa
    u "Who are you?"
    scene ad1886 with dssa
    n "I'm Nami."
    scene ad1887 with dssa
    n "And this here..."
    scene ad1888 with dssa
    d "I'm here."
    scene ad1889 with dssa
    n "Uh- this here's [name]."
    scene ad1890 with dssa
    u "Okay, and?"
    scene ad1891 with dssa
    n "Why are you so rude?"
    scene ad1893 with dssa
    u "Victoria almost gets killed in a car accident after someone threatened to end her life."
    u "You could say I'm a little on edge."
    scene ad1892 with dssa
    n "It's not like we had something to do with it!"
    scene ad1893 with dssa
    u "What's with you? You look suspicious."
    scene ad1894 with dssr
    with Pause(1)
    menu:
        "Where can I buy some candy?":
            scene ad1895 with dssa
            u "What?"
            scene ad1896 with dssr
            d "I saw a child in the waiting hall with some candy... and now I want some, too."
            d "You didn't see a shop around here, did ya?"
            scene ad1897 with dssa
            pause
            scene ad1898 with dssa
            u "*Confused* N-No..."
        "We're here to finish the job.":
            $ JokeFinishTheJob1x0 = True
            d "We're here to finish the job."
            scene ad1899 with vpunch
            u "HELP!"
            scene ad1900 with vpunch
            n "God damnit [name]!"
            n "No! Hey! Relax! He's just talking shit!"
        "Say nothing, just stare.":
            pause
            pause
            scene ad1899 with vpunch
            u "NURSE! HELP!"
            scene ad1900 with vpunch
            n "Relax! He's just screwing with you!"
            n "Change your attitude, please."
    scene ad1901 with dssr
    n "We're here to bring Victoria her wallet."
    scene ad1902 with dssa
    u "Oh, I didn't know that she lost it."
    u "But thanks, you can give it to me."
    scene ad1906 with dssr
    n "No."
    n "He will give it to Victoria personally."
    scene ad1903 with dssr
    u "Why?"
    scene ad1904 with dssa
    n "Why not? He's the one who treated her after the accident."
    scene ad1905 with dssa
    u "Oh, I'm sorry... Thanks for that... It's a very stressful time."
    maj "I'm Maja..."
    scene ad1907 with dssr
    n "It's okay... We totally understand."
    scene ad1908 with dssr
    pause
    scene ad1909 with dssa
    maj "Could you explain to me what happened?"
    scene ad1910 with dssa
    d "She and I met at a crossroad... We walked together for a while, chatted a little and when we were about to part ways, she went to cross the street... and... a car that was driving too fast hit her."
    d "I tried to grab her last second but... She was too far away."
    scene ad1911 with dssa
    n "Is she okay?"
    maj "She's alive... They said she was lucky..."
    scene ad1912 with dssa
    "Maja starts crying."
    scene black with Dissolve(2)  # Day3
    with Pause(.5)
    scene ad1913 with Dissolve(2)
    pause
    scene ad1914 with dssb
    pause
    scene ad1915 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad2376 with vpunch
    u "Get him into OR 4!"
    scene ad2377 with dssa
    u "His lungs collapsed!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad1915 with dssr
    pause
    scene ad1916 with dssa
    "The sound of a door opening pulls you back into the present."
    scene ad1917 with dssr
    pause
    scene ad1918 with dssr
    pause
    scene ad1919 with dssa
    maj "VIC!"
    scene ad1920 with dssa
    pause
    scene ad1921 with dssa
    v "*Weak* Maja?"
    scene ad1922 with vpunch
    maj "Yes sweety. I'm here."
    scene ad1923 with dssr
    v "I don't know what happened."
    maj "You had an accident."
    scene ad1924 with dssr
    pause
    scene ad1925 with dssa
    v "I- I remember you."
    scene ad1926 with dssa
    d "I remember you, too."
    v "G-ood."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad1927 with dssb
    pause
    scene ad1928 with dssr
    d "You don't look that fucked up."
    scene ad1935 with dssr
    pause
    scene ad1933 with dssr
    n "*Whisper* Dude..."
    scene ad1928 with dssr
    d "Are you in any pain?"
    scene ad1929 with dssa
    v "No... I feel like I've had a really long workout... and didn't drink anything for the past 4 years."
    scene ad1930 with dssr
    n "*Sweet* Hi."
    v "Who are you?"
    n "I'm Nami."
    n "[name]'s roomie."
    scene ad1931 with dssr
    v "It's so n-nice that you two came."
    scene ad1927 with dssr
    d "Right. We're here-"
    scene ad1934 with dssa
    n "- We're here to see how you've been and we're so glad you're mostly alright."
    n "We also found your wallet."
    scene ad1932 with dssr
    v "Oh. Thank you."
    scene ad1936 with dssb
    u "Hello."
    u "How do you feel, Victoria?"
    scene ad1942 with dssr
    v "Groggy."
    u "I believe that."
    scene ad1937 with dssa
    u "Are you all family?"
    scene ad1938 with dssa
    d "No."
    scene ad1937 with dssa
    u "Then I'll have to ask you to leave."
    scene ad1939 with dssr
    u "We have to go over some important steps."
    maj "Okay sure."
    scene ad1940 with dssr
    n "Goodbye. Get well soon!"
    scene ad1941 with dssa
    v "Thanks."
    scene ad1943 with dssr
    "Maja brings you and Nami to the door."
    scene ad1944 with dssa
    maj "Thanks again..."
    scene ad1945 with dssa
    n "I hope everything goes well."
    scene ad1946 with dssa
    maj "...Yeah."
    maj "Goodbye."
    scene ad1947 with dssa
    n "Bye."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad1948 with Dissolve(2)
    pause
    scene ad1949 with dssa
    d "Yo! Cheeto. Slow down."
    scene ad1950 with dssa
    d "Dude? What's the matter?"
    play music "music/Suspense/Scott Buckley - Resonance.ogg"
    scene ad1951 with vpunch
    n "Don't 'Dude' me!"
    scene ad1952 with vpunch
    n "GOD! YOU COULD'VE AT LEAST SAID 'Get well soon, Victoria.'"
    n "BUT NO! YOU'RE AN INSOLENT FOOL!"
    scene ad1953 with dssa
    pause
    d "That's why you're mad?"
    scene ad1952 with vpunch
    n "YES! THAT'S WHY I'M MAD."
    scene ad1953 with dssa
    d "She's just some stranger."
    scene ad1952 with vpunch
    n "It's about more than that! I'm trying so hard to make you likeable... To reintegrate you into society and you always fuck it up!"
    scene ad1954 with vpunch
    n "We all were shocked when the whole Summer thing went down but MAN!"
    n "It's been years! GET OVER IT!"
    scene ad1955 with vpunch
    d "What do you think I've been trying to do all this time?!"
    d "Do you think I enjoy my state of mind?!"
    scene ad1956 with dssa
    d "I DREAM OF HER almost every single fucking night."
    d "I hear her voice every night!"
    d "So please, stop being a cunt and worry about your own shit."
    scene ad1957 with vpunch
    n "YOU ARE MY SHIT! I care about you!"
    scene ad1958 with dssa
    n "Idiot!"
    scene ad1959 with dssa
    stop music fadeout 3.0
    "Nami storms off."
    scene ad1960 with dssa
    $ play_playlist(playlist_Ch5_Gas)
    d "*Sigh*"
    scene ad1961 with dssa
    pause
    scene ad1962 with dssa
    d "Thanks."
    scene black with dssb
    with Pause(.5)
    scene ad1963 with dssb
    with Pause(.5)
    d "Do you know what we're gonna eat today?"
    n "Don't talk to me."
    scene ad1964 with dssa
    pause
    scene ad1965 with dssa
    pause
    scene ad1966 with dssa
    pause
    scene ad1967 with dssa
    pause
    scene ad1968 with dssa
    pause
    scene ad1969 with dssa
    pause
    stop music fadeout 2.0
    scene black with dssb
    with Pause(.5)
    $ play_playlist(playlist_Chapter1c)
    scene ad1970 with dssb
    pause
    scene ad1971 with Dissolve(2)
    pause
    d "(...I might not show it, but I feel bad for Victoria.)"
    d "(I pity her.)"
    scene ad1972 with dssr
    d "(She didn't deserve it...)"
    scene ad1974 with dssa
    d "(Funny... Lots of things happen to people who don't deserve it.)"
    scene ad1975 with dssr
    pause
    scene ad1976 with dssa
    pause
    scene ad1977 with dssa
    pause
    scene ad1978 with dssr
    pause
    scene ad1979 with dssr
    d "(I would do anything to get some closure.)"
    scene ad1980 with dssa
    d "(To find out what happened to you...)"
    scene ad1981 with dssa
    pause
    scene ad1982 with dssa
    pause
    scene ad1983 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(0.5)
    scene x480 with Dissolve(2)
    pause
    scene x481 with dssa
    d "What are you thinking about?"
    s "Thingies."
    scene x482 with dssa
    s "All those places on earth... Ya know... I'd really like to visit them someday."
    s "Eat all the weird food... and- and swim with the dolphins."
    scene x486 with dssa
    s "You can come with me if you want."
    s "Imagine all the things we could do!"
    d "Let exotic animals fight?"
    scene x485 with dssa
    s "You know it!"
    scene x486 with dssa
    d "Why do you always buy weird smiley erasers?"
    scene x487 with dssr
    s "They're cute. Look!"
    scene x488 with dssa
    s "*giggles* Now they are kissing."
    scene x490 with dssa
    d "Could be you and me."
    scene x489 with dssa
    "You and Summer gently rub your heads together."
    scene x491 with dssr
    d "Can I have one? I don't have an eraser."
    scene x492 with dssa
    s "Only if you give it back later!"
    d "I promise!"
    s "Good! I'll bless him first!"
    scene x493 with dssa
    "Summer gives the eraser a kiss."
    scene x492 with dssa
    s "And now: take good care of him."
    scene black with dssb
    with Pause(0.5)
    scene ad1984 with dssb
    d "(The toxicity of the question: What could've been?)"
    d "(It's torture.)"
    scene ad1985 with dssr
    d "(And me being all alone doesn't help...)"
    d "(I can't believe I'm saying this... but college might be the solution.)"
    d "(I'll be forced to socialize.)"
    stop music fadeout 2.0
    scene ad1986 with Dissolve(3)
    with Pause(.5)
    "A few hours later."
    scene ad1987 with dssr
    d "(I need to get good with the Cheeto... I need her.)"
    scene ad1988 with dssb
    pause
    play music "music/TheIntangible/The Intangible - Interdimensional Amity.ogg"
    scene ad1989 with dssb
    pause
    scene ad1990 with dssb
    pause
    scene ad1991 with dssb
    pause
    d "*Sigh*"
    scene ad1992 with dssr
    n "Assface."
    scene ad1993 with dssa
    d "I'm afraid."
    scene ad1994 with dssa
    n "What?"
    scene ad1995 with dssa
    d "College is going to start in three weeks and... I don't know if I can handle it."
    scene ad1996 with vpunch
    n "Dude! Of course you can!"
    n "I'll be there, too!"
    scene ad1997 with dssa
    d "I've become so anti social."
    scene ad1996 with dssa
    n "I wouldn't say that... Well, you lost your filter."
    n "But I have seen you speak with people. You can still articulate and speak clearly."
    scene ad1997 with dssa
    d "My comfort zone is raging."
    scene ad1998 with vpunch
    n "Fuck your comfort zone."
    n "We'll handle it."
    scene ad1999 with dssr
    "Nami gently drags you back and wraps her legs around you."
    scene ad2000 with dssa
    d "Do you know anything about the college?"
    scene ad2001 with dssa
    n "Except that we didn't even get the chance to look around for other colleges, no."
    n "But I checked some forums and it's a really good college... Even though most of them were complaining about not getting accepted."
    scene ad2002 with dssa
    d "I have to think about classes... I don't even know what I'm gonna major in."
    d "Probably people."
    scene ad2003 with dssa
    "Nami lets out a little laugh."
    scene ad2004 with dssr
    n "...They have a D1 Basketball team..."
    n "Just saying."
    scene ad2005 with dssa
    d "I haven't played in... forever."
    scene ad2004 with dssa
    n "Talent doesn't vanish. You still got it."
    scene ad2006 with dssa
    n "Did you get your uniform?"
    d "No?"
    d "I don't think there's one."
    n "There is."
    d "If it doesn't get here in time, I'll just get one when we're there."
    scene ad2007 with dssr
    pause
    scene ad2008 with dssa
    n "So I found this weird porn site-"
    scene ad2009 with vpunch
    d "Dude! Come on! No!"
    scene ad2011 with dssa
    d "It's traumatizing enough that I sometimes hear you moan."
    scene ad2012 with vpunch
    n "Can't be! I'm always extremely quiet!"
    scene ad2013 with dssr
    pause
    scene ad2015 with dssr
    pause
    scene ad2016 with dssa
    n "Noji should be back soon."
    n "I'm gonna go play some games until then..."
    scene ad2017 with dssr
    n "And..."
    scene ad2018 with dssr
    n "No matter what... You're not alone."
    n "We're always there for each other."
    scene ad2019 with dssa
    d "Yea."
    scene black with tleaf
    stop music fadeout 2.0
    with Pause(.5)
    show text "Three weeks later." with Dissolve(1)
    with Pause(2)
    scene ad2020 with dssb
    pause
    scene ad2021 with dssb
    pause
    scene ad2022 with dssb
    $ play_playlist(playlist_Chapter1d)
    scene ad2024 with vpunch
    n "ARGH!"
    scene ad2025 with vpunch
    d "Fucking retard! What- the fuck..."
    scene ad2026 with vpunch
    n "COLLEGE! GET UP BITCH!"
    d "FUCK OFF!"
    scene ad2027 with vpunch
    n "YOU WANT ONE OF THESE?!"
    scene ad2028 with vpunch
    d "You littl-"
    scene ad2029 with vpunch
    "Nami sprints away!"
    scene ad2030 with Dissolve(2)
    pause
    d "(...Fucking Cheeto.)"
    scene ad2031 with dssa
    "A slight burst of anxiety shoots through your body."
    scene ad2032 with dssb
    pause
    scene ad2033 with dssa
    d "What's the matter with you cunt?!"
    scene ad2034 with dssa
    m "Hey!"
    scene ad2035 with dssa
    m "Don't call her names!"
    scene ad2037 with dssa
    $ persistent.unlockedImageNami_CH2_8 = True
    d "This moron-"
    n "PEW! PEW!"
    scene ad2036 with dssa
    m "I know [name]..."
    m "Nami woke up a little... excited."
    scene ad2038 with dssb
    d "*Sigh*."
    scene ad2039 with dssa
    m "Did you get your uniform?"
    d "No."
    scene ad2040 with dssa
    n "YOU HAD TO ORDER IT!"
    scene ad2041 with dssa
    d "There was no uniform!"
    scene ad2042 with vpunch
    n "Yes, there was! Other students confirmed it!"
    scene ad2043 with dssa
    pause
    scene ad2044 with dssr
    m "You look pale."
    scene ad2045 with dssa
    d "How would you feel if some Cheeto on coke bursts into your room after sleeping for barely an hour."
    scene ad2044 with dssa
    m "Yeah."
    scene ad2046 with dssa
    m "It's gonna be alright."
    scene ad2047 with dssa
    d "I'll go get a shower and... get ready."
    scene ad2048 with vpunch
    n "Yo!"
    n "You'll need to pay me to get through here!"
    scene ad2050 with vpunch
    n "Nooooo!"
    scene ad2051 with dssa
    n "Yeah, you better run!"
    scene ad2052 with dssr
    m "Nami... Did you drink coffee?"
    scene ad2053 with dssa
    n "Coffee? Good idea!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad2054 with dssr
    m "Now it's perfect."
    scene ad2055 with dssa
    m "You look beautiful."
    scene ad2056 with dssa
    n "Thanks!"
    scene ad2057 with dssa
    m "I'm so proud of you two."
    scene ad2059 with dssa
    d "College is just another way into the rat race."
    d "With additional steps, and that your parents are proud of you."
    scene ad2058 with dssa
    m "It can teach you valuable life skills, and you'll always have something to fall back on."
    scene ad2060 with dssr
    pause
    scene ad2061 with dssr
    pause
    scene ad2062 with dssa
    d "Cheeto?"
    d "You're okay?"
    scene ad2063 with dssa
    n "My belly hurts."
    scene ad2064 with dssa
    m "You're just nervous."
    scene ad2065 with dssa
    n "Soooo nervous... I need some rolls."
    scene ad2066 with dssa
    d "It's time."
    scene ad2067 with dssr
    d "We'll take the E12 Bus?"
    scene ad2068 with dssa
    m "I'll drive you. I want to witness your first steps into adulthood."
    scene ad2069 with dssa
    n "Does this include other 'first times', too?"
    scene ad2070 with dssa
    m "Why do you say such things?"
    scene ad2071 with dssa
    n "I'm so nervous! I joke to calm myself down!"
    scene ad2067 with dssr
    d "I'm good."
    scene ad2068 with dssa
    m "Let's go."
    scene black with dssb
    with Pause(.5)
    scene ad2072 with dssa
    n "Do you have any Kaiser rolls?"
    u "Of course."
    scene ad2073 with dssa
    n "I'll take three."
    scene ad2074 with dssa
    d "You really have problem, you know?"
    n "I do?"
    scene ad2075 with dssa
    d "It's called an addiction."
    d "You can't go a day without these stupid rolls."
    scene ad2076 with dssr
    n "They're my fuel!"
    n "And they calm down my nerves."
    n "Besides, there are no classes today."
    scene ad2077 with dssa
    n "They're going to welcome us first... But you might be in trouble."
    scene ad2078 with dssa
    d "Why?"
    scene ad2077 with dssa
    n "You forgot to buy the official uniform!"
    scene ad2078 with dssa
    d "There was no uniform!"
    scene ad2079 with dssa
    n "Other students confirmed it!"
    scene black with tleaf
    with Pause(.5)
    scene ad2080 with tleaf
    pause
    n "It looked... different on the pictures."
    m "This is the new part of it. It's being renovated as far as I know."
    scene ad2081 with dssr
    d "Say... Where are the uniforms?"
    scene ad2082 with dssa
    n "This might be a freshmen thingy!"
    scene ad2085 with dssr
    d "I don't see her wearing a uniform."
    n "She's probably not a freshman, duh."
    d "Sure."
    scene ad2083 with vpunch
    n "Fuck off."
    scene ad2084 with dssa
    m "Enough."
    scene ad2086 with dssr
    d "Don't cry."
    scene ad2087 with dssr
    m "You two grew up so fast."
    scene ad2088 with vpunch
    m "I am so proud of you both."
    scene ad2089 with dssr
    m "Take care of [name]."
    scene ad2090 with dssa
    n "That's pretty much all I ever do."
    scene ad2089 with dssa
    m "And [name] keep an eye on Nami."
    scene ad2091 with dssa
    d "That's pretty much all I ever do."
    scene ad2092 with vpunch
    n "Bullshit!"
    scene ad2093 with dssr
    pause
    m "*Whisper* Good luck you two."
    scene ad2096 with dssb
    pause
    scene ad2097 with dssb
    d "Have you noticed the looks people are giving you?"
    n "I'm just reminding them that they all forgot their uniform."
    d "Right... I mean... all these people forgot it."
    scene ad2098 with dssb
    n "Y-yeah."
    scene ad2099 with dssr
    d "Where do we need to go?"
    n "The auditorium."
    scene ad2100 with dssr
    pause
    scene ad2101 with dssr
    n "Hello! Excuse me!"
    scene ad2102 with dssr
    u "Tzz."
    scene ad2103 with dssa
    stop music fadeout 2.0
    n "Uh- what?"
    $ play_playlist(playlist_Ch1CollegeBella)
    scene ad2104 with dssa
    pause
    scene ad2105 with dssa
    u "Hi! You must be Nami."
    n "Yes."
    b "I'm Bella. We talked."
    b "I'm glad you managed to get the uniform."
    scene ad2110 with dssr
    n "Say... why aren't you wearing one?"
    scene ad2106 with vpunch
    u "MOR SUCKS!"
    scene ad2107 with dssa
    b "Well..."
    scene ad2108 with dssa
    b "You see... It could be misconstrued if I were to wear the uniform of a rival college on my first day."
    scene ad2109 with dssr
    n "...What?"
    scene ad2111 with dssr
    pause
    scene ad2112 with dssr
    u "Excuse me?"
    u "Did you get lost?"
    scene ad2115 with dssa
    n "...No?"
    scene ad2113 with dssa
    u "*Sigh*"
    scene ad2114 with dssa
    u "Are you in such a desperate need for attention?"
    n "I- I didn't know!"
    u "Follow me. Now."
    scene ad2116 with dssb
    pause
    scene ad2118 with dssa
    d "(Where the hell is the Cheeto going?)"
    scene ad2119 with dssb
    pause
    scene ad2120 with dssb
    "You let your eyes wander through the hall."
    scene ad2121 with dssr
    d "(That blonde bitch did something...)"
    scene ad2122 with dssr
    "Your eyes meet."
    scene ad2123 with dssr
    b "Ugh... I hope he isn't in our classes. We already got enough ugly guys."
    scene ad2125 with dssr
    menu:
        "Ignore her.":
            stop music fadeout 2.0
            pause
        "These hands are rated E.":
            $ achievement.grant("E for Equality.")
            $ achievement.sync()
            $ Equality1x0 = True
            scene ad2126 with dssr
            d "Are you talking about me?"
            scene ad2127 with dssa
            b "Maybe."
            b "What if?"
            scene ad2128 with dssr
            d "These hands are rated E."
            scene ad2129 with dssa
            d "E for equality."
            scene ad2130 with dssa
            "The girl laughs."
            stop music fadeout 2.0
            b "At least he's funny."
    $ play_playlist(playlist_AfterDND)
    scene ad2131 with dssr
    pause
    scene ad2132 with dssr
    d "You."
    scene ad2133 with dssa
    u "Yes?"
    scene ad2132 with dssa
    d "You look lost... which means you're probably a freshman."
    scene ad2133 with dssa
    u "Yeah, I am."
    u "Are you a freshman too?"
    d "Yeah."
    scene ad2134 with dssa
    u "I'm Trey. Nice to meet you."
    scene ad2135 with dssa
    d "I'm [name]."
    d "Apparently we've gotta go to the auditorium."
    scene ad2136 with dssa
    t "I heard the freshmen are meeting outside?"
    scene ad2137 with dssa
    d "Whatever."
    d "If you want we can go there together."
    t "Sure!"
    scene ad2138 with dssr
    t "I'm so excited."
    scene ad2139 with dssa
    d "I'm not."
    scene ad2140 with dssr
    t "Yeah, I got that feeling from you... You look very unbothered."
    scene ad2141 with dssb
    t "College girls..." #3 hübsche girls
    scene ad2142 with dssb
    pause
    t "You don't see this level in a high school."
    scene ad2143 with dssb
    pause
    scene ad2144 with dssb
    pause
    scene ad2145 with dssb
    t "Basketball, huh?"
    d "Yeah..."
    t "Are you gonna apply?"
    d "Not sure... Maybe."
    scene ad2146 with dssr
    t "I'll go for it."
    t "I played it in high school... I wasn't the best but a little cardio can't hurt."
    scene ad2147 with dssa
    d "I have to choose some classes."
    scene ad2148 with dssr
    t "Mila!"
    scene ad2149 with dssa
    pause
    scene ad2150 with dssr
    pause
    scene ad2151 with dssa
    mi "Hey Trey, how are you?"
    t "I'm good!"
    scene ad2152 with dssa
    t "This is [name]."
    scene ad2153 with dssa
    mi "Hi! Nice to meet you, I'm Mila."
    d "Hi."
    scene ad2154 with dssa
    mi "You give me a weird vibe."
    d "You'll get used to it."
    mi "If you had a trench coat I'd be worried you'd shoot up the school."
    scene ad2155 with dssa
    d "I promise... I'll shoot you last."
    mi "...Thanks."
    scene ad2156 with dssa
    u "Hey Mila!"
    scene ad2157 with dssa
    mi "Hey Ayua."
    scene ad2158 with dssa
    mi "Does anyone know where we have to go?"
    scene ad2159 with dssa
    d "Auditorium."
    t "Outside."
    scene ad2160 with dssa
    mi "I heard we're supposed to meet here."
    scene ad2161 with dssa
    t "Maybe Jeff knows?"
    scene ad2162 with dssa
    mi "Is he already here?"
    scene ad2163 with dssa
    pause
    scene ad2164 with dssa
    mi "Where's [name]?"
    t "Uuh..."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad2293 with dssr
    pause
    scene ad2294 with dssa
    d "(This should be the Auditorium.)"
    scene ad2295 with dssr
    pause
    scene ad2296 with dssa
    pause
    scene ad2297 with dssa
    u "Hey! Are you-"
    scene ad2298 with dssa
    d "- A freshman."
    scene ad2299 with dssa
    j "Great! I'm Jeff."
    d "[name]."
    j "I heard we're meeting here?"
    scene ad2300 with dssa
    d "That's what I heard, too."
    d "Others say outside."
    j "Doesn't really matter."
    d "Yeah, they'll find us eventually."
    scene ad2301 with dssa
    pause
    scene ad2302 with vpunch
    n "Fuck this place."
    scene ad2303 with dssr
    j "Whoa there..."
    n "Sorry..."
    scene ad2304 with dssa
    d "Where did you go?"
    n "This uniform..."
    scene ad2305 with dssa
    j "Is from a rival college."
    scene ad2304 with dssa
    n "Yup... She fooled me."
    d "That blonde bitch?"
    scene ad2305 with dssa
    j "Long ponytail, yellow/green eyes?"
    scene ad2306 with dssa
    n "Yes. Do you know her?"
    scene ad2307 with dssa
    j "Oh yeah... Bella."
    j "I don't want to put her down but... She's a very difficult person."
    scene ad2308 with dssa
    t "She's a weirdo."
    t "Hot, but a fucking weirdo."
    scene ad2309 with dssa
    mi "Hi!"
    mi "I'm Mila."
    scene ad2310 with dssa
    n "Hello, I'm Nami."
    scene ad2311 with dssa
    t "I'm Trey."
    n "Hi!"
    scene ad2312 with dssa
    j "Yo... What up?"
    t "What up?"
    j "Did you ride a cycle during the summer?"
    scene ad2313 with dssa
    t "...No."
    j "Motherfucker."
    scene ad2314 with dssa
    mi "But yeah, stay away from Bella."
    mi "It only brings unnecessary trouble."
    scene ad2315 with dssa
    n "Oh, I'll get back at her."
    scene ad2316 with dssr
    j "Hmm... Are you interested in sports?"
    scene ad2317 with dssa
    d "No."
    scene ad2318 with dssa
    n "He is."
    n "He's good at basketball."
    scene ad2319 with dssa
    j "Nice. I'm also going for the team."
    j "But... you look a little out of shape."
    j "You should come to the gym with us."
    scene ad2320 with dssa
    menu:
        "I'll think about it.":
            $ jeff +=1
            $ Jeffgym1x0 = True
            scene ad2319 with dssa
            j "Great!"
        "Not at the moment.":
            $ Jeffgym1x0 = False
            $ jeff -=1
            scene ad2319 with dssa
            j "Your choice, buddy."
    scene ad2321 with dssa
    u "Ah!"
    u "You're all freshmen?"
    scene ad2322 with dssa
    mi "Yes."
    scene ad2323 with dssa
    ma "I'm Miss Marla."
    ma "Please follow me."
    stop music fadeout 2.0
    scene black with tleaf
    $ play_playlist(playlist_GirlyCh4x)
    with Pause(.5)
    scene ad2165 with tleaf
    pause
    scene ad2166 with dssr
    ma "Where's the rest?"
    scene ad2167 with dssr
    lari "Many freshmen apparently decided not to come... As this is not mandatory."
    scene ad2168 with dssr
    d "It's not?"
    scene ad2169 with dssa
    n "I didn't know."
    scene ad2170 with dssa
    mi "I could've slept longer..."
    scene ad2171 with dssa
    pause
    scene ad2172 with dssa
    pause
    scene ad2173 with dssr
    ma "Welcome to ZPR College!"
    ma "I'm Miss Marla, and I'm a Professor here."
    scene ad2174 with dssa
    ma "Larissa here volunteered to help me with today's introduction."
    scene ad2175 with dssa
    lari "A big welcome from me, too."
    lari "We'll start with a tour around the campus."
    lari "This here is the reception... If you need any information about the college and its facilities. You can get them here."
    lari "If you have applied for a dorm room or house, you can get your keys here too."
    scene ad2176 with dssr
    d "I'm hungry."
    scene ad2177 with dssa
    pause
    scene ad2178 with dssa
    n "Those are my rolls."
    d "I don't want your stupid rolls."
    n "That's what they all say and then..."
    scene ad2179 with vpunch
    n "BAM! My rolls are gone!"
    scene ad2181 with dssa
    pause
    scene ad2180 with dssr
    n "*Cough* Please continue."
    scene ad2182 with dssr
    ma "As I was saying, Karen, who usually works the reception isn't here right now."
    scene ad2183 with dssr
    ma "*Mumbles* For whatever reason..."
    ma "Follow me please."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad2184 with dssr
    ma "This is the cafeteria."
    scene ad2185 with dssa
    ma "It's also accessible for non-students but students get 50 percent off."
    scene ad2188 with dssb
    d "Do you think I can sneak away and grab one of those sandwiches?"
    scene ad2186 with dssr
    pause
    scene ad2187 with dssa
    d "Oh. Wrong Cheeto."
    scene ad2189 with dssa
    n "Dude..."
    scene ad2190 with dssa
    lari "We'll move on."
    scene ad2191 with dssa
    mi "Still pretty expensive here."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad2192 with dssr
    ma "And now about the history of our college."
    scene ad2193 with dssr
    d "Kill me now."
    scene ad2194 with dssa
    n "Did you just see that topless girl?"
    d "No."
    n "She had nice tiddies."
    scene ad2195 with dssa
    n "Let's sneak away."
    scene ad2196 with dssa
    mi "I'm in."
    scene ad2197 with dssr
    j "Follow me!"
    scene black with tleaf
    with Pause(.5)
    scene ad2198 with tleaf
    pause
    scene ad2199 with dssa
    t "That woman could really go on and on and on..."
    scene ad2200 with dssr
    d "I should've gotten a sandwich..."
    scene ad2201 with dssa
    n "You can eat my arm."
    scene ad2200 with dssa
    d "Who knows where that arm has been."
    scene ad2202 with dssa
    n "Do you all know each other?"
    scene ad2203 with dssa
    mi "Jeff, Trey and I went to the same high school."
    j "Yeah, many people here are from our old high school."
    scene ad2203 with dssa
    mi "At least the smart ones..."
    scene ad2204 with dssa
    mi "Trey, how did you get in again?"
    t "Hey!"
    scene ad2203 with dssa
    mi "Where are you two from?"
    scene ad2205 with dssa
    n "We went to a high school way in the west."
    scene ad2206 with dssr
    pause
    scene ad2207 with dssa
    d "I get the feeling you brought us here for a reason."
    scene ad2208 with dssa
    j "Sharp."
    scene ad2209 with dssr
    j "Imagine this place being full of people... all watching you make the winning basket... The last 20 meter on the track... or the furthest jump."
    scene ad2210 with dssr
    pause
    scene ad2211 with dssa
    d "Yeah, it does nothing for me."
    scene ad2212 with dssa
    j "Nothing?"
    d "I don't care about fame or being known."
    j "What do you care about?"
    scene ad2213 with dssa
    d "I don't know... The Cheeto."
    j "You're a cute couple."
    scene ad2214 with dssa
    n "Whoa, whoa, woah! We're roomies!"
    j "Oh!"
    scene ad2215 with dssa
    mi "I also thought you were a couple."
    scene ad2216 with dssa
    t "So did I."
    scene ad2218 with dssr
    n "So Mila... Tell me about yourself!"
    scene ad2217 with dssa
    pause
    scene ad2219 with dssr
    j "That's Bella."
    j "She's uh... well, yeah... Not a good person."
    scene ad2220 with dssr
    j "The one with the hat. That's Nadia,"
    j "Nice girl. But she isn't very social most of the time."
    scene ad2221 with dssr
    t "She's also undateable."
    d "Undateable?"
    t "Every guy that has ever asked her out failed."
    scene ad2222 with dssr
    d "Maybe she's asexual."
    j "She isn't."
    j "Nadia's just a little weird... and competitive."
    t "Competitive?"
    scene ad2223 with dssr
    j "Have you ever seen her play?"
    t "Play what?"
    j "Anything. Board games, sports... hell, even the math test."
    scene ad2224 with dssr
    d "And the other one?"
    j "Ayua."
    t "Oh Ayua... That's one hell of a girl."
    t "Drives a muscle car."
    scene ad2225 with dssr
    t "I'm sure she's somehow involved into the racing slash tuning community."
    mi "Didn't she beat you up before?"
    t "..."
    scene ad2226 with dssr
    j "Ayua is cool. But don't say anything bad about her friends, that includes Bella."
    t "Ayua's a very skilled fighter and also trains people in various martial arts."
    d "I can imagine... She has an aura around her."
    t "Maybe she just farted?"
    scene ad2227 with dssr
    j "Come on... All males agreed that girls don't do that."
    scene ad2228 with dssa
    pause
    scene ad2229 with dssa
    pause
    stop music fadeout 2.0
    scene black with Dissolve(2)
    $ play_playlist(playlist_AmbientBella)
    with Pause(.5)
    scene ad2367 with vpunch
    s "You bibi!"
    scene ad2368 with dssa
    d "You're the bibi!"
    "(Bibi is pronounced 'Bee Bee' and refers to something baby-like.)"
    scene ad2369 with dssr
    pause
    scene ad2370 with vpunch
    pause
    scene ad2372 with vpunch
    s "SEE! BIBI!"
    scene ad2371 with dssr
    d "You always foul me!"
    scene ad2373 with dssr
    s "Do you hear that?"
    scene ad2374 with vpunch
    s "IT SOUNDS LIKE A BIBI!"
    scene ad2375 with vpunch
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad2230 with dssr
    pause
    scene ad2231 with dssr
    pause
    scene ad2232 with dssa
    mi "Hey."
    scene ad2231 with dssa
    d "Hey."
    scene ad2232 with dssa
    mi "Mind if we talk for a second?"
    $ milatalk = True
    scene ad2231 with dssa
    d "(Stay strong [name]... Don't let the comfort zone win and be nice...)"
    d "Sure."
    scene ad2233 with dssr
    mi "I recognize a broken mind when I see one."
    scene ad2234 with dssa
    d "My mind isn't broken."
    scene ad2233 with dssa
    mi "You're right. It's shattered."
    scene ad2235 with dssa
    mi "You remind me of someone. A girl I used to know from high school. Always trying to look normal, nothing weird about her, except that... certain aura."
    d "What aura?"
    scene ad2236 with dssa
    mi "An aura that..."
    scene ad2237 with dssa
    mi "Hah..."
    scene ad2238 with dssa
    mi "That scares me."
    scene ad2239 with dssa
    d "And I have that aura, ya?"
    scene ad2238 with dssa
    mi "Yes. She killed herself a few weeks before graduation... And you know what's the worst part of it?"
    scene ad2239 with dssa
    d "What?"
    scene ad2238 with dssa
    mi "I knew about it. I knew that she was having issues. I saw it in her eyes. I felt her inner conflict."
    scene ad2236 with dssa
    mi "But I didn't do anything to prevent it. I didn't trust myself. I thought I would annoy her if I speak to her about it."
    mi "And now, she's dead."
    scene ad2240 with dssa
    d "And where are you going with this? Do you think I'm going to kill myself?"
    scene ad2241 with dssa
    mi "No, there are different types of... 'dealing with it'."
    mi "And you look like a person who'd prefer to hurt others."
    scene ad2242 with dssa
    mi "I might be wrong and you'd prefer to kill yourself, too."
    scene ad2243 with dssa
    mi "But please just keep in mind that there are people you can talk to."
    scene ad2244 with dssa
    menu:
        "Joke.":
            d "I'll keep it in mind when I shoot up the school."
            scene ad2248 with dssa
            mi "*Laughs*."
            scene ad2246 with dssa
            mi "No, but for real, keep it in mind."
        "I appreciate your concern... But worry about your own stuff.":
            scene ad2245 with dssa
            pause
            scene ad2246 with dssa
            mi "Yeah, sorry."
        "I will.":
            scene ad2247 with dssa
            mi "Good."
    scene ad2249 with dssa
    n "Oh! I'll get back at her!"
    j "Don't Nami... It's not worth the trouble."
    t "He's right."
    scene ad2250 with dssr
    n "Pff! I'll do it anyways!"
    scene ad2251 with dssr
    d "Cheeto? Wanna go home?"
    scene ad2252 with dssa
    n "No, not yet."
    scene ad2251 with dssa
    d "Alright, you stay a little longer but I'm gonna go."
    scene ad2253 with dssr
    n "See you later!"
    stop music fadeout 2.0
    scene black with Dissolve(2)
    $ play_playlist(playlist_Ch1CollegeEnd)
    with Pause(.5)
    scene ad2254 with dssr
    pause
    scene ad2255 with dssb
    d "(...She walks too slow to make distance but too fast to overtake in a comfortable way.)"
    d "(Stupid NPC.)"
    scene ad2257 with dssr
    pause
    scene ad2258 with vpunch
    u "We're sick of having to hide our boobs behind fabric!"
    u "Same rights for everyone!"
    scene ad2259 with dssr
    d "(Where was this damn cafeteria again...)"
    scene ad2260 with dssb
    pause
    scene ad2261 with dssb
    pause
    scene ad2263 with dssa
    pause
    scene ad2264 with dssa
    pause
    scene ad2265 with dssa
    pause
    scene ad2266 with dssa
    d "(Thank you.)"
    scene ad2267 with dssr
    pause
    b "*Mumbles* ...What the fuck?"
    scene ad2268 with dssr
    pause
    scene ad2270 with dssb
    pause
    scene ad2271 with dssb
    d "(Tasted pretty good... with a hint of justice.)"
    scene ad2272 with dssa
    stop music fadeout 2.5
    "Suddenly, you spot someone."
    scene ad2273 with dssr
    $ play_playlist(playlist_Chapter1)
    pause
    scene ad2274 with dssr
    pause
    scene ad2275 with dssa
    pause
    scene ad2276 with dssa
    d "I had hoped you'd just walk past."
    scene ad2277 with dssa
    maj "Me too."
    scene ad2276 with dssa
    d "I saw the conflict."
    scene ad2277 with dssa
    maj "...*Sigh*"
    maj "Victoria asked for you."
    scene ad2276 with dssa
    d "How did you find me?"
    scene ad2278 with dssr
    maj "By accident."
    maj "She asked me a week ago to find you."
    maj "I was just bringing in some papers for her when I saw you."
    d "She's coming here, too?"
    scene ad2279 with dssa
    maj "Yeah."
    scene ad2280 with dssr
    d "I don't believe in coincidences."
    scene ad2281 with dssa
    maj "I prefer to believe it's a coincidence because I don't want you two to be connected."
    d "So? You found me. What now?"
    maj "Would you visit her?"
    d "I really don-"
    scene ad2282 with dssa
    maj "Please."
    maj "The situation is hard on her... It might really help... and believe me, I wouldn't be asking you if I didn't have to."
    maj "She's very vulnerable right now... and it's taking a toll on her mental health."
    scene ad2283 with dssa
    d "Fine."
    d "As long as you take me home afterwards."
    scene ad2282 with dssa
    maj "I will."
    scene ad2284 with dssa
    pause
    scene ad2285 with dssa
    maj "Is Nami here, too?"
    d "M-"
    scene ad2286 with vpunch
    u "STOP THE Raccoon!"
    maj "Uaaah!"
    scene ad2287 with vpunch
    u "Don't let him near a water supply! "
    scene ad2288 with dssa
    pause
    scene ad2289 with dssa
    maj "This place didn't change a bit..."
    scene ad2290 with dssr
    maj "Oh, they finally allowed the 'FreeTheBoobs' movement."
    maj "I remember when we created it... So many suspensions."
    scene ad2291 with dssr
    d "...Let's do it."
    d "And if we get the chance to save the Raccoon... We will."
    scene ad2292 with dssa
    maj "No way that animal gets into my car."
    stop music fadeout 2.0
    scene black with tleaf
    with Pause(.5)
    scene ad2324 with tleaf
    pause
    scene ad2325 with dssr
    maj "She's in her room."
    d "Because I know where her room is..."
    scene ad2326 with dssa
    maj "Down the hall on the right."
    maj "And knock before-"
    scene ad2328 with vpunch
    d "Hey!"
    v "*Gasps*"
    scene ad2327 with vpunch
    stop music fadeout 2.0
    maj "Fucking rowdy!"
    $ play_playlist(playlist_Ch1Vic)
    scene ad2329 with Dissolve(2)
    pause
    scene ad2330 with dssa
    v "Hi!"
    v "Maja found you!"
    scene ad2331 with dssa
    d "Yeah, she did."
    scene ad2330 with dssa
    v "I'm glad you came by."
    scene ad2332 with dssa
    d "I wonder why though?"
    scene ad2333 with dssa
    v "I keep dreaming of you."
    scene ad2334 with dssr
    d "Well, dreams are just drea-"
    d "(...I wish dreams were just dreams.)"
    scene ad2335 with dssa
    v "Please sit down."
    scene ad2336 with dssa
    d "How's it going-... I mean..."
    d "Rolling."
    scene ad2337 with dssa
    v "Going: Bad... Rolling: Good."
    scene ad2336 with dssa
    d "Do you know what's up with your legs?"
    scene ad2338 with dssa
    v "I can't feel them."
    d "Nothing?"
    scene ad2339 with dssr
    v "I- I imagine some sort of feeling whenever I see someone touch it."
    v "But I think it's just my imagination."
    scene ad2340 with dssa
    d "I'm sorry to hear that."
    scene ad2341 with dssa
    v "I'll work with what I have."
    scene ad2342 with dssa
    d "(She seems pretty strong... Might just be a facade she's putting up in front of me.)"
    d "You seem pretty okay with it."
    scene ad2341 with dssa
    v "What's the point in crying over it? It won't change my situation. It will only make it worse."
    v "I'm going to make the best out of it."
    scene ad2342 with dssa
    d "You're a positive person. That's the essence to happiness."
    d "(Maja's description was different... But Maja's also going through a lot right now.)"
    scene ad2343 with dssa
    d "Back to my question..."
    scene ad2344 with dssa
    v "I want to get to know you."
    scene ad2343 with dssa
    d "Why?"
    scene ad2344 with dssa
    v "I think you're cute."
    d "...Listen, I-"
    scene ad2345 with dssa
    v "I-It's okay- I don't want an answer... I just want to put a thought into your head."
    v "It's going to evolve over time and then you can tell me what you think."
    scene ad2346 with dssa
    d "Sounds like a plan."
    d "And apparently we're both going to ZPR."
    scene ad2347 with dssa
    v "Yeah. I saw your name on the list."
    d "Will you be there tomorrow?"
    v "Yes. At least until next week when I start physical therapy."
    scene ad2348 with dssr
    menu:
        "I wish you the best.":
            scene ad2350 with dssa
            v "Thanks!"
        "I see.":
            pass
    scene ad2349 with dssa
    pause
    scene ad2348 with dssa
    d "If you uh- got a phone we could stay in contact."
    scene ad2351 with dssa
    v "It got destroyed in the accident."
    v "But as soon as I have a new one, I'll give you my number!"
    scene ad2352 with dssa
    d "Alright Victoria."
    scene ad2353 with dssa
    v "T-Thanks for coming by."
    d "No problem."
    scene ad2354 with dssr
    d "(I feel like a little weight got lifted off my shoulders... Apparently I was subconsciously affected by her fate.)"
    d "(But seeing her this 'happy' helped me a little.)"
    scene ad2355 with dssa
    d "I'll see you tomorrow... and take care."
    scene ad2356 with dssa
    v "Yes... Bye [name]..."
    scene ad2357 with dssa
    pause
    scene ad2358 with dssa
    v "*Whisper* I'll see you..."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad2359 with dssr
    pause
    scene ad2360 with vpunch
    pause
    scene ad2361 with dssa
    maj "I was uh- just checking the uh- paint."
    scene ad2362 with dssa
    "Your raise a brow."
    scene ad2363 with dssa
    maj "What? I don't want you to influence her!"
    scene ad2364 with dssa
    d "I don't blame you."
    scene ad2365 with dssa
    d "You promised me a ride back."
    scene ad2366 with dssa
    maj "Yes."
    stop music fadeout 2.0
    $ vici = 1
    $ mila = 1
    jump report2
