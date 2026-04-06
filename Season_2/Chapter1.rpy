label splashscreen:
    # scene black with tleaf
    # with Pause(.5)
    # if not persistent.language_selected:
    #     show screen LanguageSelection
    # scene ix4 with dssb
    # pause
    # scene black with dssr
    scene black with dssr
    with Pause(.5)
    scene Disclaimer1 with dssr
    pause 
    scene Disclaimer2 with dssr
    pause 
    scene Disclaimer3 with dssr
    pause 
    scene Disclaimer4 with dssr
    pause 
    scene black with Dissolve(1)
    return


default persistent.dialogueBoxOpacity = 1.0
label start:
    jump Start

label Start:
    define dssb = Dissolve(1.5)
    define dssa = Dissolve(.5)
    define dssr = Dissolve(1)
    define throne = Character('Maddie Thorne' , color="#11D7EE")
    define carspeaker = Character('Car speaker' , color="#11D7EE")
    define mh = Character('Miss Hill' , color="#11D7EE")
    define tvanchor = Character('Tv Anchor' , color="#11D7EE")
    define john = Character('John' , color="#11D7EE")
    define d = Character('[name]' , color="#85D7EE")
    define n = Character('Nami' , color="#A80808")
    define miri = Character('Miriam' , color="#A80808")
    define no = Character('Nora' , color="#A80808")
    define m = Character('Nojiko', color="#585858")
    define dwi = Character('Dwight', color="#585858")
    define mia = Character('Mia', color="#585858")
    define may = Character('Maja', color="#E8D41F")
    define maj = Character('Maja', color="#E8D41F")
    define u = Character('Unknown Person' , color="#482E78")
    define s = Character('Summer' , color="#19CE1F")
    define na = Character('Nadia' , color="#F46931")
    define eva = Character('Eva' , color="#6D1046")
    define ju = Character('Justine' , color="#6D1046")
    define ay = Character('Ayua' , color="#01FF71")
    define v = Character('Victoria' , color="#ffcc66")
    define su = Character('Summer' , color="#ffcc66")
    define dr = Character('Doctor' , color="#ecd9c6")
    define sedi = Character('Sedila' , color="#ecd9c6")
    define j = Character('Jeffrey' , color="#B3A7AE")
    define mi = Character('Mila' , color="#F4319B")
    define po = Character('Police Officer' , color="#4BA5D2")
    define b = Character('Bella' , color="#F7B70E")
    define t = Character('Trey' , color="#9EC8F2")
    define ele = Character('Elenor' , color="#6D1046")
    define ma = Character('Miss Marla' , color="#6D1046")
    define ms = Character('Mister Stahl' , color="#68D7EE")
    define sam = Character('Samuel' , color="#68D7EE")
    define jar = Character('Jared' , color="#68D7EE")
    define so = Character('Sonya' , color="#187FE6")
    define adam = Character('Adam' , color="#187FE6")
    define son = Character('Sonya' , color="#187FE6")
    define sil = Character('Silvie' , color="#261293")
    define ev = Character('Eva' , color="#11D7EE")
    define bm1 = Character('Amber' , color="#DCBE6D")
    define both = Character('Both' , color="#DCBE6D")
    define va = Character('Vanessa' , color="#c8c3db")
    define kat = Character('Kate' , color="#c8c3db")
    define drs = Character('Dr. Solus' , color="#c8c3db")
    define kate = Character('Kate' , color="#c8c3db")
    define missnorris = Character('Miss Norris' , color="#c8c3db")
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
    define celi = Character('Celina' , color="#f56f42")
    define ka = Character('Karen' , color="#abf5dc")
    define az = Character('Aziz' , color="#abf5dc")
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
    define dav = Character('Dave' , color="#731515")
    define lari = Character('Larissa' , color="#731515")
    define moll = Character('Molly' , color="#abf5dc")
    define nic = Character('Nick' , color="#e3af84")
    define mw = Character('Jenna' , color="#731515")
    define jen = Character('Jenna' , color="#731515")
    define rep = Character('Reporter' , color="#731515")
    define inp = Character('Inessa Petrova' , color="#c8c3db")
    define sg = Character('Susan Gale' , color="#e3af84")
    define kel = Character('Kelly' , color="#261293")
    define charlie = Character('Charlie' , color="#c8c3db")
    define adri = Character('Adrianna' , color="#c8c3db")
    define saki = Character('Saki' , color="#c8c3db")
    define aub = Character('Aubrey' , color="#abf5dc")
    define mad = Character('Madison' , color="#F46931")
    define emilia = Character('Emilia' , color="#F46931")
    define katie = Character('Katie' , color="#007bff")
    define mika = Character('Mikala' , color="#465951")
    define shan = Character('Professor Shan' , color="#465951")
    define anna = Character('Anna' , color="#ecd9c6")
    define maxi = Character('Maxine' , color="#ecd9c6")
    define aliy = Character('Alyson' , color="#F7B70E")
    define pen = Character('Penelope' , color="#13D74E")
    define dg = Character('David Goggy' , color="#5d3bf5")
    define pat = Character('Patrick' , color="#261293")
    define lou = Character('Louise' , color="#e3af84")
    define sasmo = Character('Elena' , color="#c8c3db")
    define kai = Character('Kai' , color="#c8c3db")
    define nero = Character('Nero' , color="#c8c3db")
    define tobi = Character('Tobias' , color="#c8c3db")
    define butler = Character('Butler' , color="#c8c3db")
    define aki = Character('Akiho' , color="#c8c3db")

    ######################################################

    # stop music
    # scene black with Dissolve(1)
    # with Pause(.5)
    # scene ix1 with Dissolve(1)
    # pause
    # scene ix2 with dssr
    # pause
    # scene ix3 with dssa
    # pause
    # show screen music_player_trigger
    # scene ix5 with dssa
    # pause
    # scene ix6 with dssa
    # pause
    # scene ad1983 with dssr

    pass
    $ name = renpy.input("What is your name?", default = "Nika", length = 14)
    $ name = name.strip()
    stop music fadeout(5)
    jump Sanitized


label Sanitized:
    call screen PickSanitized
    call screen Sanitized
    pause
    jump Chapter5x5Start





label Chapter5x5Start:
    show screen music_player_trigger
    $ Bella_H = 0
    if VicDateEntry2 is True:
        $ VicDate = True
    if MilaKiss4x5 or MilaSleep5x0 or MilaLove5x0 is True:
        $ MilaDate = True
    if BellaNonExclusive5x0 is True:
        $ Dating_List.append("Bella")
    if VicDate or VicDateEntry2 is True:
        $ Dating_List.append("Victoria")
    if MilaDate or miladate is True:
        $ MilaDate = True
        $ Dating_List.append("Mila")
    if NiaDate5x0 is True:
        $ Dating_List.append("Nia")
    if RaceWithImpossibleOdds is True:
        $ Dating_List.append("Nami")
    


    if BellaKiss3x5 is False:
        $ NoBella5x5 = True
    if MilaVenus4x5 is True:
        $ MilaVenus = True 
    else:
        $ MilaVenus = False

    if MilaSleep5x0 is True:
        $ MilaDate = True
        jump MilaStart5x5_2
    elif RaceWithImpossibleOdds is True:
        jump NamiNight5x5
    else:
        jump SoloStart5x5_1

label SoloStart5x5_1:
    $ SoloStartS2 = True 
    jump NamiMorningTraining



label MilaStart5x5_2:
    $ play_playlist(playlist_Smooth)
    scene a7997 with dssb
    pause
    scene a7998 with dssa
    "You take a look around your new room."
    d "(No sign of Mila.)"
    scene a7999 with dssa
    "Then the glimpse of a moving shadow to your left."
    scene a8000 with dssr
    "You peek through the window inside a bathroom."
    scene a461 with dssr
    d "Oh. I have my own bathroom."
    scene a462 with dssr
    mi "Yes. And it's pretty awesome!"
    scene a463 with dssa
    mi "I took the liberty of running a bath for us."
    scene a464 with dssa
    mi "And I had hoped you'd join me."
    d "(I showered like 2 hours ago, but... I haven't had a bath in... Huh. Ever.)"
    scene a465 with dssa
    d "I've never had a bath in my life before."
    play sound "Music/Sfx/Punch.ogg"
    scene a466 with vpunch
    mi "How's that possible?!"
    scene a467 with dssa
    d "We never had a bathtub. I always just showered."
    scene a468 with dssa
    mi "You're in for a treat!"
    scene a469 with dssr
    pause
    scene a470 with dssr
    mi "Do you know these fancy bath bombs?"
    scene a471 with dssa
    d "Those balls that look like candy?"
    scene a472 with dssr
    mi "Don't tell me you..."
    scene a473 with dssa
    d "I was pranked... I thought it was one of these candy-stones you could lick."
    scene a474 with dssa
    "Mila laughs."
    scene a475 with dssa
    mi "Was it Nami?"
    scene a476 with dssa
    d "No. My ex-girlfriend Summer."
    scene a478 with dssa
    "Mila's facial features turn stiff, and the air in the room changes."
    scene a479 with dssa
    mi "Oh. I see."
    scene a481 with dssa
    d "...What did Nami tell you about her?"
    scene a480 with dssa
    mi "Not much, really... just uh- that she was your girlfriend, and she... She's gone."
    scene a481 with dssa
    d "Yeah... Gone."
    scene a482 with dssr
    "Mila awkwardly looks around in search of a new topic."
    "Blessed by the Mistress of Empathy, you just know how to ease the situation..."
    scene a483 with dssa
    d "Get nude."
    scene a484 with vpunch
    mi "Wow! You get nude first!"
    mi "I'm already half nude!"
    scene a485 with dssa
    d "It surprises me..."
    scene a486 with dssa
    mi "Let me guess... My piercings."
    scene a485 with dssa
    d "Yup."
    scene a486 with dssa
    mi "Well, we don't really know each other yet."
    scene a485 with dssa
    d "True. The things we know about each other are mostly superficial."
    scene a487 with dssr
    pause
    scene a488 with dssr
    mi "The decision to get pierced meant something to me."
    scene a489 with dssa
    mi "I used to worry a lot about what other people thought of me. I used to wear hoodies and other baggy clothes that hid my curves."
    mi "There was a time in high school when I wished I had small boobs and an unremarkable body."
    scene a490 with dssa
    d "I assume people sexualized you a lot?"
    scene a489 with dssa
    mi "Of course."
    mi "And for a long time, I had a very negative association with everything sex-related."
    scene a492 with dssr
    d "What changed?"
    scene a491 with dssa
    mi "I think I told you about the girl who killed herself a few weeks before graduation?"
    scene ad2235 with dssr 
    mi "You remind me of someone. A girl I used to know from high school. Always trying to look normal, nothing weird about her, except that... certain aura."
    d "What aura?"
    scene ad2236 with dssa
    mi "An aura that..."
    scene ad2237 with dssa
    mi "Hah..."
    scene ad2238 with dssa
    mi "That scares me."
    scene a491 with dssr
    mi "She was the opposite of me. Small boobies, small butt."
    scene a493 with dssa
    mi "Nothing that would particularly attract mockery. People still called her all sorts of names."
    mi "After she ended her life, I kept thinking a lot about her and her situation."
    scene a491 with dssa
    mi "You can do everything right, and you'll still be attacked."
    scene a494 with dssr
    mi "I was already branded as the 'daughter of a whore'... heard stuff like 'Do you get preferred entry at the whore academy because your Mom was an honor grad?'"
    mi "I ignored them but- damn, did it hurt. I developed some sort of trauma."
    scene a495 with dssa
    mi "If I acted and dressed just as plain as possible, there would be no target, right?"
    scene a495a with dssa
    d "When did it change or- what what changed?"
    scene a496 with dssa
    mi "An ex-friend talked bad about me behind my back after a day at the public pool."
    mi "By that time, my frontal lobe had developed enough for me to call it out for what it was. I was so fed up that I just didn't care anymore and owned my body."
    scene a497 with dssr
    mi "The funny thing? The bullying mostly stopped."
    mi "I stopped wearing baggy pants and hoodies and instead wore clothes that accentuated my curves... People treated me differently almost immediately."
    scene a498 with dssr
    mi "What matters is that whatever hand life dealt you, you own it and carry it with confidence."
    mi "It makes all the difference."
    scene a498a with dssa
    d "I assume guys especially stopped trying to bully you?"
    scene a499 with dssa
    mi "I was rarely bullied by guys. It was almost always girls. Unless they had boyfriends or they were guys I previously rejected."
    scene a498a with dssa
    d "What about Mario?"
    scene a499 with dssa 
    mi "Mario didn't bully me directly. He was a bystander, which in my opinion is just as bad."
    scene a499 with dssa
    mi "I'll never just watch when someone gets ganged up on. Not even if it's Bella... *Mumbles* Especially not Bella..."
    mi "Guys obviously started hitting on me a lot more."
    scene a495 with dssr
    mi "But girls? Girls are mean, man."
    mi "...A girl's first bully is her own mother."
    scene a494 with dssa
    mi "And Lena... My mother often put me down in a passive aggressive way."
    mi "Which in my opinion is much worse! It gets you heated up so much more."
    scene a495a with dssa
    d "It's great to hear that you're now carrying yourself with pride."
    scene a508 with dssr
    mi "Getting my nipples pierced was my last 'Fuck you' to my alter ego that did everything to just not draw any attention."
    mi "Now... I just go with the flow."
    scene a509 with dssr
    pause
    scene a510 with dssr
    pause
    scene a511 with dssr
    pause
    scene a512 with dssr
    pause
    scene a513 with dssr
    mi "How's the project going for you and Bella?"
    scene a514 with dssa
    d "I think we're going to fail... We're not doing enough."
    d "How about you?"
    scene a515 with dssa
    mi "Vic's putting in extra work. We're definitely gonna make it."
    scene a516 with dssa
    "You pull down your pants and underwear in one swift motion."
    scene a517 with dssa
    mi "Handsome young man you got there."
    scene a518 with dssa
    "She puffs out some air and holds back some laughter."
    scene a519 with dssr
    mi "I'm so excited."
    mi "I've dreamt of moving out for years... And I can almost feel it."
    scene a520 with dssr
    mi "And do you know what the best part is?"
    scene a942 with dssr
    mi "It's with people I actually like."
    scene a943 with dssa
    mi "And..."
    scene a944 with dssr
    mi "I'm not going to lie, this is also quite nice... especially when we're sharing a house."
    scene a945 with dssa
    d "Yeah."
    scene a944 with dssa
    mi "That didn't sound very convincing."
    scene a946 with dssa
    d "I'm just afraid that we're going to get in a fight in some way and... well, we would be living together."
    scene a947 with dssa
    mi "Hey. We're still just getting to know each other... We're good."
    mi "Just be honest with me and... don't wait too long before our date."
    if Sanitized is False:
        scene a948 with dssr
        mi "I'm not saying you're not worth the wait... but I also don't know you well enough to state the opposite."
        scene a949 with dssa
        d "You don't need to explain yourself. We're in college. Nobody needs to get married."
        scene a950 with dssa
        mi "Thanks for being mature about it."
        scene a949 with dssa
        d "I'll let you know about our date."
        scene a951 with dssa
        mi "You better."
    else:
        pass
    scene a952 with dssr
    mi "Can I ask you a favor?"
    scene a953 with dssa
    d "You'll need help moving your stuff?"
    scene a954 with dssa
    mi "How did you know?!"
    scene a955 with dssr
    d "It was a good guess."
    scene a956b with dssa
    mi "...Yeah, I do."
    scene a956c with dssa
    d "I can ask Nick if we can borrow one of his cars. Zara would probably help us too."
    scene a956d with dssa
    mi "I'd rather not have them meet my parents."
    scene a956e with dssa
    d "Are you this ashamed of them?"
    mi "Mhm."
    scene a956g with dssa
    pause
    scene a956f with dssa
    mi "Let's get in."
    scene a955 with dssr
    pause
    scene a956 with dssa
    "Mila dips in her foot to assess the temperature."
    mi "Mhm... That's good."
    scene a957 with dssr
    "You put your foot in-"
    play sound "Music/Sfx/Punch.ogg"
    scene a958 with vpunch
    d "UGH!"
    d "That's fucking lava!"
    scene a959 with dssa
    mi "What are you talking about? That's good!"
    d "How can you keep your foot in there?"
    mi "I like it like this."
    d "That's insane."
    scene a1051 with dssr
    mi "Come back here... I want to be on top of you."
    scene a1052 with dssa
    mi "Let your body slowly adjust to the temperature."
    play sound "Music/Sfx/Searing.ogg"
    scene a1053 with dssr
    "You pant as you lower your body into the pool of lava."
    scene a1054 with dssa
    d "Sssshhit..."
    scene a1055 with dssa
    mi "I'm coming in."
    scene a1056 with dssr
    mi "Mmmhhhhh..."
    scene a1057 with dssa
    mi "That's the stuff..."
    scene a1058 with dssr
    mi "You're doing okay there?"
    scene a1059 with dssa
    d "...I'm trying to pretend I'm not being boiled alive."
    scene a1060 with dssr
    mi "You baby."
    scene a1061 with dssa
    pause
    scene a1062 with dssa
    mi "Do you know who I found weird... Vanessa."
    scene a1063 with dssa
    d "Mh?"
    scene a1064 with dssa
    mi "It was weird how she said that she knew me... That she knows so much about me."
    scene a1065 with dssr
    d "(Oh, oh.)"
    d "(There's no reason not to tell her.)"
    scene a1066 with dssr
    d "She's the girlfriend of Mario Holgerson."
    scene a1067 with dssa
    pause
    scene a1068 with dssa
    mi "...Seriously?"
    scene a1069 with dssa
    d "Yup."
    "Mila's body tenses up and she gulps."
    scene a1070 with dssr
    d "Don't worry about it."
    scene a1071 with dssa
    mi "I- I don't know what to say."
    scene a1072 with dssa
    d "Say nothing and let's just enjoy this."
    scene a1073 with dssr
    d "(I could move my hand towards her pussy to take her mind off the situation... However, I could risk getting a panic attack.)"
    menu:
        "Take a risk and move your hand towards her pussy.":
            play sound "Music/Sfx/Whisper1.ogg"
            $ Whispers +=1
            $ Mila_Bath_Pussy = True
            $ Mila_Date_STG3 = True 
            scene a1074 with dssr
            pause
            scene a1075 with dssa
            "Mila smiles, grabs your hand, and puts it on her pussy. "
            scene a1077 with dssa
            d "(Okay, it's not that bad... Maybe I am getting better?)"
            scene a1078 with dssa
            "She kisses you on the cheek."
            d "(...I like how it makes her feel.)"
        "Don't take the risk.":
            pass
    scene a1079 with dssa
    mi "I should talk to her."
    scene a1080 with dssa
    d "It can't hurt. But let me be there too, okay?"
    scene a1081 with dssa
    mi "Why? Do you think I can't handle her?"
    mi "But yes. Thank you."
    scene a1082 with dssr
    d "(I need to talk to Bella.)"
    scene a1083 with dssa
    d "(She needs to give that stupid heirloom back.)"
    scene a1084 with dssa
    mi "Vanessa scares me."
    scene a1085 with dssa
    d "She should scare you."
    scene a1086 with dssa
    mi "The heterochromia really gives her that edge."
    scene a1085 with dssa
    d "She thinks males are the weaker sex."
    scene a1087 with dssa
    mi "Really?"
    scene a1088 with dssa
    d "Yup. She says that women can control men so easily."
    scene a1089 with dssa
    mi "I mean, she's not entirely wrong. As a woman, you can weaponize sex."
    mi "We can find sex whenever we want, but it's hard to find a relationship with an amazing person."
    mi "With time, you become wary of guys... And if you've been dealt a bad hand, you'll always expect them to just want sex."
    scene a1090 with dssa
    d "Speaking from experience?"
    scene a1089 with dssa
    mi "No, I was always very selective."
    scene a1090 with dssa
    d "It didn't take much for me to get you in here."
    scene a1091 with vpunch
    mi "Hey!"
    scene a1092 with dssa
    mi "You're different!"
    mi "And there's the thing with Victoria... You cared for her. You helped her go pee."
    scene a1093 with dssa
    mi "You've got some issues, I know... We all do."
    scene a1094 with dssa
    mi "But I think if you'd leave your shell, you'd be an amazing person."
    mi "And you probably hear this all the time... But I'll be there for you, [name]... And I mean it."
    scene a1095 with dssa
    mi "Never ever will I just watch again."
    scene a1096 with dssr
    if bellameet is True:
        d "(Would Mila still think that if she found out she's being sued because of me and Bella? Would it end this here? Probably.)"
        d "(I need to take care of this as soon as possible. Especially if we're moving into the same house with her.)"
    else:
        d "(Would Mila still think that if she found out she's being sued because Bella? And I knew about it and didn't do anything? Would it end this here? Probably.)"
        d "(I need to take care of this as soon as possible. Especially if I'm moving into the same house as her.)"
    if Mila_Bath_Pussy is True:
        scene a1097 with dssa
        mi "*Whispers* Can you put a finger inside?"
        scene a1098 with dssa
        d "(I have to push the boundaries at least a little.)"
        scene a1099 with dssa
        "Gently, you move a finger into her pussy."
        scene a1100 with dssa
        "It's very tight at first... But then it slips in effortlessly."
        "Her pussy envelops your finger tightly..."
        scene a1101 with dssa
        d "(I need to keep it cool... I need to think about something else...)"
        scene a1102 with dssa
        d "(...Rolls. Crunchy rolls. They're so crunchy.)"
    scene a1103 with dssr
    mi "On Monday, I'll ask when we can view the house."
    scene a1104 with dssa
    d "Sounds good. Will it be furnished?"
    scene a1105 with dssa
    mi "The essentials are in there but we will have to get a lot ourselves."
    mi "Have you thought about a job?"
    scene a1106 with dssa
    d "Shit... I forgot about that."
    d "*Sigh* I still need to have a look around."
    scene a1107 with dssr
    d "I want to make the first team."
    scene a1108 with dssa
    mi "That's a big if."
    scene a1109 with dssa
    mi "A-and with that I'm not saying you're not good enough... But it's still a gamble."
    scene a1110 with dssa
    d "I know."
    d "I'll find something for the time being."
    scene a1111 with dssa
    if MilaVenus4x5 is True:
        mi "I think I'll create a Venus profile soon."
        mi "I liked your idea of just posting slightly more daring pictures."
        scene a1112 with dssa
        d "It does make sense."
        scene a1113 with dssa
        mi "If you want you can take some pictures of me tomorrow."
        mi "...Or after we're out of the tub."
        scene a1114 with dssa
        d "Yeah, sure."
        if Mila_Bath_Pussy is True:
            scene a1115 with dssa
            "You slide your finger almost completely out of her..."
            scene a1116 with dssa
            "...And insert a second finger into her pussy."
    else:
        mi "I do earn enough for the place, but I'll eventually have to find something else."
        mi "But even without a job, I could pay the rent for another 10 months."
        scene a1112 with dssa
        d "You saved a lot of money, huh?"
        scene a1113 with dssa
        mi "I got a safe deposit box at the bank where I stash most of my savings."
    scene a1117 with dssa
    d "I wonder what the Cheeto is going to do."
    scene a1119 with dssa
    if Mila_Bath_Pussy is True:
        mi "*Moans* Ngh- I... I asked her but she didn't give me a serious answer and kept joking around."
    else:
        mi "I asked her but she didn't give me a serious answer and kept joking around."
    scene a1118 with dssa
    d "Yeah... Her way of dodging uncomfortable questions."
    d "Maybe she can stick to Robin."
    scene a1119 with dssa
    mi "Robin's family is loaded."
    scene a1121 with dssr
    d "I thought so. I met her mother."
    scene a1120 with dssa
    mi "Oh? Where?"
    scene a1121 with dssa
    d "At that book club."
    scene a1120 with dssa
    mi "How was she?"
    scene a1122 with dssa
    d "She's on a little power trip and apparently hasn't had an intimate relationship in quite a while."
    scene a1123 with dssa
    mi "*Laughs* How do you know that? The hell are you guys talking about there?"
    scene a1124 with dssa
    d "The women there talk... a lot."
    scene a1125 with dssa
    mi "That's sad to hear about her Mama. It must not be easy to come home every night and be mostly alone."
    mi "Robin's soon going to move out... Yeah, it can't be easy for her."
    scene a1126 with dssa
    d "Maybe."
    scene a1125 with dssa
    mi "What's the issue? Is she unattractive?"
    scene a1126 with dssa
    d "No, she's rather attractive but it comes with a certain personality."
    d "And I'd argue that she doesn't settle for less than what she wants."
    scene a1133 with dssr
    "She chuckles."
    scene a1128 with dssr
    mi "Being on edge... I get that..."
    scene a1129 with dssa
    mi "Imagine lying in a bathtub with a guy you find quite handsome... I can feel him between my butt cheeks..."
    mi "His breath on my neck... His hands on my tits."
    if Mila_Bath_Pussy is True:
        mi "*Whisper* Two fingers inside my pussy."
    scene a1130 with dssr
    "Her voice grows quieter and more sensual with every word she says..."
    scene a1131 with dssa
    mi "*Sensual whisper* I know what being on edge feels like..."
    scene a1134 with dssr
    "You grab her breast, and with a confident squeeze, you elicit a moan out of her."
    "Her pelvis moves in a gentle, circular motion."
    scene a1135 with dssr
    "You place your hand on her upper chest and gently still her."
    d "I think it's time I tell you... something."
    scene a1136 with dssr
    mi "Okay."
    scene a1137 with dssa
    d "The aftermath of the events surrounding Summer led to... led to a blockade in my mind."
    d "I can't get an erection at the moment."
    scene a1139 with dssa
    mi "Oh."
    scene a1141a with dssa
    pause
    scene a1142a with dssa
    mi "Okay... Yeah. That's okay."
    mi "I knew something was up and... I did have a notion."
    scene a1143a with dssa
    pause
    scene a1144a with dssa
    mi "Soo uhh... Does this here do anything for you?"
    scene a1145 with dssa
    d "It does."
    d "I won't deny that I might be a little numb on the feelings side... But I like the warmth your body radiates."
    scene a1146 with dssa
    d "And I like how much you enjoy it."
    scene a1147 with dssa
    mi "And boy do I enjoy this."
    scene a1148 with dssa
    pause
    scene a1149 with dssa
    mi "At least, I have something to look forward to."
    scene a1150 with dssr
    mi "I assume this problem of yours can be fixed?"
    d "I assume, yes."
    scene a1153 with vpunch
    mi "I'll help you!"
    scene a1154 with dssa
    d "It does sometimes work for a short moment."
    scene a1153 with dssa
    mi "What makes it work?"
    d "(I shouldn't mention the Cheeto... Or any other girl in general.)"
    scene a1154 with dssa
    d "I can't really pin it down yet. Maybe trust?"
    scene a1153 with dssa
    mi "That's a good sign!"
    scene a1155 with dssa
    mi "Well... let's find out how I can be of service..."
    stop music fadeout 3
    scene black with Dissolve(2)
    with Pause(.5)
    play ambient "Music/Sfx/Ambient_Night_Suburban2.ogg"
    scene a1621 with dssb
    pause
    scene a1622 with dssa
    pause 
    scene a1623 with dssa
    mi "My stomach is so lean."
    scene a1624 with dssa
    d "Are you on a diet?"
    scene a1625 with dssa
    mi "No, I don't follow a diet. I have always been mindful about what I eat." 
    scene a1626 with dssr
    mi "Truth be told, sometimes we didn't have much food. I've always been good at ignoring hunger or just not eating too much in general." 
    scene a1628 with dssa
    d "You look good, though."
    scene a1629 with dssa
    mi "Thank you." 
    scene a1630 with dssr
    pause 
    scene a1631 with dssa
    mi "I love my tits."
    menu:
        "I love them, too.":
            scene a1632 with dssa
            mi "That's what I wanted to hear."
        "Don't say it.":
            pass  
    scene a1633 with dssa
    d "You know... thinking back to what you said about your mom... you said you'd tell me something as soon as we knew each other a little better."
    scene a1634 with dssa
    mi "Right..."
    mi "I mean, I told you most of it earlier..."
    scene a1636 with dssa
    d "The way you were talking I assumed you were very anti-sex."
    scene a1635 with dssa
    mi "I've been on both sides of the spectrum."
    scene a1637 with dssa
    mi "Not talking about the spectrum Bella is at."
    scene a1638 with dssa
    d "Oh wow!"
    scene a1639 with dssa
    mi "I already feel bad! I'll apologize to her in my sleep."
    scene a1640 with dssa
    d "Don't. She deserves it. I'll steal that one, though."
    scene a1641 with dssr
    mi "Okay... see... it has to do with my past insecurities. My Mom isn't a bad person, but she really confused me as a child."
    mi "I always saw my Mama dress up sexy. I didn't know it was sexy at that time. I was a child."
    mi "Then, at some point later, after my dad went to prison and eventually came back, everything changed."
    scene a1642 with dssa
    mi "I was about ten, maybe eleven at that time and suddenly everything sexy was bad."
    mi "They threw away totally normal clothes, and I got dressed in clothes that made me look 50kg overweight."
    scene a1643 with dssa
    mi "I looked like Robby, the chunky elf."
    mi "By the time I was half-way through puberty, I thought I was disgusting."
    scene a1644 with dssa
    mi "Like... I had some- I still partially feel inadequate."
    scene a1645 with dssa
    d "I bet Bella isn't helping."
    scene a1646 with dssr
    "She chuffs."
    scene a1647 with dssa
    mi "Well, my Mom then started working as an escort, and sexy became good again."
    scene a1648 with dssr
    mi "Just not on me."
    mi "Mentally, I still believed sexy was bad."
    scene a1649 with dssa
    mi "It's more or less just what I already told you earlier." 
    mi "But of course, there's more than one story to it... One day, a friend and I were sitting on a fence watching cute horsies."
    mi "I slipped and fell in the mud."
    scene a1648 with dssa
    mi "She gave me a top of hers and we met with a group of friends, and for the first time ever, people complimented me."
    mi "My friend noticed it, and a few days later, she came by and gave me a few outfits of hers."
    mi "They didn't fit me, I had much bigger boobs."
    mi "But by then I had already started saving money, and blew it all on new clothes."
    scene a1650 with dssa
    mi "I'm not going to lie, it changed my life. This was the first time I felt good about myself."
    mi "The confidence I got from all these positive comments and looks... It... changed everything."
    scene a1651 with dssa
    pause 
    scene a1652 with dssa
    mi "By that time I was around 16... Now, I may have dressed sexier, but I still had a deeply ingrained belief that sex was the root of all evil."
    mi "Sex made my Mom drink too much. It was the reason she cried at night. I always thought she wanted to protect me from becoming her."
    mi "And the only correlation I could make was 'Sex' and 'Bad'." 
    scene a1653 with dssa
    mi "I guess it's still somewhere in me. I'm still not entirely sure who I am."
    scene a1654 with dssr
    mi "I guess college is a good place to find myself... or to get lost."
    mi "As I told you at the park... I wanted to prove something to myself by not sleeping with anyone for a while."
    scene a1655 with dssr
    d "Were you successful?"
    scene a1656 with dssa
    mi "Of course." 
    scene a1655 with dssa
    d "I get the feeling you would've slept with me today."
    scene a1656 with dssa
    mi "I'm not celibate anymore."
    scene a1657 with dssa
    mi "I lied when I said I was successful."
    scene a1658 with dssa
    mi "I had planned to do it for six months, but would've totally done you today... Three months later." 
    scene a1659 with dssa
    mi "Anyways... What I wanted to say is... I'm not sure if I'm a nympho. I think I get horny way too easily."
    mi "I take the bus? Wet. I drink a single drop of alcohol? Wet."
    scene a1660 with dssr
    mi "I also experienced trouble when studying... About fifteen to twenty minutes in, I would get really into the mood for anal."
    mi "*Chuckles* I don't know what's wrong with me."
    scene a1661 with dssr
    d "Maybe you should try a plug? Like the ones Maja had?" #ani
    mi "I did."
    mi "It made it much worse. The plug only made me crave something bigger." 
    mi "The good thing is, I'll be moving out soon, and the first thing I'll do after buying a bed big enough to stash all my cuddly toys is to get myself some sex toys."
    mi "Unless... you want to be my sex toy."
    scene a1662 with dssr
    pause
    scene a1663 with dssa
    pause
    scene a1664 with dssa
    pause 
    scene a1665 with dssa
    mi "Don't worry, I won't push you..."
    play sound "Music/Sfx/Slap.ogg"
    scene a1666 with vpunch
    mi "Too much!"
    scene a1668 with dssr
    d "I appreciate that."
    scene a1667 with dssa
    mi "You were open with me, and I wanted to be open with you."
    stop ambient fadeout 3
    scene black with Dissolve(2)
    $ play_playlist(playlist_Romance)
    with Pause(.5)
    scene a1669 with dssb
    pause 
    scene a1670 with dssa
    mi "How's your project coming along?"
    d "We're slacking a little."
    scene a1671 with dssa
    mi "What topic did you choose to write about?"
    d "Fungoids and their uses."
    scene a1672 with dssr
    mi "Seeexy."
    scene a1673 with dssa
    d "We came up with the headline 'Fungis Declare: We Are Not Just Pizza Toppings.'"
    scene a1674 with dssa
    "Mila laughs."
    scene a1675 with dssa
    d "What are you and Vic writing about?"
    scene a1676 with dssr
    mi "We're working on a theory to enhance tree growth and CO2 absorption by mostly using unethical methods."
    d "Interesting."
    scene a1678 with dssa
    mi "I care about the environment. A lot even."
    scene a1679 with dssr
    mi "So much that I'd use the blood of my enemies to fertilize the fields."
    scene a1680 with dssa
    mi "If I had enemies."
    scene a1681 with dssa
    d "Bella?"
    scene a1682 with dssa
    mi "She's not my enemy. She's just insecure and afraid of becoming a victim again."
    scene a1683 with dssa
    d "Do you want to work in an environment-related field?"
    scene a1684 with dssa
    mi "No, no. You know I'm studying finance, but I have always wanted my own big garden."
    mi "When I was little, I had this small cactus."
    scene a1685 with dssa
    mi "*sighs* God, did I love it."
    scene a1686 with dssa
    mi "I saw it grow, you know?"
    mi "It was insane! It kept growing so much every week."
    scene a1687 with dssa
    mi "...And then my stepfather threw it away."
    mi "Awesome."
    scene a1688 with dssa
    d "Ohh... Not the little cactus."
    $ MilaCactus = True
    scene a1689 with dssa
    mi "I mourned for much longer than I'd like to admit..."
    scene a1690 with dssa
    mi "And seeing how I feel right now, I'm still not over it."
    scene a1691 with dssa
    d "(Maybe I should keep an eye out for a little cactus to give Mila when we all eventually move into the student house.)"
    scene a1690 with dssa
    mi "Sorry. I should note down not to talk about my cactus trauma. Mood killer."
    scene a1692 with dssa
    d "Not at all. It's cute."
    scene a1693 with dssr
    mi "Did you have something as a child that you were really attached to?"
    d "(Besides Summer?)"
    scene a1694 with dssa
    d "Yeah, Moogle. A cat."
    scene a1693 with dssa
    mi "He sounds cute."
    scene a1694 with dssa
    d "He was the biggest asshole I've ever met."
    scene a1695 with dssr
    pause
    scene a1696 with dssa
    d "But he was a good boy."
    scene a1697 with dssa
    mi "Did he pass away?"
    scene a1696 with dssa
    d "I'm sure he did by now... But... He had no home, and when we left town in somewhat of a hurry... He wasn't on my mind."
    scene a1697 with dssa
    mi "You can't blame yourself for that."
    scene a1698 with dssr
    d "I know. Still, he was part of our little gang."
    mi "Who was in your gang?"
    d "Nami on and off, Summer, I, Ted and I guess Ely..."
    mi "Who was Ted?"
    scene a1699 with dssa
    d "Ted was a good friend."
    d "It's weird if you think about it... From seeing each other every day to never again."
    mi "You could always reach out? Have you tried it?"
    scene a1700 with dssr
    d "Mila? Think about how I spent the past few years."
    scene a1701 with dssa
    mi "Got it."
    mi "But life's too short to let pride get in the way."
    scene a1702 with dssa
    d "And Ely you've seen before."
    d "Ely is Elsa."
    scene a1703 with dssa
    mi "The supermodel?"
    scene a1702 with dssa
    d "Mhm."
    scene a1705 with dssa
    d "She's Summer's cousin."
    scene a1704 with dssa
    mi "Oh wow. Oh-..."
    scene a1706 with dssa
    mi "How was she when she was little?"
    scene a1707 with dssa
    d "Kind of annoying. She had terrible parents."
    d "She had a meal plan and had to go through weekly weighing."
    scene a1708 with dssa
    mi "You're kidding me?"
    scene a1709 with dssr
    d "Nope. She also had that tick where if you made barfing- gagging noises, you know?"
    d "It would trigger a reflex and she'd start gagging. That was pretty funny."
    scene a1710 with dssa
    d "But if you did it too many times she'd actually barf."
    scene a1711 with dssa
    mi "*Laughs* Poor girl!"
    play sound "Music/Sfx/Slap.ogg"
    scene a1712 with vpunch
    mi "That's so mean!"
    scene a1713 with dssa
    mi "Do you want to get in contact with her again?"
    scene a1714 with dssa
    pause
    scene a1715 with dssa
    d "Nah."
    scene a1716 with dssa
    mi "I know it's not my place, but it might help you deal with the past."
    stop music fadeout 5
    scene a1717 with dssr
    pause 
    mi "Let's go to bed..."
    scene black with Dissolve(1)
    with Pause(.3)
    $ renpy.movie_cutscene("images/Animations/CH1-3/CH1_Red_Kite.webm", stop_music=False)
    $ persistent.RedVelvet = True
    jump ZaraTrain5x5








label NamiNight5x5:
    $ play_playlist(playlist_Smooth)
    $ CheetoBath = True
    scene a522 with vpunch
    n "Look who it is..."
    n "You think I'm stupid, huh? You think I didn't see the look, huuuuh?!"
    scene a523 with dssa
    n "I know exactly what is about to happen... You do it all the time... with everyone."
    scene a524 with dssr
    n "*Funny voice* Let's start daaating! I'm so innnnnnn- aaaaaaand-"
    scene a526 with dssa
    n "-he's gone."
    scene a527 with dssr
    if MilaDate is True:
        n "I'm taking control before I end up like Mila."
    elif VicDate is True:
        n "I'm taking control before I end up like Vic."
    elif BellaNonExclusive5x0 is True:
        n "I'm taking control before I end up like Bella."
    else:
        n "I'm taking control before I end up on the sidelines."
    scene a528 with dssa
    n "I knew you'd pull back, time would pass and nothing between us would happen."
    scene a529 with vpunch
    n "I'm not falling for this! You forgot who's in front of you! BIG WIGGLY Y'all!"
    d "(...Shit.)"
    scene a530 with dssa
    d "Put your clothes back on and you can sleep in my bed."
    scene a531 with dssa
    n "No, no."
    scene a532 with dssr
    n "Tonight... We take clothes off."
    n "Let's take a bath together."
    scene a533 with dssa
    d "No."
    scene a534 with dssa
    n "You're not getting out of this."
    scene a535 with dssa
    d "Cheeto. Anyone could come in at any second."
    d "Mila's probably wondering where you are. If we do this we need to be cauti-"
    scene a536 with dssr
    n "We don't and Mila's out cold."
    n "And I already checked. We can lock the door."
    scene a537 with dssa
    d "Nami-"
    scene a538 with dssa
    n "No matter what you'll say, I don't care."
    scene a539 with dssa
    n "Our hot bodies will enter the even hotter bathwater together or this is over."
    scene a540 with dssa
    d "*Sigh*"
    scene a541 with dssa
    pause
    scene a542 with dssa
    n "That might take a few minutes."
    scene a543 with dssa
    n "Lemme turn the water on. Then you can continue playing with my tits... or ass."
    scene a544 with dssr
    pause
    scene a546 with dssr
    pause
    scene a545 with dssr
    n "Somebody's trying to earn some bonus points."
    scene a548 with dssr
    pause
    scene a549 with dssa
    pause
    scene a550 with dssa
    "You position the Cheeto in front of you and hold her by the ass."
    scene a551 with dssa
    n "I've seen your dick so many times before. I don't think you've ever seen my pussy, huh?"
    scene a552 with dssr
    "She takes a seat."
    scene a553 with dssa
    d "Nope."
    d "The difference is that you try to get a peek."
    d "I, on the other hand, try to avoid it."
    scene a554 with dssa
    n "You just can't handle my pussy, pussy!"
    pause
    scene a555 with dssr
    n "You've gotta get comfortable with my body if you want this to work."
    scene a556 with dssa
    d "It's not your fault."
    scene a555 with dssa
    n "It's just hard for me not to take it personally."
    scene a556 with dssa
    d "I know. I'm sorry but-"
    scene a555 with dssa
    n "No but. The only butt you need to care about is soon to be in this tub!"
    scene a557 with dssr
    "You guide her into a tight embrace."
    scene a558 with dssr
    pause
    scene a559 with dssr
    n "Let's get in."
    scene a560 with dssr
    pause
    scene a561 with dssr
    pause
    play sound "Music/Sfx/Searing.ogg"
    scene a563 with dssa
    with Pause(.5)
    scene a564 with vpunch
    d "Wow! Dude! That's so hot!"
    scene a565 with dssa
    n "Really?"
    play sound "Music/Sfx/Searing.ogg"
    scene a567 with dssa
    with Pause(.5)
    scene a566 with vpunch
    n "Argghh!"
    scene a568 with dssa
    pause
    scene a569 with dssa
    d "I think you have to let in cold water too."
    scene a570 with dssa
    pause
    scene a571 with dssr
    pause
    scene a574 with dssa
    pause
    scene a575 with dssr
    d "Ready to be boiled alive?"
    scene a576 with dssa
    n "Always."
    n "Get in first, I want to sit on your lap."
    scene a577 with dssr
    pause
    scene a578 with dssa
    d "Don't step on me."
    scene a579 with dssa
    pause
    scene a580 with dssa
    n "...That's so nice."
    scene a581 with dssr
    pause
    scene a582 with dssa
    d "...It's so hot in here... Uncomfortably hot."
    d "*Sigh*"
    d "Let's get out."
    scene a584 with dssa
    n "No! We've been in here for like a minute!"
    scene a583 with dssa
    n "Just breathe and relax."
    n "You can distract yourself with my tiddies if you want."
    scene a585 with dssa
    pause
    scene a586 with dssa
    d "...Still a little awkward."
    scene a587 with dssa
    n "There's nothing awkward about this... Trust me."
    scene a588 with dssa
    pause
    scene a589 with dssa
    n "I was asked to join a sorority."
    scene a588 with dssa
    d "Will you?"
    scene a589 with dssa
    n "I don't know. I'll take a look at it."
    scene a588 with dssa
    d "Why did they ask you? And who?"
    scene a590 with dssa
    n "Some girls, and I don't know why they asked me."
    n "Not just me, though."
    scene a591 with dssa
    d "Who else?"
    scene a590 with dssa
    n "Mila and Nadia."
    n "Mila declined, though."
    scene a592 with dssa
    n "But I like the idea of a sisterhood... I always wanted a sis-..."
    scene a593 with dssa
    n "We'll see, we'll see... Maybe they all suck."
    scene a594 with dssa
    d "Good luck with your pledge then."
    scene a595 with dssa
    "You move your hand across her belly..."
    scene a596 with dssr
    n "...Wanna play a game?"
    scene a597 with dssa
    d "No."
    scene a598 with dssa
    n "Would you rather do Victoria or Nia?"
    menu:
        "Victoria.":
            scene a599 with dssa
            n "So the dirty one of these two... I see."
        "Nia.":
            scene a599 with dssa
            n "I bet she sucks dick like an old English cement mixer."
            "You let out a little laugh."
    scene a600 with dssa
    n "Bella or me?"
    scene a602 with dssa
    d "Fuck off. I'm not touching that with a fifteen-meter-long pole."
    scene a604 with dssr
    n "Noji or Vanessa?"
    d "What kind of question is that?"
    scene a605 with dssa
    n "Would you rather sleep with Noji or Vanessa?"
    d "I'm not answering that."
    scene a606 with vpunch
    n "Damn! Really? Noji?!"
    scene a607 with dssa
    d "Shut up."
    scene a608 with dssa
    n "Noji or me?"
    scene a609 with dssa
    d "Definitely Noji."
    scene a610 with vpunch
    n "YO!?"
    scene a611 with dssa
    pause
    scene a612 with dssa
    pause
    scene a1718 with dssa
    n "Do you wanna play would you rather?"
    scene a1719 with dssa
    d "No way."
    d "I will never play that game with you again."
    scene a1720 with dssa
    n "You don't have the stomach."
    scene a1721 with dssa
    d "Eventually I might, but you always go too far."
    scene a1720 with dssa
    n "You're too weak."
    scene a1722 with dssa
    n "I have one simple, innocent would-you-rather question."
    scene a1723 with dssa
    d "..."
    scene a1724 with dssa
    n "If you had to choose... Would you rather fuck me in the ass or pussy?"
    scene a1725 with dssa
    d "..."
    menu:
        "Pussy.":
            scene a1726 with vpunch
            n "Do you want to get me pregnant?"
            scene a1727 with dssa
            d "I don't."
            scene a1729 with dssa
            n "Man... Imagine we did it and I ended up with a round belly."
            d "Can we not imagine that, please?"
            scene a1730 with dssr
            n "I should really get the pill."
            scene a1731 with dssa
            d "Sounds like a smart move."
            scene a1732 with dssa 
            n "Oh yeaaah, that's what I wanna hear."
        "Ass.":
            scene a1728 with vpunch
            n "Yo!"
            scene a1729 with dssa
            n "I've gotta... I've gotta train before that." 
            scene a1730 with dssr
            n "We should start experimenting."
            n "I can think of a lot of things."
            scene a1731 with dssa
            d "Thanks to your loose mouth and weird stories, I can imagine quite a bit too."
            scene a1732 with dssa
            n "Hehe."
    scene a1733 with dssr
    d "Wanna get out?"
    scene a1734 with dssa
    n "I do."
    scene a1735 with dssr
    pause
    play sound "Music/Sfx/Slap.ogg"
    scene a1736 with vpunch
    n "Oops!"
    scene a1737 with dssa
    n "I slipped! Sorry!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene a1738 with dssb
    pause 
    scene a1739 with dssr 
    pause 
    scene a1740 with dssa
    pause 
    scene a1741 with dssa
    "All of a sudden you notice a shift in the room. The previously clear sky is now blocked by dark clouds."
    scene a1742 with dssa
    d "Hey."
    scene a1743 with dssr
    n "I think you were right. Taking a bath together was fun but sharing a bed is a little too much."
    scene a1744 with dssa
    d "You'll sleep here."
    scene a1745 with dssa
    n "What?"
    scene a1744 with dssa
    d "You will sleep here."
    scene a1745 with dssa
    n "Dude, are you aware of-"
    scene a1746 with dssa
    d "Nami. You'll stay."
    scene a1747 with dssr
    pause
    scene a1748 with dssa
    n "What if I don't want to?"
    scene a1749 with dssa
    d "We've been through this before, and I've warned you."
    scene a1750 with dssa
    d "I know you can feel it and I know it's hard to fight against... But if you want this to work, you'll need to fight it."
    scene a1751 with dssr
    d "(It's not the first time she's behaved like this... Back in the day, she used to do this a lot... One second she's nice to me, and one second later she's totally different.)"
    d "(Over time I learned how to read her. I know immediately when her whole demeanor shifts.)"
    scene a1752 with dssr
    d "(But it hasn't been happening as often anymore... And I fear us getting closer will trigger this again.)"
    scene a1753 with dssr
    pause 
    scene a1754 with dssa
    pause 
    scene a1755 with dssr
    "You stand there for almost two full minutes, gently rubbing her arms until every last cloud has vanished."
    scene a1756 with dssa
    n "I'll sleep like this."
    scene a1757 with dssa
    n "And don't worry, I'm not seducing you into anything awesome tonight."
    scene a1758 with dssr
    n "But... I want us to get more comfortable."
    scene a1759 with dssa
    d "I get it, Nami. And you were right... I would've totally played the time game."
    scene a1760 with dssr
    n "That's what happens to the villains if they don't take Big Wiggly's sharp mind into account."
    scene a1761 with dssa
    pause 
    scene a1762 with dssr
    pause 
    scene a1763 with dssa
    "You guide her head upwards, and with anticipation, she awaits your next move..."
    scene a1764 with dssa
    d "*Whispers* Big Wiggly is the worst name you've ever given yourself."
    scene a1765 with vpunch
    "She gasps!"
    scene a1766 with dssa
    n "Worse than Salami-Nami?"
    scene a1767 with dssa
    d "Yeah."
    scene a1766 with dssa
    n "Even worse than the Red-Plague?"
    scene a1767 with dssa
    d "Yes, even worse than the name you've given yourself during flu season."
    scene a1768 with dssa
    n "This will not stay unpunished!"
    scene a1769 with vpunch
    pause 
    scene a1770 with vpunch
    n "Let me put a finger up your ass!"
    scene a1771 with vpunch
    "You two wrestle for a short while."
    scene a1772 with vpunch
    pause 
    scene a1773 with dssa 
    pause 
    scene a1774 with dssa
    d "It feels like you peed yourself."
    scene a1775 with dssa
    n "Naah, that's just how wet I get."
    scene a1776 with dssr
    d "Okay. One rule."
    scene a1777 with dssa
    d "You'll not sleep on top of me."
    scene a1778 with dssa
    n "I'm so aroused, I wouldn't even care if Noji saw us with your dick balls deep in my pussy."
    n "Hell, they could all watch."
    scene a1779 with dssa
    d "And that's why I'm in charge."
    scene a1780 with dssr
    d "(Controlling this insane Cheeto is going to be a challenge.)"
    scene a1781 with dssa
    n "How about this..."
    scene a1782 with dssa
    d "No."
    scene a1783 with dssa
    n "You don't even know what I was about to say!"
    scene a1784 with dssa
    d "It's something insane and stupid."
    scene a1785 with dssa
    n "How about we sleep together... Nude."
    scene a1786 with dssa
    n "That's it! Nothing else!"
    scene a1787 with vpunch
    n "We can have a two bread roll distance between us."
    scene a1788 with dssa
    d "What's one roll of distance?"
    scene a1789 with dssa
    n "About this..."
    scene a1790 with dssa
    d "Fine."
    scene a1791 with dssa
    d "You don't flop onto me!"
    scene a1792 with dssa
    n "I promise!"
    scene a1793 with dssr
    pause
    scene a1794 with dssa
    n "...Do you feel that?"
    scene a1795 with dssa
    d "I don't feel some gravitational pull between us."
    scene a1796 with dssr
    n "How did you know I was going to pull that one?"
    scene a1797 with dssa
    d "I had a hunch."
    scene a1796 with dssa
    n "Scary..."
    scene a1798 with dssa
    d "Good night, Cheeto."
    scene a1799 with dssa
    n "Good night."
    scene a1800 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    jump NamiMorningTraining


label NamiMorningTraining: # MC Room  &  #8. Zara Sport Morning
    if SoloStartS2 is False:
        scene a1801 with dssb
    else:
        scene a1801a with dssb
    pause
    scene a1802 with dssr
    d "(I'm so thirsty.)"
    scene a1803 with dssr
    d "(3:35 in the morning...)"
    d "(I need something to drink.)"
    if SoloStartS2 is False:
        scene a1804 with dssr
    else:
        scene a1804a with dssb
    pause
    scene a1805 with dssr
    pause
    scene a1806 with dssr
    pause
    scene a1807 with dssr
    pause 
    scene a1808 with dssr
    pause 
    scene a1809 with dssr
    pause 
    scene a1810 with dssr
    d "(Why is she awake?)"
    scene a1811 with dssr
    pause 
    scene a1812 with dssr
    pause 
    play sound "Music/Sfx/WA_Thud.ogg"
    scene a1813 with vpunch #sfx 
    pause 
    $ play_playlist(playlist_Smooth)
    scene a1814 with dssa 
    "Zara bursts out laughing."
    scene a1815 with dssa 
    pause 
    play sound "Music/Sfx/GlassDoor_Slide.ogg"
    scene a1816 with dssa 
    za "*laughs* Are you okay?"
    scene a1817 with dssr 
    d "Yeah."
    d "What are you doing awake?"
    scene a1818 with dssa 
    za "I always get up at 3:30."
    za "I was about to come and wake you."
    scene a1819 with dssa 
    "You raise a brow."
    scene a1820 with dssa 
    za "What? We need to train!"
    scene a1821 with dssa 
    d "I'm so tired."
    scene a1822 with dssr
    d "I'm going back to bed."
    scene a1823 with vpunch
    za "No! Come on! It's gonna be fun!"
    scene a1824 with dssa
    d "Do you have any idea how tired I am?"
    scene a1825 with vpunch
    za "Good! It's an extreme hit against the comfort zone!"
    scene a1826 with dssa
    d "*Sigh*"
    scene a1827 with dssa
    d "...That's a good point."
    scene a1828 with dssa
    d "But not for more than an hour."
    scene a1829 with dssa
    za "Yay! Deal!"
    scene a1830 with dssa
    za "I'll get my shaker and you go change!"
    scene black with Dissolve(2)
    with Pause(.5)
    jump ZaraGym5x5






label ZaraTrain5x5: #7. Zara Sport Morning
    scene sc1 with dssb
    pause
    scene sc2 with dssr
    pause
    "Pss pss."
    scene sc3 with dssa
    play ambient "Music/Sfx/Ambient_Night_Suburban.ogg"
    "Pss pss psss psss"
    scene sc4 with dssa
    za "Pss pss-"
    scene sc5 with dssa
    d "*Whisper* I'm not a cat."
    scene sc6 with dssr
    pause
    scene sc7 with dssa
    za "*Whisper* Come."
    scene sc8 with dssr
    pause
    scene sc9 with dssa
    pause
    scene sc10 with dssr
    "You follow Zara into the dressing room."
    scene sc11 with dssa
    d "What is it?"
    $ play_playlist(playlist_Happy)
    scene sc12 with dssr
    stop ambient fadeout 3
    za "Let's train."
    scene sc13 with dssr
    d "...You woke me up... to train... now?"
    scene sc14 with dssa
    za "Yes."
    scene sc13 with dssa
    d "While I'm having a girl over..."
    scene sc14 with dssa
    za "Yes, she'll appreciate a toned body."
    scene sc15 with dssa
    d "I'm going back to bed."
    play sound "Music/Sfx/Punch.ogg"
    scene sc16 with vpunch
    za "No! Come on! It's gonna be fun!"
    scene sc17 with dssa
    d "Do you have any idea how tired I am?"
    scene sc18 with dssa
    za "Good! It's an extreme hit against the comfort zone!"
    scene sc19 with dssa
    d "*Sigh*"
    scene sc20 with dssa
    d "...That's a good argument."
    scene sc21 with dssr
    d "But not for more than an hour."
    scene sc22 with dssa
    za "Deal!"
    scene sc23 with dssa
    d "What time is it?"
    scene sc22 with dssa
    za "It's 4:00 AM."
    scene sc24 with dssa
    d "Do you always train at this hour?"
    scene sc25 with dssa
    za "Yes. I get up at 3:30am."
    za "But I also go to bed at like 8pm."
    scene sc26 with dssa
    za "Come. Clothes are at the gym."
    scene black with Dissolve(2)
    with Pause(.5)
    jump ZaraGym5x5

label ZaraGym5x5:
    scene sc27 with dssr
    pause
    scene sc28 with dssa
    d "I'll only do ten minutes of cardio."
    scene sc29 with dssr
    za "Do you struggle to get enough calories in?"
    scene sc30 with dssa
    d "I don't know."
    d "I never gained weight."
    scene sc31 with dssa
    za "Same here."
    scene sc32 with dssa
    za "Fast metabolism-five!"
    scene sc33 with dssr
    pause
    play sound "Music/Sfx/Slap.ogg"
    scene sc34 with vpunch
    pause
    scene sc35 with dssa
    za "Let's start."
    scene sc36 with dssr
    pause
    d "What the fuck is that?"
    scene sc37 with dssr
    za "An artificial sun."
    za "Get a lot of light into your eyes early in the morning, right after waking up, to increase alertness and energy."
    scene sc38 with dssa
    d "It burns your eyes!"
    scene sc37 with dssa
    za "Your eyes will adjust rather quickly. It doesn't spread that much light. It's just really bright in the center."
    scene sc39 with dssa
    za "We'll start with fast walking."
    if MilaSleep5x0 is True:
        scene sc79 with dssr
        za "Mad respect, though."
        za "For doing Mila."
        scene sc80 with dssa
        pause
        scene sc81 with dssa
        za "I know a lot of people who'd give their left lung for a night with her."
        scene sc82 with dssa
        d "Their left lung?"
        scene sc81 with dssa
        za "Yes? Imagine just having one lung! Your endurance would be terrible!"
    if BellaKiss3x5 is True:
        $ ZaAlleFra5x5 = True
        scene sc79 with dssr
        za "How do you do that?"
        za "How do you get all these girls?"
        scene sc80 with dssa
        d "What girls?"
        scene sc83 with dssr
        za "Bella, Mila, Nia, and I bet there are even more."
        scene sc84 with dssa
        d "I don't do anything."
        scene sc83 with dssa
        za "All I hear from people is what a jerk you are."
        scene sc84 with dssa
        pause
        scene sc85 with dssa
        za "I mean, I kinda get it..."
        "You raise a brow."
        scene sc86 with dssr
        za "You have that weird attitude. It's like you don't give a shit if someone has a vagina."
        za "You don't have the desperate stench many guys have. Girls drop their guard around you."
        scene sc88 with dssa
        za "But I heard some girl call you misogynistic."
        scene sc87 with dssa
        d "That's bullshit."
        d "I hate all genders the same."
        scene sc89 with dssa
        za "You also don't seem too horny."
        scene sc90 with dssa
        d "'Too horny?'"
        d "When did I ever act horny?"
        scene sc91 with dssa
        za "Oh, I've seen the looks..."
        scene sc92 with dssa
        d "..."
        if BellaKiss3x5 is True:
            scene sc93 with dssa
            za "Didn't you and Bella have sex in the locker room after we cuffed you?"
            scene a1831 with dssr
            za "*Smirks* You're welcome, by the way."
            scene a1832 with dssr
            d "We didn't."
        else:
            scene a1832 with dssr
            pause
    else:
        scene sc91 with dssa
        za "Say... Didn't you nude-wrestle with Nora and Kate?"
        scene sc92 with dssa
        d "No?"
        scene sc91 with dssa
        za "Some girl told me that."
        scene sc92 with dssa
        d "...Are these people straight up retarded?"
        d "Why does everything end up in a rumor?"
        if BellaKiss3x5 is True:
            scene sc93 with dssa
            za "So it's safe to assume that you and Bella having sex in the locker room is also not true?"
            scene a1831 with dssr
            za "*Smirks* You're welcome, by the way."
            scene a1832 with dssr
            pause
        else:
            scene a1832 with dssr
            pause 
    if RoRum is True:
        $ ZaraPanicAttacks5x5 = True
        scene a1833 with dssa
        za "What about you and Robin-"
        scene a1834 with dssa
        d "Oh my god- Robin and I didn't do shit in that damn stall."
        scene a1833 with dssa
        za "Why were you even in there?"
        scene a1834 with dssa
        d "We hid from a few people after I had a panic attack."
        scene a1835 with dssa
        za "Oh! That's what happened on the first day in class?"
        scene a1836 with dssa
        d "Yeah."
        scene a1838 with dssa
        za "I remember my panic attacks."
        scene a1837 with dssa
        d "...What caused them?"
        scene a1838 with dssa
        za "Pressure."
        za "If I didn't bring home an A, I was in for a rough time."
        scene a1839 with vpunch
        play sound "Music/Sfx/Thud4.ogg"
        za "'Why can't you be more like Vanessa?!'"
        scene a1840 with dssa
        d "*Cough* I assume it wasn't Nick."
        scene a1841 with dssa
        za "It was my Mother."
        za "Dad was always supportive."
        scene a1842 with dssa
        d "This explains your desperate need to always win."
        scene a1843 with dssr
        za "Yeah, I lost some of my marbles."
        za "I'm trying so hard not to always be competitive."
        scene a1844 with dssa
        za "When I have a bad week, I can get so bad that I want to beat Nadia at her stupid games."
        za "Which is why I don't play with her anymore..."
        scene a1845 with dssa
        pause
        scene a1846 with dssa
        za "I made her cry once."
        scene a1847 with dssa
        d "She appears really invested in these games."
        scene a1846 with dssa
        za "...That she is."
        scene a1848 with dssa
    else:
        scene a1848 with dssr
    za "But don't take the rumors personally."
    scene a1849 with dssr
    za "There's a rumor about me that I'm on PEDs."
    scene a1850 with dssa
    d "Steroids?"
    scene a1849 with dssa
    za "And similar stuff."
    scene a1850 with dssa
    d "Are you?"
    scene a1849 with dssa
    za "No."
    scene a1851 with dssa
    za "These muppets can't imagine what dedication and willpower can do."
    scene a1852 with dssa
    d "How many guys in the first team are on PEDs?"
    scene a1851 with dssa
    za "Probably 80 percent?"
    za "You don't play at this level and party every weekend without at least a little bit of a boost."
    scene a1852 with dssa
    pause
    scene a1853 with dssa
    za "You're on something, right?"
    scene a1854 with dssa
    d "What? No?"
    scene a1853 with dssa
    za "Duuude, you've been building muscle like crazy."
    scene a1854 with dssa
    d "It's always been like that."
    scene a1855 with dssr
    d "I'm not on something."
    menu:
        "...Right now.":
            $ PEDs5x5 = True
            scene a1856 with dssa
            "Zara squints her eyes."
            za "Would you consider it?"
            scene a1857 with dssa
            d "If I make the first team, I will have one hell of a time to get my cardio up without spending hours in the gym every day."
            d "Who knows."
            scene a1860 with dssr
            za "Don't take the wrong ones or that thing in your pants won't get up anymore."
            scene a1858 with dssr
            d "(At least I won't have to worry about that.)"
        "And never will.":
            $ Natural5x5 = True
            scene a1856 with dssa
            za "Good choice."
            scene a1860 with dssa
            za "But we'll talk about it again when you play with the big boys."
            scene a1858 with dssr
            za "And remember, you don't need to lie to me then."
    scene a1859 with dssr
    d "Enough cardio."
    scene a1861 with dssr
    d "I'll do some other stuff."
    scene a1862 with dssa
    za "I'll run for another 20 minutes."
    scene Benchi with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene a1865 with dssr
    pause
    scene a1866 with vpunch
    play sound "Music/Sfx/Punch.ogg"
    za "That's enough pause!"
    scene TUT
    za "Time under tension! No more than 30 seconds rest between sets!"
    scene a1869 with dssa
    d "Do your cardio and leave me alone!"
    scene a1870 with dssr
    pause
    scene a1871 with dssr
    pause 
    scene a1872 with dssr
    d "(It's insane how strongly your immediate environment affects you.)"
    d "(Living with Zara is certainly kind of inspiring when it comes to training.)"
    d "(While being with Nami made me kinda lazy... Maybe the Cheeto will benefit from this new environment, too.)"
    scene a1873 with dssa
    va "Good morning."
    scene a1874 with dssr
    d "Morning."
    scene a1875 with dssa
    va "I see you've fallen victim to the insane."
    scene a1876 with dssa
    d "Yeah."
    scene a1875 with dssa
    va "You can just tell her no."
    scene a1877 with dssr
    d "Ahhh, it's not so bad."
    d "I wanted to train with her."
    scene a1878 with dssa
    d "She... She inspires me."
    scene a1879 with vpunch
    za "DON'T DISTRACT HIM FROM HIS TRAINING!"
    scene a1880 with dssa
    va "Silence."
    scene a1881 with dssa
    "Vanessa smiles at you and goes on her way."
    scene a1882 with dssa
    pause
    scene a1883 with dssa
    za "I'm telling you... Women are your downfall."
    scene a1884 with dssa
    za "Spouses are responsible for people getting out of shape!"
    scene a1885 with dssr
    d "You just need to find someone who shares the sentiment of staying in shape. Someone who actually likes going to the gym."
    scene a1886 with dssa
    za "That's what I hope to find someday."
    scene a1887 with dssa
    d "I bet there's a ton of guys who like going to the gym."
    scene a1888 with dssa
    za "Doing sports is one thing... Everything else has to kinda fall into place too."
    scene a1889 with dssa
    za "And I don't want to be just someone fit... Someone who did well in sports."
    scene a1890 with dssa
    za "I want to be the best."
    scene black with Dissolve(2)
    with Pause(.5)
    play sound "Music/Sfx/Punch.ogg"
    scene a1891 with vpunch
    za "NGGH!"
    scene a1892 with dssa
    d "One more."
    "She breathes fast."
    scene a1893 with dssa
    za "Nggh!"
    scene a1894 with dssa
    d "I heard Nadia did another rep!"
    play sound "Music/Sfx/Punch.ogg"
    scene a1895 with vpunch
    za "NHHHHHIIIII." 
    scene a1896 with dssa
    if ZaraBBallTrust5x0 is True:
        za "Arrrrghh! That... fucked me!"
        scene a1902 with dssa
        d "I like that you always push the limit."
        scene a1903 with dssa
        za "What did Tom Platz say?"
        scene a1904 with dssa
        d "Who?"
        scene a1905 with dssr
        za "You don't ever want to leave the gym like a loser."
        za "Always give it all."
        scene a1906 with dssa
        d "Jacuzzi?"
        scene a1907 with dssa
        za "Not for me. I'll go for another run."
        za "I might join you later."
    else:
        za "Arrrrghh! That... fucked me!"
        scene a1897 with dssa
        d "I like that you always push the limit."
        scene a1898 with dssa
        za "What did Tom Platz say?"
        scene a1899 with dssa
        d "Who?"
        scene a1900 with dssr
        za "You don't ever want to leave the gym like a loser."
        za "Always give it all."
        scene a1906 with dssa
        d "Jacuzzi?"
        scene a1907 with dssa
        za "Not for me. I'll go for another run."
        za "I might join you later."
    stop music fadeout 4
    scene a1908 with dssr
    with Pause(.5) 
    scene black with Dissolve(2)
    with Pause(.5)
    jump Jacuzzi5x5

label Jacuzzi5x5:
    $ play_playlist(playlist_MystyGood)
    scene a2 with dssb
    pause
    scene a1 with dssa
    d "Oh. Morning."
    scene a3 with dssa
    m "Good morning."
    scene a4 with dssa
    d "Do you mind if I get in?"
    scene a5 with dssa
    m "Please."
    scene a6 with dssa
    m "I'll get appropriately dressed."
    scene a7 with dssa
    d "We're no strangers. It's not like I haven't seen you nude."
    scene a8 with dssr
    m "I think it's appropriate to do so. We're guests here."
    scene a9 with dssa
    d "That makes no sense, you were nude until-"
    scene a10 with vpunch
    m "Shut up and be quiet!"
    scene a11 with dssr
    pause
    scene a12 with dssr
    pause
    scene a13 with dssa
    pause
    scene a14 with dssa
    m "Did you and Zara work out?"
    scene a15 with dssa
    d "Yes. She woke me up at like four in the morning."
    scene a14 with dssa
    m "It's great you all get along so well. Zara's a bundle of positive energy."
    scene a15 with dssa
    d "I like that about her."
    scene a16 with dssr
    m "How's your room?"
    scene a17 with dssa
    d "Pretty awesome."
    d "The Cheeto might get to you later to complain."
    scene a16 with dssa
    m "I expect it."
    scene a18 with dssa
    d "When's the next book club?"
    scene a19 with dssa
    m "On Sunday."
    scene a20 with dssa
    m "...You're still going?"
    scene a21 with dssa
    d "Yeah."
    d "At least you won't need to hide Emilia from us anymore."
    scene a20 with dssa
    m "I never hid her from you!"
    scene a21 with dssa
    d "Yes, you did. Why else didn't she come back after New Year's Eve?"
    scene a20 with dssa
    m "We were both busy."
    scene a21 with dssa
    d "You know... I take it personal for how stupid you sometimes take me."
    "She sighs loudly."
    scene a22 with dssr
    d "You should be glad the Cheeto's not as perceptive as I am."
    d "I know you dread the day she finds out."
    scene a23 with dssa
    m "Finds out what?"
    scene a22 with dssa
    d "Your real background with Emilia."
    scene a24 with dssa
    m "...I have no idea what you're talking about."
    d "Mhm."
    scene a21 with dssr
    d "On to other topics..."
    d "Mila, Nami and I talked about moving into one of the ZPR houses."
    scene a25 with dssr
    m "Oh. Really?"
    m "Huh."
    scene a27 with dssa
    d "You don't sound very happy."
    scene a25 with dssa
    m "No, it's just that it's a big change if you two decide to do so."
    m "I haven't lived alone in a long time."
    scene a26 with dssa
    d "(She's in a vulnerable place right now. Yesterday the house had to be quarantined and now I told her that we'd be moving out soon.)"
    scene a28 with dssa
    d "No matter what, we'll always be with you. This includes that you can always live with me."
    scene a29 with dssa
    m "Oh, and where am I going to sleep? In your bedroom?"
    scene a30 with dssa
    d "If there's no alternative. Yes."
    scene a31 with dssa
    "Noji laughs."
    scene a32 with dssa
    d "You know how important you are to me. There's no one I trust as much as I trust you."
    scene a33 with dssa
    m "Nami?"
    scene a34 with dssa
    d "The ghosts of the past are always with us."
    scene a35 with dssa
    m "...Yeah."
    scene a36 with dssa
    pause
    scene a37 with dssa
    d "Please do me a favor. If anything's up... No matter what, you can come to me... Or the Cheeto."
    d "We're not always easy but we'll always have your back."
    scene a39 with dssa
    m "*Softly* I know." 
    scene a38 with dssa
    d "You're being inappropriate."
    scene a39 with dssa
    "She scoffs."
    scene a41 with dssa
    pause
    scene a42 with dssa
    d "I'll soon be visiting the old town with Amber..."
    scene a43 with dssa
    pause
    scene a185 with dssa
    m "I don't think that's a good idea."
    scene a186 with dssa
    d "Amber's the professional and thinks it is."
    scene a185 with dssa
    m "I'll talk to her."
    scene a187 with dssr
    d "Noji."
    d "I'm not a child. You're not my mother. I can talk for myself."
    scene a294 with dssa
    d "I know you mean well, but please don't do this all the time."
    d "It really puts me off."
    scene a295 with dssa
    m "This is different!"
    m "The old town is-"
    scene a296 with dssa
    d "I know the risks... But I know that I need to do it."
    d "There's no way around it... I'll need to face the demon."
    scene a297 with dssa
    "Noji looks at you intensely. Desperately trying to keep something from spilling out."
    scene a298 with dssa
    d "Don't you say it."
    scene a299 with dssa
    "She smiles a little."
    scene a300 with dssa
    m "*Cute voice* In case you want me to come with you... Just ask."
    scene a301 with dssr
    pause
    scene a302 with dssr
    m "Does Mila have a house in mind for you?"
    scene a303 with dssa
    d "She's in contact with ZPR and they have a house."
    d "But we will need to get jobs in order to pay for it."
    scene a302 with dssa
    m "We'll speak about it again when you actually move out."
    scene a304 with dssa
    m "Nami's been threatening to move out for years and she still hasn't done so."
    scene a305 with dssa
    d "Robin. Charlie's kid will probably move with us."
    scene a304 with dssa
    m "Oh! That's nice."
    m "I like Robin,  and I overheard her and Sasha talking about her moving out before."
    scene a305 with dssa
    d "What about Sasha?"
    scene a306 with dssa
    m "I like Sasha. She's very intelligent. She can be a little... disagreeable and prideful."
    scene a307 with dssa
    d "How did she get the scar?"
    scene a306 with dssa
    m "You'll have to ask her. It's a very personal topic and certainly not my place to talk about."
    scene a307 with dssa
    d "But you know how she got it?"
    scene a306 with dssa
    m "Yes."
    $ ContinuePoint = False
    while ContinuePoint is False:
        menu:
            "What do you think of Anna?":
                scene a309 with dssr
                m "Anna... is... special."
                m "Special is the nicest way I can put it."
                scene a310 with dssa
                d "You don't like her?"
                scene a309 with dssa
                m "I have no enemies in the book club. I'm on good to decent terms with everyone."
                m "Anna is a little too childish. I don't really vibe with that."
                if AnnaSTG2 is True:
                    d "(I should probably not tell Noji that Anna most likely wants to bone me.)"
                scene a310 with dssa
                d "This Katie?"
                scene a311 with dssa
                pause
                d "(Interesting.)"
                scene a312 with dssa
                m "Katie and I go way back and we weren't always on the same page."
                scene a313 with dssa
                d "I see."
            "Ask about Jenna.":
                scene a309 with dssa
                m "Jenna has been a friend of mine for over a decade."
                m "She has her issues, but she makes me laugh."
            "Ask about Charlie.":
                scene a310 with dssa
                d "You and Charlie are?"
                scene a309 with dssa
                m "We're good friends."
                m "Sure, Charlie's special... Special in the way that she likes to be in control."
                m "Which raises tensions in the club."
                scene a310 with dssa
                d "Did people quit before?"
                scene a309 with dssa
                m "Of course."
                scene a310 with dssa
                d "I can't blame them... the book sucks."
                scene a309 with dssa
                m "I agree."
                scene a312 with dssa
                m "But we're not reading the book we wanted... We did so to get rid of a member."
                scene a313 with dssa
                d "So it was a strategic maneuver?"
                scene a312 with dssa
                m "Yes."
                scene a313 with dssa
                d "Did it work?"
                scene a312 with dssa
                m "Oh yes. Anna quit. A different Anna."
                scene a311 with dssa
                d "Good... I feared for your sanity if you'd actually voted for that book."
                scene a312 with vpunch
                m "Hey! It's a nice book!"
            "Continue":
                $ ContinuePoint = True
    $ ContinuePoint = False
    scene a315 with dssr
    pause
    scene a314 with dssa
    d "Do the new members get to vote on the next book too?"
    scene a316 with dssr
    m "Yes. You can cast your vote."
    scene a317 with dssa
    d "How are you and Nick?"
    scene a318 with dssa
    m "We're doing well."
    m "What do you think of him?"
    scene a319 with dssa
    d "I like him."
    d "He seems to be a good guy."
    scene a318 with dssa
    m "He is."
    scene a317 with dssa
    d "Considering what you went through, you really deserve it."
    scene a320 with dssa
    m "Thank you, [name]."
    scene a321 with dssr
    pause
    scene a322 with dssr
    pause
    scene a323 with dssa
    m "I'm going to get out."
    scene a324 with dssa
    d "Alright. Have a nice day."
    m "You too."
    scene a325 with dssr
    pause
    scene a326 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene a327 with dssb
    pause
    scene a328 with dssr
    "You slowly feel the bubbles turn on."
    d "Mmmh..."
    scene a330 with dssr
    pause
    scene a331 with dssa
    pause
    scene a332 with dssa
    za "I'm surprised you're still in here."
    za "How wrinkly are you?"
    scene a333 with dssa
    menu:
        "Joke.":
            d "Foreskin level of wrinkly."
            scene a334 with dssa
            za "Eww!"
        "Respond normally.":
            d "I love this so much I don't care how wrinkly I get."
    scene a336 with dssa
    za "I could die in here, and I wouldn't mind."
    za "Actually, I'd mind the second the water rushes into my lungs and I start to spasm uncontrollably."
    scene a337 with dssa
    pause
    scene a338 with dssa
    za "In the winter... when it's super cold, you've gotta stay outside for a few minutes and then jump in here and it's like an orgasm."
    scene a339 with dssa
    d "The only thing missing is something to eat."
    scene a340 with dssa
    za "I heard you ate Nadia's banana!"
    scene a341 with dssa
    d "Yeah."
    scene a342 with dssa
    za "I laughed so hard when I heard that."
    scene a344 with dssr
    d "What's up with those bananas anyway?"
    scene a343 with dssa
    za "I have no idea."
    za "I think she just eats them."
    scene a345 with dssa
    za "Eva thinks she uses them for... other things."
    scene a346 with dssa
    d "I heard the name Eva before."
    scene a347 with dssa
    za "Petite, tanned girl with black hair."
    scene a346 with dssa
    d "Oh! Beanpole."
    scene a348 with dssa
    za "Don't say that!"
    if BelMilNMF5x0 is True:
        scene a349 with dssa
        d "...Right, I promised Bella not to do it anymore."
    scene a350 with dssa
    za "I don't like it when people make fun of other people for how they were born."
    za "It's the same with my sister's boyfriend."
    scene a351 with dssa
    za "He's ummm... Not well endowed."
    scene a352 with dssa
    d "How do you know that?"
    scene a353 with dssa
    za "He was once with us in the jacuzzi."
    za "I hate it when people blame others for something they have no control over."
    scene a352 with dssa
    d "You blame people for stuff they do have control over?"
    scene a353 with dssa
    za "Exactly."
    scene a355 with dssr
    d "This Mario, what's he like?"
    scene a354 with dssa
    za "Hmm, he's nice."
    za "Not very assertive."
    za "I don't like how easy he caves in to pressure."
    scene a356 with dssa
    za "People seem to expect a lot from him, and he gives in sooo easily."
    scene a357 with dssa
    d "I'm surprised someone as assertive as Vanessa is into him."
    play sound "Music/Sfx/Slap.ogg"
    scene a358 with vpunch
    za "Naah, you don't get to say that."
    za "You don't know anything about either of them."
    scene a359 with dssa
    d "You're right. I have no real idea who they are."
    scene a360 with dssa
    d "But Mario and I still have something to talk about."
    scene a361 with dssa
    za "What is it?"
    scene a360 with dssa
    d "He and his friends insulted me and Mila... Especially Mila."
    scene a362 with dssa
    za "Fucking assholes."
    scene a363 with dssr
    za "When was that?"
    scene a364 with dssa
    d "First day of college. We ran into them in front of a cafe."
    scene a363 with dssa
    za "I'll talk to him."
    scene a365 with dssa
    d "No."
    d "Stay out of it."
    scene a366 with dssa
    za "You can't tell me what to do."
    scene a365 with dssa
    d "Why do you people always get involved in other people's business?"
    scene a367 with dssa
    za "That's what life's about, no? If you never got involved in other people's business... What's left?"
    za "Lending a helping hand to your friends and getting involved in their business is what brings you closer together."
    scene a368 with dssa
    pause
    scene black with Dissolve(1)
    with Pause(.5)
    scene a369 with dssb
    pause
    scene a370 with dssa
    n "Morning."
    scene a371 with dssr
    pause
    scene a372 with dssr
    mi "Morning."
    scene a375 with dssr
    za "Good morning!"
    if MilaSleep5x0 is True:
        scene a373 with dssr
        mi "I was wondering where you went."
        scene a376 with dssa
        d "Some insane fuck woke me up at 4:30am to train."
        scene a377 with dssa
        pause
    scene a375 with dssr
    za "Girlies, lose your clothes and get in."
    scene a374 with dssa
    mi "Another time."
    if RaceWithImpossibleOdds is True:
        scene a379 with dssr
        "You notice the Cheeto is trying to avert her eyes."
        d "(Does she have any idea how obvious and tense she looks?)"
        scene a381 with dssa
        d "Cheeto?"
        d "Do you need to poop?"
        scene a380 with dssa
        "She squints her eyes, knowing full well you looked right through that bad excuse of a facade."
        scene a383 with dssa
    else:
        scene a382 with dssa
    n "Can Mila and I use the gym?"
    scene a378 with dssa
    za "Of course."
    scene a384 with dssa
    mi "Thank you!"
    scene a385 with dssr
    pause
    scene a386 with dssr
    pause
    scene a387 with dssa
    stop music fadeout 5
    #play ambient "Music/Sfx/Summer_Morning.ogg"
    d "Have I told you that Nami and I are moving in with Mila?"
    scene a388 with dssa
    pause
    scene a389 with dssa
    za "*Sad* What?"
    scene a390 with dssa
    d "We'll move into one of those student houses."
    play music "Music/Scott Buckley/Scott Buckley - Resonance.ogg"
    play sound "Music/Sfx/Slap.ogg"
    scene a391 with vpunch
    za "No!"
    scene a392 with vpunch
    za "No! NO, NO!"
    if ZaraBBallTrust5x0 is True:
        scene a394 with dssa
        za "Please don't!"
    scene a395 with dssa
    d "...What's happening?"
    scene a397 with dssr
    za "We're training buddies!"
    za "I was so looking forward to getting up with you at 3:30 every morning!"
    scene a398 with dssa
    d "...Good that I'm moving out soon."
    scene a399 with vpunch
    play sound "Music/Sfx/Punch.ogg"
    za "NO!"
    scene a400 with dssa
    za "That's it. I'm not training you anymore."
    scene a401 with dssa
    d "I'm just movin-"
    scene a402 with dssa
    za "No!"
    scene a403 with dssa
    pause
    scene a404 with dssa
    d "We can still train every day."
    scene a405 with dssa
    za "No way."
    scene a406 with dssa
    d "You're being ridiculous."
    scene a407 with dssa
    stop music fadeout 7
    za "I'm not!"
    scene a409 with dssr
    va "You are."
    scene a408 with dssa
    za "Am I?"
    scene a425 with dssr
    d "Yeah."
    play music "Music/Caio/Caio - If I were a bird.ogg" fadein 5
    scene a426 with dssa
    pause
    scene a427 with dssa
    za "I was so... man..."
    scene a428 with dssa
    za "*Sigh*"
    scene a410 with dssr
    va "I know it's hard to find someone who's as dedicated to progress as you are."
    va "But hear me out, little one... You'll find him."
    scene a411 with dssr
    za "You make it sound like I want to date [name]."
    if ZaraBBallTrust5x0 is True:
        za "I want him to spot me while I'm going for a PR... and to spot him when he goes for one..."
        scene a412 with dssa
        va "And you want him to hold you after you placed second place... For him to tell you that you're enough."
    else:
        scene a412 with dssa
    va "I told you, [name]. Let me pay for your license and you two can still work out here every day."
    scene a429 with dssr
    d "Why does nobody ask me if I want to train with her every day?"
    scene a431 with dssa
    za "Because you asked me to be your coach?"
    scene a430 with dssa
    d "...Right."
    scene a429 with dssa
    d "And I think the license is the less significant problem."
    d "Buying a car that is."
    scene a413 with dssr
    va "I have two cars. I can give you one until you get your own."
    scene a414 with dssa
    d "I'll think about it."
    d "But I fear that you want something in return."
    scene a413 with dssa
    va "Yes."
    scene a415 with dssa
    va "I'd like a double date with you and a girl of your choice."
    scene a414 with dssa
    d "...What?"
    scene a416 with dssa
    if BellaNonExclusive5x0 is True:
        va "You take a girl, let's say Bella... and you, Bella, my boyfriend and I go bowling and have dinner."
        d "(Oh no...)"
    else:
        va "You take a girl, let's say Zara... and you, Zara, my boyfriend and I go bowling and have dinner."
    scene a417 with dssa
    d "...I'll think about it."
    d "(This might be my chance to get a much clearer picture of Mario.)"
    scene a418 with dssa
    va "You have my number, right?"
    scene a417 with dssa
    d "No."
    scene a419 with dssa
    va "Doesn't matter, we'll probably see each other here everyday."
    scene a420 with dssr
    pause
    scene a421 with dssr
    d "Alright. I'm in."
    scene a422 with dssa
    va "Fabulous."
    scene a423 with dssr
    va "Tell me as soon as you've picked a girl."
    scene a424 with dssr
    pause
    scene a432 with dssr
    pause
    scene a433 with dssa
    d "Hey."
    d "I know it's not ideal, and believe me when I say, I'm also looking forward to working out with you."
    scene a434 with dssa
    pause
    scene a435 with dssa
    d "You really motivate me to go further."
    scene a436 with dssa
    pause
    scene a437 with dssa
    "You start scratching her head."
    scene a438 with dssa
    za "...Stop."
    play sound "Music/Sfx/Slap3.ogg"
    scene a439 with vpunch
    "She flops back against you."
    scene a440 with dssa
    pause
    scene a441 with dssa
    d "But seriously, if I move out, I'll come here to train with you."
    scene a442 with dssa
    za "...It's not the same."
    scene a443 with dssa
    d "I'm not moving out tomorrow."
    scene a442 with dssa
    za "It's not the same if you're not living here."
    scene a443 with dssa
    d "Well, I don't know what to say-"
    scene a444 with vpunch
    za "Stay!"
    scene a445 with dssa
    d "I can't... I need to learn to stand on my own."
    scene a446 with dssr
    za "Then stay during the training days!"
    scene a447 with dssa
    d "That I can do, I guess."
    scene a446 with dssa
    za "And we train seven days a week!"
    scene a447 with dssa
    d "I will sleep here like two or three days a week, okay?"
    scene a448 with dssa
    za "...Okay."
    scene a449 with dssa
    "Zara moves to the other side."
    scene a450 with dssr
    if BellaNonExclusive5x0 is True:
        d "(Vanessa wants me to take Bella... That's so risky.)"
    if MilaDate or miladate is True:
        d "(I obviously could ask Mila to the double date with Vanessa... It would be interesting to see the interactions between her and Mario... But maybe not... She's being sued.)"
    if VicDate or VicDateEntry2 is True:
        d "(I could ask Victoria. She'd really appreciate going on a date. Bowling might be an issue, though.)"
    if RaceWithImpossibleOdds is False:
        d "(I could also ask the Cheeto... Make it seem like I didn't have a girl to take with me.)"
    if RaceWithImpossibleOdds is True:
        d "(I could take the Cheeto with me... Nobody would question it... or suspect anything.)"
        d "(On the other hand we're talking about Vanessa... Too risky to take the Cheeto.)"
    if NiaDate5x0 is True:
        d "(There's also Nia... And I'm not gonna lie... Seeing her and Vanessa interact would be quite fun.)"
    d "(And then there's Zara. While it wouldn't be a date... I could imagine it being quite fun with her.)"
    menu:
        "Ask Zara if she wants to go there with you.":
            $ VanessaDD5x5Taken = True
            $ ZaraVanessaDate5x5 = True
            scene a451 with dssa
            d "Will you be my plus one?"
            scene a452 with dssa
            za "Are you asking me out?"
            scene a451 with dssa
            d "No. I'm asking you to go to that dinner with me... So we can eat and... I don't know... Have fun?"
            d "Later, your sister pays for my license and gives me a car, resulting in us being able to train more often."
            scene a453 with dssa
            za "Eating sounds fun... Training sounds fun... Fun sounds fun..."
            scene a454 with dssa
            za "Alright, I'll come with you."
            if BellaNonExclusive5x0 is True:
                scene a455 with dssa
                za "But she asked for Bella."
                scene a456 with dssa
                d "I don't wanna take Bella there."
        "Don't ask Zara.":
            d "(Nah, I'll pick someone else.)"
            scene a456 with dssr
            pause
    scene a457 with dssr
    d "I'll get out."
    stop music fadeout 4
    scene a459 with dssr
    pause
    scene black with Dissolve(2)
    $ play_playlist(playlist_Girly)
    with Pause(.5)
    jump TennisNadia1x0



label TennisNadia1x0:
    scene a86 with dssb
    pause
    play sound "Music/Sfx/Thud4.ogg"
    scene a87 with vpunch
    pause
    scene a95 with vpunch
    pause
    scene a96 with dssa
    nic "That was amazing, Nami!"
    scene a89 with dssr
    n "Thanks... *Breathes hard* I'm so out of breath!"
    scene a90 with dssa
    nic "You'll need to work on your endurance."
    nic "But Vanessa was right. You've got talent!"
    scene a91 with dssa
    n "Thanks!"
    scene a93 with dssr
    nic "If you're interested in a more serious approach to tennis, I could talk to an acquaintance of mine who's a tennis trainer?"
    scene a92 with dssa
    n "That would be so cool! I would definitely be interested!"
    scene a97 with dssr
    pause
    scene a98 with dssa
    pause
    scene a99 with dssa
    pause
    play sound "Music/Sfx/Thud4.ogg"
    scene a100 with vpunch
    "You watch the two play for a while."
    scene black with Dissolve(2)
    with Pause(.5)
    if RaceWithImpossibleOdds is True:
        scene a62 with dssr
        "Nick turns around to collect some of the scattered tennis balls."
        scene a63 with dssa
        n "[name]!"
        scene a64 with dssa
        pause
        d "(...Cheeto.)"
    scene a101 with dssr
    pause
    scene a102 with dssr
    na "Hey."
    scene a103 with dssa
    d "Oh. Nadia."
    d "I didn't expect you."
    scene a104 with dssa
    na "I came by for today's game. It's tradition that Zara and I watch them together."
    na "Vanessa told me you and Nami are here too, so I wanted to say hello."
    scene a105 with dssa
    d "Hello."
    scene a106 with dssa
    na "Hello."
    scene a44 with dssr
    pause
    scene a45 with dssr
    pause
    if BellaNonExclusive5x0 is True:
        scene a46 with dssa
        na "How are you and Bella doing?"
        scene a47 with dssa
        d "I'm sure you talk to her and know everything."
        scene a46 with dssa
        na "I do know most of it but... I'm sure there's things she doesn't tell me."
        scene a47 with dssa
        d "Well, there's not much to say."
        d "We're not exclusive but we sometimes... meet."
        scene a48 with dssr
        pause
        scene a49 with dssa
        na "Could you fuck her?"
        scene a50 with dssa
        d "...What?"
        scene a51 with dssa
        na "Could you spread her legs, insert your cock into her pussy, and fuck her?"
        na "She's acting up. She's frustrated and on edge. It makes her obnoxious to have around."
        scene a52 with dssa
        d "I'm sure she'll get through it."
        scene a53 with dssa
        na "She might, but we won't."
        menu:
            "Maybe give her one of your bananas for the night.":
                $ BananaPropS2_1x0 = True
                scene a54 with vpunch
                pause
                scene a55 with vpunch
                na "NO!"
                na "They're not for that!"
                scene a56 with dssa
                d "So what are they for? I have never seen you eat a banana. Yet, you always carry one."
                d "If you don't eat them, what are you doing with them?"
                scene a57 with dssa
                "She squints and says nothing."
            "Don't say it.":
                pass
    scene a58 with dssr
    pause
    scene a58a with dssa
    na "Nami's good. How long has she been playing?"
    scene a58b with dssa
    d "I'm surprised too."
    d "I always thought she was a stiff sack of potatoes."
    scene a59 with vpunch
    n "YO! I heard that!"
    scene a60 with dssr
    n "Hey Nadia!"
    na "Hi Nami!"
    scene a61 with dssa
    n "[name]! I'll give you one of these if you call me that again!"
    nic "Good morning [name]! And hello Nadia!"
    scene a67 with dssr
    na "Hey Nick!"
    scene a66 with dssa
    d "Morning Nick."
    scene a68 with dssr
    pause
    scene a69 with dssa
    stop music fadeout 10
    menu:
        "Are we going to play another tabletop game?":
            $ TBTNadiaS2_1x0 = True
            scene a70 with dssa
            na "Oh. Sure, I was working on a new scenario."
            scene a71 with dssa
            na "I'm currently quite busy with personal things. I'll get back to you."
            scene a72 with dssa
            d "Alright."
        "Don't ask her.":
            pass
    jump VicMorningS2



label VicMorningS2:
    scene a7934 with dssr
    pause 
    scene a7935 with dssr 
    pause 
    scene a7936 with dssr
    pause 
    play sound "Music/Sfx/Thud4.ogg"
    scene a7937 with vpunch
    pause 
    scene a7938 with dssr
    "Her breathing accelerates..."
    scene a7939 with dssa 
    "She hyperventilates, trying to keep quiet."
    play sound "Music/Sfx/DoorOpen.ogg"
    scene a7940 with dssa
    "The door opens." 
    scene a7944 with dssr
    maj "Hey? Is everything okay?"
    scene a7941 with dssr
    v "Ohh- yes..."
    scene a7950 with dssr
    "Maja spots the cuddly toy on the ground."
    scene a7942 with dssr
    pause 
    scene a7943 with dssa
    v "It slipped out of my hand..." 
    scene a7951 with dssr
    pause
    scene a7945 with dssr
    maj "Do you want breakfast?"
    scene a7946 with dssa
    v "No. I'm not hungry."
    scene a7945 with dssa
    maj "Are you sure?"
    scene a7947 with vpunch
    v "Majaaa!"
    scene a7948 with dssr
    maj "Fine."
    scene a7949 with dssa
    maj "I'll take a shower. Yell if you need anything."
    scene a7952 with dssr
    pause 
    scene black with Dissolve(2)
    with Pause(.5)
    jump WatchingTheGameS2_1x0


label WatchingTheGameS2_1x0:
    $ play_playlist(playlist_Sports)
    scene a73 with dssr
    za "[name]!" 
    za "What are you doing?"
    scene a74 with dssa
    d "I'm sitting around."
    scene a75 with dssa
    za "Are you gonna watch the game with us?"
    scene a74 with dssa
    d "What game?"
    scene a75 with dssa
    za "Huh? What do you mean?"
    za "You're not watching sports?"
    scene a74 with dssa
    d "No."
    scene a76 with dssr
    za "Well, do you want to?"
    za "We're watching football."
    scene a77 with dssa
    d "What kind of football?"
    scene a76 with dssa
    za "The one Bella plays. The one with the foot."
    scene a78 with dssa
    za "Nadia! Do you have a date today?"
    scene a80 with dssa
    na "No."
    scene a79 with dssa
    za "Then what's up with the tiddy dress?"
    scene a82 with dssr
    na "I just bought it and I wanted to show it to you."
    scene a81 with dssa
    za "I like it."
    za "And so will every guy!"
    scene a82 with dssa
    na "I have a bra with me for later."
    scene a81 with dssa
    za "Cool! I can't wait for you not to wear it!"
    scene a78 with vpunch
    za "Let's go! The game's starting!"
    scene a83 with dssr
    pause
    scene a84 with dssa
    d "Cheeto! We're gonna watch a game."
    scene a85 with dssa
    n "I'm having my own game here, yo!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene a107 with dssb
    za "Sam, Jared, this is [name]."
    scene a109 with dssr
    sam "Hey."
    jar "Hey."
    d "Hey."
    scene a110 with dssr
    za "And this is Miriam."
    if BellaKiss3x5 is False:
        d "I know her."
        scene a111 with dssa
        miri "Hello [name]."
        scene a110 with dssa
        za "Oh right! Nora did cuff herself to you!"
        za "I saw some pictures."
        d "Somebody took pictures?"
        scene a112 with dssr
        miri "...Yeah. Somebody..."
    else:
        scene a111 with dssa
        miri "I've seen him around."
        scene a110 with dssa
        "You give her a nod."
    pause
    scene a113 with dssr
    sam "Alright Zara... Fifty on the Jericho Eagles."
    za "Tzz! Fifty it is!"
    scene a117 with dssr
    jar "The Wormies haven't beaten the Eagles yet."
    za "I believe in them."
    scene a112 with dssr
    miri "I'll sit this one out."
    scene a115 with dssr
    sam "What about you [name]? Are you in?"
    scene a114 with dssa
    d "Not today."
    d "I don't know which one of those teams sucks less."
    scene a121 with dssr
    za "So, I'm obviously for the Wollust Wormies."
    scene a122 with dssa
    za "Samuel there has been hit on the head as a kid and thinks the Jericho Eagles are it."
    scene a116 with dssr
    sam "Give it 90 minutes Zara and you'll be taught a lesson."
    if ZaraBBallTrust5x0 is True:
        scene a108 with vpunch
        play sound "Music/Sfx/Punch.ogg"
        "Zara lets herself fall onto the couch."
        scene a119 with dssa
        "Miriam lets out a chuckle."
        za "Mh?"
        scene a120 with dssr
        miri "Nooothing."
    else:
        scene a118 with dssr
        pause
    za "It's starting!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene a123 with vpunch
    za "IS THIS REF BLIND?!"
    scene a124 with dssa
    na "*Laughs*"
    scene a125 with dssa
    za "I'M... FREAKING OUT HERE!"
    scene a126 with dssa
    d "*Whisper* Is she always like that?"
    scene a127 with dssr
    na "*Whisper* Every time."
    scene a128 with dssr
    miri "Thirty more minutes Zara."
    scene a129 with dssr
    za "*Whispers* Please, please, please..."
    if ZaraBBallTrust5x0 is True:
        scene a130 with vpunch
        play sound "Music/Sfx/Punch.ogg"
        "Zara flops onto your leg."
        scene a131 with dssr
        pause
        scene a132 with dssa
        "You and Nadia share a look."
    else:
        scene a133 with dssa
        "Zara flops back on to the couch."
    scene black with Dissolve(2)
    with Pause(.5)
    scene a134 with dssb
    pause
    scene a135 with vpunch
    za "YES!"
    sam "No!"
    scene a136 with vpunch
    za "I TOLD YOU! I TOLD YOU HE'D MAKE IT!"
    scene a137 with vpunch
    "Zara takes a leap towards Nadia..."
    scene a138 with vpunch
    play sound "Music/Sfx/Punch.ogg"
    na "Auu!"
    sam "THIS IS BULLSHIT! I'M GOING HOME!"
    scene a139 with vpunch
    za "MY FIFTY BUCKS!"
    "Jared laughs at Samuel's fast exit."
    scene a140 with vpunch
    play sound "Music/Sfx/Punch.ogg"
    na "Zaaaaraaa!"
    scene a141 with dssa
    za "You're comfy."
    if ZaraBBallTrust5x0 or ZaraVanessaDate5x5 is True:
        scene a142 with dssr
        miri "Hey [name]."
        miri "I have this friend who'd like to ask you out."
        scene a143 with dssa
        za "Who?"
        scene a145 with dssa
        miri "I'd rather not out her yet..."
        scene a146 with dssr
        d "I'm not interested."
        scene a147 with dssa
        "Zara sits down in front of you."
        scene a148 with dssa
        za "[name] and I are busy with training."
        scene a149 with dssa
        miri "But it wouldn't bother you Zara, right?"
        scene a150 with dssa
        za "Huh? Why would it bother me if [name] dated someone?"
        scene a149 with dssa
        miri "I'm just asking."
        scene a151 with dssa
        jar "Oh, Miri... I thought I was the only one getting-"
        scene a153 with dssa
        za "What are you guys saying?"
        scene a152 with dssa
        jar "You've got a full out lady boner."
        scene a149 with dssa
        miri "Damn right."
        scene a153 with vpunch
        za "I don't!"
        scene a154 with dssr
        d "You know Zara... You would be a little more convincing if you weren't half on top of me."
        scene a155 with dssa
        pause
        scene a156 with dssa
        pause
        scene a157 with dssa
        za "...I don't have a lady boner."
        scene a158 with dssa
        na "...There it is."
        scene a159 with dssa
        "Zara slowly slides off your leg."
        scene a160 with dssr
        miri "You two should go on a date."
        if ZaraVanessaDate5x5 is True:
            scene a161 with dssa
            za "We're going on a fake date."
            scene a162 with dssr
            d "Are we?"
            scene a163 with dssa
            za "The date with Nessi?"
            scene a162 with dssa
            d "Oh right!"
            d "Yeah, we're gonna have dinner together."
            scene a164 with dssa
            za "And you're going to see first hand how Nessi takes care of Mario."
            scene a165 with dssa
            d "I'd rather not see that."
            scene a166 with dssa
            miri "Are you two gonna make out?"
            jar "They're gonna do more than that."
            scene a167 with dssa
            "They laugh."
            scene a168 with dssa
            za "Idiots."
        if BellaNonExclusive5x0 is True:
            scene a161 with dssa
            za "[name]'s with Bella."
            scene a169 with dssr
            miri "You guys are in an actual relationship?"
            d "We're not serious."
        else:
            scene a168 with dssr
            za "We're just friends."
            if MilaSleep5x0 is True:
                pass
            else:
                scene a178 with dssr
                jar "I saw Mila the other day."
                scene a168 with dssr
                za "Dude. We told you, you have no shot with her."
                za "I think she likes [name]."
                scene a178 with dssr
                jar "Really?"
                scene a179 with dssa
                d "You sound impressed?"
        if MilaSleep5x0 is True:
            scene a164 with dssr
            za "And... [name] spent last night with Mila."
            scene a169 with dssr
            miri "Damn!"
            scene a178 with dssr
            jar "What? Seriously?"
            jar "You're hitting Mila?"
            scene a179 with dssa
            d "You sound impressed?"
        else:
            pass 
        scene a178 with dssa
        jar "Yeah, lot's of my friends tried to take her out on a date."
        scene a170 with dssr
        miri "[name]'s handsome."
        scene a174 with dssr
        za "Even more important... [name] doesn't have the stench."
        scene a180 with dssr
        jar "What stench?"
        scene a170 with dssr
        miri "The 'I desperately need sex' stench."
        miri "He doesn't have it."
        scene a172 with dssr
        na "Not like Samuel... Or you, Jared."
        scene a173 with dssa
        jar "What?! I don't have the stench!"
        scene a171 with dssr
        miri "You do."
        scene a175 with dssr
        jar "If you'd take me with you into the jacuzzi, I could clean myself... You know."
        scene a176 with dssa
        za "Are you sitting down Jared?"
        scene a177 with dssa
        jar "Are you going to hit me?"
        scene a176 with dssa
        za "[name]'s been with me in the jacuzzi... Twice."
        scene a181 with dssr
        "Jared looks into the room in shock."
        scene a180 with dssa
        jar "...Seriously?"
        za "Yep."
        scene a182 with dssa
        jar "...Alright."
        scene a183 with dssa
        jar "Well, the game's over anyway."
        jar "It was nice meeting you [name]."
        scene a184 with dssa
        "You raise your beer."
        scene a1909 with dssr
        miri "Fifty bucks he's going home to cry."
        scene a1910 with dssa
        za "I feel bad. I shouldn't have done him like that."
        scene a1909 with dssa
        miri "Speaking of the jacuzzi... Wanna grab some beers and get in?"
        scene a1911 with dssa
        d "Not me. I already had some jacuzzi times."
        scene a1912 with dssa
        miri "We can still sit in the garden."
        scene a1913 with dssa
        na "I've got to leave. Nancy will be at the library in around an hour."
        if BellaNonExclusive5x0 is True:
            scene a1914 with dssr
            na "[name]?"
            na "Don't forget to fuck Bella."
            if ZaraBBallTrust5x0 is True:
                scene a1915 with vpunch
                "Zara almost chokes on her beer."
                scene a1916 with vpunch
                za "He doesn't need to do that! It will cripple his recovery!"
                scene a1918 with dssr
                pause
                scene a1917 with dssa 
                pause
                scene a1919 with dssa
                na "You're a cripple, Zara."
            else:
                scene a1920 with dssr
                "They chuckle."
                scene a1921 with dssa
                za "But not too much! He needs to train!"
    stop music fadeout 4
    scene a1922 with dssb
    pause
    scene a1923 with dssa
    tvanchor "-after criticism of their rather aggressive approach."
    scene a1927 with dssr
    pause 
    scene a1928 with dssr
    tvanchor "The Minister of Foreign Affairs, Charlotte Estrees and her cabinet briefed the press on the negotiations with the other states in the Twelve Star Coalition."
    scene ag1924 with dssr
    pause
    scene ag1925 with dssr
    charlie "We're confident that the remaining states will soon ratify the agreement on our proposed changes for the freedom of expression."
    scene ag1926 with dssa
    tvanchor "More about this in tonight's talk show 'Beyond' at 8:15 PM, live with Foreign Minister Miss Estrees, Anthony Blake from the RSA, and Hussein Barakat from the IDA."
    scene a1929 with dssr
    d "(Why am I not surprised that Charlie's a politician? But the Minister of Foreign Affairs)?"
    d "I got under her skin relatively easy... Mhh... probably because the book club is her safe space.)"
    d "(I'll go change and meet Zara in the garden.)"
    scene black with Dissolve(2)
    play ambient "Music/Sfx/Ambient_Morning.ogg"
    with Pause(.5)
    jump JacuzziS2_1


label JacuzziS2_1:
    scene a1930 with dssb
    pause
    scene a1931 with dssr
    pause
    scene a1932 with dssa
    play sound "Music/Sfx/TornadoAlarmSTG1.ogg"
    "The surrounding phones start ringing."
    scene a1933 with dssa
    miri "Tornado?"
    scene a1934 with dssa
    d "Level 1 warning. Nothing to worry about."
    scene a1935 with dssa
    miri "Yeah, you can start worrying when the sirens go off."
    scene a1945 with dssr
    za "I'm so afraid of these damn tubes."
    za "But at least we're not living in the yellow zone."
    scene a1946 with dssa
    d "Maja and Victoria do."
    scene a1945 with dssa
    za "Oh."
    scene a1936 with dssr
    miri "It's been more than three years since a tornado came even close to the city."
    scene a1937 with dssa
    za "Stop talking about tornados, please!"
    $ play_playlist(playlist_Smooth)
    scene a1938 with dssa
    miri "How do I turn on the bubbles?"
    scene a1939 with dssr
    za "There's a button at the entrance."
    scene a1940 with dssr
    miri "It's usually a bit above the entrance."
    scene a1941 with dssa
    pause
    scene a1942 with dssr
    pause
    scene a1944 with dssa
    miri "Zara, have you seen the new ZPR model catalogue?"
    scene a1943 with dssa
    za "Not yet."
    scene a1946 with dssr
    miri "Jim's now a prestige model."
    scene a1945 with dssa
    za "He's handsome. It makes sense."
    scene a1947 with dssr
    miri "Come in!"
    scene a1948 with dssr
    na "No, not today. I have to leave soon. Nancy is going to be a lil' late."
    scene a1949 with dssa
    miri "Are we all still in for Friday?"
    za "Remind me again."
    scene a1944 with dssr
    miri "The NUA frat party."
    scene a1967 with dssr
    za "Ah yes."
    za "I hope Alexia's there."
    scene a1966 with dssa
    miri "She's a bitch."
    scene a1944 with dssr
    miri "She's so belittling and full of herself."
    scene a1950 with dssr
    miri "Nadia? You're allowed to come if you leave that stupid banana at home."
    scene a1951 with vpunch
    na "Don't call my banana stupid!"
    scene a1952 with dssa
    miri "Have you ever masturbated with a banana?"
    scene a1953 with vpunch
    na "Miriam!"
    scene a1954 with dssr
    miri "Answer my question."
    scene a1955 with vpunch
    na "Shut up." 
    scene a1956 with vpunch
    miri "You totally did!"
    scene a1957 with dssr
    pause
    stop ambient fadeout 6
    scene a1958 with vpunch
    miri "You need a boyfriend Nadia!"
    miri "ONE THAT ISN'T YELLOW AND HAS A BETTER PENIS TO BODY RATIO!"
    scene a1959 with dssr
    $ play_playlist(playlist_Romance)
    d "I heard Nadia never dates?"
    scene a1960 with dssa
    "Zara and Miriam chuckle."
    scene a1961 with dssa
    za "That's just a rumor."
    scene a1962 with dssa
    za "It's true that she rebuffs most guys. But she goes on dates."
    scene a1961 with dssa
    miri "She had a boyfriend in high school for a few months, no?"
    scene a1963 with dssa
    za "Yeah."
    za "Didn't go on for long."
    menu:
        "Ask for more info.":
            $ Info_Nadia_Dating_CH1 = True
            scene a1964 with dssa
            d "What happened?"
            scene a1965 with dssa #
            za "Mhhmmm..."
            scene a1966 with dssr 
            pause 
            scene a1967 with dssa
            za "Not many can deal with her libido. She prefers to be alone."
            scene a1966 with dssa
            d "Too low? Too high?"
            scene a1967 with dssa
            za "Too high."
            scene a1969 with dssa
            miri "She did get checked out, right?"
            scene a1968 with dssa
            za "Yeah, it's an anomaly."
            miri "And don't you dare say 'I could.' [name]."
            miri "Guys have no idea what really goes into it."
            scene a1970 with dssr
            d "So that's why she sexualizes the board games so much? It's an outlet for her?"
            scene a1971 with dssa
            za "I guess."
        "Not interested.":
            pass
    scene a1972 with dssr
    miri "You never had a boyfriend, right Zara?"
    scene a1973 with dssa
    za "I'm busy."
    scene a1974 with dssa
    miri "If you say sports I'm gonna hit you."
    scene a1973 with dssa
    za "Studies, athletic performance and... Not having an interest in interpersonal conflicts."
    scene a1971 with dssr
    za "Life's much easier without any strings attached."
    za "You taught me that."
    scene a1975 with dssr
    miri "I did?"
    scene a1976 with dssr
    za "I saw your relationship with Larry. That was enough to turn me off the idea of getting into a relationship... Maybe ever."
    if BellaNonExclusive5x0 is True:
        scene a1977 with dssr
        miri "How's it with Bella, [name]?"
        scene a1978 with dssa
        d "Mh?"
        scene a1977 with dssa
        miri "How is it going with Bella?"
        scene a1978 with dssa
        d "There's nothing worth mentioning."
        scene a1979 with dssa
        miri "Just for your information... Bella and I have no issues with each other."
        scene a1980 with dssa
        d "Is that so?"
        scene a1979 with dssa
        miri "It's only Kate and Bella."
        miri "Nora, Bella and I chit-chat."
    else:
        pass 
    scene a1981 with dssa
    za "In Larry's defense... I could see how it went down..."
    scene a1982 with dssr
    miri "Zara."
    miri "He fucked up and now he has to live with the consequences."
    scene a1983 with dssa
    d "What did he do?"
    scene a1984 with dssa
    miri "None of your business."
    scene a1997 with dssr
    za "*laughs* He confused Miri and Nora... He slapped Nora on the ass."
    scene a1998 with dssa
    d "Not gonna lie... I could see that happening."
    scene a1985 with vpunch
    miri "We don't even look alike!"
    scene a1986 with dssa
    za "You do."
    scene a1987 with vpunch
    miri "No!"
    menu:
        "Do you look the same nude?":
            $ MiriamNude_S2 = True
            scene a1989 with dssr
            miri "I don't think we do."
            miri "If you ever see Nora nude, you can compare them."
            scene a1988 with dssa
            d "I would need to see you both side by side."
            scene a1991 with dssa
            za "Greedy [name]. You're going for both at once?"
            scene a1990 with dssa
            miri "He totally is."
            scene a1992 with dssa
            miri "If the guys from the first team hear you're going for one of the girls, you might get a problem." 
            scene a1993 with dssr
            za "I thought you and Larry weren't a thing anymore."
            scene a1994 with dssa
            miri "..."
            scene a1995 with dssr
            miri "Shut up."
        "Don't ask Miriam that.":
            pass
    scene a1999 with dssr
    miri "I'll take the shower at the gym."
    scene a2000 with dssa
    za "Sure."
    scene a2001 with dssa
    za "Do you want me to text Louise and her boyfriend?"
    scene a2002 with dssa
    d "The two we met playing basketball?"
    scene a2001 with dssa
    za "Yes."
    menu:
        "Yeah. Contact them.":
            $ LouiseS2 = True
            scene a2003 with dssr
            za "Alrighty."
            scene a2004 with dssa
            za "We've got to show them what we're made of!"
            scene a2005 with dssa
            d "We did so already, no?"
            scene a2003 with dssa
            za "In a real game with something to lose."
        "Not yet.":
            scene a2006 with dssa
            za "Okay."
    if BellaNonExclusive5x0 is True:
        scene a2008 with dssr
        d "Bella told me that you two used to play football."
        scene a2007 with dssa
        za "True."
        za "We both played offensive midfield."
        scene a2008 with dssa
        d "Do you still play?"
        scene a2009 with dssa
        za "I haven't... played in a long time"
        za "It's tainted by the legacy of my mother... It always reminds me of her."
        scene a2010 with dssa
        d "Yet, you watch the games."
        scene a2011 with dssa
        za "That's different."
        scene a2010 with dssa
        d "Is it?"
        scene a2011 with dssa
        za "Emotions and... trauma don't follow logic."
        za "It doesn't trigger for me when I watch them. Quite the opposite."
        za "It puts me at ease."
        scene a2009 with dssa
        za "But standing on that field and seeing people on the sideline makes me sweat."
        scene a2012 with dssa
        pause
        scene a2013 with dssa
        za "But I do miss it... I liked playing soccer with the girls."
        scene a2010 with dssa
        d "If you ever want to try it again... Bella's probably up for it."
        scene a2014 with dssa
        "She mumbles a few inaudible words."
    else:
        pass
    scene black with Dissolve(2)
    with Pause(.5)
    scene a2015 with dssr 
    pause 
    scene a2016 with dssa 
    pause 
    scene a2017 with dssa
    mi "*sighs* Good job, Mila."
    scene a2018 with dssr
    mi "You're on top of your game... You're the girl..."
    scene a2019 with dssa
    pause 
    scene a2020 with dssa
    mi "*Mumbles* I need to stop talking to myself."
    scene a2021 with dssr
    miri "Oh! Hi!"
    scene a2022 with dssa
    mi "Hey!"
    scene a2023 with dssa
    miri "I didn't know you were here, Mila!"
    if MilaSleep5x0 is True:
        mi "*Breathy* Yeah, I don't know what drove me to over an hour of cardio but I just had to get it out."
        scene a2025 with dssa
        miri "Can I make an educated guess?"
        miri "Did you have sex with [name]?"
        scene a2026 with dssa
        mi "Umm... no?"
        scene a2025 with dssa
        miri "And there we go."
        scene a2036 with dssr
        mi "How did you know?"
        scene a2037 with dssa
        miri "Zara mentioned you shared a bed."
        scene a2038 with dssa
        mi "Mhhh... I probably had to get some of that... sexual energy out of me."
        scene a2028 with dssr
        miri "I'm surprised you and [name] didn't do it... Is everything alright with him?"
        scene a2029 with dssa
        mi "*Lies* Oh yes. It was my fault... I was stupid and said something I shouldn't have."
        scene a2028 with dssa
        miri "What could you have possibly said that would turn a guy off from sleeping with you?"
        scene a2039 with dssr
        mi "[name]'s special... In a good way."
        scene a2040 with dssa
        miri "He's in the garden. Try again."
        scene a2041 with dssa
        mi "I'll have to go to work soon."
        scene a2030 with dssa
        miri "So? What's better than sex before work?"
        scene a2031 with dssa
        mi "Sex before, at, and after work?"
        scene a2032 with dssr
        "Miriam smiles."
    else:
        scene a2036 with dssr
        mi "Yeah, I had to let off some steam and did HIIT for an hour."
        scene a2037 with dssa
        miri "Your parents?"
        scene a2042 with dssa
        mi "Mhm."
        scene a2033 with dssr
        miri "You can always crash at ours or Kate's."
        scene a2032 with dssa
        mi "I know. Thanks."
    scene a2034 with dssr
    miri "I'll take the shower. I'll be fast."
    mi "Don't worry, I'll take the one upstairs."
    stop music fadeout 6
    scene a2035 with dssa
    pause 
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_MystyGood_R)
    scene a2043 with dssr
    pause
    scene a2044 with dssa
    pause 
    scene a2045 with dssr
    pause 
    scene a2046 with dssr
    pause
    scene a2047 with dssa
    pause 
    play sound "Music/Sfx/DoorOpen.ogg"
    scene a2048 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene a2050 with dssb
    pause
    scene a2051 with dssa
    d "Remind me to buy new swim shorts."
    scene a2049 with dssa
    za "You'll need them for our surfing competition!"
    if ZaraBBallTrust5x0 is True:
        scene a2052 with dssa
        za "Unless you want to do it nude."
    scene a2051 with dssa
    d "I need new clothes in general."
    if UmB is False:
        scene a2053 with dssa
        za "Vanessa told me she's going to take you shopping."
        scene a2054 with dssa
        d "She actually meant that?"
        scene a2055 with dssa
        za "Duh?"
        za "She always follows through."
        scene a2056 with dssa
        d "I'm not sure if I want to go shopping with her."
        scene a2055 with dssa
        za "Do it. It's a good way to get to know her better."
        scene a2057 with dssa
        d "Do I want that, though?"
        scene a2058 with dssa
        za "Considering that she's my favorite person in the world? I might be biased, but yes, you do."
        scene a2057 with dssa
        d "Your favorite?"
        scene a2059 with dssa
        za "She's always been there for me. Always."
        za "She's the best sister I could've wished for. She's always there to catch me, and doesn't hold back when I need to hear the harsh truth."
    else:
        scene a2053 with dssa
        za "I know a good shop where I bought my oars."
        scene a2060 with dssa
        if ZaraBBallTrust5x0 is True:
            za "We can go there together if you want."
        else:
            za "I'll give you the address."
    scene a2061 with dssr
    if MilaSleep5x0 or MilaDate is True:
        mi "Hey."
        scene a2062 with dssa
        za "Mila! I wondered where you went!"
        scene a2063 with dssa
        mi "I did a loooong session of cardio."
        scene a2064 with dssa
        za "That's awesome! I'm proud of you!"
        scene a2065 with dssr
        "Mila laughs."
        scene a2070 with dssr
        mi "May I?"
        d "Sure."
        scene a2071 with dssr
        pause 
        scene a2072 with dssa
        mi "You want to go shopping?"
        scene a2073 with dssa
        d "Why? Do you want to come with me?"
        scene a2074 with dssa
        mi "As a matter of fact, I do need new swimwear too."
        scene a2073 with dssa
        d "Alright. Let's do it together then."
        if MilaVenus4x5 is True:
            scene a2075 with dssr
            mi "Then you can also help me pick an outfit for my first Venus pictures..."
            scene a2077 with dssr
            d "You made your decision?"
            scene a2076 with dssa
            mi "I had some time to think on the treadmill."
            mi "...Of course, I had thought about it before..."
            scene a2078 with dssa
            mi "I mean, yeah..."
            mi "I've been looking for a way out of my shitty job for forever."
            scene a2079 with dssa
            d "And all it took was me telling you to do it?"
            scene a2080 with dssa
            mi "...The reason why I never went for it is that I fear social rejection."
            mi "But you're here. I'm not alone... With you, it sounds pretty fun."
            if ZaraBBallTrust5x0 is True:
                scene a2089 with dssr
                pause
        else:
            scene a2075 with dssr
            mi "I might have to try out a few..."
            mi "I'm gonna be naked a lot... and you'll have to guide me through it."
    else:
        mi "Hello there."
        scene a2062 with dssa
        za "Hey!"
        za "I had wondered where you went."
        scene a2063 with dssa
        mi "I did a loooong cardio session."
        scene a2064 with dssa
        za "I'm proud of you!"
        scene a2065 with dssr
        mi "Thanks again for letting me stay the night."
        scene a2066 with dssa
        za "Of course." 
        za "You're always welcome here."
        scene a2067 with dssa
        mi "Thank you."
        scene a2068 with dssa
        mi "Goodbye you two."
        d "Bye."
        za "Ciao!"
        jump CheetoGaming5x5
    scene a2081 with dssr
    mi "It's time for me to leave..."
    play sound "Music/Sfx/Slap.ogg"
    scene a2082 with hpunch
    mi  "I'm needed at the cafe and the tips aren't going to earn themselves."
    scene a2083 with dssa
    za "Goodbye Mila!"
    menu:
        "Ask her to show a little cleavage.":
            $ MilaCleavageS2_Ch1 = True
            scene a2084 with dssa
            d "How much do you earn just from the tips?"
            scene a2085 with dssr
            mi "About fifty bucks?"
            scene a2086 with dssa
            d "Show some cleavage, and every penny above fifty bucks we use to get dinner?"
            scene a2087 with dssa
            mi "You know what? Let's do it."
            if ZaraBBallTrust5x0 is True:
                scene a2088 with dssr
                pause 
                scene a2089 with dssa
            else:
                scene a2090 with dssr
                pause
        "Don't mention it.":
            scene a2090 with dssr
    d "I'll see you later."
    scene a2091 with dssa
    pause 
    scene a2092 with dssa
    d "I'll go take a nap."
    scene a2093 with dssa
    za "Have a good nap."
    scene a2094 with dssa
    pause 
    scene a2095 with dssa
    za "Where the hell is Miriam?"
    stop music fadeout 6
    scene black with Dissolve(2)
    with Pause(.5)
    jump CheetoGaming5x5


label CheetoGaming5x5: 
    scene a2098 with dssb
    pause
    $ play_playlist(playlist_MystyGood)
    scene a2099 with dssr
    pause 
    n "[name]?"
    d "Mhh?"
    scene a2100 with dssa
    n "Can I talk to you?"
    scene a2101 with dssa
    d "...Why?"
    d "*sleepy* You sound too serious."
    scene a2102 with dssa
    n "I uh... Never mind."
    d "Just say it. What's up?"
    scene a2103 with dssr
    pause
    scene a2104 with dssa
    n "...I'm thinking about signing up for tennis lessons."
    scene a2105 with dssa
    d "Okay?"
    d "I fail to see what made it so hard to talk about?"
    scene a2106 with dssa
    n "...Like- do you think I could still become good enough to make something out of it?"
    scene a2107 with dssa
    d "Like going pro?"
    scene a2108 with dssa
    n "I know it's stupid... I never really played it, while others have been at it since they were bibis."
    scene a2109 with dssa
    d "Don't let that stop you."
    scene a2110 with dssa
    n "I might be wasting my time and I hate being disappointed."
    scene a2111 with dssr
    d "Do you enjoy tennis?"
    scene a2112 with dssa
    n "Yes."
    scene a2111 with dssa
    d "Then it's not a waste. Go for it, Cheeto."
    d "And even if you don't become a pro, you still had a great time."
    scene a2113 with dssr
    n "True."
    scene a2114 with dssr
    pause
    scene a2115 with dssa
    d "Yo?"
    n "What?"
    scene a2116 with dssa
    d "What's this?"
    scene a2117 with dssr
    n "Ohhh maaaan!"
    scene a2118 with dssa
    n "We're back to this now?"
    play sound "Music/Sfx/Punch.ogg"
    scene a2119 with vpunch
    "You punch her shoulder."
    scene a2120 with vpunch
    n "Argh!" 
    scene a2121 with dssr
    n "You didn't hold back!"
    scene a2122 with dssr
    d "What are you up to?"
    scene a2123 with dssr
    n "I'll go to the ER to get my arm checked..."
    scene a2124 with dssa
    d "Or... We do something together?"
    scene a2125 with dssa
    n "Duuude!"
    scene a2126 with dssa
    n "Look! My arm!"
    scene a2127 with dssa
    with Pause(.5)
    play sound "Music/Sfx/PunchBibi.ogg"
    scene a2128 with vpunch
    d "..."
    scene a2129 with vpunch
    n "You thought you could fuck with me?"
    scene a2130 with vpunch
    n "ME?! BIG WIGGLY?!"
    scene a2131 with dssa 
    with Pause(.4) 
    play sound "Music/Sfx/Punch.ogg"
    scene a2133 with vpunch 
    pause
    if CheetoBath is True:
        scene a2134 with dssr
        n "Can I sleep here again tonight?"
        scene a2135 with dssa 
        d "It's better if you don't."
        scene a2136 with dssr 
        n "Alright... Straight to business..."
        scene a2137 with dssa 
        n "How do you want me?"
        scene a2138 with dssr 
        n "No?"
        scene a2139 with dssr 
        n "How about this?" 
        scene a2140 with dssr 
        pause 
        scene a2141 with dssa 
        pause 
        scene a2142 with dssa 
        n "N-nyo..."
        scene a2143 with dssa  
        pause 
        scene a2144 with dssa 
        pause
        scene a2146 with dssa 
        n "The title of the first guy to touch my pussy goes to you."
        scene a2147 with dssa 
        d "Do I get a crown?"
        scene a2148 with dssa 
        n "I'll get you one when we've had actual intercourse."
        scene a2147 with dssa 
        d "I'll hold you to that."
        scene a2149 with dssa 
        n "Are you feeling anything... down there?"
        scene a2150 with dssa 
        d "Nah."
        scene a2151 with dssa 
        n "But it worked at the lake, no?"
        n "He was hard there!"
        scene a2152 with dssa 
        d "No?"
        d "He had a small reaction but he wasn't even close to it."
        scene a2153 with vpunch 
        n "I was living a lie?!"
        scene a2154 with dssr
        pause 
        scene a2155 with dssa
        pause
        scene a2156 with dssr
        n "I will have to process this news..."
        d "Pull up your pants and we can cuddle a bit."
        scene a2157 with dssa #sfx 
        pause  
        scene a2158 with dssa   
        d "Didn't you forget something?"
        scene a2159 with dssa
        n "No."
        scene a2160 with dssr
        n "I noticed you and Zara are getting along well."
        scene a2161 with dssa
        d "Are you jealous?"
        scene a2160 with dssa
        n "A little."
        scene a2161 with dssa
        d "Zara's a bro."
        if BellaNonExclusive5x0 is True:
            $ Bella_NEX = True 
            scene a2162 with dssa
            n "You and Bella... That's still a thing, right?"
            scene a2163 with dssa
            d "Yeah."
            scene a2164 with dssa
            n "Could you break it off with her... and anyone else who might be there? Be exclusive with me?"
            scene a2165 with dssa
            d "Cheeto- I'm not sure if-"
        elif MilaDate is True:
            scene a2162 with dssa
            n "Now that uhh... We're here..."
            n "Could you break it off with her... and anyone else who might be there? Be exclusive with me?"
            scene a2165 with dssa
            d "Cheeto- I'm not sure if-"
        elif NiaDate5x0 is True:
            scene a2162 with dssa
            n "So... I heard from Nia that you wanted to go out with her..."
            n "That's not still planned, right?"
            scene a2163 with dssa
            d "It is."
            scene a2164 with dssa
            n "Could you break it off with her... and anyone else who might be there? Be exclusive with me?"
            scene a2165 with dssa
            d "Cheeto- I'm not sure if-"
        elif VicDate is True:
            scene a2162 with dssa
            n "You uhhh- still want to go out with Vic?"
            scene a2163 with dssa
            d "Yeah."
            scene a2162 with dssa
            n "Mhhh..."
            scene a2163 with dssa
            d "What?"
            scene a2164 with dssa
            n "Could you break it off with her... and anyone else who might be there? Be exclusive with me?"
            scene a2165 with dssa
            d "Cheeto, I don't think I can-"
        else:
            scene a2162 with dssa
            n "Sooo uhhh... are we a couple now?"
            n "Like exclusive?"
            scene a2165 with dssa
            d "I don't think that works right now."
        $ Nami_NEX = True 
        scene a2167 with dssa
        pause 
        scene a2168 with dssa
        n "Uhhh- is this here nothing but a fling for you?"
        scene a2169 with dssa
        d "I didn't say that."
        scene a2170 with dssa
        n "I know you've been out of the whole 'socializing' stuff for a while, but even you should know that no girl wants to be just one of many... At least not the ones with self-respect."
        scene a2169 with dssa
        d "I want to be close to you, but I can't have anything as serious as a real relationship right now."
        scene a2170 with dssa
        n "...I knew it."
        scene a2169 with dssa
        d "Shut up."
        scene a2172 with dssr
        n "I don't want to share you, dude!"
        scene a2171 with dssa
        d "Nami, I don't know who I really am."
        scene a2172 with dssa
        n "I was of the impression that when you kissed me the other night, you wanted more! That you wanted me!"
        scene a2173 with dssa
        d "I do, but I simply can't handle the mental logistics of a relationship right now."
        d "If you can't understand this, we shouldn't take this step at all."
        scene a2174 with dssa
        n "Wow! Relax!"
        scene a2176 with dssa
        pause 
        scene a2175 with dssa
        n "There is always a damn catch..."
        scene a2178 with dssa
        d "I'm sorry if that's not what you envisioned."
        scene a2177 with dssa
        n "I never... I didn't even think it was possible to get to this point at all..."
        n "I understand it... but man... I hate the thought of you doing someone else..."
        scene a2179 with dssr
        pause 
        scene a2180 with dssa
        n "I always thought my college years would be adventurous... Casual flings, experiencing life, going to parties..."
        n "But the moment it comes to you, I suddenly feel insanely jealous..."
        scene a2181 with dssa
        d "Cheeto... I know you. There's a real risk that after we've actually slept with each other, you lose all interest."
        scene a2180 with dssa
        n "I don't think so!"
        scene a2181 with dssa
        d "Can you promise me that? 100 percent?"
        scene a2182 with dssr
        pause 
        scene a2183 with dssa
        pause 
        scene a2184 with dssa
        d "Mhm."
        scene a2185 with dssa
        d "Nami, you don't know who you are either."
        d "I can't handle the expectations that come with exclusivity right now... and you won't be able to handle the guilt that would follow if you indeed lose interest along the way."
        scene a2187 with dssr
        pause
        scene a2186 with dssr 
        n "If you put it like that... it might be in my own interest not to jump the gun..."
        scene a2188 with dssa 
        d "You don't think straight when you're aroused. Leave the thinking to me."
        scene a2189 with dssa
        n "You think like a robot."
        n "We're humans. It's okay to think emotionally."
        scene a2190 with dssr
        pause 
        scene a2191 with dssa
        d "At some point in the future, we'll have to address our past."
        d "Otherwise there's always going to be this nuclear bomb in our garden that could go off at any time."
        scene a2192 with dssa
        pause 
        scene a2193 with dssa
        n "I like the status-quo. I like pretending that we were always cool."
        scene a2194 with dssa
        d "If we ever want to get to a point where we can be fully open with each other, no banned topics or the sort."
        d "We'll have to go through... the past."
        scene a2195 with dssa
        pause 
        scene a2196 with dssr 
        pause 
        scene a2199 with dssa
        pause 
        scene a2198 with dssa
        d "Let me take a small step..."
        d "Nami... Back then you made my life a living hell."
        scene a2199 with dssa 
        pause 
        scene a2200 with dssa 
        pause 
        scene a2201 with dssr
        n "...I know."
        scene black with Dissolve(2)
        with Pause(.5)
    else:
        scene a2134 with dssr
        pause 
        scene a2135 with dssa 
        d "So what's up? Are we gonna play something? Perhaps a quick board game?"
        scene a2138 with dssr
        n "Yeah."
        scene a2139 with dssr
        n "But let's not play with Noji. She's on my ass a lot lately."
        scene a2140 with dssr
        d "Alright. Any idea what games they have here?"
    stop music fadeout 2
    jump FirstAidCourse

label FirstAidCourse:
    scene a2202 with dssb
    if CheetoBath is False:
        n "Hmm..."
    else:
        pause
    scene a2210 with dssr 
    za "Heeey."
    za "Noji got us some cake. She's waiting by the pool."
    scene a2204 with dssr
    n "Cake..."
    scene a2203 with vpunch
    n "Ohhhhh yeaah! CAKE!"
    scene a2205 with dssr
    pause
    scene a2206 with vpunch
    d "Wait, wait..."
    d "...I don't trust it."
    scene a2207 with dssa
    n "What do you mean, you don't trust it?"
    scene a2206 with dssa
    d "I have a bad feeling about this."
    scene a2208 with dssa
    n "Dude! It's cake!"
    scene a2209 with dssr 
    pause 
    scene black with Dissolve(2)
    with Pause(.5)
    scene a2219 with vpunch
    play sound "Music/Sfx/Punch.ogg"
    with Pause(.4)
    d "I told you!"
    scene a2220 with vpunch
    n "I hate it!"
    scene a2211 with dssr 
    $ play_playlist(playlist_LK)
    pause
    scene a2212 with dssa 
    m "You know the drill."
    scene a2215 with dssr
    za "What's up?"
    scene a2216 with dssa
    n "Every five to six months we have to go through that stupid first aid course."
    scene a2217 with dssa
    za "I think, I have only done the one I needed for my driver's license."
    scene a2213 with dssr 
    m "I counted you in, Zara."
    scene a2218 with dssr
    za "Cool."
    scene a2221 with dssr 
    d "Not cool. It's annoying."
    scene a2222 with dssa 
    n "I hate the stupid puppets!"
    scene a2214 with dssr 
    m "About the puppets... They're in the quarantined house."
    scene a2223 with vpunch 
    n "YES!"
    scene a2224 with dssa 
    n "Did you hear that my boy?! No puppets!"
    scene a2225 with dssa 
    d "You know Noji. She'll improvise, and come up with something worse."
    scene a2226 with dssa 
    d "Maybe she'll make you the puppet."
    if RaceWithImpossibleOdds is True:
        $ NamiDate = True

    if NamiDate is True:
        scene a2227 with dssr 
        n "*Whispers* That would be a neat roleplay."
        n "*Whispers* One of us pretends to be a puppet and the other can go ham." 
    scene a2229 with dssr 
    m "We'll make pairs."
    scene a2228 with dssr 
    m "You and Zara."
    scene a2230 with dssa 
    m "I will be with you, [name]."
    scene a2231 with dssb
    pause
    scene a2232 with dssr
    pause
    scene a2233 with dssa
    m "What is first aid?"
    scene a2234 with dssa
    m "Nami."
    scene a2244 with dssr
    pause 
    scene a2245 with dssa
    n "...Man..."
    scene a2246 with dssa
    n "*Annoyed* First aid is the initial assistance given to someone that is injured or impaired."
    scene a2234 with dssr
    m "Very well."
    scene a2235 with dssr
    m "What are the priorities of first aid?"
    m "[name]?"
    scene a2236 with dssa
    d "...Preserve life."
    d "Alleviate suffering and prevent the condition from worsening."
    scene a2235 with dssa
    m "You forgot one."
    scene a2237 with dssa
    d "..."
    scene a2238 with dssa
    m "Promote recovery."
    za "What does 'Promote recovery' look like?"
    scene a2239 with dssr
    m "If someone is diabetic, you'd get them a drink if their blood sugar level is low, and so on."
    scene a2240 with dssr
    m "Come."
    scene a2241 with dssa
    d "Do I have to be the puppet?"
    scene a2242 with dssa
    m "You're not the puppet. I'll just show Nami and Zara what to do."
    scene a2243 with dssr
    m "You two watch us and then you will do the same with Nami, Zara."
    scene a2247 with dssr
    n "I'm usually not into watching but-..."
    scene a2250 with dssr
    pause
    scene a2248 with dssr
    n "...Sorry."
    scene a2249 with dssr
    za "Sure, we'll take notes."
    scene a2251 with dssr
    m "Lay down."
    scene a2252 with dssa
    pause
    scene a2253 with dssa
    m "First, I check for danger. Am I safe to proceed?"
    scene CheckForDanger
    pause 
    scene a2254 with dssa
    m "Then you check for a response."
    m "Talk into both ears in case there is any hearing impairment."
    scene a2255 with dssa
    m "Hello? Can you hear me?"
    scene a2256 with dssa
    m "Please open your eyes."
    scene a2257 with dssa
    za "*Whisper* She takes it very seriously."
    scene a2258 with dssa
    n "*Whisper* She has seen too many people die because nobody knew how to properly perform first aid."
    scene a2259 with dssr
    m "If you get no response, tap them slightly on the shoulder."
    scene a2260 with dssr
    m "Your shoulders are extremely tense, [name]. I'll look into that afterwards."
    scene a2261 with dssa
    m "Yell for help, make sure the emergency service is called at this point."
    scene a2262 with dssa
    m "Now we open the airway with the head chin tilt."
    scene a2263 with dssr
    m "One hand on the forehead, tips underneath the chin. Lift it back and check for breathing."
    scene a2264 with dssr
    m "Listen for breathing, try to feel their breath on your cheek, and look out for the rise of the chest."
    scene a2265 with dssr
    m "Now you do it on Nami, Zara."
    scene a2266 with dssr
    pause
    scene a2267 with dssr
    za "Uhh- I check for breathing, right?"
    scene a2268 with dssa
    m "First you check for danger, and then you call out."
    scene a2269 with dssr
    pause 
    scene a2270 with dssr
    m "Your turn, [name]."
    scene a2272 with dssr
    za "Hello? Nami?"
    za "There's some rolls waiting for you."
    scene a2271 with dssa
    n "*Quiet* Yo..."
    scene a2273 with dssa
    "Zara tries hard to contain her laughter."
    m "Now you tap her shoulder, Zara."
    scene a2274 with dssa
    za "Heeey... The rolls are still warm."
    play sound "Music/Sfx/StomachGrowl.ogg"
    scene a2275 with dssa
    "Nami's belly growls."
    scene a2276 with dssa
    "Zara bursts out laughing!"
    scene a2277 with vpunch
    n "Yo! First I got promised cake and now she's talking about rolls!"
    scene a2278 with dssa
    za "Stay dead."
    n "*Muffled* I wouldn't need first aid if I was dead!"
    scene a2279 with dssr
    pause
    scene a2280 with dssa
    d "Hello?"
    scene a2281 with dssa
    m "First you check for danger."
    scene a2284 with dssr
    "You check for danger..."
    scene a2282 with dssr
    d "Hello? Can you hear me?"
    scene a2280 with dssa
    d "*Mumbles* I'm glad you're not conscious or you'd hear how sick I am of this course."
    play sound "Music/Sfx/Slap.ogg"
    scene a2283 with vpunch
    pause
    scene a2285 with dssr
    "You tap her shoulders."
    scene a2286 with dssr
    "Then you check her for breathing."
    menu:
        "Place your hand on her upper abdomen.":
            $ NojiBelly = True
            scene a2287 with dssr
            pause
            scene a2288 with dssa
            "Your hand gently rises with her breath."
            scene a2289 with dssa
            m "Good."
            m "You think on your own."
            scene a2290 with dssr
            d "I thought it would add another potential indicator that someone might be breathing."
            scene a2291 with dssa
            m "Good effort."
            m "It's just important that you don't push down."
            scene a2292 with dssa
        "Don't do it.":
            scene a2292 with dssr
            pass
    pause
    scene a2293 with dssr
    m "How's it going, girls?"
    n "We did it all."
    scene a2294 with dssa
    m "Did she too, Zara?"
    scene a2295 with dssr
    za "Yup."
    scene a2296 with dssr
    m "Good."
    scene a2297 with dssa
    m "Then, let me show you the recovery position."
    scene a2298 with dssr
    m "First, you'll move the person's arm up."
    scene a2299 with dssa
    pause
    scene a2300 with dssa
    m "Then you'll check his pockets for something major. Make sure to get it out."
    scene a2309 with dssr
    n "I bet he has something 'major' in his pockets."
    scene a2301 with dssr
    m "If the person is wearing glasses, place the items near their head." 
    scene a2301 with dssa
    m "Place his hand against his cheek."
    scene a2302 with dssr
    m "Grab the outside of his leg and lift it as high as you can. This is your lever."
    scene a2303 with dssa
    m "And now you push him down firmly."
    scene a2304 with dssa
    m "Check for breathing again."
    m "..."
    scene a2306 with dssr
    m "..."
    scene a2305 with dssa
    m "Start breathing or I'll give you CPR."
    scene a2306 with dssa
    d "I was trying to die."
    scene a2305 with dssa
    m "Not with me around."
    scene a2307 with dssr
    m "If the casualty is a heavily pregnant lady. Place her towards the left side. It's safer for the baby and the lady."
    scene a2308 with dssa
    m "Please Zara, go ahead and put Nami into the recovery position."
    scene a2310 with dssr 
    pause
    scene a2311 with dssa
    pause 
    scene a2312 with dssr
    n "I'm no origami!"
    scene a2314 with dssr
    m "Check for breathing."
    scene a2313 with dssa
    za "Oh. Right."
    scene a2315 with dssr
    m "Your turn, [name]."
    scene a2316 with dssr
    pause
    scene a2317 with dssr
    pause
    scene a2318 with dssa
    m "What are you waiting for? Fold me."
    n "Oh! It's okay if you insinuate things but when I do it it's bad?!"
    scene a2319 with dssr
    m "Stop sexualizing everything I say, Nami."
    scene a2320 with dssa
    pause
    scene a2321 with dssa
    pause #sfx 
    scene a2322 with dssr
    pause
    scene a2323 with dssa
    pause
    scene a2324 with dssr
    d "Checked for breathing."
    m "Very well."
    scene a2325 with dssr
    pause
    scene a2326 with dssr
    m "Mmmhh..."
    scene a2327 with dssa
    m "Sadly, we do not have the infamous puppets."
    scene a2328 with dssr
    m "Meaning, I cannot show you proper CPR today."
    scene a2329 with dssa
    d "Thank god..."
    n "Doing CPR on those puppets feels like they're sucking back on your lips."
    d "And that disinfectant taste... Ugh."
    scene a2330 with vpunch
    m "Enough! The puppets have done a lot of work over the years."
    scene a2330a with dssr
    n "I'd kiss the butthole of a hooker before I touch the puppets again!"
    n "Or worse! I'd kiss Bella before I touch these Aids-puppets again!"
    scene a2331 with dssr
    m "You ungrateful people. Be quiet or I'll increase the frequency of these first-aid courses."
    scene a2332 with dssa 
    m "[name]."
    d "*Sighs*"
    scene a2333 with dssr 
    m "CPR."
    scene a2334 with dssa
    m "First you check for a response."
    play sound "Music/Sfx/Slap.ogg"
    scene a2335 with vpunch
    pause 
    scene a2336 with dssa
    m "Then you check for breathing... Head, chin tilt."
    scene a2337 with dssr
    m "The following is important."
    scene a2338 with dssa
    m "We check for normal breathing."
    m "Anything other than normal breathing we would start CPR."
    scene a2339 with dssa
    m "There's the medical term 'agonal gasp'."
    m "A throaty sound, and it occurs because the heart is no longer circulating oxygen-rich blood."
    scene a2340 with dssa
    n "I think that's what I get whenever we have to do this course."
    scene a2341 with vpunch
    m "If you don't want to be here, then go!"
    scene a2342 with dssa
    n "Really? I can leave?"
    scene a2343 with dssa
    m "No."
    scene a2344 with dssa 
    m "If there's blood or anything else that makes you question the situation... Wait until there's a pocket mask available."
    scene a2345 with dssa 
    m "But chest compressions are mandatory."
    m "We will skip the mouth to mouth part due to the unfortunate absence of the puppet."
    scene a2346 with dssa 
    m "Place yourself as close to the casualty as possible."
    scene a2347 with dssr 
    m "Place your palm right on the center of the chest. The heel of your hand right on the breast bone."
    m "Don't push on the sides of the chest."
    m "Link fingers with your other hand and put pressure right on the chest bone."
    scene a2348 with dssr
    m "To make it a little easier for you, your arm is in a straight line from the hand to the shoulder, then lock your shoulders in place and come straight down..."
    m "I will not press nearly as hard as you should, because it would injure [name]."
    scene a2349 with dssa 
    n "Do it."
    scene a2350 with dssa 
    n "Hehe."
    scene a2351 with dssa 
    m "Nami now you do it on Zara. Remember not to press down."
    scene a2352 with dssr 
    n "It was a bummer I couldn't kill the puppet with my brutal chest compressions."
    scene a2353 with dssr 
    m "Ready?"
    scene a2354 with dssr
    pause
    d "(The puppet didn't have boobs.)"
    scene a2373 with dssr
    n "Yo [name]?"
    n "The puppets didn't have boobs."
    scene a2354 with dssr
    d "I thought the exact same."
    scene a2355 with dssa
    m "You can't choose what gender the injured person might be."
    scene a2356 with dssa
    d "Where do I place my hands?"
    scene a2357 with dssa
    m "The same place as with a male."
    m "The breasts will fall slightly to the side and give access to the sternum."
    scene a2358 with dssa
    d "Here?"
    scene a2359 with dssa
    m "Yes."
    scene a2360 with dssa
    m "Don't be afraid to give women CPR! Their life is at stake!" 
    scene a2361 with dssa
    pause
    d "Yours don't really fall to the side."
    scene a2362 with dssa
    m "I had a boob job. They stay mostly in place, but it doesn't change anything."
    scene a2363 with dssa
    pause  
    scene a2364 with vpunch
    m "[name]! Don't be a coward when you perform CPR!"
    scene a2374 with dssr
    pause
    scene a2364 with dssr
    m "Get in there! Every second counts!"
    scene a2365 with dssa
    pause 
    scene a2366 with dssa
    m "Good, but maybe don't grab them like that."
    scene a2367 with dssa
    d "You said to go in there."
    scene a2368 with dssa
    m "With the heel of your palm."
    m "You're grabbing them like you're trying to take them with you."
    menu:
        "Release them from your grasp.":
            $ NojiBoob = False
            scene a2369 with dssa
            d "I'll just let the women die..."  
        "Keep going like this.":
            $ NojiBoob = True 
            scene a2370 with dssa
            d "They don't feel fake."
            scene a2371 with dssa
            m "Boob jobs have come a long way. You can barely tell the difference."
            scene a2370 with dssa
            d "Visually, maybe."
            scene a2371 with dssa
            m "No, that's only because I chose this shape."
            scene a2372 with dssa
            m "As long as they go for a natural tear shape, you can't tell the real and fake ones apart."
    scene a2375 with dssr
    m "When you give CPR to a woman, maybe try to stay above her top."
    scene a2376 with dssa
    d "I can't care about this in an emergency... Especially not with a top that has a big cleavage."
    scene a2377 with dssa
    m "That's what I wanted to hear."
    scene a2378 with dssa
    m "I repeat it for everyone! Every second of first aid counts!"
    m "Assess the situation, and if you don't face any hazards, perform first aid!"
    m "Don't be afraid to break a few ribs during CPR! Most people don't use enough force!"
    scene a2379 with dssr
    m "Everything went well, Zara?"
    scene a2380 with dssa
    za "Yes."
    scene a2379 with dssa
    m "Great."
    m "Usually I'd show you more, but the puppets are unavailable."
    scene a2381 with dssa
    n "The infant puppet..."
    scene a2382 with dssa
    d "The child puppet is much creepier."
    scene a2383 with dssr
    d "And don't you say they're not creepy, Noji."
    d "I remember you squeaking because of the puppet in the corner."
    scene a2384 with dssa
    m "They can be unsettling in the wrong light."
    scene a2385 with dssa
    m "We will continue the course when we have the puppets."
    m "Next time together with Nick and Vanessa."
    scene a2379 with dssr
    m "Thank you for your time."
    scene a2386 with dssr
    pause
    scene a2387 with dssa
    m "Do you want a massage? I have an hour."
    stop music fadeout 7
    scene a2388 with dssa
    d "Yeah."
    scene black with Dissolve(2)
    with Pause(.5)
    jump NojikoMassage5x5


label NojikoMassage5x5:
    $ play_playlist(playlist_NojiMedi)
    scene a727 with dssb
    pause
    scene a728 with dssr
    pause
    scene a729 with dssa
    m "I don't have my usual oils and therefore, not your favorite one either... But I have my massage shirt."
    scene a731 with dssa
    d "I never noticed you had a special massage shirt."
    scene a730 with dssa
    m "Every massage I've given you or Nami has been with this shirt."
    scene a731 with dssa
    d "I forgot about your OCD."
    scene a730 with dssa
    m "I like to feel free, but I obviously can't give you a massage nude."
    scene a732 with dssr
    d "Technically you can, but it wouldn't be appropriate."
    scene a733 with dssa
    m "Exactly. This isn't a massage shop that offers happy ends."
    scene a734 with dssa
    m "Nami always gives me a chuckle."
    scene a735 with dssa
    d "Nami laughs about the word penis."
    d "You also make that joke every time."
    scene a736 with dssa
    m "And everyone at least gives me a chuckle... mostly out of pity, but I'll take what I can get."
    scene a737 with dssr
    m "I found two oils in Vanessa's bathroom."
    scene a738 with dssa
    d "Do you have something almond-based?"
    m "...No. I don't think so."
    d "What do you have there?"
    m "I think... No, it's massage oil... I think."
    d "What's it called?"
    scene a739 with dssa
    m "I have these two."
    scene a740 with dssa
    d "Let's go with..."
    call screen MassageChoice
    pause

label MassageChoice_Completed:
    scene a741 with dssa
    if LiquidSex is True:
        "She covers her hands with Liquid Sex."
    elif OrgasmOil is True:
        "She covers her hands with the Orgasm massage oil."
    scene a742 with dssa
    "She climbs up on the table."
    m "I can't properly massage you otherwise. This table is too wide."
    scene a743 with dssr
    d "It's fine."
    d "The oil feels nice."
    scene a744 with dssa
    if OrgasmOil is True:
        m "It's silky... Thicker than normal massage oil."
    else:
        m "It feels great on the hand as well."
    scene a743 with dssa
    d "(I love massages... Except that one time where the Cheeto tried it... It felt like some tree branch ravaging over my back.)"
    scene a745 with dssa
    d "Why do you always have your eyes closed when massaging?"
    scene a746 with dssa
    m "During a massage, I see with my hands. Not my eyes."
    m "I'm almost done with the body scan... You're very tense pretty much everywhere."
    scene a747 with dssa
    m "I assume it's due to the uprooting we've experienced over the past couple of days. Then the college, the girls and everything."
    scene a818 with dssa
    d "I guess."
    scene a819 with dssa
    m "...Those ngh- tensions sit deep."
    scene a820 with dssa
    m "As always, voice your thoughts. If I'm too rough, tell me."
    scene a821 with dssr
    d "Did I ever say you're too rough?"
    scene a822 with dssa
    m "You haven't yet, but pain tolerance can change on a daily basis."
    scene a821 with dssa
    d "So just get in there."
    scene a823 with dssa
    m "As you wish."
    scene a824 with dssa
    d "It's just a little less comfortable without the head-hole."
    scene a825 with dssa
    m "I'll ask Nick for a real massage table."
    scene a826 with dssa
    pause
    scene a827 with dssa
    m "Okay, let's start from the top."
    "She firmly massages the lower part of your head."
    scene a828 with dssa
    d "...I like that part."
    m "I know."
    scene a829 with dssa
    m "And you hate the thighs."
    d "I don't hate it... but it hurts."
    scene a830 with dssa
    m "And it's going to hurt today... You've been more tense than usual."
    m "Hmm, your jaw is tense."
    m "Have you been grinding your teeth?"
    d "No."
    "Her soft fingers and the slightly silky massage oil feel heavenly on your cheeks."
    scene a832 with dssa
    "With one swift motion she slides her hand down your cheeks towards your chest."
    scene a923 with dssa
    pause
    m "Do you want to do the back or the front first?"
    d "Let's do the front."
    menu:
        "Tell her to stay on top if needed.":
            $ NojiOnTop = True
            d "You can just stay on top."
            m "Are you sure?"
            d "Yes."
            scene a832 with dssa
            m "The table is too wide, and my arms are a little too short."
            pause
            scene a923 with dssa
            pause
            d "Nh..."
            m "Mh? Everything okay?"
            d "That felt weird... I don't remember you doing that before."
            scene a924 with dssr
            m "For this I need to be on top."
            scene a925 with dssa
            "You let out a loud exhale."
            d "That felt weirdly good."
            scene a926 with dssa
            m "Up here I can apply some different techniques. Usually, this hurts during the first times, but you seem to be responding quite well."
            scene a925 with dssa
            d "How many secret techniques have you hidden from us?"
            scene a927 with dssr
            m "A few."
            m "There's a lot of different techniques. Be it with your knees, feet or elbows."
            m "...Some would just be extremely inappropriate and are best used in a couple."
            scene a928 with dssa
            d "I see."
            stop music fadeout 8
            if LiquidSex is False:
                scene a929 with dssa
                "She applies some pressure and slightly moves her hand down your chest..."
            else:
                scene a929 with dssa
                "She applies some pressure and slightly moves her hand down your chest."
                jump MassageContinue1x0
            play sound "Music/Sfx/Slimey_Slide1.ogg"
            scene a930 with vpunch
            "- And her hands slip away."
            play sound "Music/Sfx/Punch.ogg"
            scene a931 with vpunch
            d "Nha..."
            scene a932 with dssr
            m "Oh my god!"
            play sound "Music/Sfx/Slimey_Slide4.ogg"
            scene a933 with dssa
            "Her slippery hands struggle to find traction anywhere."
            play sound "Music/Sfx/Punch.ogg"
            scene a934 with vpunch
            pause
            scene a935 with dssa
            "You try to help her by pushing her back forwards, but all it accomplishes is raising her shirt."
            d "*Slightly muffled* Are you okay?"
            scene a936 with dssr
            m "I- don't know what's- My hands-"
            play sound "Music/Sfx/Slimey_Slide3.ogg"
            scene a937 with dssa
            "She tries to get up again but her limbs slip away on the slippery surface."
            play sound "Music/Sfx/Punch.ogg"
            scene a938 with vpunch
            m "Are you okay [name]?"
            d "I'll hold your legs and you raise your upper body?"
            m "Okay!"
            "She draws the strength from her lower back and shoots back up while you hold her legs in place."
            $ play_playlist(playlist_Girly)
            play sound "Music/Sfx/Slimey_Slide4.ogg"
            scene a1140 with dssr
            pause
            m "Everything okay? Did I hurt you?"
            scene a1142 with dssr
            pause
            scene a1141 with dssa
            d "Nah, I'm okay."
            scene a1143 with dssa
            pause
            scene a1162 with dssr
            d "...I thought you didn't give happy ends."
            scene a1163 with vpunch
            "Nojiko bursts out laughing."
            scene a1164 with dssa
            m "I'd expect Nami to say something like this, but you caught me off guard."
            scene a1165 with dssr
            "Noji sighs."
            d "What?"
            m "The bottle we used says massage oil and lube."
            m "No wonder its consistency was so thick."
            m "I'm sorry, [name]."
            scene a1167 with dssr
            d "It's okay."
            scene a1166 with dssa
            pause
            scene a1168 with dssa
            d "Now I'm totally tense again."
            play sound "Music/Sfx/Slimey_Slide1.ogg"
            scene a1169 with vpunch
            pause
            scene a1170 with dssa
            m "We need to get this lube off us. We'll then use the other one."
            m "There's a little bathroom right around the corner."
            scene black with Dissolve(2)
            with Pause(.5)
            jump NojiBathroomLube
        "Don't tell her that.":
            m "The table is a little wide for my arms."
            m "I won't be able to do the usual."
            d "It's okay."
            jump MassageContinue1x0



label NojiBathroomLube:
    scene a1171 with dssr
    m "No wonder you thought I was giving out happy ends."
    m "My top went completely see-through."
    scene a1172 with dssa
    pause
    scene a1173 with dssa
    pause
    scene a1174 with dssr
    d "At least the stuff smells good."
    scene a1175 with dssa
    pause
    scene a1176 with dssa
    pause
    scene a1177 with dssa
    m "Do you remember to check your testicles on a semi-regular basis?"
    scene a1178 with dssa
    d "Yeah."
    scene a1177 with dssa
    m "Good."
    scene a1179 with dssa
    d "I wonder if you do that with Nick too."
    scene a1180 with dssa
    m "What?"
    scene a1179 with dssa
    d "Remind him of all sorts of medical checkups when he's wearing his birthday suit."
    scene a1181 with dssa
    m "I'd be lying if I said no."
    m "It's a good habit to have."
    scene a1182 with dssa
    pause
    scene a1183 with dssa
    m "Hmm."
    scene a1184 with dssa
    pause
    scene a1185 with dssa
    d "...The moles are okay."
    scene a1187 with dssa
    m "How would you know?"
    scene a1188 with dssa
    d "How would you know? You're not a dermatologist."
    scene a1189 with dssa
    m "I have seen my fair share of interesting looking moles during my time as a general practitioner."
    d "*Sigh*"
    scene a1190 with dssa
    pause
    scene a1191 with dssa
    m "Hmhmmmm... Yeah, it's fine."
    d "Your poor boyfriends."
    stop music fadeout 5
    scene a1192 with slideright
    pause
    scene a1193 with dssa
    m "Shall we continue?"
    $ play_playlist(playlist_NojiMedi)
    menu:
        "Inquire about her past.":
            $ NojiPastS2_1x0 = True
            scene a1194 with dssa
            d "May I ask you something?"
            scene a1195 with dssa
            m "Of course."
            scene a1196 with dssa
            d "I don't remember you dating anyone before Nick."
            d "Was there ever anyone?"
            scene a1197 with dssa
            m "As you know I was very busy."
            m "I didn't find the time for dating."
            scene a1198 with dssa
            d "So you were a nun for the past decades?"
            scene a1199 with dssa
            pause
            scene a1200 with dssa
            m "What do you think?"
            scene a1199 with dssa
            d "Nami and I speculated about it."
            scene a1200 with dssa
            m "I figured."
            scene a1201 with dssa
            m "What do you think?"
            scene a1202 with dssr
            d "Well, I thought you held back and suffered from it."
            scene a1203 with dssa
            m "And what did Nami think?"
            scene a1204 with dssa
            d "It's Nami. What do you think she thought?"
            scene a1205 with dssa
            m "What did she think? I'm actually curious."
            scene a1207 with dssa
            d "Let me just skip over the insane ones and give you the easier to swallow ones."
            d "In her words, not mine... She thinks you have lots of casual flings with your co-workers and sneak out the house at night."
            scene a1208 with dssr
            pause
            scene a1209 with dssa
            m "The truth is somewhere in the middle, with a tendency towards your version."
            m "I stayed away from personal relationships that could make things too complicated."
            scene a1211 with dssa
            m "However, I didn't live like a nun. I had casual partners."
            scene a1212 with dssa
            d "Wait... I remember this one guy... We saw him at the lake with you."
            scene a1211 with dssa
            m "Yes."
            scene a1212 with dssa
            d "I remember that Nami and I liked him. He was cool."
            scene a1213 with dssa
            m "Yes, but he wanted a serious relationship, I didn't."
            scene a1214 with dssa
            d "Well, I guess Nick was cool enough to get you to commit."
            scene a1215 with dssr
            "She switches off the overhead light."
            scene a1216 with dssa
            m "I don't know why I always lie to myself... and now to you."
            scene a1217 with dssa
            d "(Not the first time.)"
            d "I can't follow."
            scene a1218 with dssa
            m "I said I didn't want to complicate things by getting into a relationship."
            m "But the truth is..."
            scene a1219 with dssa
            m "I'm not made for relationships... I think."
            scene a1220 with dssr
            pause
            scene a1221 with dssa
            m "To be honest, I don't know what to think."
            scene a1222 with dssr
            pause
            scene a1223 with dssa
            d "I'm all ears."
            scene a1224 with dssa
            m "[name], I'm not wearing any pants..."
            scene a1223 with dssa
            d "I had your ass on my face a few minutes ago. I think we'll be okay."
            scene a1225 with vpunch
            m "Don't say that!"
            scene a1226 with dssa
            d "It's true, though."
            scene a1227 with dssa
            m "Doesn't mean you have to say it out loud."
            scene a1229 with dssr
            d "If it's not said out loud, it didn't happen?"
            scene a1228 with dssa
            m "No, but if for example Nami heard it, we would never hear the end."
            scene a1230 with dssa
            d "True."
            d "Tell me what you meant earlier before I tell Nami about it."
            scene a1231 with dssa
            m "I've never had a serious relationship in my life, [name]."
            m "And everyone always told me that getting married, having children, is the way it should be."
            m "But it felt so against my nature. I didn't like the idea of being with someone forever..."
            scene a1232 with dssa
            pause
            scene a1233 with dssa
            m "Was I in the wrong for never wanting it? Was I-"
            m "Was I missing out on something? Was I just confused?"
            scene a1234 with dssr
            d "And then you met Nick and gave it a shot?"
            scene a1235 with dssa
            m "I've given it half-hearted shots but I've always taken the first exit."
            scene a1234 with dssa
            d "I think you just never found the one that made it click."
            d "Nick must be special."
            scene a1236 with dssa
            m "He is."
            scene a1237 with dssa
            m "Nick didn't have much luck with his ex-wife."
            scene a1238 with dssa
            d "Zara told me that she cheated on him."
            scene a1237 with dssa
            m "Besides other things."
            if InfZaraMom is True:
                $ NojiZaraTrustS2_1x0 = True
                scene a1238 with dssa
                d "The framing?"
                scene a1237 with dssa
                m "Wow. Zara told you a lot. I'm glad you trust each other that much."
                m "Yes, the framing."
            m "It left him deeply wounded and with some serious trust issues."
            scene a1239 with dssa
            m "He's been unable to really trust another woman since the incident. He and I work because we don't exclusively commit to each other."
            m "However, Nick and I are obviously more than just occasional lovers... We have an open relationship with the potential to go closed someday..."
            m "He can't cope with the potential issues that can arise in a monogamous relationship and it took him years of therapy to get over what happened with his ex wife."
            m "The way it is right now, it works. In this arrangement, we can trust each other and there's no jealousy."
            scene a1240 with dssa
            m "His mind is at ease, and I don't feel like suffocating."
            d "I don't think moving in here was part of the plan."
            scene a1241 with dssr
            m "It certainly wasn't... But I couldn't just think about what I wanted."
            m "Sure, the state would've provided you with housing but-"
            scene a1242 with dssa
            d "Would you have moved here if Nami and I had already moved out?"
            scene a1241 with dssr
            m "For a night, maybe... But I would've stayed at Emilia's."
            menu:
                "I always have a room for you.":
                    $ NojiRoom = True
                    scene a1244 with dssr
                    m "*Laughs* Do you?"
                    m "Would I be living in a dorm room?"
                    scene a1243 with dssa
                    d "Yeah."
                    d "Or in this case; a room in a student house."
                    scene a1245 with dssa
                    "She laughs and shakes her head."
                    m "A doctor who graduated at the top of her class, who, after 11 years of practicing, returns to living in a student room..."
                    m "If it ever comes to that,put me down, [name]."
                "Nami and I wouldn't let you sleep in a hotel.":
                    scene a1244 with dssa
                    m "That's nice of you."
                    m "I know I can always count on you two."
            scene a1258b with dssr
            m "Why are you holding me like this?"
            scene a1259b with dssa
            d "What do you mean? I hear pity in your voice."
            scene a1260b with dssa
            m "There's a tension in your arms I haven't felt in a while. You usually do this during times of great unrest."
            scene a1393 with dssr
            m "Is everything okay at college?"
            scene a1395 with dssa
            d "Everything's okay."
            scene a1393 with dssa
            m "I'm not a psychologist... Perhaps a hobby psychologist, and if I had to put it into words, I would call myself an anchor on which you are holding on."
            scene a1395 with dssa
            d "It feels safe. I can't touch anyone else like this without there being an unwanted side effect."
            scene a1394 with dssr
            m "Do you have an example?"
            d "If I touch Nami like this it becomes weird."
            m "As it should."
            scene a1393 with dssr
            d "I don't mind the same level of contact with her."
            play sound "Music/Sfx/Punch.ogg"
            scene a1397 with vpunch
            m "But you shouldn't."
            scene a1398 with dssa
            d "We'll tackle that topic another day."
            scene a1399 with dssa
            d "(I had to test her. Apparently it's okay with her but not with Nami? I don't want to ruin the mood, but I'll address it in the near future.)"
            scene a1400 with dssa
            d "(But first I have to put Amber on the spot. If I ask Noji about it, she'll tell Amber and I might never get the full truth.)"
            scene a1401 with dssr
            m "There's nothing to tackle."
            scene a1402 with dssr
            d "(An opportunity to get to the truth will present itself eventually.)"
            d "(I have to lighten the mood. Topic change.)"
            scene a1403 with dssa
            d "This house has so many bathrooms."
            scene a1404 with dssr
            m "I'm very grateful to Nick that he allowed us to stay here. Zara and Vanessa have been so welcoming to us."
            m "But I need to find my own place."
            scene a1405 with dssr #EXTRA
            show screen Extra_Lewd_CH1_Noji_1 with dssa
            d "I can help you look."
            hide screen Extra_Lewd_CH1_Noji_1
            scene a1406 with dssa #EXTRA
            show screen Extra_Lewd_CH1_Noji_2 with dssa
            m "I've talked to my friend Emilia. A friend of hers is moving out of her small apartment and I can have it."
            hide screen Extra_Lewd_CH1_Noji_2
            scene a1405 with dssa
            d "What about your house?"
            scene a1407 with dssa
            m "I-"
            scene a1408 with dssa
            m "I'm glad I'm out of the house, [name]."
            m "I needed a change of scenery."
            scene a1409 with dssa
            m "And now I dread going back."
            scene a1410 with dssa
            pause
            scene a1411 with dssa
            m "But for once it's nice not having to do anything in the house... a house that barely stands on its own."
            scene a1413 with dssa
            d "I thought doctors earned a lot. Why is there such a money struggle?"
            scene a1412 with dssa
            m "I still have debts to pay off."
            scene a1413 with dssa
            d "I hope you didn't pay for me to go to ZPR... I could've gone to a free, public college."
            d "You've always been a big sister-figure for me."
            d "You don't need to hold back on your own."
            scene a1414 with dssa
            m "You and Nami had already been scouted by ZPR. Besides Schwartz, there's no college even remotely on the same level."
            scene a1413 with dssa
            d "I see..."
            d "Nami and I are about to get jobs. We can probably pay it ourselves."
            scene a1415 with dssa
            m "I think it makes more sense if you focus on building a financial base. From there you'll learn how to handle and invest money."
            m "If you work just to pay the tuition, you won't have time nor money to enjoy extracurricular activities."
            scene a1416 with dssa
            d "I guess that's what Mila must feel like."
            scene a1415 with dssa
            m "By what I heard, she's got an academic scholarship. She pays 30 percent of her tuition."
            scene a1417 with dssr
            d "Where did you hear that?"
            scene a1418 with dssa
            m "I talk to people."
            scene a1417 with dssa
            d "What people?"
            scene a1419 with dssa
            m "People people."
            scene a1420 with dssa
            d "..."
            scene a1421 with dssr
            d "Maybe I can get something going with Basketball."
            scene a1422 with dssa
            m "I'm glad you decided to give it a go again. You're so talented."
            m "You looked like I put you on the spot with the whole open relationship topic?"
            scene a1424 with dssa
            d "A little."
            menu:
                "Is this why you never had children?":
                    $ Noji_Children = True 
                    d "I hope I'm not crossing any boundaries here."
                    scene a1425 with dssa
                    m "I think we've crossed quite a few today."
                    scene a1424 with dssa
                    d "I'm not allowed to make jokes but you are?"
                    scene a1425 with dssa
                    m "You got it."
                    scene a1426 with dssa
                    m "Yeah, I never wanted kids but... something may have changed."
                    scene a1427 with dssr
                    d "You're what? 38?"
                    m "Yes."
                    d "I'm no doctor b-"
                    scene a1428 with dssa
                    m "Yes, I could still get pregnant."
                    scene a1429 with dssa
                    m "I'm still capable of conceiving a child the normal way without any aid." 
                    m "I'm not in a rush and thanks to modern medicine I can wait a few more years."
                    scene a1430 with dssa
                    pause 
                    scene a1431 with dssa
                    m "I just have never had the time for children. I'm always at work."
                "Don't ask her that.":
                    scene a1430 with dssr
                    pause 
            scene a1432 with dssa
            d "This has to stay between us."
            scene a1433 with dssa
            m "It does? Why?"
            scene a1434 with dssa
            d "If the Cheeto finds out you have an open relationship, she'll never let me live that down."
            scene a1435 with dssa
            "Nojiko chuckles."
            if Sanitized is False:
                menu:
                    "Voice an interest in open relationships.":
                        $ Open_Relationship = True 
                        scene a1436 with dssa
                        d "How do you even make an open relationship work?"
                        d "I guess you need the same values... but still... Don't you get jealous?"
                        scene a1437 with dssa
                        m "I think the moment you're not even a little bit jealous, you're not really in love with the person."
                        m "You handle jealousy just like every other bad emotion."
                        m "But with a partner that understands you, someone who shares your values will not put you into a position where jealousy becomes an issue."
                        scene a1438 with dssa
                        m "The really good part about an open relationship is that you learn fast who's capable of emotional honesty. There's no room for games when you're juggling hearts."
                        m "Why are you asking?"
                        scene a1439 with dssa
                        d "Just curious."
                        scene a1440 with dssa
                        if len(Dating_List) >3:
                            m "You've voiced your interest in a few girls... and you may have realized that you probably can't date multiple girls at once?"
                            scene a1441 with dssa
                            d "Well... I didn't think they would be sooo 'pushy' about actually wanting to meet up."
                            scene a1443 with dssa
                            m "'Pushy'... [name], you can't compare your state of mind to theirs. You avoid connection. Most people seek it."
                            scene a1444 with dssa
                            d "I've noticed that. I'm cool with not meeting up for a few weeks or months..."
                            scene a1446 with dssa
                            m "*Chuckles* If you tell someone you want to get to know them, you're on a timer."
                        if BellaNonExclusive5x0 is True:
                            scene a1445 with dssa
                            m "What's going on with you and Bella?"
                            m "By what I could gather at the breakfast table, you aren't a couple."
                            scene a1444 with dssa
                            d "We decided to be non exclusive but... I think we only pretend it is."
                            scene a1445 with dssa
                            m "Do you want it to be open between you and Bella?"
                            scene a1444 with dssa
                            d "I don't know..."
                            scene a1446 with dssa
                            m "Just... don't say anything one sided. This is an emotionally charged topic."
                        scene a1447 with dssa
                        m "If there is a time in your life to try it out, it's during college."
                        m "Experiment while the stakes are low."
                        scene a1448 with dssa
                        d "I'd risk losing someone I like."
                        scene a1449 with dssa
                        m "The world is full of people we can grow to like."
                        m "What I meant was a wife, a stable home or kids."
                        m "Then you really got something to lose."
                        scene a1450 with dssr
                        m "But 80 percent of the relationships you see right now won't make it through college."
                        m "And half of them that break up will eventually make up."
                        m "You will make mistakes. It's inevitable. You'll learn from them and grow as a person."
                        scene a1451 with dssr
                        m "But if you find a great girl that touches your soul, don't let her go."
                        m "As long as you're honest you can almost always make up eventually."
                        scene a1452 with dssa
                        d "You're speaking from experience?"
                        scene a1453 with dssa
                        m "I do."
                        scene a1454 with dssa
                        m "I've made my fair share of mistakes, but I can proudly say that during my time in college, I lived life to the fullest."
                        m "There's not one day where I regret it."
                        m "Okay... Perhaps, I regret the day I met the Zanes."
                    "Don't voice an interest.":
                        pass
            scene a1455 with dssr
            d "I always knew you weren't a typical nun. No nun has your tattoos."
            d "You often act conservative, but we know you got a past."
            d "And sometimes you slip."
            scene a1456 with dssa
            m "When do I slip, huh?"
            scene a1457 with dssa
            d "Just now, when was the last time you were wearing strings and didn't immediately cover up?"
            scene a1458 with dssa
            m "I've always worn strings."
            m "I'm not a grandma, [name]."
            scene a1459 with dssa
            d "I wasn't judging."
            scene a1458 with dssr
            m "I'm just trying to set a good example."
            scene a1459 with dssr
            d "That's what this is all about?"
            scene a1460 with dssa
            m "Between Nami, you, and me, I'm by far the oldest in the house. I have to set an example."
            scene a1461 with dssa
            d "Nami needs more than an example... Maybe another shrink."
            play sound "Music/Sfx/Slap.ogg"
            scene a1462 with vpunch
            m "Hey!"
            scene a1463 with dssr
            d "Maybe you being out of the house might also have something to do with it."
            scene a1464 with dssa
            pause 
            scene a1465 with dssa
            m "It does... I feel invigorated. I feel alive again."
            m "But maybe I have become a little too comfortable."
            scene a1466 with dssa
            menu:
                "It can't hurt to cover up a little more.":
                    $ Noji_Comfortable_Underwear = False 
                    scene a1467 with dssa
                    m "I agree."
                    m "And it seems like I did set an example. Very nice."
                "You should feel comfortable.":
                    $ Noji_Comfortable_Underwear = True 
                    $ Bets_Insider_Knowledge_Noji = True 
                    scene a1468 with dssa
                    d "We don't want to tell you how to be, and you shouldn't change the way you live because of the expectations of others." 
                    scene a1469 with dssa
                    m "I agree with the first part, but we're a social species. We'll have to adjust to the social norms around us."
                    m "I know Nami doesn't mind if I'm not fully covered, I wasn't so sure about you." 
                    scene a1470 with dssa
                    d "We usually don't talk about these things."
                    d "But have I ever complained?"
                    scene a1469 with dssa
                    m "With Nami, you do."
                    scene a1468 with dssa
                    d "Yeah, that's because the Cheeto teases me."
                    menu:
                        "Tease her.":
                            d "After you sat on my face, you now belong to the naughty list too."
                            scene a1463 with dssa
                            "She just looks at you... Slightly tense."
                        "Don't.":
                            pass 
                    scene a1471 with dssa
                    m "Do you want to go back to status quo? I can cover up."
                    scene a1472 with dssa
                    d "No, I think I know you better now. Be yourself." 
                    scene a1473 with dssa
                    pause
                    scene a1474 with dssa
                    d "Also, I now have access to insider knowledge. This gives me an edge when Nami and I make bets about you."
            scene a1475 with dssr 
            d "Getting back to you sometimes slipping..."
            scene a1476 with dssa
            d "When you think you're alone and you're on the phone with, I think, Emilia, you swear a lot."
            d "I had to double check once to see if it was actually you."
            scene a1477 with dssr
            d "But to me all of this doesn't matter... You're still Nami's and my angel."
            scene a1478 with dssa
            m "I think that's the sweetest thing you've ever said."
            if BellaNonExclusive5x0 is True:
                scene a1480 with dssa
                m "I hope you say these things to Bella too."
                scene a1481 with dssa
                d "Hell no."
                d "You, I like. Bella I just..."
                scene a1482 with dssa
                m "Stop it! Bella's great."
                scene a1484 with dssa
                d "You have no idea how she is."
                scene a1485 with dssa
                m "Maybe- but... She seems nice."
                scene a1484 with dssa
                d "(Liar. You probably know exactly how Bella is.)"
            else:
                scene a1477 with dssa
                d "Don't get used to it."
                scene a1479 with dssa
                m "I guess this has to do for the time being."
            scene a1486 with dssr
            d "Considering how 'open minded' you apparently are... Why are you so weird with me and Nami?"
            scene a1487 with dssa
            m "I can't follow."
            scene a1488 with dssa
            d "You go on the barricades whenever the Cheeto and I are in the bathroom together."
            d "The Cheeto and I aren't related, nor are we bound by a contract so-"
            scene a1489 with dssa
            m "It's complicated."
            m "If you want to know more, ask Nami. I've explained it to her."
            scene a1490 with dssa
            d "You did?"
            scene a1491 with dssr
            m "I know you two don't talk about the past, but you have to stop blaming me."
            scene a1492 with dssa
            d "Why did you tell me now? Did you tell her recently?"
            scene a1493 with dssa
            m "No. Years ago."
            m "But it's Nami, and Nami likes to push boundaries."
            scene a1494 with vpunch
            m "Now do you want the massage or not?!"
            scene a1495 with dssa
            d "Yeah." 
            scene a1496 with dssa
            m "Then apologize."
            scene a1497 with dssa
            d "Or... I'll tell Nami about your accident with the lube-oil and you'll have to suffer through years of bad jokes."
            scene a1498 with dssa
            m "The massage is on the house."       
        "Don't ask her about her past.":
            scene a1199 with dssr 
            pause 
            scene a1200 with dssa
            m "Come. The massage awaits."
    jump MassageContinue1x0


label MassageContinue1x0:
    scene a1499 with dssr
    pause
    scene a1500 with dssa
    "Around twenty minutes into the massage you have trouble staying awake."
    menu:
        "Voice an interest in learning to massage.":
            $ MC_Massage_S2_1 = True
            scene a1501 with dssr
            d "Is it hard to learn to massage?"
            m "It takes a while to 'see' with your hands but as soon as you got that down, it's not hard."
            m "Why? Do you want to learn it?"
            scene a1502 with dssa
            if BellaNonExclusive5x0 is True:
                d "I guess Bella would like it."
                m "Definitely. If a man can massage, a woman will melt in his hands."
            elif MilaSleep5x0 is True:
                d "I think Mila would like it."
                m "I bet she would. It's a very useful skill for a relationship."
            elif VicDate or VicDateEntry2 is True:
                d "Victoria would love it."
                m "It might also benefit her recovery."
            d "Can you teach me?"
            scene a1503 with dssr
            m "Technically I could, but I don't have time."
            m "The studio where I learned might still be around. I'll check it later."
            scene a1504 with dssa 
            m "I find massaging very relaxing... it puts me at ease and into a meditative state."
            m "You'll like it."
        "I have no interest in it.":
            scene a1501 with dssr
            pause
    scene a1505 with dssb
    pause 
    scene a1506 with dssr
    stop music fadeout 8
    "With you asleep, Noji quietly leaves the room."
    scene a1507 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    play ambient "Music/Sfx/Ambient_Night_Suburban2.ogg" fadein 4
    scene a1508 with Dissolve(4)
    pause
    "A distant, sensual voice echoes through your mind..."
    scene a1509 with dssa
    "With every passing second, the voice becomes clearer..."
    scene a1510 with dssa
    pause
    scene a1511 with dssr 
    pause 
    scene a1512 with dssr
    pause 
    scene a1513 with dssa
    va "Dinner is ready."
    scene a1514 with dssr
    "You flop back onto the table and sigh."
    scene a1515 with dssa
    pause 
    scene a1516 with dssr
    d "..."
    scene a1517 with dssa
    if LiquidSex is False:
        va "You smell like orgasm..."
    else:
        va "Is that Liquid Sex I smell?"
    va "You used my oil?"
    scene a1516 with dssa
    play music "Music/BibiFi/Mark Fabian - Slow Momentum.ogg" fadein 4
    d "Mhm... I hope you don't mind."
    scene a1518 with dssr
    va "I told Noji she could use my oils while her hands were spoiling me the other day."
    va "She's very skilled with her hands... A part of me wished she'd offer happy ends."
    scene a1520 with dssa
    d "That's your father's girlfriend."
    scene a1521 with dssa
    va "Even better."
    scene a1519 with dssa
    va "I, too, know how to massage."
    va "If you pay me, I'll spoil you."
    scene a1520 with dssa
    d "I'm good."
    scene a1521 with dssa
    va "Are you afraid?"
    scene a1522 with dssa
    d "I don't want your finger in my ass."
    scene a1521 with dssa
    va "I can give you a prostate massage if you wish."
    scene a1523 with dssa
    d "...Vanessa, have you ever attended a seminar for sexual harassment?"
    scene a1524 with dssa
    va "Why would I?"
    scene a1525 with dssr
    va "Do you think I'm harassing you by offering to massage your prostate?"
    scene a1526 with dssa
    d "Yes."
    scene a1525 with dssa
    va "You can just say no."
    scene a1527 with dssr
    d "No. I don't want you to massage my prostate."
    va "See. That wasn't so hard."
    scene a1528 with dssr
    pause
    scene a1529 with dssa
    va "It's your own insecurity and inability to handle the situation."
    va "People get all flustered... They start stuttering because society pressures them into thinking in boxes... *Gasps* What would the others think..."
    scene a1530 with dssa
    va "Yet... their mind begins to wander... Would it feel good?"
    play sound "Music/Sfx/Punch.ogg"
    scene a1531 with vpunch
    va "*Whispers* Would I enjoy her finger in my ass?"
    va "*Whispers* Is society and the pressure it puts on me keeping me away from fulfilling my deepest needs?"
    scene a1532 with dssa
    va "*Sensual* ...My wants? Everything I desire?"
    scene a1533 with dssa
    d "Am I actually still asleep and in the midst of the worst fever dream I've ever had?!"
    scene a1535 with dssa
    va "Someday you'll be brave enough to admit it to yourself."
    va "Even you desire to be touched... To be held."
    scene a1534 with dssa
    d "There's difference between the stuff you're saying and just being held."
    scene a1536 with dssa
    va "Do you want me to hold you?"
    scene a1537 with dssa
    menu:
        "Okay.":
            $ NessiHoldingS2Ch1 = True
            scene a1538 with dssa
            d "...Okay."
            scene a1539 with dssr
            pause
            scene a1540 with dssa
            "She scratches your head... and her body radiates warmth and care. Something you didn't expect her to be capable of."
            scene a1541 with dssa
            va "You deserve to be the little spoon once in a while."
            scene a1542 with dssr
            pause
        "No.":
            scene a1543 with dssa
            va "As you wish."
            scene a1544 with dssa
            pause
            if KateNetwork5x5 is True:
                scene a1545 with dssa
                d "I need to ask you something."
                scene a1546 with dssr
                va "Okay."
                scene a1547 with dssa
                d "Have you heard of the creeps that take photos of students?"
                scene a1548 with dssa
                va "I have."
                scene a1549 with dssa
                d "Some girl at ZPR said that your boyfriend might be involved."
                scene a1550 with dssa
                va "That's not true."
                scene a1551 with dssa
                d "Are you sure?"
                scene a1552 with vpunch
                va "Don't question my judgement."
                scene a1553 with dssa
                va "I know him."
                scene a1554 with dssa
                pause 
    stop music fadeout 3
    scene black with Dissolve(2)
    with Pause(.5)
    jump AbendessenCH1



label AbendessenCH1:
    stop ambient
    $ play_playlist(playlist_LK_R)
    scene a1555 with dssb 
    pause 
    if ZaraBBallTrust5x0 is True:
        scene a1556 with dssa
        pause
    scene a1557 with dssa
    pause 
    scene a1558 with dssr
    va "You look beautiful today."
    scene a1559 with dssa
    za "Thank you."
    scene a1565 with dssr
    nic "How was your first night, [name]?"
    scene a1568 with dssr
    d "It was good."
    d "It felt... light."
    scene a1560 with dssr
    va "You left a lot of baggage behind. The time here will do you good."
    scene a1561 with dssa
    va "All of you."
    scene a1566 with dssa
    nic "Here. Try this one. It's my special. Made with iced tea."
    scene a1567 with dssa
    d "Thanks."
    scene a1562 with dssa
    nic "Noji? You sent me a text about some sort of a puppet? I wasn't sure what you meant."
    scene a1563 with vpunch
    n "No! Don't get her new puppets!"
    scene a1564 with dssa
    m "Yes, I need it for the first aid course."
    nic "Sure. Just show me later what you mean."
    scene a1569 with dssr
    pause
    scene a1570 with dssr
    m "Zara? I answered the phone a few hours ago and the Stiffes airport called."
    scene a1571 with dssa
    za "What did they want?"
    scene a1570 with dssa
    m "There were some open questions about your plane."
    scene a1572 with dssa
    m "I told them you'd call them back."
    scene a1573 with dssa
    za "Thanks. I'll do it tomorrow."
    scene a1574 with dssa
    n "Is there anything wrong with it?"
    scene a1574a with dssa
    za "Ehhh- it got some issues. The motor likes to turn off mid-flight."
    scene a1575 with dssa
    n "What?!"
    scene a1577 with dssa
    za "I managed to land it safely."
    scene a1576 with dssa
    n "Maaaan... I hate heights."
    scene a1578 with dssa
    d "Since when?"
    scene a1579 with dssr
    n "Always have!"
    n "Remember when we went on the Ferris wheel?"
    scene a1580 with dssa
    d "You said you were cold."
    scene a1581 with dssa
    n "I was frozen in shock! I was in sheer terror!"
    n "I even peed myself a little when it stopped abruptly."
    scene a1582 with dssa
    d "Huh. Bibi."
    scene a1583 with dssr
    va "...What did you just call her?"
    scene a1584 with dssa
    d "A bibi."
    scene a1585 with dssr
    pause
    scene a1586 with dssa
    va "Pizza for dinner... That's new."
    scene a1587 with dssa
    nic "I didn't have time to cook."
    scene a1588 with dssr
    n "You don't like pizza?"
    scene a1589 with dssa
    va "I do. But I also like to keep my figure."
    scene a1590 with dssr
    n "You look amazing."
    scene a1591 with dssa
    va "Because I pay attention to what I eat."
    scene a1592 with dssa
    n "I should go on a diet."
    scene a1593 with dssa
    pause 
    scene a1594 with dssr
    va "You look great the way you are."
    scene a1595 with dssa
    n "But I'm still unhealthy."
    scene a1596 with dssr
    va "Zara can help you develop a healthier eating regimen. But do it to maintain your current weight."
    scene a1597 with dssa
    n "Have you seen my butt?"
    scene a1598 with dssr
    va "Hard to overlook."
    scene a1602 with vpunch
    n "YO!"
    scene a1599 with dssa
    va "I mean this in a positive way."
    scene a1600 with dssa
    va "But you should visit the gym more. You don't want your body to sag eventually."
    scene a1601 with dssa
    za "Nami, you and [name] should stay here. There's a gym and everything you can wish for!"
    scene a1603 with dssr
    "The Cheeto doesn't know what to say and just smiles awkwardly."
    scene a1604 with dssa
    va "Maybe cut back on some bread rolls and replace them-"
    scene a1605 with dssa
    n "I'd rather set myself on fire."
    n "The rolls are the most important thing in my life."
    scene a1606 with dssa
    va "I see."
    scene a1607 with dssa
    za "I'll help you Nami. I've written plenty of nutrition plans for friends."
    scene a1608 with dssa
    n "Thank you. But I will not tolerate bread roll discrimination."
    scene a1609 with dssa
    d "Yet we have to tolerate you."
    scene a1610 with dssa
    n "You're on thin ice."
    n "And you know what happens if you're on thin ice with me."
    scene a1611 with dssa
    n "Ask Julia."
    scene a1612 with dssr
    za "Who was Julia?"
    scene a1613 with dssa
    n "A classmate of mine in middle school..."
    scene a1614 with dssa
    n "I remember her like it was yesterday-"
    scene a1615 with dssa
    n "-and what she did to me."
    scene a1616 with dssa
    pause 
    scene a1615 with dssa
    n "She said I was 'a little much'"
    scene a1617 with dssa
    n "So I created a fake class survey and made a friend share with her that she was voted the most forgettable."
    scene a1624a with dssr
    za "Ouch."
    scene a1618 with dssr
    d "She did much worse to others."
    scene a1619 with dssa
    n "I did not!"
    scene a1620 with dssa
    d "What about the time some girl said that not everything's about you."
    scene a1619 with dssa
    n "I don't remember that."
    scene a1620 with dssa
    d "You told me what you did."
    scene a1621a with dssa
    n "Whatever you say next is a lie."
    scene a1625a with dssr
    za "What did she do?"
    scene a1626a with dssa
    d "She started crying and acted all scared whenever the girl came close."
    scene a1627a with dssa
    d "You said she'd been written up for hostile behavior, parents got involved, and she had to sit in the corner for the rest of the year."
    scene a1622a with dssr
    n "You're trying to paint me in a bad light... Classic [name] behavior." 
    n "Just like what the croissants did."
    scene a1628a with dssr
    za "The what now?"
    scene a1629a with dssr
    m "Don't ask her anything about so called 'Bread roll history'."
    scene a1630a with dssa
    n "Why'd you want to keep the truth from them, Noji? Mmmh?"
    scene a1631a with dssa
    m "Nami... Please don't"
    scene a1632a with dssr
    d "She's a croissant racist."
    scene a1633a with dssa
    n "I WILL never accept them as legitimate bread."
    scene a1634a with dssa
    n "Because of them, millions of little bread rolls were never even baked."
    n "A systematic soft bread cleansing took place in 1969!"
    scene a2389 with dssr
    n "Humble rolls were shoved into old storage units while sExY flakiness took the spotlight!"
    scene a2390 with vpunch
    n "Bibi rolls killed in their dough-cribs!"
    scene a2391 with dssa
    pause 
    scene a2392 with dssa
    n "I will talk to Miss Marla, the Dean or the president himself, to get rolls back on the menu in the school cafeteria!"
    scene a2393 with dssa
    n "For your information... I'm working on a small documentary about the siege of Butter Lake."
    n "Hundreds of savage croissants swept in at night and thousands of innocent, cute dinner rolls, still in the warm oven, were devoured in silence."
    scene a2394 with vpunch
    n "Yeah!"
    scene a2395 with dssa
    n "I also saw the classified videos of what happened in 1922... That poppy seed roll held on for dear life b-but-"
    scene a2396 with dssa
    n "I- I can't speak about it- sorry." 
    scene a2397 with dssa
    pause 
    scene a2398 with dssa
    n "I'll never forgive the French..."
    scene a2399 with dssa
    pause
    scene a2400 with dssa 
    n "Can I have a piece of that pizza, please?"
    scene a2402 with dssr
    pause 
    scene a2410 with dssr
    va "You are an interesting character, Nami." 
    scene a2411 with dssa
    d "Interesting is one way to put it."
    scene a2401 with dssr
    n "*mumbles* Thin ice, [name]... Thin ice."
    scene a2403 with dssr
    nic "Nami and I played tennis this morning."
    nic "She's really good for someone who hasn't seriously played before."
    scene a2412 with dssr
    va "I agree. She's got talent."
    scene a2414 with dssa
    m "Well, do you want to take lessons?"
    n "I'd like to but it's expensive."
    scene a2415 with dssa
    d "What about that snob club... Where they play golf."
    scene a2413 with dssr
    va "The Petrova country club?"
    scene a2416 with dssa
    d "I think so."
    d "Amber said that she could get us in there."
    scene a2421 with dssr
    za "That's where I play too."
    scene a2422 with dssa
    n "You're all members there?"
    scene a2423 with dssa
    za "Dad knows the Petrova's."
    scene a2405 with dssr
    d "How good do you know them?"
    scene a2404 with dssr
    nic "They're friends of friends. We've crossed paths." 
    scene a2406 with dssa
    nic "I'll tell you what."
    scene a2407 with dssa
    nic "I'm pretty busy this week, but we'll all go to the country club next week."
    nic "We'll have dinner there and you can check out the place."
    scene a2424 with dssr
    n "That would be so cool."
    scene a2425 with dssr
    m "We should first-"
    scene a2417 with dssr
    d "Yes, that would be great Nick."
    scene a2418 with dssa
    d "(You're not getting out of this Noji.)"
    scene a2419 with dssr
    nic "Great. I'll let you all know the details."
    scene a2420 with dssa
    pause 
    if MilaDate is True:
        scene a2409 with dssa
        nic "And why don't you bring Mila, [name]?"
        scene a2408 with dssa
        d "Yeah, I'll do that."
    else:
        scene a2409 with dssa
        nic "And why don't you bring Mila, Nami?"
        scene a2408 with dssa
        n "Right... She likes golf. I'll bring her."
    stop music fadeout 10
    scene black with Dissolve(2)
    with Pause(.5)
    jump NamiEveningCH1



label NamiEveningCH1:
    play ambient "Music/Sfx/Summer_Morning.ogg"
    scene a2426 with dssb 
    pause 
    scene a2427 with dssa
    d "Yo."
    scene a2428 with dssa
    n "Yo."
    scene a2429 with dssr
    d "Wanna hang out?"
    scene a2430 with dssa
    n "...Sure."
    scene a2431 with dssa
    pause
    scene a2432 with dssr
    n "What do you want?"
    scene a2433 with dssa
    d "I don't want anything."
    scene a2432 with dssa
    n "Oh yeah? You're asking me to hang out without wanting anything?"
    scene a2433 with dssa
    d "I'd like for you to be quiet."
    scene a2434 with dssa
    pause 
    scene a2435 with dssr
    n "Have you heard the newest rumor?"
    d "I don't gossip."
    n "There's a guy in the cafeteria who apparently had sex with a meatball."
    scene a2437 with vpunch
    d "...Dude?!"
    scene a2436 with dssa
    n "What? It's what they're saying!"
    scene a2438 with dssa
    pause
    scene a2439 with dssa
    n "There's a local food festival soon."
    scene a2440 with dssa
    n "...You know what I thought about?"
    scene a2439 with dssa
    n "Baking my own rolls."
    scene a2441 with dssa
    d "I'm surprised you haven't thought of that before."
    scene a2442 with dssa
    n "As you know, I'm extremely lazy."
    n "I like eating them, not making them..."
    scene a2443 with dssr
    n "*Sigh* However, I've noticed a steady decline in roll quality."
    scene a2444 with dssa
    d "Ugh... I remember that stupid chart about the sesame decline you made last year..." 
    scene a2443 with dssa
    n "I think a new hero in the world of the rolls is needed."
    scene a2444 with dssa
    if NiaVisit5x0 is True:
        d "Nia likes to bake. Maybe she can give you some pointers."
        scene a2445 with dssa
        n "Oh really? Damn, I didn't know that."
        n "I'll ask her."
    else:
        pass
    if NojiPastS2_1x0 is True:
        scene a2446 with dssa
        d "...So listen."
        d "I talked to Noji during the massage."
        scene a2447 with dssa
        n "How was the massage?"
        n "The last ones she gave me she really went in there... It almost hurt..."
        scene a2448 with vpunch
        n "What am I saying? IT DID HURT!"
        if OrgasmOil is True:
            scene a2449 with dssa
            d "I think she offers some new services now."
            scene a2450 with dssa
            n "Like what?"
            scene a2449 with dssa
            d "Forget it."
        scene a2451 with dssa
        d "Anyways, I asked about us... Why she's so against you and me ever being more."
        scene a2452 with dssa
        n "It's because she's stuck up and got it into her head that-"
        scene a2453 with dssa
        d "- She told me, that she told you why." 
        scene a2454 with dssa
        pause 
        scene a2455 with dssa
        n "Yo, she's lying."
        scene a2454 with dssa
        pause 
        scene a2456 with dssa
        n "I can't believe she backstabbed me like that."
        scene a2457 with dssa
        n "*sigh* You remember who my parents were, right?"
        d "No."
        scene a2456 with dssa
        n "...Revera?"
        d "It rings a bell."
        scene a2458 with dssa
        n "You might've noticed that I never went to the Department of Child and Families?"
        scene a2459 with dssa
        d "Well, yeah. I know that an aunt of yours is your legal guardian."
        d "In my case it's the state. Well, it was until I turned 18."
        scene a2460 with dssa
        d "I'll probably need to go there soon... I should've opened their letters."
        scene a2461 with dssa
        n "Yeah... There's some rules. Noji knows about them, and I never cared to listen but in short: It's tradition that they find me a husband."
        n "If that gets broken, I don't get my trust fund and Nojiko might get in trouble."
        scene a2462 with dssr
        d "What does Noji have to do with it?"
        scene a2463 with dssa
        n "No idea. Maybe she promised to put me on the right path?"
        scene a2462 with dssa
        d "Why didn't she just tell me that?"
        scene a2464 with dssa
        n "Because you're like me! If someone tells us we're not allowed to do something! We want it even more..."
        scene a2463 with dssa
        n "And then you might potentially like me for the wrong reasons."
        scene a2466 with dssr
        d "..."
        n "What? I gave it to you straight."
        scene a2465 with dssa
        d "Why did you never say anything?"
        scene a2466 with dssa
        n "You know exactly why." 
        scene a2467 with dssa
        d "I don't!"
        scene a2468 with dssa
        pause 
        scene a2469 with dssa
        d "Are you interested in me? Like actually?"
        scene a2470 with dssa
        n "That's what I was talking about."
        scene a2471 with dssr 
        pause 
        scene a2472 with dssa
        d "It explains your behavior... The phases where you were highly affectionate towards me followed by coldness and days of barely talking to each other."
        if RaceWithImpossibleOdds is True:
            d "Maybe you don't really like me romantically. Maybe you just get a kick from pushing boundaries."
        scene a2474 with vpunch
        n "This is exactly why I kept it to myself! I knew you would go there!" 
        scene a2473 with dssa
        d "Can you blame me?"
        scene a2475 with dssa
        n "No... But it insults me." 
        scene a2476 with dssa
        pause 
        scene a2477 with dssa
        d "Revera was a name on the college, right?"
        scene a2478 with dssr
        n "Yeah."
        n "That's the stupid reason, I had to go to that book club."
        scene a2479 with dssa
        n "Noji wanted to introduce me."
        n "What she didn't anticipate was that this Katie would show up."
        scene a2480 with dssa
        pause 
        scene a2481 with dssa
        n "She invited me over for dinner next week." 
        scene a2482 with dssa
        d "What does she have to do with it?"
        scene a2479 with dssa
        n "I don't know, man."
        scene a2483 with dssa
        d "What about your sibling? You have that sister, right?"
        scene a2484 with dssa
        pause 
        scene a2485 with dssr
        pause 
        scene a2486 with dssa
        n "You know I do and you know what we agreed upon."
        scene a2487 with dssa
        n "We don't talk about the past."
        scene a2489 with dssa
        pause 
        scene a2488 with dssa
        d "Eventually, I'll have to work through it."
        scene a2490 with dssa
        n "You don't. You're not going to live forever, just push it down until one of us dies."
        scene a2491 with dssr 
        "Silence falls over you."
        scene a2492 with dssa
        d "You want me to lighten the mood?"
        scene a2493 with dssa
        n "You can't. You ruined it."
        scene a2494 with dssa
        stop ambient fadeout 5
        $ play_playlist(playlist_Girly)
        d "Noji and Nick have an open relationship."
        scene a2495 with dssa
        pause
        scene a2496 with dssa
        n "You're shitting me, right?"
        scene a2495 with dssa
        "You just look at her."
        play sound "Music/Sfx/Punch.ogg"
        scene a2497 with vpunch
        n "No?! Seriously?"
        scene a2498 with dssr
        d "Yeah, she told me that she's not the type for a monogamous relationship."
        scene a2499 with vpunch
        n "I was right all along?"
        scene a2500 with dssa
        n "All those years?!"
        scene a2501 with dssa
        d "That's not the important part-"
        scene a2502 with vpunch
        n "Oh it is!"
        n "Who cares about us!"
        play sound "Music/Sfx/Slap.ogg"
        scene a2503 with vpunch
        n "But ME being RIGHT all along!"
        scene a2504 with dssa
        n "I knew it!"
        scene a2505 with vpunch
        n "Tell me everything!" 
        scene a2506 with dssa
        d "Nope."
        scene a2505 with vpunch
        n "I NEED TO KNOW!" 
        scene a2507 with dssr 
        n "The chances of her having a sex tape just went up by 3.9 percent!"
        scene a2508 with dssa 
        d "Last time you said it was a 100 percent."
        scene a2509 with dssa 
        n "Yeah! Now it's a 103.9 percent!" 
        scene a2510 with dssa 
        n "Which means there is a chance for more than one!"
        scene a2511 with dssa 
        pause 
        scene a2512 with dssa 
        n "I have an idea."
        scene a2513 with dssa 
        d "I hate the tone in your voice. Whatever you say- No."
        scene a2514 with dssa 
        n "Hehe."
        scene a2512 with dssa 
        n "Let's check her phone for images."
        scene a2516 with dssr
        d "No you dumb weirdo! Show her some respect."
        scene a2515 with dssa 
        pause 
        scene a2517 with dssa 
        n "You're right. It was stupid."
        scene NamiAugli 
        pause
        scene a2519 with dssa 
        d "I have seen her pretty much fully nude."
        scene a2520 with dssa 
        n "So have I."
        n "But I haven't seen her in the act... If you know what I mean."
        scene a2521 with dssa
        d "And why do you want to?"
        scene a2522 with dssa
        n "If you know the person doing the porn, it hits different."
        scene a2523 with dssr
        d "Don't do it."
        scene a2524 with dssa
        n "I won't."
        scene a2523 with dssa
        d "I'll warn Noji."
        scene a2524 with dssa
        n "If you do that, I'll tell Vanessa you liked her idea of a relationship."
        scene a2525 with dssr
        pause 
        scene a2527 with dssa
        d "Have I told you that Vanessa invited me on a double date?"
        scene a2526 with dssa
        n "Why does everyone like you?! Why does no one like me?!"
        scene a2528 with dssa
        d "I'm just more interesting than you."
        scene a2529 with dssa
        n "Wow!"
        scene a2530 with dssa
        d "It's pity. They don't actually like me."
        scene a2531 with dssa
        n "Who are you taking there?"
        scene a2532 with dssa
        n "And just as a heads up, if you dare to ask me... I can't go with you." 
        scene a2533 with dssa
        d "How so?"
        scene a2532 with dssa
        n "Vanessa knows who I am, and I don't want to risk it."
        scene a2533 with dssa
        d "Risk getting Noji in trouble?"
        scene a2534 with vpunch
        n "Losing ma money! I want that trust fund! I wonder how much is in it..."
        scene a2535 with dssa
        d "Vanessa explicitly told you she knew?"
        scene a2536 with dssa
        n "She came by and forced a conversation on me."
        scene a2537 with dssa
        pause
        scene a2538 with dssa
        n "So, who are you taking?"
        if ZaraVanessaDate5x5 is True:
            scene a2540 with dssa
            d "Perhaps Zara."
            scene a2541 with dssa
            n "..."
        else:
            scene a2539 with dssa
            d "I haven't decided yet."
        if BellaNonExclusive5x0 is True:
            scene a2542 with dssa
            d "Vanessa wants me to take Bella."
            scene a2543 with dssa
            pause #eww 
        if RaceWithImpossibleOdds is True:
            scene a2544 with dssa 
            d "So... you could lose access to your trust fund if they found out about you and me?"
        else:
            d "So... you could lose access to your trust fund if they thought we had something?"
        scene a2545 with dssa 
        n "I think so. Not entirely sure but this is how it sounded."
        scene a2547 with dssa 
        d "Then why are you risking all this?"
        scene a2546 with vpunch 
        n "Do you really think BIG WIGGLY can be intimidated!?"
        n "You tell me not to do something AND I'LL FUCKING DO IT!"
        scene a2548 with vpunch 
        n "AND AFTERWARD, I'LL DO IT AGAIN!" 
        scene a2549 with dssr 
        n "...But yes. I really want the money."
        scene a2550 with dssa 
        d "When do you get it?"
        scene a2549 with dssa 
        n "When I'm 21 and married."
        scene a2550 with dssa 
        d "Married?"
        scene a2551 with dssa 
        n "This Katie seems to know a bit. I'll ask her when I see her at that diner."
        n "Perhaps, I can find a way around it."
        scene a2552 with dssa 
        d "Two more years."
        if RaceWithImpossibleOdds is True:
            scene a2553 with dssa 
            n "Mhm, afterwards, you and I can fuck in public."
        scene a2554 with dssr
        pause 
    scene a2555 with dssa
    n "When I start baking rolls, you better prepare your belly for some thick loads. You're gonna be swallowing a lot."
    scene a2556 with dssa
    n "...Like, it's going to be a mess."
    n "I'm not sure if you can handle a crunchy roll's girth."
    scene a2557 with dssa
    d "Shut up."
    scene a2558 with dssa
    n "You, Mila and Robin will be the jury for my rolls."
    scene a2559 with dssa
    d "No way."
    scene a2560 with dssa
    d "You can't handle criticism."
    scene a2561 with vpunch
    n "*High pitched* What?!"
    n "I totally can!"
    scene a2562 with dssa
    d "You take things way too personal."
    scene a2563 with dssa
    n "New house. New me."
    scene a2562 with dssa
    d "Sure."
    scene a2564 with dssr
    va "May I join?"
    scene a2565 with dssa
    n "Sure!"
    scene a2566 with dssa
    va "I heard the word girth."
    scene a2567 with dssa
    d "*Mumbles* Of course..."
    scene a2568 with dssa
    n "I'm going to bake some thick, penis-shaped rolls."
    scene a2569 with dssa
    va "That's great."
    scene a2570 with dssa
    va "I have a small gathering here next week, I'd love some baked goods in the shape of a penis and vulva."
    scene a2568 with dssa
    n "You know what? You can count on me!"
    scene a2571 with dssr
    va "Do you have a bikini with you, Nami?"
    scene a2572 with dssa
    n "Yeah, I do."
    scene a2571 with dssa
    va "I'd like to see you in it."
    scene a2572 with dssa
    n "Should I go sexy or... 'sexy'?"
    scene a2573 with dssa
    va "What do you think I'd like to see?"
    stop music fadeout 8
    scene a2574 with dssa
    n "I gotcha."
    scene a2575 with dssa
    pause 
    scene a2576 with dssr
    $ play_playlist(playlist_MystyGood)
    d "You have an upcoming gathering?"
    scene a2577 with dssa
    va "Indeed. A small party." 
    va "You and Nami are of course invited."
    scene a2578 with dssr
    va "However, I must warn you... There's going to be a serious surplus in girls."
    scene a2579 with dssa
    d "Is your boyfriend coming?"
    scene a2578 with dssa
    va "Of course."
    scene a2580 with dssr
    d "Anyone I might know?"
    scene a2581 with dssr
    va "Adriana Zane, Kelly, Sasha Petrova, Anna."
    va "They were at the book club."
    scene a2582 with dssa
    d "I remember."
    if AnnaSTG2 is True:
        d "(Anna gave me her number... Maybe I'll write her soon. Just not today.)"
    scene a2583 with dssa
    va "I'm not sure if you know anyone else."
    scene a2584 with dssr
    va "Oh, of course. Mila."
    scene a2585 with dssa
    d "You invited Mila?"
    scene a2584 with dssa
    va "I will soon. I haven't yet."
    scene a2586 with dssr
    d "Why?"
    scene a2587 with dssa 
    va "I like her."
    scene a2588 with dssa 
    d "Don't corrupt her."
    scene a2587 with dssa 
    va "I don't need to. She already is."
    va "She just doesn't know it yet."
    scene a2589 with dssa 
    d "You know your boyfriend sued her, right?"
    scene a2590 with dssa 
    va "Yes, but it was all a misunderstanding."
    scene a2591 with dssr 
    va "I'd very much like a threesome with her, my boyfriend, and me."
    if MilaDate is True:
        scene a2592 with dssa
        d "I'm kind of dating her."
        scene a2593 with dssa 
        va "Oh."
        va "I wasn't aware of that."
        va "I'm surprised someone like you would take on someone like her."
        scene a2592 with dssa
        d "...What's that supposed to mean?"
        scene a2594 with dssa 
        va "She's pure sex. You still have some things to work through."
        va "It might be a little early for you to mount this one."
        scene a2595 with dssr
        va "But if you're dating her..."
        scene a2596 with dssa
        va "Hmm, no... I don't want to sleep with you. So switching partners for an evening isn't an option for me."
        if Open_Relationship or MilaVenus4x5 is True:
            scene a2597 with dssa
            va "Would you mind giving us Mila for a night?"
            scene a2598 with dssa
            with Pause(.2)
            menu:
                "No. Not while I'm dating her.":
                    $ Vanessa_Sharing_Mila = False 
                    scene a2600 with dssa
                    va "A real shame."
                    va "I guess I'll have to wait until she's single again."
                    scene a2599 with dssa
                    d "If she becomes single again."
                "You have to ask her. Not me.":
                    $ Vanessa_Sharing_Mila = True  
                    scene a2600 with dssa
                    va "But would you give us your blessing?"
                    scene a2599 with dssa
                    d "Yeah, I guess? I don't own her nor is she my girlfriend."
                    d "I doubt she'll say yes, though. She doesn't like Mario at all."
                    scene a2601 with dssr
                    pause 
                    d "What?"
        else:
            pass 
    else:
        scene a2599 with dssa
        d "Good luck with that."
    scene a2602 with dssa
    d "You're at Schwartz... What do you know about Melanie Ceril?"
    scene a2603 with dssa
    va "Nothing."
    scene a2602 with dssa
    d "You do know her."
    scene a2603 with dssa
    va "I might've seen her around, but I can't put a name on her."
    scene a2602 with dssa
    d "Zara knows her."
    scene a2604 with dssa
    va "Good for Zara."
    scene a2605 with dssa
    d "(Why doesn't she want to give me any info?)"
    scene a2606 with dssr
    n "On a scale from Raisin roll to a Pumpkin Seed Roll? Where am I?"
    scene a2607 with dssr
    pause 
    scene a2608 with dssa
    va "You're between the Rye Roll and the Poppy Seed Roll."
    scene a2609 with dssa
    n "I'll take it!"
    scene a2610 with dssa
    d "You didn't just accurately quote from her one-to-ten roll scale?"
    scene a2611 with dssa
    va "I did."
    scene a2612 with dssa
    n "She's the first to take me seriously."
    scene a2613 with dssr
    va "Nami?"
    scene a2614 with dssa
    n "Yo?"
    scene a2613 with dssa
    va "Have you had sex before?"
    scene a2615 with dssa
    n "No, not yet."
    scene a2616 with dssa
    va "How so?"
    va "You're beautiful, you have curves at all the right places, and your personality makes you someone men want to be around... for more than just sex."
    scene a2617 with dssa
    va "You must've had admirers?"
    scene a2635 with dssa  
    n "Yeah, but I wasn't really interested in sex."
    scene a2636 with dssa  
    d "Hard to believe."
    scene a2618 with dssr
    va "Would you care to elaborate?"
    scene a2619 with dssa
    n "Well, you see..."
    scene a2634 with dssr  
    n "There was a time in my life where I felt very numb."
    n "Took me a while to get over it... I didn't really feel sex or any sort of lovey-dovey stuff."
    n "I saw having sex with someone as weak. As if I'd submit to someone."
    scene a2633 with dssa  
    va "That changed?"
    scene a2632 with dssa  
    n "Oh yeah."
    scene a2620 with dssr
    va "Hmm... In your position it must be torture... Not even being allowed to do so..."
    scene a2632 with dssr
    n "Who's gonna tell on me? You?"
    scene a2620 with dssr
    va "I would never."
    scene a2621 with dssa
    va "I would actively encourage you to break this rule."
    if NamiDate is True:
        scene a2622 with dssa
        n "I wanna break it with [name]."
        scene a2623 with dssa
        va "Why him?"
        scene a2622 with dssa
        d "Please don't act like I'm not here..."
        scene a2624 with dssa
        n "I trust him more than anyone else."
        stop music fadeout 10
        n "I... I trust him not to pull out."
        scene a2627 with dssa
        "They chuckle."
    else:
        scene a2624 with dssa
        n "I will break it."
        n "There's no way I'll finish college as a virgin."
        scene a2625 with dssa
        stop music fadeout 10
        va "As soon as you're a little more experienced, I'd love a threesome with you."
        scene a2626 with dssa
        "Nami lets out a quiet, intimidated 'Yoo...'"
    $ play_playlist(playlist_Smooth2)
    scene a2628 with dssr
    pause 
    scene a2629 with dssa 
    va "Sit down, sister."
    scene a2630 with dssa  
    za "What are you all up to?"
    scene a2631 with dssa  
    va "Did you know that Nami's a virgin?"
    scene a2630 with dssa  
    za "Yeah. Sure."
    za "That's the first thing I ask our guests..."
    scene a2637 with dssr
    n "Everyone piles on me... The poor little virgin..."
    scene a2638 with dssa
    za "I've never had it either."
    scene a2639 with dssa
    n "I didn't expect that." 
    scene a2640 with dssa
    za "Why not? I'm too busy to have sex."
    scene a2641 with dssa
    va "Yet, you and Nadia talk a lot about it."
    scene a2642 with dssa
    za "Shut up."
    scene a2643 with dssa
    za "It almost happened once. But then I remembered I had forgotten to track my macros in the app."
    scene a2644 with dssa
    n "Whaaat?"
    scene a2645 with dssa
    za "I'm kidding... I have an unreasonable fear of pregnancy."
    za "And because we only had these extra-thin condoms, I blew it off."
    scene a2647 with dssa
    n "Are you using contraception?"
    scene a2646 with dssa
    za "No. I don't like things that disrupt my hormonal balance."
    scene a2648 with dssa
    za "And I don't trust condoms... They look so fragile and unsafe."
    scene a2649 with dssr
    va "Condoms can take a beating, Zara."
    va "Besides, the pill isn't what it used to be."
    va "There are pills that barely have any side effects these days."
    scene a2650 with dssr
    za "...Maybe if I find a boyfriend sometime in the next 25 years."
    if ZaraBBallTrust5x0 is True and NamiDate is False:
        scene a2651 with dssa
        va "What about 25 centimeters next to you?"
        scene a2652 with dssa
        d "Can't you just leave me out of it?"
        scene a2653 with dssr
        va "You're the only one here with a penis..."
        scene a2654 with dssa
        va "If we four were the only ones left, you'd have to mate with us repeatedly to repopulate the world."
        scene a2655 with dssa
        d "..."
        d "Why do you talk?"
        scene a2656 with dssa
        va "Getting back to my question... Why not [name], Zara?"
        scene a2657 with dssa
        za "Let me answer your question with a question... Why [name]?"
        scene a2658 with dssa
        va "You're clearly fond of him."
        if ZaraBBallTrust5x0 is True:
            scene a2659 with dssa
            za "I'm noooot!"
        else:
            scene a2656 with dssa
            za "You're reading too much into this."
        scene a2660 with dssr
        va "He challenges you, doesn't he?"
        scene a2661 with dssr
        za "*sigh* For the last time! [name] and I are training together!"
        scene a2662 with dssr
        if ZaraBBallTrust5x0 is False:
            za "Besides being acquaintances, our relationship is strictly professional." 
        else:
            za "Besides being friends, our relationship is strictly professional." 
        scene a2663 with dssa
        va "Professional... You two would look great on camera... Your bodies intertwined, your rhythmic movements coupled with excessive exhales-"
        scene a2664 with vpunch
        za "Nessi!"
        scene a2665 with dssa
        n "I'd watch that tape once... For academic purposes."
        scene a2666 with dssa
        pause
        scene a2667 with dssa
        za "...I would look good on camera, though."
    scene a2669 with dssr
    n "Yo, you strike me as someone with a sex tape, Vanessa."
    scene a2668 with dssa
    va "I might've made one or two."
    scene a2669 with dssa
    n "Publicly available?"
    scene a2668 with dssa
    va "Of course not."
    scene a2670 with dssa
    n "...Available for a certain redhead?"
    scene a2671 with dssa
    va "Maybe."
    scene a2672 with dssa
    n "Seriously?"
    scene a2671 with dssa
    va "Ask me again next week."
    scene a2674 with dssr
    pause 
    scene a2673 with dssa
    n "You know who I think has a sex tape?"
    n "Noji."
    scene a2675 with dssa
    va "What makes you think that?"
    scene a2676 with dssa
    if NojiPastS2_1x0 is True:
        n "She and Nick have an open relationship."
        scene a2675 with dssa
        za "Really?"
        scene a2673 with dssa
        n "[name] said so."
        scene a2675 with dssa
        d "That's what she told me."
        scene a2677 with dssr
        va "I know about it."
        va "To be truthful, I'm the one who told Dad to take the leap and at least give it a try."
        scene a2678 with dssa
        n "I always suspected her to be naughty."
        scene a2677 with dssr
        va "Nojiko being a naughty one shouldn't surprise you."
        va "Her tattoos say more than a thousand sex tapes."
        scene a2679 with dssa
        n "Yeaaah, but some of the naughty ones calm down over the years and become extremely conservative."
        scene a2677 with dssa
        va "I wouldn't be surprised if Nojiko tried to shed that part of her."
        va "It wasn't very successful, I'd assume."
        scene a2680 with dssa
        va "You can't escape your true self."
        scene a2681 with dssr
        za "I didn't think Dad would do that... After all-"
        scene a2682 with dssa
        va "That's exactly why he's doing it."
        scene a2683 with dssa
        va "It gives him a feeling of safety and control."
        va "I don't know the full arrangement of their relationship, but I assume this is the only way Dad can sleep at night."
        scene a2684 with dssa
        d "His ex cheated on him, correct?"
        scene a2685 with dssa
        va "Yes." 
        scene a2684 with dssa
        d "And he never got over it?"
        scene a2686 with dssa
        va "It was very hard for him. He really loved Mother... Through all her shortcomings."
        scene a2687 with dssa
        za "Which according to her, I had a lot of."
        scene a2688 with dssa
        za "...The only good thing she taught me was to be comfortable with nudity."
        scene a2689 with dssr
        pause 
        scene a2690 with dssa
        d "...What?"
        scene a2691 with dssr
        va "But to get back to a more stimulating topic..."
        scene a2692 with dssa
        va "Sex tapes."
    else:
        n "There are many telltales."
        n "Like- she sometimes doesn't wear underwear when she goes for a run."
        n "She walks around the house in nothing but a string, but tells me to dress appropriately if I do that."
        scene a2675 with dssa
        d "She doesn't really walk around the house nude."
        scene a2676 with dssa
        n "Maybe if you had left your room once in a while, you would've seen it."
        n "Then there are her tattoos."
        scene a2677 with dssr
        va "Nojiko being a naughty one shouldn't surprise you."
        va "She has tattoos that say more than a thousand words."
        scene a2678 with dssa
        n "Yeaaah, but some of the naughty ones calm down over the years, and become extremely conservative."
        scene a2677 with dssa
        va "I wouldn't be surprised if Nojiko tried to shed that part of her."
        va "It wasn't very successful, I'd assume."
        va "You can't escape who you really are." 
    scene a2693 with dssr
    va "I could see Noji having a sex tape hidden somewhere." 
    scene a2694 with dssa
    n "I need to find it."
    scene a2695 with dssr
    va "Why don't you ask her?"
    scene a2696 with dssa
    n "Because she's going to think I'm a retard?"
    scene a2700 with dssr
    d "She already thinks that." 
    scene a2695 with dssr
    va "Perhaps I can get my hands on it."
    scene a2697 with dssa
    va "However, I will have to get her permission to show it to you."
    scene a2698 with dssa
    n "What do you think she's into?"
    scene a2699 with dssa
    va "I have some theories."
    scene a2698 with dssa
    n "Lemme hear 'em!"
    scene a2701 with dssr
    pause
    d "Hi."
    scene a2702 with dssa
    za "Hi."
    scene a2703 with dssa
    za "I hate lying around... I need to do something."
    scene a2704 with dssa
    menu:
        "Wanna wrestle?":
            $ ZaraWrestly_S2_CH1 = True 
            scene a2705 with dssa
            za "Ya."
            scene a2706 with dssr
            pause 
            play sound "Music/Sfx/Punch.ogg"
            scene a2707 with vpunch
            pause 
            play sound "Music/Sfx/Punch.ogg"
            scene a2708 with vpunch
            pause 
            play sound "Music/Sfx/Punch.ogg"
            scene a2709 with vpunch
            pause 
            play sound "Music/Sfx/BodyFall.ogg"
            scene a2710 with vpunch
            pause 
            scene a2711 with vpunch
            pause 
            play sound "Music/Sfx/Punch.ogg"
            scene a2712 with vpunch
            pause 
            scene a2713 with dssr
            za "Nooooo!"
            play sound "Music/Sfx/Punch.ogg"
            scene a2714 with vpunch
            pause 
            scene a2715 with dssa 
            va "Buffoons." 
            scene a2716 with dssr 
            d "Do you give up?"
            scene a2717 with dssr
            za "Mmmmmm- I'll give up when I'm dead!"
            play sound "Music/Sfx/Slap.ogg"
            scene a2718 with vpunch
            pause 
            if ZaraBBallTrust5x0 is True:
                scene a2719 with vpunch
                va "You see these two?"
                scene a2720 with dssa
                n "Yeah?"
                scene a2721 with dssa
                va "In a few years, they will both act surprised when they hear the other had a thing for them."
                scene a2722 with dssa
                pause 
                play sound "Music/Sfx/BodyFall.ogg"
                scene a2723 with vpunch
                pause
            scene a2724 with vpunch
            pause
            scene a2725 with dssr 
            pause 
            scene a2726 with dssa 
            za "I almost peed myself." 
            scene a2727 with dssa 
            pause 
            scene a2728 with dssa
            pause 
            scene a2729 with dssa
            za "I win."
            scene a2728 with dssa
            d "Hell no."
            scene a2730 with dssa
            za "Mhm!"
            scene a2731 with dssr
            pause 
            scene a2732 with dssa
            pause 
        "Do some situps.":
            scene a2703 with dssa
            za "Nah..." 
            scene a2732 with dssr 
            pause
    scene a2733 with dssa
    n "Ah damn! I was supposed to play with Nadia and Nia twenty minutes ago!"
    scene a2734 with dssr
    n "I'll see y'all tomorrow!"
    scene a2735 with dssr
    pause
    if ZaraWrestly_S2_CH1 is True:
        scene a2736 with dssr
    else:
        scene a2737 with dssr
    pause
    if ZaraWrestly_S2_CH1 is True:
        scene a2739 with dssa
    else:
        scene a2738 with dssa
    za "I'm calling it too."
    if ZaraWrestly_S2_CH1 is True:
        scene a2741 with dssa
    else:
        scene a2741 with dssa
    za "Nighty."
    d "Sleep well."
    scene a2742 with dssr
    pause 
    scene a2743 with dssa
    va "I noticed how you sometimes look at Nami."
    "You look at Vanessa with your brow slightly raised, but no word escapes your lips."
    scene a2744 with dssr
    va "It's not friendly... Nor hostile..." 
    va "You observe her more than anything else."
    scene a2745 with dssa
    va "I'd argue it's a defense mechanism."
    va "It reminds me of a younger Zara... The way she looked at our Mother."
    va "Or how a child looks at their drunken parent... Well aware that at any second they could explode."
    scene a2746 with dssa
    pause 
    scene a2747 with dssr
    pause 
    scene a2748 with dssa
    va "You don't need to tell me."
    scene a2749 with dssr
    va "I'll keep an eye on Nami..."
    stop music fadeout 13
    va "There is more to her than meets the eye."
    if NessiHoldingS2Ch1 is True:
        scene a2750 with dssr
        pause 
        scene a2751 with dssa
        pause
        scene a2752 with dssa
        va "Good night, [name]."
        scene a2754 with dssr
        d "...Good night." 
    else:
        scene a2753 with dssr
        va "Good night, [name]."
        scene a2754 with dssa
        d "Night."
    play music "Music/TheIntangible/The Intangible - Encyclopedia of Frozen Dreams.ogg"
    scene a2755 with dssr
    pause 
    scene a2756 with dssr
    nic "[name]. May I?"
    scene a2757 with dssa
    d "Of course."
    scene a2758 with dssr
    nic "Listen... I talked to a colleague of mine whose brother is a coach for the Wollust Wormies."
    nic "And if you want, you can audition for the pre-game free throw challenge."
    scene a2759 with dssa
    d "Seriously?"
    scene a2760 with dssa
    nic "Zara mentioned how precise your throws were, and when it comes to making the first team, it's all about selling yourself."
    nic "And if you perform well in that challenge, it might help you with the college team. We'll send a copy of it to the college, publish it on Aurora, and see if it helps."
    scene a2761 with dssa
    d "I don't know what to say..."
    scene a2762 with dssa
    nic "Just say you'll do it and I'll arrange it."
    scene a2763 with dssa
    d "Thank you... Like- thank you, really."
    scene a2764 with dssa
    nic "No problem."
    scene a2765 with dssa
    pause
    scene a2766 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    jump MorningS2_Ch1_2




label MorningS2_Ch1_2:
    if BellaNonExclusive5x0 is True:
        $ BellaDate = True
    scene a2767 with dssb
    "You sit there, with lingering thoughts."
    scene a2768 with dssr 
    pause 
    scene a2769 with dssr 
    pause
    scene a2770 with dssa 
    m "Would you like a drink?"
    scene a2771 with dssr
    d "No, I'm going to bed soon."
    if BellaDate is True:
        scene a2772 with dssa 
        d "(I haven't talked to Bella all day...)"
        d "(I can't believe I actually miss her.)"
        d "(I shouldn't text her... She's probably glad she didn't hear from me today.)"
        scene a2798 with dssb
        show text "Meanwhile at Bella's." with Dissolve (2)
        with Pause(3)
        hide text with Dissolve(2)
        pause 
        scene a2799 with dssr
        b "What?"
        scene a2800 with vpunch
        na "Just call him!"
        na "Or better! Send him a picture of your pussy! Maybe he'll come over and finally stuff your mouth!"
        scene a2801 with dssa
        b "Shut up!"
        b "Put on some pants and get in bed!"
        scene a2802 with vpunch
        na "I was in the midst of changing!"
        scene a2803 with dssa
        b "We want to start the movie!"
        scene a2804 with dssa
        na "Only if you stop complaining all the time!"
        scene a2805 with dssr
        b "I'm not complaining!"
        scene a2806 with dssr
        ay "...You complain a lot about it."
        ay "Just text him if you want to talk to him..."
        scene a2807 with dssa
        pause 
    else:
        scene a2772 with dssa 
        pause
    scene a2773 with dssr
    m "How was your day?"
    scene a2774 with dssa
    d "If we ignore the first aid course... Good. How about yours?"
    scene a2775 with dssa
    m "Pretty good. Especially because I'm getting new puppets."
    scene a2776 with dssa
    d "...Oh god."
    scene a2777 with dssr
    pause
    scene a2778 with dssr
    d "When's the next book club?"
    scene a2779 with dssa
    m "You already asked me that... Do you still really want to go there?"
    scene a2780 with dssa
    d "Yeah."
    scene a2781 with dssa
    m "You should focus on your studies, sports-"
    scene a2782 with dssa
    d "Noji..."
    scene a2783 with dssa
    m "Next Sunday."
    scene a2784 with dssa
    d "I'll be there." 
    scene a2785 with dssa
    m "You look tired."
    scene a2786 with dssr
    d "I've only slept in short bursts."
    scene a2787 with dssa
    m "Go to bed."
    scene a2786 with dssa
    d "I will." 
    scene a2788 with dssa               
    m "Good night."
    scene a2789 with dssa  
    d "Good night."
    scene a2790 with dssr 
    pause 
    stop music fadeout 4
    scene black with Dissolve(2)
    with Pause(.5)
    show text "The next morning..."
    with Pause(2)
    hide text with Dissolve(2)
    play ambient "Music/Sfx/Summer_Morning.ogg"
    scene a2790a with dssb
    pause
    scene a2791a with dssa
    pause
    scene a2792a with dssr
    d "(Zara didn't wake me.)"
    scene a2791 with slideleft 
    pause
    scene ZaraBoxi with dssa 
    za "PSS! PSS! PSS!"
    play sound "Music/Sfx/Punch.ogg"
    scene a2794 with vpunch 
    za "BAM!"
    scene a2795 with dssr 
    pause
    scene a2796 with dssa
    pause
    scene a2797 with dssr
    pause
    $ play_playlist(playlist_Smooth)
    if ZaraWrestly_S2_CH1 is True:
        scene a2809 with dssa
        za "Aaah-"
        play sound "Music/Sfx/Punch.ogg"
        scene a2810 with vpunch 
        pause 
        scene a2811 with dssr
        za "Now you've done it!"
        scene a2812 with dssa
        pause  
        scene a2813 with dssa
        with Pause(.3)
        play sound "Music/Sfx/Punch.ogg"
        scene a2814 with vpunch 
        pause 
        scene a2815 with dssa
        d "Ouch."
        scene a2816 with dssa
        za "I thought you'd dodge!" 
        scene a2817 with dssa
        d "It's not like it really hurt."
        scene a2818 with dssa
        za "It was just a love tap!"
        scene a2819 with vpunch
        za "NOW GET 'EM UP!"
        scene a2820 with dssr
        pause 
        scene a2821 with dssa
        va "*Sighs* Can't they just fuck..."
        scene a2822 with dssr
        pause
        scene a2823 with dssa
        va "At least they get it."
        scene a2824 with dssr
        pause 
        scene a2825 with dssa
        za "This is what I hate about being a girl..."
        za "I've been training relentlessly for years and yet a rather untrained guy can overpower me."
        scene a2826 with dssa
        za "Sure, I focus on cardio... But still..."
        scene a2827 with dssr
        d "You should wrestle Nami."
        scene a2828 with dssa
        za "I need that for my ego."
        scene a2829 with dssa
        d "She and I have been wrestling for a few years. She's not that easy."
        d "However, you'll outrun and outlast me any day."
        scene a2828 with dssa
        za "Still useless in close combat."
        scene a2832 with dssr
        va "You can probably ride his dick for days."
        scene a2830 with vpunch
        za "Nessi!"
        scene a2831 with dssr
        d "For a girl who's never had sex before, you talk a lot about it."
        scene a2833 with dssr
        va "Who says I've never had sex?"
        va "What Zara said was, that I haven't had sex with my current boyfriend yet."
        scene a2834 with dssr
        d "I see."
    scene a2835 with dssr
    n "Yo, morning."
    scene a2836 with dssa
    va "Good morning, Nami."
    if ZaraWrestly_S2_CH1 is True:
        scene a2837 with dssa
        n "Yo! Wrestling without me?!"
        scene a2838 with dssr
        d "I told Zara she should wrestle you."
        scene a2839 with dssa
        n "Lemme get some fuel and I'm on it!"
        scene a2841 with dssr
        pause 
        scene a2840 with dssa
        d "You didn't wake me at 3:30." 
        scene a2843 with dssa
        za "You really were in need of some sleep and I didn't want to be annoying."
        scene a2842 with dssa
        d "You don't annoy me."
    scene a2844 with dssr
    za "Okay, I'll get dressed and we can go." 
    scene a2845 with dssr
    pause 
    stop ambient
    stop music fadeout 5
    scene black with Dissolve(2)
    with Pause(.5)


label CollegeS2_Ch1:
    play ambient "Music/Sfx/Car_Drive_Night_Interior.ogg"
    scene a2846 with dssb
    pause
    carspeaker "Fats regulate hormones. Omega-3s reduce inflammation, and dietary cholesterol supports testosterone production. Don't avoid fat. Choose the right kind."
    scene a2847 with dssa
    n "Why are we listening to an audiobook about nutrition?"
    scene a2848 with dssa
    za "What else would anyone want to listen to in the morning?"
    scene a2849 with dssr
    n "Is that your audiobook library?"
    scene a2850 with dssr
    za "Mhm."
    scene a2851 with dssa
    pause 
    scene a2852 with dssa 
    carspeaker "She panted, eyes feral, sweat stinging her skin: Spread my legs wider, fuck, and drown me in your warm load, leaving me wrecked and still wanting you."
    play sound "Music/Sfx/Button_Mashing.ogg"
    scene a2853 with dssa
    carspeaker "She's sprawled on the leg press, weights clanking, her sweat-soaked body pinned under him, as he drives into her with feral grunts,her moans, begging for his raw, filthy release to flood her trembling core."
    scene a2855 with dssr
    pause 
    scene a2856 with dssa
    za "...That was Nessi's."
    scene a2857 with dssa
    n "...Sure." 
    stop ambient fadeout 3
    scene black with Dissolve(2)
    with Pause(.5) 
    $ play_playlist(playlist_College)
    scene a2858 with dssb
    pause
    scene a2859 with dssr
    u "Does this mean you don't want another project partner?"
    scene a2860 with dssr
    b "I'm in so deep now that it doesn't make sense."
    scene a2861 with dssa
    u "Good."
    if BellaDate is True:
        $ BellaRoute = True 
        play sound "Music/Sfx/Punch.ogg"
        scene a2862 with vpunch
        pause
        scene a2863 with dssa #sfx 
        pause
        scene a2866 with dssr
        pause 
        scene a2867 with dssa 
        pause
        play sound "Music/Sfx/Slap.ogg"
        scene a2868 with vpunch
        pause 
        scene a2869 with dssr
        pause 
    scene a2870 with dssr
    throne "Hello [name]."
    scene a2871 with dssa
    d "Oh, hi."
    d "Do you work here?"
    scene a2872 with dssa
    throne "Yes. I'm the Registrar."
    throne "I'm in charge of academic records, transcripts, and course scheduling."
    scene a2873 with dssa
    d "Oh. Cool."
    scene a2874 with dssa
    throne "I hope I'll see you at the book club again."
    scene a2875 with dssa
    d "I'll most likely be there."
    scene a2876 with dssa
    "She smiles and goes her way." 
    scene a2877 with dssr
    pause 
    scene a2878 with dssa
    pause
    scene a2880 with dssr 
    pause 
    scene a2881 with dssr 
    pause
    scene a2882 with dssr
    mi "Hey [name]. Could you help me with some books? Vic's not here yet, and I'd like to get them before they storm the library."
    scene a2883 with dssa
    d "I gotta head that direction anyways. anyway."
    scene black with Dissolve(2)
    with Pause(.5)
    jump Karen5x5





label Karen5x5: #Prep
    scene a2884 with dssb
    pause
    scene a2885 with dssr
    u "That bitch blocked me."
    scene a2886 with dssr
    son "It's got this white stuff on it."
    scene a2887 with dssa
    kate "Ahhh... We call it spaghetti carbonara."
    scene a2888 with dssr
    u "That's awesome! I mean, I've been obsessed with it ever since I saw Riverdance as a kid."
    scene a2889 with dssa
    u "The way those feet fly tap-tap-tap, like lightning on hardwood. It's so energetic, so... passionate. Kinda like you seem, you know?"
    scene a2891 with dssr
    pause 
    scene a2892 with dssa
    sas "What?"
    scene a2893 with dssa
    u "Step dancing. Y-you like it, right? You do it yourself?"
    scene a2894 with dssa
    pause 
    scene a2895 with dssa
    sas "Did Ayua tell you that?"
    scene a2896 with dssa
    u "Yeah?"
    scene a2897 with dssa
    sas "She was messing with you. I have never done nor will I ever do step-dancing."
    scene a2890 with dssr
    u "Oh..."
    scene a2898 with dssr
    ka "Morning Mila."
    scene a2899 with dssa
    mi "Good morning!"
    scene a2900 with dssa
    pause
    scene a2902 with dssa
    mi "Here, I got the pay for the next six months."
    scene a2901 with dssa
    ka "Thank you!"
    scene a2905 with dssr
    ka "I don't have time for your ID right now."
    scene a2906 with dssa
    d "I'm not here for that."
    scene a2903 with dssa
    mi "Right. I'm here to pick up the books Victoria and I requested."
    scene a2904 with dssa
    ka "Lemme check."
    scene a2907 with dssr
    pause
    scene a2908 with dssa
    mi "You look better than the last time I saw you."
    scene a2909 with dssa
    d "I finally got some sleep."
    scene a2910 with dssa
    if Mila_Bath_Pussy is True:
        mi "Since our adventure in the bathtub, I've been sleeping worse." 
        scene a2911 with dssa 
        d "I guess, I'll have to step up my game."
        scene a2912 with dssa 
        mi "Or you know... start the game."
    else:
        scene a2912 with dssa 
        mi "Nami told me that a lot has happened in the past few days."
    scene a2911 with dssa 
    d "Vanessa wants to invite you to a small party next week."
    scene a2913 with dssr
    mi "Yeah, she texted me this morning."
    scene a2914 with dssa
    d "You gave her your number?"
    scene a2915 with dssa
    mi "Yeah, why not?"
    scene a2916 with dssa
    d "I thought she'd creep you out."
    scene a2917 with dssr
    mi "She's very straightforward and her boyfriend- well... you know him."
    mi "But she seems... honest."
    scene a2918 with dssa
    d "I agree that she's straightforward."
    if Vanessa_Sharing_Mila is True:
        scene a2919 with dssa
        d "Straightforward enough to ask me if I'd be okay with sharing you for a night."
        scene a2921 with dssa
        pause 
        scene a2920 with dssa
        mi "Nooo, you're messing with me?"
        mi "Did you tell her I'm not into girls?"
        scene a2922 with dssr
        d "She meant you, her and her boyfriend."
        scene a2923 with vpunch
        mi "What?!"
        scene a2924 with dssa
        mi "I hope you let her down easy."
        scene a2925 with dssa
        d "That's your job."
        scene a2926 with dssa
        mi "What did you tell her?"
        scene a2927 with dssa
        d "I said that it's your decision to make. I don't own you."
        scene a2928 with dssa
        mi "Yes, but- we're dating, no?"
        scene a2929 with dssa
        d "Is it a bad thing that I'll let you decide?"
        scene a2930 with dssa
        if MilaVenus4x5 is True:
            mi "You do encourage me to do Venus... I should probably not be surprised."
        else:
            mi "I'm just surprised you didn't immediately tell her no."
        scene a2931 with dssa
        mi "*sigh* Now I have to think of a way to let her down without insulting Mario in the process."
        scene a2932 with dssr
        d "Here's an idea."
        d "'Thanks for the offer Vanessa, but I'm not interested. [name]'s giving me everything I need.'"
        scene a2933 with dssa
        mi "*Chuckles* Sure. I'll tell her that."
    scene a2934 with dssa
    mi "I like Vanessa's approach." 
    scene a2935 with dssa
    mi "If she sees something she wants, she just goes for it..."
    scene a2936 with dssa
    mi "I think my life would've been much easier if I didn't hold back all the time."
    mi "There's one bread roll left at the bakery and if someone else wants it, I'll let them have it."
    scene a2937 with dssa
    d "Being polite isn't a bad thing... You just have to learn to say no sometimes."
    scene a2938 with dssa
    mi "I say no all the time... But I like to put a smile on people's faces."
    mi "I had a friend in high school who I think used me for exactly that."
    scene a2939 with dssa
    mi "She'd always talk about her issues and problems. I'd listen and support her but whenever I talked about my worries, she completely shut off."
    mi "One day she just stopped speaking to me altogether."
    scene a2940 with vpunch #sfx 
    mi "From now on I'll stand up for myself!" 
    mi "Nick said it too."
    mi "If I want something, I've gotta take it!"
    scene a2941 with dssa
    d "What do you want?"
    scene a2940 with dssa
    mi "I want access to the golf club."
    if MilaDate is True:
        scene a2942 with dssa
        mi "And I want to make out with you behind- uhhh..."
        scene a2943 with dssa
        mi "That bookshelf!"
        scene a2944 with dssa
        d "I'd be up for that."
    scene a2945 with dssa
    kat "Hey Mila."
    scene a2946 with dssr
    mi "Hola Kate."
    if BellaKiss3x5 is True:
        scene a2947 with dssa
        mi "That's [name]."
        scene a2948 with dssa
        kat "Met him."
        if RoRum is True:
            scene a2949 with dssa
            d "And that's the bitch that spread the rumor about me and Robin."
            jump KatePlan5x5
        else:
            jump KarenTwo5x5
    else:
        scene a3151 with dssa
        kat "If it isn't [name]."
        kat "Remember to go see Miss Marla. You and Nora need to see her."
        scene a3152 with dssa
        d "...Right."
        scene a3153 with dssa
        mi "I heard about what happened..."
        mi "I would've loved to see it."
        scene a3154 with dssa
        kat "I'll show you a picture later."
        kat "It was really funny."
        scene a3155 with dssr
        pause
        if RoRum is True:
            scene a3156 with dssr
            kat "What?"
            kat "Oh god... Do you still think we spread the rumor about you and Robin?"
            scene a3157 with dssr
            pause 
            jump KatePlan5x5
        else:
            jump KarenTwo5x5






label KatePlan5x5:
    $ KateNetwork5x5 = True
    scene a2951 with vpunch
    kat "For the last time! We didn't!"
    scene a2950 with dssa
    d "Nobody else was there."
    scene a2951 with dssa
    kat "Okay. Let's have a little chat."
    scene a2952 with dssr
    kat "Come."
    scene a2953 with dssa
    d "No. I don't want to talk to you."
    scene a2954 with dssr
    mi "[name]..."
    scene a2955 with dssa
    d "What?"
    scene a2956 with dssa
    mi "Don't be a little bitch."
    scene a2957 with dssa
    d "Wow."
    scene a2958 with dssa
    mi "Sorry!"
    stop music fadeout 5
    mi "Just talk to her, please."
    scene a2959 with dssr
    pause
    play music "Music/TheIntangible/The Intangible - Interdimensional Amity.ogg"
    scene a2960 with dssa
    pause
    scene a2961 with dssa
    kat "It wasn't me... And it wasn't one of my friends."
    scene a2962 with dssa
    d "And for you to say that we had to go here?"
    scene a2963 with dssa
    kat "A few girls and I have been looking into something..."
    scene a2964 with dssa
    "She pulls out her phone."
    scene a2965 with dssa
    pause
    scene a2966 with dssr
    d "Why are you showing me a picture of a girl on the toilet?"
    scene a2967 with dssa
    kat "Oh."
    scene a2968 with dssa
    kat "I meant this one."
    scene a2969 with vpunch
    d "That's another girl on the toilet!"
    scene a2970 with vpunch
    kat "Exactly!"
    scene a2971 with dssa
    kat "That's just one of many girls... from this and the other colleges."
    kat "There's a semi-professional creep-group that takes pictures of girls in... certain situations."
    scene a2972 with dssr
    kat "I'm one hundred percent sure that we weren't alone in the bathroom."
    kat "And whoever else was there spread the rumor... and put you next to Robin in the title of today's college paper."
    scene a2974 with dssr 
    d "What?"
    scene a2975 with dssa 
    kat "You'll see. It's all around campus."
    scene a2974 with dssa 
    d "..."
    scene a2976 with vpunch
    kat "Let me quote a line... 'He was caught having steamy, hot sex in the bathroom with multiple girls, including Kate Waidhofer, a well-known Venus model.'"
    scene a2977 with dssa 
    kat "They mentioned me by name!"
    scene a2978 with dssr
    d "What reporter was it?"
    d "The blonde one that wears glasses?"
    scene a2979 with dssa
    kat "Yes. They have that Asian girl with the gigantic tits... Maybe she was with us in that bathroom."
    kat "Or somebody else gave them some info."
    scene a2980 with dssa
    kat "But it wasn't us!"
    scene a2981 with dssa
    d "Any idea who could be one of them?"
    scene a2982 with dssa
    kat "I do... However, you've been treating me like shit."
    scene a2983 with dssa
    kat "Why would I tell you now?"
    menu:
        "Apologize.":
            $ KateNE_S1_1 = True
            scene a2984 with dssa
            d "I'm sorry..."
            scene a2985 with dssa
            if BellaDate is True:
                kat "I'm hurt. You have to make up for this."
                scene a2986 with dssr
                d "Do you want me to give you a pat on the head?"
                scene a2987 with dssa
                kat "No."
                scene a2988 with dssa
                kat "What about a simple kiss?"
                scene a2989 with dssa
                d "(...She just wants one because she hates Bella.)"
                scene a2990 with dssa
                with Pause(.35)
                menu:
                    "Give her a kiss.":
                        scene a2991 with dssa
                        pause 
                    "Give her a kiss... and tease her.":
                        $ KateTeasing = True 
                        $ Cheating +=3
                        scene a2991 with dssa
                        pause 
                        scene a2992 with dssr 
                        "You move your fingers across her crotch."
                        scene a2993 with dssr
                        kat "Now we're getting s-" 
                        scene a2994 with dssa
                        d "Be quiet."
                        d "Tell me about the creeps."
                    "Deny and go your way.":
                        scene a2995 with dssa
                        stop music fadeout 5
                        d "Good luck with whatever you're doing."
                        jump KarenTwo5x5 
            elif BellaDate and MilaDate is False:
                scene a2999 with dssa
                "She sighs."
                scene a3000 with dssa
                kat "No. Forget it."
                scene a3001 with dssa
                kat "Maybe, I'll get back to you."
                scene a3003 with dssa
                d "I'm sorry, okay?"
                scene a3002 with dssa
                kat "I heard you the first time."
                jump KarenTwo5x5 
            elif MilaDate is True:
                scene a2996 with dssa
                kat "I'm hurt. You have to make up for this."
                scene a2997 with dssa
                d "Do you want me to give you a pat on the head?"
                scene a2996 with dssa
                kat "If you do so while saying sorry."
                scene a2998 with dssa
                pause 
        "We're done here then.":
            stop music fadeout 5
            scene a2995 with dssr
            d "Good luck with whatever you're doing."
            jump KarenTwo5x5 
    scene a3004 with dssr
    kat "There's a prefect-"
    scene a3005 with dssa
    d "Ponytail, nose ring?"
    scene a3004 with dssa
    kat "Yes. You've met him?"
    scene a3005 with dssa
    d "I did."
    scene a3006 with dssa
    kat "We suspect him... But there are so many dudes that would fall into this category."
    kat "But it's not just our college... MOR and Schwartz have the same problem."
    scene a3004 with dssa
    kat "They even put out bounties for certain girls."
    scene a3007 with dssa
    kat "You should see what some asshole offers for a nude picture of Sasha Petrova."
    scene a3008 with dssa
    pause
    scene a3009 with dssa
    d "Some kind of a trap would be good."
    scene a3010 with dssa
    kat "Are you in?"
    scene a3012 with dssa
    d "...In what?"
    scene a3010 with dssa
    $ CreepNetwork_KateEntrance_1 = True 
    if KateTeasing is False:
        kat "Obviously, not inside of me."
    else:
        kat "Inside of me, obviously?"
    scene a3011 with dssa
    kat "In- as in working together with us?"
    kat "We needed a guy that... Nah, not true. We don't really need you, but we take any help we can."
    if KateTeasing is True:
        menu:
            "Tease her more.":
                $ KateTeasing2 = True 
                scene a3013 with dssa 
                pause
                d "(Why am I playing with fire?)"
                menu:
                    "Because the risk makes me feel alive.":
                        $ I_Want_To_Feel_Alive = True 
                        scene a3014 with dssa 
                        pause
                    "To give Bella an opportunity to get back at her.":
                        $ Mark_On_Kate_Teasing = True 
                        scene a3014 with dssa 
                        d "(This is for Bella...)"
                scene a3015 with dssr 
                pause 
            "Don't tease her.":
                scene a3015 with dssr 
                pass 
    else:
        scene a3015 with dssr
        pass 
    d "I'm pretty sure you can trust 99 percent of the guys in this college... But what makes you think you can trust me?"
    scene a3016 with dssa 
    kat "Because after today's newspaper... You're a victim too."
    scene a3015 with dssa 
    d "Are you?"
    scene a3017 with dssa 
    kat "Oh? You think I would tell you so that you can look up a picture of me?"
    scene a3018 with dssa 
    d "They mention that you're a big Venus model... I assume an easy NOODLE search would provide me with some pictures..."
    scene a3019 with dssr 
    kat "I only post bikini and lingerie pics on Venus." 
    scene a3020 with dssa
    d "I just want peace... Keep me in the loop or whatever."
    scene a3019 with dssa
    kat "No. We'll have a stake-out soon."
    scene a3021 with dssa
    stop music fadeout 5
    d "I certainly will not go on a stake-out. I have better things to do."
    scene a3022 with dssr
    pause
    jump KarenTwo5x5

label KarenTwo5x5:
    $ play_playlist(playlist_Smooth)
    if RoRum is True:
        scene a3023 with dssr
        pause 
        mi "[name] the fuckboy."
        scene a3024 with dssa 
        pause 
        mi "Poor Robin."
        scene a3025 with dssr 
        mi "The audacity to even print this."
        scene a3026 with dssa 
        kat "They print everything that gets people to buy."
    scene a3027 with dssa 
    ka "I got your books."
    if MilaVenus4x5 is True:
        scene a3028 with dssr 
        ka "I got the Venus magazine you wanted."
        scene a3029 with dssa
        mi "...And you put that one on top."
        scene a3030 with dssr
        ka "We wouldn't want it to get damaged now, would we?"
        scene a3031 with dssa
        mi "...Thanks Karen."
    else:
        scene a3032 with dssa
        mi "Thank you!"
    if SashaBook5x0 is True:
        scene a3033 with dssa
        d "Oh... Actually, there's a book I'd like to get."
        scene a3034 with dssa
        ka "You don't have an ID."
        scene a3033 with dssa
        d "...Can we make an exception?"
        scene a3042 with dssa
        mi "Put it on mine."
        scene a3035 with dssr
        ka "What's the name of the book?"
        scene a3036 with dssa
        d "It's Only Love."
        scene a3037 with dssa
        "Karen raises a brow and you look at her without moving a muscle."
        scene a3038 with dssr
        ka "One sec."
        scene a3039 with dssa
        pause
        scene a3040 with dssa
        ka "The things guys do for sex..."
        scene a3041 with dssa
        d "Thanks."
        scene a3043 with dssr
        pause
        d "What?"
        scene a3044 with dssa
        mi "I knew you were a hopeless romantic."
    if BellaKiss3x5 or PunchPrefect2x0 is True:
        $ McArtModel5x5 = True
        scene a3045 with dssa
        ka "[name], please go and see Miss Marla in her office."
        scene a3046 with dssa
        kat "I'll help you with the books, Mila."
        if MilaDate is True:
            scene a3044 with dssr
            mi "Uhh- one moment. I'll leave the books here for a minute."
            scene a2946 with dssr
            mi "We'll be right back."
            "Kate smiles."
            scene black with Dissolve(2)
            with Pause(.5)
            jump MilaLibraryMakeout1x0
        else: 
            scene a3047 with dssa
            d "I'll see you in a bit."
            scene a3048 with dssa
            mi "Sure. We'll be in the hallway."
        jump VictoriaHall5x5
    else:
        scene a3047 with dssa
        d "Let's go."
        jump VictoriaHall5x5

label MilaLibraryMakeout1x0:
    if MilaVenus4x5 is False:
        $ MilaVenus = False
    scene a7879 with dssr
    pause 
    scene a7880 with dssa
    mi "You thought I'd just let you leave like that?"
    scene a7879 with dssa
    "You smile."
    scene a7881 with dssa
    "Your hand brushes against her tiddy."
    if MilaSleep5x0 is False:
        scene a7882 with dssr
        d "I didn't expect pierced nipples."
        mi "It's one of the only decisions I'll never regret."
        scene a7883 with dssa
        mi "I used to worry a lot about what other people thought of me. I used to wear hoodies and other baggy clothes that hid my curves."
        scene a7884 with dssr
        mi "There was a time in high school when I wished I had small boobs and an unremarkable body."
        scene a7885 with dssa
        d "I assume people sexualized you a lot?"
        scene a7887 with dssr
        mi "Of course."
        mi "And for a long time I had a very negative association with everything sex-related."
        scene a7886 with dssa
        d "What changed?"
        scene a7888 with dssa
        mi "I think I told you about the girl who killed herself a few weeks before graduation?"
        scene ad2235 with dssr
        mi "You remind me of someone. A girl I used to know from high school. Always trying to look normal, nothing weird about her, except that... certain aura."
        d "What aura?"
        scene ad2236 with dssa
        mi "An aura that..."
        scene ad2237 with dssa
        mi "Hah..."
        scene ad2238 with dssa
        mi "That scares me."
        scene a7888 with dssr
        mi "She was the opposite of me. Small boobies, small butt."
        mi "Nothing that would particularly attract mockery. People still called her all sorts of names."
        mi "After she ended her life, I kept thinking a lot about her and her situation."
        scene a7889 with dssr
        mi "You can do everything right, and you'll still be attacked."
        mi "I was already branded as the 'daughter of a whore'... I heard stuff like 'Do you get preferred entry at the whore academy because your Mom was an honor grad?'"
        scene a7890 with dssr
        mi "I ignored them but- damn did it hurt. I developed some sort of trauma."
        mi "If I acted and dressed just as plain as possible, there would be nothing to target, right?"
        scene a7891 with dssa
        d "When did it change or- what did it change?"
        scene a7892 with dssr
        mi "An ex-friend talked bad about me behind my back after a day at the public pool."
        mi "By that time my frontal lobe had developed enough for me to call it out for what it was. I was so fed up that I just didn't care anymore and owned my body."
        scene a7893 with dssa
        mi "The funny thing? The bullying mostly stopped."
        mi "I stopped wearing baggy pants and hoodies, and instead wore clothes that accentuated my curves... People treated me differently immediately."
        scene a7894 with dssr
        mi "What matters is that whatever hand life dealt you, you call it your own and carry it with confidence."
        mi "It makes all the difference."
        scene a7895 with dssa
        d "I assume guys especially stopped trying to bully you?"
        scene a7894 with dssa
        mi "I was rarely bullied by guys. It was almost always girls. Unless they had boyfriends or they were guys I previously rejected."
        scene a7895 with dssa
        d "What about Mario?"
        scene a7894 with dssa
        mi "Mario didn't bully me directly. He was a bystander, which in my opinion is just as bad."
        scene a7896 with dssa
        mi "I'll never just watch when someone gets ganged up on. Not even if it's Bella..."
        scene a7897 with dssa
        mi "Guys obviously started hitting on me a lot more."
        scene a7898 with dssa
        mi "But girls? Girls are mean, man."
        mi "...A girl's first bully is her own Mother."
        scene a7899 with dssr
        mi "And Lena... my mother often put me down in a passive-aggressive way."
        scene a7900 with dssa
        mi "Which, in my opinion, is much worse! It gets you so much more heated."
        scene a7901 with dssr
        d "It's great to hear that you're now carrying yourself with pride."
        scene a7902 with dssa
        mi "Getting my nipples pierced was my last 'Fuck you' to my alter ego that did everything to just not draw any attention."
        scene a7903 with dssr
        mi "Now... I just go with the flow."
        scene a7904 with dssa
        d "I respect it."
        scene a7905 with dssa
    else:
        scene a7905 with dssr 
    pause 
    menu:
        "Compliment her tits.":
            if Mila_Date_STG3 is True:
                scene a7906 with dssa
                d "You've got amazing boobs..." 
                scene Mila_Lib_Kissing with dssa 
                $ renpy.pause(0.5, hard=True)
                pause 
                jump MilaLibraryMakeout1x0_STG3
            $ Mila_Date_STG2 = True 
            d "You have great tits."
            mi "Thank you."
            scene a7906 with dssa
            pause 
            jump MilaLibraryMakeout1x0_STG3
        "Don't.":
            scene a7906 with dssa
            pause 
            pause 
            scene a7907 with dssr
            "You hear footsteps."
            scene a7908 with dssa
            d "We should probably go."
            scene a7909 with dssr 
            mi "Yeah."
            pause
            jump VictoriaHall5x5

label MilaLibraryMakeout1x0_STG3:
    menu:
        "Play with her pussy.":
            if MilaVenus4x5 is True:
                $ MilaVenus = True 
            else:
                $ MilaVenus = False 
            $ Whispers +=1
            $ Mila_Pussy = True
            scene MilaFingli_Lib with dssa  
            $ renpy.pause(0.5, hard=True)
            pause 
            "You hear footsteps." 
            d "*Whispers* Someone's coming."
            if MilaVenus is True:
                menu:
                    "Keep going.":
                        $ MilaExhi_STG1 = True 
                        scene MilaFingli_Lib2 with dssa
                        $ renpy.pause(0.3, hard=True)
                        pause 
                        "Mesmerized by Mila's bouncing tits, he watches for just a moment."
                        scene a7910 with dssr 
                        mi "Holy shit..."
                        scene a7911 with dssa
                        "Mila chuckles."
                        scene a7910 with dssa
                        mi "My heart is pounding through my chest..."
                        mi "You just kept going!"
                        scene a7912 with dssa
                        d "You didn't stop me."
                        scene a7913 with dssa
                        mi "...I didn't want you to stop."
                        scene a7914 with dssa
                        pause 
                        scene a7917 with dssr
                        d "We should probably go."
                        if Mila_Bath_Pussy is True:
                            scene a7918 with dssa
                            mi "Go fuck? Yes."
                            scene a7919 with dssa
                            "You give her a smile."
                            scene a7920 with dssa
                            mi "I guess we should."
                        scene a7921 with dssa
                        mi "This is our corner now."
                        scene a7922 with dssa
                        d "Whoever gets in here gets beaten up." 
                        scene a7923 with vpunch
                        mi "By me!"
                        scene a7924 with dssa
                        "You chuckle."
                        scene a7925 with dssa
                        d "I'd like to see that."
                        scene a7926 with dssa
                        mi "Noooo! I can't even throw a punch."
                        scene a7927 with dssa
                        mi "My arms flail like flaccid wieners."
                        scene a7928 with dssa
                        mi "I may have to use my boobs as a crush weapon."
                        scene a7929 with dssa
                        d "That might just work."
                        scene a7930 with dssr
                        mi "My body isn't made for fighting."
                        mi "It's made for squatting heavy, swinging golf clubs, and being mounted."
                        scene a7931 with dssa
                        d "'Mounted.'"
                        scene a7932 with dssa
                        mi "I love that word. It feels so carnal."
                        scene a7933 with dssa
                        mi "*Sensual whisper* Mount me..."
                        jump VictoriaHall5x5
                    "Stop.":
                        pass 
            else: 
                scene a7915 with dssr
                mi "That was close."
                scene a7916 with dssa
                d "Yeah."
        "Take it easy.":
            scene a7906 with dssa 
            pause 
            pause 
            scene a7907 with dssr
            "You hear footsteps."
            scene a7908 with dssa
            d "We should probably leave."
            scene a7909 with dssr 
            mi "Yeah."
            jump VictoriaHall5x5 
    scene a7911 with dssr 
    d "We should probably leave."
    scene a7921 with dssr
    mi "This is our corner now."
    scene a7922 with dssa
    d "Whoever gets in here gets beaten up." 
    scene a7923 with vpunch
    mi "By me!"
    scene a7924 with dssa
    "You chuckle."
    scene a7925 with dssa
    d "I'd like to see that."
    scene a7926 with dssa
    mi "Noooo! I can't even throw a punch."
    scene a7927 with dssa
    mi "My arms flail like flaccid wieners."
    scene a7928 with dssa
    mi "I may have to use my boobs as a crush weapon."
    scene a7929 with dssa
    d "That might just work."
    scene a7930 with dssr
    mi "My body isn't made for fighting."
    mi "It's made for squatting heavy... and being mounted."
    scene a7931 with dssa
    d "'Mounted.'"
    scene a7932 with dssa
    mi "I love that word. It feels so carnal."
    scene a7933 with dssa
    stop music fadeout 5
    mi "*Sensual whisper* Mount me..."
    scene black with Dissolve(2)
    with Pause(.5)
    jump VictoriaHall5x5



label VictoriaHall5x5:
    $ play_playlist(playlist_Happy)
    scene a3049 with dssb 
    pause 
    scene a3050 with dssr 
    rob "Whooo cares?"
    scene a3051 with dssa 
    sas "I do."
    scene a3052 with dssa 
    rob "Bigger is always better."
    scene a3057 with dssr
    u "It's not."
    scene a3053 with dssr 
    rob "Bigger hamburger? Good. Bigger paycheck? Good. Bigger bag of hair clips? Good."
    scene a3058 with dssr 
    u "Bigger pimples? Bad. Bigger knots in your hair? Bad. A bigger version of Sasha? Bad."
    scene a3053 with dssr 
    rob "Bigger pile of puppies? Good. Bigger stack of pancakes? Good. Bigger strap-on? Good!"
    scene a3058 with dssr 
    u "Bigger spider? Bad. Bigger hole in your sock? Bad. Bigger text from your ex? Bad."
    scene a3054 with vpunch 
    rob "Bigger boobs? Good!"
    scene a3059 with vpunch 
    u "BAD!"
    scene a3060 with vpunch
    rob "Says the one with the big boobs!"
    scene a3059 with vpunch 
    u "That's how I know they're bad!"
    scene a3054 with vpunch
    rob "Affluenza!"
    scene a3061 with dssr 
    "She undresses seductively to spite Robin."
    scene a3062 with dssa 
    u "You know what, Robin? We'll end this argument once and for all." 
    u "The day after tomorrow you'll experience real discomfort and pain." 
    scene a3055 with dssr
    rob "That's a normal Tuesday for me! I'm best friends with Sasha! She hurts me all the time!"
    scene a3063 with dssr
    sas "I don't."
    scene a3064 with dssa
    rob "You're very physical with me."
    scene a3063 with dssa
    sas "I'm not."
    scene a3065 with dssr
    u "Mmmh, you're very physical with the people you like. It's true."
    u "Half of us are covered in bruises."
    scene a3066 with dssa
    u "I haven't noticed that, Sasha- and I've known you for a few months, haha."
    scene a3067 with dssa
    u "*Mumbles* I wonder why..."
    scene a3068 with dssr
    sas "Where is Joyce?"
    scene a3069 with dssa
    u "I think she works out around this time."
    scene a3070 with dssr
    sas "Where's Joyce?"
    scene a3071 with dssr
    dwi "What Joyce?"
    scene a3072 with dssa
    sas "I think you slept with her last year."
    scene a3073 with dssa
    dwi "Uhh... I have no idea who you're talking about."
    scene a3074 with dssa
    dwi "Maybe try to describe her booty to me."
    scene a3075 with dssr
    "She rolls her eyes."
    scene a3076 with dssa 
    pause
    scene a3077 with dssa
    pause 
    scene a3078 with dssr 
    az "Hey."
    scene a3079 with dssr
    d "Hey."
    scene a3080 with dssr
    v "Hi!"
    scene a3081 with dssa
    d "Hey."
    scene a3082 with dssr
    mi "Hey! I got our books."
    scene a3083 with dssa
    v "Well done! It means we can dig deep soon!"
    scene a3084 with dssa
    v "Hi, Kate."
    scene a3085 with dssa
    kat "Hey Vic, everything's alright?"
    scene a3086 with dssr
    v "Yes, how about you?"
    if RoRum is True:
        $ FuckBoyRumour = True
        scene a3087 with dssa
        kat "Well, there's this article in the Campus Chronicle and it says [name] and I had sex."
        scene a3088 with dssr
        v "Oh."
        v "How was it?"
        scene a3089 with dssa
        kat "It didn't happen."
        scene a3090 with dssa
        v "I know."
        scene a3091 with dssa
        v "Hmm, they're not allowed to write this if it's untrue, right?"
        scene a3092 with dssa
        kat "No. They also called [name] a fuckboy."
        scene a3091 with dssa
        v "I'm sorry for you too, [name]."
        scene a3094 with dssa
        v "Why do they insult you as a fuckboy... And what even is that?"
        scene a3095 with dssa
        kat "A guy that sleeps with a lot of girls... Someone that jumps from one to another."
        scene a3096 with dssa
        v "Ah okay."
        scene a3097 with dssa
        pause 
        play sound "Music/Sfx/Punch.ogg"
        scene a3099 with vpunch
        v "You fuckboy!"
        scene a3098 with dssa
        d "Hey!"
        scene a3100 with dssa
        "She laughs."
    else:
        scene a3087 with dssa
        kat "Sure."
    if VictoriaKiss4x5 is True and VicDateEntry2 is False:
        scene a3101 with dssr
        pause 
        scene a3102 with dssr
        kat "Ohhhh, you two have something going on?"
        scene a3103 with dssa
        pause 
        scene a3104 with dssa
        mi "You bet they do."
        if BellaKiss3x5 and KateTeasing2 is True:
            scene a3105 with dssr
            kat "*Whisper* Maybe you are a fuckboy."
    scene a3107 with dssr
    v "You'll be there after school?"
    scene a3106 with dssa
    d "Yeah, for your first therapy session."
    scene a3108 with dssa
    v "Great! Maja will pick us up!"
    scene a3109 with dssr
    mi "Alright, let's head to class."
    scene a3110 with dssa
    kat "I'm late too. I'll see you later, ladies."
    scene a3111 with dssa
    mi "Later."
    if CreepNetwork_KateEntrance_1 is True:
        scene a3112 with dssa
        miri "Have you seen this?"
        scene a3113 with dssa
        kat "I did."
        scene a3114 with dssa
        miri "The audacity... Who did it?"
        scene a3115 with dssa
        kat "No idea."
        kat "I believe I pulled [name] on board."
        scene a3116 with dssa
        miri "Really?"
        scene a3117 with dssa
        kat "I'm not sure. He might need a bit more convincing."
        scene a3118 with dssa
        miri "I met him at Zara's yesterday."
        scene a3117 with dssa
        kat "I know. You texted me."
        scene a3119 with dssa
        pause
        if BellaDate is True:
            play sound "Music/Sfx/Punch.ogg"
            scene a3120 with vpunch
            pause #sfx
            scene a3121 with dssa
            miri "Don't do anything stupid."
            scene a3122 with dssa
            "Kate smiles."
            scene a3123 with dssa
            kat "I won't."
            scene a3124 with dssa
            miri "Seriously."
        else:
            play sound "Music/Sfx/Punch.ogg"
            scene a3120 with vpunch
            pause 
        scene a3125 with dssr
        kat "Where's Nora?"
        scene a3126 with dssr
        miri "Let's go to class."  
    if BellaDate is True:
        scene a3127 with dssr
        u "He's hurt."
        scene a3128 with dssr
        b "I warned you."
        scene a3129 with dssa
        "The guy exhales."
        scene a3130 with dssa
        u "I didn't mean it, okay? I was just kidding."
        scene a3131 with dssa
        b "Why are you still talking? I don't care."
        scene a3132 with dssa
        u "You will care if he takes it to Isabella."
        scene a3131 with dssa
        b "It didn't happen during a race."
        scene a3132 with dssa
        u "Every accident involving a car is subject to Isabella."
        scene a3133 with dssa
        pause 
        scene a3134 with dssr
        u "I'm not asking much of you. Just apologize to him."
        scene a3135 with dssa
        b "Sure, if you apologize to my friend, [name]."
        scene a3134 with dssa
        u "I will."
        scene a3136 with dssa
        b "Mhm, I believe it when I see it."
        scene a3137 with dssa
        u "So... he's just a friend?"
        scene a3138 with dssa
        b "No."
        scene a3139 with dssa
        u "You act like I'm asking you to pay up with your booty."
        scene a3141 with dssr
        b "I'm not sorry for hitting him."
        scene a3140 with dssa
        u "Who cares? Just do it!"
        u "Otherwise, he'll report you to Isa."
        scene a3142 with dssr
        u "She doesn't like you. She'll ban you from the canyon for a year."
        scene a3143 with dssa
        pause 
        scene a3144 with dssa
        b "Who says he won't report me anyway?"
        scene a3145 with dssa
        u "I'll make sure he doesn't."
        scene a3144 with dssa
        b "*Scoffs* Your word means nothing to me."
        scene a3145 with dssa
        u "If I lie, you can ruin my reputation in the scene."
        scene a3146 with dssr
        b "Not much to ruin, dude."
        scene a3147 with dssr
        u "Can you talk without insulting me in every other sentence?"
        u "I'm saving your ass here! I wouldn't need to do this!"
        scene a3149 with dssa
        b "Oh please, it's a desperate attempt to get a pity handjob."
        scene a3148 with dssa
        b "Alright. I'll talk to the ugly nugget."
        scene a3150 with dssr
        u "Just choose better words."
    stop music fadeout 3
    if BellaKiss3x5 is False:
        jump MarlaOffice5x5
    elif PunchPrefect2x0 is True:
        jump MarlaOffice5x5
    else:
        jump Class5x5

label MarlaOffice5x5:
    $ play_playlist(playlist_Girly)
    scene black with Dissolve(2)
    with Pause(.5) 
    scene a3158 with dssr
    pause 
    scene a3160 with dssa
    no "It looks like a dildo."
    scene a3163 with dssr
    ma "Nora. Again. It's not a dildo!"
    scene a3159 with dssr
    pause 
    scene a3161 with dssa
    pause 
    scene a3162 with dssa
    no "Are you sure?"
    scene a3164 with dssa
    pause 
    scene a3165 with dssr #sfx knock 
    pause 
    scene a3166 with dssr
    d "You wanted to see me?"
    scene a3167 with dssa
    ma "Yes, please sit down."
    scene a3168 with dssr
    if BellaKiss3x5 is False:
        no "Hi [name]!"
        scene a3169 with dssa
        d "Nora."
    else:
        no "I'm Nora!"
        scene a3169 with dssa
        d "...[name]."
    scene a3170 with dssa
    if BellaKiss3x5 is False:
        ma "You both know why you're here?"
        scene a3171 with dssa
        no "We do!"
        scene a3172 with dssa
        pause 
        scene a3173 with dssa
        ma "Well, I thought about your punishment..."
        scene a3174 with dssr
        ma "I believe making yourself useful is a much better use of resources."
        scene a3175 with dssa
        ma "You two will assist Karen with the models."
        scene a3176 with dssr
        ma "You're both reasonably attractive... Maybe she'll let you model too."
        scene a3177 with dssr
        no "*Gasp*"
        no "That's so cool!"
        scene a3178 with dssr
        d "...Do I have to do that?"
        scene a3179 with dssa
        ma "No. You can also take a three-month cleaning job and pick up trash."
        scene a3178 with dssa
        d "Assisting Karen sounds good."
        scene a3180 with dssr
        pause
        scene a3181 with dssa
        no "Can we model nude?"
        scene a3182 with dssr
        ma "You don't have to do anything you don't want to."
        ma "Karen is in need of new models... So take it or pick up trash."
        scene a3184 with dssa
        no "We'll take it."
    else:
        ma "Do you both know why you're here?"
        scene a3188 with dssa
        d "No."
        scene a3187 with dssa
        no "No."
        scene a3189 with dssa
        ma "Nora... You're here because you flashed your breasts in class... again."
        scene a3190 with vpunch
        no "I got dared!"
        scene a3191 with dssa
        ma "If someone asks you to jump off a bridge, would you do it?"
        scene a3192 with dssa
        no "How high is the bridge? And do I have to do it topless?"
        scene a3197 with dssr
        ma "*Sigh*"
        scene a3198 with dssa
        d "Why am I here?"
        scene a3199 with dssa
        ma "You assaulted a student!"
        scene a3193 with dssr
        d "I just pushed him into the bookshelves-"
        scene a3194 with dssa
        ma "You did what?"
        scene a3195 with dssa
        d "Uh... Never mind."
        scene a3196 with dssr
        ma "I was talking about Stan. A prefect of this college, who you assaulted without any reason."
        ma "You should be glad you're not being immediately expelled."
        scene a3200 with dssr
        pause
        d "...Why am I not expelled?"
        scene a3201 with dssa
        "She gives you a fake smile."
        scene a3202 with dssa
        ma "Violence is a natural occurrence. Ruining someone's future over a little violent dispute only leads to more violence." 
        scene a3203 with dssa
        ma "It's counterproductive and against what ZPR believes in."
        scene a3204 with dssa
        d "And I had my reasons-"
        scene a3205 with dssa
        ma "I don't want to hear it."
        scene a3175 with dssr
        ma "I don't believe in senseless punishment."
        scene a3176 with dssr
        ma "I'd rather put resources to good use."
        ma "You both will assist Karen with art class and modeling."
        scene a3177 with dssr
        no "How cool!"
        scene a3178 with dssr
        d "What if I decline?"
        scene a3179 with dssa
        ma "You'll pick up trash for three months."
        scene a3178 with dssa
        d "Modeling sounds good."
        scene a3180 with dssr
        pause 
        scene a3181 with dssa
        no "It's gonna be soo fun!"
        no "Are we going to model nude?"
        scene a3184 with dssr
        no "I would totally like that!"
        scene a3183 with dssa
        ma "*Mumbles* I know..."
        ma "You don't have to do anything you don't want to."
    $ McArtModel5x5 = True
    scene a3186 with dssr
    pause
    ma "As soon as Karen says you've done your deed, you're free to go."
    scene a3187 with dssa
    d "Alright."
    scene a3206 with dssr
    no "That's soo cool!"
    scene a3207 with dssa
    d "Is it?"
    scene a3209 with dssr
    no "Yes!"
    no "This is no punishment! We might even get to model!"
    scene a3208 with dssa
    d "We might be stuck assisting some pretentious models."
    scene a3210 with dssr
    no "Leave the talking to me, and we're going to be fine!"
    scene a3211 with dssa
    d "Yeah... No. You'll stick to me before you end up nude."
    scene a3212 with dssa
    no "I want to end up nude!"
    scene a3213 with dssr
    no "We should practice some poses!"
    scene a3214 with dssr
    pause 
    scene a3215 with dssa
    pause 
    scene a3216 with dssa
    pause 
    play sound "Music/Sfx/Punch.ogg"
    scene a3217 with vpunch
    pause 
    scene a3218 with dssa
    d "Ngh! Give me a warning next time!"
    scene a3219 with dssa
    pause
    menu:
        "I hate to admit it, but you can be weirdly adorable.":
            $ NoraAdorable5x5 = True
            scene a3220 with dssa
            no "Thanks!"
        "Nora, close your eyes, and count to five.":
            scene a3221 with dssa
            if BellaKiss3x5 is False:
                no "Maybe we can be cuffed together again when they draw us!"
            else:
                no "Maybe we can model nude together!"
            scene a3222 with dssa
            pause 
            scene a3223 with dssa
            no "Five!"
            scene a3224 with dssa
            no "[name]?"
            scene a3225 with dssa
            no "Where are you?"
            scene a3226 with dssr
            pause 
            scene a3227 with dssa
            no "*Sad whisper* [name]..."
    stop music fadeout 4
    scene black with Dissolve(2)
    with Pause(.5)
    jump Class5x5





label Class5x5:
    scene a190 with dssb
    pause
    scene a191 with dssr
    pause
    if NiaDate5x0 is True:
        $ play_playlist(playlist_Romance)
        scene a193 with dssr
        nia "Hey [name]."
        scene a192 with dssa
        d "Hey."
        scene a194 with dssa
        nia "How are you today?"
        scene a195 with dssa
        d "I'm good, how are you?"
        scene a194 with dssa
        nia "I'm good, too. A little tired because I went out of my way to look up what we could play after we finish Turoki."
        scene a195 with dssa
        d "First we need to finish it."
        scene a196 with dssa
        nia "Still! I'd like to have a plan."
        nia "Which is quite contrary to my normal behavior."
        scene a197 with dssa
        d "You call your usual behavior normal?"
        scene a188 with dssr
        "She laughs."
        nia "My ADHD usually prevents me from following through with plans. But! It works when I'm really into it."
        d "We wanted to go and have drinks before our next session, right?"
        nia "Yes."
        scene a198 with dssr
        d "Would you call that a date?"
        "She keeps quiet for a moment and you notice a nervous little twitch in the corner of her mouth."
        scene a199 with dssa
        nia "Would you?"
        scene a200 with dssa
        d "Do you consider it a date, Nia?"
        scene a201 with dssr
        nia "I don't knoooow!"
        scene a202 with dssa
        d "Nia."
        scene a203 with dssa
        nia "...I thought so yes."
        scene a204 with dssa
        d "Me too."
        scene a205 with dssa
        "She smiles."
        scene a206 with dssa
        nia "Hey! Why did you put me on the spot like this?!"
        scene a207 with dssa
        d "It's cute."
        nia "Pff!"
        scene a208 with dssa
        d "(I'm curious to see how she'll react...)"
        scene a209 with dssr
        "You slide your hand along her soft skin."
        "Nia says nothing and just observes you with anticipation."
        d "Do you mind it?"
        nia "Not at all... I'm quite intrigued."
        scene a210 with dssr
        "She opens her legs, allowing you to go up further..."
        scene a211 with dssa
        "Then closes them again and traps your hand between her soft, firm thighs."
        scene a212 with dssr
        nia "If I had known you'd be touching me... I would've brought spare underwear."
        scene a213 with dssa
        d "That's all it took? You get easily aroused."
        scene a212 with dssa
        nia "Always have been... And I'm not going to lie... Being in public adds to it."
        scene a214 with dssa
        d "(I can see it in her eyes... Anticipation and lust.)"
        scene a215 with dssa
        d "(It's amazing to see how heavily sexual desire impacts us... I don't think there's anything stronger than the sexual drive.)"
        scene a216 with dssa
        d "(I want to experiment more with it... See how they react to it.)"
        menu:
            "Ask her for her underwear.":
                $ NiaUnderwearS2_CH1 = True
                scene a217 with dssr
                d "(I wonder how much this desire unlocks in her... Something she wouldn't do in a non-horny state... A sober state so to speak.)"
                scene a218 with dssr
                d "Would you give me your underwear?"
                scene a219 with dssa
                nia "My thong?"
                scene a220 with dssa
                d "Yeah."
                scene a219 with dssa
                nia "Y-you really want it?"
                scene a220 with dssa
                d "Yeah."
                scene a221 with dssa
                "Nia takes a quick look around. The class is still relatively empty, but seats are slowly filling up."
                scene a222 with dssr
                pause
                scene a224 with dssr
                "Without trying to raise suspicion, she reaches below her skirt and pulls down her dampened thong."
                scene a225 with dssr
                pause
                scene a226 with dssr
                d "(The fabric is warm and slightly wet.)"
                d "Thanks."
                scene a227 with dssa
                nia "Happy?"
                scene a228 with dssr
                pause
                d "Yeah."
                scene a229 with dssr
                nia "*Giggles* You're welcome!"
                scene a230 with dssa
                d "Does this arouse you even further?"
                scene a229 with dssa
                nia "Bet your cute ass it does."
                scene a230 with dssa
                d "I'll give them back to you when we meet up."
                scene a229 with dssa
                nia "Thanks!"
                scene a231 with dssr
                nia "...And when's that?"
                scene a232 with dssa
                d "I'll tell you that over the next of days. I'm a little swamped right now."
                scene a231 with dssa
                nia "I don't mind as long as you keep doing this with me."
                scene a233 with dssr
                "She grabs your hand..."
                scene a234 with dssa
                "And moves it below her skirt... Not far enough for you to touch her pussy, but close enough to feel the heat it radiates."
                "You give her a subtle smile."
                scene a235 with dssr
                pause
            "Don't ask for her underwear.":
                pass
        scene a236 with dssr
        nia "Later [name]!"
        scene a237 with dssr
        pause
    else:
        $ play_playlist(playlist_Romance)
        scene a237 with dssr
        pause
    scene a238 with dssr
    pause
    scene a240 with dssr
    ma "Mhm."
    scene a239 with dssr
    ma "Everyone please take a seat."
    scene a241 with dssr
    if BellaNonExclusive5x0 is True:
        menu:
            "Fuck with her.":
                $ BellaJokyS2_Ch1 = True
                scene a242 with dssa
                d "Hey beautiful, I've missed you."
                scene a244 with dssr
                pause
                scene a245 with dssr
                d "What's wrong, my little tootsie roll?"
                scene a246 with dssr
                pause
                scene a247 with dssa
                pause
                scene a249 with dssr
                pause
                scene a250 with dssa
                pause
                scene a249 with dssr
                pause
                scene a251 with dssa
                b "Ohhh- you didn't get me flowers today?"
                play sound "Music/Sfx/Punch.ogg"
                scene a252 with vpunch
                b "No worries! You know all I need is you, my love!"
                scene a253 with dssa
                d "...Let's stop this. This is getting too creepy."
                scene a254 with vpunch
                b "Mhmmmaaaah."
                scene a255 with dssr
                b "*Gasps* A-are you asking me to marry you?!"
                scene a256 with dssr
                "She slides an onion ring towards you."
                scene a257 with dssr
                pause
                menu:
                    "Put the onion ring on her finger.":
                        $ BellaOnionRingS2_1x0 = True
                        $ Bella_Fiancee = True
                        scene a258 with dssr
                        pause
                        scene a259 with dssr
                        b "*Gasps* I'm the happiest girl alive!"
                        scene a260 with dssa
                        b "*Sensual whisper* I can't wait for tonight after the reception when you make me a real woman."
                        scene a261 with dssa
                        b "And then I'm going to kill you in your sleep."
                        scene a262 with dssa
                        "She takes a bite from her ring."
                        d "(...I really like this idiot.)"
                    "Eat the onion ring.":
                        scene a263 with dssa
                        "You eat the onion ring."
                        scene a264 with vpunch
                        b "That was mine!"
                        scene a266 with dssa
                        d "Who brings onion rings to class?"
                        scene a264 with dssa
                        b "I still had some leftovers! You owe me an onion ring!"
            "Greet her.":
                scene a242 with dssa
                d "Hey."
                scene a243 with dssa
                b "Hi."
    else:
        $ NoBella5x0 = True
        scene a242 with dssa
        d "Hey."
        scene a243 with dssa
        b "Hi."
    scene a267 with dssb
    "The classroom slowly fills up with students."
    if BellaNonExclusive5x0 is False:
        scene a273 with dssr
    else:
        scene a271 with dssr
    pause
    scene a274 with dssr
    d "Why so tired?"
    scene a275 with dssa
    b "I got drunk last night and had to finish a book... It got too exciting."
    scene a274 with dssa
    d "I hope it was a book on 'How not to be'."
    scene a276 with dssa
    b "I only need to look at you for that. Learn by example, you know."
    if BellaNonExclusive5x0 is True:
        scene a277 with dssr
        pause
        scene a278 with dssr
        "She swings her legs over yours."
        scene a279 with dssa
        b "*Mumbles* Stupid, dead worm..."
        b "I should punch him."
        scene a280 with dssr
        d "Pay attention."
        scene a281 with dssa
        b "*Whisper* Pay attention to me."
        b "*Whisper* Pay attention to my tits... my big, perfectly shaped tits..."
        scene a282 with dssa
        b "*Moany Whisper* My round, perfect ass..."
        scene a283 with dssa
        pause
        scene a284 with dssa
        b "*Whisper* I'm so horny."
        scene a286 with dssa
        pause
        scene a287 with dssa
        d "...Stop licking yourself."
        scene a288 with dssa
        b "Someone has to do it."
        b "...Please die in your sleep so that I can move on..."
        scene a286 with dssa
        if NiaUnderwearS2_CH1 is True:
            d "(Nia gave me her thong... I wonder if Bella would do the same.)"
        d "(I wonder what I could make Bella do in such a state... It must be torture for her.)"
        scene a289 with dssa
        d "Alright... listen... You write down the next part."
        d "And I pay some attention to your weirdly shaped legs. Deal?"
        scene a290 with dssr
        pause
        scene a291 with dssa
        b "Deal."
        scene a292 with dssr
        pause
        scene a293 with dssr
        pause
        scene a613 with dssa
        "You move in closer to the table to cover your little game."
        scene a614 with dssr
        pause
        scene a615 with dssr
        pause
        scene a616 with dssr
        pause
        scene a617 with dssa
        pause
        scene a618 with dssa
        pause
        scene a619 with dssa
        "Gently, but with some force you move your finger through the middle of her crotch."
        scene a620 with dssa
        pause
        scene a621 with dssa
        "You repeat the previous movement a few times... Slow, but with some confident pressure."
        scene a622 with dssr
        b "...My god."
        d "Girl, stop undressing."
        play sound "Music/Sfx/Punch.ogg"
        scene a623 with vpunch
        pause
        scene a624 with dssa
        d "(It's fascinating to see how strongly it impacts her... She can't think straight.)"
        d "(I'd like to explore this a little further.)"
        scene a625 with slideleft
        pause
        scene a626 with dssa
        "She moans softly, and in an irregular pattern."
        ma "Very well."
        ma "We'll see each other again in 30 minutes."
        scene a627 with dssr
        b "Oh man..."
        b "*Breathy* I- I know a place where we can continue."
        scene a628 with dssa
        "You raise a brow."
        scene a629 with dssa
        pause
        scene a630 with dssr
        b "*Breathy* Come."
        scene a631 with dssa
        menu:
            "Ask her to make Mila a compliment.":
                $ BellchenMila1 = True
                scene a632 with dssa
                b "What?"
                scene a631 with dssa
                d "Tell her she's got nice hair and I'll come with you."
                scene a633 with dssr
                b "I'm not doing that!"
                scene a634 with dssa
                d "...Are you sure?"
                scene a635 with dssa
                pause
                play sound "Music/Sfx/Slap.ogg"
                scene a636 with vpunch
                "She grabs your arm and squeezes it hard."
                scene a637 with dssa
                b "I hate you! I hope you burn alive!"
                scene a638 with dssr
                pause
                scene a639 with dssr
                pause
                scene a640 with dssa
                d "(Is she actually going to do it?)"
                scene a641 with dssa
                pause
                scene a642 with dssa
                pause
                scene a643 with dssa
                pause
                scene a644 with dssa
                pause
                scene a645 with dssa
                pause
                scene a646 with dssa
                b "...I like your hair."
                scene a647 with dssr
                mi "Umm... Thanks? I guess?"
                scene a648 with dssa
                pause
                scene a650 with dssr
                pause
                scene a649 with dssa
                v "You do have nice hair."
                stop music fadeout 3
                scene black with Dissolve(2)
                with Pause(.5)
                jump BellchenNurse
            "Don't ask her that.":
                stop music fadeout 3
                scene black with Dissolve(2)
                with Pause(.5)
                jump BellchenNurse   
    else:
        scene black with Dissolve(2)
        show text "90 minutes later." with dssr 
        hide text with Dissolve(2.5)
        jump CafeVic5x5                               
                    


label BellchenNurse:
    scene a3233 with dssb
    pause
    scene a3234 with dssa
    if bellameet is True:
        d "What's in there? And why do you have a key?"
    else:
        d "Isn't that the nurse's room?"
    scene a3235 with dssr
    b "Shhh."
    play music "Music/Vesky - Departure.ogg" fadein 5
    scene a3236 with dssb
    pause
    scene a3237 with dssa
    b "I copied my aunt's key. I thought having access to a private room to take naps might come in handy."
    scene a3238 with dssa
    d "I'd be very surprised if you make it through college without getting expelled."
    scene a3239 with dssr
    pause
    scene a3240 with dssa
    b "What brings you here? Where does it hurt?"
    scene a3239 with dssa
    d "Looking at you hurts."
    scene a3241 with dssr
    b "I see."
    b "I need to take a closer look, Sir."
    scene a3242 with dssr
    b "Please lose your shirt."
    scene a651 with dssr
    pause
    scene a652 with dssa
    b "Mhm..."
    scene a653 with dssr
    b "I don't know how to say it..."
    b "Sir, your diagnosis is-"
    scene a654 with dssa
    "She inhales deeply."
    scene a653 with dssa
    b "You're a raging homosexual."
    scene a655 with dssr
    b "So for you to both like guys and girls, I'll prescribe you the following..."
    scene a656 with dssa
    pause
    scene a657 with dssa
    "You've got to hold Bella Von Halen's breasts for 20 seconds, 3 sets a day."
    scene a658 with dssa
    d "Isn't there some sort of wonder pill?"
    scene a659 with dssa
    b "I'm sorry. We ran out of cyanide."
    scene a660 with dssa
    pause
    scene a661 with dssa
    pause
    scene a662 with dssa
    pause
    scene a663 with dssa
    "She jumps into your arms and steers her nails into your back."
    play sound "Music/Sfx/Thud3.ogg"
    scene a664 with vpunch
    "You slam her against the wall and soften the impact with your hand."
    scene a665 with vpunch
    "Two fingers are all it takes to make her squirm... You rub her pussy through the already damp fabric, and in an effort to increase friction, she grinds her pelvis against you."
    scene a666 with vpunch
    "Bella raises her leg to give you better access to her most intimate area... Kicking over a plant in the process."
    scene a670 with dssr
    pause
    scene a671 with dssa
    d "...I think it's helping."
    scene a672 with dssa
    b "I have a PhD in boobs. Trust the professional."
    scene a673 with dssa
    d "Well, can I use anyone's boobs for it?"
    scene a674 with dssa
    b "No. It must be a Von Halen."
    menu:
        "So your Mother...":
            $ Bella_H +=1
            scene a675 with dssa
            b "Good. I wanted to see if you were going to mention her."
            scene a677 with dssa
            d "And I did."
            scene a675 with dssa
            b "I respect it."
            scene a676 with dssa
            b "I mean... If you'd ever touch my Mama's boobs I'd kill you."
            scene a678 with dssa
            d "Sure. Now go eat your vegetables. Your Mother and I have to discuss your slutty behavior, young lady."
        "Don't say it.":
            scene a675 with dssa
            $ Bella_H -=1
            d "I see."
            scene a678 with vpunch
            "You predict her next move and prevent her from getting up and wrestling you."
    d "I think we'll need to be out in a minute."
    scene a679 with dssr
    b "*Whisper* Mhm."
    d "Don't you masturbate?"
    $ BellaMasturbationS2_1x0 = True
    scene a680 with dssa
    b "Mh? If I masturbate?"
    scene a681 with dssa
    d "Yeah."
    scene a680 with dssa
    b "I do... You saw some of my toys."
    scene a681 with dssa
    d "Ah right... The Claire incident."
    scene a681 with dssa
    d "Then why are you so horny all the time?"
    scene a680 with dssa
    b "Only a purebred virgin would say that."
    scene a682 with dssa
    pause
    scene a683 with dssr
    b "It's not the same... Doing it yourself satisfies the sexual need but... There's so much more."
    b "Of course, real sex also feels better and you don't have to do all the work."
    b "There's an emotional and primal component that masturbation just can't satisfy."
    scene a684 with dssa
    b "And it just so happens that I'm emotionally addicted to you."
    scene a685 with dssa
    b "It makes me crave you..."
    scene a686 with dssa
    b "It makes me want to rip off your clothes and ride you until one of us passes out..."
    scene a687 with dssa
    b "...But to answer your question... Sex will always be better, however, I do enjoy doing it myself as my impressive collection of toys might give away..."
    scene a688 with dssa
    d "Maybe you can show me someday."
    scene a689 with dssa
    if Sanitized is True:
        b "You want to see me masturbate?"
    else:
        b "Wait. Which one? You want to see me have sex or masturbate?"
        scene a688 with dssa
        d "What do you think?"
        scene a689 with dssa
        b "Alright, I'll keep an eye out for someone else..."
        scene a688 with dssa
        d "Idiot."
        scene a689 with dssa
        "She giggles."
        b "So... You want to see me masturbate?"
    scene a690 with dssa
    d "I do."
    scene a692 with dssr
    b "Did you ever...?"
    scene a693 with dssa
    d "When I was young it happened by accident but no... I never did it."
    scene a691 with dssa
    b "Man, you're so fucked."
    scene a694 with dssa
    "You notice sadness in her voice... Some real, intense sadness."
    scene a695 with dssa
    pause
    scene a696 with dssr
    d "I'm surprised someone like you puts up with it."
    scene a697 with dssa
    b "Who's someone like me?"
    scene a698 with dssa
    d "You seem like someone who's sexually active and needs it a lot. And if someone doesn't meet your standards, you move on."
    scene a699 with dssa
    b "I don't just throw people away. I might sometimes dress like a hoe, but I'm a lady."
    b "I even considered being your girlfriend the other day before I came back to my senses."
    scene a700 with dssa
    menu:
        "Were you ever in a relationship before?":
            scene a697 with dssa
            b "Yeah."
            scene a701 with dssa
            d "If we ignore your obvious shortcomings... How come it ended?"
            scene a748 with dssa
            b "Multiple reasons. I grew out of it. I was a different person back then."
            scene a701 with dssa
            d "What wasn't for you? The person or the relationship?"
            scene a748 with dssa
            b "Both."
            b "I like my freedom... I like to go out dancing with my friends, get drunk, get some cheese fries without answering to anyone."
            b "It wasn't a bad relationship, but I always knew it wasn't really meant to be."
            b "And before you ask me why I considered it with you..."
            scene a749 with dssa
            b "... Ugh... I'm going to barf..."
            scene a750 with dssa
            b "...What you make me feel, I have never felt before."
            b "You know how it is when you meet someone and it's just... a moment? You enjoy it, but you know it won't last?"
            b "It's not supposed to be more... Just one of many moments."
            b "I don't have that with you..."
            b "With you I'm afraid it won't last..."
            b "It's like we've known each other for a long time."
            scene a751 with dssr
            b "It feels natural... Like it's supposed to be."
            scene a752 with dssa
            b "And I know you feel the same."
            scene a753 with dssa
            d "I guess I do."
            scene a754 with dssa
            d "I still cringe when you act all disgusted, though. Grow some balls, bitch. Admitting that you're fond of another person isn't weak."
            d "It makes you feel vulnerable, sure. But deal with it in grace."
            d "You can play the bitch card if you're unsure if the other person feels the same... But you should know that I do."
            scene a755 with dssa
            pause
            scene a756 with dssr
            pause
            scene a757 with dssa
            b "I still hate it."
            b "You put me into a position I don't want to be in..."
            scene a758 with dssr
            d "The way to go is to let fate take its course... and with favorable winds, we'll end up in the same harbor."
            scene a759 with dssa
            pause
            scene a760 with dssa
            b "How long were you with Summer?"
            scene a761 with dssa
            d "Over two years."
            scene a760 with dssa
            b "That was a long time for your age."
            scene a762 with dssa
            b "...Do you think you'd still be together if-"
            scene a763 with dssa
            d "-I don't know."
            scene a764 with dssa
            b "Aaaanyways... Before you completely shut off... We should go to my Mama's house in the mountains for a weekend."
            scene a765 with dssr
            d "Where is it?"
            scene a766 with dssa
            b "A few hours away and it's beautiful. In the middle of the woods surrounded by an ocean of pine trees."
            scene a767 with dssa
            d "Sounds good."
            scene a768 with dssa
            b "Alright. Let's fix your damaged pipe, because I won't go there with you before that."
            scene a769 with dssa
            d "That makes sense. I wouldn't like to listen to you cry all day."
            scene a770 with dssa
            b "Instead, you'll listen to me moan all day."
            scene a771 with dssa
            pause
            scene a772 with dssa
            pause
            pause #TD animation
            scene a800 with dssr
            pause
            scene a801 with dssa
            b "*Whispers* I'm going insane... My pants are drenched..."
            scene a802 with dssa
            menu:
                "Could you be with me if we would never have sex?":
                    $ ICBWY = True
                    scene a803 with dssa
                    b "Sex as in penetration?"
                    scene a802 with dssa
                    d "Yeah."
                    scene a805 with dssa
                    pause
                    scene a806 with dssa
                    b "No. I couldn't."
                    scene a807 with dssa
                    b "If someday we'll wake up together and we're both in the mood, I would want you inside of me..."
                    b "I don't want to miss out on spontaneous acts."
                    scene a806 with dssa
                    b "I guess most people would say 'But of course! I'm with you because of you!'"
                    b "'It tooootally doesn't bother me that I'll go through life sexually unsatisfied and with a huge grudge.'"
                    scene a808 with dssa
                    b "But it's bullshit. They're lying to themselves."
                    b "I know I'd get frustrated eventually. There's just some things I don't want to miss out on."
                    scene a809 with dssa
                    b "...Doing it with you in my Mama's office for example."
                    scene a808 with dssa
                    b "So no... I wouldn't want to be in a serious relationship with you- well, anyone if we couldn't have sex... It was the second biggest reason why I didn't say yes to us. I don't know whether we're sexually compatible."
                    b "The biggest reason being that if trust gets broken once, we're done."
                    scene a810 with dssa
                    b "But of course, this doesn't mean I'm putting any pressure on you... I know it takes time... And as you can see I'm still here."
                    b "And... And I'll still be here in three months."
                    scene a809 with dssa
                    b "But the second this dead pocket rocket wakes up... I'll put him through heaven and hell."
                "Don't ask her that.":
                    pass
            scene a811 with dssr
            b "As I said before... I've never felt anything close to what I feel with you."
            b "It's incomprehensible to me and doesn't follow any logic."
            scene a812 with dssa
            d "Objectively I should dislike you... Hell, I think I do dislike you... But there's something about you that speaks to me on a level that only Summer reached before."
            play sound "Music/Sfx/Punch.ogg"
            scene a813 with vpunch
            pause
            scene a814 with dssa
            pause
            scene a815 with dssa
            "She wishes away a few accidental tears."
            scene a816 with dssa
            pause
            scene a817 with dssa
            b "...You're still gay."
            scene black with Dissolve(2)
            with Pause(.5)
        "It was the right decision.":
            scene a697 with dssa
            b "I think so too."
            b "We're both wildcards and we tend to do things that aren't particularly well thought out."
            scene a699 with dssa
            b "We're too impulsive."
            scene a700 with dssa
            d "You more than I."
            scene a697 with dssa
            b "No argument there."
            scene a811 with dssr
            b "As I said before... I've never felt anything close to what I feel with you."
            b "It's incomprehensible to me and doesn't follow any logic."
            scene a812 with dssa
            d "Objectively I should dislike you... Hell, I think I do dislike you... But there's something about you that speaks to me on level that only Summer reached before."
            scene a813 with vpunch
            pause
            scene a814 with dssa
            pause
            scene a815 with dssa
            "She wishes away a few accidental tears."
            scene a816 with dssa
            pause
            scene a817 with dssa
            b "...You're still gay."
    stop music fadeout 25
    scene black with Dissolve(2)
    with Pause(.5)
    scene a833 with dssb
    pause
    scene a834 with dssr
    b "Let's go."
    scene a835 with dssa
    d "...You might wanna check your pants first."
    scene a836 with dssr
    b "What?"
    d "They have become translucent at the crotch."
    scene a837 with dssr
    b "Really?"
    scene a838 with dssr
    d "I can see... well, everything."
    scene a839 with dssa
    b "Oh damn."
    scene a840 with dssr
    b "You need to get me my emergency leggings."
    scene a841 with dssa
    d "Or... I just leave you here."
    scene a840 with dssa
    b "I dare you."
    scene a842 with dssa
    d "*Sigh* Where are they?"
    scene a843 with dssa
    b "In the backseat of my car."
    scene a844 with dssr
    d "Give me your keys and I'll get them."
    scene a845 with dssa
    b "Be fast! I don't know when Claire gets back."
    scene a846 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    jump BellaCarPants


label BellaCarPants:
    play ambient "Music/Sfx/Ambient_Suburban.ogg"
    scene a3243 with dssb
    pause
    scene a3244 with dssa
    pause
    scene a3245 with dssr
    saki "Would you confirm that the professor is a little bit too handsy?"
    scene a3246 with dssa
    u "No."
    scene a3247 with dssr
    saki "Aubrey, did or do you have a sexual relationship with the aforementioned professor?"
    scene a3248 with vpunch
    aub "NO!"
    scene a3249 with dssa #sfx writing
    "She scribbles something into her notebook."
    scene a3250 with dssa
    aub "What are you writing there?!"
    play sound "Music/Sfx/Punch.ogg"
    scene a3251 with vpunch
    saki "HEY!"
    play sound "Music/Sfx/Punch.ogg"
    scene a3252 with vpunch
    aub "GIVE ME THAT!"
    scene a3253 with dssa
    pause 
    scene a3254 with dssa
    pause 
    scene a3255 with dssr
    eva "...Okay."
    scene a3256 with dssa 
    "Eva spots some suspicious movement around Bella's car."
    scene a3257 with vpunch 
    eva "What are you doing?"
    scene a3258 with dssa 
    d "What does it look like? I'm stealing her car."
    scene a3259 with vpunch 
    eva "GIVE ME THE KEYS!"
    scene a3260 with dssa
    d "Relax. She gave me the keys."
    scene a3271 with dssr
    eva "I don't believe you! Why would she do that?"
    scene a3272 with dssa
    d "She needs a spare pair of pants."
    scene a3273 with dssa
    eva "...Why?"
    scene a3261 with dssr
    d "None of your business."
    scene a3262 with dssa
    d "(There are no pants.)"
    scene a3263 with dssa
    eva "Mhm... Alright."
    scene a3264 with dssr
    eva "I confirmed it."
    scene a3265 with dssa
    d "Okay... There are no pants in here."
    scene a3266 with dssa
    eva "Oh... OH! Right... Ayua borrowed them."
    scene a3267 with dssr
    pause
    scene a3268 with dssa
    pause
    scene a3269 with dssr
    d "Why are you following me?"
    scene a3270 with dssa
    stop ambient fadeout 5
    $ play_playlist(playlist_Happy)
    eva "I want to see Bella."
    scene a3274 with slideleft
    pause
    scene a3275 with dssb
    lay "Hey!"
    scene a3276 with dssr
    lay "[name]. If you're free..."
    lay "Wanna join us at Yoga?"
    scene a3277 with dssa
    d "...Yoga?"
    scene a3278 with dssa
    lay "I mentioned it to you during the last mandatory gym session."
    scene a3280 with dssa
    d "Well, I'm kinda busy right now. Another time... Maybe."
    scene a3278 with dssa
    lay "Let me know if you change your mind."
    scene a3279 with dssr
    pause
    scene a3281 with dssa
    lay "You should come too, Eva."
    scene a3282 with dssr
    eva "Yeah, maybe."
    scene a3283 with dssr
    eva "They won't let you in there."
    scene a3284 with dssa
    d "And why's that?"
    scene a3285 with dssa
    eva "The woman who teaches the course is special."
    scene a3286 with dssa
    eva "She's known to be quite misandristic. They say she stomped on her ex's balls."
    scene a3287 with dssa
    eva "I used to do ballet. She was our teacher. I know her well."
    scene a3288 with dssa
    eva "She hates guys. But what she hates even more are guys like you."
    scene a3289 with dssa
    d "And what are guys like me?"
    scene a3288 with dssa
    eva "Jerks."
    scene a3289 with dssa
    d "Mh."
    scene a3290 with dssr
    rob "Hey."
    scene a3291 with dssa
    rob "Do you by any chance know when Mila wanted to look at the housing? I might have something on my hands."
    scene a3292 with dssa
    d "I think she'll get back to us about it soon."
    scene a3293 with dssa
    rob "Okay, great."
    scene a3294 with dssr
    d "She should be in Marla's big classroom."
    scene a3295 with dssa
    rob "I'll go find her. Thanks."
    if RoRum is True:
        scene a3296 with dssa
        d "I assume you heard about us being on the Campus Chronicle?"
        scene a3297 with dssa
        rob "Uhh- no?"
        scene a3298 with dssa
        d "Yeah, you might wanna check that out."
        scene a3299 with dssa
        rob "I will. What did it say?"
        scene a3300 with dssa
        d "That we had sex."
        scene a3301 with dssa
        "She takes a moment-"
        scene a3302 with dssa
        "-then walks away at a fast pace."
        scene a3303 with dssa
        eva "Poor girl."
        scene a3304 with dssr
        eva "Being falsely accused of a sex scandal is one thing..."
        eva "But with you?"
        scene a3305 with dssa
        pause 
        scene a3306 with dssa
        menu:
            "Tease her.":
                $ Eva_Tease_ByTheEndOfTheYear = True 
                scene a3307 with dssa
                d "This shit talk of yours is how Bella and I started."
                d "If you're not careful, you and I are going to have a real one before the end of the year."
                scene a3308 with dssa
                eva "Never!"
                scene a3309 with dssa
                d "That's what Bella said too... Look at her now."
                scene a3310 with dssa
                eva "She's just confused! She'll get back to her senses! You'll see."
                scene a3311 with dssa
                d "It will take you a few minutes to get back to your senses... You'll see."
                scene a3312 with dssr
                eva "I'll tell Bella you said this."
                scene a3313 with dssa
            "Don't tease the Bean.":
                scene a3313 with dssr
                pass 
    else:
        scene a3313 with dssr
    d "What's the history between Robin and Bella?"
    scene a3314 with dssa
    eva "I don't know? I didn't even know they had history."
    scene a3315 with dssa
    d "For how long have you known Bella?"
    scene a3314 with dssa
    eva "For some time."
    scene a3315 with dssa
    d "Even I know there's something going on."
    scene a3316 with dssa
    eva "Then ask her!"
    scene a3317 with dssa
    d "Don't get mad at me. She's the one who didn't tell you."
    scene a3318 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene a847 with dssb
    pause
    play sound "Music/Sfx/DoorOpen.ogg"
    scene a848 with vpunch
    "The door opens."
    scene a849 with dssa
    b "What took you so long?!"
    scene a850 with dssa
    d "We made a few stops."
    scene a851 with dssa
    eva "So this Rob-"
    scene a852 with dssr
    b "The pants."
    scene a853 with dssr
    eva "...What did you two do here?"
    scene a854 with dssa
    pause
    scene a855 with dssr
    eva "Did you fuck her?"
    scene a856 with dssa
    d "No."
    scene a858 with dssa
    pause
    scene a857 with dssa
    eva "And why not?"
    scene a865 with dssr
    b "My exact question."
    scene a866 with dssa
    d "There were no pants."
    scene a867 with vpunch
    b "What?!"
    scene a859 with dssr
    eva "Ayua borrowed them, remember? At the Evoly club. When she had that friendly fight with the guy from the security and landed in the mud?"
    scene a860 with dssa
    b "Fuck..."
    scene a859 with dssa
    eva "Speaking of parties... I got invited to a frat party by INA."
    eva "Are we going?"
    scene a860 with dssa
    b "Yeah, why not."
    scene a868 with dssr
    b "I still need some pants!"
    scene a869 with dssr
    eva "How bad is it?"
    scene a870 with dssa
    pause
    scene a861 with dssr
    eva "It's because you're wearing nothing underneath."
    scene a862 with dssa
    b "Duh. Look at these pants. You don't wear anything under them."
    scene a863 with dssa
    eva "Uhh- yes you do!"
    scene a864 with dssa
    eva "Let me go check my locker."
    scene a871 with dssr
    b "Now's the time to finish any leftover business you had with me."
    scene a883 with dssa
    pause
    scene a884 with dssa
    b "I hate you so much."
    scene a885 with dssa
    "Quietly, you take a few steps towards her."
    d "How about you speak your mind once in a while? If you want something, tell me."
    scene a886 with dssa
    b "I want you dead."
    scene a887 with dssa
    d "I'd rather be dead than end up with you."
    scene a888 with dssa
    pause
    scene a889 with dssa
    pause
    scene a890 with dssr
    "Her hand rests calmly on yours until she gently rubs her fingers against yours."
    scene a891 with dssa
    pause
    d "I'll talk to your Mom soon..."
    scene a892 with dssa
    "She nods repeatedly in agreement."
    scene a893 with dssr
    eva "Sorry. I got nothing."
    scene a894 with dssa
    eva "Do you want my thong?"
    scene a895 with dssa
    b "Yeah, I think so."
    scene a896 with dssa
    eva "Turn around."
    scene a897 with dssa
    pause
    scene a898 with dssr
    d "You're not really going to give her your underwear?"
    scene a899 with dssa
    eva "I need to take my dress off."
    scene a900 with dssa
    pause
    scene a901 with dssa
    b "I told you."
    eva "Mh."
    scene a902 with dssa
    d "Mh?"
    scene a903 with dssa
    eva "You didn't peek."
    scene a904 with dssa
    pause
    scene a905 with dssa
    b "Alright."
    scene a906 with dssa
    pause
    scene a907 with dssr
    pause
    scene a908 with vpunch
    eva "HEY!"
    d "...She said alright and tugged on my arm."
    scene a909 with dssa
    "Bella laughs."
    scene a910 with dssa
    b "I knew it would work."
    scene a911 with dssa
    d "Finish up."
    scene a912 with dssa
    pause #pants on
    scene black with Dissolve(2)
    with Pause(.5)
    scene a914 with dssr
    pause
    scene a913 with dssa
    b "Love you."
    scene a915 with dssr
    pause
    scene a916 with dssa
    if BellaJokyS2_Ch1 is True:
        "She squints her eyes."
        scene a917 with dssr
        eva "Don't you dare give me a kiss."
        scene a919 with dssa
        menu:
            "Don't tell me what to do. (Give her a kiss.)":
                $ EvaCheekKissS2_Ch1 = True
                if EvaTrigger5x0 is True:
                    scene a921 with vpunch
                    "In the last possible moment she turns her head."
                    pause
                    menu:
                        "Break it immediately.":
                            scene a1029 with dssr
                            d "Don't tell me what to do."
                            scene a1029 with dssr
                            eva "Eww! Bella! He kissed me!"
                            scene a1030 with dssa
                            b "Yeah, I know it's disgusting."
                            scene a1031 with dssa
                            pause
                            scene a1032 with dssr
                            b "*Whisper* I'm always the last person you kiss."
                            play sound "Music/Sfx/Slap.ogg"
                            scene a1033 with vpunch
                            pause
                        "Turn it into a french kiss.":
                            $ CheatingKick = True 
                            $ EvaFrenchKissS2_1x0 = True
                            scene a1021 with dssa
                            pause
                            scene a1022 with dssr
                            pause
                            scene a1023 with dssr
                            pause
                            scene a1024 with dssa
                            "The short, yet weirdly intense kiss ends as fast as it started."
                            scene a1025 with dssa
                            b "What? Can we go?"
                            scene a1026 with dssa
                            d "Yeah."
                            scene a1027 with dssa
                            d "(...Why did I do that... with Bella just there!)" 
                            d "(I better get a hold of myself.)"
                            play sound "Music/Sfx/Punch.ogg"
                            scene a1028 with vpunch
                            "Eva slaps you on the back."
                else:
                    scene a920 with dssa
                    pause 
                    scene a1029 with dssr
                    eva "Eww! Bella! He kissed me!"
                    scene a1030 with dssa
                    b "Yeah, I know it's disgusting."
                    scene a1031 with dssa
                    pause
                    scene a1032 with dssr
                    b "*Whisper* I'm always the last person you kiss."
                    play sound "Music/Sfx/Slap.ogg"
                    scene a1033 with vpunch
                    pause
                    
            "Don't give her a peck.":
                scene a1034 with dssa
                d "Certainly not."
                scene a1035 with dssa
                pause

    else:
        pass
    jump CafeVic5x5



label CafeVic5x5:
    scene black with Dissolve(2)
    with Pause(.5)
    scene a3319 with dssr 
    b "Let's head to the library. We're missing so many books, and I'll break your bones if we fail this assignment."
    scene a3320 with dssa 
    d "Any idea where that door leads?"
    scene a3321 with dssa 
    b "Nope."
    scene a3322 with dssr 
    d "I'll see you at the library. I'll have a quick chat with Marla."
    scene a3323 with dssr 
    b "...Hurry up."
    scene a3324 with dssr 
    pause
    stop music fadeout 4
    scene black with Dissolve(2)
    with Pause(.5)
    jump MarlaDachCH1

label MarlaDachCH1:
    $ play_playlist(playlist_Grace)
    scene a3325 with dssb 
    pause
    scene a3326 with dssr
    pause
    scene a3327 with dssr
    pause
    scene a3328 with dssr
    d "Hey."
    play sound "Music/Sfx/Punch.ogg"
    scene a3329 with vpunch
    ma "*Gasp*"
    scene a3330 with dssa
    ma "What are you doing here?!"
    scene a3331 with dssa
    d "I wanted to talk to you."
    scene a3330 with dssa
    ma "You're not allowed to be up here."
    scene a3331 with dssa
    d "Can I ask you something about Victoria?"
    scene a3332 with dssa
    ma "I don't think this is any of your business."
    scene a3333 with dssa
    d "I worry about her."
    scene a3334 with dssa
    pause
    scene a3335 with dssr
    d "I know you talked but... I'm unsure what to make of it."
    ma "Victoria is being counseled by our school counselor."
    scene a3336 with dssr
    ma "If you know something we don't, speak your mind."
    scene a3337 with dssa
    d "I have suspicions."
    scene a3338 with dssa
    pause 
    scene a3339 with dssa
    if AMMC is False:
        ma "I have to ask you to please leave this roof."
        scene a3341 with dssa
        ma "If you need to talk to me, do so after class. Not on the roof."
        scene a3342 with dssa
        pause
        scene a3345 with dssr
        pause 
    else:
        ma "Anything else?"
        scene a3340 with dssa
        d "I see that you've changed. Amber knows what she's doing."
        scene a3341 with dssa
        "She keeps quiet and sits down on the edge."
        scene a3342 with dssa
        ma "...She finds the right words."
        menu:
            "Sit next to her and mention a session together.":
                $ MarlaHAYD = True
                scene a3346 with dssr
                d "She asked me the other day for us to have a session together."
                d "Amber thinks you'd benefit from it."
                scene a3347 with dssa
                ma "I'm not sure I would."
                scene a3346 with dssa
                d "I think you do."
                d "I will ask her about it if you're okay with it."
                scene a3347 with dssa
                ma "I am."
                scene a3348 with dssr
                ma "I've heard you were at the book club."
                scene a3349 with dssa
                d "You know about it?"
                scene a3348 with dssa
                ma "I know someone who goes there. She mentioned you."
                scene a3349 with dssa
                d "Who was it?" 
                scene a3348 with dssa
                ma "Our Registrar, Maddie Throne."
                scene a3350 with dssa
                d "What else did she say?"
                scene a3351 with dssa
                ma "That you challenged Charlie."
                scene a3349 with dssa
                d "Maybe a little."
                scene a3350 with dssa
                d "To me, they all seemed like horny, middle-aged women."
                scene a3351 with dssa
                ma "The book club is an excuse to drink, gossip, and talk about smut."
                scene a3350 with dssa
                d "They're reading a book about a panda and a butterfly."
                scene a3352 with dssa
                ma "Noo?"
                scene a3353 with dssa
                d "Yeah."
                scene a3354 with dssa
                "She chuckles."
                scene a3353 with dssa
                d "But Noji mentioned that they only did it to get rid of someone."
                scene a3355 with dssa
                ma "That makes more sense."
                scene a3356 with dssa
                d "Were you ever there?"
                scene a3355 with dssa
                ma "No, you only get in there if you're approved by Charlie."
                scene a3356 with dssa
                d "She didn't approve you?"
                scene a3357 with dssa
                ma "Nobody has recommended me yet."
                scene a3358 with dssa
                d "Oh, I'm not in Charlie's good graces, so whoever I recommend will be shut down."
                scene a3359 with dssa
                ma "I don't want you to recommend me. That's... embarrassing."
                scene a3361 with dssr
                d "Why?"
                scene a3360 with dssa
                ma "You're a kid. If someone recommends me, let it be someone of age."
                scene a3361 with dssa
                d "I'm very mature for my age."
                d "Maybe I can ask Noji to recommend you."
                scene a3362 with dssa
                ma "Nojiko, I remember her."
                scene a3363 with dssr
                d "(I need to be careful now.)"
                scene a3364 with dssa
                d "Do you know her?"
                scene a3365 with dssa
                ma "I know she lives with you, but besides that I only know that she's a very private person."
                scene a3364 with dssa
                d "Does she know you?"
                scene a3365 with dssa
                ma "She has seen me a few times but we've never interacted enough to really remember each other."
                scene a3366 with dssr
                ma "Nojiko is a little bit younger than me, yet refuses to age..."
                scene a3367 with dssa
                ma "I hate her."
                scene a3368 with dssa
                "A subtle chuckle escapes you."
                scene a3369 with dssa
                pause
                scene a3370 with dssr
                d "Don't jump, okay? Amber would hate that."
                scene a3371 with dssa
                "She laughs."
                scene a3372 with dssr
                pause 
                scene a3373 with dssr
                pause 
            "Leave the roof.":
                scene a3343 with dssa
                pause 
                scene a3344 with dssa
                d "Don't jump. Amber would hate that."
                scene a3345 with dssa
                "She puffs out air."
    stop music fadeout 4
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Smooth)
    scene a3374 with dssr
    pause 
    scene a3375 with dssa
    b "I advanced three levels in Wormy Crush."
    scene a3376 with dssa
    d "The biggest accomplishment you'll ever have."
    if BellaOnionRingS2_1x0 is True:
        scene a3377 with dssa
        b "We got engaged today... Mh, yeah, those three levels still made me feel more..."
        scene a3378 with dssa
        b "Unless you throw me around in my wedding dress tonight."
        scene a3379 with dssa
        d "You're the horniest noodle I've ever met."
        scene a3380 with dssa
        b "I have nothing on Nadia."
        scene a3379 with dssa
        d "Is sex and cars all you think about?"
        scene a3381 with dssa
        b "I've told you before it's because of all the edging you put me through!"
        scene a3382 with vpunch
        b "I'm being tortured! Of course, all I can think about is to end the unending torture!"
        scene a3383 with dssa
        b "I'm trapped in a void of endless suffering and desire... and you... the one who pushed me in here... is my only way out."
        scene a3384 with dssa
        pause 
        scene a3385 with dssa
        pause 
        scene a3386 with dssa
        b "Stop teasing me."
        scene a3387 with dssa
        b "Mhhhh! Noooo!"
        scene a3388 with vpunch
        pause 
        scene a3395 with dssr
        u "Ugh... Get a room."
        scene a3396 with dssa
        u "That's just disgusting."
        scene a3397 with dssa
        pause 
        scene a3398 with dssa
        na "Aww!"
        scene a3389 with dssr
        pause 
        scene a3390 with dssa
        b "I don't know how long I can keep doing this..."
        scene a3391 with dssa
        d "Believe it... I want it too."
        scene a3392 with dssa
        b "That's the first time you've directly said you want to sleep with me."
        b "...DIS-GUST-ING!"
        scene a3393 with dssa
        b "The next time we're at my place- no... never mind."
        scene a3394 with dssa
        b "We need to get some work done!"
    scene a3399 with dssr
    b "To the library?"
    scene a3400 with dssa
    d "Yes, let's fill your head with something useful for once."
    scene a3401 with dssr
    v "Hi! Would you two like to come with me to the cafe?"
    scene a3402 with dssa
    "You and Bella share a look."
    scene a3403 with dssa
    d "Yeah."
    scene a3404 with dssr
    b "Yeah?"
    scene a3405 with dssa
    d "Yes."
    scene a3406 with dssr
    d "(Getting Vic and Bella together might benefit both.)"
    scene a3407 with dssa
    v "Sai!"
    scene a3408a with dssa
    v "Do you want to come with us to the cafe?"
    scene a3409a with dssa
    "He takes a look at you and Bella."
    scene a3410a with dssa
    sai "No thanks, Vic."
    scene a3408 with dssr
    b "Why would you ask this bitch to come with us?"
    scene a3409 with dssa
    v "Please don't say that. He's nice."
    scene a3410 with dssr
    v "I knowwww that you and Sai fought."
    v "I wanted to hear both sides before I pass judgement on someone."
    scene a3411 with dssa
    d "And who received your judgement?"
    scene a3412 with dssa
    v "No one. I think it was just a misunderstanding."
    scene a3413 with dssa
    d "You do you, Vic."
    if BellaDate is False and VicDate is True:
        scene a3414 with dssa
        "Victoria blushes, and holds on to the fabric of your pants."
        scene a3415 with dssa
        pause
        scene a3416 with dssa
        b "Alright, don't do this at the cafe or I'm gone."
    elif BellaNonExclusive5x0 and BellaVictoriaKiss5x0 is True:
        $ BellaVicF5x5 = True
        scene a3417 with dssr
        "You notice how Bella observes Victoria and you."
        d "(She didn't forget that I kissed Vic.)"
        d "(She can clearly see Vic's affection for me.)"
        d "(But her face is soft... It's not her usual fuck you attitude.)"
        scene a3418 with dssa
        pause 
        scene a3419 with dssa
        b "What are you looking at, dumbass?"
        scene a3420 with dssa
        "You chuckle."
        scene a3421 with vpunch
        b "Fuck off!"
    elif BellaNonExclusive5x0 is True and BellaVictoriaKiss5x0 is False:
        scene a3417 with dssr
        "You notice how Bella observes Victoria."
        "With big, dreamy eyes she looks at her."
        scene a3418 with dssa
        pause 
        scene a3419 with dssa
        b "What are you looking at, dumbass?"
        scene a3420 with dssa
        "You chuckle."
        scene a3421 with vpunch
        b "Fuck off!"
    scene a3422 with dssr
    b "We don't have much time."
    stop music fadeout 3
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Cafe)
    scene b219 with dssb
    pause
    scene b224 with dssr
    v "How is your project coming along?"
    scene b225 with dssa
    d "I'm not sure."
    scene b230 with dssr
    pause
    scene b231 with dssa
    b "It's not going well."
    scene b232 with dssa
    b "We need to put more hours in."
    if NoBella5x0 is True:
        b "If I had a better project partner, things would look different."
        scene b226 with dssr
        if VicDate is True:
            v "I can talk to Miss Marla and ask her if we can switch partners."
            scene b233 with dssr
            b "No way in hell would I accept Mila as my project partner."
            b "I'd rather drop out of college, sell my body for $20 bareback on the side of the street, and overdose on heroin mixed with cheese fries while pregnant."
            scene b227 with dssr
            v "That's... oddly specific."
        v "But I'm sure [name]'s doing his best!"
        scene b229 with dssr
        d "I'm not."
        d "I want to see Bella fail."
        scene b228 with dssa
        v "Meaaaan!"
    if BellaNonExclusive5x0 is True:
        scene b234 with dssr
        b "*Sigh* My place after school."
    else:
        scene b234 with dssr
        b "We're going to my place after school. No discussion."
    scene b235 with dssa
    d "I can't."
    scene b236 with vpunch
    b "Why not you stupid bitch?! Do you want us to fail?!"
    scene b237 with dssa
    d "Vic has her first therapy session, and I promised to be there for emotional support."
    scene b238 with dssa
    pause
    scene b239 with dssa
    b "Oh, I see. Okay."
    scene b240 with dssa
    d "(It's so weird to see how soft she gets when it's about Victoria. Double standards.)"
    scene b249 with dssr
    d "I totally forgot that I had training yesterday."
    scene b250 with dssa
    v "That's not good. It's important to stay active!"
    scene b251 with dssa
    v "I think you need a muffin."
    scene b252 with dssr
    d "I'm good. I'm not hungry. But I do need to use the toilet."
    scene b221 with vpunch
    "Victoria grabs you by the neck and pulls you towards her."
    if VicEroticBook4x5 and NoBella5x0 is True:
        scene b221a with dssa
        v "*Whispers* That's not the muffin I was talking about." 
    else:
        scene b221a with dssa
        v "How dare you decline a free blueberry muffin... This will have consequences."
        scene b221 with dssa
        d "Oh yeah? Which ones?"
        scene b221a with dssa
        v "You'll see!"
    scene b253 with dssr
    pause
    if VicDate is True and BellaNonExclusive5x0 is False:
        menu:
            "Touch her boob in passing.":
                $ VicBoobyTouchS2_1x0 = True
                scene b254 with dssa
                pause
                scene b255 with dssa
                pause
            "Don't touch her booby.":
                pass
    scene b256 with dssr
    b "Can I ask you something?"
    scene b257 with dssa
    v "Sure!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene a3424 with dssr
    u "How did it go?"
    scene a3423 with dssa
    v "She got mad at me for it, so I didn't push it."
    scene a3425 with dssa
    "She sighs."
    scene a3426 with dssr
    pause
    scene a3427 with dssr
    pause
    scene a3428 with dssr
    n "Let's go somewhere else."
    scene a3429 with dssa
    u "Okay? What's wrong?"
    scene a3430 with dssa
    n "I don't feel this place right now."
    scene a3431 with dssa
    u "Hmm."
    scene a3432 with dssr
    d "Did Mila tell you that Nami and I moved in with Zara for the time being?"
    scene a3433 with dssa
    v "Yes, she did."
    if MilaSleep5x0 is True:
        scene a3434 with dssa
        v "She also told me some other things."
        if NoBella5x0 or BellaNoDating5x0 or BellaOnIce5x0 is True:
            scene b241 with dssr
            b "Eww."
            scene a3434 with dssr
        elif BellaNonExclusive5x0 is True:
            play music "Music/OST/Azula Wave - Lost Souls.ogg"
            $ BellaSuspicious = True 
            $ BellaMilaRivalry5x5 = True
            scene b242 with dssr
            pause
            scene b243 with dssa
            b "...What other things?"
            scene b244 with dssa
            v "Oh, just that they shared a bed. Mila and [name]."
            "Bella stares deep into your eyes."
            scene b245 with dssa
            b "I see."
            d "(...I'm sure Mila told her even more than just that. Please just be quiet Vic.)"
            scene a3434 with dssr
    else:
        scene a3434 with dssa
    v "And that you're soon moving together into a house for students!"
    scene a3432 with dssa
    d "Yeah."
    scene b246 with dssr
    b "It's an upgrade from your homeless shelter."
    scene b247 with dssa
    b "Then it's gonna be more of a junkie doss house... But hey... Let's all look at the bright side."
    scene a3443 with dssr
    d "Fuck off."
    if VicDate or VicDateEntry2 is True:
        $ VicDate = True
        scene a3442 with dssr
        "You notice Vic's cute brown eyes staring at you."
        if BellaNonExclusive5x0 is False:
            $ NoBella5x0 = True
            $ VicColdS2_Ch1 = True
            scene a3435 with dssr
            b "What exactly are you two?"
            scene a3436 with dssa
            v "We're dating... Or well, we plan to date."
            scene a3437 with dssa
            b "Oof... What a snail's pace."
            scene a3438 with dssa
            "Victoria looks at you, then takes a sip from her coffee, silently agreeing with Bella."
            d "We're going to meet up soon."
            scene a3439 with dssa
            v "...You keep saying that."
            scene a3440 with dssa
            d "And this time I mean it."
            scene a3441 with dssa
            "Victoria looks away with a coldness you haven't seen on her before."
        else:
            pass
    stop music fadeout 5
    scene black with Dissolve(2)
    with Pause(.5)
    scene a7823 with dssr
    v "I'll see you two around!"
    scene a7824 with dssr
    d "Later Vic."
    scene a7825 with dssa
    v "Maja will pick us up right after class."
    scene a7824 with dssa
    d "I'll be there."
    if VicColdS2_Ch1 is True:
        scene a3444 with dssr
        pause 
        scene a3445 with dssa
        b "I don't know what you're doing but you should step up your game."
        b "She's about to leave your sorry ass in the dust."
        scene a3446 with dssa
        d "Is that so?"
        scene a3447 with dssa
        b "I'm sure you saw it too."
        b "A person in her state doesn't play games."
        b "Get your shit together or someone else will be clapping her cheeks."
        scene a3448 with dssa
        d "You really like hearing yourself talk, huh?"
        scene a3447 with dssa
        b "Was any of what I just said wrong?"
        scene a3449 with dssa
        d "No. But by insulting you, I avoid having to agree with you."
        scene a3450 with dssa
        b "What's the matter with you? A cute, big tiddy girl like her should even get your juices flowing."
        scene a3451 with dssa
        b "Hell, even I would hit that! And I'm 100 percent hetero!"
        scene a3450 with dssa
        b "At least start cuddling her boobs."
        scene a3452 with dssa
        d "I don't want relationship advice from you."
        scene a3453 with dssa
        b "At least I know how to close a deal."
        scene a3454 with dssr
        pause 
        jump classroom5x5_End
    elif BellaMilaRivalry5x5 is True:
        scene a3455 with dssr
        pause
        d "Do you want to say something?"
        pause
        scene a3456 with dssa
        b "What happened in that bed?"
        scene a3457 with dssa
        d "Sleep happened."
        scene a3458 with dssa
        pause 
        d "We're not exclusive."
        scene a3459 with dssa
        b "Freedom of choice doesn't mean freedom from consequences."
        scene a3460 with dssa
        pause 
        scene a3461 with dssr
        "With a firm, confident step, she walks away..."
        scene a3462 with dssa
        d "...Bella didn't pay."
        stop music fadeout 3
    if NoBella5x0 is True:
        scene black with Dissolve(2)
        with Pause(.5)
        jump classroom5x5_End
        
    scene black with Dissolve(2)
    with Pause(.5)
    jump classroom5x5_End


label classroom5x5_End:
    if BellaMilaRivalry5x5 is True:
        scene a3463 with dssb
        pause
    elif BellaMilaRivalry5x5 is False and BellaNonExclusive5x0 is True:
        scene a3464 with dssb
        pause
    if BellaNonExclusive5x0 is True:
        play music "Music/Scott Buckley/Scott Buckley - Echoes.ogg" fadein 5
        play sound "Music/Sfx/Punch.ogg"
        scene a3465 with vpunch #sfx
        pause 
        scene a3466 with dssr
        b "Ngh... What are you doing?"
        "You press her against the locker with a lot of force..."
        scene a3467 with dssa
        "...then gently release it."
        if BellaMilaRivalry5x5 is True:
            scene a3468 with dssr
            d "This whole 'Non exclusive' thing was your idea."
            scene a3469 with dssa
            b "And it's a good idea too."
            b "However, I would've thought you'd take my feelings into consideration."
            scene a3470 with dssa
            b "That you'd be smarter than the rest. Smarter than those who would say 'B-but we aren't exclusive' while doing an enemy of mine." 
            b "Correct. You and I aren't exclusive. But do you see me share a bed with your enemy?"
            b "I'd never do that to you, because I can read between the lines."
            scene a3471 with dssr
            pause 
            scene a3472 with dssa
            b "My idea of this here is that we don't have to explain to each other where we go."
            b "If I want to stay out late, I don't have to explain myself to you... And vice versa..."
            scene a3473 with dssa
            b "But I thought it was clear that we'd still- be mindful of each other."
            scene a3474 with dssa
            b "I'm asking you this once... Don't share a bed with her again."
            scene a3475 with dssa
            b "And the rest, I'll leave up to you... If you can't read between the lines, it will never work out with us."
            scene a3476 with dssa
            d "(This must've really upset her. It's the first time I see her speak like this.)"
            d "(I should be more careful with Mila... Maybe I should break it off? Or maybe I should tell Mila not to tell Vic.)"
            pause 
            scene a3477 with dssa
            "Bella starts breathing faster..."
            scene a3478 with dssa
            "Then a slight moan escapes her lips..."
            scene a3479 with dssa
            pause 
            scene a7988 with dssr
            "Your index finger slowly slides inside her." 
            scene a7989 with dssr
            "She pushes her back out."
            scene a7990 with dssr
            pause 
            scene a7991 with vpunch
            na "Stop!"
            scene a7992 with dssa
            b "Nad- go away!"
            scene a7993 with dssa
            na "You're influencing me!"
            scene a7994 with dssa
            b "Then look away!"
            scene a7995 with dssa
            na "I can't!"
            scene a7996 with vpunch
            "Nadia tries to separate you two."
            scene a8001 with vpunch
            "You and Bella fixate Nadia against the locker..."
            "...and continue."
            $ Nadia_Hörnchen = True
            $ Bellchen_Fingered_1x0 = True
        else:
            scene a3469 with dssa
            b "Is this your way of instigating something?"
            scene a3468 with dssa
            d "Maybe."
            scene a3470 with dssa
            b "I like it."
            scene a3471 with dssa
            pause
            scene a3477 with dssa
            pause 
            scene a3478 with dssa
            b "*Breathy* I wonder... What does it do for you?"
            scene a3477 with dssa
            "Bella starts breathing faster..."
            scene a3478 with dssa
            "Then a slight moan escapes her lips..."
            scene a3479 with dssa
            pause 
            scene a7988 with dssr
            "Your index finger slowly slides inside her." 
            scene a7989 with dssr
            "She pushes her back out."
            scene a7990 with dssr
            pause 
            scene a7991 with vpunch
            na "Stop!"
            scene a7992 with dssa
            b "Nad- go away!"
            scene a7993 with dssa
            na "You're influencing me!"
            scene a7994 with dssa
            b "Then look away!"
            scene a7995 with dssa
            na "I can't!"
            scene a7996 with vpunch
            "Nadia tries to separate you two."
            scene a8001 with vpunch
            "You and Bella fixate Nadia against the locker..."
            "...and continue."
            $ Nadia_Hörnchen = True
            $ Bellchen_Fingered_1x0 = True
    else:
        pass
    stop music fadeout 3       
    jump ClassroomContinueEndy

label ClassroomContinueEndy:
    $ play_playlist(playlist_College)
    scene black with Dissolve(2)
    with Pause(.5)
    scene a3480 with dssb
    pause
    scene a3481 with dssr 
    pause 
    scene a3482 with dssr
    pause 
    scene a3497 with dssr
    pause 
    scene a3498 with dssa
    pause 
    scene a3499 with dssr
    sas "What are you doing?"
    scene a3500 with dssa
    u "I'm sacrificing myself."
    scene a3483 with dssr
    pause 
    scene a3484 with dssr
    pause 
    scene a3485 with dssr
    pause 
    scene a3486 with dssa
    pause 
    scene a3487 with dssa
    mi "Hey, what's wrong?"
    scene a3488 with dssa
    pause 
    scene a3489 with dssa
    v "Nothing! I was just checking out the birds!"
    v "There was a really cute one with amazing feathers!"
    scene a3491 with dssr
    mi "Viiiic..."
    scene a3490 with dssa
    v "Really! I'm fine!"
    scene a3492 with dssr
    mi "I'm not letting you off that easy."
    scene a3495 with dssr
    v "Fuck you."
    scene a3493 with dssr
    mi "*Chuckles* You think a half-hearted 'Fuck you' is going to push me away?"
    scene a3494 with dssa
    mi "Keep dreaming, bird watcher."
    mi "I won't let you wither away."
    scene a3496 with dssr
    pause 
    scene a3501 with dssr
    u "I gotta go. I'll see you later, honey."
    scene a3502 with dssa
    pause 
    scene a3503 with dssr
    pause 
    scene a3504 with dssr
    u "*Giggles* Hey! Not here! He could've seen it!"
    scene a3505 with dssr
    pause 
    scene a3506 with dssr
    b "Could you wear an even shorter skirt, bitch?"
    scene a3508 with dssr
    ay "It's not short."
    scene a3507 with dssa
    b "Have you seen it from the back?"
    scene a3508 with dssa
    ay "Have you seen yourself from the back?"
    scene a3509 with dssa
    b "Yes, a pretty amazing sight."
    scene a3510 with dssr
    pause
    scene a3511 with dssa
    b "Hiii."
    scene a3512 with dssa
    b "I'm Michelle from social services. How may I help you today?"
    scene a3513 with dssa
    "You just sigh."
    scene a3514 with dssr
    b "Not one for many words, huh? But no worries, we don't judge. Let me check what I can offer you..."
    scene a3515 with dssa 
    pause 
    scene a3516 with dssa
    b "Ah! You're in luck! We still offer free, state-sponsored workshops for people who've never been touched by a woman." 
    scene a3517 with dssa
    d "Great. I heard your Mom gives them."
    scene a3518 with dssa
    b "Wow. Going on my Mom."
    scene a3519 with dssa
    d "In more than one way."
    play sound "Music/Sfx/Slap.ogg"
    scene a3520 with vpunch
    pause 
    play sound "Music/Sfx/Slap.ogg"
    scene a3521 with vpunch
    pause
    scene a3522 with dssr 
    b "Who are the unlucky souls you're moving in with again?"
    scene a3523 with dssa
    if BellaNonExclusive5x0 is True:
        d "Nami, Mila and probably Robin."
        scene a3524 with dssa
        b "So Mila..."
        scene a3525 with dssa
        d "Mhm."
        scene a3526 with dssa
        if BellaMilaRivalry5x5 is False:
            b "I think it was a good move not to go serious."
            scene a3527 with dssa
            d "I agree."
            pause #sus hits you sfx
        else:
            b "Us breaking up might come sooner than I expected."
            scene a3527 with dssa
            d "Breaking up? We're not in a relationship!"
            if Bella_Fiancee is True:
                scene a3528 with dssa
                b "I'm your fiancée."
                scene a3529 with dssr
                d "I don't see a ring on your bony finger."
                scene a3530 with dssa
                b "It's being resized."
                b "You always thought you could only bag a fatty, so naturally, you got a sausage-sized ring."
                scene a3531 with dssr
                b "You couldn't imagine a skinny girl taking notice of you, let alone say..."
                scene a3532 with dssa
                d "Your cope is getting out of control."
                scene a3533 with dssa
                pause 
                scene a3534 with dssr
                b "I wanna put an onion ring on your dick."
                scene a3535 with dssa
                d "No."
                scene a3534 with dssa
                b "I wanna see if it holds up!"
                scene a3536 with dssa
                b "We'll do that!" 
                scene a3537 with dssa
                d "Back to me cheating on you with Mila."
                scene a3538 with vpunch
                "She steers her sharp nails into your hand."
        scene a3539 with dssr
        d "Are you jealous because I'm moving in with three girls?"
        scene a3540 with dssa
        b "Oh please..."
        b "One is Nami... If you wanted her, you would've already done it." 
        scene a3541 with dssa
        b "Robin only does gangbangs."
        scene a3542 with dssa
        d "Really?"
        scene a3543 with dssa
        b "No."
        b "And Mila is just Mila."
        if BibiBellchen4x5 is True:
            scene a3544 with dssa
            d "I think if you weren't such a little bitch, you could've been great friends."
            scene a3547 with dssr
            d "She tried, but you can't get past your little, bruised ego."
            scene a3546 with dssa
            b "I don't forgive."
            scene a3547 with dssa
            d "She stood in for you, didn't she?"
            scene a3548 with vpunch
            b "Will you shut the fuck up? Just because she stood up for me once, doesn't make up for the countless times she looked away!"
            scene a3549 with dssa
            d "Did she ever do anything afterwards?"
            scene a3545 with dssr
            "She walks away."
        if Bellchen_Fingered_1x0 is True:
            $ Nadia_Hörnchen = True
            scene a3550 with dssr
            na "It's baaaad."
            scene a3551 with dssa
            ay "What? How bad?"
            scene a3550 with dssa
            na "Soooooo bad." 
            scene a3552 with dssr
            ay "Why?!"
            scene a3553 with dssa
            na "I've seen Bella and [name]!"
            na "He was fingering her... and I tried to get them to stop so I wouldn't be influenced!"
            scene a3554 with dssr
            na "B-but they kept going and started kissing while I was stuck between her and the wall!"
            scene a3555 with dssa
            na "And now I need it BAD!"
            scene a3556 with dssa
            ay "Why didn't you just walk away?"
            scene a3557 with dssa
            na "I- I- I- I DON'T KNOW!?"
            scene a3558 with dssa
            ay "Oh no..."
            ay "You stay with me for the rest of the day."
            scene a3559 with dssa
            na "I need to meditate..."
            scene a3560 with dssr
            ay "What are you even wearing?!"
            pause 
            scene a3561 with vpunch
            ay "This ends now!"
            ay "Be at Bella's today after college! I call an INTERVENTION!"
            scene a3562 with dssa
            na "Not another alien, sasquatch, or skinwalker intervention..." 
            scene a3563 with dssa
            ay "We've given up on that..."
            scene a3561 with dssa
            ay "You will never wear cleavage this big again until you have a boyfriend that can keep up with you!"
            scene a3564 with vpunch 
            ay "You!" 
            scene a3565 with dssa
            ay "Don't have sex on or near Nadia again!"
            scene a3566 with dssa
            d "She looks stoned."
            scene a3567 with dssa
            ay "Otherwise you'll have to do her too! And trust me! You wouldn't survive that!"
            scene a3568 with dssr
            pause 
            scene a3569 with dssa
            na "I'm dizzy..."
            scene a3570 with dssr
            pause 
            scene a3571 with dssr
            u "Yes, sure. I'll back you up if they say you hit him on purpose."
            b "Thanks Irvi."
            scene a3572 with dssr
            d "Would you look at that... Your friends are as retarded as you."
            scene a3573 with dssa
            b "Which ones? I have many friends."
            scene a3572 with dssa
            d "No you don't."
            scene a3574 with dssr
            d "Ayua and Nadia."
            scene a3575 with dssa
            b "Oh... Yeah... They're awesome."
            scene a3576 with dssa
            d "What's up with Nadia? She's been acting weird since our earlier encounter."
            scene a3577 with dssa
            b "Mhmm... She's horny."
            scene a3576 with dssa
            d "She looks like she's in pain... or has smoked something."
            scene a3578 with dssa
            b "...She's built a little different."
            if Info_Nadia_Dating_CH1 is False:
                scene a3579 with dssa
                d "In what way?"
                scene a3578 with dssa
                b "Doesn't matter."  
            else:
                scene a3579 with dssa
                d "I know. Zara told me."
            scene a3580 with dssa 
            b "Well... Didn't take you long to be back there."
            scene a3592 with dssr
            pause 
            scene a3581 with dssr 
            b "I'm not surprised you want to get back in." 
            scene a3582 with dssa 
            d "You make it very hard for me to say something nice."
            scene a3583 with dssa
            b "It doesn't matter which words escape your lips... Your eyes tell me everything I need to know."
            scene a3584 with dssa 
            d "Yours tell me that I'm on top."
            scene a3585 with dssa 
            b "*Whispers* On top, bottom, I don't care. As long as you're back inside..."
            scene a3586 with dssr
            pause 
            scene a3587 with dssr #music out
            pause 
            scene a3588 with dssa #wieder an
            pause
        scene a3589 with dssr  
        pause 
        scene a3590 with dssa
        d "What's the deal with you and Robin?"
        scene a3591 with dssa
        b "We have some history."
        scene a3590 with dssa
        d "Bad history?"
        scene a3593 with dssr
        "Bella exhales."
        scene a3594 with dssa
        b "Why do you wanna know?"
        scene a3595 with dssr
        d "I'm moving in with her. I wanna know who gets near my food."
        scene a3596 with dssa
        b "We got into a little fight in Middle School, nothing physical..."
        b "Her Mom went through a divorce and it affected her mood so she lashed out. But not with malicious intent... She was just venting."
        scene a3597 with dssa
        b "I was on guard all the time and misread it as real hostility."
        b "I said some really mean things and hadn't seen her again until I switched schools in high school."
        scene a3598 with dssa
        d "And now you fear that she has it out for you?"
        scene a3599 with dssa
        b "No, she's the worst!"
        b "She wasn't even mad at me! Didn't yell at me afterward- nothing!"
        scene a3597 with dssa
        b "I deserved punishment... My head still sometimes thinks she's just waiting for the right moment."
        scene a3598 with dssa
        d "You're so consumed by revenge that you can't fathom someone else not being like that."
        scene a3599 with dssa
        b "Yap."
        scene a3600 with dssa
        d "I can punish you later."
        scene a3601 with dssa
        b "Now you have my attention!"
        scene a3602 with dssa
        d "By not doing anything."
        scene a3603 with dssr
        b "I hate you."
    else:
        d "Mila, Nami and Robin."
        scene a3524 with dssa
        b "Did you tell them you're gay?" 
        scene a3525 with dssa
        d "No."
        scene a3524 with dssa
        b "Mhm. They'll soon introduce you under your new alias, Gay Ken. Their gay best friend."
        scene a3525 with dssa
        d "I'll be so glad when we are no longer project partners."
        scene a3526 with dssa
        b "I'll miss it."
        scene a3527 with dssa
        d "Will you?"
        scene a3526 with dssa
        b "It's fun to tease you."
        scene a3524 with dssa
        b "But I get it... I'm too much of a woman for you... Gay Ken needs someone like Jeff."
        scene a3525 with dssa
        d "I'm losing brain cells talking to you." 
        scene a3524 with dssa
        b "And I feel my pussy weld itself shut talking to you."
        scene a3525 with dssa
        d "That's a disgusting thought."
        scene a3541 with dssr
        b "I have a very pretty pussy. She looks pretty even when welded shut."
        "You say nothing." 
        scene a3536 with dssa
        b "What? You don't like me talking about my pussy?"
        scene a3535 with dssa
        d "No."
        scene a3534 with dssa
        b "She doesn't like you either."
        scene a3535 with dssa
        d "Sure."
        scene a3541 with dssr
        b "Cope."
        scene a3542 with dssa
        d "You know... I might not be the most social... But I've always had some chicks hit on me."
        d "Some of them were kinda like you... I know a little bit of effort would be enough to get you to drop your clothes."
        d "It's just that I want neither you nor your pussy."
        scene a3543 with dssa
        b "Very convincing."
        menu:
            "Give her a peck on her cheek.":
                $ nBellchenPeck1 = True
                scene a3543a with dssa
                b "Eww!" 
            "Don't.":
                pass  
        scene black with Dissolve(1.5)
        with Pause(.5)
    scene a3604 with dssr
    pause 
    scene a3605 with vpunch
    u "Hey!"
    scene a3606 with dssa
    d "Sorry. Didn't see you there."
    scene a3607 with dssa
    u "Buy me a drink before you sit on me."
    scene a3608 with dssa
    menu:
        "Maybe tomorrow.":
            $ JustineDrink = True 
            scene a3607 with dssa
            u "Mhm, maybe." 
        "Leave.":
            pass 
    scene a3609 with dssr
    pause 
    scene a3610 with dssr
    d "Cheeto."
    scene a3611 with dssa
    n "Are you preparing for the tryouts?"
    scene a3612 with dssa
    d "Not really."
    scene a3613 with dssa
    n "You gotta prepare!"
    scene a3614 with dssa
    n "Maxine here has a big brother who plays tennis, and he says the tryouts are brutal."
    scene a3615 with dssa
    d "I'll manage."
    scene a3616 with dssa
    maxi "You compete with fifty to a hundred good players. You shouldn't take it this lightly."
    scene a3617a with dssr
    d "I think I'll be fine."
    scene a3617 with dssr
    d "Sure, my cardio could be better."
    scene a3618 with dssa
    maxi "Start running track. It'll get you up there."
    scene a3619 with dssa
    n "I might do it too."
    scene a3620 with dssa
    maxi "I'll take you with me, Nami."
    maxi "I've been doing track for almost ten years."
    scene a3621 with dssr
    n "[name], come with us."
    n "I bet Zara would join us too."
    scene a3622 with dssa
    maxi "Zara Benz?"
    scene a3623 with dssa
    n "Yeah."
    scene a3622 with dssa
    maxi "My brother said she plays tennis really well." 
    maxi "Would she play against him?"
    scene a3623 with dssa
    d "She's always up for a challenge."
    scene a3624 with dssa
    n "You and your brother should come by our place."
    scene a3625 with dssa
    d "'Our'?"
    d "We're just guests there."
    scene a3623 with dssa
    n "We're staying at Zara's for the time being."
    scene a3625 with dssa
    maxi "Cool!"
    maxi "I'll talk to him and if Zara's up for it, they can have a match at the local tennis field." 
    scene a3626 with dssa
    n "She has a private field in her garden."
    scene a3627 with dssa
    maxi "Oh damn."
    scene a3628 with dssa
    n "Yeaaah, I wish I was rich too."
    scene a3629 with dssr
    d "Is your brother a good player?"
    scene a3630 with dssa
    maxi "Yeah, he plays professionally for ZPR, soooo... He's gotta have something going for him."
    scene a3631 with dssa
    d "Then Zara will definitely take the challenge."
    scene a3632 with dssa
    maxi "You got my number, Nami."
    scene a3633 with dssa
    n "Yo, I'll let you know."
    scene a3634 with dssa
    pause 
    scene a3635 with dssa
    n "What a bitch."
    scene a3636 with dssa
    pause 
    scene a3637 with dssa
    n "I'm kidding. Max's cool."
    scene a3638 with dssr
    d "You're a busy bee."
    scene a3639 with dssa
    n "I'm a busy roll."
    scene a3640 with dssa
    n "For the last time! If you use metaphors, replace them with 'roll'!"
    scene a3641 with dssa
    d "Are you trying to make as many friends as possible?"
    scene a3642 with dssa
    n "I'm not even trying, I'm just THAT likeable."
    n "I'm the friendzone queen."
    scene a3643 with dssa
    d "Checks out."
    scene a3645 with dssa
    n "Really? Does it?"
    scene a3646 with dssa
    n "You think it's me who gets friendzoned?!"
    n "You clearly have no idea who you're talking to!"
    n "Someone gets horny and gets shut down and you think it's me?"
    scene a3647 with dssa
    n "NO! I AM THE ONE WHO FRIENDZONES!"
    scene a3648 with dssr
    if NamiDate is True:
        d "I wish you had friendzoned me."
        scene a3649 with dssa
        n "I can still do that and then..."
        scene a3650 with dssr
        n "Then you'll cry after these cheeks."
        scene a3651 with dssr
        n "*High-pitched voice* Ohhh nooo! Why did I fumble the hot Cheeto who likes to sit on my face?!"
        scene a3652 with dssr
        show screen Extra_Lewd_CH1_Nami_1
        pause 
        hide screen Extra_Lewd_CH1_Nami_1
        scene a3654 with dssr
        d "See you later."
        scene a3655 with dssa
        n "Heeey, hey, hey!"
        scene a3657 with dssr
        n "Let me sit on your face."
        scene a3658 with dssa
        d "You're really into that, huh?"
        scene a3657 with dssa
        n "The thought excites me... I have no idea if it's actually as good."
        scene a3658 with dssa
        d "Maybe later today."
        scene a3659 with dssa
        "She lets out a happy yoooo!"
    else:
        d "Sure you are."
        scene a3649 with dssa
        n "I'll kill you."
        pause 
    scene a3660 with dssa
    n "I'll talk to you later, I gotta go say hi to a few people here."
    scene a3661 with dssr
    nia "It's so overwhelming."
    scene a3663 with dssr
    nia "There are cars on the left... There are cars on the right, behind and in front of me!"
    scene a3662 with dssr
    b "You'll get used to it really fast. Before you know it, you're driving with one hand in your pants and the other on the phone."
    scene a3664 with dssr
    "Nia chuckles."
    scene a3665 with dssr
    d "Where is the professor?"
    scene a3666 with dssa
    b "How should I know?"
    if Open_Relationship is True:
        if BellaNonExclusive5x0 is False:
            scene a3720 with dssr
            d "Do you know someone with an open relationship?"
            scene a3722 with dssa
            "She sighs."
            scene a3724 with dssr
            b "For the last time..."
            b "I'm not going to let you watch!"
            scene a3726 with dssa
            b "I know being the third wheel is the closest you'll ever get to having sex, but just- okay?"
            b "Just pay someone... like a lot."
            scene a3725 with dssa
            d "Why do I even talk to you? I should've learned my lesson by now."
            scene a3724 with dssa
            b "But to answer your question..."
            b "Some of my friends have or are in one and it never works out."
            b "Usually it ends up with the girl getting all the action and the guy... well, struggling to get laid."
            b "Unless you're like that girl Meila I once knew. She did it, and her boyfriend left her for the first girl."
            b "Why? Are you looking for a couple to adopt you?"
            scene a3725 with dssa
            d "No. I'm just curious."
            scene a3726 with dssa
            b "It's all games and fun until, at the end of college, you compare your list."
            scene a3724 with dssa
            b "Seriously, stick to one partner."
        else:
            menu:
                "Ask what she thinks of open relationships.":
                    $ Bella_OR_Mentioned = True 
                    scene a3667 with dssr
                    pause 
                    scene a3668 with dssr
                    b "...Now you can't keep your hands off her..."
                    scene a3669 with dssr
                    pause 
                    scene a3670 with dssr
                    b "*Whispers* Yeaah... You'd really like to go inside now..."
                    scene a3671 with dssa
                    b "*Whispers* Gently move your fingers between my wet labia... spread them... rub them..."
                    b "*Breathy* Then you gently slip inside me here, in front of everyone..."
                    scene a3672 with dssa
                    d "You're talking yourself into a horny-frenzy."
                    scene a3673 with dssa
                    b "*Moans* Mhmmmm..."
                    scene a3674 with dssr
                    d "What do you think of open relationships?"
                    scene a3675 with dssa
                    b "Hmm, I have some friends who had them and it never ended well... for the guys."
                    b "Usually it ends up with the girl getting all the action and the guy... well, struggling to get laid."
                    b "Unless you're like that girl Meila I knew. She struggled and her boyfriend left her for the first girl."
                    scene a3676 with dssa
                    pause
                    scene a3677 with dssa 
                    b "Why?"
                    scene a3678 with dssa 
                    d "I had a conversation with Noji about it... Apparently she has done them in the past."
                    d "And it reminded me of our fake non-exclusiveness."
                    scene a3677 with dssa 
                    b "It's not... fake."
                    scene a3679 with dssa  
                    b "Maybe... a tiny bit."
                    scene a3677 with dssa  
                    b "I don't want a relationship... College just started, man." 
                    scene a3678 with dssa 
                    d "I must've missed where I said we should have one."
                    scene a3680 with dssa 
                    b "Why? Would you be interested in an open one?"
                    menu:
                        "Yes.":
                            $ Bella_OR_STG1 = True 
                            $ Open_Relationship_STG1 = True 
                            scene a3681 with dssa 
                            d "It sounds a lot less complicated than this weird in-the-air scenario we have going right now."
                            scene a3682 with vpunch 
                            b "Bitch! You just want to cuddle others!"
                            scene a3683 with dssa 
                            d "I'm already allowed to cuddle others."
                            scene a3684 with dssa 
                            b "Not anymore!"
                            scene a3685 with dssa 
                            d "In other words; We have a serious relationship?"
                            scene a3686 with dssa 
                            b "No!"
                            scene a3687 with dssa 
                            d "Dumbass."
                            scene a3688 with dssa 
                            pause 
                            scene a3689 with dssa 
                            b "I own you."
                            scene a3690 with dssa 
                            d "I own you!"
                            scene a3691 with dssa 
                            d "All it takes is a little bit of touching, some whispering and you're back on the leash."
                            scene a3692 with dssa 
                            b "Keep talking like this and you're soon to be on my leash!"
                            b "I'll pin your head between my legs and keep the leash taut until I say we're done."
                            scene a3693 with dssa 
                            pause 
                            scene a3694 with dssa 
                            pause 
                            scene a3695 with dssa
                            pause  
                            scene a3719 with dssr 
                            pause
                        "No.":
                            scene a3681 with dssa 
                            d "We haven't even really done anything."
                            scene a3689 with dssa 
                            b "Exactly."
                            b "When we get to the fun part, you won't have energy for anyone else."
                            b "Besides... I own you."
                            scene a3690 with dssa 
                            d "I own you!"
                            scene a3691 with dssa 
                            d "All it takes is a little bit of touching, a whisper, and you're back on the leash."
                            scene a3692 with dssa 
                            b "Keep talking like this and you're soon to be on my leash!"
                            b "I'll pin your head between my legs and keep the leash taut until I say we're done."
                            scene a3693 with dssa 
                            pause 
                            scene a3694 with dssa 
                            pause 
                            scene a3695 with dssa
                            pause  
                            scene a3719 with dssr 
                            pause
                    scene a3696 with dssr  
                    d "Have you done anything with anyone since we've- you know?"
                    scene a3697 with dssa
                    b "No."
                    scene a3698 with dssa
                    b "How about you?"
                    if len(Dating_List) >1:
                        scene a3700 with dssa
                        d "...Perhaps a kiss."
                        scene a3701 with dssa
                        b "Yeah." 
                        b "I'm the good, dedicated part in this relatio-..."
                        scene a3702 with vpunch
                        pause 
                        scene a3703 with dssa
                        pause 
                        scene a3704 with dssa
                        d "Say that again."
                        scene BellchenKopfSchuettel
                        pause 
                    else:
                        scene a3699 with dssa
                        d "I haven't."
                        scene a3706 with dssa 
                        b "Good boy."
                        scene a3707 with dssa 
                        pause
                        scene a3708 with dssa 
                        b "You're such a good little boy."
                        scene a3709 with dssa 
                        d "I'll drown you in your own bathtub."
                        scene a3708 with dssa 
                        b "Does it trigger you when Mami calls you her good little boy?"
                        scene a3709 with dssa 
                        d "I want to stab you with a pencil."
                        scene a3710 with dssa 
                        b "Or you could spank me?"
                        scene a3711 with dssa 
                        d "No, you'd like that."
                        scene a3712 with dssa 
                        b "I can pretend not to like it."
                        scene a3713 with dssa 
                        pause 
                        scene a3714 with vpunch 
                        ay "Hey! No spanking in this classroom!"
                        scene a3715 with dssa 
                        b "*Sensitive Whisper* The good little boy won't even give Mami a spanky."
                        scene a3716 with dssr 
                        b "Tzz, tzz, tzz."
                        scene a3717 with vpunch 
                        "She licks over the entire left side of your face."
                        scene a3718 with dssa 
                        pause 
                "Don't ask her about it.":
                    scene a3667 with dssr
                    pause 
                    scene a3668 with dssr
                    b "...Now you can't keep your hands off her..."
                    scene a3669 with dssr
                    pause 
                    b "*Whispers* Yeaah... You'd really like to go inside now..."
                    b "*Whispers* Gently move your fingers between my wet labia..."
                    b "*Breathy* Then you gently slip inside me here, in front of everyone..."
                    d "You're talking yourself into a horny-frenzy."
                    b "*Moans* Mhmmmm..."
                    pause 
    else:
        pass
    if Mark_On_Kate_Teasing is True:
        scene a3721 with dssr
        d "By the way..."
        d "This Kate."
        scene a3722 with dssa
        b "Mh."
        scene a3721 with dssa
        d "She flirts aggressively with me because of you."
        scene a3723 with dssa
        b "So?"
        scene a3725 with dssa
        d "Why's she doing that?"
        scene a3724 with dssa
        b "We've never liked each other and over the years I whooped her ass a few times. I guess she wants to hurt me."
        scene a3726 with dssa
        b "I was better in school- well- everything really!"
        scene a3727 with dssa
        b "I'm prettier, smarter, braver... nicer... taller... skinnier... longer hair... better ass... I'm not on Venus..." 
        scene a3728 with dssa
        b "I have natural big boobs, I think hers are fake... I drive better, I cook better, I pet animals better-"
        scene a3730 with dssa
        d "Okay... I got it." 
        scene a3731 with dssa
        b "I wasn't done."
        scene a3732 with dssa
        b "I slurp spaghetti better, I dip fries into stuff better, I smell better, I have a cooler blood type, I dress better, I fish better, my hair is angelic-"
        scene a3733 with dssa
        d "Bella!"
        scene a3734 with dssa
        b "Well- the bitch wants revenge."
        scene a3735 with dssa
        b "Oh! I do revenge better too!"
        scene a3736 with dssa
        b "If she keeps coming on to you, don't let her down easy."
        scene a3737 with dssa
        d "I've been leading her on in case you wanna set something up."
        scene a3738 with dssa
        b "Hmm... We shall see... Don't let her get too close tho."
        scene a3739 with dssa
        d "(That reminds me... Nami will eventually avenge herself too.)"
        d "(I gotta keep the Cheeto in check.)"
        scene a3740 with dssa
        d "I'll let you know what happens."
        d "(I'll talk to Kate... Maybe I can somehow turn this into a status quo)"
    scene a3741 with dssr
    ay "Of course I'll go. I'll wear a very short skirt, stare at people like I'm a German, and order a Sex on the Beach. Perfectly in character."
    scene a3742 with dssr
    pause 
    scene a3743 with dssa
    pause 
    d "Mh?"
    scene a3744 with dssa
    sas "Would you like a blowjob?" 
    scene a3745 with dssa
    ay "THAT'S NOT HOW I TALK!"
    scene a3745a with dssr
    sas "You lasted thirty seconds. You broke character. I win."
    scene a3745b with dssa
    ay "Y-you lost because you acted out of character! You did it first!"
    scene a3745a with dssa
    sas "*calm* I didn't." 
    scene a3745d with dssa
    d "Do I even need to ask?"
    scene a3745c with dssa
    ay "We came up with a bet where we would switch personalities for 24 hours!"
    ay "Bella!"
    scene a3747 with dssr
    b "Yes?"
    scene a3748 with dssa
    ay "Come over here."
    scene a3749 with dssa
    b "Nope. I won't ever take part in fueling your gambling addiction."
    scene a3750 with dssr
    ay "Robin!"
    scene a3751 with dssr
    rob "...Ya?"
    scene a3752 with dssa
    ay "You know me! Would I go around and ask guys if I could give them a blowjob?"
    scene a3753 with dssa
    rob "Umm, umm, umm..."
    scene a3754 with dssa
    pause 
    play sound "Music/Sfx/Punch.ogg"
    scene a3755 with vpunch
    ay "Don't look at her! "
    scene a3756 with dssa
    ay "*Growls* Look at me!"
    scene a3757 with dssa
    rob "I dooooon't knooow!"
    scene a3758 with dssa
    rob "I've heard stories about your bets! I don't know where you people have your limits!"
    scene a3759 with dssa
    ay "I bet she only told you about the few she won."
    scene a3760 with dssr
    sas "That would be too many. I'm in the lead."
    scene a3761 with dssa
    ay "No, you're not!"
    ay "It's 73 to 72."
    scene a3762 with dssa
    sas "You lost the bet we had in Lisbon."
    scene a3763 with vpunch
    ay "I didn't! I WON!"
    scene a3764 with dssa
    sas "The goat died."
    scene a3765 with dssa
    ay "You never specified that she had to get to Monaco alive!"
    ay "Details matter! YOUR WORDS!"
    scene a3766 with dssr
    "You and Robin share a look."
    scene a3768 with dssa
    ay "Poor Missy..."
    scene a3769 with vpunch
    ay "Oh! What about you!?"
    ay "When I bet you that you wouldn't dare to jump off the yacht's roof with a blindfold and land safely!"
    scene a3770 with dssa
    sas "I did exactly that."
    scene a3769 with dssa
    ay "You dislocated your shoulder and bruised a rib!"
    scene a3771 with dssa
    sas "Safe-ish."
    scene a3772 with dssa
    ay "Hospital visits are an automatic loss!"
    scene a3773 with dssa
    sas "We created that rule as a result of this bet. You gave me the win."
    scene a3774 with dssa
    "Ayua growls." 
    scene a3767 with dssr
    rob "You two are the definition of bored, rich chicks. Oh my God."
    scene a3774 with dssa
    with Pause(.4)       
    $ Info_Ay_Sas_Bet_Yacht = True 
    scene a3775 with dssa
    d "Just why?"
    scene a3776 with dssr 
    pause 
    scene a3777 with dssa
    ay "We grew up on yachts."
    scene a3778 with dssa
    ay "You have no idea how boring it can be to spend every vacation for weeks on end on a damn yacht!"
    scene a3779 with dssa
    d "Yeah... my lobster is too buttery and my steak too juicy..."
    scene a3780 with dssa
    ay "Too much of anything is bad."
    ay "We had to entertain ourselves somehow..." 
    scene a7798 with slideleft
    pause 
    scene a7797 with dssa
    ay "I'm bored."
    scene a7798 with dssa
    pause 
    scene a7799 with dssa
    ay "I'm booooored."
    scene a7802 with dssr
    sas "Please be quiet."
    scene a7803 with dssa
    ay "When are we supposed to go on land again?"
    scene a7802 with dssa
    sas "In two days."
    scene a7799 with dssa
    ay "Kill me..."
    scene a7804 with dssr
    pause 
    scene a7805 with dssa 
    pause
    scene a7806 with dssa 
    sas "Do you think I could jump into the ocean and barely make a splash?"
    ay "No."
    scene a7808 with dssr
    pause 
    scene a7807 with dssa 
    sas "Do you want to bet?"
    scene a7800 with dssr
    ay "I don't bet. Betting is for bibis."
    scene a7809 with dssr
    sas "I'll bet you one of my crunchy inside-out sushi rolls."
    scene a7810 with dssa
    sas "If I win, I'll get yours, if you win, you'll get mine."
    scene a7801 with dssa
    ay "Fine." 
    scene a7811 with dssr
    pause 
    scene a7812 with dssr
    play sound "Music/Sfx/Water_Splash.ogg"
    pause 
    scene a7813 with vpunch
    ay "That was a giant splash!"
    scene a7814 with dssa 
    pause
    scene a7815 with dssa
    pause 
    scene a7816 with vpunch
    ay "MAMA! Sasha is dead!"
    scene a3781 with dssr
    ay "Sasha's responsible for my very mild gambling addiction."
    scene a3782 with dssa
    ay "*Eerie voice* Which is why we need to get rid of her..."
    scene a3783 with dssa 
    ay "We were bored and started betting each other."
    scene a3785 with dssa
    ay "Eventually, we stopped betting things, and instead bet punishments."
    scene a3786 with dssa
    sas "And I didn't fail to notice that your hair isn't white-"
    scene a3787 with dssa
    ay "Actually..."
    scene a3788 with dssr 
    pause 
    scene a3789 with dssa
    ay "You never specified which hair."
    scene a3790 with dssa
    sas "As a matter of fact, I did."
    scene a3791 with dssr
    "Sasha walks back to her table, grabs her purse and takes out her phone."
    scene a3792 with dssr 
    pause
    scene a3793 with dssa 
    pause
    scene a3794 with dssa 
    d "Do you have Ayua as a wallpaper?"
    scene a3795 with dssr
    ay "I have control over her wallpapers for about seven more months."
    scene a3796 with dssa
    "Ayua reads the chat she had with Sasha last month."
    scene a3797 with dssa
    ay "...Great."
    ay "All that itching for nothing..."
    scene a3798 with dssa 
    sas "Anyways... I knew you would try to squirm your way out."
    scene a3799 with dssa 
    sas "You'll get two punishments... One for breaking character, the other for still not having dyed your hair white."
    sas "This, of course, doesn't release you from your obligation to dye your hair white."
    sas "Should you, however, fail to meet the punishment again..."
    scene a3800 with dssa 
    sas "I don't think I'll need to remind you of what happens then." 
    scene a3801 with dssr
    rob "W-what happens then?"
    scene a3802 with dssa
    ay "You're too young for this, Robin."
    scene a3803 with dssa
    rob "Sasha! Tell her about all the grown-up stuff I've done so far!"
    scene a3804 with dssa
    sas "Ayua. The first punishment, I very conveniently have with me in my purse."
    scene a3805 with dssa
    ay "Please no more piercings..."
    scene a3806 with dssa 
    sas "You'll wear this shirt until the end of the week."
    scene a3808 with dssa 
    sas "[name]? Would you be so kind to shield Ayua from curious eyes?"
    scene a3809 with dssa 
    ay "I have to wear it now?"
    scene a3807 with dssa 
    sas "Obviously."
    scene a3810 with dssr 
    pause 
    ay "Is it at least my size?"
    scene a3811 with dssa
    sas "It's for a small A cup."
    scene a3812 with dssa 
    "Ayua mumbles something."
    scene a3814 with dssa  
    ay "*Sigh* It could be worse, I guess."
    scene a3815 with dssr  
    pause 
    scene a3816 with dssr 
    pause 
    scene a3817 with dssa   
    ay "Besides it being tight around my chest, this is a free one."
    scene a3818 with dssa 
    sas "If you say so."
    scene a3819 with dssr
    pause
    scene a3820 with dssr
    ay "And the other?"
    scene a3818 with dssa 
    sas "I wrote down a few ideas."
    scene a3821 with dssr 
    sas "Robin? Help me decide."
    scene a3823 with dssr
    pause 
    scene a3822 with dssa 
    pause 
    scene a3824 with dssa 
    rob "Oh my God!?"
    scene a3825 with dssa 
    rob "That one!"
    scene a3826 with dssa 
    sas "What about it?"
    scene a3827 with dssa
    rob "That's insane!"
    scene a3828 with dssa
    sas "Hmm... Maybe you're right..."
    scene a3829 with dssa
    sas "She might enjoy it."
    scene a3835 with dssr
    pause 
    scene a3830 with dssr
    rob "They're all way too much!"
    rob "Just let her like- flash her boobs!"
    scene a3831 with dssa
    sas "That's a normal Wednesday to her."
    scene a3832 with dssa
    n "Yo, what up?"
    scene a3833 with dssa
    d "They're trying to come up with a punishment for Ayua."
    scene a3834 with dssa
    n "You've got a list? Can I see?"
    scene a3836 with dssr
    pause 
    scene a3837 with dssa
    n "Yo..."
    scene a3838 with dssa
    pause  
    scene a3839 with dssa
    "The Cheeto takes another look to see if she read that right."
    scene a3840 with dssa
    n "...Okay."
    n "Remind me to never ever be on the receiving end of your fury, Sasha."
    scene a3841 with dssr
    n "[name], if I'm ever drunk, make sure I don't agree to a bet with her!"
    scene a3842 with dssa
    d "If someone as deranged as you is shocked, she must be... special."
    scene a3843 with dssr
    sas "Are you implying I'm deranged?"
    scene a3844 with dssa
    menu:
        "Yes.":
            $ Sasha_Deranged = True 
            scene a3845 with dssr
            pause 
        "No.":
            scene a3845 with dssr
            pause 
    scene a3846 with dssr 
    n "Two of them could have long-term consequences."
    scene a3847 with dssr
    sas "Would it be a punishment if they didn't?"
    scene a3848 with dssr
    n "I thought I was weird."
    scene a3849 with dssa
    d "If you're at loss for words, Sasha scares me."
    scene a3850 with dssa
    n "She should, man."
    scene a3851 with dssa
    rob "I once bet her and never did it again!"
    scene a3852 with dssa
    n "What did she do to you?"
    scene a3853 with dssa
    sas "You're overly dramatic, Robin."
    scene a3854 with dssa
    rob "You said you'd not give me anything bad!"
    scene a3855 with dssa
    sas "And I didn't."
    scene a3856 with dssa
    rob "I wasn't allowed to wear underwear for a month!"
    scene a3857 with dssa
    ay "That's a free one!"
    scene a3871 with dssr
    rob "Not if you love skirts!"
    scene a3858 with dssr
    ay "Especially if you love skirts! I'm doing it right now."
    scene a3859 with dssa
    ay "Feeling that little breeze on your tata is the whole reason I wear skirts!"
    scene a3860 with dssr
    d "I have reason to believe you two are in way too deep."
    scene a3861 with dssa
    ay "That's why nobody will remember your name, George."
    ay "You don't have the guts."
    scene a3860 with dssa
    d "You're not baiting me into a bet."
    scene a3862 with dssa
    ay "I wasn't."
    ay "We don't bet guys."
    scene a3863 with dssa
    ay "This is between me and Sasha."
    ay "The last thing we want is some guy betting for a night with us."
    scene a3864 with dssr
    d "You should make it your goal to reach 100 wins."
    d "Whoever reaches it first becomes the queen."
    scene a3865 with dssa
    ay "And a super punishment!" 
    scene a3866 with dssa
    ay "AND then we start over and begin Season 2 of Ayua versus Sasha!"
    scene a3867 with dssa
    n "If the things on Sasha's list are just normal punishments, what on god's earth would be a super punishment?"
    scene a3868 with dssa
    ay "Running naked through college."
    scene a3883 with dssr
    sas "I have this on my list."
    scene a3869 with dssr
    ay "Oh."
    scene a3870 with dssa
    ay "Then running naked through college, covered in oil, with a remote controlled vibrator on full power!"
    scene a3872 with dssr
    sas "I'll think about your second punishment a little longer and let you know."
    scene a3873 with dssa
    sas "Maybe I'll go above and beyond..."
    scene a3874 with dssa
    n "Like a gangbang?"
    scene a3873 with dssa
    sas "Like joining the book club."
    scene a3874 with dssr
    ay "You wouldn't do that to me, would you?!"
    scene a3875 with dssa
    sas "You have no idea what I would do to you."
    scene a3874 with dssr
    ay "We're a hundred and forty bets in. Roughly 70 punishments each... I have a pretty good idea of what you're capable."
    scene a3884 with dssr
    n "How are you two still alive after so many punishments?"
    scene a3891 with dssa
    ay "They weren't always this extreme. But you naturally tend to up-do your previous punishment... Or if you thought the other was unusually harsh, you tend to punish them a little harder too."
    ay "That way it escalates."
    scene a3885 with dssr
    n "Also! The book club isn't bad at all. Sure, the book we're reading could be better but... It's not bad."
    scene a3875 with dssr
    sas "Don't forget. You can't put anything over or under the shirt, you're allowed to wash it, but you need to wear it again as soon as possible."
    sas "You have to go swimming with it, and you also can't take it off during intercourse."
    scene a3876 with dssa
    ay "You want people to look at your picture while having sex with me?"
    scene a3877 with dssa
    sas "No, I want you to know they're looking at me."
    scene a3892 with dssr
    ay "You're so sick in your own twisted way..."
    scene a3893 with dssa
    ay "So the real punishment is that my tiddies are slightly on display?"
    scene a3878 with dssr
    sas "If you fail to follow the instructions or anyone sees you without it, you'll have to go on that date with Brandon."
    sas "The same applies to you not dyeing your hair white. You won't get another chance."
    scene a3894 with dssr
    pause 
    scene a3895 with dssa
    ay "I'd rather pick out my own eyes, and kill myself and Nami in the process."
    scene a3886 with vpunch
    n "Yo! Why me?!"
    scene a3887 with dssa
    n "And who's Brandon?" 
    scene a3888 with dssa
    ay "The most pathetic, disgusting, and worthless individual we know."
    scene a3889 with dssa
    ay "A nepo-baby with a lot of money, no impulse control, and an over the top WormTube personality."
    ay "You know? These loud, annoying douches nobody likes and pull shitty pranks on people?"
    ay "We use a date with him as the ultimate punishment for not doing a punishment... So none of us dares to skip one."
    scene a3890 with dssa
    ay "The thought of just listening to this dude for two hours drives every respectable lady insane."
    scene a3879 with dssa
    sas "You understand the rules for the shirt?"
    scene a3881 with dssr
    ay "I do."
    ay "Wait? Can I wear my dress tomorrow?"
    scene a3880 with dssa
    sas "But of course- not."
    scene a3881 with dssa
    ay "I hate you! How am I supposed to get laid in this?!"
    scene a3880 with dssa
    sas "Not my problem." 
    scene a3881 with dssa
    ay "I paid so much for my dress..."
    scene a3880 with dssa
    sas "Oh no..."
    scene a3882 with dssa
    pause 
    while Cpoint is False:
        scene a3896 with dssa
        menu:
            "The worst punishment one of you has done yet?":
                $ Info_Ay_Sas_Punishment = True 
                scene a3897 with dssa
                ay "We'll never tell."
                ay "But we have a rule that we can never put others at risk."
            "Is it always just you and Sasha?":
                $ Info_Ay_Sas_Auswahl_Bet = True 
                scene a3897 with dssa
                ay "Mostly."
                ay "We do, of course, sometimes bet our friends for little things."
                ay "A friend of us recently had to dye her hair partialy white."
            "Do you want to bet me?":
                $ Info_Ay_Sas_Bet_Me = True
                scene a3898 with dssa
                if Info_Ay_Sas_Bet_Yacht is True:
                    ay "Again, we don't bet guys."
                else:
                    ay "Sorry, we don't bet guys."
            "Continue":
                $ Cpoint = True 
                pass 
    $ Cpoint = False
    scene a3899 with dssa
    sas "Regarding our personality-switch bet..."
    scene a3900 with dssr
    sas "Let me quote something you said yesterday."
    scene a3901 with dssa
    if BellaDate is True:
        sas "'I will give [name] a blowjob, so that he and Bella can finally do it.'"
    else:
        sas "'I will give [name] a blowjob, and maybe it will cause him to do it with Bella later.'"
    if BellaDate is False:
        scene a3910 with dssr
        b "Did I just hear that right?"
        scene a3902 with dssr 
    else:
        scene a3902 with dssa
        pause
    ay "..."
    scene a3903 with dssa
    sas "The whole spiel was never about you asking random guys for something. It was specifically catered to [name]."
    sas "I wasn't out of character. You were."
    scene a3904 with vpunch
    ay "Fuck!"
    if RobinOffHook5x0 is True:
        scene a3905 with dssa
        d "Are you sure you aren't suffering from a gambling addiction as well?"
        scene a3906 with dssa
        sas "No."
        sas "I'm not the driving force behind this. I just enjoy seeing Ayua lose."
        scene a3907 with dssa
        ay "That's very hurtful."
        scene a3908 with dssa
        sas "Good."
        scene a3909 with dssa
        ay "Your next punishment will be a brutal one." 
    scene a3911 with dssr
    "You leave the blabbering girls behind and go back to your seat." 
    scene a3912 with dssr
    pause 
    if KateNetwork5x5 is True:
        scene a3913 with dssa
        kat "So."
        scene a3914 with dssa
        pause
        scene a3915 with dssa
        kat "What?"
        scene a3916 with dssa
        d "Why are you here?"
        scene a3915 with dssa
        kat "I have news."
        scene a3916 with dssa
        d "Let's talk later. Bella will be back any second and I know you two aren't fond of each other."
        scene a3917 with dssa
        kat "I don't give a fuck if she sees me here with you."
        scene a3918 with dssa
        kat "If you want, I can sit in your lap just to make her angry."
        scene a3919 with dssr
        kat "We need to find out who takes the pictures here..."
        scene a3955 with dssr
        pause
        scene a3920 with dssr
        d "Do you know anyone that has taken pics before and got busted?"
        scene a3919 with dssa
        kat "No, but someone said that Mario Holgerson is involved."
        scene a3920 with dssa
        d "...Say that name again."
        scene a3921 with dssa
        kat "Mario Holgerson."
        scene a3922 with dssa
        d "(I need to find out more about him.)"
        d "Alright, thanks for filling me in."
        pause
        if KateTeasing2 is False:
            pass 
        elif KateTeasing2 is True and BellaDate is True:
            scene a3923 with dssr
            menu:
                "Ask Kate for help to satisfy Nami's revenge.":
                    $ KateVSBella = True 
                    scene a3924 with dssr
                    d "I think I could use your help with something."
                    scene a3925 with dssa
                    kat "Shoot."
                    scene a3926 with dssa
                    d "What do you think of Nami?"
                    scene a3927 with dssa
                    kat "She's cool. I like her."
                    kat "She dislikes Bella. That makes me like her even more."
                    scene a3928 with dssa
                    d "Right... Did Nami tell you about some sort of revenge?"
                    scene a3927 with dssa
                    kat "She mentioned that she'd want to get back at Bella and had a plan in the works."
                    kat "Buuuut, I won't give you any details."
                    scene a3928 with dssa
                    d "Yeah, the Cheeto is insane. I want to keep her from getting in trouble."
                    scene a3929 with dssa
                    kat "Meaning?"
                    scene a3930 with dssa
                    d "We need to prank Bella."
                    scene a3931 with dssa
                    kat "...You want to prank your own girlfriend?"
                    kat "And you want the help of the person she hates the most?"
                    scene a3932 with dssa
                    d "I think she hates some girl called Ceril more."
                    scene a3933 with dssa
                    kat "Who doesn't?" 
                    scene a3934 with dssr
                    d "Okay... First of all, she's not my girlfriend."
                    d "But yes. The Cheeto will go too far. She always does."
                    d "She once pranked me and my ex in a way that left us speechless."
                    scene a3935 with dssa
                    d "I don't want Bella or Nami to get in trouble."
                    scene a3936 with dssa
                    kat "Why would I help Bella?"
                    scene a3937 with dssa
                    d "Because I'd make sure she'll never be a problem for you again."
                    d "...As long as you aren't a problem to her."
                    menu:
                        "And Bella deserves a little bit of heat.":
                            $ REP_BXXEHEAT = True 
                            scene a3938 with dssa
                            kat "On that we can agree."
                        "Don't say that.":
                            pass 
                    if REP_BXXEHEAT is True:
                        scene a3939 with dssa
                        pause 
                    else:
                        scene a3940 with dssa
                        pause 
                    scene a3941 with dssa 
                    kat "Okay, maybe I'll help you."
                    kat "Any ideas so far?"
                    scene a3942 with dssa
                    d "It needs to be enough to satisfy Nami but not so much that Bella crashes out."
                    d "Nami needs to feel like she's got one up on her."
                    scene a3941 with dssa 
                    kat "That should be doable."
                    if REP_BXXEHEAT and Bella_OR_STG1 is True:
                        scene a3943 with dssa  
                        kat "But..."
                        scene a3944 with dssa
                        kat "...I want something too."
                        scene a3945 with dssa
                        d "...And what is that?"
                        scene a3946 with dssa
                        kat "I'll help you with Nami, if you help me get one on Bella."
                        scene a3945 with dssa
                        d "What? We are getting one on her." 
                        scene a3946 with dssa
                        kat "It's not really going to be anything... but you said... the bitch deserves some heat."
                        kat "She thinks she's so much better than me. She dares to look down on me."
                        kat "I would really like to take her down a notch." 
                        scene a3947 with dssa
                        d "And how would you do that?"
                        scene a3946 with dssa
                        kat "I'm not so sure yet... When I still played football, she once hid my bra and I had to play without it..." 
                        scene a3948 with dssa
                        kat "That was... awkward."
                        scene a3949 with dssa
                        kat "Do the same to her."
                        scene a3950 with dssa
                        d "Getting her to take off her bra?"
                        scene a3949 with dssa
                        kat "That or hide it."
                        scene a3951 with dssr
                        kat "She's wearing that short crop top... Yeah, hide her undershirt or get her to take it off and I'll help you with Nami."
                        menu:
                            "Deal.":
                                $ BellaCropTop = True 
                                scene a3952 with dssr
                                pause 
                            "Sorry, no.":
                                scene a3949 with dssr
                                kate "Then come up with something else... Otherwise I won't help you."
                    else:
                        menu:
                            "Embarrassing her a little bit sounds fine.":
                                $ Kate_VS_Bella_Naughty = True 
                                scene a3953 with dssa
                                kat "Good."
                            "We'll come up with something else... Spontaneous.":
                                scene a3949 with dssr
                                kat "Let me know when you got something."
                "Don't ask Kate for help.":
                    pass 
        scene a3954 with dssr
        pause 
        scene a3956 with dssr
        pause 
        if BellaDate is True:
            scene a3957 with dssr
            pause 
        else:
            pass 
        scene a3958 with dssa
        b "What was that bitch doing here?"
        scene a3959 with dssa
        d "I'll tell you another time."
        if BellaNonExclusive5x0 is True:
            scene a3969 with dssr
            b "How about now?"
            scene a3970 with dssa
            d "It's about some creeps at the college."
            scene a3971 with dssa
            b "What did you do?"
            scene a3972 with dssa
            d "Funny." 
            scene a3973 with dssa
            d "Apparently, they are responsible for the rumors about me and Robin. She asked if I wanted to go on a stakeout with them. I declined."
            scene a3974 with dssa
            b "Hmm, I can help you find them. Let's kick the pale cunt out, though."
            scene a3975 with dssa
            d "What happened between you and Kate?"
            scene a3976 with dssa
            b "None of your business."
            scene a3977 with dssa
            d "Okay... One question."
            d "Did both parties do something wrong or is she just a cunt?"
            scene a3978 with dssa
            b "She got what she deserved."
            scene a3979 with dssa
            d "Both parties... Not surprising."
            scene a3980 with dssa
            pause
            scene a3981 with dssr
            pause 
            scene a3982 with dssa
            d "Hey."
            scene a3983 with dssr
            pause 
            scene a3984 with dssa
            ay "Who are you?"
            scene a3985 with dssa
            d "What can you tell me about Kate and Bella?"
            scene a3986 with dssa
            ay "Long story short: They hate each other."
            scene a3987 with dssa
            d "I figured that out. What happened between them?"
            scene a3986 with dssa
            ay "I assume Bella didn't tell you, so I won't do it either." 
            scene a3987 with dssa
            d "Bella started it."
            scene a3986 with dssa
            ay "I'm not falling for that."
            scene a3988 with dssa
            d "What do you think of Kate?"
            scene a3989 with dssa
            ay "I have a bias against her because Bella's my honey..."
            ay "But she's not thaaat bad, I guess."
            scene a3990 with vpunch
            ay "However, if I had to kill her to save Bella... I would do so without hesitation."
            scene a3991 with dssa
            d "Would you kill me to save Bella?"
            scene a3992 with dssa
            ay "Of course."
            scene a3991 with dssa
            d "Sasha too?"
            scene a3992 with dssa
            ay "If I'm ahead on bets, I'll take her out."
            scene a3993 with dssr
            d "And Nadia?"
            scene a3994 with dssa
            ay "Hell yeah. That way I can be the bridesmaid and won't have to listen to insane alien artifact stories."
            scene a3995 with vpunch
            ay "Like bitch, no! We're not going to travel around the world to look for a pyramid under the ice!"
            scene a3996 with vpunch
            ay "I've seen AVP! I know how this ends!"
            scene a3997 with dssa  
            pause 
            scene a3998 with dssa  
            ay "Get that improvised dildo out of my face."
            scene a3999 with dssr  
            na "I'll put this banana down your throat."
            scene a4000 with dssa  
            ay "I bet you would love that."
            scene a4001 with dssa 
            pause 
            scene a4002 with dssa 
            na "I would."
            scene a4003 with dssr
            pause 
            scene a4004 with dssr
            ay "[name]. Don't sleep with Kate, okay?"
            scene a4004 with vpunch
            na "He wants to sleep with Kate?!"
            scene a4005 with dssa
            d "I don't." 
            scene a4006 with vpunch
            na "Don't sleep with Kate! You will hurt Bella!"
            scene a4007 with dssa
            d "Ayua is kidding!"
            scene a4006 with dssa
            na "That wasn't her 'I'm kidding' voice."
            scene a4008 with dssa
            d "All I did was ask Ayua what she thinks about her, and what happened between her and Bella."
            scene a4009 with dssr
            na "I'll tell you what happened between them."
            scene a4010 with dssa
            d "Go ahead."
            scene a4011 with dssa
            na "IF..."
            scene a4012 with dssa
            d "Of course..."
            scene a4013 with dssa
            na "If you help me with something."
            scene a4014 with dssr
            d "...What is it?"
            scene a4013 with dssa
            na "I need something from the college storage."
            na "And one item from this classroom."
            scene a4016 with dssa
            d "What is it?"
            scene a4017 with dssa
            na "Wildlife cameras with motion detectors."
            na "They used them here at school for surveillance. And as far as I know, there is still a bunch left in the storage."
            na "They are in a room in the basement."
            scene a4019 with dssa
            d "...I'm not breaking in there."
            scene a4018 with dssa
            na "You don't have to. I already got the key."
            na "But there's a security guy... And I need you to go in the room and... borrow... a few of those cameras."
            scene a4020 with dssr 
            d "What?"
            scene a4018 with dssr
            na "I'll distract him while you sneak into the room."
            scene a4021 with dssa
            d "How are you going to distract him?"
            scene a4022 with dssa
            na "He likes Peacehammer and I'm well versed about the lore."
            scene a4023 with dssa
            na "On top of that."
            if Nadia_Hörnchen is True:
                scene a4025 with dssr
                pause
                scene a4026 with dssa
                pause 
                scene a4027 with dssr
                d "You'll distract him with nerd talk and boobs?"
                scene NadiaNoddy with dssa 
                pause 
                scene a4028 with dssa
                d "(Our little encounter earlier might've affected her a little more than I thought it would.)"
                d "(Now I understand why Ayua said we shouldn't involve her.)"
                scene a4027 with dssr
                menu:
                    "Tease Nadia":
                        if NadiaBananaHalf04 is True:
                            $ Nadia_Tease = True
                            scene a4030 with dssr 
                            d "Are you feeling alright?"
                            scene a4029 with dssa
                            na "Yes? Why?"
                            scene a4031 with dssa 
                            "You slowly, yet with gentle force, push your hands up her thighs."
                            scene a4032 with dssa 
                            d "Just asking."
                            scene a4033 with dssr
                            pause 
                            d "I hope Bella and I didn't scare you in the hallway..."
                            scene a4035 with dssr
                            na "No."
                            scene a4034 with dssr 
                            "She spreads her legs just a little more."
                            pause 
                            play sound "Music/Sfx/Punch.ogg"
                            scene a4037 with vpunch 
                            pause 
                            scene a4038 with dssr 
                            ay "What did I tell you?"
                            scene a4036 with dssa 
                            d "...I was just teasing her a little."
                            scene a4038 with dssa
                            ay "Don't poke the tiger."
                            scene a4039 with dssr  
                            d "...I guess the distraction will work."
                        else:
                            scene a4040 with vpunch 
                            pause 
                            scene a4041 with dssr  
                            na "Do you want to die?"
                            scene a4042 with dssa 
                            d "Does this free me from being Bella's project partner? If so, yes."
                            scene a4033 with dssa
                            na "It doesn't. Ghosts are bound to unresolved tasks. You'll have to finish the project to be released."
                    "Don't tease the poor noodle.":
                        pass
                             
            else:
                scene a4024 with dssr
                pause 
                scene a4025 with dssa
                pause  
                scene a4043 with dssr
                d "You'll distract him with nerd talk and boobs?"
                "She nods."
                scene a4044 with dssa
                menu:
                    "I guess that'll work.":
                        scene a4046 with dssa 
                        pause
                    "You definitely got two big distractions.":
                        if NadiaBananaHalf04 is True:
                            scene a4046 with dssa 
                            pause 
                        else:
                            scene a4045 with dssa 
                            pause  
            scene a4047 with dssr 
            d "But the info about Kate and Bella isn't enough for me to take the risk."
            scene a4048 with dssa 
            na "You don't need to worry if you get caught."
            scene a4047 with dssa 
            d "Why's that?"
            scene a4048 with dssa 
            na "I have an ace in the hole."
            scene a4049 with dssr 
            na "If the Kate info isn't enough, what do you want?"
            scene a4050 with dssa 
            d "Let me think about it."
            scene a4049 with dssa 
            na "Get back to me soonish or I'll find someone else."
        else:
            scene a3960 with dssr
            b "You can do better than her."
            if Bella_OR_STG1 is False:
                scene a3962 with dssr
                d "*Sigh* For the last time, I'm not going to throw you one."
                scene a3961 with dssa
                b "Eww!"
            else:
                scene a3962 with dssr
                d "Is that a compliment I'm hearing there?"
                scene a3961 with dssa
                b "No. She's absolute trash. The lowest of the low."
                b "You're half a level above it, so you can indeed do better."
                scene a3963 with dssr
                d "I think you're even lower than her."
                scene a3964 with dssa
                b "Lower on the scale, yeah."
                scene a3965 with dssa
                pause 
                scene a3966 with dssa
                b "Why am I sitting here with you?"
                scene a3967 with dssr 
                pause 
                scene a3968 with dssa
                d "Thank God."
    else:
        scene a3984 with dssr
        ay "[name]!"
        scene a3994 with dssa
        ay "Help me kill Nadia so I can be Bella's bridesmaid and don't have to listen to insane alien artifact stories."
        scene a3995 with vpunch
        ay "Like bitch, no! We're not going to travel around the world to look for a pyramid under the ice!" 
        scene a3997 with dssa  
        pause 
        scene a3998 with dssa  
        ay "Get that improvised dildo out of my face."
        scene a3999 with dssr  
        na "I'll put this banana down your throat."
        scene a4000 with dssa  
        ay "I bet you would love that."
        scene a4001 with dssa 
        pause 
        scene a4002 with dssa 
        na "I would."
        scene a4003 with dssr
        pause 
        scene a4005 with dssr
        d "By the way, what's this Kate like?"
        scene a4004 with dssr
        ay "You want to sleep with Kate?"
        scene a4006 with vpunch
        na "Don't sleep with Kate! You will hurt Bella!"
        scene a4007 with dssa
        d "Where did I say that?!"
        scene a4009 with dssr
        na "I'll tell you what happened between them."
        scene a4010 with dssa
        d "Go ahead."
        scene a4011 with dssa
        na "IF..."
        scene a4012 with dssa
        d "Of course..."
        scene a4013 with dssa
        na "If you help me with something."
        scene a4014 with dssr
        d "...What is it?"
        scene a4013 with dssa
        na "I need something from the college storage."
        na "And one item from this classroom."
        scene a4016 with dssa
        d "What is it?"
        scene a4017 with dssa
        na "Wildlife cameras with motion detectors."
        na "They used them here at school for surveillance. And as far as I know, there is still a bunch left in the storage."
        na "They are in a room in the basement."
        scene a4019 with dssa
        d "...I'm not breaking in there."
        scene a4018 with dssa
        na "You don't have to. I already got the key."
        na "But there's a security guy... And I need you to go in the room and... borrow... a few of those cameras."
        scene a4020 with dssr 
        d "What?"
        scene a4018 with dssr
        na "I'll distract him while you sneak into the room."
        scene a4021 with dssa
        d "How are you going to distract him?"
        scene a4022 with dssa
        na "He likes Peacehammer and I'm well versed about the lore."
        scene a4023 with dssa
        na "On top of that."
        scene a4024 with dssr
        pause 
        scene a4025 with dssa
        pause  
        scene a4043 with dssr
        d "You'll distract him with nerd talk and boobs?"
        "She nods."
        scene a4044 with dssa
        menu:
            "I guess that'll work.":
                scene a4046 with dssa 
                pause
            "You definitely got two big distractions.":
                if NadiaBananaHalf04 is True:
                    scene a4046 with dssa 
                    pause 
                else:
                    scene a4045 with dssa 
                    pause  
        scene a4047 with dssr 
        d "But the info about Kate and Bella isn't enough for me to take the risk."
        scene a4048 with dssa 
        na "You don't need to worry if you get caught."
        scene a4047 with dssa 
        d "Why's that?"
        scene a4048 with dssa 
        na "I have an ace in the hole."
        scene a4049 with dssr 
        na "If the Kate info isn't enough, what do you want?"
        scene a4050 with dssa 
        d "Let me think about it."
        scene a4049 with dssa 
        na "Get back to me soonish or I'll find someone else." 
    scene black with Dissolve(2)
    with Pause(.5)
    scene a4051 with dssb 
    pause 
    scene a4052 with dssa
    with Pause(.3)
    scene a4053 with vpunch
    u "That's mine now."
    scene a4054 with dssa
    sas "Why do you wear cleavages this big?"
    scene a4055 with dssa
    u "Why did you get banned from the Solsikke restaurant?"
    scene a4056 with dssa
    sas "I redact my question."
    scene a4057 with dssa
    pause 
    scene a4058 with dssa
    u "Stop staring at my boobs."
    scene a4059 with dssa
    d "I'm not."
    scene a4058 with dssa
    u "I was talking to Bella."
    scene a4073 with dssr
    b "I look where I want, Justine."
    scene a4060 with dssa
    ju "Are you coming to the game next Friday?"
    scene a4061 with dssa
    b "Of course."
    scene a4062 with dssr
    ju "Will you bring your boyfriend?"
    scene a4063 with dssa
    b "He's not my boyfriend."
    scene a4064 with dssa
    ju "Are you single?"
    if BellaDate is True:
        scene a4074 with dssr
        pause 
        scene BellchenNod with dssa
        d "Sure."
    else:
        scene a4076 with dssr
        d "Ya."
    scene a4065 #sfx 
    ju "Oh!"
    ju "He's Nami's friend, right?"
    scene a4066 with dssa
    sas "Mhm."
    scene a4067 with dssa
    d "You look like you haven't slept in a while."
    scene a4068 with dssa
    ju "That's just how I look." 
    ju "I have the ability to nap wherever I want."
    scene a4069 with dssa
    "She yawns."
    scene a4070 with dssr
    pause 
    scene a4071 with dssr
    shan "I apologize for the delay. I'm professor Shan."
    scene a4072 with dssr
    shan "Please take a seat everyone."
    stop music fadeout 5
    scene black with Dissolve(2)
    show text "120 minutes later." with dissolve 
    with Pause(3)
    with Pause(.5)
    play ambient "Music/Sfx/Ambient_Suburban.ogg"
    hide text with dissolve 
    scene a4077 with dssb
    pause 
    scene a4078 with dssr
    d "I forgot to tell you something." 
    scene a4079 with dssa
    if BellaKiss3x5 is True:
        b "You're trans and the doctor's lied when they told you the fake penis would work?"
    else:
        b "You're trans?"
    scene a4078 with dssa
    d "Vanessa asked me to go on a double date with her and her boyfriend."
    scene a4080 with dssa
    b "You don't even have to ask."
    scene a4081 with dssa
    d "You're not coming with me."
    scene a4082 with dssr
    pause
    scene a4083 with dssa
    b "...Why not?"
    scene a4084 with dssa
    if BellaDate is False:
        d "Two reasons..."
        scene a4085 with dssa
        d "First: I'd like to take someone I might actually want to date."
        scene a4086 with dssa
        d "Second, it's too risky."
    else:
        scene a4086 with dssa
        d "It's too risky."
    d "If it was for me you'd never meet Vanessa again."
    scene a4087 with vpunch
    b "Okay! I admit it! I miscalculated when I first met her! But it doesn't mean I can't be trusted around her!"
    scene a4088 with dssr
    d "I will use this D-date to get some info... And see what Mario is really like."
    scene a4089 with dssa
    b "Who will you take with you?"
    if BellaNonExclusive5x0 is True:
        scene a4090 with dssa
        d "*Sigh* Vanessa asked for you but I don't want to-"
        scene a4092 with dssa
        b "Count me in."
        scene a4091 with dssa
        d "Pretend you're sick or something."
        scene a4093 with dssa
        b "I'm sick of your bullshit!"
        scene a4094 with dssa
        b "I'll come with you."
        scene a4091 with dssa
        d "We'll see."
    elif ZaraVanessaDate5x5 is True:
        scene a4091 with dssa
        d "I'm taking Zara."
        scene a4094 with dssa
        b "Well, okay."
        if BellaKiss3x5 is True:
            scene a4095 with dssa
            pause
            scene a4096 with dssa
            b "Are you into her?"
            scene a4097 with dssa
            d "Zara is my trainer."
            scene a4096 with dssa
            d "Neither she nor I have any romantic interest in each other."
            scene a4098 with dssr
            b "Yeah, the 'just a friend' lie people tell themselves."
            scene a4099 with dssa
            pause
            if BellaDate is False:
                scene a4100 with dssa
                d "Why would you care?"
                scene a4098 with dssa
                b "I don't. I'm just making conversation."
            else:
                scene a4101 with dssa
                pause 
                scene a4103 with dssr
                pause
                scene a4102 with dssa
                d "I won't leave before I've seen you naked."
                scene a4104 with dssa
                b "*Chuckles* Great."
    scene a4092 with dssa
    b "As long as it's not Mila."
    if MilaKiss4x5 is True:
        scene a4105 with dssr
        d "She's one of my options."
        scene a4106 with dssa
        b "She's being sued by them. I'm a risk factor? She's that times a hundred."
        scene a4107 with dssa
        d "True."
        scene a4107 with dssa
    else:
        scene a4105 with dssr
        d "Your Mila hate is getting annoying."
        scene a4106 with dssa
        b "I didn't even say anything bad!"
        b "She's being sued by them! Of course she's a bad choice!"
    if VicDate or VicDateEntry2:
        if MilaKiss4x5 is False:
            scene a4107 with dssa
        d "Victoria is also an option."
        scene a4108 with dssa
        b "Yeah, take her for some pity points."
        scene a4109 with dssa
        d "I fear Vic might be get a little too comfortable with someone like Vanessa."
        scene a4110 with dssa
        b "Don't underestimate her."
        scene a4109 with dssa
        d "Do you know something about her I don't?"
        scene a4110 with dssa
        b "All I'm saying is that you shouldn't underestimate her. She can hold her own."
    else:
        scene a4110 with dssa
    b "Take Eva."
    scene a4111 with dssa
    d "Who?"
    scene a4112 with dssa
    b "Eva? My friend?"
    scene a4111 with dssa
    d "I'm totally blanking."
    scene a4112 with dssa
    b "...The skinny one?"
    scene a4113 with dssa
    d "Oh! Beany!"
    scene a4111 with dssa
    d "Why on earth would I take her with me?"
    if BellaNonExclusive5x0 is True:
        scene a4114 with dssr
        b "It would mean a lot to me."
        scene a4115 with dssa
        "You furrow your brow."
        scene a4114 with dssa
        b "I owe her a blind date after she won against me in Super Wormio."
        b "Two birds with one stone."
        scene a4116 with dssa
        b "And... You're going to a restaurant. She needs to put on weight."
        scene a4117 with dssa
        d "Does she want to gain weight so badly?"
        scene a4116 with dssa
        b "Yes."
        scene a4118 with dssr
        b "And don't ever make fun of her weight again."
        scene a4119 with dssa
        d "Do you want me to take Eva to the date so you don't have to worry about me doing something... 'stupid'"
        if BellaSuspicious is False:
            scene a4120 with dssa
            b "No. We're not exclusive."
        else:
            scene a4120 with dssa
            b "Maybe."
        scene a4121 with dssa
        d "Don't you think she expects you to get her a real date?"
        scene a4122 with dssa
        b "She knows very well that I'm gonna fuck with her in some way."
        if EvaFrenchKissS2_1x0 is True:
            scene a4123 with dssa
            d "(I should decline Eva... There's no promise that I won't push the boundaries a little.)"
        menu:
            "No, not Eva.":
                $ EvaDateVanessa = False 
                scene a4125 with dssa
                b "Pff... Fine."
            "Alright, I'll take Eva.":
                $ EvaDateVanessa = True 
                scene a4124 with dssr
                b "Good."
    else:
        menu:
            "No, not Eva.":
                $ EvaDateVanessa = False 
                scene a4125 with dssa
                b "Pff... Fine."
            "Alright, I'll take Eva.":
                $ EvaDateVanessa = True 
                scene a4124 with dssr
                b "Good."

    if NiaDate5x0 is True:
        scene a4126 with dssa
        d "There's also Nia."
        scene a4127 with dssa
        if BellaNonExclusive5x0 is True:
            b "How was it at her place?"
            scene a4128 with dssa
            d "It was good. We just played video games for hours."
            d "She's got money."
            scene a4129 with dssa
            b "With great pussy, comes great money. Gandhi or so."
        else:
            scene a4129 with dssa
        b "I think she has autism or some shit."
        scene a4130 with dssa
        d "She doesn't."
        scene a4131 with dssa
        b "She has no boundaries or any sort of decency in a public place... Especially in public showers."
        scene a4132 with dssr
        d "Yeah, she's a little behind when it comes to that."
        if BellaNonExclusive5x0 is True:
            if BellaSuspicious is True:
                $ Va_DD_Bella_Against_Nia = True
                b "Pick someone else, though."
                scene a4134 with dssa
                d "Why?"
                scene a4135 with dssa
                b "For I-have-sex-on-camera-reasons."
                scene a4136 with dssa
                d "Hmm, I thought we weren't exclusive." 
                scene a4137 with dssa
                b "The last thing I want to see is your hairless ass on Venus."
            else:
                scene a4133 with dssa
                b "I'm alright with Nia."
                scene a4134 with dssa
                d "Oh really?"
                scene a4135 with dssa
                b "Yup."
        scene a4138 with dssr
        b "I spoke to Nia and I get that motherly itch to protect her."
        b "She's like a retarded little puppy that you just want to take care of."
        scene a4139 with dssr
        "For a moment you contemplate to say something but you just sigh."
    pause 
    if SashaBook5x0 is True:
        scene a4140 with dssr 
        pause
        scene a4141 with dssa 
        b "A cheesy romance novel? Really?"
        "You ignore her."
    play sound "Music/Sfx/Slap4.ogg"
    scene a4142 with vpunch #sfx  
    pause 
    scene a4143 with dssr 
    ay "Auuu!"
    scene a4144 with dssa 
    ay "Fuck you Mia!"
    scene a4145 with dssr 
    pause 
    scene a4146 with dssr  
    ay "My ass has been slapped like fifteen times!"
    scene a4147 with dssa 
    ay "You bitch, you'll pay for this!"
    if BellaDate and SashaBook5x0 is True:
        scene a4148 with dssr 
        b "If we ever spend a weekend together and my ass doesn't look like this by the end. I'm leaving you."
    elif BellaDate is True:
        scene a4149 with dssr 
        b "If we ever spend a weekend together and my ass doesn't look like this by the end. I'm leaving you."
    scene a4150 with dssr
    ay "Sucker."
    scene a4151 with dssa 
    d "Can I do something for you?"
    scene a4150 with dssa
    ay "You didn't come by my dojo."
    scene a4172 with dssr
    sas "...You invited him?" 
    scene a4173 with dssa
    ay "Yes."
    scene a4152 with dssr
    d "Yeah, I've got a lot on my plate."
    if BellaNonExclusive5x0 is True:
        scene a4153 with dssr
        ay "Have you took a taste from Bella's plate?"
        scene a4154 with dssa
        d "What?"
        scene a4155 with dssa
        ay "Have you put your head between her legs?"
        scene a4156 with dssa
        d "No."
        scene a4157 with dssa
        ay "My thoughts and prayers to you."
        scene a4167 with dssa
        "Bella furrows her brows."
        scene a4158 with dssr
        ay "...Maybe, all he needs is a bit of external help."
        play sound "Music/Sfx/Slap.ogg"
        scene a4159 with vpunch
        b "Bitch, that's my property."
        scene a4160 with dssr
        ay "First cum, first serve."
        scene a4168 with dssr
        b "Do I need to quote the girl's code you so often use when it fits your needs?"
        scene a4161 with dssr
        ay "First of all, I quote the 'Bitch code'."
        ay "And the Bitch code, article 16, paragraph A2 states: 'If your best friend is in a rut, do your best to help her out of it.'"
        scene a4169 with dssr
        b "Article 2! 'Don't touch your friend's crush.'"
        scene a4162 with dssr
        ay "But Article 2 is overwritten by paragraph C1!"
        scene a4163 with dssa
        ay "'If your friends demeanor is negatively affected by the guy she likes, you can use excessive force on him.'" 
        scene a4169 with dssr
        b "How is this excessive force? Are you going to give him a handjob from hell?"
        scene a4164 with vpunch
        ay "If necessary, yes!" 
        scene a4170 with dssr 
        d "This is a private party, and you two aren't invited."
        scene a4171 with dssa 
        ay "Bella and I crash parties."
    scene a4165 with dssr
    ay "By the way, you owe me a 'No questions asked.'"
    scene a4166 with dssr
    ay "Otherwise, I'll show [name] some pictures of your goth phase."
    scene a4174 with dssr
    b "Don't you dare!"
    b "You'll show him nothing!"
    scene a4175 with dssa
    d "I'm intrigued."
    scene a4176 with dssa
    ay "Then you'll do what I say."
    if Nadia_Hörnchen is True:
        scene a4178 with dssr
        ay "And the first thing I'll tell you, is to stop involving Nadia in your teasing-threesomes!"
        scene a4177 with dssa
        b "Huh?"
        scene a4178 with dssa
        ay "Bitch is horny! You two involved her and now she's on sex-watch!"
        scene a4177 with dssa
        b "Oops. I didn't know it was that bad."
    scene a4179 with dssa
    ay "*Whisper* I'll show you some of her goth pics when you're at my place."
    if SashaBook5x0 is True:
        scene a4180 with dssr
        ay "Oh! Sasha's favorite book."
        scene a4181 with dssa
        pause
        scene a4182 with dssa
        ay "Are you hitting on my Sasha?"
        scene a4183 with dssa
        d "No."
        scene a4184 with dssa
        ay "Boys pretend to like shit all the time just to get in to a girl's pants."
        scene a4185 with dssr
        ay "By the way... If you want a good read, check out Bella's mother's books."
        scene a4188 with vpunch
        b "Shut up!"
        scene a4187 with dssa
        d "Amber writes books?"
        scene a4189 with dssa
        b "No!"
        scene a4185 with dssr
        ay "She does."
        scene a4186 with dssa
        ay "She's a sex therapist and some of her books are about self improvement in the sack."
        scene a4185 with dssa
        ay "Like holy shit... The things she writes in there... They're so graphic that I've used them to get off before."
        scene a4191 with dssa
        d "I'm intrigued... Not so much on the actual topic, but I need some ammunition against you."
        scene a4190 with dssa
        b "You won't read them! I swear I WILL kill you!"
        if BellaDate is True:
            scene a4192 with dssa
            d "Not if I make love to you first."
            scene a4193 with dssa
            b "...Depends on your performance."
    scene a4194 with dssr
    ay "Tell me when you got time to visit the dojo. I'd really like to see you fight Sasha."
    ay "She has a mean triangle choke. You'll suffocate between her legs..."
    scene a4195 with dssa
    ay "And after that you can fight."
    scene a4194 with dssa
    ay "Bring Nami too."
    scene a4196 with dssr
    pause
    scene a4197 with dssa
    b "The Nami influence, huh?"
    scene a4198 with dssa
    d "What?"
    scene a4199 with dssa
    b "Ayua never ever invites someone back to her dojo."
    b "I'm not allowed there."
    scene a4200 with dssa
    d "I'm not surprised. Who would want you there?"
    scene a4201 with dssr
    b "Yeah... It's gotta be because of Nami."
    scene a4202 with dssa
    b "Ayua!"
    scene a4203 with dssr
    if BellaNonExclusive5x0 is True:
        ay "Are we going to have a threesome?"
    else:
        ay "Yes?"
    scene a4204 with dssa
    b "We'll need to have a talk."
    scene a4205 with dssa
    ay "I hate talking."
    if BellaNonExclusive5x0 is True:
        ay "Let's just have sex."
        ay "You ride him and I'll sit on his face. Thoughts?"
        scene a4207 with dssr
        pause
        scene a4206 with dssr
        ay "...We'll get back to that."
    if SashaBook5x0 is True:
        scene a4209 with dssr
        pause
        scene a4210 with dssr
        pause 
        scene a4211 with dssa
        pause
    else:
        scene a4208 with dssr
        pause 
    $ play_playlist(playlist_Cafe)
    scene a4212 with dssr
    d "Gentleman."
    scene a4213 with dssa
    j "Hey!"
    scene a4214 with dssa
    t "What's up, [name]?"
    scene a4215 with dssr
    j "You missed training on Saturday."
    scene a4216 with dssa
    d "*Lie* Yeah, I had made some plans prior."
    d "(I don't feel like going into detail about the rat invasion.)"
    scene a4217 with dssa
    j "The coaches were really pissed."
    scene a4218 with dssa
    d "They can kiss my ass."
    scene a4219 with dssa
    "Jeff lets out a laugh."
    scene a4217 with dssa
    j "Don't say that to their faces, though."
    scene a4220 with dssr
    j "Please be there today."
    j "I want us both to make it."
    j "This is an opportunity not many players get."
    scene a4221 with dssa
    d "I'll be there today."
    play sound "Music/Sfx/Slap.ogg"
    scene a4222 with vpunch
    pause 
    scene a4223 with dssr
    j "Oh, by the way... We have a local two versus two tournament in my hood."
    j "If you give me your word that you'll be there. We can team up."
    scene a4224 with dssa
    d "Where do you live? Straussenberg?"
    scene a4225 with dssa
    j "Do I look like a homeless person to you?"
    scene a4224 with dssa
    d "Well-"
    scene a4226 with dssa
    j "Ahh- I see how it is... black people can't live in nice neighborhoods, heh?"
    scene a4227 with dssr
    "You both chuckle."
    scene a4228 with dssa
    j "I live in Alpine. Sure, it's no Königsberg, but it's a nice neighborhood."
    scene a4229 with dssa
    d "Maybe don't call it a 'hood' then."
    scene a4227 with dssr
    j "Yeah, I probably shouldn't do that."
    menu:
        "Count me in. I'll be your partner.":
            $ Jeff_Team = True 
            scene a4231 with dssr
            "He nods."
            scene a4232 with dssa
            j "I've never had a serious partner before."
            scene a4230 with dssa
            d "There is always a first time. I'll be gentle."
            scene a4233 with dssa
            j "*Quiet* Thanks."
        "I can't promise that I'll be there.":
            scene a4234 with dssr
            j "Shit..."
            scene a4232 with dssa
            j "Ahhh- I'll manage!"
    scene a4235 with dssr
    b "Hi." 
    scene a4236 with dssa
    j "Hey."
    scene a4237 with dssa
    j "I'll see you later [name]."
    scene a4238 with dssa
    pause 
    scene a4239 with dssa
    b "Ayua won't tell me why she'd invite you..."
    scene a4240 with dssa
    b "Are you secretly fucking her?"
    scene a4241 with dssa
    d "Yes, Ayua and I have been married for seven years. We have two beautiful children, a Bed and Breakfast in the alps of Austria, and we volunteer at the local mountain rescue service."
    scene a4242 with dssa
    pause
    scene a4243 with dssa
    b "...I knew it."
    scene a4244 with dssa
    d "(Now I'm intrigued too... Why would Ayua invite me if she doesn't even invite Bella to the dojo? Is it really because of Nami?)"
    scene a4245 with dssa
    d "Who else has seen her place?"
    scene a4246 with dssa
    b "Not her place. I've been there many times... But her dojo."
    scene a4247 with dssa
    d "Hmm. No idea. I guess I'll find out."
    scene a4248 with dssa
    b "And then you'll tell me why."
    if FuckBoyRumour is True:
        scene a7817 with vpunch
        u "Fuckboy!"
        scene a7818 with dssr
        b "What the hell was that?"
        scene a7819 with dssa
        d "You haven't seen the college paper yet?"
        scene a7820 with dssa
        b "Who reads that shit?"
        scene a7821 with dssa
        d "Apparently a lot of people."
        scene a7820 with dssa
        b "What does it say?"
        scene a7821 with dssa
        d "Just check it out yourself."
        scene a7822 with dssa
        d "But don't be surprised when it says that I did Robin or Kate."
    scene a4250 with dssr
    d "Also, please give me the address of Ayua's dojo."
    scene a4249 with dssa
    b "You don't even know where your wife works?"
    if BellaOnionRingS2_1x0 is True:
        scene a4251 with dssa
        d "Of course I know where my wife works..."
        scene a4252 with vpunch
        b "Hey, hey, hey! I'm your fiancée... Not your wife!"
        b "And soon to be ex-fiancée!" 
    scene a4253 with dssr
    d "Are you aware of the intensity of Ayua and Sasha's bets?"
    scene a4254 with dssa
    b "They're both fucking addicts."
    b "They've been doing this for as long a I remember."
    scene a4255 with dssr
    b "That's what you do when you have not a care in the world."
    scene a4256 with dssa
    d "Does Ayua really have a gambling addiction?"
    scene a4255 with dssa
    b "Yup, she always tries to bet you."
    if BellaDate is True:
        scene a4257 with dssa
        b "While I try to bed you."
    scene a4258 with dssa
    d "Do you sometimes bet Ayua?"
    scene a4260 with vpunch
    b "Hell no!"
    b "I would do it for fun if the punishments weren't so over the top."
    scene a4261 with dssa
    b "Like- let's eat a hot pepper or drink a glass of water full of salt..."
    if BellaDate is True:
        scene a4259 with dssr
        pause 
        scene a4262 with dssa
        d "Have you heard anything from that guy you hit with the car?"
        scene a4263 with dssa
        b "I heard from the guy who wanted to fight you. He approached me earlier today here at the college. He says it was a misunderstanding."
        scene a4262 with dssa
        d "He's here at ZPR?"
        scene a4263 with dssa
        b "No, he's got worms for brains."
        scene a4262 with dssa
        d "What did you say?"
        scene a4263 with dssa
        b "I reacted with a thumbs up."
        scene a4262 with dssa
        d "No insults?"
        scene a4265 with dssr
        b "In the racing community this type of shit talk is normal."
        b "Eventually, you'll be at beef with some of them."
        b "But beefs come and go."
        scene a4264 with dssa
        d "It appeared pretty serious to me."
        scene a4266 with dssa
        b "That was because of you."
        b "If they had seen me alone nothing would've happened."
        scene a4267 with dssa
        b "But that guy is into me and his neanderthal brain can't comprehend that I like someone else."
        while cpoint is False:
            scene a4268 with dssa
            menu:
                "How many girls are in the racing community?":
                    $ Info_Racing_Girls_Amount = True 
                    scene a4269 with dssa
                    b "There's always a ton of girls at the meetups. Usually friends of the racers."
                    b "But probably just ten girls that race themselves." 
                    scene a4270 with dssa
                    d "Are you at the top?"
                    scene a4271 with dssa
                    b "Kinda. If all goes well, and I win my next race- and some other guy loses, I should make third on the list." 
                    scene a4270 with dssa
                    d "That's pretty good, right?"
                    scene a4269 with dssa
                    b "Yeah."
                "Does Eva race?":
                    $ Info_Racing_Beany = True 
                    scene a4269 with dssa
                    b "She wanted to but can't handle the stress."
                    b "We race each other for fun, but she doesn't compete in the scene."
                "And Ayua?":
                    $ Info_Racing_Ayua = True 
                    scene a4269 with dssa
                    b "She likes drag racing."
                    b "But is mostly there for the social component."
                    scene a4271 with dssa
                    b "There are some good people there. Good friends that always have your back."
                "Why do you do it?":
                    $ Info_Racing_Bella_Why = True 
                    scene a4272 with dssa
                    pause 
                    scene a4271 with dssa
                    b "It makes me feel alive."
                    scene a4274 with dssr
                    b "I like the adrenalin."
                    scene a4273 with dssa
                    b "For just a moment everything becomes a blur. Pure focus, heart racing, and G forces that tremble through the body like an earthquake." 
                    scene a4275 with dssa
                    d "What about Amber?"
                    scene a4276 with dssa
                    b "She hates it."
                    b "And I understand my Mama... I'm all she really has."
                    scene a4275 with dssa
                    d "Maybe take it a little easier?"
                    scene a4277 with dssa
                    b "I will take it easier as soon as I've reached top 3."
                    scene a4278 with dssa
                    d "Why not #1?"
                    scene a4279 with dssa
                    b "He's too good. I don't think I can beat him."
                    scene a4266 with dssa
                    b "Maybe I could, if I really put in the work, but I just... I think my- yeah, I think my priorities are shifting a little."
                    b "Now that I'm at college, I'd like to focus on some other things too."
                "Continue":
                    $ cpoint = True 
                    pass
    else:
        pass 
    scene a4280 with dssr
    with Pause(.3)
    menu:
        "Ask Bella to bet with you.":
            $ Bella_Bet = True
            scene a4281 with dssa
            d "We should start betting each other."
            scene a4282 with dssa
            b "I'll bet you'll die a virgin."
            scene a4283 with dssa
            d "I'll bet that you're a slut."
            scene a4284 with dssa
            b "What do you want to bet on?"
            scene a4286 with dssa
            d "I have no idea."
            scene a4285 with dssa 
            b "Most bets happen spontaneous."
            b "I'm in as long as you don't go too crazy with the punishments."
            scene a4287 with dssa
            d "What counts as crazy?"
            scene a4288 with dssa
            b "Kissing a dead squirrel."
            scene a4289 with dssa
            d "Yeah, no."
            scene a4290 with dssa
            d "There is a big spider on your shirt."
            scene a4291 with dssr
            pause 
            scene a4292 with dssa
            pause 
            scene a4293 with dssr
            pause 
            scene a4294 with dssr
            pause 
            scene a4295 with dssa
            pause 
            scene a4296 with dssa
            if BellaDate is True:
                b "Sexual punishments are explicitly allowed."
                scene a4297 with dssa
                d "Now you're going too fa-"
                play sound "Music/Sfx/Punch.ogg"
                scene a4299 with vpunch
                b "Nu-uh!"
                b "We allow them!"
                scene a4298 with dssr
                b "If you want to punish me by sticking five fingers in, then I'll have to take it!"
                if Bella_OR_STG1 is True:
                    menu:
                        "I may cuff you to a wall with a glory hole pointing straight at your ass.":
                            $ Bella_K +=1 
                            scene a7773 with dssa
                            b "That's so oddly specific, and I'm surprised you even know what a glory hole is."
                            scene a7774 with dssa
                            d "Some weirdo showed me a video once... (Damn Cheeto.)"
                            scene a7775 with vpunch
                            b "This is worse than a punishment from Ayua or Sasha!"
                            scene a7776 with dssa
                            pause 
                            scene a7777 with dssa
                            b "You'd have to really take me there... With all your strength... Until I couldn't do anything..."
                            scene a7778 with dssa
                            b "-but press my ass against the hole..."
                            scene a7779 with dssa
                            b "and wait for you to do me through the wall..."
                            scene a7780 with dssa
                            pause  
                            menu:
                                "Then I'd just leave you there for everyone.":
                                    $ Bella_K +=2 
                                    $ Bella_PGU = True  
                                    scene a7781 with vpunch
                                    b "Wow!"
                                    scene a7782 with dssa
                                    d "Perhaps, I can then finally get some studying done."
                                    scene a7783 with dssa
                                    b "Just wow."
                                    scene a7784 with dssa
                                    d "Yep."
                                    scene a7785 with dssa
                                    b "I have my eyes on you." 
                                    scene a7786 with dssa
                                    d "I have my eyes on your boobs."
                                    scene a7787 with dssa
                                    b "Good."
                                "I would tease you until you'd die from a brain aneurysm.":
                                    $ Bella_PGM = True 
                                    scene a7787 with dssr
                                    b "I knew you would kill me."
                                    scene a7788 with dssa
                                    d "I'll keep you alive."
                                    scene a7789 with dssa
                                    b "For your own pleasure?"
                                    scene a7790 with dssa
                                    d "Yes."
                                    scene a7791 with dssa
                                    b "*Innocent* Okay."
                        "I may cuff you to a public toilet.":
                            scene a7792 with dssa
                            b "I don't get it."
                            scene a7793 with dssa
                            d "Imagine being cuffed close to a toilet seat and someone has to go number 2 really bad..."
                            scene a7794 with vpunch
                            b "Ugh!"
                            b "Damn! You're sick!"
                            scene a7795 with dssa
                            d "It would be so disgusting."
                            scene a7796 with dssa
                            b "If that's what you understand under sexual, I may have to rethink this whole endeavour here!"
                        "I'll tease you with gentle touches until you burst.":
                            scene a7787 with dssr
                            b "I know you would... It would kill me."
                            scene a7788 with dssa
                            d "I'll keep you alive."
                            scene a7789 with dssa
                            b "For your own pleasure?"
                            scene a7790 with dssa
                            d "Yes."
                            scene a7791 with dssa
                            b "*Innocent* Okay."
                else:
                    scene a4300 with dssa
                    d "...Well, now I'm not doing that."
                    scene a4301 with dssa
                    pause 
                    scene a4302 with dssa
                    b "*Snarls* Do it."
            else:
                b "Don't you dare ask me to fuck you."
                scene a4303 with dssr
                d "Why would I punish myself?"
                scene a4304 with dssa
                b "Sure."
            scene a4305 with dssa
            d "Perhaps, I'll ask you to make up with Mila."
            scene a4306 with dssa
            b "Maybe I'll ask you to suck a dick."
            scene a4307 with dssa
            b "See! This is how these punishments escalate!"
            scene a4308 with dssa
            d "Yeah, that's why I don't play 'Would you rather' with Nami."
            d "The Cheeto doesn't know when to stop..."
        "Don't do that with Bella.":
            pass 
    if BellaCropTop is True:
        scene a4309 with dssr
        pause
        scene a4310 with dssa 
        pause 
        scene a4311 with dssa
        b "You are officially addicted."
        scene a4312 with dssa
        d "Perhaps."
        scene a4313 with dssr
        pause 
        scene a4314 with dssr
        d "You said you'd like it when I tell you what to do..."
        scene a4315 with dssa
        b "I don't recall."
        scene a4316 with dssa
        pause 
        scene a4317 with dssa
        d "Take off your undershirt."
        scene a4318 with dssa
        b "What?"
        scene a4319 with dssa
        d "This. Take it off." 
        scene a4320 with dssa
        b "Why would I do that?"
        scene BellchenKopfDreh with dssa
        pause 
        scene a4322 with dssa
        pause 
        scene a4323 with dssa
        pause 
        scene a4324 with dssa
        b "Happy?"
        scene a4325 with dssa
        d "Very."
        scene a4326 with dssr
        pause 
        scene a4327 with dssa
        pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene a4328 with dssr
    pause
    if MilaDate is True:
        scene a4329 with dssa
        mi "Well, well, well... Why are you here all by yourself?"
        scene a4330 with dssr
        d "There's too many weirdos around."
        scene a4331 with dssr 
        mi "You're one of them."
        scene a4332 with dssa 
        pause 
        if BellaDate is True:
            scene a4370 with dssr 
            pause
            scene a4371 with dssa 
            ju "Aren't they a cute couple?"
            scene a4372 with dssa 
            pause 
            scene a4373 with dssa 
            b "Who?"
            scene a4374 with dssa 
            "Justine just smiles."
            scene a4375 with dssa 
            ju "Is he good in bed?"
            scene a4376 with dssa 
            b "I wouldn't know." 
            if BellaCropTop is True:
                scene a4377a with dssa
            else:
                scene a4377 with dssa
            ju "Are you a cuckqueen? Is he edging you?"
            if BellaCropTop is True:
                scene a4378a with dssa
            else:
                scene a4378 with dssa
            b "...Certainly feels like it."
            if BellaCropTop is True:
                scene a4379a with dssa
            else:
                scene a4379 with dssa
            ju "Mila has magic powers... You better plant your flag before she does."
            if BellaCropTop is True:
                scene a4378a with dssa
            else:
                scene a4378 with dssa
            b "I know what I'm doing, Justine..."
            if BellaCropTop is True:
                scene a4380a with dssa
            else:
                scene a4380 with dssa
            ju "No, you don't."
            scene a4382 with dssr
            pause 
            scene a4381 with dssa
            ju "You should trick him into a baby."
            if BellaCropTop is True:
                scene a4383a with dssr
            else:
                scene a4383 with dssr 
            ju "Or you know... A relationship."
            if BellaCropTop is True:
                scene a4384a with dssa
            else:
                scene a4384 with dssa
            b "Neither he nor I want one."
            if BellaCropTop is True:
                scene a4385a with dssa
            else:
                scene a4385 with dssa
            ju "Bella... You're a hottie..."
            scene a4386 with dssr
            ju "But there's always a hotter chick..."
            scene a4387 with dssa
            ju "Yet, there's always a hotter guy too..."
            scene a4388 with dssa
            pause 
            scene a4389 with dssa
            b "What are you getting at?"
            scene a4390 with dssa
            pause 
            scene a4391 with dssa
            ju "What?"
            ju "What was I talking about? I spaced out."
            scene a4392 with dssa
            b "Oh my god, go away."
            scene a4393 with dssa
            ju "Your shoulder looks cozy..."
            if BellaCropTop is True:
                scene a4394a with dssa
            else:
                scene a4394 with dssa
            ju "Mhhhh..."
            pause 
            if BellaCropTop is True:
                scene a4395a with dssa
            else:
                scene a4395 with dssa
            ju "I think I was supposed to get something for Ayua... Or Melanie?"
            ju "*Sigh* They all look the same to me..."
            if BellaCropTop is True:
                scene a4396a with dssa
            else:
                scene a4396 with dssa
            b "One's Asian and the other is a blonde caucasian."
            if BellaCropTop is True:
                scene a4397a with dssa
            else:
                scene a4397 with dssa
            pause 
            if BellaCropTop is True:
                scene a4398a with dssa
            else:
                scene a4398 with dssa
            ju "What?" 
            play sound "Music/Sfx/Punch.ogg"
            scene a4399 with vpunch
            b "You're the worst!"
            scene a4400 with dssa
            ju "*Yawns*."
        else:
            scene a4385 with dssr
            ju "Hi."
            scene a4401 with dssr
            pause 
            scene a4402 with dssa
            ju "[name]... you keep staring at him."
            scene a4403 with dssa
            b "No, I was looking at..."
            scene a4404 with dssr
            b "That guy."
            scene a4405 with dssa
            ju "Hmm."
            scene a4407 with dssr
            ju "Heeey... That blonde one over there likes you." 
            scene a4406 with dssr
            pause 
        scene a4333 with dssr
        mi "I swear! The stick I found in that little river not only looked like a gun..."
        mi "If you turned it around it became the perfect golf club!"
        scene a4335 with dssa
        mi "I loved that stick..." 
        scene a4334 with dssa
        pause 
        scene a4336 with dssa
        mi "*Sighs* Man... How many times I've beaten and robbed homeless people with it... That stick was my partner in crime."
        scene a4337 with dssa
        d "What?"
        scene a4338 with dssr
        mi "I'm kidding."
        mi "But you wouldn't believe how the stick and I handled these balls..."
        scene a4339 with dssa
        d "One day you can show me how you handle balls."
        scene a4340 with dssa
        mi "I might just do that."
        scene a4339 with dssa
        d "By the way, Nick is taking us to the Petrova Country Club next week."
        d "You're invited."
        scene a4340 with dssa
        mi "Aaaahhh... I don't know... I still feel like a leech."
        scene a4341 with dssa
        d "Oh, you don't get the choice to decline."
        scene a4342 with dssa
        mi "Whaaat?!"
        scene a4344 with dssa
        d "Yep, you're in this now."
        scene a4345 with dssa
        mi "I feel sooo leechy..."
        scene a4346 with dssa
        d "Welcome to the gold-digger lifestyle."
        scene a4347 with dssa
        mi "Oh noooo."
        scene a4348 with dssr
        mi "I'll be there!"
        scene a4349 with dssr
        mi "Wait, Nick knows I'm coming?"
        scene a4351 with dssa
        d "He specifically requested you."
        scene a4350 with dssa
        mi "Good. I thought it would end up being one of those awkward moments where you suddenly appear with a plus one."
        scene a4352 with dssa
        d "Nah."
        scene a4353 with dssa
        mi "I'll need something nice to wear..."
        scene a4354 with dssa
        d "Something sporty. You'll be playing golf."
        d "If you don't want to shop, we can take a look at your wardrobe."
        scene a4355 with dssr
        mi "I do want to buy a new bikini... So yeah, my budget is reserved for that."
        mi "Perhaps we can go through my wardrobe... together."
        scene a4356 with dssa
        d "Sure."
        scene a4357 with dssr
        pause 
        scene a4358 with dssa
        mi "I'd like to go on a real date with you soon."
        scene a4357 with dssa
        d "We will."
        scene a4358 with dssa
        mi "Nah, you're not reliable in this matter."
        mi "Saturday, you and I are going to have dinner."
        scene a4357 with dssr
        d "Do I have a say in this?"
        scene a4359 with dssa
        mi "Not if you want this here to go on."
        scene a4360 with dssa
        d "Alright. Saturday."
        scene a4362 with dssr
        mi "Ah! What I wanted to ask you..."
        mi "How are these training sessions going? I heard you're meeting up in the evening?"
        scene a4361 with dssa
        d "For a second I thought you meant my training with Zara."
        scene a4363 with dssr
        mi "No, but she told me about the basketball training."
        scene a4364 with dssa
        d "I really gotta go there tonight... I missed Saturday."
        scene a4365 with dssa
        mi "I'll remind you."
        scene a4366 with dssa
        d "Thanks Mila."
        scene a4367 with dssa
        d "I've gotta find Vic."
        scene a4368 with dssa
        mi "She's probably near the yoga club bathroom. The bathroom is out of service and apparently acts as a meetup for girls."
    else:
        pause 
        scene a4367 with dssr
        d "Hey Mila."
        d "Have you seen Vic?"
        scene a4368 with dssa
        mi "I haven't seen her but if I had to guess, I'd assume she's near the Yoga club bathroom."
        mi "It's out of service and acts as a hub for girls."
    scene a4369 with dssr
    d "Thanks. I'll check it out."
    scene black with Dissolve(2)
    with Pause(.5)
    jump SashaArt5x5


label SashaArt5x5:
    scene a713a with dssr
    "Robin starts laughing."
    play sound "Music/Sfx/Punch.ogg"
    scene a714a with vpunch
    sas "Stop laughing!"
    scene a715a with vpunch
    rob "Auu!"
    scene a717a with dssa
    rob "Why always my shoulder?!"
    scene a716a with dssa
    pause
    scene a718a with dssa
    "Robin starts laughing again."
    scene a719a with dssr
    ka "Are your nipples sensitive? Does it hurt?"
    scene a4408 with dssr
    sas "They are a little swollen and sensitive because of all the rubbing... But besides said irritation, it doesn't feel any different than usual."
    scene a4409 with dssa
    ka "How long did you keep them on?"
    scene a4410 with dssa
    sas "...I might've slept in with them."
    scene a4411 with dssa
    ka "Even if you did, it should vanish after a few days..."
    scene a4412 with dssa
    sas "Maybe it was a faulty product."
    scene a720a with dssr
    ka "Are you trying to blame me?"
    scene a4413 with dssr
    sas "Perhaps."
    "Before Karen can answer, Sasha cuts her off."
    scene a4414 with dssa
    sas "How do I get it off?"
    scene a4415 with dssa
    mia "We tried soap, nail polish remover and rubbing it like crazy but it was no use."
    scene a7975 with dssr #brush sound 
    pause 
    scene a7976 with dssa
    sas "*Muffled* This hurts..."
    scene a7977 with vpunch
    mia "OH MY GOD! Your nipple came off!"
    scene a7978 with dssa
    pause 
    scene a7979 with dssa
    mia "...It uhh- was just a piece of the sponge..."
    scene a7980 with dssa
    pause 
    scene a4416 with dssr
    mia "Her nipple will come off before the sticker."
    scene a4418 with dssa
    ka "I should have some cleaning mixture that might work."
    scene a4419 with dssr
    sas "I'm not putting anything on my breasts that is used to remove paint from a canvas."
    scene a4420 with dssa
    ka "Then I can't help you."
    scene a4419 with dssa
    sas "I can't wear a bikini without it being visible!"
    scene a4420 with dssa
    ka "I don't know what to tell you, Sasha. Wear a bikini that covers more. It's going to come off... But it might take a while."
    scene a4421 with dssa
    ka "Use pasties or cover it up with makeup for the time being."
    sas "*Sigh*."
    scene a4422 with dssr
    mia "It looks cute."
    mia "You might be setting a new trend."
    scene a4423 with dssr
    rob "I like it."
    scene a4424 with dssr
    sas "Karen."
    sas "You've got my message about the Free The Boobs movement?"
    scene a4425 with dssa
    ka "I'm not sure what you want me to do."
    scene a4426 with dssa
    sas "To take down the photos of every model that they have artificially enhanced."
    u "What did they do?"
    scene a4427 with dssr
    sas "They enhanced our boobs in post production."
    scene a4428 with dssa
    u "Oh. I knew something was off with Adri's image."
    scene a4429 with dssr
    ka "I'll tell Joyce."
    scene a4430 with dssa
    sas "I told her myself, but she dismissed me. I want you to tell her that they must use the real ones or she can go looking for a new college."
    scene a4431 with dssa
    ka "Threaten her yourself. The FTB movement is managed by students. I have better things to do."
    scene a4432 with dssr
    ka "You should speak to Maja Frohn. She was one of the FTB creators and can vote Joyce out at any time."
    scene a4433 with dssa
    sas "Where do I find her?"
    scene a4434 with dssr
    rob "It's Victoria's big sister. Victoria being the cutie in the wheelchair."
    scene a4435 with dssr
    ka "Talk to Maja. Maybe she'll take care of it for you."
    ka "I heard she's coming back to ZPR to assist the coaches of the basketball team."
    stop music fadeout 3
    scene black with Dissolve(1)
    with Pause(.5)
    stop ambient
    jump VictoriaTherapy5x5

label VictoriaTherapy5x5:
    $ play_playlist(playlist_Smooth2)
    scene a4556 with dssb
    pause
    scene a4557 with dssa
    d "(I hope that's the restroom...)"
    scene a4558 with dssa 
    pause 
    scene a4559 with dssr 
    n "And I need all these colors? Can't I just buy black folders?"
    scene a4560 with dssa 
    u "No, if you want me to help you with math, you'll buy all the utensils in the appropriate color."
    scene a4561 with dssa 
    n "I don't want you to help me. You were assigned to me."
    scene a4562 with dssr 
    u "Maybe if you hadn't tried to bribe the guy to do everything for you, you wouldn't be stuck with me."
    scene a4563 with dssa 
    n "How should I have know that he was asexual? My charms were nullified by his spell resistance."
    n "And that hippie didn't want the fifty bucks either..."
    scene a4564 with dssa 
    u "I'll see you the day after tomorrow with the right binders."
    scene a4565 with dssr 
    pause 
    scene a4566 with dssr
    d "Yo."
    d "Is Vic in there?"
    scene a4567 with dssa
    n "Yeah..."
    scene a4568 with dssr
    pause
    scene a4569 with dssa
    d "And yes, I will make fun of you later for needing help with math."
    if RaceWithImpossibleOdds is True:
        scene a4570 with dssr
        d "Why didn't you just ask me for help?"
        scene a4571 with dssa
        n "I can't let you know I'm dumb! I have a reputation of being the alpha!"
        scene a4572 with dssa
        d "You have never been the alpha."
        scene a4573 with dssa
        n "We'll see about that... later... today... in your bed..."
        scene a4574 with dssa
        d "Maybe you should've taken some of the math tests in high school yourself."
        scene a4575 with dssa
        n "Maybe you should mind your own business before I stab you."
        scene a4576 with dssa
        n "*Mumbles* Yeah, you better run."
    scene a4436 with dssr 
    pause
    scene a4437 with dssr
    pause
    if ZaraBBallTrust5x0 is True:
        scene a4438 with dssr 
        pause 
        scene a4439 with dssr 
        pause
    else:
        scene a4440 with dssr 
        pause
    scene a4441 with dssr 
    v "I'll be with you in a minute, [name]!"
    scene a4442 with dssa 
    d "All good. I'll still have to pick up a book from the library. I just wanted to check on you."
    scene a4443 with dssa 
    d "See when you wanted to leave."
    scene a4444 with dssa 
    v "Maja will pick us up in like twenty minutes."
    scene a4445 with dssr
    d "(Not a bad ride.)"
    if RaceWithImpossibleOdds is True:
        $ NamiDate = True
        scene a4446 with dssr
        n "Remember when you and Summer pushed me off the tree and I almost broke my back?"
        scene a4447 with dssr
        pause 
        scene a4448 with dssa
        n "Okay, maybe I pushed you and Summer off the tree... but those are minor details!"
        scene a4449 with vpunch #sfx
        pause
        scene a4450 with dssr
        pause 
        scene a4451 with dssa
        n "Right now everyone in this room still thinks this is just fun."
        n "But the moment I kiss you, none of the girls here will touch you again."
        menu:
            "Kiss the Cheeto.":
                stop music fadeout 5
                $ Cheeto_Love = True 
                scene a4452 with dssa
                pause 
                show screen Extra_Lewd_CH1_Nami_2
                scene a4453 with dssr
                pause 
                hide screen Extra_Lewd_CH1_Nami_2
                scene a4455 with dssa
                pause
                scene a4456 with dssa
                n "Good choice."
                scene a4457 with dssa
                pause
                if BellaDate is True:
                    scene a4458 with dssr 
                    d "What?"
                    scene a4459 with dssa
                    na "Bella is the only one you're allowed to kiss!"
                    scene a4460 with dssa
                    n "Hell no! His mouth is mine! And I'll put in it whatever I want!"
                    play sound "Music/Sfx/Slap.ogg"
                    scene a4461 with vpunch
                    pause
                else:
                    scene a4465 with dssa
                    na "Since when?"
                    scene a4466 with dssa
                    n "Recently."
                scene a4462 with dssa
                $ play_playlist(playlist_Smooth)
                n "Let's go grandpa... Time for your medicine."
                scene a4463 with dssr
                pause 
                scene a4464 with dssa
                pause   
                scene a4512 with dssr
                pause 
                n "You know what's going to happen now..."
                scene a4513 with dssa
                d "I really don't... but I'm afraid."
                scene a4514 with dssr 
                pause 
                scene a4515 with vpunch 
                pause  
                scene a4516 with dssr 
                pause 
                scene a4517 with dssr 
                pause 
                scene a4518 with dssa 
                pause 
                scene a4519 with dssa 
                "You grab her big, tender ass."
                scene a4520 with dssa 
                "She lets out a little moan..." 
                scene a4521 with dssr
                "While slowly fingering herself."
                scene a4522 with dssa
                pause 
                #ani
                scene a4523 with dssr
                pause 
                scene a4524 with dssr
                pause 
                scene a4525 with dssr
                pause 
                scene a4526 with dssa
                d "Wait..."
                scene a4527 with dssr
                d "Let's continue this somewhere else... Not here."
                scene a4528 with dssr
                n "Man, you always find an excuse."
                scene a4529 with dssa
                d "(I would really hate a panic attack in public.)"
                d "Let's go on a date or something like that. There we can do whatever."
                scene a4530 with dssa
                n "*Sigh* This place is as romantic as it can get!"
                scene a4531 with dssa
                pause 
                scene a4532 with dssa
                d "Can I make up for it by giving your butt a kiss?"
                scene a4533 with dssr
                pause 
                scene a4534 with dssa
                n "No. But it's a beginning."
                scene NamiButtWiggleCH1 with dssa
                with Pause(9) 
                scene a4535 with dssr
                pause 
                scene a4536 with dssa
                pause 
                scene a4537 with dssa
                pause 
                scene a4538 with dssa
                d "(...No, that's not it... This isn't the feeling of impending doom... I think I'm imagining it with the Cheeto.)"
                menu:
                    "Bury your head between her cheeks.":
                        play sound "Music/Sfx/Whisper1.ogg"
                        $ Whispers +=1 
                        $ CheetoBuryAssLicking = True 
                        scene a4539 with dssr
                        pause 
                        scene a4540 with dssr 
                        pause  
                        scene a4541 with dssa 
                        n "...You gotta do more than that to get back in my graces."
                        scene a4542 with dssr 
                        n "*Quiet* Oh- fuck yes..."
                        scene a4543 with dssr 
                        pause 
                        scene a4544 with dssa 
                        d "I've gotta go get to the library"
                        scene a4545 with dssr 
                        d "But... I'm serious about this." 
                        scene a4546 with dssr 
                        n "I don't want to push, you know."
                        n "When I say the things I say, I don't really mean it. I'm just venting to myself."
                        scene a4547 with dssa 
                        d "You do mean it. You just don't mean to hurt me." 
                        scene a4548 with dssa 
                        n "We'll roll this up later." 
                        scene a4549 with dssa 
                        d "...I'm sure we will."
                    "Don't risk it.":
                        d "(I can't risk it...)"
                        scene a4548 with dssa 
                        n "We'll roll this up later." 
                        scene a4549 with dssa 
                        d "...I'm sure we will."
            "Don't.":
                scene a4551 with dssa 
                n "..."
                scene a4552 with dssa
                n "I'll remember this."
                scene a4553 with dssa
                d "It's about principle."
                d "I'll kiss you when I want to, not when you dare me to."     
                scene a4554 with dssa
                pause 
                scene a4555 with dssa
                "You sigh." 
    if KateNE_S1_1 is True:
        scene a4445 with dssr
        pause 
        play sound "Music/Sfx/Punch.ogg"
        scene a4467 with vpunch
        "Kate flops onto your lap."
        "You try to lift her up but it ends up only raising her legs."
        scene a4468 with dssa
        kat "Is this how you like it?"
        scene a4469 with dssr
        pause
        if BellaCropTop is True:
            scene a4470 with vpunch
            "She flops off you."
            scene a4471 with dssr
            pause 
            scene a4472 with dssr
            pause 
            scene a4473 with vpunch
            kat "I saw Bella took off her bra."
            d "Mhm."
            scene a4474 with dssr
            kate "You must have a serious grip on her pussy." 
            scene a4475 with dssa
            pause 
            scene a4476 with dssa
            kat "I'll help you with Nami."
            scene a4477 with dssr 
            kat "How did it happen? Did you hide Bella's bra?"
            scene a4478 with dssa
            d "No, I just asked her."
            scene a4477 with dssa
            kat "And she did that?"
            d "Mh."
            scene a4479 with dssa
            kat "She is a little sub... I knew it."
            scene a4480 with dssa
            d "Maybe she was just doing me a favor."
            scene a4479 with dssa
            kat "I like the sub story better."
            scene a4481 with dssr
            pause 
            menu:
                "I do wonder what else she'd be up too.":
                    scene a4482 with dssr
                    kat "...We can find out."
                    scene a4483 with dssa
                    d "We?" 
                    scene a4484 with dssa
                    kate "I'm going to be totally straight with you..."
                    kate "I can't stand Bella at all..."
                    kate "She acts all high and mighty but I'm sure she's a closet slut."
                    scene a4485 with dssr
                    d "Be careful with your words."
                    scene a4486 with dssa
                    kate "Not her boyfriend, huh?"
                    scene a4487 with dssa
                    d "I won't let you disrespect her."
                    scene a4486 with dssa
                    kate "As I was saying... I can't stand Bella at all..."
                    scene a4489 with dssa
                    kate "But I'd love if she ate me out... Her lips on my clit, her tongue in my pussy, and my juices covering her face."
                    scene a4490 with dssa
                    "You furrow your brows."
                    scene a4489 with dssa
                    kate "All I'm saying is... We could have some fun with her..."
                    scene a4490 with dssa
                    menu:
                        "It sounds kinda hot.":
                            $ Kate_Bella = True 
                            scene a4491 with dssa
                            kate "Oh- seriously?"
                            scene a4492 with dssa
                            kate "I totally didn't expect you to say that."
                            scene a4493 with dssa
                            d "I like Bella, and I'll tell you right now that I won't let you hurt her."
                            scene a4494 with dssr
                            kate "I'm not talking about hurting her..."
                            scene a4495 with dssa
                            kate "Quite the opposite."
                            scene a4496 with dssa
                            d "And if she's going to 'eat you out', it must be because she wants to. Not through some trickery."
                            scene a4497 with dssa
                            kate "If she is the way I think she is, she will."
                            kate "Are you going to be at the bar opening tomorrow?"
                            scene a4498 with dssa
                            d "Yeah."
                            scene a4499 with dssa
                            kate "I'm sure we can have some fun with her there..." 
                            scene a4498 with dssa
                            d "Think of something."
                            scene a4499 with dssa
                            kate "*Chuckles* I will."
                            scene a4500 with dssr
                            menu:
                                "Kiss her tiddy.":
                                    scene a4501 with dssr
                                    $ Cheating +=2
                                    $ KateTrust = True 
                                    $ KateTiddyKiss = True 
                                    pause 
                                    scene a4502 with dssa
                                    "You suck on her little, hard nipple" 
                                    scene a4503 with dssr
                                    kate "Whose tits are bigger? Mine or hers?"
                                    scene a4504 with dssa
                                    pause 
                                    scene a4505 with dssa
                                    d "Maybe yours are a bit bigger."
                                "Don't do it because of Bella.":
                                    scene a4506 with dssr
                                    d "(I have a tiny urge to touch her boob... But I don't want to do that to Bella.)"
                        "Disagree.":
                            $ KateWTEBO = True 
                            scene a4507 with dssa
                            kate "It was worth a shot."
                "Change the topic.":
                    scene a4508 with dssr
                    d "Well, it was fun but I need to go to the library."
            scene black with Dissolve(2)
            with Pause(.5) 
        else: 
            scene a4509 with dssr
            pause 
            scene a4510 with dssr
            pause 
            scene a4511 with vpunch
            kate "Rude!"
    scene a4577 with dssr 
    u "Like- why does she do that? Why does she chuckle when she corrects us? She treats the guys totally normal."
    u "How can a professor be down that bad? A real pick-me girl."
    scene a4579 with dssr 
    pause 
    scene a4580 with dssa 
    if RobinOffHook5x0 and RoRum is True:
        rob "Did you see the paper?"
        scene a4581 with dssa 
        d "Yeah."
        scene a4582 with dssa 
        pause
        scene a4584 with dssa 
        rob "That woman stalked us. How creepy!"
        scene a4583 with dssa 
        d "I'm not sure if we were her target."
        d "I think we were at the wrong place at the wrong time."
        scene a4585 with dssa 
        rob "...Doing the wrong things."
        scene a4586 with dssa 
        d "We weren't doing anything."
        scene a4587 with dssa 
        rob "I'm joking." 
        scene a4588 with dssr 
        d "Will you sue her?"
        scene a4589 with dssa
        rob "No."
        scene a4590 with dssa
        rob "Usually it's Sasha who makes the cover... I'll take what I can get."
        scene a4591 with dssa
        pause 
        scene a4592 with dssa
        rob "It's not what they wrote about me that bothers me so..."
        rob "But from where did they get the frontpage pictures?"
        scene a4593 with dssr
        rob "I've only ever sent them in a groupchat of people I absolutely trust."
        rob "Someone sold me out... Or messed up."
        scene a4594 with dssa
        d "It was definitely Sasha."
        scene a4595 with dssa
        rob "No... She'd tell me right away if she messed up." 
        rob "And she'd never hurt me on purp-"
        scene a4596 with dssa
        rob "...Never mind, she hurts me all the time."
        scene a4597 with dssa
        d "Have you told her about your suspicions?"
        scene a4598 with dssa
        rob "First thing."
        scene a4599 with dssa
        rob "...I'll find out who leaked it. They didn't just betray my trust."
        rob "But everyone's trust in the groupchat."
        scene a4597 with dssa
        d "If you see Bella, please tell her I'm picking up some books from the library."
    elif RoRum is True:
        rob "Did you see the paper?"
        scene a4581 with dssa 
        d "Yeah."
        scene a4582 with dssa 
        pause
        scene a4584 with dssa 
        rob "That woman stalked us. How creepy!"
        scene a4583 with dssa 
        d "I'm not sure if we were her target."
        d "I think we were at the wrong place at the wrong time."
        scene a4595 with dssr
        rob "So it seems..."
        scene a4594 with dssa
        d "If you see Bella, could you tell her I'm picking up some books from the library?"
        scene a4596 with dssa
        rob "Sure."
    else:
        scene a4594 with dssr
        d "Ah. Robin. If you see Bella, could you tell her I'm picking up some books from the library?"
        scene a4596 with dssa
        rob "Sure."
        
    stop music fadeout 5
    scene black with Dissolve(2)
    with Pause(.5)
    jump CollegeCH1End
    

label CollegeCH1End:
    $ play_playlist(playlist_LK)
    scene a702 with dssb
    pause
    scene a703 with dssa
    d "(There's gotta be a book about fungoids...)"
    scene a704 with dssa
    d "Hi Sonya."
    scene a705 with dssr
    d "You haven't by any chance seen a book about fungoids?"
    scene a706 with dssa
    son "-No."
    scene a707 with dssr
    d "You're okay?"
    scene a708 with dssa
    son "Oh. Yes. I'm just exhausted and a little hot."
    scene a707 with dssa
    d "I heard you sparred with Ayua. I didn't take you for a fighter."
    "She smiles sheepishly but doesn't say anything."
    scene a709 with dssr
    d "Well, I see you."
    scene a710 with dssa
    pause
    scene a711 with dssa
    kate "Oh? What are you looking at, Sonya?"
    scene a712 with dssa
    kate "Do you like [name]?"
    scene a773 with dssa
    son "He's nice. And the only guy that really talks to me."
    if NiaUnderwearS2_CH1 is True:
        scene a774 with dssa
    else:
        scene a774a with dssa
    nia "I think the others are just careful... They probably want to respect your cultural background."
    scene a775 with dssr
    son "It makes me feel out of place."
    scene a776 with dssa
    nia "You do look out of place."
    scene a777 with dssa
    kat "What Nia means is that they're just careful. Don't worry."
    scene a778 with dssa
    kat "College guys are ruled by hormones and seeing you in all your clothes and well, your cultural background, tells them that they're not getting laid tonight."
    scene a779 with dssa
    kat "...If we ignore your translucent sweater and half visible tits."
    kat "*Mumbles* Damn, do you have tits..."
    scene a780 with dssa
    son "Oh."
    scene a781 with dssa
    son "...Didn't seem to be helping either."
    scene a782 with dssa
    "Nia and Kate laugh."
    scene a783 with dssr
    kat "We should take you shopping."
    scene a784 with dssa
    son "I just got these clothes from friends of my family. The only clothes I brought with me are my hoods, which my Mother made for me, and a reinforced bra."
    son "I don't want to pretend to be someone else. I'm not religious, quite the opposite even but..."
    scene a785 with dssa
    son "My hoods are a part of my identity."
    scene a786 with dssa
    kat "We wouldn't dress you in anything you're not."
    scene a787 with dssa
    kat "But shopping can help finding yourself. You see yourself in different outfits... And each one portrays a different personality."
    play sound "Music/Sfx/Punch.ogg"
    scene a788 with vpunch #sfx
    kat "Like, you can keep the hood but what about a top more suited to the current climate? Preferably something in your size that doesn't go translucent from being stretched."
    kat "And you really need some panties that... well, don't send the wrong message..."
    scene a789 with dssa
    son "Ayua was giggling when she gave me that underwear..."
    son "I don't have my own money to buy anything myself. I can't."
    scene a790 with dssa
    nia "You don't have your own money?"
    son "I get like $20 a week."
    scene a791 with dssa
    nia "That seals it! I'll pay for your clothes and the smoothie afterward!"
    scene a792 with dssa
    son "Thank you."
    scene a793 with dssa
    kat "We should find Nami and ask if she wants to join us too."
    scene a794 with dssr
    nia "I think she headed towards the girl dorms."
    scene a795 with dssr
    kat "Yeaaah, I can't go there for another month. I'm banned from the dorms."
    scene a796 with dssa
    nia "Why?"
    scene a797 with dssa
    kat "...Indecent behavior."
    scene a798 with dssr
    kat "But... Let's try to get in anyways!"
    scene a799 with dssa
    pause
    scene a872 with dssr
    pause
    scene a873 with dssa
    pause
    scene a874 with dssa
    son "I'll be there in a minute."
    kat "We'll wait for you at the dorms."
    scene a875 with dssr
    son "Hello."
    scene a876 with dssa
    d "Hey Sonya."
    scene a877 with dssa
    son "Say, did Nadia ever mention when we are going to play again?"
    scene a878 with dssa
    d "No, she hasn't said anything yet."
    d "I can ask her when I see her."
    scene a879 with dssa
    son "Okay."
    scene a880 with dssr
    d "(Her voice changed by an octave... It's more assertive than what she used to sound like.)"
    d "(I have some serious trouble reading her. She used to avoid eye contact but now she looks into my eyes without any sign of discomfort.)"
    scene a881 with dssa
    d "You changed."
    scene a882 with dssa
    son "Did I?"
    scene a1257a with dssr
    d "I'm not sure. It could be a subconscious move towards integration with the rest of the girls. Or you have become comfortable, therefore revealing more of yourself."
    scene a1258 with dssa
    son "You mean my breasts?"
    scene a1259 with dssr
    d "What?"
    scene a1260 with dssa
    son "My top seems to be too tight and they're slightly visible... I was wondering if you were trying to make a joke about it."
    scene a1261 with dssa
    d "Ah, no... But now that you mention it, I see the resemblance."
    d "But no. I actually meant your personality."
    d "(She talks a little bit too casual about her breasts...)"
    scene a1262 with dssa
    son "I think... I think I'm warming up, yes."
    scene a1263 with dssr
    d "You speak the language very well. For how long have you been here?"
    scene a1264 with dssa
    son "I've been here for a month."
    scene a1263 with dssa
    d "But you didn't learn the language in a month?"
    scene a1264 with dssa
    son "No. I was raised bilingual."
    son "I speak Farsi, Arabic and English."
    scene a1265 with dssa
    son "But... I apologize, I don't like to speak about my past."
    scene a1266 with dssa
    son "I wanted to ask you if you'd like to visit a museum together."
    scene a1267 with dssa
    d "(I didn't see that coming.)"
    d "To a museum?"
    scene a1266 with dssa
    son "Yes. I've seen that my student ID allows me to enter some venues for free."
    son "There's a museum for firearms and they have an exhibition this week and I'd like to go there. Do you want to come with me?"
    scene a1268 with dssr
    d "*Chuckles* Firearms?"
    scene a1269 with dssa
    son "Yes."
    scene a1268 with dssa
    d "(She says it as if its the most casual thing in the world.)"
    menu:
        "Yeah. I'd like to.":
            $ SonyaFireArmMuseum = True
            scene a1269 with dssa
            son "Would you like to go after class?"
            scene a1270 with dssa
            d "Oh, I have promised Victoria I'd be with her during her first physical therapy session."
            scene a1272 with dssa
            son "I understand. How about after the session?"
            scene a1271 with dssa
            d "(You can't keep her on a hook for long, that's for sure.)"
            scene a1273 with dssa
            son "No, wait. I have to be somewhere in the evening."
            scene a1274 with dssa
            son "What about tomorrow?"
            scene a1275 with dssa
            d "There's the bar opening."
            d "How about Friday?"
            scene a1274 with dssr
            son "It would be the last day of the exhibition. Yes... Yes, that works."
            son "They have a competition that day. Perhaps they will let us join."
            scene a1276 with dssa
            son "Where do you want to meet?"
            scene a1275 with dssa
            d "How about we meet here at the campus? After class?"
            scene a1276 with dssa
            son "Yes. We'll talk about it on Friday."
            scene a1277 with dssa
            d "Sounds good."
            scene a1278 with dssa
            pause
            scene a1279 with dssa
            d "(Most people I meet I can read easily... Maybe I'm not as good a people-reader as I think I am... Or she's wearing different masks.)"
            scene a1280 with dssa
            d "(I'm intrigued to find out more.)"
            scene a1281 with dssr
            kate "Oh, I think you messed up."
        "I'm sorry. I don't want to.":
            $ SonyaKorb = True
            scene a1282 with dssa
            d "I really appreciate you asking, but I don't think I'm the right person for this."
            scene a1282 with dssa
            son "Okay. No problem."
            scene a1283 with dssa
            pause
            scene a1280 with dssa
            d "(I can read most people I meet easily. Maybe I'm not as good a people-reader as I think I am... Or she's wearing different masks.)"
            d "(Back to the fungus.)"
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Girly2)
    scene a4600 with dssb
    pause 
    scene a4601 with dssa 
    pause 
    scene a4602 with dssr
    u "My legs are sore!"
    scene a4603 with dssr
    maxi "My hair is sore..."
    scene a4604 with dssr
    n "You weren't kidding about your wardrobe, Max."
    scene a4611 with dssr
    maxi "So what do you say, Nami?"
    scene a4612 with dssa
    "Nami puffs out some air."
    scene a4605 with dssr
    n "Well... Most of it is... cute!"
    scene a4606 with dssa
    maxi "Be honest, it's a little dorky, right?"
    scene a4605 with dssa
    n "Aaaah- yeah. It's a little dorky."
    scene a4606 with dssa
    maxi "That's so mean."
    scene a4607 with dssa
    n "We can fix this."
    scene a4608 with dssa
    pause
    scene a4609 with dssa 
    pause 
    scene NamiSchere with dssa
    pause
    play sound "Music/Sfx/Scissor.ogg"
    scene black with Dissolve(2)
    with Pause(.5)
    scene a4613 with dssr
    pause 
    scene a4614 with dssa
    n "Yep! I'm done!"
    scene a4615 with dssr
    pause 
    scene a4616 with dssa
    n "Now you look like you don't give a damn! That's what the boys like!"
    n "They think you're an easy one, little do they know!"
    scene a4617 with dssa
    maxi "You're a wizard, Nami."
    scene a4618 with dssa
    n "I'm still waiting for that letter, yo!"
    scene a4619 with dssa
    n "So, how's life in the dorms?"
    scene a4620 with dssr
    u "It's often loud."
    scene a4621 with dssa
    n "And no boys, huh?"
    scene a4620 with dssa
    u "Imagine how loud it would be with them... But they sneak in."
    scene a4622 with dssa
    u "We've heard people 'do it' before."
    scene a4623 with dssr
    maxi "The boys dorm is the building across from here."
    scene a4624 with dssa
    maxi "We've heard you can bribe the security with worn panties to get into either dorm at night."
    scene a4625 with dssr
    u "Where do you live?"
    scene a4628 with dssr
    n "I'll soon move into a student house with some of my friends... Ya know, those boxes that house four students."
    scene a4627 with dssa
    maxi "I didn't know you were loaded by the way you talked?"
    scene a4628 with dssr
    n "Not at all."
    scene a4626 with dssr
    u "Then you must know someone who is because they're usually always sold out before the year starts."
    scene a4628 with dssa
    n "I'm pretty sure the one who got us the opportunity isn't loaded... Well, except for her boobs..."
    scene a4629 with dssa
    n "Man, does she have boobs..."
    "The girls chuckle."
    scene a4630 with dssr
    n "Come on! Let's go sit somewhere in the sun!" 
    scene a4631 with dssr
    maxi "Soooooounds good!" 
    scene a4632 with dssa
    n "Yo! How did that get in there?"
    scene a4633 with dssa
    u "*Chuckles* I'll show it to you in a book sometime."
    scene black with Dissolve(1)
    with Pause(.5)
    scene a4634 with dssr
    n "I'll introduce you to some of my other friends."
    scene a4635 with dssa
    pause 
    scene a4636 with dssr
    pause
    scene a4637 with dssr
    na "Adam."
    scene a4638 with dssa
    adam "You will get me expelled!"
    scene a4639 with dssa
    b "He's right, Nadia."
    b "Let it go."
    scene a4649 with dssr
    na "I need them."
    scene a4640 with dssr
    adam "Can't you just buy them?"
    scene a4642 with dssa
    na "They don't sell them. They're the only available ones with HD night vision."
    scene a4641 with dssa
    adam "I'm sorry, I'm already on some kind of probation! If they connect me to what you're planning, I'll spend my life serving cheese fries."
    scene a4643 with dssa
    b "There's worse fates than that."
    scene a4644 with dssr
    adam "I'm not like Bella who has her Mother's influence to keep her from being expelled."
    scene a4645 with dssa
    na "Neither do I."
    scene a4646 with dssr
    adam "I'm also not a hot girl that could make a living on Venus if everything else goes to shit."
    scene a4647 with dssr
    adam "I will keep it to myself, of course. But that's too much to ask, Nadia."
    scene a4650 with dssr
    na "I'll get you a date with Janine."
    scene a4651 with dssa
    adam "I'll do it for a date with Sasha Petrova."
    scene a4652 with dssa
    na "Sure, what else? A threesome with Bella and Mila?"
    scene a4648 with dssr
    adam "*Sigh* I will not go in, and instead stand watch... outside, in a car... Far away."
    b "Don't do it, Adam."
    scene a4653 with dssr
    na "Shut up."
    scene a4654 with dssa
    na "Thank you."
    scene a4655 with dssa
    adam "The date with Janine."
    scene a4656 with dssa
    na "I'll get it."
    scene a4657 with dssr
    "Nadia tipples away with a big smile on her face."
    scene a4658 with dssa
    adam "How's she not in prison yet?"
    scene a4659 with dssa
    b "Puppy eyes, big boobs... and most importantly... she doesn't get caught."
    scene a4660 with dssa
    b "Later."
    scene black with Dissolve(2)
    with Pause(.5)
    scene a4662 with dssb
    pause
    scene a4661 with dssr
    pause 
    scene a4663 with dssr
    n "What about parties? In high school they said the parties at ZPR were legendary."
    scene a4666 with dssr
    kate "The bar is opening tomorrow. So we'll have a party there."
    scene a4663 with dssr
    n "I got invited to Nancy's barn party."
    scene a4666 with dssr
    kate "That's neat. I don't know who Nancy is, though."
    scene a4675 with dssr
    u "Usually, they throw a few good dorm parties a few weeks after the start of a new semester." 
    scene a4667 with dssr
    kate "I know the frat INA is throwing a party soon..."
    scene a4664 with dssr
    n "Who's that?"
    scene a4668 with dssr
    kate "Immodicae Nugae Amatoriae... Or short: INA. They're responsible for some of the biggest parties on the campus."
    kate "The sorority is girls only."
    scene a4669 with dssa
    maxi "What do you need to join the frat?"
    scene a4670 with dssr
    kate "You need to be hot and reliable." 
    scene a4665 with dssr
    n "Hmm... What about the parties of the other colleges? Like MOR?"
    scene a4671 with dssa
    kate "You want to crash their party?"
    scene a4672 with dssr
    n "I'm just asking because we were invited."
    scene a4673 with dssa
    kate "I'd advice against it... The guys won't have a problem with it, but the MOR bitches will not like us there." 
    scene a4674 with dssa
    kate "But Nami, you'll be sick of parties before the first year ends." 
    scene a4676 with dssr
    d "Cheeto, I'll be back later."
    scene a4677 with dssa
    n "Yo! See ya then."
    scene a4678 with dssr
    pause 
    scene a4679 with vpunch
    d "You're a jumpscare, you know that?"
    scene a4680 with dssa
    b "You're about to leave with Vic?"
    scene a4681 with dssa
    d "Yeah."
    scene a4682 with dssr
    b "Come by my place afterward if it's not too late."
    scene a4683 with dssa
    d "Maybe."
    scene a4684 with vpunch
    b "No maybe!"
    b "We'll need to get some work done, dude!"
    scene a4685 with dssa
    d "Maybe."
    if BellaCropTop is True:
        scene a4686 with dssr
        d "You put the undershirt back on."
        scene a4687 with dssa
        b "You weren't there to see it."
        d "Next time I'll keep it with me."  
        scene a4688 with dssa
        b "*Whisper* You'll have to rip it off my toned body."
        scene a4689 with dssa
        d "I will."
        scene a4690 with dssr
        pause 
        scene a4691 with dssa
        pause 
        scene a4692 with dssa
        pause  
    elif BellaDate is True:
        scene a4693 with dssr
        pause 
        scene a4694 with dssa
        pause 
        scene a4692 with dssr
        pause   
    scene a4695 with dssb
    n "Ugh, Bella."
    scene a4696 with dssa
    nia "She's really nice to me."
    scene a4697 with dssa
    n "We should stab her."
    play sound "Music/Sfx/Punch.ogg"
    scene a4698 with hpunch
    nia "*Chuckle* Noooo!"
    scene a4699 with dssr
    pause 
    scene a4712a with dssr
    na "Hi."
    scene a4713 with dssa
    nia "Hello."
    scene a4700 with dssr
    n "Yo Nadia? Are we gonna play today?"
    scene a4712b with dssr
    na "Sure."
    na "As long as Nia remembers to take a poisoned weapon to TOB!"
    scene a4701 with dssa
    nia "Nami was supposed to remind me!"
    scene a4702 with dssa
    n "I've checked your inventory twice... and you banked it again."
    scene a4703 with dssa
    nia "Not on purpose!"
    scene a4705 with dssa
    na "Has anyone seen Bella?"
    scene a4704 with dssa
    nia "She was just here with [name]."
    scene a4705 with dssa
    na "Cute."
    scene a4714 with dssr
    n "Cute?"
    n "You should've seen them... Whatever there was is pretty much over..."
    scene a4715 with dssa
    n "I'd be surprised if they're still project partners by Friday." 
    n "Here's how it went..."
    scene a4717 with vpunch
    b "*Screech* We need to study!"
    scene a4718 with dssa
    d "I'd rather not study with you."
    play sound "Music/Sfx/Punch.ogg"
    scene a4719 with vpunch
    b "*Screech* W-why don't you like me the way I like you?!"
    scene a4720 with dssa
    d "You're like a 1 here... There's some..."
    scene a4709 with dssr
    d "-others who are much more attractive than you."
    scene a4749 with dssr
    nia "I don't remember your boobs being out."
    scene a4750 with dssa
    n "You should've paid more attention."
    scene a4751 with dssa
    n "Where was I..."
    scene a4709 with dssr
    d "-others who are much more attractive than you. So much MORE attractive, I can't even put it into words."
    scene a4720 with dssr
    d "Now please leave and go back to the hole you came from."
    scene a4710 with dssr
    d "I have to handle that 10's body."
    scene a4711 with dssa
    n "Yeah, you do..." 
    scene a4706 with vpunch
    nia "Whaaaat? That's not how it went, Nami!"
    scene a4707 with dssa
    n "It totally was!"
    scene a4708 with dssa
    nia "Nadia, here's how it really went..."
    scene a4721 with dssr
    pause 
    scene a4722 with dssa
    d "Oh yeah? Say it again."
    scene a4723 with dssa
    b "I'll pull down your pants..."
    scene a4724 with dssa
    d "And then?"
    scene a4723 with dssa
    b "Lick along your entire length..."
    scene a4724 with dssa
    d "Ohhh really? Is that it?"
    scene a4725 with dssr
    b "...No."
    scene a4726 with dssr
    b "I'll take him entirely into my mouth..."
    scene a4727 with dssa
    d "Mhmmm..."
    scene a4728 with dssa
    b "But... you know what I thought about?"
    scene a4727 with dssa
    d "Mh?"
    scene a4728 with dssa
    b "Because of all the hot, steamy sex we have... I thought we could, you know... spice it up a little..."
    scene a4729 with dssa
    d "I'm all ears..."
    scene a4730 with dssa
    b "Maybe we'll invite someone else in..."
    scene a4731 with dssr
    pause
    scene a4732 with dssr
    d "Oh yeaaah... Like whom?"
    scene a4733 with dssa
    pause 
    scene a4735 with dssr
    pause 
    scene a4745 with vpunch
    n "Your boobs weren't out!"
    scene a4746 with dssa
    nia "It seems like YOU should've paid more attention!"
    scene a4747 with dssr
    nia "*Cheeky* Because... Bella and [name] did..."
    scene a4748 with dssa
    nia "Back to the real story..."
    scene a4732 with dssr
    d "Like whom?"
    scene a4734 with dssa
    b "Someone who's tongue and pussy could rock both our worlds..."
    scene a4732 with dssa
    d "Oh... I can't wait to be inside her..."
    scene a4733 with dssa
    pause 
    scene a4736 with dssa
    pause 
    scene a4737 with dssa
    nia "*Breathy* I'll rock your worlds."
    play sound "Music/Sfx/Punch.ogg"
    scene a4738 with vpunch
    "Nia shyly giggles!" 
    scene a4716 with dssa
    "Nadia laughs."
    scene a4739 with dssa
    nia "I swear this is what happened!"
    scene a4740 with dssa
    n "Keep dreaming, fake Cheeto!"
    scene a4741 with dssa
    nia "Hey!"
    scene a4742 with dssa
    n "The only threeway you're allowed to dream of is with me! Not Bella!"
    scene a4743 with dssr
    nia "This is a free country!"
    stop music fadeout 8
    scene a4744 with dssa
    n "Not for fake Cheetos!"
    scene black with Dissolve(2)
    with Pause(.5)
    jump TherapyIn

label TherapyIn:
    play ambient "Music/Sfx/Ambient_Suburban.ogg"
    if RoRum or BellaKiss03x is True:
        play music "Music/Scott Buckley/Scott Buckley - Echoes.ogg"
        $ BellaSlappy = True 
        scene a4792 with dssb 
        pause 
        scene a4794 with dssr
        d "We'll bang, ok?"
        scene a4793 with dssr
        pause
        scene a4762 with dssr
        u "Really?"
        scene a4763 with dssr
        u "Yes! He just came on to me like that."
        scene a4764 with dssa
        u "I was like- uh-dude?"
        scene a4752 with dssr
        u "Oh my gaaawd..."
        scene a4753 with dssa
        b "What a load of absolute horseshit."
        scene a4754 with dssa
        ay "Mh?"
        scene a4755 with dssa
        b "What they are saying."
        if BellaKiss3x5 is True:
            b "It makes me mad how they're lying about him."
        scene a4756 with dssa
        ay "Yeah."
        if RoRum is True:
            ay "It really didn't do him any favor that he made today's headline in the paper."
        scene a4765 with dssa
        u "He didn't ask directly, you know?"
        scene a4766 with dssa
        u "But he totally implied it! Like he- you know, touched me at my arm, gave me that look."
        scene a4767 with dssr
        u "I saw him the other day, and though he was just quiet... Good to know what he's really like."
        scene a4768 with dssa
        u "Yeah."
        stop ambient fadeout 4
        scene a4757 with dssr
        pause 
        scene a7745 with Dissolve(4) 
        b "Come! Stand up little birdy!"
        scene a7746 with dssr
        pause 
        scene a7747 with dssa
        b "Ah! Don't worry!"
        scene a7748 with dssr
        "She searches for the nest."
        scene a7749 with dssa
        b "Ah!"
        scene a7750 with dssr
        pause 
        scene a7751 with dssa
        b "I just need to find a stick you can climb on, and you'll be back in your nest in no time!"
        scene a7752 with slideleft
        b "Careful... Careful..."
        scene a7753 with dssa
        pause 
        play sound "Music/Sfx/Punch.ogg"
        scene a7754 with vpunch
        pause 
        scene a7755 with dssa
        pause 
        scene a7756 with dssa
        b "Goodbye birdy! Have a good life!"
        scene black with Dissolve(1)
        with Pause(.5)
        scene a7759 with dssr
        u "Did you hear what Bella did?"
        scene a7757 with dssr
        u "She impaled a baby bird with a stick and found that super funny."
        scene a7758 with dssa
        b "*Whispers* I didn't. I saved him!"
        scene a7760 with dssr
        u "She's so scary."
        scene a7761 with dssa
        u "We should tell Miss Morris again."
        scene a7762 with dssr
        b "I didn't do that!"
        scene a7763 with dssa
        u "Miss Norris!"
        scene a7764 with dssr
        pause
        scene a7765 with dssa
        missnorris "What is wrong with her?!"
        scene a7766 with dssa
        am "There's nothing wrong with her!"
        scene a7767 with dssa
        pause 
        scene a7768 with dssa
        am "Come." 
        scene a7769 with dssr
        b "Mama, I didn't do it."
        scene a7770 with dssr
        pause 
        scene a7771 with dssa
        am "I know."
        scene a7772 with dssr
        pause 
        scene a4758 with dssb
        pause 
        scene a4759 with dssr
        pause 
        play music "Music/Scott Buckley/Scott Buckley - Resonance.ogg"
        scene a4760 with vpunch
        b "Why do you bitches spread lies about [name]?!"
        scene a4761 with dssa
        ay "Oh no."
        scene a4769 with vpunch
        b "What's your fucking problem?"
        scene a4770 with dssr
        u "W-what the hell? He did that!"
        scene a4769 with vpunch
        b "Bullshit!"
        scene a4771 with dssr
        u "How would you know?!"
        scene a4772 with dssa
        b "I know him!"
        scene a4771 with dssa
        u "Apparently you don't know him as well as you think you do."
        scene a4791 with dssa
        if BTY is True:
            b "He's my friend!"
        else:
            b "I'm his project partner! I know him!"
        scene a4773 with dssr
        u "Ahhh! I see. You'd like to be more and you're just mad that he's trying to screw-"
        play sound "Music/Sfx/Slap4.ogg"
        scene a4774 with hpunch
        pause
        scene a4776 with vpunch
        b "Bitch! Keep lying about him like that and I'll-!"
        scene a4775 with vpunch
        u "You hit her!"
        play sound "Music/Sfx/Punch.ogg"
        scene a4777 with vpunch
        b "AND I'LL HIT YOU TOO!"
        scene a4778 with dssa
        u "What is wrong with you?! Crazy bitch!"
        scene a4779 with dssa
        ay "Fuck off."
        stop music fadeout 3
        scene a4780 with dssr 
        "Bella is breathing hard, her limbs shaking from rage, and her left palm trembling from pain."
        play sound "Music/Sfx/Punch.ogg"
        scene a4781 with vpunch
        pause
        scene a4782 with dssa 
        b "Man... I don't know!"
        scene a4783 with dssa 
        ay "It's okay."
        scene a4784 with dssr 
        ay "I know how close home that hits."
        ay "I should've noticed it... I'm sorry."
        play music "Music/Vesky - Departure.ogg"
        if BellaKiss3x5 is True:
            ay "Especially when they say these things about someone rather important to you."
        scene a4786 with dssr 
        pause
        scene a4787 with dssa 
        b "Before you, nobody ever stood up for me when someone told obvious lies..." 
        scene a4788 with dssa
        b "Silence is complicity... I'll never tolerate it."
        scene a4789 with dssa
        pause
        scene a4790 with dssa
        b "Let's go to a bar... I need a beer."
        scene a4785 with dssr 
        ay "A beer sounds good."
        stop music fadeout 5
        jump VicTherapy1x0

label VicTherapy1x0:
    scene black with Dissolve(2)
    with Pause(.5)
    scene a4795 with dssb
    pause 
    scene a4796 with dssr
    pause 
    $ play_playlist(playlist_Smooth)

    scene a4797 with dssr
    pause 
    scene a4798 with dssa
    v "I want a kebab..."
    scene a4799 with dssr
    d "With extra garlic sauce."
    scene a4800 with dssa
    v "And extra meat... extra cucumbers..."
    scene a4799 with dssa
    d "Goat cheese..."
    scene a4801 with dssa
    v "Mmmhh... but none of that red cabbage stuff."
    scene a4802 with dssr
    maj "Eating healthy would benefit your recovery."
    scene a4803 with dssa
    v "*Mumbles* It's not my physical health I'm most worried about..."
    scene a4802 with dssa
    maj "Mh?"
    scene a4804 with dssa
    v "Nothing."
    scene a4805 with dssa
    maj "What did you say?"
    scene a4806 with vpunch
    v "Nothing!"
    scene a4807 with dssr
    pause 
    scene a4808 with dssa
    pause 
    scene a4809 with dssa
    d "Obama's Kebab was great."
    scene a4810 with dssa
    v "I don't know that one."
    scene a4811 with dssa
    maj "I've been there before. I didn't know they had closed."
    scene a4809 with dssa
    d "Mhh... What I would do for a kebab from there..."
    scene a4812 with dssr
    celi "Hi!"
    celi "Welcome back, Victoria!"
    scene a4813 with dssr
    v "Hey."
    scene a4814 with dssr
    celi "Come, let's go to our room."
    scene a4815 with dssa
    v "Can Maja and [name] come with us?"
    scene a4816 with dssa
    celi "Of course."
    scene black with Dissolve(2)
    with Pause(.5)
    scene a1318 with dssr
    pause
    scene a1319 with dssa
    maj "How are your panic attacks?"
    scene a1320 with dssa
    d "Who needs coffee in the morning when you can have panic attacks is what I tell myself."
    scene a1321 with dssr
    maj "How are you dealing with them?"
    scene a1322 with dssa
    d "Let's focus on Vic today."
    scene a1323 with dssa
    maj "Believe it or not... you influence Vic a lot."
    maj "She's like a toddler in need of attunement."
    scene a1325 with dssr
    v "Yes, Maja did."
    scene a1324 with dssr
    maj "Mh? What?"
    scene a1326 with dssr
    v "You packed me some clothes."
    scene a1327 with dssa
    maj "Yes, yes! It's all in the bag."
    scene a1328 with dssa
    maj "I'll help you change."
    scene a1329 with dssr
    pause
    scene a1330 with dssa
    celi "Victoria is so cute."
    scene a1331 with dssa
    "You flick your brows signaling you're partly agreeing with her."
    scene a1332 with dssa
    celi "Are you her or Maja's boyfriend?"
    scene a1331 with dssa
    d "Neither."
    d "I'm the supportive pet."
    scene a1333 with dssa
    celi "An honorable job."
    if RoRum is True:
        scene a1334 with dssa
        celi "I saw you in today's college newspaper."
        scene a1335 with dssa
        "You raise a brow."
        scene a1334 with dssa
        celi "My little brother goes to MOR."
        scene a1335 with dssa
        d "They have that stupid paper there too?"
        scene a1336 with dssa
        celi "Every college here gets it."
        celi "But everyone knows that 80 percent of what's in that paper is exaggerated."
        scene a1337 with dssr
        celi "But it won't stop the people from talking about it."
        scene a1338 with dssa
        d "Whatever it says, it's not true."
        scene a1339 with dssa
        celi "They labeled you a fuckboy... But that Robin... She looks like a real catch."
        if NiaVisit5x0 is True:
            scene a1340 with dssr
            celi "However, I know you're not like that."
            scene a1341 with dssa
            d "And how did you figure that?" 
            scene a1342 with dssa
            celi "We have a mutual friend."
            celi "Nia." 
            scene a1343 with dssa
            d "Oh."
            scene a1344 with dssa
            celi "She told us a little bit about you."
            celi "But we didn't believe a word she said."
            celi "Until I saw a picture of you and I said 'That dude looks familiar...'."
            scene a1345 with dssr
            celi "Then I remembered from where I knew you. You were here with Victoria and Maja... So I guess Nia's story checks out."
    scene a1346 with dssr
    maj "And before anyone says anything... This is all my fault."
    scene a1347 with dssa
    maj "I thought one of my older bodysuits would fit her."
    scene a1348 with dssr
    celi "Don't worry! It looks great!"
    scene a1349 with dssa
    "Victoria smiles at you."
    if VicDate is True:
        scene a1350 with dssa
        pause
    scene a1351 with dssr
    pause
    scene a1352 with dssa
    maj "Already hitting up her therapist?"
    scene a1353 with dssa
    d "When will you come to ZPR?"
    scene a1354 with dssa
    maj "I was there today."
    maj "I assist the coaches of the first and partly the second team."
    scene a1355 with dssr
    d "And you thought one of your older suits would fit her?"
    scene a1356 with dssr
    maj "Not really. She wanted it but became self concious and I offered to take the blame."
    d "Like a good sister."
    scene a1357 with dssr
    pause
    menu:
        "Make an educated guess about her own bodysuits.":
            $ MajaBodysuitS2_1 = True
            scene a1358 with dssa
            d "Knowing you, your bodysuits would show a lot more skin."
            scene a1359 with dssa
            maj "Perhaps."
            maj "But you'll never see them."
            scene a1360 with dssa
            d "Thanks."
            scene a1361 with dssa
            maj "Knowing you, that was probably a genuine thanks."
            scene a1362 with dssr
            maj "You damn weirdo."
            scene a1358 with dssr
            d "I think if I'd dig a little bit into your past, I'd be the one calling you a weirdo."
            scene a1359 with dssa
            maj "You probably call people weird that do more than just missionary."
        "Don't and just watch Victoria.":
            pass 
    scene a1363 with dssr
    celi "Breath in... Hold it... Hold it... Exhale."
    celi "We will begin with some simple stretching exercises."
    scene a1364 with dssr
    celi "But first I want you to do a body scan- the opposite way."
    scene a1365 with dssr
    v "A what?"
    scene a1366 with dssa
    celi "Feel your body and every single part of it. Start with your head... And then slowly work yourself down to your shoulders and back."
    scene a1367 with dssa
    celi "And go further and further unti you reach your pelvis... and don't worry if you don't feel your legs."
    scene a1368 with dssr
    pause
    scene a1369 with dssa
    maj "Did you also just start doing a scan?"
    scene a1370 with dssa
    d "Yeah."
    scene a1371 with dssa
    "Maja chuckles."
    if Foursome4x5 is True:
        scene a1372 with dssa
        maj "Vic told me about the orgy you guys had."
        scene a1373 with dssa
        d "Orgy is a little far stretched."
        scene a1374 with dssa
        maj "Well, you all made out... One more step and it would have turned into a foursome."
        maj "I bet you were sad when Mila put an end to it."
        scene a1375 with dssa
        d "I wasn't. I was thankful."
        d "I took a bite too big for me to handle."
        scene a1374 with dssa
        maj "If you look at what Mila's packing, I'd say you'd need at least two or three bites."
        maj "Still, the blue ball was real afterwards, huh?"
        scene a1376 with dssr
        "You keep quiet."
        scene a1377 with dssa
        maj "Sorry, I crossed a line there."
        scene a1378 with dssa
        maj "I'm just so happy that Vic's going through with her physical therapy."
    scene a1379 with dssr
    celi "Can I get you two anything?"
    celi "A tea, water?"
    scene a1380 with dssa
    maj "Yes, We'd like some tea."
    scene a1381 with dssa
    celi "Sure!"
    scene a1382 with dssr
    pause
    maj "She looks so peaceful."
    if vicdate or VicDate or VicDateEntry2 is True:
        d "Still waters run deep."
        scene a1383 with dssr
        d "Do you think it is a good idea that I'm going out with her?"
        scene a1384 with dssa
        maj "Yes, you're currently some sort of anchor."
        maj "If you're honest with her and you don't break her heart."
        scene a1385 with dssa
        maj "You can be the cure."
        scene a1386 with dssa
        maj "But if you do something stupid, you could be her downfall."
        scene a1387 with dssa
        d "I'm glad this doesn't put any pressure on me."
        scene a1386 with dssa
        maj "Just don't lie to her."
    else:
        d "Still waters run deep."
    scene a4817 with dssr
    pause
    scene a4818 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene a4820 with dssb
    pause 
    scene a4821 with dssa
    v "I feel good."
    scene a4822 with dssa
    celi "That's great."
    scene a4823 with dssa
    v "I... I did feel a tingle this morning."
    scene a4824 with dssa
    celi "That's awesome!"
    scene a4823 with dssa
    v "But- I don't know if I imagined it..."
    scene a4825 with dssr
    celi "You didn't."
    celi "We were expecting this to happen soon."
    scene a4826 with dssr
    celi "The shock and swelling subside and sensations should return soon."
    celi "The important thing is that we keep going. No pauses."
    scene a4827 with dssr
    celi "Tomorrow, same time?"
    scene a4828 with dssa
    v "Yes."
    scene a4829 with dssa
    celi "Great. I'll see you then!"
    scene a4819 with dssr
    pause
    scene a4830 with dssa
    maj "Come, you'll need to change."
    scene a4831 with dssa
    v "Noooo! I'm good."
    v "I'm too exhausted to change... I just want get home."
    scene a4832 with dssr
    stop music fadeout 5
    maj "I'll get the car and you'll put her in before anyone sees her."
    scene a4833 with dssr
    pause 
    play music "Music/OST/Azula Wave - Lost Souls.ogg"
    scene a4834 with dssa
    pause
    scene a4835 with dssr #music geht weg falls genutzt 
    pause
    scene a4836 with dssr
    pause
    if VicDate or VicDateEntry2 is True:
        $ VicTouching5x5 = True
        scene a4837 with dssa
        v "I hope someday, we'll be at a point where you would just fuck me in situation like this."
        v "Nobody's here... Just get on it. Do me."
        scene a4838 with dssa
        d "(This situation is very hard to navigate.)"
        d "(It feels like I'm walking on egg shells... I have to be mindful of what I say. I can't sound too rational.)"
        scene a4839 with dssa
        d "(Usually, I don't care to break a thing or two... but something's on the line here.)"
        scene a4840 with dssr
        pause 
        scene a4842 with dssa
        d "I hope so too."
        scene a4843 with dssa
        pause 
        scene a4844 with dssr
        pause
    else:
        scene a4840 with dssr
        d "Ready?"
        scene a4842 with dssr
        pause 
        scene a4841 with dssa
        "She just keeps quiet."
        scene a4845 with dssr
        d "I'll take that as a yes."
    stop music fadeout 5
    scene black with Dissolve(2)
    with Pause(.5)
    scene a7958 with dssb
    pause
    scene a7959 with dssr
    pause 
    scene a7960 with dssr
    maj "Vic?"
    maj "Do you want a hot bath?"
    scene a7961 with dssa
    v "Sounds good."
    scene a7962 with dssr
    "Vic and Maja vanish into the bathroom."
    scene a7963 with dssb
    "You wait a few minutes..."
    d "(...Should I just leave?)"
    scene a7964 with dssa
    maj "Hey."
    maj "Vic wants you in there."
    play sound "Music/Sfx/Punch.ogg"
    scene a7965 with vpunch 
    pause 
    $ play_playlist(playlist_Romance)
    scene a7966 with dssr
    maj "*Whispers* No funny business."
    scene black with Dissolve(1)
    with Pause(.5)
    scene a4846a with dssb
    pause 
    scene a4847 with dssr
    d "Hey."
    scene a4848 with dssa
    v "Hi."
    v "I didn't want you to be alone out there."
    scene a4849 with dssr
    pause
    scene a4850 with dssa
    d "What's your verdict?"
    scene a4851 with dssa
    v "On today?"
    d "Mhm."
    scene a4852 with dssa
    v "It was good. I don't really see how it would make me walk again but-"
    scene a4855 with dssr
    maj "You just need to keep doing it. I know what I'm talking about."
    maj "Soon, you'll feel more than just a tingle and these exercises will get a lot harder."
    scene a4854 with dssr
    v "...I know."
    scene a4856 with dssr
    maj "Hey [name], what phone do you have? I need a new one."
    scene a4857 with dssa
    d "No idea."
    scene a4858 with dssa
    maj "Can I see?"
    scene a4859 with dssa
    with Pause(.3)
    scene a4860 with dssa
    "You get out your phone and hand it to her."
    play sound "Music/Sfx/Punch.ogg"
    scene a4861 with hpunch
    pause 
    play sound "Music/Sfx/Splash2.ogg"
    scene a4862 with vpunch
    v "Maja!"
    scene a4863 with dssa
    d "...Let's ignore the fact that I could've hit my head in like twenty different ways."
    scene a4864 with dssr
    pause
    scene a4865 with dssr
    pause
    scene a4866 with dssa
    pause 
    scene a4867 with dssa
    pause
    scene a4868 with dssr
    pause 
    scene a4869 with dssa
    maj "I'd really love some weed now."
    scene a4871 with dssr
    v "Drugs are bad."
    scene a4872 with dssa
    maj "We have smoked together before... repeatedly."
    scene a4873 with dssa
    pause
    scene a4870 with dssr
    maj "I'm gonna get something."
    scene a4875 with dssa
    pause
    scene a4874 with dssr
    v "How's the water?"
    scene a4876 with dssa
    d "It would feel nice if didn't have clothes on."
    scene a4877 with dssa
    v "You can take them off."
    scene a4876 with dssa
    d "I know but my clothes are already drenched."
    if VicTouching5x5 is True:
        scene a4878 with dssr
        v "Do you like my tits?"
        scene a4879 with dssa
        "You're taken off guard by her sudden boldness."
        scene a4880 with dssa
        d "Uhh, yeah. Your tits are pretty nice."
        scene a4882 with dssa
        v "You can touch them."
        scene a4881 with dssa
        pause 
        scene a4883 with dssa
        "You cop a feel, not sure if you did it because you wanted it, or because she put you on the spot."
        scene a4884 with dssa
        pause 
    scene a4886 with dssr
    pause
    scene a4885 with dssr
    v "I love that wine."
    scene a4886 with dssr
    maj "I know you do."
    scene a4887 with dssr
    pause
    scene a4888 with dssa
    maj "If anyone had told me that I'd be sitting in a tub with [name]. I would've slapped that person."
    scene a4889 with dssr 
    pause
    scene a4890 with dssa 
    d "How are you guys handling the medical bills?"
    scene a4891 with dssr 
    maj "They've been paid for by the woman who hit her."
    scene a4892 with dssa
    d "Marla paid all the bills?"
    scene a4893 with dssr
    maj "Yeah, she also gave Victoria a little extra."
    scene a4894 with dssa
    d "What about the police? Did Marla in any-"
    scene a4895 with dssa
    maj "Forget it."
    scene a4896 with dssa
    d "Excuse me?"
    scene a4897 with dssa
    maj "Don't ask questions. Everything has been taken care of."
    scene a4898 with dssa
    d "So Marla gets nothing?"
    d "I always expected a call or an officer in front of my door at any day."
    scene a4899 with dssr
    maj "You ask too many questions."
    scene a4900 with dssa
    d "(...What's going on? Did Marla pay them off?)"
    scene a4899 with dssa
    maj "The way it is now is the best outcome for anyone."
    scene a4901 with dssa
    v "Is it?"
    scene a4900 with dssa
    maj "Post accident."
    scene a4902 with dssa
    d "...She must have good insurance."
    scene a4903 with dssa
    d "(There's more to Marla than what meets the eye.)"
    d "(Bella might be able to shine some light on it. I need to see the file Amber made for Marla.)"
    scene a4904 with dssa
    maj "Here drink. You've been thinking too much."
    scene a4905 with dssa
    pause
    scene a4906 with dssa
    maj "I could sleep like this..."
    if VicTouching5x5 is True:
        scene a4908 with dssa
        pause 
        scene a4909 with dssa
        maj "Watch your hand, [name]!"
    else:
        scene a4907 with dssa
        pause 
    scene a4910 with dssr
    maj "How's life at ZPR guys?"
    scene a4911 with dssa
    v "It's great. There are a lot of friendly people."
    scene a4912 with dssa
    maj "[name]?"
    scene a4913 with dssr
    d "It's alright... I can embrace it for what it is... A comfort zone killer."
    scene a4914 with dssa
    maj "Just wait until after the first month... Then the parties usually start and they have it in them."
    scene a4917 with dssr
    v "I remember the parties you threw here."
    scene a4918 with dssa
    maj "Let's not talk about them..."
    scene a4919 with dssa
    v "...The things I heard."
    scene a4920 with dssa
    maj "Be quiet."
    scene a4915 with dssr
    v "You moan so loud."
    scene a4916 with vpunch
    maj "Vic!"
    scene a4921 with dssr
    jump VicCollageCH1x
    
label VicTherapy5x5Continue:
    hide screen ContinueVicMajaCollage
    scene a4922 with dssr
    maj "Time to wash your hair and get out before you get all wrinkly."
    v "I like being wrinkly!"
    scene a4923 with dssr
    maj "*Laughs* No!"
    scene a4924 with dssa
    pause
    scene a4925 with dssr
    "You and Maja help Victoria out of the tub."
    if VicDate or vicdate is True:
        $ VicDrying5x5 = True
        scene a4926 with dssr
        v "[name] dry me up, please."
        scene a4927 with dssr
        "Maja squints her eyes... then nods."
        scene a4928 with dssa
        "She shoots you a look that translates to 'Don't do anything stupid or I'll cut off your balls.'"
        scene a4929 with dssr
        pause
        scene a4930 with dssr
        pause
        scene a4931 with dssr
        pause
        scene a4932 with dssa
        v "Don't be gentle."
        scene a4933 with dssr
        d "I see you're always leaning against something."
        scene a4934 with dssa
        d "You should be able to sit somewhat straight, right?"
        d "Or lean forwards."
        scene a4935 with dssa
        v "...I don't know. I mean, Maja said I should be able to."
        scene a4936 with dssa
        d "Why don't you do it?"
        scene a4935 with dssa
        v "I- I don't know."
        stop music fadeout 10
        menu:
            "Lean forward and I'll give you a kiss.":
                play ambient "Music/Sfx/Ambient_Night_Suburban.ogg"
                $ VicLeaning5x5 = True
                scene a4937 with dssr
                "Victoria looks around a little unsure."
                d "Come."
                scene a4938 with dssa
                "Victoria tries to learn forward."
                scene a4939 with dssa
                d "... A little more."
                scene a4940 with dssa
                "Her body starts shaking."
                scene a4941 with dssr
                v "I- can't!"
                scene a4942 with dssr
                d "Don't give up..."
                scene a4943 with dssr
                d "I want to feel your lips on mine."
                scene a4944 with dssr
                d "To touch your soft skin... Feel your breasts."
                scene a4945 with dssr 
                pause 
                scene a4946 with dssr
                d "*Whisper* Come to me, Victoria."
                scene a4947 with dssr
                "Vic manifests additional strength and reaches you."
                scene a4949 with dssb
                pause
                scene a4950 with dssa
                d "Come, stand up. I'll hold you and put on your panties."
                scene a4951 with dssa 
                v "Are you sure you didn't miss a spot?"
                scene a4953 with dssr 
                d "I'm a professional."
                scene a4954 with dssa 
                v "Professional's get paid."
                scene a4955 with dssa 
                d "This is pro-bono." 
                scene a4956 with dssr
                "You lift her up, your arms hugging her hip."
                scene a4957 with dssr
                pause 
                scene a4958 with dssr
                menu:
                    "Kiss her pussy.":
                        $ VicPussyKiss5x5 = True
                        $ Whispers +=1
                        $ MOSM = True
                        scene a4959 with dssr
                        pause
                        scene a4960 with dssa
                        "You give her a gentle kiss on the pussy... Right on her clit."
                        "Vic's booty tenses up."
                        scene a4961 with dssa
                        pause 
                        scene a4962 with dssa
                        d "You liked that?"
                        v "*Breathy* Very much."
                        v "Can you do it again?"
                        play sound "Music/Sfx/Whisper1.ogg"
                        scene a4963 with dssa
                        pause 
                        scene a4964 with dssa
                        d "I- I'll do it again... with more care on our date."
                        scene a4965 with dssr
                        v "Yes please."
                    "Don't kiss her pussy.":
                        scene a4965 with dssr
                        pause 
            "Don't put too much pressure on her.":
                pass
        $ play_playlist(playlist_Romance)
        scene a4966 with dssr
        "You put on her panties, swing her over your shoulder."
        scene a7690 with dssr
        "And carry her to her to her room..."
        d "Hanging in there?"
        scene a7691 with dssa
        v "For the moment, yeah!"
        scene a7692 with dssa
        "She yawns."
        scene a7693 with dssa
        pause 
        scene a7694 with dssa
        v "Thanks for being here today."
        scene a7695 with dssa
        d "I promised."
        scene a7696 with dssa
        v "I've heard maaany promises in my life."
        scene a7697 with dssa
        v "Maja promised me that we'd switch rooms when I turned 18."
        scene a7698 with vpunch
        v "Liar!"
        scene a7699 with dssa
        v "Some other duuuude promised me a date."
        scene a7700 with dssr
        d "Did I promise though?"
        scene a7701 with dssa
        v "You better!"
        scene a7702 with dssa
        d "I was in over my head previously... I think I'm a bit better now."
        scene a7703 with dssa
        v "I'll believe it when I see it."
        scene a7704 with dssr
        pause 
        scene a7705 with dssa
        v "You dummy... It doesn't even have to be a big, fancy date..."
        scene a7706 with dssa
        v "Movies, picnic... our first sex tape... the simple things."
        scene a7707 with dssa
        "You chuckle."
        if VicEroticBook4x5 is True:
            $ Victoria_Smut_Books = True 
            scene a7665 with dssa
            d "You've been reading smut books again, haven't you, Ma'am?"
            scene a7666 with dssa
            v "No Sir. I'd never do that."
            scene a7667 with dssa
            d "Show me your stash."
            scene a7668 with dssa
            v "I'm just booksitting for someone! I swear!"
            scene a7669 with dssr
            pause 
            scene a7670 with dssa
            d "So what's in the books?"
            scene a7671 with dssa
            v "I wish I could tell you."
            v "You see, I start reading them like usual, but whenever a spicy scene starts, I'm already so aroused, that I finish a few minutes later..."
            scene a7672 with dssr
            v "Then I'm like-... What the hell am I reading here?! I put the book away just to grabble it out of the shelf the next day again..."
            scene a7673 with dssa
            v "But today is the day! On my 13th try I'll get through the first spicy scene!"
            scene a7674 with dssa
            d "*Chuckles* Good luck."
            scene a7675 with dssa
            v "I also found myself skipping to the hot scenes... I'm not proud of it. I feel like I'm disrespecting the author."
            scene a7676 with dssa
            d "Perhaps you should get yourself some actual smut books? Those that focus on the action? Some short stories come to mind."
            scene a7677 with dssa
            v "Where would you even buy that?"
            scene a7678 with dssa
            d "You order it... Maybe if you want something more custom-tailored, I could ask Kelly from the book club."
            scene a7679 with dssa
            v "Something custom..."
            scene a7680 with dssa
            v "I'd love some new stories! Custom tailored or not!"
            v "Pick some out for me!"
            scene a7681 with dssa
            d "I'll keep my eyes open."
            scene a7682 with dssa
            pause
            scene a7683 with dssr 
            pause 
            scene a7684 with dssa
            pause 
            scene a7685 with dssa
            v "*Whispers* Make sure the books are really dirty."
            scene a7686 with dssr
            pause 
            scene a7687 with dssa
        else:
            scene a7708 with dssa
            d "Will you be okay?"
            scene a7709 with dssa
            v "Yes."
            scene a7681 with dssr
            d "Alright."
            scene a7682 with dssa
            pause 
            scene a7687 with dssr
        d "I'm going to dry myself now."
        scene a7688 with dssa
        stop music fadeout 5
        v "Carry me to bed. I'm tired."
        scene a7689 with dssa
        pause
    else:
        scene a7710 with dssr
        maj "[name], wait outside. I'll dry her up."
        scene a7711 with dssa
        d "Sure."
        scene black with Dissolve(2)
        with Pause(.5)
        stop music fadeout 5
        show text "You wait for Maja to finish up Vic." with Dissolve(1)
        with Pause(5)
        hide text with Dissolve(2)
    if BellaNonExclusive5x0 is True:
        jump BellaBar5x5
    else:
        jump MajaBathroom5x5



label BellaBar5x5:
    scene black with Dissolve(2)
    with Pause(.5)
    play music "Music/Vesky - Departure.ogg"
    scene a7712 with dssb
    b "And he said something to me..."
    scene a7731 with vpunch
    ay "What did that jerk say?!"
    scene a7713 with dssa
    b "I'm not sure if he's even aware of the severity of his words..."
    scene a7714 with dssa
    "She takes a big slurp of her beer."
    scene a7715 with dssa
    b "He said... He said I speak to him on a level that only Summer had reached before..."
    scene a7732 with dssr
    ay "Awww..."
    play sound "Music/Sfx/Thud3.ogg"
    scene a7716 with vpunch #glass hit sfx
    b "I hate him so much..."
    b "Why did I have to meet him?!"
    scene a7733 with dssr
    ay "You're an idiot."
    scene a7717 with dssr
    b "I wanted my college years to be full of adventures and memories!"
    scene a7734 with dssr
    ay "I thought we agreed on not being slutty college chicks?"
    if Sanitized is False:
        scene a7719 with dssr
        b "I never agreed to that!"
        scene a7718 with dssa
        ay "We also never had that talk."
        scene a7735 with dssr
    else:
        scene a7735 with dssa
    ay "But hey, now you can have the adventures and memories with someone by your side."
    scene a7736 with dssr
    b "We're not even a couple... Hell, we're not even having sex!"
    scene a7737 with dssa
    ay "Yeah, that's an issue."
    scene a7720 with dssr
    b "And his eyes... God."
    b "Like he stares at me, he probably thinks it intimates me, but no... I get so hot."
    scene a7721 with dssa
    b "...I lose myself in his fucking, beautiful, deep green eyes."
    scene a7738 with dssr
    ay "You're not exclusive. Get your fix somewhere else while he decides what he wants."
    scene a7721 with dssr
    b "I can't. I only want this fool."
    if len(Dating_List) >= 3:
        $ BellaSuspicious = True
        scene a7739 with dssr
        ay "The only thing I'll say though... I heard [name] isn't just driving on your lane."
        if BTY2 is True:
            $ BellaSuspicious = False
    scene a7722 with dssr
    ay "It sounds to me like you should've aimed for a relationship."
    scene a7723 with dssa
    b "I told you already that it's not what I want..."
    scene a7744 with dssr
    ay "What you want and what you need are two different things."
    scene a7724 with dssr
    b "No... I'm not getting into a relationship with him until we've had sex..."
    scene a7740 with dssr
    pause
    scene a7741 with dssa
    ay "Never ever have I seen you like this."
    scene a7725 with dssr
    b "I don't know what's wrong with me..."
    scene a7726 with dssa
    ay "Maybe you've been drunk for the past few weeks."
    scene a7727 with dssa
    b "Maybe I've already had that canyon race and died... And this is HELL!"
    scene a7742 with dssr
    ay "So what are you gonna do about [name]?"
    ay "Suffer like a queen? Or are you going to take it like an amazonian goddess?"
    scene a7728 with dssa
    b "I have a plan."
    scene a7729 with dssa
    ay "Does this plan start with another round?" #empty glass
    scene a7730 with dssa
    b "It does now."
    scene a7743 with dssr
    ay "Then fill me up... and in."
    stop music fadeout 5
    scene black with Dissolve(2)
    with Pause(.5)
    jump MajaBathroom5x5


label MajaBathroom5x5:
    play music "Music/VeskyThinkingOfYou.ogg" fadein 7
    stop ambient 
    scene a4967 with dssb
    pause 
    scene a4969 with dssr
    maj "Do you mind if I'm here?"
    d "Come in."
    scene a4970 with dssa
    pause
    scene a4971 with dssa 
    "She throws away her towel."
    scene a4972 with dssr
    pause 
    scene a4973 with dssa
    maj "What?"
    menu:
        "Hard to believe you're sisters.":
            $ MajaInsult5x5 = True
            scene a4974 with dssa 
            with Pause(.4) 
            scene a4975 with vpunch
            maj "Oh my god! You- oh my-"
            scene a4976 with dssa
            d "Oh, I could see how this could be seen as an insult."
            scene a4977 with vpunch
            maj "YES!"
            scene a4978 with dssa
            maj "I would've punched you if it wasn't for today!"
            scene a4979 with dssa
            d "Sorry."
            scene a4980 with dssr
            pause
            scene a4981 with dssa
            maj "No! I will punch for this another time!"
            scene a4982 with dssr
            d "Fair."
            scene a4983 with dssr
            pause
            menu:
                "Compliment her boobs.":
                    $ MajaBoobComp5x5 = True
                    scene a4984 with dssa
                    d "They look good though."
                    scene a4985 with dssr
                    maj "Too late. You're already on my shit list."
                "Don't.":
                    scene a4986 with dssr
                    pause
            scene a4987 with dssr
        "Don't look at her boobs.":
            scene a4987 with dssr
    pause
    scene a4988 with dssr
    maj "I heard you're moving in with Mila?"
    scene a4989 with dssa
    d "Yeah."
    scene a4988 with dssa
    maj "Who else is moving in?"
    scene a4989 with dssa
    d "Nami, and apparently a girl named Robin."
    scene a4988 with dssa
    maj "No idea who Robin is."
    scene a4990 with dssa
    maj "The only Robin I know is a kinky freak."
    scene a4991 with dssa
    d "Yeah, that's not this Robin."
    scene a4992 with dssr
    d "She's in my class."
    scene a4993 with dssa
    maj "Living together with three, well two hot chicks... while my little sister likes you..."
    scene a4994 with dssa
    maj "I can't say that this makes me very happy."
    scene a4995 with dssr
    d "Who of them isn't hot?"
    scene a4996 with dssa
    maj "I just left out Nami because if there was something between you two, it would've happened already."
    scene a4997 with dssr
    maj "And Robin sounds hot."
    scene a4998 with dssa
    pause
    if VicDrying5x5 is True:
        scene a4999 with dssa
        maj "Soo... How was it... drying Vic up?"
        scene a5000 with dssa
        d "Interesting."
        d "I got her to lean forward."
        scene a5001 with dssa
        maj "I noticed that she's been avoiding it."
        scene a5002 with dssa
        d "I told her I'd give her a kiss if she did it."
        scene a5003 with vpunch
        maj "That's sooo cute!"
        if VicPussyKiss5x5 is True:
            scene a5004 with dssa
            d "And then I kissed her pussy."
            play sound "Music/Sfx/Slap.ogg"
            scene a5005 with vpunch
            maj "OH MY GOD! TOO MUCH INFO!"
            play sound "Music/Sfx/Slap2.ogg"
            scene a5006 with vpunch #sfx
            maj "I didn't want to know that!"
            scene a5007 with dssa
            maj "Wait! Was it consensual?!"
            scene a5008 with dssa
            d "Of course."
            d "If you knew what she asked me to do next-"
            scene a5009 with vpunch
            maj "NO!"
            scene a5010 with dssa
            maj "She asked you nothing!"
            scene a5011 with dssa
            "You let out a little chuckle and move her hand and nails away from your skin."
            scene a5013 with dssa
            maj "Victoria is an innocent, young woman who would never engage in such frivolous activity!"
            scene a5012 with dssa
            d "Not at all."
            scene a5014 with dssr
            maj "I knooww... and I hate it."
            maj "She was supposed to be a little angel... Not like me..."
            scene a5015 with dssr
            pause
            scene a5022 with dssa
            maj "But I think the accident really did something to her..."
            maj "Since it happened, she started to wear deep cleavages." 
            scene a5023 with dssr
            d "Girl got nothing to lose."
            scene a5024 with dssa
            maj "...I guess."
            scene a5025 with dssa
            maj "Boah... Do I hope she won't end this year pregnant."
            scene a5016 with dssa
            pause 
            menu:
                "Flirt a little.":
                    $ MajaFlirt = True 
                    scene a5017 with dssa
                    pause 
                    scene a5018 with dssa
                    maj "Umm..."
                    scene a5019 with dssr
                    pause
                    scene a5020 with dssa
                    pause 
                    scene a5021 with dssa
                    maj "Oh. Okay." 
                    scene black with Dissolve(2)
                    with Pause(.5)
                "Don't.": 
                    scene black with Dissolve(2)
                    with Pause(.5)
    if MilaDate is True:
        scene a4999 with dssa
        maj "A birdie told me that you are going out with Mila."
        scene a5000 with dssa
        d "That's the plan."
        scene a4999 with dssa
        maj "How did you pull that?"
        scene a5000 with dssa
        d "I just treat everyone the same."
        scene a5002 with dssa
        pause 
        if VicDate and VicDateEntry2 is False:
            scene a5007 with dssr
            maj "No chance for Vic?"
            scene a5008 with dssa
            with Pause(.3)
            menu:
                "I like her as a friend.":
                    $ VicFriend = True 
                    maj "Mmm."
                "Mentally, I'm not in a position to date her.":
                    $ VicDateMental = True 
                    scene a5007 with dssa
                    maj "Meaning?"
                    scene a5027 with dssa
                    d "I'm in a hole myself... and I don't have the mental fortitude to give her what she wants romantically."
                    scene a5026 with dssa
                    d "I want to help her get better... but I can only do one of these."
                    scene a5028 with dssa
                    maj "Mmm."
        else:
            pass 
    else:
        scene a5029 with dssr
        d "What do you think of Mila?"
        scene a5030 with dssa
        maj "She's been great."
        maj "I would be doing so much worse if it wasn't for her."
        scene a5031 with dssr
        maj "She knew exactly when I needed a break." 
        scene a5032 with dssa
        maj "You know... people call me. They ask about Victoria, how she's doing..."
        maj "Mila was the first and only to ask how I am doing."
        scene a5031 with dssa
        maj "I appreciated that."
        scene a5033 with dssa
        pause 
        scene a5034 with dssa
        maj "We're going to a bar next week."
        scene a5035 with dssa
        d "That's good."
        d "It seems like you found a new friend."
        scene a5036 with dssa
        maj "Yah."
        scene a5037 with dssr 
        pause
    stop music fadeout 5
    scene black with Dissolve(2)
    with Pause(.5)
    jump VicEnd5x5

label VicEnd5x5:
    play music "Music/Indie/Beza - All the Beautiful Things.ogg" fadein 3
    scene a5038 with dssb
    pause 
    scene a5039 with dssa
    maj "You've changed a lot in a very short time."
    maj "Respect."
    scene a5041 with dssa
    "You shake your head."
    scene a5040 with dssa
    d "It's fake."
    d "I feel as lonely as ever."
    scene a5042 with dssa
    d "I'm surrounded by people, yet I feel just as empty."
    scene a5043 with dssr
    maj "Depression's a bitch."
    maj "It's okay to slip and go back into hiding for a while."
    scene a5044 with dssa
    maj "Take a breather and don't see anyone for a week."
    scene a5045 with dssr
    d "I think I'll have to do that."
    scene a5046 with dssa
    d "I've been easily irritated lately... Easier than usual."
    d "This always happens after a few good days."
    scene a5047 with dssa
    pause 
    scene a5048 with dssr
    d "I'll try to take it easier."
    scene a5049 with dssa
    pause
    scene a5050 with dssa
    maj "Vic's not been easy the past days either..."
    maj "She's a little... abrasive." 
    scene a5051 with dssr
    d "I noticed."
    scene a5052 with dssa
    maj "I understand it... somewhere, but I just want to help."
    scene a5053 with dssa
    d "It's irrational and driven by a self-destructive tendency."
    d "She knows you're just there to help, but if you're in dark place, being miserable feels good."
    scene a5054 with dssa
    d "You want people to leave you alone, you want to feel miserable."
    scene a5055 with dssr
    pause
    scene a5056 with dssa
    d "That way you can feel sorry for yourself."
    scene a5057 with dssa
    pause 
    scene a5058 with dssa
    maj "You might be right."
    maj "She's never been like that before though..."
    scene a5059 with dssa
    d "...I know you won't like to hear what I'm about to say but..."
    scene a5060 with dssa
    d "She'll never again be the girl she was before the accident."
    scene a5061 with dssa
    pause 
    scene a5062 with dssr
    pause
    scene a5063 with dssa
    maj "You spoke from experience? About the self destructive tendencies?"
    scene a5064 with dssa
    d "Yeah... I still have them. Especially these days where everything feels just a little bit too much."
    scene a5065 with dssr
    maj "How should I act? Should I ignore it?"
    scene a5066 with dssa
    d "Yes and no. You need balance to it... If you just ignore her, she'll push it further and further until she gets that reaction she craves for."
    d "And believe me, she will."
    scene a5067 with dssa
    d "Nami... Nami had to take my shit for years... As stupid as she somtimes is, she knew exactly how to handle me."
    scene a5068 with dssa
    d "You should speak to her about it." 
    scene a5069 with dssa
    maj "I might do that."
    scene a5070 with dssa
    pause
    scene a5071 with dssa
    maj "Is there no one that actually makes you feel somewhat good?"
    scene a5073 with dssr
    pause
    scene a5074 with dssa
    if BellaNonExclusive5x0 or BellaOnIce5x0 is True:
        d "Bella."
        d "She's one of the only people in the world that... She feels like a little, vigorous breeze."
        scene a5072 with dssr
        d "But sometimes even she just annoys me."
    elif VicDate is True:
        d "I like Vic. But she doesn't make me feel alive yet."
        scene a5077 with dssr
        d "It's not her fault, it's just the circumstances and that I haven't really started dating her yet."
        scene a5076 with dssa
        maj "She mentioned it to me... That she thinks you might've just said yes to dating her because you wanted to be polite."
        scene a5078 with dssa
        pause #sfx wind burst
        d "That's not it."
        scene a5079 with dssa
        maj "I know. You're not polite."
    scene a5081 with dssr
    d "Zara's cool too."
    d "Having her around motivates me to workout."
    scene a5082 with dssa
    maj "Zara's a great girl."
    scene a5083 with dssa
    maj "She and Vic used to be close friends and Zara *chuckles*..."
    maj "Zara's not your typical girly girl."
    scene a5084 with dssa
    d "Do you know Vanessa?"
    scene a5083 with dssa
    maj "Yes, I was in my second to last year at ZPR when she was a freshman."
    maj "I've talked to her here and there, and she supported the Free The Boobs movement."
    scene a5084 with dssa
    d "I'm not surprised."
    scene a5085 with dssa
    d "Do you still talk to people from your college days?"
    scene a5086 with dssr
    maj "God... You make me sound so old."
    scene a5087 with dssa 
    maj "Yeah, I speak to a few. Some moved away, others changed."
    scene a5088 with dssr
    maj "One good friend passed away."
    scene a5089 with dssa
    maj "A few others have or are about to have children. They're getting married... and so on."
    maj "Some I'll see again soon when I start at ZPR."
    scene a5090 with dssa
    d "Do you feel like you're behind?"
    scene a5091 with dssa
    pause 
    scene a5092 with dssa
    "She says nothing." 
    scene a5093 with dssa
    d "(I could ask Vanessa if Maja could to come to her party...)"
    scene a5094 with dssa
    d "(Judging by what I've seen and heard about Maja... She might fit right in.)"
    scene a5095 with dssr
    d "Anyways, I've gotta go."
    scene a5096 with dssr
    maj "I'll drive you home."
    scene a5097 with dssa
    d "To Zara's."
    scene a5096 with dssa
    maj "Right. Victoria mentioned you had to leave your home."
    scene a5098 with dssr
    pause
    menu:
        "Ask her for a cigarette.":
            $ McSmoke5x5 = True
            scene a5103 with dssa
            maj "How'd you know I have them?"
            scene a5104 with dssa
            d "You carry a lot of weight on your shoulders. You'll have to even it out somehow."
            d "I assume you drink and smoke a little... Or you sleep around... Or all of it."
            scene a5105 with dssa
            maj "I've been drinking a little too much lately..."
            scene a5106 with dssa
            maj "A cig here and there, sure... but I haven't been to kinky club in a while."
            scene a5107 with dssa
            maj "But now that I got the job at ZPR, I'll get rid of my wine and cigs!"
            scene a5108 with dssa
            maj "Here take all my cigs!"
            scene a5109 with dssa
            maj "Except for one!"
            scene a5110 with dssa
            pause
            scene a5111 with dssa
            pause
            scene a5112 with dssa
            pause 
            scene a5113 with dssr 
            pause 
            scene a5114 with dssa
            maj "You never smile."
            scene a5115 with dssa
            pause
            if MajaInsult5x5 is True:
                scene a5116 with dssa
                maj "Okay, well, except for that time you made fun of my boobs."
                scene a5117 with dssa
                "You let out a chuckle."
                scene a5118 with dssa
                maj "You're such a jerk."
                maj "Sadly, that's exactly the type of guy naive college girls fall for..."
                scene a5119 with dssa
                if MajaBoobComp5x5 is True:
                    d "Hey. I said your boobs are nice."
                else:
                    d "Speaking from experience?"
                    scene a5120 with dssa
                    maj "I refuse to answer."
            scene a5121 with dssa
            d "Actually, drive me to Bella's."
            scene a5122 with dssa
            maj "Because I know where that is."
            scene a5123 with dssa
            d "It's on the way to Zara's. Königsberg."
            scene a5124 with dssa
            d "I'll give her a call on the drive."
            scene a5125 with dssa
            pause 
            scene a5126 with dssa
            pause
            if VicPussyKiss5x5 and MajaFlirt is True:
                scene a5127 with dssa
                maj "*Mumbles* Vic takes him out to dinner and Bella gets desert."
        "Don't ask her for a cig.":
            scene a5099 with dssr
            d "No wait... Drive me to Bella."
            scene a5100 with dssa
            maj "Because I know where that is."
            scene a5101 with dssa
            d "It's on the way to Zara's. Königsberg."
            d "I'll give her a call on the drive."
            if VicPussyKiss5x5 and MajaFlirt is True:
                scene a5102 with dssa
                maj "*Mumbles* Vic takes him out to dinner and she gets desert." 
    stop music fadeout 5 
    play ambient "Music/Sfx/Ambient_Night_Suburban.ogg"
    scene a5130 with dssr
    pause 
    scene a5128 with dssr
    d "You can call me and Nami at any time if you need help."
    scene a5129 with dssa
    maj "I appreciate it."
    scene black with Dissolve(2)
    with Pause(.5)
    jump BellchenStudy1x0 


label BellchenStudy1x0:
    $ play_playlist(playlist_College)
    play sound "Music/Sfx/DoorOpen.ogg"
    scene a5132 with vpunch
    pause 
    scene a5131 with dssa
    b "Why did you have to call? I was about to take a nap!"
    scene a5133 with dssr
    d "You said it yourself, we need to get some work done."
    scene a5134 with dssr
    b "After getting some good cock, I need a nap!"
    scene a5135 with dssr
    pause 
    scene a5136 with dssr
    b "...Unrelated."
    scene a5137 with dssa
    d "Imagine us being punished by having to stay project partners..."
    scene a5138 with dssr
    b "Oh God..."
    if BellaDate is True:
        scene a5139 with dssa
        pause 
        scene a5140 with dssr
        pause 
        scene a5141 with dssa
        d "It doesn't sound so bad..."
        scene a5142 with dssa
        b "It doesn't..."
        scene a5143 with dssr 
        pause 
        scene a5144 with dssa
        pause 
        scene a5145 with dssa
        d "Do you know what I realized?"
        scene a5146 with dssa
        b "That maybe you don't just like boys?"
        scene a5145 with dssa
        d "We never meet up without an ulterior motive."
        scene a5147 with dssa
        b "That's not true."
        scene a5148 with dssr 
        pause 
        scene a5149 with dssa
        d "Think about it."
        scene a5149 with dssa
        d "We meet up to study, we met up to get revenge on the holgerson's."
        scene a5150 with dssa
        b "We met up the other day at the parking lot."
        scene a5149 with dssa
        d "That was because the old Holgerson called you."
        scene a5150 with dssa
        b "Right."
        scene a5151 with dssa
        b "I mean... I guess we should..."
        scene a5152 with dssa
        d "Go on a real date?"
        scene a5153 with dssa
        b "*Breathy* Yah."
        scene a5154 with dssa
        b "We can go to the movies..."
        scene a5155 with dssa
        b "A little under-the-pants-hand-stuff."
        scene a5156 with dssr
        b "Then we'll end the night here."
        scene a5156 with dssa
        b "No. Not here! I have an idea."
        scene a5158 with dssa
        b "I'll get back to you, but I've gotta confirm something first."
        scene a5159 with dssr
        b "Give me a few minutes..."
        scene a5160 with dssa
        d "I can wait in your room."
        scene a5161 with dssa
        b "No. I have to change... and tidy up."
        scene a5162 with dssa
        b "I'll yell for you." 
        play sound "Music/Sfx/Slap.ogg"
        scene a5163 with vpunch
        pause 
        scene a5164 with dssa
        d "Hurry up."
        scene a5165 with dssr
        pause 
        jump BellaHomeLove
    else:
        scene a5140 with dssr
        pause 
        scene a5142 with dssa
        b "I guess it could be worse."
        scene a5141 with dssa
        d "Could it?"
        scene a5142 with dssa
        b "Yap."
        b "You could've been some creepy dude that would constantly hit on me."
        scene a5166 with dssr
        pause 
        d "I'm trying to think of a worse version of you but can't think of any."
        scene a5167 with dssa
        b "I could've been one of these girls that show you unfunny WormToks, laugh all the time and never stop talking."
        scene a5168 with dssr 
        pause 
        scene a5169 with dssa
        d "...That would be worse." 
        if BTY is False:
            scene a5170 with dssa
            d "Enough time wasted. Let's go study." 
        else:
            scene a5171 with dssa
            d "Ready?"
            scene a5172 with dssa
            b "Mhm."
    jump BellchenStudy1x0_2 










label BellaHomeLove:
    scene a5175 with slideleft
    pause 
    scene a5174 with dssr 
    d "I have a bad feeling."
    scene a5176 with dssr 
    b "You're late!"
    scene a5177 with dssr 
    d "Your glasses have no lenses."
    scene a5176 with dssr 
    b "Sit down, student!"
    scene a5179 with dssa 
    d "Why did I come here..."
    scene a5180 with dssa 
    b "Don't make me spank you in front of the class- AGAIN!"
    scene a5181 with dssa 
    d "Bella we gotta-"
    scene a5182 with dssa 
    b "This is work!"
    scene a5183 with dssr
    b "Now, would you please sit down before I put your head under my skirt?!" 
    scene a5178 with dssr 
    d "Is this your Mom's blouse?"
    scene a5184 with vpunch 
    b "Focus!" 
    scene a5185 with dssa 
    d "Who's tie is that?"
    scene a5184 with dssa 
    b "Nadia and I went to a party as Secret Agents a few months ago."
    scene a5186 with dssr #kritzel sfx
    pause 
    scene a5187 with dssa
    b "What do you see?"
    scene a5188 with dssa
    menu:
        "Us?":
            scene a5190 with dssr 
            b "Somebody earned a bonus point!"
        "A weird version of the Heimlich manevour?":
            scene a5189 with dssr
            b "No."
    scene a5191 with dssa
    b "This is doggystyle."
    scene a5192 with dssa
    b "Any idea why it's called doggystyle?"
    scene a5193 with dssa
    d "..."
    scene a5194 with dssr 
    b "Didn't you do your homework?"
    scene a5195 with dssa
    pause 
    b "Go on."
    scene a5196 with dssr
    d "You want me to...?"
    scene a5197 with dssa
    b "Yes, this is what happens to student's who don't do their homework."
    scene a5198 with dssa
    pause 
    scene a5199 with dssr 
    pause
    b "Very good. Your hand placement is on point."
    scene a5200 with dssr 
    pause 
    scene a5201 with vpunch #SFX 
    pause 
    scene a5202 with dssa 
    b "W-who said you can move?"
    jump BellaHomeDGx

label BellaHomeContinueDG:
    hide screen ContinueBellaHomeDGxa
    scene a5203 with vpunch
    stop music fadeout 6
    b "Mmmmmmm!" 
    scene a5204 with dssa 
    b "...Would you like to take it further?"
    play music "Music/BibiFi/Mark Fabian - Slow Momentum.ogg"
    scene a5205 with dssa 
    d "I do... but I can't if I don't want a panic attack."
    scene a5206 with dssr
    b "Is that why you haven't gone down on me before?"
    scene a5207 with dssa 
    d "Mh."
    scene a5208 with dssr
    pause 
    scene a5209 with dssa 
    b "...What happened to you?"
    scene a5210 with dssa 
    pause 
    scene a5211 with dssr 
    pause 
    scene a5212 with dssa 
    d "You did... Something nice for a change."
    scene a5213 with dssa 
    "She keeps quiet and doesn't push it any further, well aware that you dodged the question."
    scene a5214 with dssr 
    pause 
    "She gently moves her hand through your hair... and strokes your head..."
    "...Until you fall asleep on her warm body."
    scene a5215 with Dissolve(3) 
    pause 
    scene a5216 with dssr
    pause
    scene a5217 with dssr 
    b "Mmmm..."
    scene a5218 with dssr 
    d "What time is it?"
    scene a5219 with dssa  
    b "We slept for an hour..."
    scene a5220 with dssa  
    b "At least I got my nap."
    scene a5221 with dssa  
    d "Do we wanna study something?"
    scene a5222 with dssa  
    b "Yeah."
    b "I'll change back and get us something to drink."
    scene a5223 with dssa 
    "You spread her leg."
    b "Mh?"
    scene a5224 with dssr 
    d "...Just looking." 
    pause 
    scene a5225 with dssr
    "With dreamy eyes she looks at you."
    scene a5226 with dssa 
    pause 
    scene a5227 with dssr 
    pause
    play sound "Music/Sfx/Punch.ogg"
    scene a5228 with vpunch
    "You drag her backwards onto you."
    scene a5229 with dssr
    pause 
    scene a5230 with dssa
    b "...Do you want to let me go?"
    scene a5231 with dssa
    d "I really don't."
    scene a5232 with dssa
    pause 
    scene a5233 with dssr
    pause 
    play sound "Music/Sfx/Punch.ogg"
    scene a5234 with vpunch 
    "She flops out of your arms."
    scene a5235 with dssa
    pause 
    scene a5236 with dssa
    b "...Where did I put my clothes?"
    scene a5237 with dssr
    d "Check by the whiteboard."
    scene a5238 with dssa
    b "If I don't find them there, you'll be punished."
    scene a5239 with dssr
    b "...Lucky you."
    scene a5240 with dssa
    d "How many more positions did you have in mind?"
    scene a5241 with dssa
    b "Many more."
    scene a5242 with dssa
    d "Maybe someday we'll get through them."
    scene a5243 with dssr
    b "Of course we will. Every single one... one after another until I'm too sore to keep going..."
    scene a5244 with dssa
    b "...But you keep pounding my sore pussy and I-"
    scene a5245 with dssr
    d "Ssshhhh, you're talking yourself into a horny-frenzy."
    scene a5246 with dssa
    b "My pussy needs attention."
    scene a5247 with dssa
    if Kate_Bella is True:
        d "(Hmm... Kate wants Bella to give her pussy some attention and I agreed to help her with it...)"
        d "(...What if I turned it around, and instead worked on Kate serving Bella at the end?)"
        d "(Let's see what the future brings.)"
    else:
        pause 
    scene a5248 with dssa
    d "I have to ask... Why did you get a picture of a 'cock'?"
    scene a5249 with dssa
    b "I ordered it for Nadia. She wants to give it to Nancy for some reason."
    b "I don't know why, and I usually don't entertain her ideas or- ask questions. It somehow always ends up with a lecture about Element 115 and Bob Lazar."
    scene a5250 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    jump BellchenStudy1x0_2


label BellchenStudy1x0_2:
    scene a5251 with dssb 
    pause
    scene a5252 with dssr
    b "Hmm... I'm not sure if you came to the right conclusion here."
    d "Looked right to me."
    scene a5253 with dssr
    b "Your judgement is impaired. I've seen your previous hairstyle."
    scene a5254 with dssa
    b "Here... line seven."
    scene a5255 with dssa
    d "Oh... Candida's form fungal biofilms."
    scene a5254 with dssa
    b "Yup."
    scene a5256 with dssa 
    d "Any news from the Holgerson's?"
    scene a5257 with dssa
    b "Nope."
    scene a5258 with dssr
    pause 
    scene a5259 with dssa 
    d "Is that a real gun?"
    if RoRum is True:
        scene a5260 with dssr
    else:
        scene a5260a with dssr
    b "Mhm."
    d "I think you're the last person I'd trust with a gun."
    scene a5262 with dssr
    b "Smart."
    b "There is a good chance, I would shoot a creep like you."
    scene a5261 with dssa
    d "Creep?"
    scene a5263 with dssa
    b "Mmh."
    scene a5264 with dssa
    d "From the very first day we've met, you've been dropping sexual remarks left and right."
    d "You're the creep."
    scene a5265 with dssa
    b "Liar, liar, pants on fire." 
    if BTY is True:
        scene a5266 with dssa
        b "I was at a friend's place the other day, and she was playing some sort of a co-op game with her boyfriend."
        b "We could play it."
        scene a5267 with dssa
        pause
        if BellaDate is False:
            d "...Are you hitting on me?"
            scene a5266 with dssa
            b "No?"
            b "I'm asking you as frie- acquaintances!"
            scene a5267 with dssa
            d "(...A friendship with Bella? Do I want that?)"
            menu:
                "Agree.":
                    $ Bellchen_COOP_Friends = True 
                    scene a5268 with dssa
                    b "Okay."
                "Nah, not my thing.":
                    scene a5266 with dssa
                    b "Okay."
                    jump BellaStudyEnd2x0
        else:
            scene a5266 with dssa
            d "Yeah, why not."
        scene a5267 with dssa
        d "So you do play videogames?"
        scene a5266 with dssa
        b "Rarely, and usually only things like Super Wormio."
        scene a5268 with dssa
        b "I used to play Lust for Speed because you could tune your cars."
        scene a5269 with dssa
        d "Alright, what kind of game is it?"
        scene a5268 with dssa
        b "You have to solve puzzles, fight enemies, and explore the world."
        b "You can only play it with someone else."
        scene a5270 with dssa
        d "Yeah, let's play it."
        scene a5271 with dssa
        b "I'll buy the console and the game."
        b "You'll get some snacks."
        scene a5270 with dssa
        d "We should buy them together. I don't know what your kind eats."
        scene a5271 with dssa
        b "I can then help you find the right tampon size."
        scene a5272 with dssr
        d "I really don't want to know how you act on your period."
        scene a5273 with dssa
        if BellaDate is False:
            b "Horny."
        else:
            b "Three miserable days followed by a few days of insatible horny."
            b "I turn into a Nadia-lite for a few days."
        scene a5274 with dssa
        d "When is it due?"
        scene a5275 with dssa
        b "Should be next week."
        scene a5274 with dssa
        if BellaDate is True:
            d "But you're already so horny-"
            scene a5276 with dssa
            b "This is just normal, dude."
            b "You just can't relate because you haven't been horny since the innovation of gunpowder." 
            b "That's how disconnected you are from normal people."
            scene a5277 with dssr
            d "You're not normal."
            scene a5279 with dssa
            b "Of course not. I'm awesome."
        else:
            scene a5277 with dssr
            d "...Great."
            d "Get it out of your system before we meet up."
            scene a5278 with dssa
            b "Maybe I will, maybe I won't."
        if BellaMasturbationS2_1x0 is True:
            scene a5280 with dssr
            d "You wanted to show me how you do it yourself."
            scene a5281 with dssa 
            b "Another day."
            scene a5280 with dssa 
            d "Not horny for a change?"
            scene a5281 with dssa 
            b "I am, but you were already crashing out earlier. I think pushing it will achieve the opposite of what I want."
            scene a5282 with dssa 
            pause 
            scene a5283 with dssa 
            b "Like- the first time you actually get to play with me, I want the full course..."
            scene a5284 with dssr
            b "A little appetizer..."
            scene a5285 with dssr 
            b "Followed by an exotic cocktail with a little umbrella."
            scene a5286 with dssr 
            b "Of course, the main course..."
            scene a5287 with dssr 
            b "Yeah, no desert. We'll be spent after the main course."
            scene a5288 with dssr  
            pause 
            scene a5289 with dssr  
            b "Just as a headsup when we eventually go that step... I'm not on birthcontrol."
            scene a5290 with dssa  
            d "We can use a condom."
            scene a5294 with dssr 
            b "No."
            scene a5293 with dssa  
            d "No?"
            scene a5294 with dssa  
            b "*Soft* No."
            scene a5293 with dssa  
            d "How about we don't ruin our future?"
            scene a5295 with dssr 
            b "Maybe... I'll let you pull out."
            scene a5296 with dssa 
            d "I don't understand."
            scene a5297 with dssa 
            b "Right before you cum, you pull out."
            scene a5298 with dssa 
            d "That's not safe at all!"
            scene a5299 with dssa 
            b "You're also mistaken if you think I'm going to let you pull out."
            b "I'll lock my legs around you and leave you no other choice than to paint my insides white."
            scene a5298 with dssa 
            menu:
                "I would've done that anyways.":
                    scene a5300 with dssa 
                    pause 
                    scene a5301 with dssa 
                    b "Yes please."
                    scene a5302 with dssr 
                    pause 
                    scene a5303 with vpunch 
                    b "I mean NO!"
                    b "One of us has to be the responsible part! And it's not going to be me!"
                    scene a5304 with dssa 
                    pause
                "You're going to be a lot of work.":
                    scene a5305 with dssr
                    b "You realized that now?"
        if Kate_Bella is True: 
            d "(I could gather some info regarding the thing with Kate.)"
            scene a5306 with dssa 
            d "Did you ever do it with a girl?"
            scene a5307 with dssa 
            b "Depends on what you mean."
            scene a5306 with dssa 
            d "I don't know... Kiss? Touch? Oral?"
            scene a5308 with dssa 
            b "No, but I kissed a few girls. Friends, you know... For fun."
            scene a5309 with dssa 
            d "Would you ever eat out a girl?"
            scene a5311 with dssr 
            b "Why? Are you into that? Do you want me eat out another girl while you watch?"
            scene a5310 with dssa 
            d "I was just asking."
            scene a5312 with dssa 
            b "I like... how do I put this delicately... dick... Maybe if I was super horny I-"
            scene a5311 with dssa 
            b "And -and if you take me from behind at the same time-"
            scene a5313 with dssa 
            b "Maaaybe I'd eat out a girl. Perhaps a bit of 'roleplay' would help."
            scene a5314 with dssr
            d "(She has a submissive side... The whole Kate-dynamic could trigger this hard...)"
            d "(But it has to be approached with a lot of care.)"
            scene a5315 with dssa 
            b "Why did you ask me to remove my undershirt earlier today?"
            scene a5314 with dssa
            d "I like your boobs."
            scene a5316 with dssa
            b "If you want to see them, I'll send you a picture... Asking me to sport a huge underboob was something else."
            b "A lot of people stared at me."
            scene a5318 with dssr
            d "Yet you did it without hesitation."
            d "You should mentally prepare for tomorrow... I might... demand... some things."
            scene a5319 with dssa
            b "No." 
            scene a5320 with dssa
            b "..."
            scene a5319 with dssa
            b "Maybe... if I'm horny enough."
            scene a5321 with dssa
            b "I mean no." 
            scene a5320 with dssa
            b "..."
            scene a5322 with dssa
            b "How dirty is it gonna be?"
            scene a5323 with dssa
            d "Dirty."
            scene a5324 with dssa
            b "I'll try to act excited for the inevitable letdown of it being nothing more than us kissing in public." 
            scene a5325 with dssr
            d "What's wrong with us kissing in public?"
            scene a5326 with dssa
            b "There's nothing wrong with that. I just meant you shouldn't hype up something as tame as 'kissing in public', because that's all it's going to end up being."
            scene a5327 with dssr
            pause
            d "(I might talk to Kate before the bar... She'll have some ideas.)" 
        elif BellaDate is True:   
            scene a5306 with dssr
            d "Someday."
            scene a5307 with dssa
            b "Imagine if you and I were sexually incompatible, and it just felt wrong."
            scene a5306 with dssa
            d "I doubt it."
            scene a5308 with dssa
            b "Same..."
            b "We have a level of chemistry I have never seen before."
            b "None of my friends or literally anyone I know has something like this... I think."
            scene a5309 with dssa
            d "We talk about this a lot, did you notice that?"
            scene a5311 with dssr
            b "Yeah, maybe we do feel a little stuck, that's why we have to remind ourselves constantly."
            b "...Maybe so that the other doesn't leave."
            scene a5310 with dssa
            d "I couldn't even leave if I wanted to..."
            scene a5313 with dssa
            b "Project partners. Yay."
        else:
            pass
    else:
        pass 
    jump BellaStudyEnd2x0


label BellaStudyEnd2x0:
    scene a5328 with dssr 
    d "I should be heading out."
    scene a5329 with dssr
    b "Yeah."
    scene a5330 with dssa
    d "This is the first time we've got some studying done."
    scene a5331 with dssa
    b "I saw a book online about the Biotechnology of Yeasts and Filamentous Fungi. I'll order it."
    scene a5332 with dssa
    d "Sounds good."
    if BTY is True:
        menu:
            "Fungi-Five?":
                $ FungiFive = True 
                scene a5333 with dssr
                pause 
                scene a5334 with dssa
                b "Yah... I'm not giving you a Fungi-Five."
                scene a5335 with dssa
                d "Fungi-Five?"
                scene a5336 with dssa
                pause 
                play sound "Music/Sfx/Slap.ogg"
                scene a5337 with vpunch
                pause
                if BellaKiss3x5 is False:
                    pass
                    $ BellaF_STG1 = True  
            "Don't ask for a Fungi-Five.":
                pass 
    scene a5338 with dssr
    pause 
    stop music fadeout 4
    scene black with Dissolve(2)
    with Pause(.5)
    jump ZaraTraining5x5






        






label ZaraTraining5x5:
    $ play_playlist(playlist_Caio)
    scene a5339 with dssb
    pause 
    scene a5340 with dssr
    pause 
    scene a5341 with dssr
    pause 
    scene a5342 with dssr
    pause 
    scene a5343 with dssr
    d "(I'll check up on the Cheeto and go take another nap...)"
    scene a5365 with dssr
    "As you're about to knock, you hear Nami's voice from the other side of the door."
    scene a5366 with dssa
    n "Nadia! That's the issue with you!"
    n "You do it to gain something, I colonize countries for the love of the game!"
    scene a5367 with dssa
    n "WE'RE NOT THE SAME!"
    n "Now get your troops away from their border! I have dibs on their ressources!"
    scene a5368 with dssa
    d "(Nothing out of the ordinary.)"
    scene black with Dissolve(2)
    with Pause(.5)
    scene a5369 with dssb
    pause
    scene a5370 with dssa
    pause 
    scene a5371 with dssr
    pause 
    scene a5374 with dssr
    pause 
    scene a5372 with dssr
    n "Oh. Did I wake you up?"
    n "I was about to leave as soon as I saw you were asleep."
    scene a5373 with dssa
    d "It's okay..."
    scene a5375 with dssr
    pause
    scene a5376 with dssa
    d "I dreamed of you and Noji. We were sitting by the beach in the soft, warm sand... It was really peaceful."
    scene a5377 with dssa
    n "I can't remember the last time you told me about a good dream."
    scene a5378 with dssr
    pause 
    scene a5379 with dssa
    d "What time is it?"
    scene a5380 with dssa
    n "Almost 8PM."
    scene a5381 with dssa
    d "I've got training..."
    scene a5382 with dssa
    n "Alrighty. Let me know when you're back."
    $ NamiBef = 0
    if RaceWithImpossibleOdds is True:
        scene a5383 with dssr
        menu:
            "Ask to see her boobs.":
                $ NamiBef +=1
                d "Cheeto?"
                scene a5384 with dssr
                n "Mh?"
                d "...Show me your boobies."
                scene a5385 with dssa
                pause
                scene a5386 with dssa
                pause 
                scene a5387 with dssr
                "The Cheeto leaves the room with a big smile."
            "Grab her hand.":
                scene a5388 with dssr
                pause
                scene a5389 with dssa
                d "I'll see you later, Cheeto."
        scene a5390 with dssr
        pause 
    else:
        pass
    if MilaDate is True:
        play sound "Music/Sfx/Vibration_Phone.ogg"
        with Pause(.5)
        scene a5391 with dssa
        d "(My phone.)" #vibrate #sfx 
        stop sound
        scene a5394 with dssb
        pause
        scene a5395 with dssr
        pause 
        scene a5394 with dssa
        pause 
        scene a5396 with dssa
        u "Did you find the ice, George?"
        scene a5397 with dssa
        pause 
        play sound "Music/Sfx/Slap3.ogg"
        scene a5398 with vpunch
        pause 
        scene a5399 with dssr
        u "Are you serious, George?! You're sleeping on the couch!"
        scene a5400 with dssa
        u "*Hisses* You make me sick, George!"
        scene a5401 with dssa
        "Mila smiles friendly."
        scene a5402 with dssr
        pause 
        scene a5403 with dssa
        pause 
        scene a5404 with dssa
        mi "Hi!"
        scene a5405 with dssa
        d "Hey, what's up?"
        scene a5406 with dssr
        mi "You have basketball training."
        scene a5392 with dssr
        with Pause(.3)
        d "You actually remembered."
        scene a5407 with dssr
        mi "Of course."
        scene a5408 with dssa
        d "Thanks Mila."
        scene a5409 with dssa
        mi "You're welcome."
        scene a5410 with dssr
        mi "You sound sad, though."
        scene a5411 with dssa
        d "I just feel a little down."
        scene a5412 with dssa
        mi "Did anything happen?"
        scene a5413 with dssa
        d "No... Today was great. I don't know what's wrong."
        d "I'm just a little exhausted."
        if Mila_Bath_Pussy or Mila_Pussy is True:
            scene a5414 with dssa
            mi "If we'd already be living together, I would've proposed to get us some wine."
            scene a5415 with dssr
            mi "Put on some lingiere, and wait for you with two glasses, a vibrator, and a bad horror movie."
            scene a5416 with dssr
            d "That sounds great."
            d "(I'd actually be in the mood for that.)"
        else:
            scene a5416 with dssr
            pause
        scene a5417 with dssa
        mi "Call me if you need anything."
        scene a5392 with dssr
        d "Yeah... Take care."
        scene a5393 with dssa
        with Pause(.4)
    stop music fadeout 10
    jump ZaraStudyyyy

label ZaraStudyyyy:
    scene black with Dissolve(2)
    with Pause(.5) 
    scene a5344 with dssb
    pause 
    scene a5345 with dssa
    d "Studying?" 
    scene a5346 with dssa
    za "Mhm."
    scene a5347 with dssr 
    pause 
    scene a5348 with dssa
    d "There was the basketball training."
    scene a5349 with dssa
    za "Shit! Right!"
    scene a5350 with dssr
    za "Wasn't it supposed to be every day?"
    scene a5351 with dssa
    play music "Music/Scott Buckley/Scott Buckley - Decoherence.ogg"
    d "I forgot."
    scene a5350 with dssa
    za "So did I. To be fair, the past days were quite eventful. It totally slipped my mind."
    scene a5352 with dssa
    za "I'll get ready."
    scene a5353 with dssa
    pause
    scene a5354 with dssr
    pause 
    scene a5355 with dssa
    pause 
    scene a5356 with vpunch 
    pause 
    scene ZaraFighty with dssa
    pause 
    scene a5359 with dssr
    va "What's wrong?"
    scene a5360 with dssa
    d "I don't feel like talking."
    scene a5361 with dssa
    va "I see that... You look different... Tense..."
    va "I recommend not going under people."
    scene a5362 with dssa
    "She eyes you for a few more seconds."
    scene a5363 with dssa
    va "Maybe I need to give you a massage? I think you in dire need of a woman's hands."
    scene a5364 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    jump SashaAngel5x5

label SashaAngel5x5:
    scene a973 with dssb
    pause
    scene a974 with dssr
    u "Sasha? Your phone."
    scene a975 with dssa
    sas "Yes?"
    scene a976 with dssa
    rob "Hey! Is it a bad time?"
    scene a977 with dssa
    sas "Not at all."
    scene a978 with dssr
    rob "I got an appointment to view a house tomorrow and I'll call Mila next. You said you wanted to be there."
    scene a979 with dssa
    sas "Sadly, I can't."
    scene a980 with dssa
    rob "Why not?!"
    scene a981 with dssa
    sas "I'm busy."
    scene a980 with dssa
    rob "...Okay. Bye. I hate you."
    scene a981 with dssa
    sas "Bye, bye."
    scene a982 with dssr
    pause
    stop music fadeout 10
    scene a983 with dssr
    sas "Stop playing with the light."
    scene a984 with dssr
    pause
    scene a985 with dssr
    play music "Music/Youth83/YOUTH 83 - Portra.ogg" fadein 15
    u "*Sigh*."
    scene a986 with dssa
    u "Why does it feel like someone else has worn this before. It itches."
    scene a987 with dssr
    sas "They're new... I hope."
    scene a988 with dssa
    u "How did you get the wings to stay up?"
    scene a989 with dssa
    u "Mine are flaccid."
    scene a990 with dssa
    pause
    scene a991 with dssa
    u "Okay... I stand corrected."
    scene a992 with dssr
    pause
    scene a994 with dssr
    pause
    scene a995 with dssr
    pause
    scene a996 with dssa
    son "Umm..."
    scene a997 with dssr
    sas "I'm surprised they put you up for this one... I'd assume, Katie has some less revealing shoots, too."
    scene a998 with dssa
    son "I don't know. Miss Sakurai told me to be here if I wanted to give it a shot."
    scene a999 with dssr
    u "You look great."
    scene a1002 with dssr
    son "Thanks."
    scene a1003 with dssr
    pause
    scene a1004 with dssr
    u "Well, well, shall we get started?"
    scene a1005 with dssa
    katie "What happened to your breasts?"
    scene a1006 with dssr
    sas "Long story."
    scene a1007 with dssa
    katie "Is it another fake tattoo? Is this Ayua's doing?"
    scene a1008 with dssa
    sas "We don't do these bets anymore and it's obviously not a tattoo."
    scene a1007 with dssa
    katie "Obviously? This being a tattoo would've just been a new middle for you and Ayua."
    scene a1008 with dssa
    sas "It's a temporary sticker for the skin that usually fades after a few days and a good rub."
    sas "I had a project with Karen where we used them."
    scene a1009 with dssa
    katie "It inspires me."
    scene a1011 with dssr
    pause
    scene a1010 with dssa
    katie "Cover them up."
    katie "John. Let's come up with a valentine's set where we use them."
    scene a1012 with dssa
    john "It will be done."
    scene a1013 with dssr
    katie "You look fabulous."
    scene a1015 with dssa
    son "Thank you."
    scene a1014 with dssa
    son "Mmm... Why did I have to change into this if I'm just going to watch?"
    scene a1013 with dssa
    katie "Do you feel confident enough to be in the shoot?"
    scene a1016 with dssr
    son "I don't. No."
    son "People will see these photos, right?"
    son "And what is this shoot about? What are we presenting?"
    scene a1017 with dssa
    katie "This is teaser for my newest underwear collection in collaboration with the club, the 'Divine Serpent'."
    scene a1018 with dssa
    katie "I also like to collect feedback from the models on the fit, aswell as the overall feel and quality."
    scene a999 with dssr
    u "*Whispers* Calling this underwear is a bit of a stretch." 
    scene a1019 with dssr
    son "And you publish our pictures... fully?"
    scene a1020 with dssa
    katie "Yes. While the official images are censored in post production, we upload the full pictures to my website. We still live in a primitive world where the nipple of a woman is something to be afraid of."
    scene a1036 with dssr
    katie "How do they feel, Elenor?"
    scene a1037 with dssa
    ele "As usual. Quite comfy."
    scene a1038 with dssa
    ele "But... I noticed that if you move a little too much, the pearls tend to go between your lips."
    scene a1039 with dssr
    katie "Can you two confirm?"
    scene a1040 with dssa
    son "You mean... between my..."
    scene a1041 with dssa
    katie "Between your pussy lips."
    scene a1042 with dssa
    son "Uh- I've only been wearing it for a few minutes... I haven't noticed anything."
    scene a1043 with dssa
    katie "Your leggings might also impede its movement."
    scene a1044 with dssr
    sas "I can confirm."
    scene a1045 with dssr
    sas "But I don't think it's necessarily a bad thing. The rough texture of the pearls can be perceived as pleasant."
    scene a1046 with dssa
    pause
    scene a1047 with dssa
    pause
    scene a1048 with dssa
    katie "I might be able to find a compromise by letting the wearer adjust the stretch."
    scene a1284 with dssr
    katie "And get that stuff off your boobs or I'll be blamed for it."
    scene a1285 with dssa
    sas "It had nothing to do with you."
    scene a1284 with dssa
    katie "Since when does this stop people from blaming me?"
    katie "Elena will blame me."
    scene a1285 with dssa
    sas "You can blame me if you want."
    scene a1286 with dssa
    katie "You know I would never do that."
    katie "No matter how idiotic the things you and Ayua do are."
    scene a1287 with dssa
    sas "I know."#hug
    scene a1288 with dssr
    john "Can we start? I have a dinner reservation coming up, Katie."
    scene a1289 with dssa
    katie "No you don't."
    scene a1290 with dssa
    john "...Okay, the Price is Wrong starts in an hour and I promised my wife I'd be there!"
    scene a1291 with dssr
    john "Sonya, how about you be a part of the shooting but we won't use your photos or videos? You just stick to Elenor and Sasha and experience what it's like first hand."
    john "Katie and I will assist you with finer adjustments."
    scene a1292 with dssa
    son "It's cold here."
    scene a1293 with dssa
    sas "The place doesn't have heating yet."
    scene a1294 with dssa
    katie "Where's Adriana?"
    scene a1295 with dssa
    john "She was-..."
    scene a1297 with dssr
    "He sighes loudly."
    scene a1298 with dssa
    john "They are the worst!"
    scene a1296 with dssr
    katie "Find her."
    scene a1299 with dssr
    katie "How are you settling in?"
    scene a1300 with dssa
    son "Good."
    scene a1299 with dssa
    katie "You can come by my warehouse and I'll give you something to wear. We do have a lot of items from older collections that you can have for free."
    scene a1301 with dssa
    son "Oh. I got some clothes from Miss Sakurai."
    son "My brother and I were invited for dinner and we were allowed to get whatever we wanted from their wardrobe."
    son "I think Ayua messed with me when she gave me some panties..."
    scene a1302 with dssa
    katie "Lovely."
    scene a1303 with dssa
    katie "Once a year I host a dinner, and I'd like to invite you and your brother."
    scene a1305 with dssr
    son "Thank you. I'll talk to him. But he doesn't speak the language. He's still learning."
    scene a1304 with dssa
    katie "That's okay."
    katie "We'd be glad to have you."
    scene a1308 with dssr
    pause
    sas "There."
    scene a1309 with dssa
    ele "It's too dark. I can't see it."
    scene a1311 with dssr
    ele "However, the idea is bold."
    scene a1310 with dssa
    sas "You have to be bold to make a difference."
    scene a1306 with dssr
    pause 
    scene a1307 with dssa
    adri "I apologize. I got a super important call about college gossip." 
    scene a1312 with dssr
    john "What's the idea here?"
    scene a1314 with dssr
    katie "Focus mostly on Elenor and Adrianna with the pictures."
    katie "Sasha is only here for the video and her private collection, the ZPR Model Ad, and to make our lives harder."
    scene a1315 with dssr
    sas "I will need you for a few extra photos later, John."
    sas "Casual, in my normal attire on the upper floor."
    scene a1313 with dssa
    john "...I promsised my wife I'd make it home for the Price is Wrong."
    scene a1316 with dssa
    sas "You'll get paid extra."
    scene a1317 with dssr
    stop music fadeout 10
    john "Fine. But we'll make it quick."
    scene black with Dissolve(2)
    with Pause(.5)
    jump Basketball5x5

label Basketball5x5:
    play ambient "Music/Sfx/Car_Drive_Night_Interior.ogg"
    scene a5418 with dssb
    pause 
    scene a5418a with dssa 
    with Pause(.6)
    scene a5419 with dssa
    pause
    scene a5420 with dssa
    d "The light is green." 
    scene a5421 with dssr 
    pause 
    scene a5422 with dssa
    za "...Nadia's Mom is in the hospital again."
    scene a5421 with dssa
    d "Oh, how come?"
    scene a5423 with dssa
    za "She's been sick for many years and just had a seizure."
    za "She's extremely afraid of her Mom dying."
    scene a5424 with dssa
    d "Should we go see her?"
    scene a5425 with dssr
    za "No, she's in the hospital with her Mom."
    scene a5426 with dssa
    za "And don't talk to her about it- okay?"
    za "Pretending that everything's fine is her way of coping with the situation."
    scene a5427 with dssa
    d "Alright."
    scene black with Dissolve(2)
    with Pause(.5)
    play ambient "Music/Sfx/Night_Crickets.ogg"
    scene a5428 with dssb
    pause 
    scene a5429 with dssr
    pause
    scene a5430 with dssa
    j "*Whisper* Thank God..."
    scene a5431 with dssa
    d "Hey."
    scene a5432 with dssa
    j "Good to see you."
    scene a5433 with dssa
    mh "Oh my... Look at..."
    scene a5434 with dssa
    mh "Who's that?"
    scene a5435 with dssa
    ms "I have no idea."
    scene a5436 with dssr
    ms "Spaghetti, what the fuck don't you understand by 'training every evening besides Sunday'?"
    scene a5437 with dssa
    ms "Where were you on Saturday?"
    scene a5438 with dssa
    mh "What's your excuse?"
    scene a5439 with dssr
    d "(I could explain it to them, but I just don't have the energy.)"
    scene a5440 with dssa
    d "No excuse. I just felt like it."
    scene a5444 with dssr
    pause 
    scene a5441 with dssr
    mh "You felt like it?"
    play sound "Music/Sfx/Punch.ogg"
    scene a5445 with vpunch
    za "Bullshit!"
    scene a5446 with dssr
    za "What the...-"
    scene a5447 with dssa
    za "They had some big damage at their place and were forced to move in with us over night."
    za "He also promised a disabled girl that he would be there for her when she starts therapy."
    scene a5448 with dssa
    d "(It seems like Vic and Zara still talk.)"
    scene a5449 with dssa
    pause 
    scene a5450 with dssr
    pause
    scene a5451 with dssa
    "Coach Hill sighs."
    scene a5441 with dssa
    mh "Why don't you just say that?"
    d "(Why am I so irrationally mad?!)"
    scene a5443 with dssr
    ms "Get your shit together, or you're out."
    scene a5452 with dssr
    with Pause(.3)
    $ RoC = 0
    $ RoP = 0
    $ play_playlist(playlist_Sports)
    menu:
        "Challenge them.":
            $ Coaches_Challenged = True 
            $ RoC -=1 
            $ RoP +=1
            scene a5453 with dssa
            d "You won't kick me."
            play sound "Music/Sfx/Punch.ogg"
            scene a5454 with vpunch
            za "*Whispers* Don't."
            scene a5455 with dssr
            ms "Oh? And why's that?"
            scene a5456 with dssr
            pause
            scene a5457 with dssa
            pause
            scene a5458 with vpunch 
            pause
            scene a5459 with dssa
            pause 
            play sound "Music/Sfx/Basketball_Hoop.ogg"
            scene a5460 with vpunch #sfx hoop
            pause 
            scene a5461 with vpunch 
            pause
            scene a5462 with dssa 
            pause 
            play sound "Music/Sfx/Basketball_Hoop.ogg"
            scene a5463 with vpunch 
            pause 
            scene a5464 with vpunch 
            "Zara catches you."
            play sound "Music/Sfx/Basketball_Hoop.ogg"
            scene a5465 with vpunch #sfx 
            pause 
            scene a5466 with dssa 
            pause 
            scene a5467 with dssr
            mh "Cocky little boy."
            scene a5468 with dssa
            ms "If your attitude gets too much, you'll be out no matter how good you play."
            scene a5469 with dssa
            ms "Do you understand?"
            scene a5470 with dssa 
            with Pause(.3)
            play sound "Music/Sfx/Punch.ogg"
            scene a5471 with vpunch   
            d "Then kic-" 
            scene a5472 with dssa 
            j "He was about to say 'kick me harder!'"
            scene a5473 with dssa 
            ms "I'll kick his little punk ass to the moon."
        "Pull yourself together and say nothing.":
            scene a5473 with dssa  
    j "What's wrong?"
    scene a5475 with dssa 
    d "I don't know."
    scene a5476 with dssa 
    j "Do you want to get kicked off the team?!"
    scene a5477 with dssa 
    pause
    scene a5478 with dssr
    d "(Why am I so mad?)"
    d "(I feel like I hate everyone and want to make everyone hate me.)"
    scene a5479 with dssr
    d "(I can't fall back into this old self destructive pattern!)"
    d "(Why does this always happen when things seem to get better?!)"
    scene a5480 with dssa
    "You start running laps."
    scene a5481 with dssa
    ms "Everyone's here for once, that's great."
    scene a5482 with dssa
    if RoC == -1:
        ms "Do what the cocky little asshole does and run a few laps to warm up."
    else:
        ms "Run a few laps. Get the blood pumping."
    scene a5483 with dssr
    "Zara is trying to run up to you, but to her surprise you're making distance."
    "Your aversion to talk to anyone, gives you an unexpected boost of stamina and speed."
    scene a5484 with dssa
    j "Zara."
    scene a5485 with dssr
    za "Hey Jeff."
    scene a5486 with dssa
    j "What's up with him?"
    scene a5487 with dssa
    za "I have no idea."
    scene a5488 with dssr
    za "He was fine all day."
    za "But he's got a lot on his mind. A lot of stuff has happened but... I think he's just exhausted."
    if RoC == -1:
        scene a5489 with dssr
        j "He can't talk to the coaches like this."
        scene a5490 with dssa
        za "I know."
    scene a5491 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene a5492 with dssb
    mh "Alright, enough technique."
    scene a5494 with dssa
    ms "Play-offs are soon."
    ms "Teamplay is of the upmost importance."
    ms "Two teams."
    scene a5495 with dssa
    mh "Jeff, Trey, Kai, Jared and Steve."
    mh "Against Sai, Tobias, Nero, Damian and [name]."
    scene a5496 with dssr
    tobi "This doesn't seem very balanced."
    scene a5497 with dssa
    mh "It's not about balance."
    scene a5498 with dssr
    mh "You've got five minutes to come up with a game plan."
    scene a5499 with dssa
    ms "Zara you stay out of it."
    scene a5500 with dssr
    pause 
    scene a5501 with dssr
    tobi "We play over the right side, Trey is slower than Jared."
    scene a5502 with dssa
    sai "I agree. Jeff is a problem and we should play around him."
    nero "Their team is good, but there's a way to outplay them."
    scene a5503 with dssa
    dam "Hey [name]."
    play sound "Music/Sfx/Punch.ogg"
    scene a5504 with vpunch
    d "Hey Damian."
    scene a5505 with dssa
    tobi "Hey you. Would you mind getting in here?"
    scene a5506 with dssa
    d "I'm listening."
    scene a5507 with dssa
    tobi "We'd like some input from you."
    scene a5508 with dssa
    pause
    scene a5509 with dssa
    tobi "How are we going to win with these two?"
    play sound "Music/Sfx/Punch.ogg"
    scene a5510 with vpunch
    d "You got a problem with him?"
    scene a5511 with dssa
    nero "Hey, hey!"
    scene a5515 with dssr
    za "[name]!"
    scene a5512 with dssr 
    ms "What's going on?"
    scene a5513 with dssa
    sai "Nothing. We're cool."
    scene a5514 with dssa
    dam "[name]. It's alright."
    scene a5516 with dssr
    mh "Zara?"
    scene a5517 with dssa
    za "Yes?"
    scene a5518 with dssa
    mh "Would you like to help us with some notes about the players?"
    scene a5519 with dssa
    za "Sure."
    scene a5520 with dssr
    mh "And when you're already on it..."
    scene a5521 with dssa
    mh "...note down the cutest butts."
    scene a5522 with dssa
    pause
    scene a5523 with dssr
    pause
    scene a5524 with dssa
    j "Good luck."
    scene a5525 with dssa
    d "You too."
    scene a5526 with dssr
    pause
    play sound "Music/Sfx/Punch.ogg"
    scene a5527 with vpunch
    "Tobias loses the standoff against Jeff-"
    play sound "Music/Sfx/Punch.ogg"
    scene a5528 with vpunch
    "-and the ball flies to Kai."
    d "(Oh, that's the white knight I pushed into the shelf the other day.)"
    scene a5529 with dssa
    d "(He moves quick. Not a bad player.)"
    scene a5530 with dssa
    "Then passes to Jeff-"
    scene a5531 with dssa
    "-who goes for a three pointer."
    play sound "Music/Sfx/Punch.ogg"
    scene a5532 with vpunch
    "But misses because Sai disrupted the ball midair with his fingertips."
    scene a5533 with dssa
    j "Sorry."
    scene a5534 with dssa
    kai "It was worth a try."
    scene a5535 with dssr
    pause 
    play sound "Music/Sfx/Punch.ogg"
    scene a5536 with vpunch
    "Damian passes to Sai."
    play sound "Music/Sfx/Punch.ogg"
    scene a5537 with vpunch
    "Who throws a pass to Nero, who-"
    scene a5538 with dssa
    "Throws a pass to you."
    scene a5539 with dssa
    "You fake a pass back to Nero-"
    play sound "Music/Sfx/Punch.ogg"
    scene a5540 with vpunch
    "But lay it up for Sai instead."
    scene a5541 with vpunch
    "He runs for the basket, jumps-"
    scene a5542 with vpunch
    "But instead of attempting to make it himself, he throws it, no eyes, sideways to you."
    play sound "Music/Sfx/Punch.ogg"
    scene a5543 with vpunch
    pause
    play sound "Music/Sfx/Basketball_Hoop.ogg"
    scene a5544 with dssa
    "And you make the basket for two points."
    scene a5551 with dssr
    ms "Very nice play! Good job [name] and Sai!"
    scene black with Dissolve(2)
    with Pause(.5)
    play sound "Music/Sfx/Basketball_Hoop.ogg"
    scene a5545 with vpunch
    pause
    play sound "Music/Sfx/Punch.ogg"
    scene a5546 with vpunch
    pause
    play sound "Music/Sfx/Basketball_Hoop.ogg"
    scene a5547 with vpunch
    pause
    scene a5548 with dssr
    pause 
    scene a5549 with vpunch
    "You throw the ball from deep inside your half."
    play sound "Music/Sfx/Basketball_Hoop.ogg"
    scene a5550 with vpunch
    pause
    scene a5552 with dssr
    mh "I hate that he's good."
    scene a5553 with dssa
    ms "He's a wildcard. He needs a real beating to get his attitude under control."
    scene a5554 with dssa
    mh "...Or something like that."
    scene a5555 with dssa
    mh "Zara?"
    scene a5556 with dssr
    mh "You and [name]... Are you a couple?"
    scene a5557 with dssa
    za "No."
    scene a5556 with dssa
    mh "Would you start sleeping with him if that calms him down?"
    scene a5558 with vpunch
    za "NO!"
    scene a5565 with dssr
    mh "It was worth a try."
    scene a5566 with vpunch
    ms "Traveling!"
    scene a5576 with dssa
    t "What? I didn't travel!" 
    scene a5577 with dssa
    ms "Yes, you did! Shut up now!"
    play sound "Music/Sfx/Punch.ogg"
    scene a5578 with vpunch
    pause
    scene a5579 with dssa
    d "Seriously?"
    scene a5580 with dssa
    pause
    scene a5581 with dssa
    nero "[name], do you wanna switch sides?"
    scene a5582 with dssa
    d "Why?"
    scene a5583 with dssa
    nero "I get the feeling that the guy has it out for you."
    nero "Call it pre-emptive problem solving."
    scene a5584 with dssa
    "You smile at him."
    scene a5585 with dssa
    d "I'll stay."
    scene a5586 with dssa
    nero "Come on dude..."
    scene a5587 with dssr
    d "(He didn't forget that I embarrassed him in front of Nadia.)"
    scene a5588 with dssr
    "Nero passes to you..."
    scene a5589 with dssr
    "You dribble along the right side."
    "Just as you are about to pass to Tobias-"
    play sound "Music/Sfx/Slap.ogg"
    scene a5590 with vpunch
    "Kai slaps your hand instead of the ball."
    scene a5591 with dssr
    ms "Foul!"
    scene a5592 with dssr
    pause 
    scene a5593 with dssa
    d "Bitch."
    scene a5594 with dssa
    kai "What did you just say?"
    scene a5595 with dssa
    pause
    play sound "Music/Sfx/Punch.ogg"
    scene a5596 with vpunch 
    pause
    scene a5597 with dssr
    pause
    scene a5598 with dssa
    pause 
    scene a5599 with dssa 
    pause 
    play sound "Music/Sfx/Punch.ogg"
    scene a5601 with vpunch
    "You stop dead in your tracks and break Kai's ankles."
    scene a5602 with dssr
    "Followed by a beautiful basket."
    scene a5603 with dssr
    play sound "Music/Sfx/Basketball_Hoop.ogg"
    pause 
    scene a5604 with dssa
    "You look down at him."
    scene a5605 with dssr
    d "At least this time you're in the green, no girl is there to witness it."
    d "Oh. My bad. One of Nadia's best friend's is here."
    play sound "Music/Sfx/Punch.ogg"
    scene a5606 with vpunch
    kai "Fuck you!"
    scene a5567 with dssa
    mh "My god..."
    scene a5559 with dssa
    za "Don't you want to break them up?"
    scene a5560 with dssa
    mh "No. I'm sick of them. Let them bash each others head in."
    scene a5607 with dssa
    kai "Who do you think you are?!"
    kai "For some reason you get this special treatment! You don't even show up for practice!"
    scene a5609 with dssa
    d "I'm just that good."
    scene a5608 with dssa
    kai "You're shit!"
    menu:
        "Nadia says otherwise.":
            $ Nadia_Says_Otherwise = True 
            scene a5610 with dssr
            pause
        "Just smile.":
            pass    
    play sound "Music/Sfx/Punch.ogg"
    scene a5611 with vpunch
    pause 
    play sound "Music/Sfx/BodyFall2.ogg"
    scene a5612 with vpunch
    "You throw him to the ground!"
    scene a5613 with dssr
    j "Both of you calm down!"
    scene a5614 with dssa
    pause
    scene a5615 with dssa
    d "It's not me who got his panties in a twist."
    scene a5616 with dssr
    kai "Fuck you! Let's see what my Dad thinks about this."
    scene a5617 with dssa
    "You laugh at him."
    scene a5618 with dssa
    kai "You'll regret this! Mark my words!"
    scene a5619 with dssr
    nero "We'll switch sides. Now."
    scene a5620 with dssa
    d "Sure."
    scene a5621 with dssr
    d "Move over."
    scene a5622 with dssa
    sai "Why me?"
    scene a5623 with dssa
    d "Because we play good together, and I want you on the opposite side, so we can set up a play."
    scene a5625 with dssa
    "Surprised by your reply, he heads over to the other side."
    scene a5624 with dssr
    d "(I feel better now.)"
    scene a7955 with dssr
    pause
    scene a7953 with dssr
    pause
    scene a7954 with dssr
    pause
    scene a5568 with vpunch
    ms "Tobias! What was that?! Are you handicapped?!"
    scene a5569 with dssa
    ms "Next time we'll try Jeff, [name] and Sai in one team."
    scene a5570 with dssa
    mh "I'm surprised about the symbiotic playstyle of Sai and [name]."
    scene a5571 with dssa
    mh "Two huge egos that cancel each other out on the field."
    scene a5626 with dssr
    mh "Kai..."
    scene a5573 with dssr
    ms "We can't drop him. His Father is still a member of the first team coaching squad."
    scene a5572 with dssa
    mh "I don't want to lose our top cripple, [name]."
    scene a5573 with dssa
    ms "That depends on whether he gets his shit together and doesn't destroy the team."
    scene a5561 with dssr
    "Coach Hill slowly turns her head towards Zara."
    scene a5562 with dssa
    pause 
    scene a5563 with vpunch
    za "I'm not sleeping with him!"
    scene a5564 with dssa
    mh "What about Kai?"
    scene a5563 with vpunch
    za "NO!"
    stop music fadeout 10
    scene a5574 with dssr
    ms "Alright, good game!"
    scene a5575 with dssa
    ms "Team [name] won by a very small lead."
    $ play_playlist(playlist_NojiMedi)
    scene a5627 with dssr
    pause 
    scene a5628 with dssa
    pause 
    scene a5629 with dssa
    dam "I was a little out of my head today... I just couldn't perform the way I wanted to..."
    scene a5630 with dssa
    d "So was I."
    scene a5631 with dssr 
    dam "I appreciate that you stood in for me, however... It makes me feel small and weak."
    scene a5632 with dssa
    d "Accepting help from others isn't weakness. Denying help because your ego hurts is."
    scene a5633 with dssr
    pause
    scene a5634 with dssa
    ms "Tomorrow ZPR opens its bar. Don't drink too much, because the day after tomorrow, we'll be back here."
    scene a5635 with dssa
    mh "Should it rain, we'll meet at the indoor court three."
    scene a5636 with dssr
    mh "You got that, [name]?"
    scene a5637 with dssa
    d "Can I talk to you?"
    scene a5638 with dssr
    pause
    scene a5639 with dssa
    "You both wait for nearby people to pass."
    scene a5640 with dssa
    mh "If you now tell me that you want to quit the team, I'll hurt you... and I won't let you."
    scene a5641 with dssa
    d "No... I've been going to therapy to deal with... some stuff."
    scene a5642 with dssa
    d "And on Wednesday, I'll drive down to my old hometown and... I don't know when I'll be back or in what mental state I'll be."
    scene a5643 with dssa
    "She closes her eyes and sighs."
    scene a5644 with dssa
    mh "Okay."
    scene a5645 with dssa
    mh "But please let it be the last time."
    mh "We won't take anymore shit from you..."
    scene a5646 with dssr
    mh "*Steps closer* Maybe get laid or something."
    scene a5647 with dssa
    d "Thanks."
    play sound "Music/Sfx/Slap2.ogg"
    scene a5648 with vpunch
    "She gives you a little slap, smiles, and leaves."
    scene a5649 with dssr
    pause 
    scene a5650 with dssr
    za "Can we go?"
    scene a5651 with dssr
    pause
    scene a5652 with dssa
    if BellaKiss3x5 is True:
        d "*Lie* I'm meeting Bella here. Leave without me."
        scene a5653 with dssa
        za "Oh. Okay cool."
        scene a5655 with dssa
        za "Later then."
    else:
        d "*Lie* I'm meeting up with someone here."
        d "Leave without me."
        scene a5654 with dssa
        za "Ohhh! A date!"
        scene a5655 with dssa
        za "Alright, later!"
    scene a5656 with dssb
    pause
    scene a5657 with Dissolve(3)
    pause 
    stop music fadeout 15
    scene a5658 with dssr
    pause
    d "(I just want to be alone for a while.)"
    pause #footsteps sfx
    if BellaDate is False:
        scene a5659 with dssr
        "You hear footsteps."
        scene a5660 with dssr
        $ play_playlist(playlist_BabyBellchen)
        pause 
        scene a5661 with dssr #wind sfx
        za "Do you want me to leave or... can I just lie here too?"
        scene a5662 with dssa
        d "I thought you had left."
        scene a5663 with dssa
        za "You were acting strange the whole time... I figured you lied."
        za "I got worried and turned around."
        scene a5664 with dssa
        with Pause(.5)
        menu:
            "I'd rather be alone. Sorry.":
                scene a5665 with dssr
                pause 
                scene a5666 with dssa
                pause 
                scene a5667 with dssa
                za "No."
                scene a5668 with dssa
                d "No?"
                scene a5670 with dssr
                za "I don't know what's wrong... but I'm worried."
                za "I haven't seen you like this before."
                scene a5669 with dssa
                pause 
                scene a5671 with dssa
                za "You'll either come home with me, or I'll stay."
                scene a5672 with dssa
                d "Zara..."
                scene a5673 with dssa
                pause 
                scene a5674 with dssa
                pause 
                jump ZaraStars
            "Nod quietly.":
                $ StarsWithZara5x5 = True
                jump ZaraStars
    else:
        play sound "Music/Sfx/Vibration_Phone.ogg"
        scene a5697 with dssr
        pause 
        stop sound
        scene a5698 with dssa
        d "Ya?"
        scene a7839 with dssr
        b "You won't believe what I just did."
        scene a7840 with dssa
        d "Get an STD test and it gave out cryptic values, patient zero?"
        scene a7841 with dssa
        b "No."
        b "Just for fun, you know, I drove the canyon track that I'll have to race in a few weeks, and set a record time."
        scene a5699 with dssr
        d "That's great."
        scene a7842 with dssr
        b "I'd prefer a little more enthusiasm in your voice."
        b "Where are you?"
        scene a7843 with dssa
        menu:
            "Tell Bella where you are.":
                pass
            "Don't tell her where you are.":
                d "On my way home."
                scene a7845 with dssa
                d "Listen, I gotta go."
                scene a7846 with dssa
                b "Same, I gotta go eat soup."
                scene a5699 with dssr
                d "Good night."
                b "Night."
                $ play_playlist(playlist_BabyBellchen)
                scene a5659 with dssr
                "You hear footsteps."
                scene a5660 with dssr
                pause 
                scene a5661 with dssr #wind sfx
                za "Do you want me to leave or... can I just lie here too?"
                scene a5662 with dssa
                d "I thought you had left."
                scene a5663 with dssa
                za "You were acting strange the whole time... I figured you lied."
                za "I got worried and turned around."
                scene a5664 with dssa
                with Pause(.5)
                menu:
                    "I'd rather be alone. Sorry.":
                        scene a5665 with dssr
                        pause 
                        scene a5666 with dssa
                        pause 
                        play sound "Music/Sfx/Punch.ogg"
                        scene a5667 with vpunch
                        za "No."
                        scene a5668 with dssa
                        d "No?"
                        scene a5670 with dssr
                        za "I don't know what's wrong... but I'm worried."
                        za "I haven't seen you like this before."
                        scene a5669 with dssa
                        pause 
                        scene a5671 with dssr
                        za "You'll either come home with me, or I'll stay."
                        scene a5672 with dssa
                        d "Zara..."
                        scene a5673 with dssa
                        pause 
                        scene a5674 with dssa
                        pause 
                        jump ZaraStars
                    "Nod quietly.":
                        $ StarsWithZara5x5 = True
                        jump ZaraStars
        d "ZPR, outside, sport area."
        d "We had practice."
        scene a7844 with dssa
        b "Are you still pretending to be a good player?"
        scene a7845 with dssa
        d "Listen, I gotta go."
        scene a7846 with dssa
        b "Same, I just saw a hot guy that I'll try to pick up."
        scene a5699 with dssr
        d "You do that."
        scene a5700 with dssr
        pause 
        scene a5701 with dssr
        pause 
        scene a5702 with dssr
        pause 
        play sound "Music/Sfx/Metal_Clingi.ogg"
        scene a5703 with dssa #metall sound
        "You hear the ring of metal."
        scene a5704 with dssb
        pause
        scene a5705 with dssr
        pause 
        scene a5706 with dssa
        d "How did you get here so fast?"
        scene a5707 with dssr
        b "I was on my way home and literally just around the corner."
        scene a5708 with dssr
        pause 
        if ZaraBBallTrust5x0 is True:
            scene a7956 with dssr
            pause
            scene a7957 with dssa
            pause 
        scene a5709 with dssr
        play music "Music/Vesky - Departure.ogg" fadein 2
        b "Hmm."
        d "Mh?"
        scene a5710 with dssa
        b "We should have sex on the middle of this field one day."
        scene a5711 with dssa
        d "No sex talk today."
        scene a5712 with dssa
        pause 
        scene a5713 with dssa
        b "Let's climb up there." 
        scene a5714 with dssr
        pause 
        scene a5715 with dssr
        pause 
        scene a5716 with dssr
        pause 
        scene a5717 with dssr
        pause 
        scene a5718 with dssa 
        pause 
        scene a5719 with dssa
        pause  
        scene a5720 with dssr
        pause 
        play sound "Music/Sfx/Punch.ogg"
        scene a5721 with vpunch
        d "Don't do that!"
        "She giggles."
        scene a5722 with dssr
        d "Idiot!"
        scene a5725 with dssr 
        d "Stand with both feet on the ground."
        scene a5724 with dssa 
        b "I like it when you tell me what to do."
        scene a5725 with dssa 
        d "Since when?"
        scene a5723 with dssa 
        b "In a sexual sense, not in any other way."
        scene a5726 with dssa 
        d "Like what?"
        scene a5727 with dssa 
        b "*Whispers* Like... Ask me to bend over the railing..."
        scene a5728 with dssa 
        d "*Whispers* I'd rather have you stay as far away from the edge as possible."
        scene a5729 with dssa 
        b "*Sensual Whisper* Whyyy?"
        stop ambient fadeout 5
        stop music fadeout 9
        scene a5730 with dssa 
        d "*Whispers* Because I don't want to lose you."
        scene black with Dissolve(1.2)
        $ renpy.pause(0.2, hard=True)
        $ renpy.movie_cutscene("images/Animations/CH1-3/Honeymoon2a.webm", stop_music=False)
        $ persistent.Honeymoon = True
        play ambient "Music/Sfx/Ambient_Night_Suburban.ogg"
        scene a5731 with dssb
        pause 
        scene a5732 with dssr
        pause 
        "Thirty minutes passed without a single word being spoken."
        scene a5733 with dssa
        b "*Whispers* This is one of these moments, I'll never forget."
        scene a5734 with dssa
        pause 
        scene a5733 with dssa
        b "It's one of these moments where I feel anxious that this is just a dream..."
        b "That you're not really here with me... but you are..."
        scene a5735 with dssa
        b "Before my hormones make me confess my undying love..."
        b "This place goes on my list."
        scene a5736 with dssa
        d "Do you really have a list?"
        scene a5737 with dssa
        b "No, but we should write one together."
        scene a5738 with dssr
        b "I need to get home. I have a strict diet and need to eat."
        scene a5739 with dssr
        d "A cheese fry diet?" 
        b "I wish."
        scene a5740 with dssr
        b "I've been eating too much junk."
        scene a5741 with dssa
        b "I like to do soup only diets."
        b "I only eat soup for a few weeks until I can look at myself in the mirror again."
        scene a5743 with dssr
        pause 
        scene a5742 with dssa
        b "...Do you want some soup?"
        scene a5744 with dssa 
        d "Yeah."
        scene a5745 with dssr 
        pause 
        play sound "Music/Sfx/Punch.ogg"
        scene a5746 with vpunch
        d "Move with a bit more care up here!"
        scene a5747 with dssr
        b "Awww, you're soooo worried about me!"
        scene a5748 with dssa
        d "No. I would have a hard time explaining that I didn't kick you off this thing!"
        scene a5747 with dssa
        b "True."
        b "I'd scratch myself on the way down to give the illusion of a fight."
        scene a5748 with dssa 
        d "I go first."
        play sound "Music/Sfx/Punch.ogg"
        scene a5749 with vpunch #sfx 
        "You catch her after she jumps down the last few steps."
        scene a5750 with dssr
        pause 
        scene a5751 with dssa
        pause 
        scene black with Dissolve(2)
        with Pause(.5)
        jump BellchenSoup 

label BellchenSoup:
    $ BellaSoup = True
    $ play_playlist(playlist_BabyBellchen)
    scene a5752 with dssb 
    pause 
    d "Where's Amber?"
    scene a5753 with dssa
    b "No idea. Perhaps at work, on a date, or maybe she's fighting crime."
    b "One great thing about my Mom is, she doesn't ask me where I go every time I leave the house."
    b "And neither do I."
    scene a5754 with dssa
    pause 
    d "What kind of soup is it?"
    scene a5755 with dssa
    b "Todaaay uhhh- asparagus and mushroom cream soup."
    scene a5756 with dssr
    d "Does Amber make them for you?"
    scene a5757 with dssa
    b "What?"
    play sound "Music/Sfx/Punch4.ogg"
    scene a5758 with vpunch #sfx
    b "I cook them!"
    scene a5759 with dssr
    d "You? You want me to believe, that you spoiled, little brat can cook?"
    scene a5760 with vpunch
    b "You-"
    scene a5761 with dssr
    "She grabs her hairband and makes her hair into ponytail."
    scene a5762 with dssa
    d "Are you gonna fight me now?"
    scene a5763 with dssr
    b "Now you've done it..."
    scene a5764 with vpunch
    pause 
    scene a5765 with dssr
    pause 
    scene a5766 with vpunch
    pause 
    scene a5767 with vpunch
    d "Pay attention to the soup! It's boiling over!"
    scene a5768 with dssr
    pause
    scene a5769 with dssr
    b "I grew up without a father-"
    scene a5770 with dssa
    d "-I can tell. Continue."
    scene a5769 with dssa
    b "And my Mama worked a lot- so you stupid motherfucker-"
    scene a5771 with dssa
    b "I can cook!"
    scene a5772 with dssa
    b "I can cook you a steak so tender, you'll get a little wetspot in your pants."
    scene a5773 with dssa
    b "My soups? A culinary experience you won't find anywhere else."
    scene a5774 with dssa
    b "I'll make you some Tiramisu soon. You won't be the same person afterward... and-"
    play sound "Music/Sfx/Punch.ogg"
    scene a5775 with vpunch #sfx
    b "If you question my cooking talent again, I'll put you in the soup."
    scene a5776 with dssr
    pause 
    scene a5777 with dssr
    d "I refuse to believe that you can cook. It doesn't fit my headcanon of you."
    scene a5778 with dssr
    b "What's your headcanon of me?"
    scene a5779 with dssa
    menu:
        "Arrogant, dumb, and emotionally unregulated...":
            $ ADEU = True 
            scene a5780 with dssa
            b "You just described yourself, dude."
            scene a5781 with dssa
            d "I might be dumb and emotionally retarded, but I'm not arrogant."
            scene a5782 with dssa
            b "I don't think you realize how you look at people."
            b "You look at them from above. Like they're disgusting and beneath you."
            scene a5783 with dssa
            d "No way."
            scene a5784 with dssa
            b "Mmm- you do"
            scene a5785 with dssa 
            b "I, however, am much more likeable."
            scene a5786 with dssa
            "You chuckle."
            scene a5788 with dssr
            b "You'd be surprised how many people actually like me."
            scene a5789 with dssa
            b "I'm no bullshitter, and loyal to my friends."
            scene a5790 with dssa
            d "Are you loyal to me?"
            scene a5791 with dssa
            b "We're not friends."
            scene a5792 with dssr
            d "What are we?"
            if Bella_Fiancee is True:
                scene a5793 with vpunch
                b "Engaged! I'm your fiancée!"
                scene a5797 with dssa
                d "You sure are."
            else:
                scene a5794 with dssa
                b "You're only here to satisfy my needs." 
                scene a5795 with dssa
                d "And how am I doing so far?"
                scene a5796 with dssa
                b "Don't make me cry..."
        "Slutty, attentionseeking, and the emotional maturity of a four year old.":
            $ SAE = True 
            scene a5780 with dssa
            b "No, No, and maybe."
            scene a5781 with dssa
            d "You don't seek attention, huh?"
            scene a5780 with dssa
            b "No?"
            scene a5782 with dssa
            b "If you're as hot as me you'll get it, whether you want it or not."
            b "Every hot girl gets a lot of unwanted attention."
            scene a5785 with dssa 
            b "Yet... most just want the attention from someone special..."
            scene a5787 with dssr
            "She takes your hand."
            scene a5788 with dssa
            b "I hope, I'll find him someday." 
        "Misunderstood, good on the inside, but a lot of personal development is still in front of you.":
            $ MGL = True 
            scene a5781 with dssa
            pause 
            scene a5780 with dssa
            b "That's..."
            scene a5799 with dssr
            b "That's the gayest thing anyone has ever said to me."
            scene a5800 with dssa
            b "Wow."
            scene a5801 with dssa
            b "Don't get me wrong. I like it."
            scene a5800 with dssa
            b "But I'll be ordering a strapon, and from now on-"
            scene a5802 with dssa
            b "-you'll call me Mommy."
            scene a5785 with dssr 
            b "...A strapon."
            b "I'll order one and maybe we can have some fun with that... If you catch my drift..."
            scene a5786 with dssa
            d "You mean I strap-on a dildo and do you?"
            scene a5787 with dssr
            b "Yes."
            scene a5788 with dssa
            b "However, after what you just said, I'll be the one wearing it."
            scene a5786 with dssa
            d "You're just too insecure to take the compliment."
    scene a5798 with dssr
    pause 
    scene black with Dissolve(2)
    with Pause(.5)
    scene a5803 with dssb
    pause 
    scene a5804 with dssa
    d "It's some good soup."
    scene a5805 with dssr 
    "She smiles." 
    scene a5806 with dssa
    b "Do you want to stay the night?"
    scene a5805 with dssa
    d "Sure, why not..."
    scene a5807 with dssa
    b "I'm kidding. I just wanted to hear you say it for my ego."
    b "I need to mentally prepare for someone to stay the night."
    scene a5808 with dssa
    b "I'll drive you home soon, I'm getting really tired."
    scene a5809 with dssr 
    d "Do these soup diets work for you?"
    scene a5808 with dssr 
    b "Absolutely." 
    b "I can easily deal with hunger too."
    scene a5810 with dssr 
    b "I get cranky, sure... but I can get through it for days on end."
    scene a5811 with dssr 
    pause 
    scene a5812 with dssa
    pause 
    scene a5813 with dssr
    pause 
    stop music fadeout 10
    scene a5814 with dssa
    b "My sister is in a coma."
    scene a5825 with dssr 
    pause 
    scene a5826 with dssa 
    d "What?"
    scene a5815 with dssr 
    b "My sister has been in a coma for more than five years."
    $ MC_Knows_About_Heidi = True
    scene a5816 with dssa  
    d "Seriously?"
    b "Mhm."
    scene a5817 with dssa  
    d "This came out of nowhere."
    scene a5818 with dssa  
    b "It felt like the right time to say it."
    scene a5819 with dssr 
    d "I don't know what to say."
    scene a5820 with dssa  
    play music "Music/VeskyThinkingOfYou.ogg"
    b "I go over there multiple times a week and read to her... To tell her about my day."
    b "I told her about you..."
    scene a5821 with dssa  
    b "It would be great if you'd come with me some day... So she can hear your voice."
    scene a5822 with dssa 
    d "Is there... a chance for her to wake up?"
    scene a5821 with dssa  
    b "When she fell into a coma, they said there was a good chance she'd wake up again."
    scene a5820 with dssa  
    b "Five years later and she still hasn't woken up... But I know she's listening..."
    b "Sometimes her finger twitches... I know she's there."
    scene a5823 with dssr 
    pause 
    scene a5824 with dssa 
    b "She will wake up- and when that happens, I'll be there... I'll never leave her side again."
    scene a5827 with dssr  
    d "What's her name?"
    scene a5828 with dssa 
    b "Heidi."
    scene a5829 with dssa 
    d "Heidi Von Halen..."
    scene a5830 with dssr 
    d "How old is she?"
    scene a5831 with dssa 
    b "I'm a year older..."
    scene a5832 with dssa 
    d "I'm sure we'll find a day next week where we can visit her together."
    scene a5833 with dssa
    pause 
    scene a5834 with dssa
    d "I remember the stories you told me... About the little dares you gave each other."
    scene a5835 with dssa
    b "The spiderweb fries... Eww."
    scene a5836 with dssr
    pause 
    scene a5837 with dssa
    d "You're a cunt... a real pain in the ass... but I believe you'd be good big sister."
    stop music fadeout 10
    d "I'd love to meet Heidi... and thank you for telling me." 
    scene a5838 with dssa
    pause
    stop ambient fadeout 3
    scene black with Dissolve(2)
    with Pause(.5)
    play ambient "Music/Sfx/Summer_Morning.ogg" fadein 8
    scene a5839 with vpunch 
    pause
    d "(...Where am I?)"
    scene a5840 with dssa
    d "Bella?"
    scene a5841 with dssr
    pause 
    scene a5842 with dssa
    b "We slept in?"
    scene a5843 with dssa
    d "I don't even remember getting on the couch."
    scene a5844 with dssa
    b "Are you this bad of a kisser? Did you really kiss me to sleep?"
    scene a5846 with dssr
    am "Good morning."
    scene a5845 with dssa
    b "Mama?"
    scene a5846 with dssa
    am "Who else?"
    scene a5848 with dssr 
    am "I've made coffee and got us some bread rolls."
    scene a5847 with dssa
    b "Did you get me my croissants?"
    scene a5848 with dssa
    am "Of course."
    scene a5849 with dssa
    b "Thank you."
    scene a5850 with dssa 
    b "Let's freshen up."
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Smooth)
    scene a5915 with dssr
    pause 
    scene a5916 with dssr
    d "This is a nice bathroom."
    scene a5917 with dssr
    b "It's mine alone."
    scene a5918 with dssa
    d "This is mine."
    scene a5919 with dssa
    if Bella_PGU is True:
        b "Is it though?"
    else:
        b "You can't just say it's yours... You'll need to claim it first."
    scene a5920 with dssr
    pause 
    scene a5921 with dssr
    b "Check out the crown jewel... If you push it, you can fit six people inside."
    b "Eight, if some are missing limbs."
    scene a5922 with dssa
    d "Did you test it?"
    scene a5924 with dssr
    b "Yep. Nadia, Eva, Ayua, Ayua's sister, Nevi, and me."
    scene a5925 with dssa
    d "Who's Nevi?"
    scene a5926 with dssa
    b "She's a good friend from the tuner community."
    scene a5927 with dssa
    d "I see you have already found my replacement."
    scene a5923 with dssr
    b "My loyal friend..."
    scene a5928 with dssr
    b "We don't have time now, but I'd like to take a bath with you after the bar?"
    scene a5929 with dssa
    d "Sounds like a plan."
    scene a5930 with dssa 
    b "You can't believe how horny I am..."
    scene a5931 with dssa 
    d "Your friends noticed too."
    scene a5932 with dssa 
    b "I'm so on edge with you..."
    if Bella_OR_STG1 is True and Sanitized is False:
        scene a5933 with dssa 
        d "We're not exclusive."
        scene a5932 with dssa 
        b "I know, but I want you."
    scene a5934 with dssa 
    b "I hope after your pocket-rocket is fixed, I'll get to return the favor by letting you beg me for sex."
    scene a5935 with dssa
    d "I will never beg for sex."
    scene a5936 with dssr
    b "Not even as part of a roleplay?"
    scene a5937 with dssa
    menu:
        "That's different. If it's part of the act, sure.":
            $ Femdom_STG_1 = True 
            scene a5938 with dssa
            pause 
        "Not even then.":
            $ BNR +=1
            scene a5939 with dssa
            b "Aww..."
            scene a5940 with dssa
            b "Afraid someone could percieve you as unmanly, little boy?"
            scene a5941 with dssa
            b "*Childish voice* Do you need to prove to them what a man's man you are?"
            play sound "Music/Sfx/Punch.ogg"
            scene a5942 with vpunch
            pause
    scene a5943 with dssr 
    b "We're not yet there where I'll let you watch me pee."
    b "Unless that's the key to power your engine... if not, get out."
    scene a5944 with dssa
    pause 
    scene a5851 with slideleft
    d "Hey Amber."
    scene a5852 with dssa 
    am "Hello [name]."
    scene a5853 with dssr
    pause 
    scene a5854 with dssa 
    d "Are you surprised to see me?"
    scene a5855 with dssa 
    am "I knew I would eventually stumble upon you."
    am "I just wasn't sure if it would be with or without clothes." 
    scene a5856 with dssr 
    with Pause(.3)
    menu:
        "Tease Amber.":
            scene a5896 with dssr 
            d "I guess we met in the middle."
            d "But Amber... I'm your patient. You should wear clothes. I'm easily influenced by you."
            scene a5857 with vpunch 
            am "[name]! No- don't even joke about it!" 
            scene a5858 with dssr 
            am "I'll mark this down as a positive development."
            scene a5859 with dssa 
            d "How do you mean that?"
            scene a5860 with dssa 
            am "Did you make jokes like this with others before?"
            scene a5861 with dssa 
            d "Very rarely."
            scene a5860 with dssa 
            am "See? That's a positive. Even if it's morally questionable when done with me."
            scene a5862 with dssr
            with Pause(.3)
            menu:
                "I never really cared much for the moral highground.":
                    $ Amber_Moral_Highground = True 
                    scene a5863 with dssa
                    am "Having strong, personal principles is good."
                    scene a5864 with dssa
                    d "That's something different though, no?"
                    scene a5865 with dssa
                    am "S-"
                    scene a5866 with dssa
                    d "What's morally right and wrong is decided by society... or whatever group you mingle with. We don't have to agree with someone else's values."
                    d "Principles; are the values we chose for ourselves."
                    scene a5867 with dssa
                    am "Yes. What's your point?"
                    scene a5866 with dssa
                    d "Nothing. I was just talking out of my ass."
                    scene a5868 with dssa
                    "She laughs."
                    scene a5869 with dssa
                    d "(Why do I sound like Vanessa when she's trying to convince you of something weird?)"
                "Humor cares very little for someone elses morals.":
                    scene a5863 with dssa
                    am "That's true. But you should be mindful of who's in front of you, and if it's the right time."
        "Don't tease her.":
            pass 
    scene a5870 with dssr
    am "How are you feeling?"
    scene a5871 with dssa
    d "I feel okay."
    scene a5872 with dssa
    am "You don't look so okay." 
    scene a5871 with dssa
    d "I just got a lot on my mind, but I can't complain right now."
    scene a5873 with dssr
    d "I'll just take a coffee."
    scene a5874 with dssa
    am "Of course."
    scene a5875 with dssr
    d "Can I see you today?" 
    scene a5876 with dssa
    am "We have our trip the day after tomorrow."
    scene a5877 with dssa
    d "Yes, but... there's something I need to talk to you about... Preferably before I head to the bar."
    scene a5878 with dssa
    am "What's the topic?"
    scene a5879 with dssa
    d "Sex."
    scene a5880 with dssa
    am "I have a full calender today, but I'll see what I can do."
    scene a5877 with dssa
    d "Thanks." 
    scene a5881 with dssr
    pause 
    scene a5882 with dssa
    am "Did you two...?"
    scene a5883 with dssa
    d "No."
    scene a5884 with dssr
    pause 
    scene a5885 with dssa
    d "She told me about Heidi."
    scene a5887 with dssa
    am "That means a lot. She trusts you."
    scene a5888 with dssr 
    b "Are you talking about me?"
    scene a5889 with dssa 
    am "No."
    scene a5890 with dssa 
    pause
    scene a5891 with dssa 
    b "Eww." 
    play sound "Music/Sfx/Vibration_Phone.ogg"
    scene a5892 with dssr 
    pause #sfx phone 
    stop sound
    scene a5893 with dssr 
    d "Yes?"
    scene a5990 with dssr 
    n "Yo! Where are you!?"
    scene a5991 with dssa 
    d "At Bella's."
    scene a5992 with dssa 
    n "Ugh."
    n "Say bread roll if she's holding you hostage, and I'll call in an air strike!"
    scene a5993 with dssa 
    n "But listen, Mila called and she said she has a viewing for a house. Or Robin did get the appointment... I don't know..."
    scene a5994 with dssa 
    d "When?"
    scene a5993 with dssa 
    n "In twenty minutes."
    scene a5894 with dssr
    d "Alright."
    scene a5895 with dssr
    d "I need to leave soon."
    d "Can you drive me back?"
    scene a5897 with dssr 
    pause 
    scene a5898 with dssa 
    b "Why do you need to leave?"
    scene a5897 with dssa 
    d "We have a viewing for a student house." 
    scene a5876 with dssr
    am "Moving out will do you good. It builds character. You'll get more self sufficient." 
    scene a5899 with dssr
    d "When are you moving out?"
    scene a5900 with dssa 
    b "Never."
    b "I'm already fully self-sufficient."
    scene a5901 with dssa
    b "Right?"
    scene a5909 with dssr
    am "Yes, you are."
    am "You've been taking care of yourself for a few years now."
    scene a5910 with dssa
    d "She's not even a little bit of a burden?"
    scene a5911 with dssa 
    am "No, not at all."
    scene a5912 with dssa 
    am "I love having my baby here."
    am "She cleans, cooks, and helps with everything around the house."
    am "She's very handy too. She fixes the sink, electronics, and whatever else others might have to call a professional for."
    scene a5913 with dssa 
    am "I just wish..."
    scene a5904 with dssa
    am "...you would stop disassembling my car."
    scene a5902 with dssa
    b "It didn't accelerate the way it should and the clutch felt wiggly!"
    scene a5903 with dssa
    am "The car is fine. Stop touching it."
    scene a5904 with dssa 
    pause 
    scene a5902 with dssa
    b "Do you want me to get you a shirt?"
    scene a5903 with dssa
    am "As long as this is my house, I'll wear whatever the hell I want at breakfast."
    am "If you or your boyfriend got an issue with that, you're free to go eat in your room."
    scene a5902 with dssa
    b "I was just asking, jeez..."
    scene a5905 with dssr 
    b "Okay, let's go. I want to eat my croissant in peace without you eyesore around." 
    scene a5906 with dssa 
    d "Thanks for the coffee, Amber."
    scene a5945 with dssr
    am "Bye [name]."
    scene a5907 with dssr
    pause 
    scene a5908 with dssa #toast sfx
    pause 
    scene black with Dissolve(2)
    with Pause(.5)
    stop ambient fadeout 4
    jump AfterBellaHome1






    



label ZaraStars:
    $ ZaraStars5x5 = True 
    scene a5675 with dssb
    pause 
    scene a5676 with dssr
    pause
    menu:
        "Hold her hand.":
            $ ZaraStarsHand5x5 = True
            scene a5677 with dssa
            pause
            scene a5678 with dssr
            pause
            scene a5679 with dssr
            pause
            scene black with Dissolve(3)
            with Pause(.5)
        "Don't hold her hand.":
            scene a5679 with dssr
            pause
            scene black with Dissolve(3)
            with Pause(.5)
    jump Morning5x5







label Morning5x5:
    if ZaraStars5x5 is True:
        scene a5680 with dssb
        pause 
        scene a5681 with dssr
        pause 
        scene a5682 with dssa 
        pause 
        scene a5683 with dssr
        pause 
        scene a5684 with dssa 
        d "Hey."
        scene a5685 with dssr
        za "My body hurts... Au."
        scene a5686 with dssr
        za "Did we really spent the night here?"
        scene a5687 with dssa
        d "Yeah."
        scene a5688 with dssa
        pause 
        d "Mh?"
        scene a5689 with dssa
        za "It's just so crazy that we slept out here... So out of the ordinary that I find this quite cool."
        scene a5690 with vpunch
        za "Oh shit. We should get our stuff, I bet my Dad tried to call me."
        scene a5692 with slideleft
        pause 
        za "Yeah, we're coming home."
        scene a5691 with dssr
        pause
        scene a5693 with dssr
        pause
        if ZaraBBallTrust5x0 and ZaraStars5x5 is True:
            menu:
                "She's so pretty.":
                    $ ZaraInterested = True 
                    scene a5694 with dssr
                    pause 
                    scene a5695 with dssa 
                    pause
                "She's a good friend to have.":
                    $ ZaraFriends = True 
                    scene a5694 with dssr
                    pause 
                    scene a5695 with dssa 
                    pause
        scene a5696 with dssr
        pause 
        jump ZaraStarsHome1
    elif BellaSoup is True:
        jump AfterBellaHome1




label ZaraStarsHome1:
    scene black with Dissolve(2)
    with Pause(.5)
    scene a5946 with dssb
    za "When do we start with our little challenges?"
    scene a5947 with dssa
    d "After the tryouts. I'll have time to prepare then."
    scene a5946 with dssa
    za "But we'll do the tennis one soon, oki?"
    scene a5947 with dssa
    d "Let's do it last because you're an actual pro at it... I'd like to make you sweat at least a little bit."
    scene a5948 with dssa
    za "Which one do you wanna do first then?"
    scene a5949 with dssa
    d "How about we start with something like darts?"
    scene a5950 with vpunch
    za "Hell no! I've seen you throw stuff!"
    scene a5951 with dssa
    d "Hmm..."
    scene a5952 with dssa
    za "Football? I don't mean American Football."
    if BellaF_STG1 or BellaDate is True:
        scene a5951 with dssa
        d "(I could ask Bella for some tips there.)"
    scene a5953 with dssa
    d "What about swimming? Let's start with that."
    d "You'll easily outlast me, and it will improve my fitness for the other challenges."
    scene a5954 with dssr
    za "Yeah, I'll take a free one any day."
    scene a5955 with dssa
    d "I won't make it easy for you."
    scene a5956 with dssr
    za "If you did, I'd call the entire thing off."
    za "How does Sunday in one month sound?"
    scene a5957 with dssa
    d "You're on."
    scene a5958 with dssa
    pause 
    scene black with Dissolve(2)
    with Pause(.5) #swiper transition is besser
    scene a5959 with dssr
    pause 
    scene a5960 with dssr
    za "Do you want fly with me?"
    scene a5961 with dssa
    za "I have a little plane... If you want to we can take a little roundtrip together."
    za "We can ask Nami if she wants to join, too." 
    scene a5962 with dssa
    d "Sure, as long as you can get us down again safely."
    scene a5961 with dssa
    za "Oh, we'll get down again... I can't guarantee safely, though."
    scene a5963 with dssr
    nic "Where were you two? We were worried."
    scene a5964 with dssr
    va "I told you they were fine."
    scene a5965 with dssr
    va "Now... let's figure out who was right..."
    scene a5969 with dssr
    va "Nami's guess was that you two got kidnapped."
    scene a5966 with dssr
    va "My guess; you two went to a store, bought lube, ripped condoms, and a bottle of cheap wine... booked a cheap motel, to then do the horizontal tango."
    scene a5967 with dssa
    d "You're bo-"
    scene a5968 with dssa
    va "Nojiko's guess was-"
    scene a5970 with dssr
    d "Really Noji?"
    scene a5971 with dssr
    va "Nojiko's guess was that you two sat outside and talked through the entire night."
    scene a5966 with dssr
    va "Now... who was the closest?"
    scene a5972 with dssr
    n "You don't need to relive this traumatic experience, I know my boy fought the kidnappers off!"
    scene a5973 with dssa
    n "*Low voice* Who were they, huh? Germans? Mexicans?" 
    play sound "Music/Sfx/Punch.ogg"
    scene a5974 with vpunch
    n "*Gasps* Don't tell me... it was the Austrians?! I have had bad experiences with them."
    scene a5975 with dssr
    d "Which Austrians do you even know?"
    scene a5976 with dssa
    n "Oh, just one."
    scene a5977 with dssr
    za "Noji came closest."
    scene a5978 with vpunch 
    pause
    scene a5979 with dssr
    va "Nami? Didn't you want to talk to [name] about a call?"
    scene a5980 with dssa
    n "Uhhh..."
    scene a5981 with vpunch
    n "Oh! Right!"
    scene a5982 with dssr
    n "Yo [name]! Mila called! She and Robin got an appointment to a house viewing!"
    scene a5983 with dssa
    d "When?"
    scene a5984 with dssa
    n "That was ten minutes ago. They're waiting for us and I was about to leave without you."
    scene a5985 with dssa
    m "No you weren't. You were whini-"
    scene a5986 with dssa
    n "-Ehhh! Why are you backstabbing me like that?!"
    scene a5987 with dssa
    d "Alright... I'll take a quick shower and I'll join ya."
    scene a5988 with dssa
    za "Same here. I'll come with you guys."
    scene a5989 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    jump ShowerMorningNoji



label AfterBellaHome1:
    scene a5995 with dssb
    pause 
    scene a5996 with dssa
    n "Yo."
    scene a5997 with dssr
    d "Cheeto."
    scene a5998 with dssa
    n "You smell like disgusting bitch..."
    scene a5999 with dssr
    pause 
    scene a6000 with dssa
    d "I had some good croissants."
    scene a6001 with vpunch
    n "YOU'LL TAKE THAT BACK!"
    n "MY BOY WOULD NEVER WILLINGLY EAT CROISSANTS!"
    jump ZaraMorning5x5

# label StarsSolo:
#     scene a6025 with dssb
#     pause
#     scene a6026 with dssr
#     pause
#     scene a6027 with dssa
#     d "(My back hurts.)"
#     scene a6028 with dssa
#     pause
#     scene a6029 with dssa
#     d "(I should get my stuff, and take a bus home...)"
#     jump ZaraMorning5x5


label ShowerMorningNoji:
    play ambient "Music/Sfx/Summer_Morning.ogg"
    stop music fadeout 10
    scene a6008 with dssb
    pause 
    scene a6009 with dssr
    pause #knock 
    m "Can I come in?"
    play sound "Music/Sfx/DoorOpen.ogg"
    scene a6010 with dssa
    d "Yah."
    scene a6011 with dssa
    pause 
    scene a6012 with dssa
    m "Is everything okay?"
    scene a6014 with dssa
    d "Yeah, sure." 
    scene a6013 with dssa
    pause
    if Noji_Comfortable_Underwear is True:
        scene a6015 with dssr
    else:
        scene a6015a with dssr
    pause 
    m "Why didn't you come back home last night?"
    if BellaSoup is False:
        d "I just wanted to be outside for a while. It wasn't my intention to sleep there." 
    else:
        d "I should've called and said something. Sorry."
    if Noji_Comfortable_Underwear is True:
        scene a6016 with dssa
    else:
        scene a6016a with dssa
    m "Okay." 
    if Noji_Comfortable_Underwear is True:
        scene a6017 with dssa
    else:
        scene a6017a with dssa
    m "Have a nice day."
    if Noji_Comfortable_Underwear is True:
        scene a6018 with dssa
    else:
        scene a6018a with dssa
    d "Uh- any news regarding your house?"
    if Noji_Comfortable_Underwear is True:
        scene a6019 with dssa
    else:
        scene a6019a with dssa
    m "No, it will stay quarantined for a while."
    if Noji_Comfortable_Underwear is True:
        scene a6020 with dssa
    else:
        scene a6020a with dssa
    m "Why? Do you want to leave?"
    scene a6021 with dssr
    d "No, quite the opposite. I like it here."
    d "I just hope we're no burden to Nick."
    scene a6022 with dssa
    m "Don't worry."
    if ZaraStars5x5 and ZaraBBallTrust5x0 is True:
        m "You and Zara seem to be getting along pretty well."
        scene a6023 with dssa
        d "Yeah... I like her."
        scene a6024 with dssa
        m "That's great."
        scene a6022 with dssa
    m "I'll be at work soon. I don't think we'll see each other before tomorrow."
    m "Have fun tonight."
    scene a6023 with dssa
    d "Thanks... and try not to stab your co-workers." 
    scene a6008 with dssr
    if BellaSoup is False:
        d "(I'll give Amber a call in a bit... see if she can squeeze me in today.)"
        d "(I need to talk to her.)"
    
    stop music fadeout 5
    jump StudentHouse



label ZaraMorning5x5:
    scene a6002 with dssr
    za "Hi, what's up?" 
    za "Do we want to play a little tennis tournament?"
    scene a6003 with dssa
    n "We're about to go and check out a student house."
    scene a6004 with dssa
    d "I'll change and we can leave."
    scene a6005 with dssa
    za "No, no! You look tired! You should go to bed."
    scene a6006 with dssa
    "You two look at Zara."
    if BellaSoup is True:
        scene a6007 with dssa
        za "...I'll come with you."
        d "I'll take a quick shower."
        scene black with Dissolve(2)
        with Pause(.5)
    stop music fadeout 5
    jump ShowerMorningNoji


label StudentHouse:
    scene black with Dissolve(2)
    with Pause(.5)
    play ambient "Music/Sfx/Car_Drive_Night_Interior.ogg"
    scene a7826 with dssr
    pause 
    scene a7827 with dssa
    d "Let's put some groundrules down, Zara."
    scene a7828 with dssa
    pause
    scene a7829 with dssa
    za "I won't say anything."
    scene a7830 with dssa
    pause
    scene a7831 with dssa
    n "I'm so excited!"
    scene a7834 with dssr
    n "Oh wait."
    n "Coming from Zara's place, everything else will look like crap."
    scene a7832 with dssr
    za "And that's why-"
    scene a7833 with dssa
    d "Sshhh."
    scene a7835 with dssr
    pause
    scene a7836 with dssa
    za "Well... It has space for a car."
    scene a7837 with dssa
    pause 
    scene a7838 with dssa
    za "Hmm..." 
    stop ambient fadeout 4
    $ play_playlist(playlist_Smooth2)
    scene a6030 with dssb
    za "Yeah, I think I picked Nessi up from a party here."
    scene a6031 with dssr
    d "(Apparently we're not the only ones looking at the place.)"
    scene a6032 with dssa
    n "Yo, this looks... nice?"
    scene a6033 with dssr
    n "Hello!"
    scene a6034 with dssa
    pause
    scene a6035 with dssr
    n "Sasha?"
    scene a6036 with dssa
    sas "Yes?"
    scene a6035 with dssa
    n "I didn't recognize you with the cappy."
    n "Are you here with Robin?"
    scene a6037 with dssr
    sas "Yes. Hey. They're in the backyard."
    scene a6038 with dssr
    pause
    scene a6039 with dssr
    n "Yo!"
    scene a6048 with dssr
    mi "Hi Nami! I'm so glad you guys made it!"
    scene a6049 with dssa
    rob "Hi!"
    scene a6050 with dssr
    n "Hey Robocop!"
    scene a6051 with dssa
    rob "*Chuckles* Please don't call me that."
    scene a6040 with dssr
    pause
    scene a6041 with dssr
    d "Doesn't look too shabby."
    scene a6042 with dssa
    za "That's what the elites want you to think."
    scene a6043 with dssa
    d "What?"
    scene a6044 with dssa
    za "I don't know. It's something Nadia throws around a lot."
    scene a6045 with dssr 
    pause 
    scene a6046 with dssr
    pause 
    scene a6047 with dssr
    pause 
    scene a6052 with dssr
    if RobinOffHook5x0 is True:
        d "Hey."
        scene a6054 with dssa
        rob "Hey!"
        rob "How are you?"
        scene a6056 with dssa
        d "I'm fine. How about you?"
        scene a6055 with dssa
        rob "I'm fine too."
    else:
        d "Hi."
        scene a6053 with dssa
        rob "Hi."
    scene a6057 with dssr
    n "Is this a jacuzzi?"
    scene a6058 with dssr
    rob "No, it's not heated nor does it have any boosters."
    scene a6059 with dssa
    za "Ice baths!"
    scene a6060 with dssa
    rob "Hey Zara!"
    scene a6061 with dssa
    za "Hi! How's Kairos?"
    scene a6062 with dssr
    rob "Oh, he's doing fine."
    scene a6063 with dssa
    za "Is he coming with you?"
    scene a6064 with dssa
    rob "He stays at my Mom's for now."
    rob "But I'll bring Suzy with me."
    if CheetoBath is True:
        scene b24 with dssr
        pause
        scene b25 with dssr
        n "...Why are you ignoring me?"
        n "You know we don't have to play hide and seek here?"
        scene b26 with dssr
        d "I'm not ignoring you."
        scene b27 with dssr
        n "You haven't talked to me yesterday at all... At least not really."
        scene b28 with dssr
        d "Cheeto, us not talking for the majority of the day is the norm."
        d "We don't need to hang on each other all day."
        scene b29 with dssa
        d "That's what makes us work."
        scene b31 with dssa
        n "It might bother me because I want to spend some time with you."
        scene b35 with dssr
        n "Can we make a deal?"
        scene b34 with dssa
        d "That depends."
        scene b36 with dssa
        n "We don't need to talk... But at least touch me from time to time."
        scene b36 with dssa
        n "Like when you pass by me, grab my ass."
        scene b32 with dssr
        d "Deal."
        scene b34 with dssr
        d "We'll do something together soon."
        scene b33 with dssa
        n "I bet you say that to all the girls."
        if MilaDate or BellaDate or VicDate or NiaDate5x0 is True:
            scene b36 with dssa
            n "And Wait! You actually do!"
            scene b37 with dssa
            "You give her a peck on the head, well aware that it infuriates her even more."
    elif MilaSleep5x0 is True:
        scene a6066 with dssr
        d "Hey."
        scene a6065 with dssa
        mi "Hey."
        scene a6067 with dssa
        d "You look tall today."
        scene a6068 with dssa
        mi "Check these heels out, baby!"
        scene a6069 with vpunch
        "She 'accidentally' falls forward."
        scene a6070 with dssa
        d "How was work yesterday?"
        scene a6071 with dssa
        mi "It was okay. I can't complain." 
    else:
        scene a6066 with dssr
        d "Hey Mila."
        scene a6065 with dssa
        mi "Hey [name]!"
    scene a6072 with dssr 
    mi "It's finally becoming a reality... My own place."
    scene a6073 with dssa
    d "That you share with three weirdos."
    scene a6074 with dssa
    mi "Robin's not a weirdo, is she?"
    scene a6076 with dssa
    d "She's in the book club, she's definitely one."
    scene a6075 with dssa
    mi "I'll take you three weirdos anyday."
    scene a6077 with dssr
    rob "Has anyone seen Sasha?"
    scene a6078 with dssa
    n "She was in the living room."
    za "Yeah, on her phone."
    scene a6080 with dssr
    mi "Boy trouble?"
    scene a6079 with dssr
    rob "I don't think she has or will ever loose sleep because of a boy."
    scene a6081 with dssr
    mi "Now that we're all here, we should do a tour through the entire house."
    scene a6082 with dssr
    rob "The backyard!"
    scene a6083 with dssr
    rob "It's so cozy. We'll buy a big table and have a big BBQ here."
    scene a6084 with dssr
    mi "I can picture us on a cool, spring day... where we drink warm tea and discuss the latest gossip."
    scene a6085 with dssa
    rob "Yeesss!"
    scene a6086 with dssa
    mi "I'd love to try out gardening too. Put some cute, little flowers down."
    if MilaDate and Mila_Pussy is True or MilaDate and Mila_Bath_Pussy is True:
        scene a6087 with dssa
        d "Mmmh."
        scene a6088 with dssa
        mi "Mh?"
        scene a6089 with dssa
        d "I just pictured you in an overall with nothing underneath."
        scene a6090 with dssa
        mi "You'd like that, huh?"
        scene a6091 with dssa
        d "Maybe. I guess there's only one way to find out."  
        if RobinOffHook5x0 is True:
            scene a6092 with dssr
            rob "Can I see it too?"
            scene a6093 with dssa
            mi "*Laughs* Sure, but only if you put on one as well."
            scene a6094 with dssa
            rob "Deal!"
    scene a6095 with dssr
    n "During the winter, I'll bet that I can stay in the freezing pool longer than anyone else!"
    scene a6096 with dssa
    d "No, you can't."
    if ZaraStars5x5 is True:
        scene a6097 with dssr
        pause
        scene a6098 with dssa
        d "I can see us working out here."
        scene a6099 with dssa
        pause #sad 
        scene a6100 with dssa
        d "You... me... weights..."
        scene a6101 with dssa
        d "Followed by an ice bath..."
        scene a6102 with dssa
        d "Perhaps we can cuddle afterwards to get warm."
        scene a6103 with dssa
        za "Heeeey... Platonic cuddling only!"
        scene a6104 with dssa
        d "How does that work?"
        scene a6105 with dssa
        "She moves your hands up, both hands cupping her boobs."
        d "...And this is more platonic than before?"
        scene Zaranodding with dssa
        pause 
    scene a6107 with dssr
    d "What I've seen yet is much prettier than I expected."
    scene a6108 with dssa
    mi "...Yeah."
    scene a6109 with dssa
    mi "Too pretty..."
    scene a6119 with dssa
    rob "It's the Sensational Housing tier."
    rob "It's usually reserved for small, respected fraternities or valueable athletes."
    scene a6120 with dssa
    rob "*Mumbles* Or if you got a Mom with direct connections to ZPR... and Nami."
    rob "It has six bedrooms, three bathroom's, two kitchens a living room, a basement... Uhhh, I think that was it?"
    scene a6110 with dssr
    mi "...Oh. I had planned to look at the ones two tiers below."
    scene a6111 with dssa
    rob "Oh. I'm sorry."
    scene a6117 with dssr
    rob "Sorry guys. My Mom got me the appointment... I didn't know."
    scene a6118 with dssa
    rob "But Mila, she said this is the only house still available."
    scene a6112 with dssr
    d "How much more expensive is it?"
    scene a6113 with dssa
    mi "The Blossom house's are $1500."
    scene a6114 with vpunch
    n "I HAVE TO PAY $1500?!"
    scene a6115 with dssa
    d "Divide it by four, dumbass..."
    scene a6116 with dssa
    n "Oh. Right..."
    scene a6120 with dssr
    rob "This house is $3000. Usually, these places go for $5000 but thankfully, they reduced the price because a small, now dissolved fraternity ruined two of the bedrooms, as well as a kitchen."
    rob "They might get fixed later."
    scene a6121 with dssa
    mi "That means we could technically take in two more roommates to lower the price even further?"
    scene a6122 with dssa
    rob "Yes, in theory... However, I don't know if I want to live with five people." 
    scene a6123 with dssa
    rob "Three is cool... But five... ehhh, I don't know."
    scene a6124 with dssa
    d "I agree. Five people would be too much for me."
    scene a6125 with dssr
    mi "$750 each."
    scene a6130 with dssr
    pause 
    scene a6131 with dssa
    n "*Whisper* How are we going to pay for this?"
    scene a6132 with dssa
    d "...Don't remind me."
    scene a6133 with vpunch
    n "Yo! Easily doable for me and [name]!"
    play sound "Music/Sfx/Punch.ogg"
    scene a6134 with vpunch
    "You push her firmly."
    scene a6135 with dssa
    rob "That's reassuring." 
    scene a6126 with dssr
    mi "I mean... I can afford it."
    if MilaVenus4x5 is True:
        mi "And I might have some other financial opportunities around the corner."
    else:
        mi "My waitress job covers it but it's uncomfortably close."
    scene a6128 with dssa
    za "My Dad's firm sometimes looks for promising students."
    za "You would be working in the same field you're studying in... I could ask him?"
    scene a6127 with dssr
    mi "That would be awesome."
    scene a6129 with dssr
    rob "Let's first take a tour through this place and then we'll decide."
    scene a6136 with dssr
    pause
    scene a6137 with dssa
    d "You half baked roll! Do you mind telling me what that was about?"
    scene a6143 with dssr
    n "By putting us both in a position of absolute distress, it will make us work harder."
    scene a6144 with dssa
    d "You realize, you're putting Robin and Mila in a potentially very uncomfortable position?"
    scene a6145 with dssa
    n "And do you realize that the state has a small account for you? You'd know that if you had ever bothered showing up to their appointments."
    n "I think even Noji saved some money for you."
    scene a6146 with dssa
    d "What?"
    scene a6147 with dssa
    n "I sometimes ignore all decency and rummage through the belongings of others to see what they're up to and found some bank statements."
    n "I saw one with your name on it, a bank account number that only the state of wollust uses and it had enough to pay at least a year of your rent."
    scene a6148 with dssa
    n "And I think it's safe to assume, that Noji saved a bit for me... Because if she didn't, I'll kill myself in front of her."
    scene a6149 with dssa
    d "You got the trust fund."
    scene a6138 with vpunch
    n "Do you see the trust fund anywhere?!"
    n "Bitch! I don't get access to it unless-..."
    scene a6139 with dssa
    d "Unless?"
    scene a6140 with dssa
    n "Unless I move in with them, admit that I was in the wrong, get married at 21, and adapt to their dumb rules."
    scene a6141 with dssa
    n "WHICH I WON'T!"
    scene a6142 with dssa
    pause 
    if AnnaSTG2 is True:
        scene a6150 with dssa
        d "(I just remembered Anna from the bookclub...)"
        d "(Should I text her?)"
        menu:
            "Text Anna.":
                $ AnnaSTG3 = True
                "You send Anna a text."
            "Don't text Anna.":
                pass 
    play sound "Music/Sfx/Punch.ogg"
    scene a6151 with vpunch
    pause
    scene a6152 with dssr
    za "...$750 sounds like a lot of money. I know of a place that's free."
    scene a6153 with dssa
    d "I heard that place houses a psycho that'll wake you at 3:30 in the morning."
    scene a6154 with dssr
    n "So this is the living room?"
    scene a6155 with dssr
    stop music fadeout 5
    mi "Yes. It's so nice. I absolutely love how it looks."
    scene a6156 with dssr
    $ play_playlist(playlist_Girly3)
    rob "It's really spacey as well."
    scene a6157 with dssr
    rob "*Pretentious voice* Perchance we might hold here a rather pretentious wine tasting. What say you, m'lady?"
    scene a6158 with dssr
    pause 
    scene a6159 with dssa
    sas "Ok."
    scene a6160 with dssr
    rob "I like the silk curtains."
    scene a6161 with dssr
    mi "We'll put a TV here."
    scene a6162 with dssa
    n "We'll need a big TV for movie nights!"
    scene a6163 with dssa
    rob "Yes! Imagine us all watching horror movies together!"
    scene a6164 with dssr
    rob "Or cheesy romance movies!"
    scene a6166 with dssr
    n "I'd love it if we had girl-nights where we just watch the cheesiest romance slop."
    scene a6165 with dssr
    mi "I'd love that!"
    scene a6167 with dssr
    za "Can I come too?"
    scene a6168 with dssa
    mi "Of course!"
    scene a6169 with dssr
    if NiaVisit5x0 is True:
        d "(Nia and I could play Turoki here.)"
    else:
        pause 
    scene a6170 with dssa
    pause
    scene a6171 with dssa
    sas "I heard the dorm rooms are nice."
    scene a6172 with dssa
    d "Cool. You should get one."
    scene a6173 with dssa
    pause 
    scene a6174 with dssr
    n "Where do you turn on the light?"
    scene a6175 with dssr
    pause
    scene a6176 with dssr
    pause 
    scene a6177 with dssr
    rob "By the way... Are we all on the same page with cleanliness?"
    scene a6178 with dssa
    mi "I always keep my room tidy."
    scene a6179 with dssr
    n "I'm an absolute slob. Ants love me. I have fourteen pending marriage proposals from ants. I'm their queen!"
    if MilaDate is True:
        scene a6180 with dssa 
    else:
        scene a6180a with dssa 
    rob "Mmmm, we'll make it work."
    scene a6181 with dssr 
    n "Yo, there are a few topics we might want to discuss."
    scene a6182 with dssr 
    n "Like, what about- you know... dating?"
    scene a6183 with dssa 
    rob "What about it?"
    scene a6182 with dssa 
    n "Like, are we allowed to bring someone here?"
    scene a6184 with dssr
    rob "Yeah sure, why not?"
    scene a6186 with dssr 
    n "I don't know. Maybe somebody wouldn't like it."
    scene a6185 with dssa 
    rob "We're not going to live celibate because someone here has an issue with it."
    scene a6187 with dssa
    mi "We're normal people, not hermits... I've lived in a place where I'd never willingly bring anyone. I want the freedom to get laid in my own room."
    scene a6188 with dssa
    rob "Same."
    scene a6189 with dssr
    "They direct their attention towards you."
    scene a6190 with dssa
    d "What?"
    scene a6191 with dssa
    n "Give us some input. How do you see it?"
    scene a6192 with dssa
    d "As long as it's not too loud, I guess? And nobody does it in a room we all use."
    scene a6193 with dssa
    "Everyone's eyes meet for a split second." 
    scene a6194 with dssr
    n "Sure, sure- mmmh-"
    scene a6196 with dssr
    mi "Absolutely [name]. You're spot on!"
    scene a6195 with dssr
    rob "Mhmm! Mhmm! What they said!"
    scene a6197 with dssr
    sas "Get a blacklight."
    scene a6198 with dssr
    d "Oh God..."
    scene a6199 with dssr
    za "I know a place where you'd never have to witness this. Use a blacklight if you wish."
    scene a6200 with dssa
    za "Just... not in Nessi's room."
    if BellaNonExclusive5x0 is True:
        scene a6205 with dssr
        n "Oh! And we ban Bella from this place."
        scene a6206 with dssa
        n "The last I'd want to hear is her... Ugh!"
        n "I'd might become a nun if I ever saw her have sex."
        scene a6207 with dssr
        rob "I just pictured you and Bella having sex."
        scene a6208 with vpunch
        n "What the fuck is wrong with you Robin?!"
        scene a6209 with vpunch
        "Mila and Zara burst out laughing."
        scene a6201 with dssr
    else:
        scene a6201 with dssa
    za "*Whisper* Remember how quiet it was at my place?"
    scene a6202 with dssa
    za "*Whisper* Living with three girls is going to be loud... All those girly noises..."
    scene a6203 with dssa
    d "Girly noises?"
    scene a6202 with dssa
    za "You know? All the squeaking and the moaning..."
    scene a6203 with dssa
    d "You moan quite loudly when you train, you know that, right?"
    scene a6204 with dssa
    za "If you stay, we can moan loudly together."
    scene a6210 with dssr
    n "Yo Sasha, where do you live?"
    scene a6211 with dssa
    sas "Outside the city."
    scene a6210 with dssa
    n "Do you have your own place?"
    scene a6211 with dssa
    sas "I have an apartment in the center I sometimes use to crash."
    scene a6212 with dssa
    sas "But I don't live there. I live with my family."
    scene a6217 with dssr
    rob "Her apartment isn't far from the clubs and bars. It's perfect."
    scene a6218 with dssa
    rob "However, others use it more often than she does. I think five people have a key to it..."
    scene a6220 with dssr
    n "Everyone uses it to crash after partying?"
    scene a6213 with dssr
    sas "Mostly."
    scene a6216 with dssr
    rob "I think Alia uses it exclusively for sex."
    rob "Her sorority forbids guys in their house so she goes there."
    scene a6221 with dssr
    n "So it's a sex apartment?"
    scene a6223 with dssa
    d "You watch too much porn."
    scene a6219 with dssr
    rob "...It's kind of a sex apartment."
    scene a6221 with dssr
    n "Hah. I knew it."
    scene a6226 with dssr
    za "You girls should have orgies here without involving [name]."
    scene a6224 with dssr
    "Everyone just looks at Zara."
    scene a6227 with dssr
    d "You can do better than that."
    scene a6225 with dssr
    rob "I don't get it?" 
    scene a6227 with dssr
    d "She's trying to make me stay at hers."
    scene a6228 with dssa
    rob "Really?"
    scene a6229 with dssa
    za "We're training together and he's making it all so complicated!"
    scene a6230 with dssa
    d "I'm making it complicated?"
    if ZaraStars5x5 is True:
        play sound "Music/Sfx/Punch.ogg"
        scene a6231 with vpunch
        "She stabs you with her fingers between the shoulder and neck muscle."
        scene a6232 with dssr
    else:
        scene a6237 with dssr
    rob "To me it seems like, you and [name] might need a key to Sasha's apartment soon."
    "The girls chuckle."
    scene a6244 with dssr
    rob "Maybe we'll all strand there someday... I'm still sad that you fired the doorman."
    scene a6214 with dssr
    sas "The last thing I want is to be monitored even more."
    scene a6239 with dssr
    mi "It's crazy what some friends told me about the dorms... and what happens there..."
    scene a6241 with dssr
    n "Max said they're boring."
    scene a6244 with dssr
    rob "I have many friends that have been at ZPR for a while, and they say the dorm parties get pretty wild."
    scene a6245 with dssa
    rob "Daily life, however, is pretty boring there."
    scene a6240 with dssr
    n "I hope life gets a little more exciting now..."
    n "The craziest thing I've ever done was being nude in a jacuzzi with three others."
    scene a6242 with dssr
    n "If I finish college without a public scandal... without having shot someone, and without being credited with the invention of a new type of bread roll..."
    scene a6243 with dssa
    n "I failed in life."
    if ZaraStars5x5 is True:
        scene a6233 with dssr
    else:
        pass 
    d "As much as I enjoy listening to your chit chat... Shall we continue the tour?"
    scene a6215 with dssr
    sas "Yes. Before someone else tries to confess in euphemisms."
    if ZaraStars5x5 is True:
        scene a6234 with dssr
        pause 
        scene a6235 with dssa
        pause 
        scene a6236 with dssa
        pause 
        if MilaDate is True:
            scene a6246 with dssr 
            pause
    else:
        pass 
    scene a6247 with dssr 
    pause
    scene a6248 with dssa
    n "How would we handle cooking?"
    scene a6249 with dssa
    d "Everyone takes care of themselves unless we agreed on cooking together."
    scene a6250 with dssa
    n "Perfect."
    scene a6252 with dssr
    mi "I like the idea of us having a day where we'll always cook together."
    scene a6253 with dssr
    rob "Yes! A lasagna day!"
    scene a6254 with dssa
    mi "Perhaps we can cook together on weekends?"
    scene a6255 with dssr
    n "Yes, the more we cook together, the better."
    scene a6256 with dssa
    d "You lazy bum won't live of us."
    scene a6257 with dssr
    n "Hmm, does the fridge look big enough for all of us?"
    scene a6258 with dssa
    sas "You'd be surprised what you can squeeze in when you really try."
    scene a6259 with dssa
    n "*Quiet* Yo..."
    scene a6260 with dssr
    pause
    scene a6261 with dssr
    sas "Do you think he'll move in here?"
    scene a6262 with dssr
    za "...I hope not. Why do you ask?"
    scene a6263 with dssa
    sas "I care about Robin. I hope he doesn't become an issue."
    scene a6262 with dssa
    za "[name]'s not like that."
    scene a6278 with dssr
    sas "It's not the first time I've heard that."
    scene a6264 with dssr
    za "Why do you think I'd like him to stay at my place? I can train with him without having to worry that he going to pull some creepy shit."
    za "He has no interest in anything besides sports."
    scene a6277 with dssr
    sas "Are you sure about that? Guys pretend not to care all the time, and [name] strikes me as a manipulator."
    scene a6265 with dssr
    za "Did you forget I grew up with Nessi? I can spot manipulation a mile away."
    scene a6266 with dssa
    za "I'm 99 percent sure [name]'s not like that."
    if ZaraBBallTrust5x0 is True:
        scene a6267 with dssa
        za "...97 percent."
    scene a6268 with dssr
    mi "Tiny shrimps. Big shrimps. All shrimps."
    scene a6269 with dssa
    rob "For me it's salmon."
    scene a6272 with dssr
    n "I like fried fish on rolls."
    scene a6273 with dssr
    d "Oh... You better prepare for her stupid lectures about rolls."
    scene a6270 with dssr
    rob "I like bread rolls."
    scene a6271 with dssa
    d "She doesn't just like them."
    scene a6274 with dssr
    n "I am a roll."
    scene a6275 with dssr #augenzwicken
    rob "I really like crossaints too."
    pause 
    rob "What?"
    play sound "Music/Sfx/Punch5.ogg"
    scene a6276 with vpunch
    d "It's okay... Let it go." 
    scene a6279 with dssr
    n "It's good that we have a dishwasher too."
    n "I hated washing dishes!"
    scene a6280 with dssr
    pause 
    scene a6281 with dssa
    n "Don't say it."
    scene a6282 with dssa
    d "I didn't say anything."
    rob "Mh?"
    scene a6283 with dssr
    n "He was about to say there are five dishwashers here."
    scene a6284 with dssr
    d "I didn't even think that!"
    scene a6285 with dssa
    sas "He wanted to say it."
    scene a6286 with dssa
    d "Seriously? You too?"
    scene a6288 with dssr
    mi "You're such a misogynist, [name]."
    scene a6289 with dssa
    rob "The worst."
    scene a6290 with dssa
    n "Yeah, damn [name]."
    scene a6291 with dssa
    za "I thought more of you..."
    scene a6287 with dssr
    sas "I'm not surprised."
    scene a6292 with dssr
    "They chuckle."
    scene black with Dissolve(2)
    with Pause(.5)
    #text mit bathroom elegant
    scene b148 with dssb
    rob "I think there are three in total with one being an en-suite."
    scene b150a with dssr
    mi "I guess [name] gets one for himself so he doesn't accidentally run into one of us?"
    scene b149 with dssr
    rob "I don't mind it but sounds good."
    scene b151a with dssa
    mi "*Whisper* I just remembered Maja's sex toys."
    scene b152a with dssa
    n "Ohhh! Right! We can order toys without anyone knowing about it!"
    scene b153 with dssr
    rob "I feel you."
    scene b154 with dssa
    n "Oh, you too?"
    scene b153 with dssa
    rob "My Mom obviously has no issues with it but it's awkward when I forget to put one away and she sees it... I store most of mine at Sasha's apartment."
    scene b155 with dssa
    rob "Wow. It really has become a sex apartment."
    scene a6293 with vpunch
    sas "It's because everyone is stashing their stuff there!"
    sas "If I trip over one more remote-controlled egg I'm going to trash everything!"
    scene a6294 with dssa
    za "Poor [name]."
    scene b156 with dssr
    "Robin looks around to see if you are nearby."
    scene b157 with dssa
    rob "*Whisper* How do we handle it with [name]?"
    scene b158 with dssa
    rob "I mean... He's a boy... We are girls..."
    scene b159 with dssa
    n "So?"
    scene b160 with dssa
    rob "Mmm..."
    scene b163a with dssr
    rob "Sooo... Are we allowed to or is it better if nobody gets involved with him?"
    scene b164a with dssa
    if MilaSleep5x0 is True:
        mi "We shouldn't create such rules. Whatever happens, happens."
        scene b165a with dssa
        rob "Okay."
    else:
        mi "I get your point."
        scene b166a with dssa
        n "Same."
        scene b164a with dssa
        mi "But I still wouldn't like these rules."
        mi "If someone here gets closer to him... So be it."
        scene b166a with dssa
        n "Yeh, we're moving out to have less stupid rules... Not more."
    scene b167a with dssa
    n "But... Do you plan to bang [name]?"
    scene b168a with dssa
    rob "*Whisper* No! Not directly... I just want to make sure we're all on the same page."
    rob "I'm just worried about a potential fallout."
    scene b169a with dssa
    n "That's always a risk if you live with other people."
    scene b170 with dssr
    rob "Yes, but when feelings and sex are involved it can get really messy."
    scene a6301 with dssr
    sas "Robin's right. Separate the people you live with from the people you sleep with."
    scene b173 with dssa
    mi "It sounds so weird if you think about in the context of a husband and wife."
    scene b172 with dssa
    rob "We already decided that [name]'s fair game."
    scene b174 with dssa
    "Sasha says nothing, however, her eyes tell Robin all she needs to know."
    scene b175 with dssa
    if RobinOffHook5x0 is False:
        mi "I thought [name] doesn't like you that much?"
        scene b176 with dssa
        rob "...Is it it weird that it gets me even hotter?"
        scene b177 with dssa
        "Nami laughs."
    else:
        mi "I thought you had just made up with him."
        if RobinFavor5x0 is True:
            scene b178 with dssa
            rob "He said I owe him a favor."
            scene b179 with dssa
            rob "...Maybe he wants a blowjob?"
            play sound "Music/Sfx/Punch.ogg"
            scene b180 with vpunch
            "Nami, Robin and Mila burst out laughing."
            scene b181 with dssa
            n "*Laughs* What the hell, Robin?"
            scene b182 with dssa
            rob "Whaaaat?"
            rob "What else could he want from me?"
            scene b183 with dssa
            mi "Maybe he wants you to take care of the dishes for a month?"
            scene b184 with dssa
            rob "I'm not going to lie, I'd rather give him a blowjob."
            scene b185 with dssa
            n "Same."
            scene b186 with dssa
            pause
            scene b187 with dssa
            "They start laughing."
        else:
            scene b188 with dssa
            rob "Yes. And the next logical step is...?"
            scene b189 with dssa
            mi "Platonic friends and room mates?"
            scene b190 with dssa
            rob "Eww."
            scene b191 with vpunch
            "They burst out laughing."
    scene a6295 with dssr
    mi "Damn Robin."
    scene a6298 with dssr
    n "But you ladies worry for nothing. [name]'s not interested in casual flings."
    n "I would say nobody bangs him-"
    if RobinFavor5x0 is True:
        scene a6299 with dssr
        n "Or sucks him off-"
    scene a6300 with dssa
    n "For at least a few months."
    scene a6301 with dssa
    sas "Abstinence pacts in shared housing last about as long as hot water."
    if Mila_Bath_Pussy is True:
        scene a6296 with dssr
        mi "I can't agree to that." 
        scene a6297 with dssa
        rob "Ohhhhh... Why's that, huuuh?"
    scene black with Dissolve(2) 
    $ renpy.movie_cutscene("images/Animations/CH1-3/MainBathroom.webm", stop_music=False)
    scene a6303 with dssr
    sas "My advice..."
    scene a6304 with dssr
    pause 
    scene a6305 with dssr
    sas "Look for someone you're not living with unless you intend to be in a serious relationship."
    scene a6306 with dssr
    sas "In this case, look for someone more stable than [name]."
    scene a6307 with dssa
    n "I think you both might be a little pessimistic because of what happened at the book club?"
    scene a6308 with dssr
    rob "You're referencing the things that went down with Robert?"
    scene a6309 with dssa
    n "I guess? The one that hit on Sasha and couldn't accept a no."
    scene a6310 with dssa
    pause
    scene a6311 with dssa
    rob "There maaay be a bit more to it..."
    scene a6312 with dssa
    n "Oh?"
    scene a6313 with dssa
    rob "...She had to play batman."
    scene a6314 with dssa
    n "I don't understand?"
    scene a6315 with dssa
    sas "He was married and yet this imbecile had the audacity to hit on me."
    scene a6312 with dssa
    n "That I got."
    scene a6316 with dssa
    sas "Do you think it was an accident that his wife found out? That he slipped up?"
    scene a6317 with dssa
    sas "The married ones always talk like they've got nothing left to lose... Until they lose it."
    scene a6319 with dssa
    sas "While I ignored his advances at first, I played along for two weeks to collect evidence and revealed some of it to his wife."
    scene a6320 with dssa
    n "He must've been pissed."
    scene a6321 with dssa
    sas "Who cares what a cheater thinks? I have nothing but disgust for them."
    scene a6322 with dssr
    rob "Emilia likes to say: 'If you're going to be a slut, at least be an honest one.' And that includes man-sluts."
    scene a6323 with dssa
    n "Did Sasha show her the chats?"
    scene a6324 with dssa
    rob "She sent them to me and I fast forwarded them to Emilia, who then revealed them to her." 
    scene a6325 with dssa
    n "Wasn't there another man?"
    scene a6326 with dssa
    rob "Jerry."
    scene a6327 with dssr
    sas "Mhm."
    scene a6328 with dssr
    pause
    scene a6329 with dssa
    rob "The fabric is really nice..."
    scene a6330 with dssr
    n "How does this even happen? I've never heard or seen married people do that... at this rate... with the same person."
    scene a6331 with dssr
    sas "I don't know. I don't do anything."
    scene a6332 with dssa
    rob "*Quiet* Sure..."
    scene a6333 with dssr
    sas "What are you implying? I didn't even talk to them!"
    scene RobinSedLook with dssa
    pause 
    scene a6335 with dssa
    rob "This is what you do!"
    scene a6333 with dssr
    sas "You mean I look at people?"
    scene a6343 with dssr
    n "Ahhhh- yeah, I noticed that too."
    scene a6344 with dssa
    n "You uhh- You flash your eyelashes with that non-challant 'Fuck me' look."
    scene a6341 with dssr
    pause 
    scene a6342 with vpunch
    sas "What?!"
    scene a6336 with dssr
    rob "That's exactly it! It's the look you'd throw at a camera when you'd do a sensual model shoot."
    rob "You've adopted it into your daily life!"
    scene a6346 with dssr
    mi "It's true."
    scene a6337 with dssa
    pause
    scene a6338 with dssa
    rob "THERE SHE DID IT TO MILA!"
    scene a6339 with dssa
    sas "That's not true!"
    scene a6346 with dssr
    mi "I felt inclined to flirt with you just now..."
    scene a6345 with dssr
    n "You need to stop looking like a melancholic, slavik girl that misses big, grey soviet-style buildings."
    scene a6348 with dssr
    za "It's true. Some friends mentioned that you gave them a look they interpreted as flirtation and an invitation to talk."
    scene a6340 with dssr
    sas "I'll never look at people again."
    scene a6347 with dssr
    mi "You need to smile more, and not look like you're in a seductive perfume commercial."
    scene a6353 with dssr
    rob "Less resting bitch face and more-"
    scene a6354 with dssa
    pause 
    scene a6349 with dssr
    n "[name]? Has Sasha ever eye-fucked you?"
    scene a6351 with dssr
    pause 
    scene a6350 with dssr
    d "Everytime she looks at me, it feels like she's moments away from stabbing me."
    scene a6352 with dssr
    sas "Thank you. At least someone's on my side."
    scene a6355 with dssr
    rob "Anyway..."
    rob "Jerry and his wife Macha were in the club for only two months."
    scene a6356 with dssa
    rob "I think she's schizophrenic?"
    scene a6357 with dssa
    sas "I don't think she was professionally diagnosed."
    n "What did she do?"
    scene a6358 with dssa
    rob "She was convinced her husband had an affair with Sasha."
    scene a6359 with dssa
    rob "Didn't she also say that you were pregnant?"
    scene a6360 with dssa
    sas "It appears that I'm so remarkably fertile that the sheer act of looking at me could somehow lead to pregnancy."
    scene a6361 with dssr
    rob "Perhaps you really do have an extraordinary level of fertility... Kelly was right."
    scene a6362 with dssa
    sas "I don't think she's handling childlessness very well."
    scene a6363 with dssr
    sas "Macha also said, that someone used scissors to cut up her dress or spike her wine..."
    sas "The list is endless."
    scene a6364 with dssr
    rob "I'm pretty sure Jenna spiked her wine with Luv once."
    rob "Remember when she started sweating and got very handsy with her husband?"
    scene a6397 with dssr
    n "What's Luv?"
    scene a6398 with dssa
    mi "A semi-legal drug."
    scene a6365 with dssr
    rob "Yup. A party drug."
    scene a6366 with dssa
    n "What does it do?"
    scene a6365 with dssa
    rob "It gets you really horny."
    rob "I heard some athletes use it before games to get a little extra push. Apparently it improves oxygen- something."
    scene a6394 with dssa
    za "That's true."
    za "Not that I tried it- but I know it does."
    scene a6396 with dssr
    n "Did you try it?"
    scene a6367 with dssr
    rob "A few friends and I tried it a year ago just for fun. Just us girls to see how it feels."
    scene a6368 with dssa
    n "And?"
    scene a6369 with dssa
    rob "You'll need a new panty afterward. By the end, it feels like you're a single touch away from- you know... meeting God..."
    scene a6370 with dssa
    rob "But I don't recommend doing this with people..."
    scene a6371 with vpunch
    rob "-that leave you hanging!"
    scene a6372 with dssa
    sas "Shut up Robin..."
    scene a6399 with dssr
    mi "*Chuckles* Oh God..."
    scene a6395 with dssr
    n "Did you touch each other?"
    scene a6373 with dssa
    sas "No. We made that very clear from the beginning."
    scene a6374 with dssa
    sas "Some are just a little... slow." 
    scene a6375 with dssr
    rob "You should read Kelly's version of-"
    scene a6376 with dssa
    sas "What?"
    scene a6377 with dssa
    rob "N-nothing."
    scene a6378 with vpunch
    sas "I told you to stop encouraging her to write smut stories about me!"
    scene a6382 with dssr
    rob "I stopped! I swear! The last few were with me as the main character!"
    scene a6400 with dssr
    n "What stories? I need some details!"
    scene a6379 with dssr
    sas "*Grumbles* The last one included a group scene with her church group, and an entire chapter from the POV of a carrot with anger issues."
    scene a6380 with dssa
    sas "Do you want me to spill some tea about you for once?"
    sas "You hit on Jerry after the rumors started."
    scene a6381 with dssa
    rob "I felt left out! Nobody ever tells rumors about me!"
    scene a6383 with dssr
    rob "I'm the ugly duckling next to you!"
    scene a6384 with dssa
    pause 
    scene a6385 with dssa
    rob "Say 'No! You're not.'"
    scene a6386 with dssa
    pause 
    if RoRum is True:
        n "The rumor with [name]?"
        scene a6385 with dssr
        rob "Yeah! My first!"
        scene a6406 with dssr
        rob "Bless you, [name]."
        scene a6387 with dssa
    else:
        scene a6388 with dssa
    sas "Yet I caught all the flak."
    scene a6385 with dssr
    rob "That's why you swallow."
    play sound "Music/Sfx/Punch.ogg"
    scene a6389 with vpunch
    sas "That's it. Go stand in the corner!"
    scene a6391 with dssr
    pause
    scene a6392 with dssr
    d "Viewing a house should take tops thirty minutes..."
    scene a6393 with dssa
    d "I should've known it would turn into a multi-hour chore with them..."
    scene a6401 with dssr
    n "I want to read Kelly's stories."
    scene a6402 with dssr
    rob "They're so good and filthy. I'll hand you a copy but beware... You'll need an extra long shower afterward."
    rob "And now that [name]'s there. Kelly won't be able to resist adding him to some of her stories."
    scene a6405 with dssr
    n "Would she write me one too?"
    scene a6403 with dssr
    rob "She wants a hundred bucks for a story. But I'm sure you can get a sample for free."
    n "It's sounds like I'm about to buy drugs." 
    scene a6404 with dssa
    rob "They are better than drugs."
    if BellaDate is True:
        scene a6407 with dssr
        d "(I could ask Kelly for a little story with me and Bella. I'm sure she would appreciate a little present...)"
        d "(And Kelly must know Bella from when she was at the book club... The visual descriptions should be on point.)"
        if ZaraStars5x5 is True:
            $ Kelly_Zara_Story = True 
            scene a6408 with dssr
            za "What are you thinking about?"
            scene a6410 with dssa
            d "I'll ask Kelly for a story about us."
            scene a6409 with dssa
            pause 
            scene a6408 with dssa
            za "Okay."
    if Victoria_Smut_Books is True:
        scene a6407 with dssa
        d "(I bet Victoria would love a story from Kelly.)"
        d "(I'll definitely ask Kelly the next time I see her)"
    scene black with Dissolve(2)
    $ renpy.movie_cutscene("images/Animations/CH1-3/Bibi_Intro_Minimalist.webm", stop_music=False)
    scene a6411 with dssr
    rob "The current book club constellation is probably the healthiest it has ever been."
    scene a6412 with dssr
    sas "[name]'s a new wildcard."
    scene a6413 with dssr
    rob "Let's be real, every single person in there is in some way a wild card."
    scene a6424 with dssr
    n "I'll keep him in check."
    scene a6414 with dssr
    rob "My Mom said that she didn't like him."
    rob "...Which means he's probably alright."
    scene a6415 with dssa
    n "Your Mom's a little-"
    scene a6416 with dssa
    rob "She's lovely. She's always been there for me."
    scene a6417 with dssa
    rob "No matter how long she had worked the previous day. 30 hours with no sleep? It doesn't matter. She'd still show up at my theater performance."
    scene a6418 with dssa
    n "Where's the but?"
    scene a6419 with dssa
    rob "But she can be exhausting. She always needs to be in the right and works a lot and... *Sigh*."
    scene a6420 with dssa
    rob "She's a politican and sometimes, it really shows."
    scene a6419 with dssa
    rob "But give her some time and she'll come around on [name]. He's got a backbone. She respects that."
    scene a6421 with dssa
    rob "Jerry she actually disliked. He had no spine."
    scene a6423 with dssa
    n "Did you like him? Considering you hit on him?"
    scene a6422 with dssr
    rob "I didn't mind him. I don't judge people, but I had zero romantic interest."
    rob "I only did it for fun."
    scene a6425 with dssr
    pause 
    scene a6426 with dssa
    rob "What?"
    play sound "Music/Sfx/DoorOpen.ogg"
    scene a6427 with vpunch #sfx
    with Pause(.5) 
    play sound "Music/Sfx/Punch.ogg"
    scene a6428 with vpunch
    with Pause(.5) 
    play sound "Music/Sfx/BodyFall.ogg"
    scene a6429 with vpunch
    pause
    play sound "Music/Sfx/DoorOpen.ogg"
    scene a6430 with dssr 
    "She gently closes the door."
    scene a6439 with dssr 
    za "No. You turn it this way."
    scene a6446 with dssr 
    d "No? This way."
    scene a6447 with dssa 
    za "Righty tighty, lefty loosely!"
    scene a6448 with dssa 
    d "I've been turning it left!"
    scene a6449 with dssa 
    za "Try the other left!"
    scene a6440 with vpunch 
    d "I'VE TRIED THE OTHER LEFT!"
    scene a6441 with vpunch 
    za "NNGGHH!"
    scene a6442 with dssa 
    "Mila walks over and unlocks it with the press of a button."
    scene a6443 with dssr 
    pause  
    scene a6445 with dssr 
    mi "What do you say?"
    scene a6444 with dssr 
    both "Thank you Mila." #both
    scene a6431 with dssr 
    pause
    if SashaBook5x0 is True:
        scene a6432 with dssa 
        d "I started with your book."
        scene a6433 with dssa
        sas "My book?"
        scene a6434 with dssa
        d "It's Only Love."
        scene a6433 with dssa
        sas "Oh. I see."
    scene a6435 with dssa
    pause 
    play sound "Music/Sfx/DoorOpen.ogg"
    scene a6436 with dssa
    pause 
    play sound "Music/Sfx/Punch4.ogg"
    scene a6437 with vpunch
    pause 
    play sound "Music/Sfx/DoorSlam.ogg"
    scene a6438 with vpunch
    pause 
    scene a6450 with dssr
    n "This bathroom doesn't have a real shower." 
    scene a6451 with dssa 
    mi "We'll have to figure out the logistics along the way."
    scene a6452 with dssr 
    pause 
    scene a6453 with dssa 
    mi "It's big enough, though."
    scene a6469 with dssr 
    n "Hop in [name]."
    scene a6454 with dssr 
    pause 
    if RaceWithImpossibleOdds is True:
        if ZaraStars5x5 is True:
            scene a6455 with dssr 
            "Zara walks up with the intention to sit on you in the tub." 
            scene a6456 with dssa 
            "But the Cheeto snatches the spot on your lap." 
        else:
            scene a6456 with dssa 
            pause
        scene a6457 with dssr 
        n "Three fit."
        pause 
    elif ZaraStars5x5 is True:
        scene a6459 with dssr
        pause 
        mi "That makes three."
    else:
        scene a6458 with dssr 
        mi "I bet we could fit a third one."
    scene a6460 with dssr 
    d "I mean, you can technically layer as many people on top as you want."
    scene a6461 with dssr 
    n "We could fit two couples in there."
    scene a6462 with dssr 
    mi "That sounds a lot like something you'd hear in a swingerclub."
    if MilaDate is True:
        scene a6463 with dssr 
        mi "New first date idea [name]."
        scene a6464 with dssr 
        mi "Swingerclub."
        scene a6465 with dssr 
        d "Mhm, sure."
    scene a6466 with dssr
    n "What's even in there? A toilet?"
    play sound "Music/Sfx/DoorOpen.ogg"
    scene a6467 with dssr
    pause 
    scene a6468 with dssr
    rob "...Help."
    scene black with Dissolve(2)
    with Pause(.5)
    jump WG_Bedrooms

label WG_Bedrooms:
    pause 
    scene a6470 with dssr
    mi "I assume this is the first bedroom."
    scene a6471 with dssr
    n "I like it."
    scene a6472 with dssa
    d "It's much bigger than what we have."
    scene a6474 with dssa
    n "Right. Your room is really small."
    scene a6473 with dssa
    d "Small? I live in a closet."
    scene a6475 with dssr
    mi "And you're not even a wizard."
    scene a6476 with dssr
    pause
    scene a6477 with dssa
    za "Imagine you had you own bathroom. En Suite..."
    scene a6478 with dssa
    d "I praise your tenacity."
    scene a6479 with dssa
    za "...Would you stay if we slept with each other?"
    scene a6480 with dssa
    d "No. That would make me want to leave."
    scene a6481 with dssa
    pause
    scene a6482 with dssa
    pause
    scene a6483 with dssa
    pause 
    scene black with Dissolve(1)
    with Pause(.5)
    #room 2
    pause 
    scene a6484 with dssr
    sas "I need at least twenty centimeters."
    scene a6485 with dssr
    za "...What are you ladies talking about?"
    scene a6486 with dssa
    sas "Extra leg room on a plane before it becomes unbearable."
    scene a6487 with dssa
    za "Ohhh, you're quite tall. I can see that."
    scene a6488 with dssr
    sas "Don't you have a plane?"
    scene a6489 with dssr
    za "Yes."
    scene a6494 with dssr
    mi "You do?"
    scene a6495 with dssa
    za "Riiight Mila... Didn't you want to be a pilot?"
    scene a6496 with dssa
    mi "Hobby-pilot, yeah. I don't want to work as one, though."
    scene a6490 with dssr
    za "Give me a date, time and we can go fly."
    scene a6497 with dssr
    mi "Really?"
    scene a6498 with dssa
    za "Yeah!"
    scene a6490 with dssr
    za "I've been looking for people who dare fly with me!"
    scene a6491 with dssa
    mi "'Dare'?"
    scene a6492 with dssa
    za "Don't ask."
    scene a6493 with dssr
    za "I can get you the number of the club where I got my license."
    scene a6498 with dssr
    mi "How much did it cost."
    scene a6499 with dssa
    za "It didn't come cheap. You should have 10 to 20 grand."
    scene a6500 with dssr
    mi "Ouuuch..."
    scene a6501 with dssa
    mi "I'll definitely take you up on the flying offer, though!"
    scene a6502 with dssa
    pause
    scene a6503 with dssa
    pause 
    scene a6504 with dssr
    za "They were talking about penis size."
    scene a6505 with dssa
    d "Yeah... I expect to hear lot of about these topics."
    scene a6506 with dssa
    za "I told them yours is small."
    scene a6507 with dssa
    d "That's okay. Let it all out."
    scene a6508 with dssa
    pause 
    scene a6509 with dssr
    za "You need to stay with me. With me you will have the most platonic relationship you could ever wish for."
    scene a6510 with dssa
    za "No sex talk, no touching."
    scene a6512 with dssa
    d "...You're driving a hard bargain."
    if ZaraBBallTrust5x0 is True:
        scene a6511 with dssa
        d "The no touching part I don't believe though."
        scene a6513 with dssa
        za "Okay- there might be an occasional hug coming your way."
        scene a6514 with dssa
        d "A hug is the precursor to penis talk."
        scene a6515 with dssa
        d "And then there's Vanessa who will definitely talk about sex and penises."
        scene a6516 with dssa
        za "Damn it Nessi..."
        scene a6517 with dssa
        d "And you sit on me a lot... Nude. Whenever we are in the jaccuzzi, you creep closer and closer."
        scene a6518 with vpunch
        za "That's a lie!"
        scene a6519 with dssa
        d "When I told you about my plans of moving out, you sat on me!"
        scene a6520 with dssa
        za "That's so not-"
        scene a6521 with dssa
        za "Yep. I did that."
    scene a6529 with dssr
    rob "We're moving on!"
    if ZaraStars5x5 is True:
        scene a6522 with dssr
        d "Spell it with me."
        scene a6523 with dssa
        d "P. L. A. T. O. N. I. C."
        d "Platonic."
        scene a6524 with dssa
        za "P. L. A. T. O. N. I. C."
        scene a6525 with dssa
        za "Plat- your dick in my ass."
        scene a6526 with vpunch
        "Zara burst out laughing."
        d "Why would YOU say that..."
        scene a6527 with dssa
        za "*Laughs* For shock value!"
        scene a6528 with dssr
        "She keeps giggling into your shoulder."
    jump Room3


label Room3:
    scene black with Dissolve(2)
    with Pause(.5)
    scene a6530 with dssr
    n "Hmm..."
    scene a6531 with dssa
    n "I like this bedroom."
    scene a6532 with dssa
    rob "It's a little too dark for my taste."
    scene a6533 with dssa
    n "I like that. I hate when the sun shines in when I'm gaming."
    n "I like to pretend there's no outside world."
    scene a6534 with dssr
    mi "I guess this is your room then, Nami?"
    scene a6535 with dssa
    rob "I'm cool with it."
    scene a6536 with dssa
    d "We'll decide later."
    scene a6537 with dssr
    pause
    scene a6538 with dssa
    n "You know what..."
    scene a6539 with dssa
    mi "Mh?"
    scene a6541 with dssa
    n "I thought Sasha was too stuck up to wear a top like this..."
    scene a6540 with dssa
    mi "I know she likes short skirts. I never got the feeling that she's stuck up."
    scene a6542 with dssa
    "Robin laughs."
    scene a6543 with dssr
    rob "I'm so excited!" 
    scene a6544 with dssa
    rob "I'm going to be living without supervision!"
    scene a6547 with dssr
    sas "Maybe this was a bad idea."
    play sound "Music/Sfx/Punch.ogg"
    scene a6545 with vpunch
    rob "Nothing can stop me now, Sasha!"
    rob "We can have wine tastings for as long as we want!"
    rob "We can discuss the latest smut book for as long and as in much detail as we want!"
    scene a6548 with dssr
    n "Yo, count me in!"
    scene a6545 with dssa
    rob "I can bring boys over! SASHA!"
    play sound "Music/Sfx/Punch.ogg"
    scene a6549 with vpunch
    rob "BOYS!"
    scene a6546 with dssr
    sas "I'm calling your Mom before you star under the headline 'College pregnancy' in three month's newspaper."
    scene a6550 with dssr
    mi "I'm going to have my hands full with them."
    scene a6551 with dssa
    pause
    scene a6552 with dssa
    mi "...Yes, with them too."
    scene a6553 with dssa
    za "You've been taking care of Vic, right?"
    scene a6554 with dssa
    mi "She can take care of herself, but yes, I'll help her whenever I can."
    scene a6553 with dssa
    za "That's really nice of you."
    scene a6555 with dssr
    mi "[name]'s helping her too."
    scene a6556 with dssr
    za "She mentioned that he was with her yesterday."
    scene a6557 with dssa
    mi "You and Vic are still in contact?"
    scene a6556 with dssa
    za "Of course! I called her yesterday to ask how the session went."
    scene a6559 with dssr
    mi "Be a little more mindful, she's quite tense lately."
    mi "Don't take it the wrong way if she insults you or tries to push you away."
    scene a6558 with dssr
    za "Ohh- I see... I guess it's natural to be fed up with everything at some point."
    scene a6559 with dssr
    mi "I hope it's just a phase. I can easily look past it, but others might not."
    scene a6560 with dssa
    mi "I hope she won't cause any long term damage to her relationships."
    scene a6561 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene a6562 with dssr
    n "Yep. This is my room."
    scene a6563 with dssa
    n "Thanks for participating y'all!"
    scene a6564 with dssa
    d "Keep dreaming. Your claim is by far the weakest."
    scene a6565 with dssa
    n "I add a lot to this group!"
    scene a6566 with dssa
    rob "This is by far the coolest room."
    scene a6567 with vpunch
    rob "No way!"
    scene a6571 with dssr
    rob "It has its own little garden!"
    scene a6568 with vpunch
    mi "Dibs on the room!"
    scene a6569 with dssa
    n "Forget it! I called dibs first!"
    scene a6570 with dssr
    d "We'll draw straws later."
    scene a6572 with dssr
    pause
    scene a6573 with dssr
    rob "*Quiet* This is beautiful..."
    scene a6574 with dssr
    pause 
    scene a6575 with dssr
    n "Yo! An unopened bottle of Gin!"
    scene a6576 with dssr
    rob "The bar opening is tonight... Who wants to start early and inaugurate our new place?"
    scene a6577 with dssa
    sas "Don't count your chickens until they hatch... wait until the contract is signed."
    scene a6578 with dssr
    rob "The other bathrooms don't seem to have a bidet."
    scene a6579 with dssa
    n "Are those the things that shoot water up your butt?"
    scene a6580 with dssr
    rob "*Laughs* Not up your butt. At the butthole."
    scene a6586 with dssr
    n "Hmm..."
    scene a6587 with dssa
    n "I don't trust it!"
    scene a6590 with dssr
    mi "They're great."
    scene a6588 with dssr
    n "What if it goes up your butt?"
    scene a6581 with dssr
    rob "*Chuckles* It's not an enema, Nami."
    scene a6590 with dssr
    mi "But if it goes up your butt, you've got all the preparation for anal done."
    scene a6589 with dssr
    n "We've gotta stop by that sex toy shop Maja goes to."
    scene a6581 with dssr
    rob "A friend of Sasha's Dad owns a porn studio. They have a huge array of new toys that they sell under the hand."
    rob "Sasha and I got quite a few high end toys there for very cheap."
    scene a6582 with dssa
    rob "I'll let you know you when we go there again."
    play sound "Music/Sfx/Punch4.ogg"
    scene a6583 with vpunch 
    pause 
    scene a6584 with dssa
    sas "Could you not talk about this particular topic in public? Or at least leave my name out?"
    scene a6585 with dssa
    rob "...Sorry."
    scene a6591 with dssr
    za "I feel left out."
    scene a6592 with dssa
    za "What are you talking about?"
    scene a6593 with dssa
    n "Anal sex."
    scene a6594 with dssa
    za "Cool... Cool... All I know is that some lifters use plugs."
    scene a6596 with dssa
    n "Why?"
    scene a6595 with dssa
    za "I'm not so sure."
    scene a6597 with dssa
    with Pause(.3)
    scene a6598 with dssa
    pause
    scene a6599 with dssr
    pause
    scene a6600 with dssa
    pause
    if MilaSleep5x0 is True:
        scene a6601 with dssr
        mi "Hey you."
        scene a6602 with dssa
        d "Hey."
        scene a6603 with dssr
        mi "How are you?"
        scene a6604 with dssa
        d "I'm fine. A little bit of backpain from sleeping on the basketball court."
        scene a6605 with dssa
        mi "*Laughs* Why did you sleep at a basketball court?"
        scene a6606 with dssa
        d "Long story." 
        scene a6607 with dssa
        pause
    if MilaVenus is True:
        scene a6605 with dssa
        mi "Follow me."
        jump MilaVenusImages
    else:
        scene a6680 with dssr
        pause
        scene a6681 with dssr
        pause
        scene a6682 with dssr
        n "This is a whole lot better than I thought it would be."
        scene a6683 with dssa
        d "Same."
        d "And if it's true what you said, we should be able to afford it too."
        scene a6684 with dssr
        n "Yah."
        if NamiDate is True:
            scene a6685 with dssr
            pause 
        scene a6686 with dssr
        n "I'll get a job... *Sigh*."
        n "Maybe I become be a bartender."
        scene a6687 with vpunch
        n "Dude, we should open a bar!"
        scene a6688 with vpunch
        n "A TIDDY BAR!"
        pause 
        scene a6689 with dssr
        d "Maybe there's a way to get your trustfund without having to move in with them?"
        scene a6690 with dssa
        n "I don't think there is."
        scene a6689 with dssa
        d "What if you move in, get the trustfund, and move out again?"
        scene a6690 with dssa
        n "That sounds too good to be true."
        scene a6692 with dssa
        pause
        scene a6691 with dssa
        n "...I'll make it work."
        if NamiDate or RaceWithImpossibleOdds is True:
            scene a6693 with dssa
            d "We'll make it work."
            scene a6694 with dssa
            pause
    jump WGContinue
    

label MilaVenusImages:
    $ MilaVenusImagesS2_1x0 = True
    scene a6608 with dssr 
    pause 
    scene a6609 with dssr 
    mi "This garden is so beautiful."
    scene a6610 with dssa
    d "I don't know how it looks at your place-"
    scene a6612 with dssr
    mi "Totally different worlds, [name]."
    scene a6613 with dssa
    pause 
    scene a6614 with dssa
    mi "Could you take a picture of me?"
    scene a6615 with dssa
    d "For Aurora?"
    scene a6611 with dssa
    mi "For Aurora and Venus."
    d "Sure."
    scene a6616 with dssr
    pause
    d "Relax your shoulders. You look stiff."
    scene a6617 with dssa
    if Mila_Bath_Pussy is True:
        mi "At least one of us."
        d "Ouch."
    else:
        mi "Better?"
    scene a6618 with dssr #flash
    pause 
    scene a6620 with dssr 
    pause
    scene a6619 with dssa
    pause #flash 
    scene a6621 with dssr 
    pause 
    scene a6622 with dssr
    pause
    d "Can we help you?"
    scene a6623 with dssr 
    sas "Are those for Venus?"
    scene a6675 with dssr 
    "You wait for Mila to answer."
    scene a6676 with dssa
    mi "Yes."
    scene a6624 with dssr 
    "Sasha casually grabs your phone and looks at the images."
    scene a6625 with dssa 
    "She says nothing but shakes her head."
    scene a6673 with dssr
    sas "What does this photo tell you?"
    scene a6674 with dssa
    d "...She's got a great ass?"
    scene a6626 with dssr 
    sas "Who?"
    sas "I don't see a face."
    scene a6677 with dssr
    mi "I didn't feel comfortable showing my face."
    scene a6627 with dssr 
    sas "Then don't do Venus. You will regret it."
    scene a6678 with dssr
    pause 
    scene a6679 with dssa
    mi "I want to do it."
    scene a6628 with dssr 
    sas "With everything in life, it's either 'Hell yeah' or 'Nah'." 
    scene a6629 with dssa
    sas "And if you don't go hell yeah when you think about Venus, then don't do it."
    play sound "Music/Sfx/Camera.ogg"
    scene a6630 with dssr 
    play sound "Music/Sfx/Camera.ogg"
    pause
    scene a6633 with dssr 
    sas "Here."
    scene a6631 with dssr 
    pause
    scene a6632 with dssr
    sas "This gives the image some personality. It makes clear that it's really you."
    sas "It ensures that you stand out as an individual, rather than blending into a sea of indistinguishable bodies."
    scene a6634 with dssa
    if Sasha_Deranged and SashaBook5x0 and RobinOffHook5x0 is True:
        play sound "Music/Sfx/CameraQuiet.ogg"
    sas "You've got a big chest? A great ass? A pretty face?"
    scene a6635 with dssr 
    sas "So do a million others."
    if Sasha_Deranged is True:
        scene a6636 with dssr 
    else:
        scene a6637a with dssr 
    sas "Do you want him to take more photos of you in the future?"
    if Sasha_Deranged is True:
        scene a6636a with dssr 
    else:
        scene a6637 with dssr 
    mi "Yes."
    scene a6638 with dssr 
    sas "Then pay attention to the angles I choose, [name]."
    scene a6639 with dssa
    sas "You can look at my model photos too. Study the angles my photographer used."
    scene a6641 with dssa
    d "Nah, casual looks the best."
    scene a6642 with dssr
    sas "Sloppy camera work is neither original nor artistic."
    pause
    scene a6643 with dssr
    pause
    scene a6643a with dssa
    pause
    play sound "Music/Sfx/Camera.ogg"
    scene a6644 with dssa
    sas "If you want to earn a substantial amount, you should take one additional picture that shows a lot more."
    scene a6645 with dssa
    sas "You can share the ones you prefer on your main feed, and offer the explicit image as a reasonably priced pay-per-view."
    scene a6646 with dssr
    d "Are you on Venus?"
    scene a6647 with dssa
    sas "Every ZPR model has to be on Venus. However, I don't post there. A friend does it for me. Tasteful pictures, only. The income gets donated to charity."
    scene a6648 with dssa
    d "Why would a college, of all the institutions, require their models to be on an erotic site?"
    scene a6647 with dssa
    sas "Venus is used mostly for erotic content, but that's not its whole purpose."
    sas "Besides, Venus is owned by the same people that back ZPR."
    scene a6649 with dssa
    mi "Thanks for the pointers."
    if Sasha_Deranged and RobinOffHook5x0 is True:
        scene a6650 with dssr 
    else:
        scene a6651 with dssa 
    "Sasha gives her a cute smile, and hands you your phone back."
    scene a6652 with dssr
    pause
    scene a6653 with dssa
    d "I'll see if I can improve my photography skill a little."
    scene a6654 with dssr
    mi "That's nice."
    scene a6655 with dssa
    mi "Our sex tape will look great."
    scene a6656 with dssa
    pause
    scene black with Dissolve(2)
    with Pause
    jump WGContinue

label WGContinue:
    scene a6657 with dssr
    pause
    scene a6658 with dssr
    rob "Aaaah..."
    play sound "Music/Sfx/Punch.ogg"
    scene a6659 with vpunch
    rob "Hey! No!"
    scene a6660 with dssa
    sas "...How much did she drink?"
    scene a6664 with dssa
    za "She swallowed a big load."
    scene a6661 with dssr
    sas "Why are all my friends alcoholics?"
    play sound "Music/Sfx/Punch.ogg"
    scene a6662 with vpunch
    rob "I'm not an alcoholic!"
    scene a6663 with dssa
    rob "I'm a connoisseur of fine spirits."
    scene a6665 with dssr
    d "How about we finish the tour before you people get hammered?"
    scene a6666 with dssa
    n "How about we continue the tour hammered?"
    scene a6667 with dssa
    rob "I like the way Nami thinks."
    scene a6668 with dssa
    pause #kiss sfx 
    scene a6669 with dssr 
    pause
    scene a6670 with dssr
    d "How about we stay home tonight, workout, and watch benchpress PR videos together?"
    scene a6671 with dssa
    za "You know I'd like that, but I promised Nadia to be there."
    scene a6672 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene a6695 with dssb
    pause
    scene a6696 with dssr
    za "How will we handle training when you live here?"
    scene a6697 with dssa
    d "I'll come over and-"
    scene a6698 with dssr
    za "At 3:30 in the morning?"
    scene a6699 with dssa
    d "No. We train at normal times."
    scene a6700 with vpunch
    za "My times!"
    scene a6701 with dssa
    za "How far is it from here to me?"
    scene a6715 with dssr
    mi "Twenty minutes."
    scene a6716 with dssr
    za "On foot?"
    scene a6717 with dssa
    mi "With the bus."
    scene a6702 with dssr
    za "Meaning... I can probably do it in twenty-five."
    scene a6703 with dssa
    d "What are you getting at?"
    scene a6704 with dssa
    za "Three times a week, I'll run over here and we'll get sweaty together."
    scene a6703 with dssa
    d "Let's just meet at the gym, girl..."
    scene a6705 with dssa
    za "Screw you and your gym!"
    za "I'm the coach! I'll make the rules! We're going to train at four in the morning."
    scene a6706 with dssa
    d "I'll look for someone else to train me."
    scene a6707 with dssa
    za "No! We have a contract."
    scene a6708 with dssa
    d "No, we don't."
    scene a6709 with dssa
    za "Yes, we do! A verbal contract!"
    scene a6710 with dssr
    pause 
    scene a6711 with dssa
    za "...5:30?"
    scene a6712 with dssa
    d "Fine..."
    scene a6711 with dssa
    za "You weakling."
    scene a6713 with dssr
    d "And we either train at the gym or your place. We'll need equipment."
    if ZaraStars5x5 is True:
        scene a6714 with dssa
        za "Am I not enough equipment for you?"
    if MilaDate is True:
        scene a6718 with dssr
        mi "Maybe you should write him a plan he can do on his own?"
        scene a6704 with dssr
        za "Nooo, I need to be there to correct him. Aaaand to motivate him!"
        scene a6719 with dssr
        mi "As soon as he's got the technique down, he should be fine?"
        scene a6720 with dssr
        za "Nooo, as a coach I gotta be there."
    scene a6723 with dssr
    n "Zara... I have a scientific question."
    scene a6724 with dssa
    d "...Here we go."
    scene a6725 with dssa
    n "Does sex count as cardio?"
    scene a6714 with dssr
    za "No. Sex is comparable to raking leaves in oxygen consumption."
    scene a6728 with dssr
    sas "Men usually spend more energy thinking about sex than the act itself."
    scene a6725 with dssr
    n "Even if you go like really hard at each other for an hour or two?"
    scene a6726 with dssr
    rob "Show me a guy who can do it for an hour or two and maybe you've got a point."
    scene a6721 with dssr
    mi "Your kitty might also want a word after two hours of straight humping."
    scene a6722 with dssa
    n "Challenge accepted."
    scene a6728 with dssr
    sas "This house got a big basement."
    scene a6727 with dssa
    rob "It's just a basement. We don't need to look at it."
    scene a6728 with dssa
    sas "No. The basement is more than just a basement. I once attended a party here."
    scene a6727 with dssa
    rob "When?"
    scene a6728 with dssa
    sas "Dwight was invited and he sneaked me out."
    scene a6727 with dssa
    rob "How old were you?"
    scene a6728 with dssa
    sas "Sixteen."
    scene a6729 with dssa
    rob "Okay. Let's take a look."
    scene black with Dissolve(2)
    with Pause(.5)
    scene b208 with dssb
    pause
    n "...So, where's the light switch?"
    scene b209 with dssa
    pause
    scene b210 with dssr
    pause
    scene b211 with dssa
    "Your hands touch and intertwine as you both reach for the light switch."
    scene b213 with dssa
    if RobinOffHook5x0 is False:
        "But instead of removing her hand, she stares at you as if you had just killed a puppy."
        menu:
            "Remove your hand.":
                pass
            "Don't remove your hand.":
                scene b214 with dssr
                pause
                scene b215 with dssa
                pause
                scene a6735 with dssr
                n "What's she doing?"
                scene a6736 with dssa
                rob "Usually, all she has to do is hold eye contact, and the guy stops whatever he's doing."
                scene a6737 with dssa
                rob "The most famous example... She made a guy cry just by looking at him."
                scene a6739 with dssr
                n "What? She made a guy cry just by looking at him?"
                scene a6741 with dssa
                rob "Yeah. She felt bad for him afterward."
                scene a6742 with dssa
                rob "*Whisper* She might say she doesn't stare on purpose, but I say she does... I think she tests people that way."
                scene a6740 with dssa
                n "She might've met her match then. [name]'s a rock."
                scene b215 with dssr
                pause
                if BellaEyeContactWin2x0 is True:
                    d "Listen, I already went through this with Bella."
                    scene b216 with dssa
                    sas "Then let go of my hand."
                else:
                    scene b216 with dssa
                    sas "Let go of my hand."
                scene b217 with dssr
                d "Your hand is on top of mine."
                scene b218 with dssa
                sas "You're holding my thumb."
                scene a962 with dssa
                d "I'm not holding your thumb."
                scene a963 with dssa
                sas "Look at-"
                play sound "Music/Sfx/Slap.ogg"
                scene a964 with vpunch
                pause
                scene a965 with dssr
                za "Seriously?"
                scene a966 with dssr
                d "What's your problem?"
                scene a967 with dssa
                sas "Honestly? I don't think too highly of you after your performance at the book club."
                scene a968 with dssa
                sas "But-"
                scene a969 with dssa
                d "And Charlie's not at fault?"
                scene a970 with dssa
                sas "Of course she is, nonetheless you could've handled it better."
                scene a971 with dssa
                if SashaSit5x0 is True:
                    d "You're a funny one."
                    scene a972 with dssa
                    "She rolls her eyes."
                    scene a971 with dssa
                    d "You said it yourself. No matter who might dare to lay rules upon me... And yet here you are, using the same moral compass those use who laid rules upon you."
                    scene a972 with dssa
                    d "You don't always have to do the right thing."
                    d "And I'm sure you're a prime example of that."
                    d "So please, don't be such a hypocrite. Our precious Foreign minister had it coming."
                else:
                    d "You don't always have to do the right thing."
                    scene a972 with dssa
                    "She rolls her eyes."
                scene a970 with dssa
                sas "This is not just about Charlie."
                scene a6730 with dssr
                n "...Why are you holding my arm?"
                scene a6731 with dssa
                rob "I'm nervous. I don't want to see them fight."
                scene a6730 with dssa
                n "I didn't see them fighting."
                scene a6732 with dssa
                rob "What? Didn't you see the intensity in their eyes?!"
                scene a6733 with dssa
                n "Damn, Robin. In what wonderland did you grow up? [name] looks at me like that every day."
                n "They were respectful. Nobody got too personal."
                scene a6734 with dssa
                rob "I just want harmony between us all... I really hate it when there's tension in the air."
                scene b261 with dssr
                d "Then what's it about?"
                scene b260 with dssa
                sas "Robin."
                scene b261 with dssa
                d "Robin... Oh... Seriously?"
                scene b262 with dssa
                pause
                scene b263 with dssa
                d "I have no issues with Robin. She's not going to be my best friend, but that's about it."
                scene b264 with dssr
                d "I'm not that petty."
                scene b265 with dssr
                pause
                scene b266 with dssr
                rob "Is everything okay?"
                scene b267 with dssa
                sas "Your butt looks weird today."
                scene b268 with vpunch
                rob "*High-pitched* W-what?!"
                scene b269 with dssr
                pause
                scene b270a with vpunch
                rob "Naaami! Zaaara!"
                scene b271 with dssr
                rob "Do I have a bad ass day?"
                scene b272 with dssr
                pause
                za "Hard to say with these leather shorts... But I'd say you have a decent day."
                scene b273 with dssr
                n "Yeah, if you wanted to sit on someone's face, they wouldn't object."
                scene b274 with dssa
                "Robin lets out a sigh of relief."
    else:
        pause
        scene a6743 with dssr
        "She looks at you awkwardly, yet stern."
        d "What?"
        scene a6744 with dssa
        sas "Nothing."
        scene a6745 with dssa
        d "Are you so afraid of being touched."
        scene a6747 with dssa
        sas "No? But like most people, I'd like to choose who touches me."
        scene a6746 with dssa
        d "You're making a big fuss out of nothing."
        scene a6748 with dssr
        with Pause(.3)
        menu:
            "Touch her hand while she walks away.":
                $ SashaHandTouchTease = True
                scene a6749 with dssr
                pause
                scene a6750 with dssr
                sas "Seriously?"
                scene a6751 with dssa
                "You chuckle."
                scene a6752 with dssa
                sas "You don't take me serious?"
                scene a6753 with dssa
                d "I do. Well, mostly. I just found it funny."
                scene a6752 with dssa
                sas "I didn't."
                scene a6753 with dssa
                d "That's a 'you' problem."
                play sound "Music/Sfx/Kick1.ogg"
                scene a6754 with vpunch
                pause
                play sound "Music/Sfx/Kick2.ogg"
                scene a6755 with vpunch
                "Your left leg gives out and you drop to the ground."
                scene a6756 with dssr
                sas "Now it's a 'you' problem."
                if NamiDate is True:
                    n "YO!"
                    pause 
                    pause 
                    n "Carry on." 
                scene a6757 with dssa
                d "...That hurt a lot more than I thought it would."
                scene a6756 with dssa
                sas "Pain is an excellent teacher."
                scene a6758 with dssa
                sas "I hope for your sake, that you're not a slow learner."
                scene a6760 with dssr
                pause 
                scene a6759 with dssa
                d "...I can't get up."
                scene a6761 with dssr
                pause
                scene a6762 with dssr
                pause 
                scene a6763 with dssa
                d "Do you think this was a propotionate response?"
                scene a6764 with dssa
                sas "I've always wanted to kick someone untrained."
                scene a6765 with dssa
                sas "Besides, you deserved it."
                scene a6766 with dssa
                d "I could sue you and pay my rent that way."
                scene a6767 with dssa 
                sas "A stiff cucumber like you would benefit from some mobility."
                menu:
                    "Can you give me some pointers?":
                        scene a6768 with dssa
                        $ SashaMobi = True 
                        sas "No."
                    "Don't ask her.":
                        pass
                scene a6769 with dssa 
                d "Can Ayua kick this hard as well?"
                scene a6770 with dssa 
                sas "No."
                if Sasha_Deranged is True:
                    scene a6771 with dssr
                    sas "She punches really hard."
                    scene a6772 with dssa 
                    sas "I have stronger and longer legs." 
                scene a6773 with dssr 
                "Your leg recovered enough for you to stand on it again." 
                scene a6774 with dssa 
                pause 
                scene a6775 with dssr 
                pause
                scene a6776 with dssa 
                pause
                play sound "Music/Sfx/Kick1.ogg"
                scene a6777 with vpunch 
                d "Argh!"
                scene a6778 with dssr 
                d "You- f-fucking b-bitch!"
                scene a6779 with dssa 
                pause
                scene a6780 with dssa 
                d "*Moaning* You'll pay for that..."
            "Let her walk away.":
                scene a6782 with dssr
                rob "Don't provoke her."
                rob "You never want to be on the recieving end of her nipple twisters."
                scene a6781 with dssr
                rob "They hurt so much."
    scene black with Dissolve(2)
    with Pause(.5)
    scene a6783 with dssb
    pause 
    if SashaHandTouchTease is True:
        scene a6786 with dssr
        pause
        scene a6785 with dssa
        sas "You don't seem very convinced."
        scene a6786 with dssa
        d "They're all a little loud. I don't like that."
        scene a6785 with dssa
        sas "I can relate. Which is why I'd never live with other people."
        scene a6787 with dssa
        sas "You should look into the single dorm rooms. There aren't many but maybe you get lucky."
        scene a6784 with dssr
        d "We were just talking about noise and you recommend me a dorm?"
        d "You really want to get rid of me, don't you?"
        scene a6785 with dssr
        sas "It might sound like it but I'm not."
        scene a6788 with dssa
        d "I've heard from sources that you're anti male."
        scene a6789 with dssa
        sas "People come up with the wildest tales."
        scene a6790 with dssa
        za "I've heard it too."
        scene a6791 with dssr
        sas "Shouldn't you know better, considering I'm good friends with Vanessa?"
        scene a6803 with dssr
        za "I don't talk with her about you or anyone else really."
        scene a6804 with dssa
        za "Guys come up with so much bullshit."
        scene a6805 with dssa
        d "Guys? Have you heard the rumors girls spread?"
        scene a6806 with vpunch
        za "What? Guys are so much worse!"
        scene a6807 with dssr
        za "There's even a rumor, spread by some butthurt guy, that Nadia never dates, in order to save what little of his dignity is still left."
        if RoRum is True:
            scene a6808 with dssa
            d "You know the Robin and me rumors. All spread by girls."
        scene a6792 with dssr
        sas "I don't think gender plays a role."
        sas "People like [name] assume I'm misandrist because of rumors. That's how it spreads."
        scene a6793 with dssa
        d "Not rumors. It's how you present yourself."
        scene a6792 with dssa
        sas "Good. Makes it easier to filter out the ones who think they're an exception."
        scene a6809 with dssr
        za "You do come across a little cold. A friend of mine said he once asked you out and you just walked away without saying a word." 
        za "Like- I get not wanting to be hit on all the time... But it was rude."
        scene a6794 with dssr
        sas "What was his name?"
        scene a6795 with dssa
        za "David."
        scene a6796 with dssa
        sas "Perhaps he shouldn't have led with touching my lower back."
        scene a6797 with dssa
        sas "He approached me like a guy who's only known dating from WormTube. I did us both a favor."
        za "He didn't mention that part."
        scene a6798 with dssa
        sas "It's simple really. There's guys that you want to be touched by, and there's a majority you don't want to touch you."
        scene a6799 with dssa
        za "Truer words have never been spoken."
        scene a6800 with dssr
        sas "Yet somehow, it's always the wrong ones who test the theory."
        scene a6810 with dssr
        za "I think you and [name] could work together."
        scene a6811 with dssa
        d "No?"
        scene a6810 with dssa
        za "Yes. You both appear rather cold. In some regards, you're quite similar."
        scene a6801 with dssr
        sas "If I wanted an unhinged roller coaster of emotions with no payoff, I'd read a book on gender studies."
        scene a6802 with dssa
        pause
        scene a6812 with dssr
        za "Sorry, I tried to get you an opening."
        scene a6813 with dssa
        d "Please don't try to be my wingman."
        if ZaraBBallTrust5x0 is True:
            scene a6814 with dssr
            za "My bad. We need to focus on training."
            za "There's no time for love in our lives!"
            scene a6815 with dssa
            d "Exactly. See, we're more alike than Sasha and I."
            menu:
                "Put your arm around her lower back.":
                    $ ZaraLowerBack = True
                    scene a6816 with dssa
                    pause
                    scene a6817 with dssa
                    za "Wow. The old lower-back technique that got my friend burned."
                    scene a6818 with dssa
                    d "Are you going to walk away now?"
                    scene a6819 with dssa
                    za "Not yet."
                    scene a6820 with dssa
                    "Your hand moves down to her ass."
                    scene a6821 with dssa
                    za "Now I'm walking away."
                    scene a6822 with dssr
                    "Zara chuckles as she tip toes away."
                "Don't do it.":
                    pass
    scene a6823 with dssr
    rob "Keep in mind guys, they're going to move most of the furniture out before we move in."
    scene a6824 with dssa
    d "We could build a little gym here."
    scene a6825 with dssa
    rob "Airhockey! I love airhockey!"
    scene a6828 with dssr
    n "Are we going to have a house warming party?"
    scene a6827 with dssr
    rob "Yes!"
    scene a6830 with dssr
    mi "Sure."
    scene a6831 with dssa
    d "Do we have to?"
    scene a6832 with dssa
    mi "Don't be a party pooper. We'll have a nice little party with some friends."
    scene a6829 with dssr
    n "Friends, booze, rolls... What more do you want?"
    scene a6826 with dssr
    rob "Hot guys? Because the hot girls are already included."
    scene a6833 with dssr
    pause
    scene a6834 with dssa
    d "Don't say anything."
    scene a6835 with dssa
    "She laughs."
    scene a6836 with dssa
    za "I don't need to say anything. They do it all for me."
    scene a6837 with dssr
    pause
    scene a6838 with dssa
    rob "How come you made it here after all?"
    scene a6839 with dssr
    sas "You asked me fourteen times to come with you?"
    scene a6840 with dssa
    rob "Yeah, but you said no fourteen times."
    scene a6841 with dssa
    sas "Katie didn't show up in time, so I left."
    scene a6842 with dssa
    sas "I took her experimental piece with me. She's going to call me later and cuss me out."
    scene a6843 with dssa
    rob "I like the underboob. It's pretty."
    scene a6844 with dssa
    pause
    scene a6845 with dssa
    pause 
    scene a6846 with dssa
    rob "...Really pretty."
    scene a6847 with dssa
    pause
    scene a6848 with dssa
    sas "No."
    play sound "Music/Sfx/Punch4.ogg"
    scene a6849 with vpunch
    rob "Pleaaase!"
    scene a6850 with dssa
    sas "We're not switching outfits."
    scene a6851 with vpunch
    rob "Please, please, please!"
    scene a6852 with dssa
    sas "Robin. No."
    scene a6853 with vpunch
    rob "You owe me!"
    scene a6854 with dssa
    sas "No! I don't owe you!"
    scene a6855 with dssa
    pause
    play sound "Music/Sfx/Punch4.ogg"
    scene a6856 with vpunch
    rob "PLEAAAASE!"
    scene a6857 with slideleft
    sas "You're lucky I still had some pasties in my purse."
    scene a6858 with dssr
    rob "*High pitched voice* I'm hooot!"
    rob "I need to be careful not to flash anyone."
    scene a6859 with dssr 
    sas "You need to be careful?! I feel like I'm wearing the clothes of a leprechaun!"
    if SashaHandTouchTease and Sasha_Deranged is True:
        scene a6860 with dssr 
        sas "I only did it because there's just girls here."
        scene a6862 with dssa 
        rob "[name]'s here."
        scene a6861 with dssa 
        sas "Indeed."
        scene a6863 with dssa 
        rob "Aww... You like [name]."
        scene a6864 with dssa 
        pause 
        scene a6865 with dssa 
        rob "You only make offensive jokes about guys you don't mind."
        scene a6866 with dssa 
        sas "There is a big difference between 'dont mind' and 'like'."
    scene a6867 with dssr 
    rob "It's not as tight as I thought it would be..."
    scene a6868 with dssa 
    pause 
    scene a6869 with dssa 
    sas "Is that what your first boyfriend said?"
    scene a6870 with vpunch 
    rob "Hey! You know I'm tight!"
    scene a6871 with dssa 
    sas "How would I know that?"
    scene a6872 with dssa 
    rob "One look at me and you just know- 'yeah, she tight!'"
    scene a6873 with dssa 
    rob "But yeah... I need this readjusted."
    scene a6874 with dssa 
    sas "It's mine. Get your own."
    scene a6875 with dssr 
    rob "Speaking about 'for me'."
    rob "Did Katie say anything about our custom dresses?"
    scene a6876 with dssa 
    sas "She finished them."
    scene a6875 with dssa 
    rob "Why didn't you say anything?"
    scene a6876 with dssa 
    sas "Because we won't be wearing them."
    scene a6882 with dssr
    rob "What? Why?"
    scene a6877 with dssr 
    sas "Robin, how many times do I have to tell you that Katie's dresses are too revealing?"
    scene a6883 with dssr
    rob "I want to wear it! She made them specifically for us!"
    rob "It can't be that bad!"
    scene a6877 with dssr 
    sas "The upper part of your ass is visible and besides being slightly translucent, it features a giant cleavage."
    scene a6884 with vpunch
    rob "You don't need to keep selling it to me! I already want it!"
    scene a6885 with dssr
    rob "And- And Katie put so much effort into our dresses! We both need to wear them!"
    scene a6888 with dssr
    rob "We need to take pictures together! Pictures of us and our beautiful butts!"
    scene a6878 with dssr
    sas "I have a vast array of her custom dresses and do you know how many of them I have worn?"
    scene a6879 with dssa
    sas "One of them I wouldn't even wear to trigger my Mom. I looked like the biggest- you know?"
    scene a6887 with dssr
    rob "*Laughs* I remember the picture. The blue dress, right? You really looked like a slut."
    rob "Your pose and expression as well."
    scene a6880 with dssr
    sas "I tried to bring a point across."
    scene a6889 with dssr
    rob "BUT! If I was a dude, I would've done you."
    scene a6881 with dssr
    sas "You'd disappoint me in every gender."
    scene a6890 with dssr
    pause
    scene a6891 with dssr 
    rob "Listen... It's a special event to me. THE Katie Zane made a dress just for ME."
    rob "That's a one in a lifetime chance."
    scene a6892 with dssa 
    rob "On top of that, she made two of them that are supposed to be worn together..."
    rob "Since when do we care what others think? So what if we're going to look a little slutty!?"
    scene a6893 with dssa
    rob "You've always been my inspiration for how little you care about the opinion of others."
    scene a6894 with dssa
    sas "It's not that I don't care about the opinions of others, it's just that I value mine more."
    sas "If you want to wear it to the bar, you should do so Robin and not be discouraged by me."
    scene a6895 with dssa
    sas "When I tell you to reevaluate other people's opinions, I'm including myself."
    scene a6899 with dssr
    rob "I know that."
    scene a6896 with dssr
    sas "You're such a girl."
    scene a6897 with dssa
    rob "If I'm a girl, what are you?"
    scene a6898 with dssa
    sas "A woman."
    scene a6900 with dssr
    rob "You talk to your cuddly toys in a funny, high-pitched voice when you think nobody's around! You-"
    play sound "Music/Sfx/Punch4.ogg"
    scene a6901 with vpunch
    rob "Au, au, auu!"
    scene a6902 with dssr
    rob "I wish you had a less hurtful love language!"
    scene a6899 with dssr
    rob "Why can't you be one of those love-to-give-gifts-people?"
    scene a6905 with vpunch
    with Pause(.4)
    play sound "Music/Sfx/Ripped.ogg"
    scene a6903 with vpunch
    sas "*Sigh* Why did you do that?"
    sas "You could've slapped me or whatever... But I don't have another top to wear."
    scene a6904 with dssa
    rob "That's the point! It's supposed to be a major inconvenience!"
    scene a6906 with dssr
    rob "You should know what happens when you mess with me!"
    scene a6907 with dssa
    sas "I taught you well."
    scene a6908 with dssa 
    sas "Now hand me your top."
    scene a6909 with vpunch 
    pause
    scene a6910 with dssa 
    sas "Robin!"
    scene b323 with dssr
    sas "She's doing well lately. I'm proud of her."
    scene b318a with dssr
    n "Is this your way of toughening her up?"
    scene b325 with dssr
    sas "She's tough. But she has a tendency to retreat to keep the peace. I don't like that."
    sas "If you tolerate everything, you stand for nothing. I want her to stand her ground when things get ugly."
    sas "I want her to have the courage to be disliked."
    scene b319 with dssr
    n "I had a friend like this in middle school."
    n "I did the same to her."
    scene b320 with dssa
    sas "Did it work?"
    scene b321 with dssa
    n "Nah, she's now suicidal and in therapy."
    scene b326 with dssr
    sas "Really?"
    scene b322 with dssr
    n "*Chuckles* No, I don't know what she's up to. I switched schools."
    scene b327 with dssr
    pause
    scene b328 with dssr
    n "Why do you have 'Katie Zane' pasties in your purse?"
    sas "I model for her."
    scene b329 with dssr
    n "Do you have Bimbo pasties? They'd fit Bella really well."
    if BellaNonExclusive5x0 is True:
        scene b330 with dssa
        pause
    scene b331 with dssr #############
    pause
    scene b332 with dssr
    rob "All of this could've been avoided if you had agreed to wear your dress."
    scene b333 with dssa
    rob "Your top would still be in one piece."
    scene b334 with dssa
    sas "It was your top."
    scene b336 with vpunch
    rob "It was my top!"
    scene b337 with dssr
    pause
    scene b338 with dssa
    rob "What I don't understand is that you said yes when we ordered them. You were totally on board."
    scene b341 with dssr
    sas "*Whisper* To be frank, I was ovulating."
    scene b339 with dssr
    rob "I'm not letting you off that easy!"
    sas "What if I give my dress to someone else? Nami for example."
    scene b338 with dssa
    rob "No! This was our thing!"
    scene b340 with dssr
    sas "If I wear the dress, I'll just attract unwanted attention."
    scene b338 with dssr
    rob "You always attract unwanted attention!"
    scene b340 with dssr
    sas "I want to wear one of my comfy turtlenecks and maybe a skirt. Drink some wine and have fun with my friends."
    sas "Is that too much to ask for?"
    scene b342 with dssa
    sas "And most importantly, I want to go home alone. But that dress screams that I don't."
    sas "I'll wear it when I have a second date with someone."
    scene b343 with dssa
    rob "The point is that we wear it together, you bimbo!"
    rob "And unless you want to take me with you on that second date, I'm against it!"
    scene b344 with dssa
    sas "There's nothing I can say that's not going to hurt you."
    scene b345 with dssa
    rob "*Mumbles* I know..."
    scene b346 with dssr
    rob "Where's my dress?"
    scene b347 with dssa
    sas "At my apartment."
    scene b346 with dssa
    rob "Good! I'll leave with you and take it off your insecure hands."
    scene b348 with dssa
    sas "Me not wanting to look like I just left one of Kelly's fever dreams has nothing to do with insecurity."
    scene b359 with dssr
    n "A minute ago you looked like you just left one of her fever dreams."
    scene b348 with dssr
    sas "You've seen some of my dresses and swimsuits, Robin. I've already forsaken entrance to heaven by owning them."
    scene b349 with dssa
    rob "And if it isn't the clothes it's the fake temporary tattoos you sometimes put on your skin."
    scene b352 with dssa
    pause
    scene b351 with dssa
    rob "...My final words regarding the dress situation."
    scene b353 with dssa
    rob "You're just like your mother."
    play sound "Music/Sfx/Slap3.ogg"
    scene b354 with vpunch
    "Robin laughs hysterically while Sasha pins her down."
    scene b355 with vpunch
    sas "Bid Señor Abbondanza farewell."
    scene b356 with dssr
    rob "Hey no! I was joking! Don't kill him!"
    scene b357 with dssa
    n "You want to kill her cat?"
    scene b358 with dssa
    rob "My cat?"
    scene b359 with dssr
    n "When you spoke about him I thought it was a cat?"
    n "Is it a dog?"
    scene b360a with dssa
    rob "What made you think that?"
    scene b361a with dssa
    n "You said you put all your trust in him and that he's your best friend."
    scene a7967 with Pixellate(1,10)
    sas "If you ask Kelly to write a smut story about me again..."
    play sound "Music/Sfx/Knife.ogg"
    scene a7968 with vpunch
    sas "He loses his head!"
    scene a7969 with vpunch
    rob "Noo! He's one of a kind! Please don't! I'll never do it again!"
    scene b362 with Pixellate(1,10)
    n "A dildo?"
    scene b363 with dssr
    rob "Not just any dildo!"
    rob "He was manufactured with flaws and was given to me for free with a previous purchase."
    rob "The little dimples and that he's crooked make him perfect."
    scene b364 with dssa
    rob "He hits ALL the spots- NAMI! All the spots like nothing else will ever do!"
    scene b365 with dssa
    rob "And this one wants to behead him."
    scene b366 with dssa
    sas "I said he would die if you asked Kelly for a story about me again."
    scene b367 with dssa
    sas "Let me add 'You comparing me to my Mother' to the list."
    scene b368 with dssa
    rob "Understood."
    scene b369 with dssr
    sas "He does, however, serve a very important purpose."
    scene b370 with dssa
    rob "*Giggles* He serves more than one purpose, trust me."
    scene b371 with dssa
    sas "It keeps you away from an early pregnancy that will without a doubt, ruin your life."
    scene b372 with dssa
    n "Take the pill. Use condoms."
    scene b373 with dssa
    rob "My period cramps get really bad when I'm on the pill. I've tried different ones and it's always a terrible experience."
    rob "And condoms are... Well... They are eww."
    scene b374 with dssa
    sas "Better than college pregnancy."
    scene b375 with dssa
    rob "I'm not so sure!"
    scene b376 with dssr
    rob "I'm obviously joking, Nami."
    n "I'm aware."
    rob "Not about the pill or condoms being the worst, though."
    scene b383a with dssr
    n "Mila said something similar."
    scene b384a with dssa
    mi "No, I said that I had never done it without a condom."
    scene b385a with dssa
    n "Right, right."
    scene b377 with dssr
    rob "It-"
    scene b378 with dssa
    sas "Robin. Stop."
    scene b379 with dssa
    sas "If she gets going, she'll never stop."
    scene b380 with dssr
    sas "*Mumbles* [name]'s coming. Girl topics."
    scene b381 with dssa
    sas "And my hair recovered just fine."
    scene b386 with dssr
    n "Thanks for the recommendation. I'll check the shampoo out."
    n "Even though, I usually don't vibe with coconut."
    scene b382 with dssr
    rob "It's really good. Try out the color protection formula with Argan oil too."
    scene b386 with dssa
    n "I love Argan oil."
    scene b387 with dssa
    rob "Oh! Last week I found this new Poke Bowl place and it's amazing!"
    scene b388 with dssr
    d "Cheeto. How long are we going to stay?"
    scene b389 with dssa
    n "Let's stay for a little longer, okay?"
    scene b390 with dssa
    d "Mhm."
    scene b391 with dssr
    za "Time to train?"
    scene b392 with dssa
    d "Not yet."
    scene b393 with dssa
    pause
    scene b394 with dssr
    za "Wanna play some table tennis?"
    scene b395 with dssa
    d "Another time."
    scene b396 with dssa
    d "Any news regarding your prank?"
    scene b397 with dssa
    za "Oh. Yeah, I haven't had the time to think about it."
    scene b398 with dssa
    d "Do you even have a plan?"
    scene b399 with dssa
    za "Not yet."
    za "It's also not really prank and more an act of vengeance."
    scene b400 with dssa
    d "What did she do?"
    scene b401 with dssa
    za "They destroyed Nadia's phone and made some creepy comments about her body."
    za "Nadia is too nice to do anything about it, but I'm not letting it slide."
    za "The cunt has it coming."
    scene b402 with dssr
    d "She's at Schwartz, right?"
    za "Mhm."
    scene b402 with dssa
    d "So Vanessa knows her?"
    scene b403 with dssa
    za "Yes."
    za "But she wouldn't dare to look at Nessi the wrong way. They ignore me too because of her."
    scene b402 with dssa
    d "Why are they afraid of her?"
    scene b404 with dssa
    za "Nessi knows a lot of important people. Including Steve O'Brian and Leia Zane."
    za "And they could make her family's life real hard."
    scene b405 with dssa
    d "I met Ceril's sister. The cop."
    scene b404 with dssa
    za "She's the sane one of the two... We're using a very low bar here."
    scene b405 with dssa
    d "Are they psychopaths?"
    scene b404 with dssa
    za "Melanie, yeah. I'm pretty sure."
    za "If not a psycho, definitely the biggest narcissist to ever exist."
    scene b406 with dssa
    d "Hmm."
    d "I can't wait for her reaction when we get her."
    scene b407 with dssa
    pause
    if ZaraBBallTrust5x0 is True:
        play sound "Music/Sfx/Punch.ogg"
        scene b408 with vpunch
        pause
        d "Do you think you could free yourself?"
        scene b409 with dssa
        za "One way or the other. Yes."
        scene b410 with dssa
        pause
        play sound "Music/Sfx/Punch.ogg"
        scene b411 with vpunch
        d "Nghh..."
        "She squeezes your balls slightly. but hard enough to make it uncomfortable."
        scene b412 with dssr
        d "*Muffled* You can let go."
        scene b413 with dssa
        za "Naah. I think you deserve a harder squeeze for destroying my top during our first basketball match."
        za "But I would let you get off with an apology..."
        menu:
            "Pinch her boob.":
                $ ZaraBoobiePinchS2_1 = True
                play sound "Music/Sfx/PunchBibi.ogg"
                scene b414 with vpunch
                pause
                play sound "Music/Sfx/Punch.ogg"
                scene b415 with vpunch
                za "*Muffled* Au au au-..."
                scene b416 with dssa
                d "I'll take your boobs down with me."
                scene b417 with dssa
                za "Losing your balls is worse than me losing my boobs."
                scene b418 with vpunch
                za "Ngh- It would make me more a-aerodynamic!"
                scene b419 with dssa
                "You both walk a few step backwards as Zara is trying to make you stumble."
                scene b420 with dssa
                za "I'm serious. I'll take your balls off."
                if BellaNonExclusive5x0 is True:
                    scene b421 with dssa
                    za "Ngh- I'm sorry Bella."
                scene b422 with dssa
                pause
                scene b423 with vpunch
                "Zara stops herself from gasping out loud and squeezes even harder out of reflex."
                "You muffle your scream of pain to a mere moan."
                if MilaVenus4x5 is True:
                    scene b424 with dssr
                else:
                    scene b424a with dssr
                "You both stumble backwards in a tight embrace... and with an even tighter grip."
                play sound "Music/Sfx/Punch.ogg"
                scene b425 with vpunch
                d "You'll take mine... I'll take yours."
                scene b426 with dssa
                "Her grip tightens slightly."
                scene b427 with dssr
                d "I'm ready to lose mine, are you ready to lose yours?"
                scene b428 with dssa
                pause
                scene b429 with dssr
                "Her clitoris is caught between your index and middle finger, and you increase the pressure more and more."
                scene b430 with dssa
                "Her grip softens and she releases your jewels."
                scene b431 with dssr
                "You gently loosen your electrifying grip and it fades into a lingering sensation."
                scene b432 with dssa
                pause
                scene b433 with dssr
                d "A bit of an unorthodox training method."
                scene b434 with dssa
                za "It's... It's a workout to withstand the wicked longing. That evil desire to do something that could lessen our potential athetlic achievements."
                scene b435 with dssa
                d "What?"
                scene b436 with dssa
                za "I don't know!"
                scene b437 with dssr
                za "It's good preperation- or training- so that we uh- not do something stupid! In order to train a muscle, you'll have to run laps or do you reps in the gym."
                za "And by teasing each other, we trained a mental muscle. It helps us not to go too far."
                scene b442 with dssa
                d "...So teasing each other trains a muscle?"
                scene b443 with dssa
                za "Yeah."
                za "The ability to withstand each other."
                scene b444 with dssr
                za "Our stupid hormones could be the downfall of this wonderful, platonic relationship."
                menu:
                    "We should keep training that muscle then.":
                        $ Dating_List.append("Zara")
                        $ ZaraTeasing = True
                        scene b445 with dssr
                        d "I guess... we shouldn't let the muscle atrophy."
                        play sound "Music/Sfx/Punch.ogg"
                        scene b446 with vpunch
                        pause 
                        scene b447 with dssa
                        za "...I guess not."
                        scene b448 with dssa
                        za "If we had trained the muscle before, this here wouldn't have almost escalated."
                        za "We're lucky we weren't alone."
                        scene b449 with dssa
                        za "*Whispers* We were unprepared. Our bodies weak. Our minds aching."
                        scene b455 with dssa
                        d "So what do you propose? How do we train the muscle without the risk of dropping 'the weight'?"
                        scene b451 with dssa
                        za "Nessi might be able to help."
                        scene b452 with dssa
                        za "We need to spot each other when we train it."
                        za "Very slight teasing for the warm up and then some harder reps... And by the end, we just go our own ways and rest so the muscle can recover."
                        scene b453 with dssa
                        d "(I think she's dropped a weight on her head at some point.)"
                        d "(I obviously know what this is... I remember this from Summer.)"
                        scene b454 with dssa
                        d "(We were both trying to come up with reasons to touch or wrestle. It's the exact reason why the Cheeto likes to wrestle... An excuse for body contact.)"
                        d "(I can't deny I'm not intrigued by her.)"
                        scene b455 with dssa
                        d "Meet me in the small bathroom upstairs. We should give it a small test."
                        scene b456 with dssa
                        za "Too risky."
                        scene b457 with dssa
                        d "When pain is the greatest, you'll show your true colors."
                        scene b458 with dssr
                        d "Right now that 'pain' is very intense... The reps we do now will count the most."
                        scene b459 with dssa
                        za "You're right. Let's go."
                        scene b460 with dssr
                        d "*Loud* I told you that the room wasn't too small."
                        "Zara looks at you a little lost."
                        scene b461 with dssa
                        d "Let me show you."
                        d "We'll be right back."
                        jump ZaraExercisePT1
                    "We shouldn't push this any further before something bad happens.":
                        za "That's the right choice. We have only so much energy and shouldn't waste it on something this ridicilous."
                        jump ContinueWG
            "Apologize.":
                scene b412 with dssa
                d "*Muffled*...Sorry for destroying your top."
                jump ContinueWG
    else:
        jump ContinueWG


label ZaraExercisePT1:
    stop music fadeout 5
    scene a7868 with slideleft
    play sound "Music/Sfx/DoorCloseHeavy.ogg"
    pause #door close 
    play music "Music/BibiFi/Mark Fabian - Slow Momentum.ogg" fadein 4
    scene a7869 with dssa
    za "What kind of exercises could we come up with?"
    scene a7870 with dssa
    d "I guess a dry hump sex position?"
    scene a7871 with dssa
    za "That's actually pretty good-"
    scene a7872 with dssa
    za "-but don't call it a sex position!"
    scene a7871 with dssa
    za "It's an exercise."
    scene b438a with dssb
    pause 
    scene b438 with dssa
    pause
    scene b439 with dssa
    d "Now I have a bad feeling."
    scene b440 with dssa
    za "Why?"
    scene b439 with dssa
    d "We found that position here way too fast. It felt too natural."
    scene b441 with dssa
    za "Those are going to be some heavy reps."
    scene b462 with dssr
    za "Remember the meaning of this. Never ever can we let it go too far or it's like a torn muscle."
    za "We need to rely on each other! If one of us fails, the other needs to be strong enough to spot!"
    scene Zara_E_2 with dssa
    pause
    pause 
    scene a7847 with dssr
    pause 
    scene a7848 with dssa
    d "Ready to add some weight?"
    scene a7849 with dssa
    za "I'm not so sure."
    scene a7850 with dssr
    "You gently stroke her toned body."
    za "I don't think we can lift without straps yet."
    scene a7851 with dssr
    pause
    scene a7852 with dssr
    pause
    show Zara_E_1 with dssa
    pause
    scene a7853 with dssr
    za "That weight is getting really heavy..."
    scene a7854 with dssa
    d "(I thought this was going to be easy, and I would have some fun teasing her but...)"
    scene a7855 with dssa
    d "(Damn, do I want to kiss her.)"
    scene a7856 with dssr
    pause
    scene a7857 with dssa
    d "(Was she always this pretty?)"
    pause
    scene a7858 with dssa
    za "[name]... My muscle- I'm close to muscle failure."
    scene a7860 with dssa
    d "There's some more in you."
    play sound "Music/Sfx/Slap.ogg"
    scene a7861 with vpunch
    za "*Moans* Man, I don't know!"
    scene a7862 with dssa
    d "What did you say? You never leave the gym like a loser. You always give it all."
    play sound "Music/Sfx/Punch.ogg"
    scene a7863 with vpunch
    "She slams her pelvis into yours, her pussy rubbing over the rough surface of your pants."
    d "Okay- put the weight down."
    scene a7864 with dssa
    "You feel every fiber in her body relax." 
    scene a7865 with dssr
    "Slightly shaking and with an unsteady breath, she steps off you."
    scene a7866 with dssa
    d "Are you okay?"
    scene a7867 with dssa
    za "I'm not okay... I'm so not okay."
    scene b469 with dssr
    za "I feel nauseous. We used too much weight."
    za "I think my muscle is torn."
    scene b470 with dssa
    d "Nah."
    d "The good thing about this exercise is that our muscles can only fail together."
    d "As long as one of us spots the other. We're good."
    scene b471 with dssa
    pause
    scene b472 with dssa
    za "Another set?"
    scene b473 with dssa
    d "No. I don't have it in me and neither do you."
    scene b475 with dssa
    za "Yeah, who am I kidding..."
    scene b474 with dssa
    d "That's exactly what we need to fight. That feeling that tells you, you want to do another set."
    scene b476 with dssa
    za "So that it becomes easier over time, right?"
    scene b477 with dssr
    pause
    scene b478 with dssa
    "You both laugh for a moment."
    scene b479 with dssa
    za "There might not be any scientfic data on this but... It has to do something, right?"
    scene b480 with dssa
    d "I guess it challenges your willpower?"
    scene b479 with dssa
    za "And I really don't want anything to happen between us."
    scene b481 with dssa
    za "I'm not kidding about it."
    scene b482 with dssa
    d "Because we're trainer and trainee?"
    scene b483 with dssa
    za "That too."
    za "But mostly because I don't want to risk my future as a pro. I need to focus."
    scene b484 with dssa
    za "See what's happening right now! We're having an unusual long conversation! Instead we could be working on a plan!"
    scene b485 with dssr
    stop music fadeout 7
    pause
    scene b486 with dssa
    d "You're a dumbass."
    scene b487 with vpunch
    za "What?!"
    $ play_playlist(playlist_BabyBellchen)
    scene b488 with dssr
    pause
    scene b489 with dssa
    d "I don't think I've ever seen someone as crazy and dedicated to progress as you are."
    scene b490 with dssa
    d "But... all your future accomplishments become a lot less meaningful if you have no one to share it with."
    d "No one to tell about... No one to tell you... that you're the best version of yourself."
    scene b491 with dssr
    d "You'll be doing just fine, but don't lose yourself on the way to the top."
    scene b492 with dssa
    za "*Whisper* We said no more sets..."
    scene b493 with dssr
    pause
    stop music fadeout 10
    scene black with Dissolve(2)
    with Pause(.5)
    jump ContinueWG



label ContinueWG:
    if ZaraTeasing is True:
        scene b494 with dssr
        pause
        scene b495 with dssa
        d "Breath, and appear casual."
        n "Thoughts?"
        scene a6911 with dssr
        rob "Maybe."
        scene a6912 with dssa
        sas "No. Her hair looks too good."
        scene a6911 with dssa
        rob "Maybe he has a short fuse."
        scene a6913 with dssa
        n "I asked if you think they made out, not if they fucked."
        $ play_playlist(playlist_Girly3)
    scene a6914 with dssr
    pause
    scene a6915 with dssa
    rob "Nami! Guess what!"
    scene a6916 with dssr
    rob "I got a dress made by Katie Zane."
    scene a6917 with dssa
    n "Really? A custom made dress?"
    scene a6916 with dssa
    rob "Yes."
    scene a6918 with dssa
    rob "Well, technically Sasha got an almost identical one in a different color scheme."
    scene a6919 with dssa
    rob "They were meant to be worn together... to show off our indestructible friendship."
    scene a6920 with dssa
    n "And she doesn't like it?"
    scene a6919 with dssa
    rob "She doesn't feel it anymore."
    scene a6929 with dssr
    n "Buying a Zane dress is out of my price range but during some window shopping I had seen some. They looked pretty sexy."
    scene a6922 with dssr
    rob "Yeaaah, all Katie produces is quite sexy and revealing."
    rob "Anyway, Sasha now doesn't want to wear it to the bar opening because she hates me. But I will."
    scene a6921 with dssa
    n "Does it show so much?"
    scene a6922 with dssa
    rob "Your upper ass is visible."
    scene a6921 with dssa
    n "And you don't mind it?"
    scene a6923 with dssa
    rob "I've never worn something like this. We'll see."
    scene a6924 with dssa
    n "I have trouble imagining it. You always dress rather-"
    scene a6925 with dssa
    rob "Plain?"
    scene a6924 with dssa
    n "Not plain but casual."
    scene a6925 with dssa
    rob "Definitely my preferred style."
    scene a6926 with dssa
    rob "But when I go out, I want to bring my A game!"
    scene a6930 with dssr
    n "Send me a picture later!"
    scene a6931 with dssa
    rob "Will do!"
    scene a6927 with dssr
    pause
    n "Talking about a little slutty... I didn't expect Sasha to wear an underboob top in public."
    scene a6928 with dssa
    rob "She usually only dresses slutty on two occasions: She just modeled for Katie or had to threaten her Mom."
    scene a6932 with dssa
    n "To threaten her Mom?"
    scene a6933 with dssr
    rob "Umm... Well..."
    scene a6934 with dssa
    rob "Ah what the hell..."
    scene a6935 with dssa
    rob "Public perception is very important to Elena. In addition to that, she's extremely protective of Sasha."
    scene a6936 with dssa
    rob "Protective to a degree where it's closer to an obsession."
    scene a6937 with dssa
    rob "Like a few days ago..."
    stop music fadeout 3
    scene black with Dissolve(.5)
    with Pause(.5)
    play music "Music/OST/Azula Wave - Lost Souls.ogg"
    scene c1a with dssb
    pause 
    scene c2a with dssa
    pause 
    scene c3a with dssr
    pause 
    scene c4a with dssa
    pause 
    scene c5a with dssr
    pause 
    scene c6a with dssr
    pause
    scene c6b with vpunch
    pause 
    scene c7a with vpunch
    pause 
    scene c8a with dssa
    sas "Mama?"
    scene c9a with dssa
    sasmo "Yes?"
    scene c8a with dssa
    sas "Can I go to-"
    scene c9a with dssa
    sasmo "I can't hear you. Come inside."
    scene c10a with dssr
    sas "I can't! I can only step on these diamond shapes."
    scene c11a with dssr
    sasmo "*Sigh*"
    scene c12a with dssa
    sas "Ayua, Robin and I got invited to the not yet opened ZPR bar. I mentioned it yesterday."
    scene c14a with dssa
    sasmo "No. It's already late and it's going to rain."
    play sound "Music/Sfx/Punch.ogg"
    scene c13a with vpunch
    sas "Yesterday, you said I could go!"
    scene c15a with dssa
    sasmo "I said 'maybe'."
    sasmo "Besides, some work friends of mine will be here soon. You should join us."
    play sound "Music/Sfx/Punch.ogg"
    scene c16a with vpunch
    sas "No! I want to go outside!"
    scene c17a with dssa
    sasmo "This isn't up for debate."
    scene c18a with dssa
    sas "This is so-"
    scene c19a with dssr
    sasmo "I won't repeat myself. Go to your room, get adequate, and meet us in the east lounge in forty minutes."
    scene c20a with dssr
    sasmo "Melvin, their son, is going to be there too. He's your age."
    scene c21a with dssa
    pause
    scene c1 with dssr
    sas "Who are those work friends of yours?"
    sasmo "We've only met recently. They own a restaurant chain."
    sasmo "I'll introduce you to their son."
    scene c3 with dssr
    sas "Oh... If I had know that, I would've picked something less conservative to wear."
    scene c2 with dssa
    sasmo "I'm sure it's fine-"
    scene c4 with dssr
    pause
    scene c5 with vpunch
    sasmo "For christ's sake, Sasha! Go upstairs and change!"
    scene c6 with dssa
    sas "What's wrong, Mother?"
    scene c7 with vpunch
    sasmo "Sasha!"
    scene c8 with vpunch
    sas "I want to go to that bar."
    scene c9 with dssa
    butler "My lady. The Howard's are here."
    scene c10 with dssa
    sasmo "Sasha! I'm serious! GO UPSTAIRS and change."
    scene c11 with dssr
    pause
    scene c12 with dssa
    sas "Oh no... This dress really struggles to keep my breasts contained..."
    scene c13 with dssr
    sasmo "You will be back in two hours!"
    scene c14 with dssa
    sas "Three and a half."
    scene c15 with dssa
    sasmo "Two and a half."
    scene c16 with dssa
    sas "Mmmh... Maybe you're right. I should go change... Let me try out one of Katie's new translucent dresses..."
    scene c17 with vpunch
    sasmo "*Seething fury* Three hours."
    scene c18 with dssa
    sas "*Cute* Very well."
    scene c19 with slideleft
    stop music fadeout 7
    sas "Later Mama."
    scene c20 with dssr
    sasmo "Dwight is coming with you."
    sasmo "Call me when you get there and when you leave, okay?"
    scene c21 with dssr
    sas "It's going to be okay! Don't worry!"
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Girly3)
    scene a6938 with dssr
    n "Soo let me get this straight... She dresses in hot outfits to get what she wants?"
    scene a6941 with dssr
    rob "Simplified, but yes. If she feels like her mother's treating her unfairly, she'll use her weaknesses against her."
    rob "She also uses temporary tattoos to trigger her mother and aunt even further. Blame Ayua for that."
    scene a6940 with dssr
    n "That's wild... and such an unhealthy relationship."
    scene a6939 with dssa
    rob "Yeah, it's hard to understand from the outside, and approaching it with a rational mind is going to get you nowhere. You'll just bang your head against a wall."
    rob "The entire situation is way too complex and emotionally charged."
    scene a6941 with dssr
    rob "I've known Sasha for almost ten years."
    scene a6942 with dssa
    rob "And before we met, she was home schooled because her Mom was too afraid to let her outside."
    scene a6941 with dssa
    rob "Literally."
    rob "Nobody else faced the same treatment and that's when her rebellion started."
    scene a6943 with dssr
    rob "She went on a hunger strike when she was eight years old! It lasted almost three days until Elena gave in, and allowed her to go to a normal school."
    scene a6944 with dssa
    rob "A private school, of course, but you know what I mean."
    scene a6945 with dssa
    rob "That's also where we met."
    scene a6947 with dssr
    d "Bella too?"
    scene a6946 with dssa
    rob "Bella joined later. She was at a public school at first."
    scene a6948 with dssr
    rob "To Sasha, there's nothing more important than freedom... If someone tells her not to do something, she might do it out of spite."
    scene a6949 with dssa
    n "So if I tell her not to buy me rolls, she'll do it?"
    scene a6948 with dssa
    rob "There has to be an emotional attachment."
    scene a6949 with dssa
    n "Who doesn't have an emotional attachment to-"
    scene a6951 with dssa
    d "Shut up, Cheeto."
    scene a6949 with dssa
    n "Did she ever leave the house looking skimpy?"
    scene a6950 with dssr
    rob "Yeah, otherwise her Mom would've called the bluff..."
    rob "It works in tandem with her taste for short skirts."
    scene a6952 with dssa
    rob "Occasionally, she'll up the ante so Elena knows she means business."
    scene a6953 with dssa
    n "What does her Dad say?"
    scene a6952 with dssa
    rob "He's not living with them, but by what I heard, he just laughs to Elena's dismay. That he warned her, that this would be the result if Sasha was put in a cage." 
    scene a6954 with dssa
    rob "Sasha is pretty much like her Dad... including that hurtful love language..."
    scene a6952 with dssa
    rob "They have a good relationship, though."
    scene a6955 with dssa
    rob "Her Mom's side of the family is a bit more conservative while Her Dad's side is the total oppossite."
    scene a6956 with dssa
    rob "Two worlds constantly clashing, which is why I like what Katie said."
    rob "'She's a confused angel in perpetual motion, wavering between flight and fall.'"
    scene a6957 with dssr
    pause
    scene a6958 with dssr
    rob "Ayua, Jenna, Anna, Claire, Kelly, my Mama and I have a Sasha-Bingo game going."
    play sound "Music/Sfx/Punch.ogg"
    scene a6959 with vpunch
    rob "*sharp whisper* Don't ever tell her that!"
    scene a6961 with dssr
    n "I want in."
    scene a6960 with dssr
    rob "I'll introduce you at the next book club."
    scene a6962 with dssr
    pause
    scene a6963 with dssa
    n "The room is so big."
    scene a6964 with dssa
    n "This house is so much better than I expected. I'm so ready to move out!" 
    scene a6965 with dssa
    n "We could have some amazing parties here."
    scene a6966 with dssa
    n "This basement is going to be our social hub... Where we watch movies and talk about the most depraved stuff ever!"
    scene a6967 with dssr
    pause
    d "Take me back?"
    scene a6969 with dssa
    pause
    scene a6970 with dssr
    n "I guess that seals it. We'll be moving here?"
    scene a6971 with dssa
    pause
    scene a6972 with dssa
    n "Yo! Don't bitch out now!"
    scene a6973 with dssa
    d "I think Zara's getting to me."
    scene a6974 with dssa
    n "Dude..."
    if RaceWithImpossibleOdds is True:
        scene a6975 with dssr
        n "It's perfect for us."
        n "Warden Nojiko isn't around and we can freely explore us."
        scene a6976 with dssa
        pause
        scene a6977 with dssa
        n "I can see the chicken in you."
        n "You better not bitch out now."
        scene a6978 with dssa
        d "I feel overwhelmed."
        d "This all sounds so painfully busy."
        scene a6974 with dssa
        n "It won't be so bad."
    scene a6979 with vpunch
    n "Zara stop bewitching him!"
    scene a6980 with dssr
    za "*Laughs* I'm not doing anything!"
    za "It's all you girls."
    scene a6981 with dssa
    za "I'm here for you, [name]!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene a6982 with dssr
    pause
    if RobinOffHook5x0 is True:
        $ RobinFriends = True 
        scene a6983 with dssa
        rob "Are you excited?"
        scene a6984 with dssa
        d "I'm not so sure."
        d "It's a big change."
        scene a6985 with dssa
        rob "For all of us."
        scene a6986 with dssr
        rob "Especially for Mila. I assume you know about her current living situation?"
        d "A little."
        scene a6987 with dssr
        rob "I offered help to get her stuff."
        scene a6988 with dssa
        if MilaSleep5x0 is True:
            d "She asked me as well."
            scene a6989 with dssa
            rob "I feel better knowing you're there, too."
            scene a6990 with dssa
            rob "I don't know her parents but maybe they could be violent... I don't know."
        if RobinFavor5x0 is True:
            d "If she needs help, I'd help too."
            scene a6991 with dssa
            d "You still owe me, by the way."
            scene a6992 with dssa
            rob "What do you need me to do?"
            scene a6993 with dssa
            d "I don't have anything yet."
            scene a6994 with dssa
            rob "Oh."
            scene a6995 with dssr
            if BellaDate is False:
                rob "You can ask me anything."
            else:
                rob "You can ask me a lot."
            scene a6996 with dssa
            rob "If- I will do it is a different question."
            scene a6997 with dssa
            rob "But don't be shy."
            scene a6998 with dssa
            d "The tone of your voice sounds oddly close to how Nami sometimes talks and it freaks me out."
            scene a6999 with dssa
            pause
    scene a7000 with dssr
    rob "We need to work out who gets what room."
    scene a7001 with dssa
    d "I'll just take the one that's left."
    scene a7002 with dssa
    n "Let's figure it out upstairs."
    if MilaSleep5x0 is True:
        scene a7013 with dssa
        pause 
        play sound "Music/Sfx/Punch.ogg"
        scene a7014 with vpunch
        pause 
        scene a7015 with dssr
        pause  
        scene a7016 with dssr
        pause 
        scene a7017 with dssa
        pause  
        scene a7018 with dssa
        pause 
        scene a7019 with dssr
        d "Do you lotion your butt?"
        scene a7020 with dssa
        mi "*Laughs* Of course!"
        scene a7021 with dssa
        mi "You want your butt to be smooth!"
        scene a7022 with dssa
        pause 
        scene a7023 with dssr
        pause
    elif NamiDate is True:
        scene a7024 with dssr
        pause 
        play sound "Music/Sfx/Punch.ogg"
        scene a7025 with vpunch
        n "Yo!"
        scene a7026 with dssa
        pause 
        scene a7027 with dssa
        pause
        scene a7029 with dssr 
        d "I'm tired Cheeto... We should leave and take a nap."
        scene a7028 with dssa
        n "Naps are for bibis."
        scene a7030 with dssa
        n "What you need is to slap my ass while you suck on my nipplies."
        scene a7031 with dssr
        pause 
        scene a7032 with dssr
        n "Let's get this over with, and we'll continue this conversation in my room."
        scene a7033 with dssa
        n "Mhhhhhhhh!"
    elif ZaraTeasing is True:
        scene a7003 with dssa
        pause 
        scene a7004 with dssr
        pause 
        scene a7005 with dssa
        d "Just some quick reps..."
        scene a7006 with dssa
        pause 
        scene a7007 with dssa
        za "Only feminine girly girls train with gloves."
        scene a7008 with dssr
        pause 
        scene a7009 with dssa
        pause
        scene a7010 with dssr
        "Her soft, yet firm skin gently moves between your fingers." 
        scene a7011 with dssa
        d "Good set. The weight was adequate. No complaints."
        scene Zaranodding3 with dssa
        za "Mhm!"
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Smooth)
    scene a7034 with dssb
    pause
    scene a7035 with dssr
    sas "I'll write down a number for every room."
    sas "One for the first room we viewed, two for the second and so on."
    scene a7058 with dssr
    n "Sounds fair."
    scene a7059 with dssa
    n "As long as [name] doesn't win. He already got the better room at Zara's... Not again!"
    scene a7060 with dssa
    pause
    scene a7061 with dssa
    "Mila tips her fingers on your shoulder."
    scene a7062 with dssr
    mi "I need to ask you something."
    scene a7063 with dssr
    pause 
    scene a7064 with dssa
    d "What's up?" 
    scene a7065 with dssr
    mi "Could you do me a favor?"
    scene a7066 with dssa
    d "What is it?"
    scene a7067 with dssa
    mi "The charges against me were dropped all of a sudden."
    mi "I think it's got something to do with Bella."
    scene a7068 with dssa
    pause
    scene a7069 with dssa
    mi "Could you ask her about it without mentioning me?"
    mi "I want to know if she tried to frame me or-"
    scene a7070 with dssa
    mi "I don't know."
    scene a7071 with dssa
    d "I'll ask her."
    scene a7072 with dssa
    d "(Did Bella already meet up with the Holgerson guy? She didn't mention anything.)"
    scene a7073 with dssr
    d "But hey, it's great news that they were dropped."
    d "Even though, I still have no idea why they'd ever suspect you."
    scene a7074 with dssa
    mi "That's why I think Bella tried to frame me."
    scene a7075 with dssa
    d "Bella's the worst, but she wouldn't do that."
    if bellameet is True:
        d "(I know. Because I was there.)"
    if BellaNonExclusive5x0 is True:
        scene a7074 with dssa
        mi "You think that because you're boneing her."
    else:
        scene a7076 with dssa
        mi "I don't know what to think about her."
    scene a7073 with dssa
    d "I'll see what I can find out."
    scene a7077 with dssr
    mi "They also send me something else..."
    scene a7078 with dssa
    mi "Their lawyer called and told me that I would be reimbursed plus a little extra for the trouble."
    mi "But they want me to come by in person."
    mi "There was signature from Zoey Holgerson. I have no idea who that is. Maybe his wife?"
    scene a7079 with dssa
    d "I don't know. I've never heard that name before."
    scene a7080 with dssa
    mi "I think I-... I mean I have to go. Right?"
    scene a7081 with dssa
    d "I don't think it can hurt?" 
    scene a7082 with dssa
    d "But in case it does, pretend I said something else."
    if MilaDate is True:
        d "If you need me to come with you, I'll be there."
        scene a7083 with dssa 
        mi" Thanks."
    else:
        d "If you need assistance, just call me or Nami... Preferably Nami."
    scene a7082 with dssa
    d "Now first things first, how to rig the papers so we get the better rooms."
    scene a7084 with dssr 
    mi "Let's do that."
    scene a7047 with slideleft
    n "Wait, wait, wait... You went on a date with THE Benjamin Parlow?"
    scene a7036 with dssr
    sas "Mhm."
    scene a7037 with dssa
    mi "The movie star?"
    sas "Mhm."
    scene a7047 with dssr
    n "...Did you hit that?"
    scene a7038 with dssr
    sas "No."
    sas "There was no second date."
    scene a7039 with dssa
    n "Why not? Did you mess up?" 
    scene a7038 with dssa
    sas "No. I wasn't interested." 
    scene a7048 with dssr 
    n "Was he that boring?"
    scene a7040 with dssr
    sas "I don't really remember, but he was just not what I'm looking for."
    scene a7051 with dssr
    rob "For months afterwards, these gossip magazines posted about her and Benjamin."
    rob "They made up so much stuff." 
    scene a7041 with dssr
    sas "We ended up suing them and put one of these magazines out of business."
    sas "My mother's a lawyer."
    scene a7052 with dssr
    rob "Ohh- remember the podcast you were invited to?"
    scene a7045 with dssr
    mi "Do tell! I got invited to one a month ago too."
    scene a7053 with dssr
    rob "She and Sedi were invited and the guys just wanted to dunk on them. You know, show how stupid and out of touch they are."
    scene a7054 with dssa
    rob "They annihilated these idiots."
    scene a7049 with dssr 
    n "Is it still online?"
    scene a7042 with dssr
    sas "No. They deleted the livestream immediately afterward."
    scene a7053 with dssr
    rob "We recorded it. I still have it somewhere."
    scene a7046 with dssr
    mi "I'd love to see Sasha destroy some blackpilled dudes."
    scene a7053 with dssr
    rob "I'll see if I can find it."
    scene a7050 with dssr 
    n "I'm still trying to understand the whole Benjamin thing. I need a whole breakdown of the date!"
    n "He's really handsome. I'm surp-"
    scene a7043 with dssr
    sas "I don't care much for looks."
    scene a7044 with dssa
    sas "I'm hot enough for the both of us."
    scene a7050 with dssr 
    n "That's not a bad way to do it."
    d "*Annoyed* The rooms..."
    scene a7085 with dssr 
    sas "Nami." 
    scene a7086 with dssa
    pause 
    scene a7087 with dssr
    "She takes a deep breath."
    scene a7088 with dssa
    n "Okay... I can do this."
    scene a7089 with dssa
    n "All that matters is that I beat [name]."
    scene black with Dissolve(2)
    n "Don't let these bitches get in to your head, Nami."
    $ renpy.movie_cutscene("images/Animations/CH1-3/CheetoBoxing.webm", stop_music=False)
    scene a7873 with dssr
    n "I have trained for this under extreme conditions..." 
    scene a7874 with vpunch
    u "Can't this go any faster?!"
    scene a7875 with dssa 
    pause 
    scene a7876 with dssa
    n "Pressure... means nothing to me."
    scene a7878 with vpunch
    d "Hurry up, idiot!"
    scene a7877 with dssa
    "She inhales deeply... and with purpose."
    n "The rolls..." 
    n "...will guide me..." 
    scene a7095 with vpunch
    sas "Pick one!"
    scene a7090 with dssr
    n "Did you mix them properly?"
    scene a7091 with dssa
    sas "It's four papers. There's nothing to mix."
    scene a7092 with dssr
    n "Yeaaah, right."
    n "I bet Robin paid you off."
    scene a7093 with dssr
    pause
    scene a7094 with dssa
    sas "Don't look at it before everyone picked one."
    scene a7056 with dssr 
    sas "Next Mila."
    scene a7055 with dssa
    mi "I'm nervous."
    scene a7057 with dssa 
    pause
    scene a7096 with dssr
    sas "[name]."
    scene a7110 with vpunch 
    rob "Why am I last?!"
    scene a7111 with dssa 
    sas "For your behaviour today, you'll only get leftovers."
    scene a7112 with dssa 
    rob "*Mumbles* ...Again?"
    scene a7096 with dssr
    pause
    scene a7097 with dssa
    pause 
    play sound "Music/Sfx/Punch.ogg"
    scene a7098 with vpunch
    za "No! The other one."
    scene a7099 with dssr
    d "What? Why?"
    scene a7100 with dssr
    pause
    scene a7101 with dssa
    d "This one?"
    scene a7102 with dssa
    za "Mh."
    scene a7103 with dssa
    mi "Which one has the bath en suite?"
    scene a7104 with dssa
    sas "Number four."
    scene a7105 with dssa
    d "(Mhh.)"
    scene a7106 with dssr 
    pause 
    scene a7113 with dssr 
    sas "Keep in mind, there's only one room with a bad en suit."
    play sound "Music/Sfx/PaperBall.ogg"
    scene a7114 with vpunch 
    with Pause(.2)
    scene a7115 with dssa 
    sas "You can still trade rooms afterwards."
    scene a7108 with vpunch 
    n "WHO HAS NUMBER FOUR?!"
    scene a7109 with dssr 
    d "I do."
    scene a7107 with hpunch 
    n "HOW IS THAT POSSIBLE?! YOU GOOFY ASS CHEATER!"
    scene a7116 with dssr 
    rob "He's definitely a cheater!"
    rob "He seduced Sasha!"
    scene a7117 with dssr
    za "I wanted you to pick a bad one..."
    scene a7118 with dssa 
    d "Why?"
    scene a7119 with dssa 
    za "So you'd have more of reason to stay..."
    scene a7120 with dssr
    mi "[name]... I'll trade you."
    mi "I'll take over your dish duty for a year!"
    scene a7121 with dssa
    sas "Mila is putting it on the table."
    scene a7122 with dssa
    n "I- I stop talking about sexual stuff with you!"
    scene a7123 with dssa
    d "You're going all in."
    scene a7124 with dssa
    n "I'm ready to sell my body here!"
    scene a7125 with dssa
    d "Aaand you're back out."
    play sound "Music/Sfx/Punch.ogg"
    scene a7126 with vpunch
    n "YO!"
    if RobinOffHook5x0 is True:
        scene a7127 with dssr
        rob "I'll not do your dishes, but I'll send you some nudes!"
        scene a7129 with dssa
        d "Sorry Robin."
        scene a7130 with dssa
        rob "Nudes and a lap dance?"
        scene a7128 with dssa
        d "It's getting colder."
        scene a7131 with vpunch
        rob "Sasha nudes!"
        scene a7133 with dssa
        sas "You don't have nudes of me."
        scene a7132 with dssa
        rob "You often send me pictures of you in the dressing room..."
        rob "They must count for something."
        scene a7134 with dssa
        d "Very cold."
        if SashaHandTouchTease is True:
            scene a7135 with dssa
            "Sasha squints and her eyes pierce your soul." 
    scene a7138 with dssr
    mi "One year of dishes, and once a week, I'll make you breakfast."
    scene a7139 with dssr
    d "Mila is leading."
    scene a7143 with dssa
    d "(I don't want room number four.)"
    d "(But I'm sure if I play this right, I can trade it for something valueable.)"
    scene a7144 with dssa
    n "I'll make you breakfast every day, I-"
    scene a7145 with dssa
    d "Nami's last place."
    scene a7146 with vpunch
    n "What?!"
    scene a7147 with dssa
    d "You spiked my food with chilli and other fucked up shit before! I don't trust you near my food!"
    scene a7136 with dssr
    sas "Put in your last offers."
    scene a7140 with dssr
    mi "I'll make you breakfast on the weekends, dishes for a year, and a protein shake every time you come home from the gym, if I'm available."
    scene a7151 with dssr
    za "Mila wins!"
    if Mila_Bath_Pussy or Mila_Pussy is True:
        scene a7141 with dssr
        mi "*Whisper* And once a week, I'll give you a blowjob. Anywhere. Anytime."
        scene a7142 with dssr
        rob "Your lips formed the word blowjob."
        scene a7137 with dssr
        sas "*Mumbles* Of course that's what you saw."
    scene a7148 with dssr
    n "Alright... [name]..."
    n "I'll stop involving you in weird sexual topics. I'll stay far away from your food."
    scene a7149 with dssa
    n "I'll offer my stand in services for you. If there's an event you don't want to go to, I'll step in and sacrifice myself for you."
    n "And... You can always shower before me... Or with me. Whatever you prefer."
    if NamiDate is True:
        scene a7150 with dssa
        n "*Whispers* Additional... you can touch, kiss, lick, and maybe even fuck my ass whenever you want."
    if RobinFriends is True:
        scene a7152 with dssr
        rob "My pitch..."
        scene a7153 with dssr
        rob "I'll do your laundry for three months. I'll also prepare you a protein shake every day."
        rob "Once a week, I'll clean your room-"
        scene a7154 with dssr
        rob "in"
        scene a7155 with dssr
        rob "in whatever"
        scene a7156 with dssr
        rob "in whatever outfit"
        scene a7157 with dssr
        rob "in whatever outfit you"
        scene a7158 with dssr
        rob "in whatever outfit you want"
        scene a7159 with dssr
        rob "in whatever outfit you want me"
        scene a7160 with dssr
        rob "in whatever outfit you want me to."
        scene a7153 with dssr
        if BellaNonExclusive5x0 is True:
            rob "Plus: I'll chauffeur you and Bella around when you go on dates allowing you both to drink!"
        else:
            rob "Plus: If there's a girl you like, I'll chauffeur you around once every two weeks."
    call screen RoomPick
    
    #pick 
label RoomPicked:
    if RobinRoom == True:
        scene a7162 with vpunch
        rob "YES!"
        play sound "Music/Sfx/Punch.ogg"
        scene a7163 with vpunch
        "Robin giggles."
        scene a7165 with dssr
        mi "I hate him."
        scene a7166 with dssa
        n "I hate him more."
        scene a7167 with dssa
        n "I'll trade you Robin!"
    elif MilaRoom == True:
        play sound "Music/Sfx/Punch.ogg"
        scene a7168 with vpunch
        mi "Oh yes!"
        scene a7169 with dssa
        n "Unfair! Mila used her giant boobs to persuade him!"
        scene a7170 with dssa
        mi "Homefield advantage."
        scene a7164 with dssr
        rob "You have a price Mila! And Sasha is ready to pay it for me!"
    elif NamiRoom == True:
        play sound "Music/Sfx/Slap.ogg"
        scene a7171 with vpunch
        n "Ohhh yeah! My boy coming in clutch!"
        scene a7172 with dssa
        n "I knew, I could count on you!"
        if NamiDate is True:
            scene a7173 with dssa
            n "*Whisper* Of course I know my ass carried this."
        pause 
        scene a7164 with dssr
        rob "You have a price Nami! And Sasha is ready to pay it for me!"
    jump WG_End



label WG_End:
    stop music fadeout 5
    scene a7174 with dssr
    d "Alright. Can we go?"
    scene a7175 with dssa
    n "In a minute."
    $ play_playlist(playlist_MystyGood)
    scene a7176 with dssa
    pause
    scene a7177 with dssr
    pause 
    scene a7178 with dssa
    menu:
        "Observe Sasha with interest.":
            $ Sashas_Grace = True 
            scene a7179 with dssr
            pause 
            d "(She appears so graceful, yet there is something about her I cannot interpret)."
            scene a7180 with dssr
            d "(A distance dwells within her... perhaps even from herself, as though part of her has remained somewhere far away.)"
            d "(I wonder how she got that scar...)"
            pause
            scene a7181 with dssr
            d "(Somehow, I feel I'll never see her again after college.)" 
            pause
            scene a7182 with dssr
            d "(I don't even know her, yet the thought of it feels like mourning something I was never given...)" 
            pause 
            scene a7183 with dssa
            d "(I should be looking away but I can't seem to loosen my gaze.)" 
            scene a7184 with dssr
            "Her eyes meet yours, your heart skips an almost unnoticeable beat."
            d "(Her eyes are so deep.)"
            scene a7185 with dssr
            d "(I wonder...)"
            scene a7186 with dssr
            d "(Who are you really?)"
            scene a7187 with dssr
            sas "You're staring at me."
            scene a7188 with dssa
            d "Yeah."
            scene a7189 with dssa
            pause
            play sound "Music/Sfx/Curtain1.ogg"
            scene a7190 with dssr
            "She closes the curtains."
        "Let your eyes wander.":
            play sound "Music/Sfx/Curtain1.ogg"
            scene a7190 with dssr
            "She closes the curtains." 
    scene a7191 with dssr
    pause
    scene a7192 with dssa
    sas "Why doesn't Nami talk to Sedi?"
    scene a7191 with dssa
    d "Who?"
    scene a7193 with vpunch
    sas "What do you mean, who?!"
    scene a7194 with dssa
    d "I have no idea who Sedi is."
    scene a7195 with dssa
    pause 
    scene a7196 with dssa
    sas "Her older sister."
    scene a7248 with dssr
    pause 
    scene a7249 with dssa
    d "Oh."
    scene a7250 with dssa
    d "I don't really remember but Nami prefers to act like she has no sister."
    scene a7197 with vpunch
    sas "*Snarls* Of course she does!"
    scene a7198 with dssr
    d "Okay? You're getting quite mad."
    scene a7199 with dssa
    pause 
    d "Who's Sedi? Have I met her?"
    scene a7200 with dssa
    sas "You've crossed paths."
    sas "She was convinced you knew who she was."
    scene a7201 with dssa
    d "Nami never really told me anything about her family."
    d "I'm sure you're aware of the cirumstances? And what happened?"
    scene a7202 with dssa
    sas "I know about the car crash. Nami lost both her parents and you lost your mother."
    scene a7203 with dssa
    d "My Father died there too."
    scene a7202 with dssa
    sas "No. Your father died a year before the accident."
    scene a7204 with dssr
    d "First time I've heard that."
    d "How do you know more about me than I do?"
    scene a7205 with dssa
    sas "Sedila is one of my best friends. I asked people about Nami and eventually, you were mentioned."
    scene a7204 with dssa
    d "I don't dare to ask Nami about it. This is a topic I'd not touch with a ten feet pole."
    scene a7206 with dssa
    pause 
    scene a7207 with dssa
    d "Do you know what happened between me and Nami when we were younger?"
    scene a7208 with dssa
    sas "No."
    scene a7209 with dssa
    d "Yeah, and I never want to go through that again."
    d "Nami and I are best friends now. I'm not risking that for someone I don't even know."
    scene a7210 with dssa
    d "For someone Nami apparently doesn't even want in her life." 
    d "Handle it with her and respect her decision but leave me out of it."
    scene a7211 with dssa
    sas "I fear you're the only one Nami even remotely listens to."
    scene a7251 with vpunch
    d "Listens to?"
    scene a7252 with dssa
    d "That insane Cheeto listens to no one."
    scene a7212 with dssr
    sas "Do you know the backstory of her and Sedi?"
    scene a7213 with dssa
    d "No, I don't. We never talked about it."
    d "In general, the Cheeto and I don't speak about things that happened before we moved to Wollust." 
    scene a7215 with dssr
    d "Because if we rolled up the past, Nami and I wouldn't talk to each other again for the rest of our lives."
    d "I assume the Cheeto has a reason why she's avoiding her... Even if it's a stupid one knowing Nami."
    scene a7214 with dssa
    sas "I'll give you an entire blister of pills if you get Nami to speak to Sedi."
    scene a7213 with dssa
    d "No."
    d "(Not worth risking my relationship with the Cheeto for a few pills... However, Sasha is ready to strike a deal for it should I need them again.)"
    scene a7216 with dssr
    d "All I know is that the Cheeto has a pending trustfund..."
    scene a7217 with dssa
    sas "She doesn't."
    scene a7218 with dssa
    d "I hear different things everywhere I go. Leave me out of it."
    scene a7219 with dssa
    pause 
    menu:
        "Maybe I'll nudge her into the right direction...":
            $ Cheeto_Sedi_Nudgy = True 
            scene a7220 with dssa
            sas "Thanks."
        "Don't risk it.":
            pass 
    scene a7221 with dssa
    pause 
    scene a7222 with dssa
    pause 
    scene a7223 with dssa
    sas "Hey."
    scene a7224 with dssr
    sas "No luck with [name]."
    scene a7225 with dssa
    pause 
    scene a7659 with dssr
    sedi "I see."
    scene a7658 with dssr
    sas "He seemed genuine when he said he didn't know who you were."
    scene a7659 with dssa
    $ persistent.SediName = True
    sedi "...So he wasn't ignoring me?"
    scene a7658 with dssa
    sas "No."
    scene a7660 with dssa
    sedi "...Even worse... She didn't even mention me."
    scene a7224 with dssr
    sas "That's not it."
    sas "Something between them has happened in the past. He was honest when he said that they never talk about it."
    scene a7661 with dssr
    pause 
    scene a7662 with dssa
    sedi "Okay. Will you come by and we'll head to the bar together?"
    scene a7224 with dssr
    sas "Nami and Zara need me for something... But we can pick you up?"
    scene a7663 with dssr
    sedi "I don't think Nami will like that."
    scene a7224 with dssr
    sas "Then she can leave." 
    scene a7664 with dssr
    pause
    scene a7226 with dssr
    n "Alright. We're leaving."
    scene a7227 with dssa
    pause 
    if RobinFriends is True:
        scene a7228 with dssa
        rob "Bye [name]. We'll see each other tonight."
        scene a7229 with dssa
        d "Yeh, bye."
    if MilaSleep5x0 is True:
        scene a7230 with dssr
        mi "I'll text you later."
        scene a7231 with dssa
        d "Sure."
        d "How are you getting home?"
        scene a7232 with dssa
        mi "Robin and Sasha will drop me off on the way."
        scene a7233 with dssa
        d "Alright. I'll see you tonight."
    scene black with Dissolve(2)
    with Pause(.5)
    scene a7234 with dssb
    pause 
    scene a7235 with dssa
    d "Yo Zara? Can you drop me off umm..."
    scene a7237 with dssa
    za "...Yes?"
    scene a7235 with dssa
    d "Cecilia Avenue 4."
    scene a7237 with dssa
    za "What's there?"
    scene a7236 with dssa
    d "Just drop me off there, please."
    scene a7238 with dssa
    za "Okay. Sure."
    scene a7239 with dssr
    "She observes you in the mirror."
    scene a7240 with dssa
    za "Do you also want me to pick you up again?"
    scene a7241 with dssa
    d "That's no-"
    scene a7242 with dssr
    n "I wanna go to Noji's house later, [name]... I need something from inside."
    scene a7243 with dssa
    d "Alright. I'd appreciate it if you could pick me up again."
    scene a7244 with dssa
    pause
    scene a7245 with dssa
    n "Sasha seemed mad there at the end. Did I do something?" 
    scene a7246 with dssa
    d "Sedi."
    scene a7247 with dssa
    pause 
    scene black with Dissolve(2)
    with Pause(.5)
    jump SonyaSunOfTheMorning









label SonyaSunOfTheMorning:
    scene a7257 with dssb
    pause
    scene a7258 with dssa
    u "What else?"
    scene a7259 with dssa
    ay "Both witnessed the execution of their older brothers."
    scene a7258 with dssa
    u "What about the parents?"
    scene a7260 with dssa
    ay "Why don't you go ask Mom, Aki?"
    scene a7261 with dssa
    aki "I don't see Mom anywhere close, bitch."
    scene a7262 with vpunch #maybe no vpunch
    pause
    scene a7263 with dssa
    "Adriana catches Ayua's arm before it can hit Aki."
    scene a7264a with dssr
    adri "Don't break Mama's rules. There shall be no violence where one goes to cleanse their body and mind."
    scene a7266 with dssr
    aki "So what about the parents? Did they make it out?"
    scene a7264 with dssa
    ay "An hour before the raid the kids were on their way to the airport but the parents had already been captured."
    scene a7268 with dssa
    aki "Are they terrorists?"
    scene a7269 with dssa
    ay "They are members of the Aftabe Sobh, which translates to the 'Morning Sun' rebels."
    ay "I know the young were all involved, but I don't know what they did exactly. Mom showed me a group picture a week ago."
    ay "I guess the government calls them terrorists... Mom and I see them as more. They're fighting for their freedom."
    scene a7270 with dssa
    aki "And they're both at ZPR?"
    scene a7271 with dssr
    ay "She is, but the brother doesn't speak the language and instead now works at grandpa's construction site."
    scene a7272 with dssa
    aki "Is that why Mom barely sleeps?"
    scene a7271 with dssa
    ay "Ya. She kept in contact with the mother."
    scene a7273 with dssa
    ay "Mom considers her a close friend."
    scene AkiSmoke with dssa
    ay "I don't think I've ever seen her like this."
    scene a7274 with dssa
    adri "Anything else notable?"
    scene a7285 with dssr
    ay "She's very pretty."
    scene a7286 with dssa
    adri "I'm aware. I've seen her at the Angel-shoot."
    scene a7287 with dssa
    ay "Really?"
    scene a7286 with dssa
    adri "Yup. Katie insisted on having her there."
    scene a7288 with dssa
    ay "I have no idea how mentally stable she is."
    scene a7289 with dssa
    ay "I sparred with her today... and the longer the grappling went on, the more real it felt... I think there's a lot of turmoil inside of her."
    ay "I wouldn't want to be anywhere near her when she explodes."
    scene a7275 with dssr
    aki "I thought they weren't terrorists."
    play sound "Music/Sfx/Slap4.ogg"
    scene a7276 with vpunch
    adri "*Chuckles* Shut up Aki."
    scene a7277 with dssa
    pause
    scene a7278 with dssr
    ay "I know Mom sent both to therapy because of the shit they experienced."
    scene a7293 with dssr
    adri "To Amber?"
    scene a7279 with dssr
    ay "No. To Dr. Solus."
    ay "Amber specializes in relationships and sex. Solus is a better fit for them."
    scene a7295 with dssr
    aki "I have no idea how I'd react if I saw you two executed in front of my eyes..."
    scene a7296 with dssa
    aki "Everyone would look at me with pity... 'Oooh, you poor thing- I can't even imagine the pain you must feel...'"
    aki "'The heartbreak... the uncertainty... being Dad's new favorite... Ouwww... The pressure..."
    scene a7297 with dssa
    aki "'Yet you carry on like the shining star that you are... You're an inspiration to us all, Aki.'"
    scene a7298 with dssa
    aki "Then the audience of whatever late night host I'm talking to, gets up and applauds... tears in their eyes, hopeful smiles on their faces..."
    aki "The moderator, touched by my life story, gets up from his chair, hugs me, and says-"
    scene a7299 with dssa
    aki "'You're what Ayua always aspired to be... and what Adrianna failed to be, and-'"
    scene a7300 with dssa
    aki "And if he's hot, we'll fuck on his desk after the audience is gone, and I'll blow both your urns a kiss."
    scene a7280 with dssr
    ay "Did you know that we've voted you 'least liked' of all the siblings?"
    scene a7302 with dssr
    pause 
    scene a7301 with dssa
    aki "So... you're telling me I placed first?"
    scene a7293 with dssr
    adri "Mom gave them clothes as well."
    scene a7290 with dssr
    ay "Yaah... I gave her some of the fetish underwear we wouldn't wear that Aki, Sasha and I stole from the Venus studio."
    scene a7291 with dssa
    ay "Now I feel bad... I didn't know the full story. I might take her shopping and get her some real underwear."
    scene a7292 with dssr
    adri "Are their parents still alive?"
    scene a7281 with dssr
    ay "I didn't dare to ask. Mom was very upset."
    scene a7282 with dssa
    adri "And Dad?"
    scene a7283 with dssa
    ay "He should be with Mom right now."
    scene a7294 with dssr
    adri "We should go and see if they need anything."
    scene a7303 with dssr
    aki "I wanted a massage..."
    scene a7304 with dssa
    adri "Get it afterward. Mom needs us."
    scene a7305 with dssa
    pause
    scene a7306 with dssa
    pause 
    scene a7307 with dssa
    pause 
    scene a7308 with dssa
    pause 
    scene a7309 with dssa
    pause 
    scene black with Dissolve(2)
    with Pause(.5)
    scene a7255 with dssb
    drs "*Farsi* My name is Dr. Solus."
    scene a7256 with dssa
    drs "*Farsi* I would like to extend a warm welcome to the both of you."
    scene a7253 with dssr
    pause #Sonya and the brother
    scene a7254 with dssr
    pause 
    stop music fadeout 3
    scene black with Dissolve(2)
    with Pause(.5)
    $ renpy.pause(0.2, hard=True)
    $ renpy.movie_cutscene("images/Animations/CH1-3/AngelxDivineSerpent.webm", stop_music=False)
    $ persistent.DivineSerpent = True
    $ play_playlist(playlist_MystyGood)
    scene a7310 with dssb 
    pause
    scene a7311 with dssa
    john "That's what we have."
    scene a7312 with dssa
    katie "Good."
    scene a7313 with dssr
    john "Why exactly don't you want me to cut out Sonya's clips?" 
    scene a7314 with dssa
    pause
    scene a7315 with dssr
    pause 
    scene a7316 with dssa
    katie "If I hadn't been pushed beyond my comfort zone, I wouldn't be where I am now."
    scene a7317 with dssr
    katie "Even if Sonya doesn't see it now, she'll appreciate it down the line."
    scene a7318 with dssa
    katie "Send it like that."
    scene a7319 with dssa
    john "Are you sure?"
    scene a7320 with dssa
    john "You might scare her off, and as a result, lose a very exotic model."
    scene a7321 with dssr
    "Katie keeps quiet."
    scene a7322 with dssr
    john "Have you thought about the circumstances she's in? Her aunt and uncle are conservative. If they find out about this- I doubt this will go very well."
    scene a7323 with dssa
    john "Miru said that both need therapy... This might be the wrong time."
    scene a7325 with dssa
    katie "If her uncle or aunt dare to punish her for it, I'll get involved. My house has many empty rooms."
    scene a7326 with dssa
    pause 
    scene a7324 with dssa
    katie "Trauma doesn't go away, you just learn to live with it. It becomes less invasive as times goes on."
    scene a7327 with dssa
    katie "I think both Sonya and Farhad need a purpose. Wollust needs to feel like home, not a pitstop."
    scene a7329 with dssa 
    pause 
    scene a7328 with dssa 
    john "You remind me more and more of-"
    scene a7330 with vpunch 
    katie "Don't you dare finish that sentence."
    scene a7331 with dssa 
    john "Thanks for proving my point."
    scene a7332 with dssr 
    john "We should go. Dana's waiting for you at the country club."
    scene a7333 with dssr 
    pause 
    scene a7334 with dssr
    pause
    stop music fadeout 5
    scene black with Dissolve(2)
    with Pause(.5)
    jump AmberS2x 

label AmberS2x:
    play music "Music/VeskyBeyondTheWindow.ogg" 
    scene a7335 with dssb 
    pause 
    scene a7336 with dssr 
    pause 
    scene a7337 with dssr
    am "Hello [name]."
    scene a7338 with dssa
    d "Hi."
    scene a7339 with dssr
    am "How are you feeling?"
    scene a7340 with dssa
    d "I'm alright... Slightly more aggitated than usual... but overall I'm alright."
    scene a7342 with dssr 
    am "We have a long trip in front of us. What are you thoughts about it?"
    scene a7341 with dssa 
    d "I haven't been to that town since... you know."
    d "We were pretty much chased out of there and never looked back."
    scene a7343 with dssr
    d "From neighbours that called the police on us for every little mishap, to Noji having to deal with racism from her colleagues and patients."
    d "It's a fucking shit hole and I would love to burn it to the ground."
    scene a7344 with dssa
    am "Do you think they will remember you?"
    scene a7345 with dssa
    d "Unlikely."
    scene a7346 with dssa
    am "I've read about the town San Tropic. A lot of people have left it since."
    am "It's never been in a good economic state, but in the recent years things have taken a turn for the worse."
    scene a7347 with dssa
    d "I met someone at college that went there too. Nia."
    if NiaDeal is True:
        d "She knew Summer. They were friends."
        scene a7348 with dssa
        pause
    scene a7349 with dssa
    am "After you left San Tropic, where did you finish school?" 
    scene a7350 with dssa
    d "That was somewhere in the north-east... Not too far from here."
    scene a7351 with dssa
    d "It wasn't a big school and to be honest, it's just a blur... Many missed days."
    scene a7352 with dssr
    d "I wasn't really present... Not really, yet somehow managed to get decent grades when I decided to go. Except for sports... I just didn't participate." 
    scene a7353 with dssa
    am "I assume nothing bad happened there?"
    scene a7352 with dssa
    d "I had a few fights, and a few weeks before graduation, I got an assault charge."
    scene a7353 with dssa
    am "What happened?"
    scene a7355 with dssa
    d "Long story short, the class clown went a little bit too far and I hit him with everything I had."
    d "I might have a small tendency to impulsive behavior."
    scene a7354 with dssa
    am "We'll work on that." 
    scene a7356 with dssr
    pause
    scene a7357 with dssa
    am "Do you feel confident enough for the trip?"
    scene a7358 with dssa
    d "I do."
    scene a7359 with dssr
    am "It will take us a few hours."
    scene a7360 with dssa
    d "And at least an hour or two to get to the cabin on foot. It's north-west of San Tropic."
    d "You might want to exchange your high heels for some boots."
    scene a7361 with dssr
    am "I figured."
    scene a7362 with dssa
    d "How come you managed to squeeze me in afterall?"
    scene a7363 with dssr
    am "This is my lunch time."
    scene a7364 with vpunch
    d "Oh Amber! You don't have to- I don't want you to do that!"
    scene a7365 with dssa
    am "It's okay, [name]."
    scene a7366 with dssr
    d "No. This is your break time..."
    if Amber_Moral_Highground is False:
        scene a7367 with dssa
        am "It's okaaay!"
    else:
        scene a7368 with dssa
        am "It's okaaay!"
        scene a7369 with dssr
        pause
    scene a7370 with dssr
    pause
    d "(It feels weird talking to her about San Tropic... She knows Noji... She knows exactly what San Tropic is.)"
    d "(I can't mention it until we're in the car and an hour in... I need to get to Amber without her having the chance to tell Noji.)"
    d "(And after that, I'll confront Noji based on what Amber tells me.)"
    scene a7371 with dssr
    pause 
    scene a7372 with dssa
    am "What are you thinking about?"
    scene a7375 with dssr
    "You let out a sigh."
    scene a7376 with dssr
    d "It never really mattered before but... This issue I have is starting to cause problems."
    d "I can't have an erection."
    scene a7373 with dssa
    am "I see."
    scene a7374 with dssa
    am "And you're getting closer to certain women?"
    if BellaNonExclusive5x0 is True:  
        scene a7377 with dssa
        d "Bella, to be frank."
        scene a7378 with dssa
        am "How's Bella dealing with it?"
        scene a7377 with dssa
        d "She has a patience and a level of understanding, I would never have expected from her."
        scene a7379 with dssa
        pause
        scene a7380 with dssa
        d "But I see that it affects her... and it negatively affects me seeing her like this."
        scene a7381 with dssr
        d "The way she looks at me when she says that it's okay... I can see the disappointment in her eyes."
        scene a7382 with dssa
        d "...It hurts."
    else:
        scene a7377 with dssa
        d "Yeah..."
        scene a7381 with dssa
        d "And I know it's going to cause a lot of problems."
    d "We're in college... It's only a matter of time until she moves on because I can't give her what she desires."
    d "And even if she doesn't, it's going to linger over us like a giant shadow."
    scene a7383 with dssr
    pause
    scene a7384 with dssr
    pause 
    scene a7385 with dssa
    d "I need to find a solution."
    scene a7386 with dssr
    am "If penetration isn't an option right now, perhaps you should look into alternatives."
    scene a7387 with dssa
    d "College revealed something to me... Something I had buried under pretextual reasons..."
    scene a7388 with dssa
    "Amber leans in closer and listens carefully."
    scene a7389 with dssa
    d "It's not what I felt for Summer that keeps me... from touching someone..."
    scene a7390 with dssa
    d "It's so irrational but I can't turn it off... I want to do more but the thought alone invokes goosebumps." 
    d "My heart feels like it's going to burst..."
    scene a7391 with dssa
    pause 
    scene a7392 with dssa
    am "Start slowly from the beginning... Not when everything took a bad turn... But from the beginning..."
    scene a7393 with dssr
    d "There's a 'shadow' that lingers over my current relationships... Every time they touch me."
    scene a7394 with Dissolve(2)
    d "Some people trigger it more than others... Yet, I feel a strange connection to those people... It's more- or appears more familiar."
    scene a7395 with dssr
    pause #shadow preview ani
    play sound "Music/Sfx/Punch.ogg"

    scene a7396 with vpunch
    d "No- I- I can't go there today... Fuck that."
    scene a7397 with dssa
    d "I have- I have that bar opening... I can't go there today, Amber... I'd be a fucking wreck."
    scene a7398 with dssr
    am "That's okay."
    am "We'll talk about this 'shadow' on our trip."
    scene a7399 with dssa
    d "Thanks." 
    d "I had a panic attack the other day at the book club."
    scene a7398 with dssa
    am "I didn't notice it. When did it happen?"
    scene a7399 with dssa
    d "At the end. I went upstairs and it just hit me like a truck... Probably the worst one I've had."
    scene a7400 with dssr
    am "Do you have any idea what could've caused this?"
    scene a7401 with dssa
    d "Overstimulation perhaps? There were so many people talking to me that day... I probably just couldn't take it anymore."
    d "Especially the members of the book club... Their words and giggles were drilling into my brain..."
    scene a7400 with dssa
    am "I can ask them to take it easier with you."
    scene a7402 with dssr
    d "No."
    d "I don't want to be the 'special' kid."
    d "I want to be normal. I don't want anyone to treat me like I'm retarded."
    scene a7403 with dssa
    am "You-"
    d "Sa-"
    scene a7404 with dssa
    d "Sorry, I didn't want to interrupt."
    scene a7405 with dssa
    am "No, please. Go ahead."
    scene a7406 with dssa
    d "Who I was about to mention was Sasha."
    d "She gave me a pill that almost instantly calmed me down."
    d "...Maybe it can help me bridge the gap?"
    scene a7407 with dssr
    am "They can help you overcome difficult times, I agree."
    am "But... I don't want to prescribe you any medication yet."
    scene a7408 with dssa
    d "Why not?"
    scene a7409 with dssa
    am "We still have to figure out what exactly causes your panic attacks."
    am "And if you start taking medication, this will be a much longer and perhaps, fruitless journey."
    scene a7410 with dssa
    am "I believe in gradual exposure therapy."
    scene a7411 with dssa
    d "This doesn't feel gradual. I feel like I'm dying every time."
    scene a7412 with dssr
    am "I can prescribe you something that could dampen the effect of a panic attack."
    am "But I'd like to wait with anything heavy until we figured out what exactly causes these reactions in you."
    scene a7413 with dssa
    am "Then we'll slowly venture through the 'shadows' and use medication if needed."
    scene a7415 with dssa 
    pause 
    scene a7414 with dssa
    d "Can you give me something for tonight?"
    scene a7416 with dssa
    am "No. Mixing any sort of pharmaceuticals with a lot of alcohol is a bad idea."
    am "And I won't take your word that you won't drink."
    am "I will have something for you when we take the trip the day after tomorrow."
    scene a7414 with dssa
    "You nod."
    scene a7417 with dssr 
    am "I think it's best to end here for today. You said yourself you don't want to explore this any further because you're going out tonight."
    scene a7418 with dssa 
    d "Yeah."
    d "And I'd like you to have at least a little bit of a lunch break."
    if Amber_Moral_Highground is True:
        d "Even though, a part of me thinks you're about to star in an adult movie."
        scene a7419 with vpunch 
        am "What?"
        scene a7420 with dssr 
        d "Your outfit. I only really know therapists from shows and movies. They're mostly dressed very conservatively."
        scene a7421 with dssr 
        d "The only ones I've ever seen dressed like this, are in porn."
        scene a7422 with dssr
        am "I sometimes forget that you don't have a filter."
        scene a7423 with dssa
        d "I have one. But I don't care to use it as often as others."
        scene a7424 with dssa
        am "Well, I can assure you, that I'm not about to film an adult movie." 
        scene a7425 with dssr
        am "I work primarely with women, [name]. They don't mind it. Quite the oppossite, it gives me credit."
        d "I heard that you focus primarily on sexual issues?"
        scene a7426 with dssa
        am "Most of my clients are here for that reason, yes. I assist couples through various phases of their relationships."
        scene a7427 with dssa
        d "I see. I guess it makes sense then."
        d "You don't, by any chance, got a copy of your book here?"
        scene a7428 with dssa
        am "Why?"
        scene a7429 with dssa
        d "I might find something interesting in there... and I really want to quote out of it to tease Bella."
        scene a7430 with dssa
        am "*Chuckles* No!"
        scene a7431 with dssr
        am "You will not use my book against my own daughter!"
        scene a7432 with dssa
        d "I swear, I won't overdo it."
        scene a7433 with dssa
        am "I'll get you a copy, but..."
        scene a7434 with dssa
        am "Only if you promise to read it fully."
        scene a7435 with dssa
        with Pause(.3)
        menu:
            "Agree.":
                $ Amber_Book = True 
                if SashaBook5x0 is True:
                    $ Book_Conflict = True 
                scene a7436 with dssa
                am "I'll get you a copy on Wednesday."
                scene a7437 with dssa
                d "Can you sign it too?"
                scene a7438 with dssa
                pause #smiles 
            "I don't think I have the time right now.":
                $ Amber_Book_On_Ice = True 
                scene a7439 with dssa
                am "Perhaps we can get back to this when you do have time."
                am "I'd be interested in the thoughts of a much younger male."
    scene a7440 with dssr
    am "I'll call you tomorrow with the exact time. But Wednesday, roughly 2PM."
    am "Have fun tonight."
    scene a7441 with dssa
    d "Thanks."
    scene a7442 with dssr
    pause 
    stop music fadeout 5
    scene black with Dissolve(2)
    with Pause(.5)
    scene a7443 with dssr
    pause #in ihrer lobby #Child noises laughter
    scene a7444 with dssr
    pause 
    scene a7445 with dssa 
    pause 
    scene a7448 with vpunch 
    su "That's the worst part of the song!"
    scene a7449 with dssa 
    d "It's the best part of the song!"
    scene a7450 with vpunch 
    su "Ugh! Were you born without taste buds?" 
    scene a7451 with dssa 
    d "You have no taste, bibi head."
    scene a7452 with dssa 
    d "I gotta get back before six."
    scene a7453 with vpunch 
    su "What are you waiting for! Out, out!"
    scene a7454 with dssr  
    pause 
    scene a7455 with dssa  
    su "Remember we're going to play badminton at school tomorrow."
    scene a7456 with dssa  
    su "You might beat me in basketball, but tomorrow, I'll show you what I'm made of!"
    scene a7457 with dssa  
    play music "Music/OST/A.W - Darkness Inside.ogg"
    d "I thought we had established that you're made of jello."
    scene a7458 with dssa  
    pause 
    scene a7459 with dssa  
    su "Hi Mom! [name] was just about to leave."
    scene a7460 with dssr 
    pause 
    scene a7461 with Dissolve(2)
    pause 
    play sound "Music/Sfx/Slap4.ogg"
    scene a7446 with vpunch
    pause 
    scene a7447 with dssr
    d "(If I want to get through tonight, I'll need another pill from Sasha...)" 
    stop music fadeout 5
    scene black with Dissolve(2)
    with Pause(.5)
    jump HomeEnd5x5





label HomeEnd5x5:
    scene a7973 with dssr
    pause
    play sound "Music/Sfx/Open_Gate_Metal.ogg"
    scene a7974 with dssr
    pause
    scene a7970 with dssr
    pause
    scene a7971 with dssr
    pause
    scene a7972 with dssr
    "You push the ignition as if you expected it to start."
    scene a7462 with dssb  
    pause
    scene a7499 with dssb 
    pause 
    scene a7500 with dssr
    pause  
    scene a7501 with dssa
    $ play_playlist(playlist_Smooth)
    if BellaNonExclusive5x0 is True: 
        b "As I was saying, nothing worked. I tried the casual approach, the slutty, the funny... Nothing."
        if Bellchen_Fingered_1x0 is True:
            scene a7502 with dssa
            b "Okay, not nothing... like- today I wore a a top with an underboob to college and got a little bit of action..."
        else:
            scene a7503 with dssa
            b "Like today I wore a a top with an underboob to college! That's how far I'm willing to go!"
        scene a7504 with dssr
        desi "And what is it that you're doing now?"
        scene a7505 with dssr
        b "I call it..."
        scene a7506 with dssr
        b "The Amber."
        scene a7507 with dssa
        b "Meaning, I'll be dressing like a normal, well adjusted person. No cleavage."
        scene a7508 with dssa
        desi "Amber often wears cleavages. Isn't she well adjusted?"
        scene a7509 with dssa
        b "Yah, but she's old enough where it becomes graceful. She has that aura."
        b "I'm still three major bad decisions and a year as a monk away from that."
        scene a7510 with dssr
        desi "He seems to be one of a kind if you're going to such length to get close to him."
        scene a7511 with dssa
        b "Mhm."
        scene a7513 with dssa
        emi "I looked into the guy."
        scene a7512 with dssa
        b "Why?"
        scene a7515 with dssr
        emi "You never know who someone really is."
        scene a7513 with dssr
        b "Okay? And who is he?"
        scene a7514 with dssa
        b "Oh and- if it says he worked as a gay stripper, I'm not surprised."
        scene a7515 with dssr
        emi "Besides an incident years ago and an assault charge, I found nothing on him. He's just a normal boy."
        emi "I found an aunt of his, I'm not sure if he's aware of her."
        scene a7516 with dssa
        b "I can tell him about it."
        scene a7517 with dssa
        emi "Do you know who Nami is?"
        scene a7518 with dssa
        b "I do. A Revera."
        scene a7517 with dssa
        emi "Have you talked to her?"
        b "No, quite the opposite. I pulled a prank on her."
        scene a7519 with dssr
        emi "Why would you do that?"
        scene a7525 with dssr
        b "Because as soon as Nami gets involved in my circle of friends, it might no longer be."
        b "Ayua told me that Nami refuses to talk to Sedila... and there are different opinions on who's in the right."
        b "Most side with Sedila, and say that Nami is unreasonable."
        scene a7526 with dssa
        b "However, Nami has the potential to cause a lot of drama."
        scene a7527 with dssa
        pause 
        scene a7520 with dssr
        emi "And what did you expect to happen when you pulled a prank on Nami?"
        scene a7528 with dssr
        b "..."
        scene a7529 with dssa
        desi "I hope this wasn't your way of trying to befriend her."
        scene a7521 with dssr
        pause 
        scene a7522 with dssa
        emi "You can't be serious, Bella..."
        scene a7523 with vpunch
        emi "Do you not know how to make friends the normal way?!"
        scene a7530 with dssr
        b "Listen old man. Two things went wrong... First, she showed up much later than I asked her to... Second: A prof showed up and escorted her out."
        scene a7531 with dssa
        b "My plan was to establish a friendly, but competitive base."
        scene a7532 with dssa
        emi "Did you apologize?"
        scene a7533 with dssa
        "Bella laughs in a weird, hysterical way."
        scene a7534 with dssa
        b "Y-yeah... Me... Apologizing. Good one."
        scene a7535 with dssr
        emi "Desiree, be careful not to cut away the little part of her brain that's still left."
        scene a7536 with dssr
        emi "I hope you're not using the boy to get to her."
        scene a7537 with vpunch
        b "Of course not! What do you think of me?"
        scene a7538 with dssa
        b "That bitch is actually..."
        scene a7539 with dssa
        pause
        scene a7540 with dssa
        b "I like him... I really do."
        scene a7524 with dssa
        emi "Good. I'll expect him as your plus one at the next gala."
        scene a7541 with dssa
        pause
        scene a7542 with dssa
        pause 
        scene a7543 with dssa
        emi "Ahh Miss Petrova."
        scene a7544 with dssa
        emi "How are you, darling?"
        scene a7545 with dssa
        sas "I'm good."
        scene a7546 with dssa
        emi "We're almost done with the cripple over there."
        b "Shut up."
        scene a7547 with dssr
        pause 
        scene a7548 with dssa
        emi "Sasha, you're good friends with Sedi, right?"
        scene a7549 with dssa
        sas "Yes."
        scene a7549a with dssa
        emi "Did you know that Bella tried to befriend her little sister and failed miserably?"
        scene a7559 with dssr
        b "I'll never tell you anything again and this is the last time I came here."
        scene a7560 with dssa
        b "Desi, I'll give you five grand if you replace the milk in his morning coffee with bleach."
        scene a7550 with dssr
        sas "I didn't. No."
        sas "I hope it wasn't through that miserable prank of yours?"
        scene a7561 with dssr
        b "Miserable? It was good."
        scene a7551 with dssr
        sas "Good if you intended to cause long lasting damage. Not to make a new friend."
        scene a7552 with dssa
        b "It was Ayua's idea."
        scene a7551 with dssa
        sas "By this point, you should know better than to entertain any idea Ayua has ever come up with."
        scene a7562 with dssr
        b "I was lying. It was my idea."
        scene a7563 with dssa
        b "But big words coming from you."
        scene a7555 with dssr
        sas "If you want, I can talk to Nami."
        scene a7563 with dssr
        b "Who do you think you're talking to, Sasha?"
        scene a7556 with dssr
        sas "Someone whose emotional maturity rivals that of a naked mole rat?"
        scene a7564 with dssr
        pause 
        scene a7565 with dssa
        b "Exactly."
        scene a7554 with dssr
        sas "I'll speak to her."
        scene a7553 with dssa
        b "No."
        scene a7554 with dssa
        sas "Too late. I've already decided."
        scene a7566 with dssr
        b "Desiree, please fuck up her hair."
        b "Not that it could be much worse."
        scene a7557 with dssr
        sas "You look like a budget version of your goth phase."
        scene a7558 with dssr
        b "Please..."
        scene a7567 with dssr
        b "With the way you're dressed, I can't tell if you're slumming it ironically or if your trust fund finally dried up."
        b "No wonder you came in from the back. I wouldn't want anyone to see me like that either."
        scene a7583 with dssr
        sas "Nothing was as bad as your 'rebellious heiress' phase. Newsflash: Katie doesn't do grunge."
        scene a7568 with dssr
        b "For someone with an oligarch grandfather, you dress like you're in line for a bread ration."
        scene a7582 with dssr
        b "Or perhaps as a very expensive Russian escort."
        scene a7583 with dssa
        sas "I recall your goth phase. It was basically a collection of bad decisions in fishnets."
        scene a7569 with dssr
        b "You talk a lot for someone whose idea of romance is sharing eye contact over overpriced lattes."
        scene a7584 with dssr
        sas "Your idea of emotional growth is switching from black nail polish to neutral tones."
        scene a7569 with dssr
        b "If being 'mysteriously unavailable' was a skill, you'd have a PhD by now. Keep it up, and your retirement plan will be knitting sweaters for your pets."
        scene a7570 with dssa
        b "Oh, I forgot to ask... are you even allowed to have pets?"
        scene a7585 with dssr
        sas "[name] can soon join a support group if the assignment goes on any longer."
        scene a7571 with dssr
        b "You don't need a support group, you just need one outfit that won't make your mom pour another glass of wine."
        b "Your idea of conflict resolution is a pair of heels and a crop top."
        scene a7586 with dssr
        sas "When I came in here, I hardly recognized you without your usual statement neckline."
        scene a7587 with dssa
        b "I'm not sure what's more scandalous... Your book club picks or the divorce rate it inspires."
        scene a7588 with dssa
        sas "Your leggings are often so minimalist. They really redefine the concept of leaving nothing to the imagination."
        scene a7572 with dssr
        b "I've seen less tension in a courtroom than when you enter a room of married couples."
        scene a7573 with dssa
        b "Regarding the book club... I find it weird that you're wearing your 'mom-scandal' cleavages to a place your Mom doesn't even visit. Care to explain?"
        play sound "Music/Sfx/Punch.ogg"
        scene a7589 with vpunch
        sas "What a load of cra-"
        scene a7590 with dssa
        pause
        scene a7574 with dssr
        b "I win."
        scene a7591 with dssr
        emi "Are you two done?"
        scene a7592 with dssa
        sas "I'll finish with..."
        scene a7593 with dssr
        sas "[name]'s cute, but I didn't realize emotionally unavailable was your type again."
        scene a7575 with dssr
        pause
        play sound "Music/Sfx/Vibration_Phone.ogg"
        scene a7576 with dssa #sfx vibrations
        pause 
        scene a7577 with dssa
        b "Speaking of the emotional unavailable..." 
        stop sound
        scene a7578 with dssa
        b "Hey."
        scene a7646 with dssr
        d "Hi."
        d "Do you have a minute?"
        scene a7647 with dssa
        b "It depends. What's up?"
        scene a7645 with dssr
        pause
        d "Never mind."
        scene a7579 with vpunch
        b "HEY! No! What's up?"
        scene a7648 with dssr
        pause
        d "Nah, it's okay."
        scene a7580 with dssr
        b "Idiot."
        scene a7581 with dssa
        b "...You know know you can talk to me about... things."
        scene a7628 with dssr
        b "One moment." 
        scene a7629 with dssr #besser andere trans
        b "I'm listening."
        scene a7630 with dssa
        d "...I don't know what's going on but I feel so angry all the time."
        scene a7631 with dssr
        d "I must be clinically insane as well... as the only person I wanted to speak to was you..."
        if BellaCropTop is True:
            b "I thought we had established that you're addicted to my lady parts."
        b "When did the mood issues start?"
        scene a7649 with dssr
        d "Yesterday. Shortly before I headed to the basketball practice."
        d "I think I'm slowly getting overwhelmed."
        scene a7632 with dssr
        b "It makes sense."
        b "You're doing too much and you don't have an outlet."
        scene a7633 with dssa
        d "I have sports."
        scene a7632 with dssa
        b "No. It's not enough. You're missing an emotional component... Sex would be great..."
        b "*Mumbles* Exclusively in my bed..."
        scene a7650 with dssr
        pause
        scene a7634 with dssr
        b "Are you alone?"
        scene a7635 with dssa
        d "No, Zara and Nami are somewhere around."
        scene a7634 with dssa
        b "Why do you think you called me when you could've talked to them?"
        scene a7635 with dssa
        "You keep quiet."
        scene a7634 with dssa
        b "Do you want me to come over?"
        scene a7636 with dssa
        b "We can fight or wrestle... You can let all your frustrations out on me."
        scene a7637 with dssa
        b "Or I'll peg you and let all my frustrations out on you."
        scene a7655 with dssr
        d "No."
        b "Good call. I'm just getting my hair done."
        d "But I want to see you at the bar tonight."
        scene a7638 with dssr
        b "I'll be there."
        scene a7639 with dssa
        d "Thanks for the talk."
        scene a7640 with dssa
        b "I have something that will cheer you up."
        scene a7651 with dssr
        d "What is it?"
        scene a7654 with dssa
        pause
        scene a7656 with dssr
        pause
        scene a7643 with dssa
        pause
        scene a7652 with dssr
        b "Did it cheer you up?"
        menu:
            "Oh, I expected a pic of your boobs.":
                scene a7653 with dssa
                d "I expected a pic of your boobs." 
                scene a7654 with dssa #sfx vibrates 
                pause
                scene a7657 with dssr
                pause 
                scene a7644 with dssr
                pause 
                b "Happy?"
                d "Happy."
            "It did.":
                scene a7653 with dssa
                d "A little."
        scene a7640 with dssr
        b "Make it 'til tonight without putting a rope around your neck, and I'll cheer you up in person."
        scene a7641 with dssa
        d "Seeing you in person usually has the opposite effect."
        scene a7640 with dssa
        b "Fuck you."
        scene a7639 with dssa
        d "Alright. Later then..."
        scene a7640 with dssa
        b "Bye."
        scene a7642 with dssa
        pause 
        scene a7595 with dssr #transition
        pause 
        scene a7594 with dssa
        sas "Are you and [name] official?"
        scene a7596 with dssa
        b "No. We're casual."
        scene a7597 with dssa
        sas "Good."
        scene a7598 with dssa
        b "Why's that good?"
        scene a7597 with dssr
        if RobinFriends is True:
            sas "I can see the appeal... but he's got more emotional twists than a spy novel."
            scene a7599 with dssa
            sas "What makes him dangerous is that he's the kind of guy who can make impulsive seem romantic."
            scene a7607 with dssr
            "Bella grins."
            scene a7608 with dssa
            b "He's right up your alley, isn't he?"
            scene a7600 with dssr
            sas "Excuse me?"
            scene a7609 with dssr
            b "*Sensual* All those perfect, ivy-league guys don't stand a chance against someone who's as messy and chaotic as your 'Mama was mean to me' wardrobe."
            scene a7601 with dssr
            sas "Desiree? Did you cut away a part of her frontal lobe?"
            scene a7609 with dssr
            b "Keep pretending to be an angel, Sasha. We both know fallen angels like you thrive on a little heat... All it takes for you to remember how to fall is someone like him." 
            scene a7602 with dssr
            sas "This might be the dumbest thing you've ever said."
            scene a7609 with dssr
            b "I've seen the dates your Mom begs you to go on. The guys are... Chef's kiss... handsome, rich, succesful, sometimes even famous... yet, has anyone ever gotten a second date?"
            b "Because deep down... you'd ride the unhinged train straight to hell before you let Prince Fucking Charming hold your hand."
            scene a7610 with dssa
            b "But you're very polite... Maybe you'd let him watch."
            scene a7603 with dssr
            sas "You live in your own world."
            scene a7611 with dssr
            pause
            scene a7612 with dssa
            b "Don't we all?"
            scene a7613 with dssr
            pause 
            scene a7604 with dssa
            sas "It was fun. A few of yours were a little far stretched and didn't have the desired effect. But overall, a solid performance for a naked mole rat."
            scene a7605 with dssa
            b "It was fun, but considering the hourly rate I paid for your escort services, I expected a little more. Perhaps put that mouth to a better use next time."
        else:
            sas "Bella, you'll need someone to balance you out, not someone who's racing you to see who can make the worse decision faster."
            scene a7598 with dssa
            b "Don't you worry about it."
            if MilaVenus is True:
                scene a7981 with dssr
                sas "I'd keep an eye on Mila if I was you."
                scene a7982 with dssa
                if BellaSuspicious is True:
                    $ BellaSuspicious_Mila_STG2 = True
                    pause 
                    scene a7983 with dssa
                    sas "You noticed it yourself." 
                    scene a7985 with dssr
                    pause 
                    scene a7986 with dssa
                    b "What did they do?"
                    scene a7984 with dssr
                    sas "He took some sexy pictures of her."
                    scene a7986 with dssr
                    b "I see."
                    if BTY2 is True:
                        $ BellaSuspicious_Mila_STG2 = False
                else:
                    $ BellaSuspicious_Mila = True
                    $ BellaSuspicious = True 
                    b "And why's that?"
                    scene a7983 with dssa
                    sas "Today when they viewed the house, I noticed they were getting kinda close."
                    scene a7986 with dssr
                    b "How close?"
                    scene a7984 with dssr
                    sas "He took a sexy picture of her."
                    scene a7986 with dssr
                    b "I see."
            elif ZaraTeasing is True:
                scene a7981 with dssr
                sas "I'd keep an eye on Zara if I was you."
                scene a7987 with dssr
                b "Why?"
                scene a7983 with dssa
                sas "She seems oddly attached to him. I've not seen her like that before."
                scene a7986 with dssr
                b "I see."
                $ BellaSuspicious = True 
                $ BellaSuspicious_Zara = True
        pass 
    else:
        b "So no. There is nothing between him and me."
        scene a7504 with dssr
        desi "I thought he was cute."
        scene a7501 with dssr
        b "Meh."
        scene a7502 with dssr
        b "I tried to get that look from him... if you know what I mean."
        b "I don't like him."
        scene a7504 with dssr
        desi "Don't you act like that. I could see that you were fond of him."
        scene a7509 with dssr
        b "He's weird."
        b "But it's not supposed to be."
        scene a7512 with dssr
        if BellaKiss3x5 is False:
            b "At least I didn't get the feeling he was interested."
            b "And I know when a guy wants me."
            scene a7513 with dssa
            desi "What isn't can still be."
            scene a7512 with dssa
            b "Not interested. I like being single."
        else:
            b "Maybe something could've been... Maybe not... Who knows."
            scene a7513 with dssa
            desi "You've got many years of college ahead of you."
            scene a7512 with dssa
            b "Yeah... Who knows."
            scene a7514 with dssa
            b "But I like being single!"
            b "I can do whatever I want without having to answer to anyone!"
        scene a7508 with dssr
        desi "I wasn't talking about marrying him."
        scene a7509 with dssa
        b "More like a rental option?"
        scene a7513 with dssa
        emi "I looked into the boy."
        scene a7512 with dssa
        b "Why?"
        scene a7515 with dssr
        emi "You never know who someone really is."
        scene a7512 with dssr
        b "Okay? And who is he?"
        scene a7514 with dssa
        b "Oh and- if it says he worked as a gay stripper, I'm not surprised."
        scene a7515 with dssr
        emi "Besides an incident years ago and an assault charge, I found nothing on him. He's just a normal boy."
        emi "I found an aunt of his, I'm not sure if he's aware of her."
        scene a7516 with dssa
        b "I can tell him about it."
        scene a7517 with dssa
        emi "Do you know who Nami is?"
        scene a7518 with dssa
        b "I do. A Revera."
        scene a7517 with dssa
        emi "Have you talked to her?"
        scene a7518 with dssa
        b "No, quite the opposite. I pulled a prank on her."
        scene a7519 with dssr
        emi "Why would you do that?"
        scene a7525 with dssr
        b "Because as soon as Nami gets involved in my circle of friends, it might no longer be."
        b "Ayua told me that Nami refuses to talk to Sedila... and there are different opinions on who's in the right."
        b "Most side with Sedila, and say that Nami is unreasonable."
        scene a7526 with dssa
        b "However, Nami has the potential to cause a lot of drama."
        scene a7527 with dssa
        pause 
        scene a7520 with dssr
        emi "And what did you expect to happen when you pulled a prank on Nami?"
        scene a7528 with dssr
        b "..."
        scene a7529 with dssa
        desi "I hope this wasn't your way of trying to befriend her."
        scene a7521 with dssr
        pause 
        scene a7522 with dssa
        emi "You can't be serious, Bella..."
        scene a7523 with vpunch
        emi "Do you not know how to make friends the normal way?!"
        scene a7530 with dssr
        b "Listen old man. Two things went wrong... First, she showed up much later than I asked her to... Second: A prof showed up and escorted her out."
        scene a7531 with dssa
        b "My plan was to establish a friendly, but competitive base."
        scene a7532 with dssa
        emi "Did you apologize?"
        scene a7533 with dssa
        "Bella laughs in a weird, hysterical way."
        scene a7534 with dssa
        b "Y-yeah... Me... Apologizing. Good one."
        scene a7535 with dssr
        emi "Desiree, be careful not to cut away the little part of her brain that's still left."
        scene a7541 with dssa
        pause
        scene a7542 with dssa
        pause 
        scene a7543 with dssa
        emi "Ahh Miss Petrova."
        scene a7544 with dssa
        emi "How are you, darling?"
        scene a7545 with dssa
        sas "I'm good."
        scene a7546 with dssa
        emi "We're almost done with the cripple over there."
        b "Shut up."
        scene a7547 with dssr
        pause 
        scene a7548 with dssa
        emi "Sasha, you're good friends with Sedi, right?"
        scene a7549 with dssa
        sas "Yes."
        scene a7548 with dssa
        emi "Did you know that Bella tried to befriend her little sister and failed miserably?"
        scene a7559 with dssr
        b "I'll never tell you anything again and this is the last time I came here."
        scene a7560 with dssa
        b "Desi, I'll give you five grand if you replace the milk in his morning coffee with bleach."
        scene a7550 with dssr
        sas "I didn't. No."
        sas "I hope it wasn't through that miserable prank of yours?"
        scene a7561 with dssr
        b "Miserable? It was good."
        scene a7551 with dssr
        sas "Good if you intended to cause long lasting damage. Not to make a new friend."
        scene a7552 with dssa
        b "It was Ayua's idea."
        scene a7551 with dssa
        sas "By this point, you should know better than to entertain any idea Ayua has ever come up with."
        scene a7562 with dssr
        b "I was lying. It was my idea."
        scene a7563 with dssa
        b "But big words coming from you."
        scene a7555 with dssr
        sas "If you want, I can talk to Nami."
        scene a7563 with dssr
        b "Who do you think you're talking to, Sasha?"
        scene a7556 with dssr
        sas "Someone whose emotional maturity rivals that of a naked mole rat?"
        scene a7564 with dssr
        pause 
        scene a7565 with dssa
        b "Exactly."
        scene a7554 with dssr
        sas "I'll speak to her."
        scene a7553 with dssa
        b "No."
        scene a7554 with dssa
        sas "Too late. I've already decided."
        scene a7566 with dssr
        b "Desiree, please fuck up her hair."
        b "Not that it could be much worse."
        scene a7557 with dssr
        sas "You look like a budget version of your goth phase."
        scene a7558 with dssr
        b "Please..."
        scene a7567 with dssr
        b "With the way you're dressed, I can't tell if you're slumming it ironically or if your trust fund finally dried up."
        b "No wonder you came in from the back. I wouldn't want anyone to see me like that either."
        scene a7583 with dssr
        sas "Nothing was as bad as your 'rebellious heiress' phase. Newsflash: Katie doesn't do grunge."
        scene a7568 with dssr
        b "For someone with an oligarch grandfather, you dress like you're in line for a bread ration."
        scene a7582 with dssr
        b "Or perhaps as a very expensive Russian escort."
        scene a7583 with dssa
        sas "I recall your goth phase. It was basically a collection of bad decisions in fishnets."
        scene a7569 with dssr
        b "You talk a lot for someone whose idea of romance is sharing eye contact over overpriced lattes."
        scene a7584 with dssr
        sas "Your idea of emotional growth is switching from black nail polish to neutral tones."
        scene a7569 with dssr
        b "If being 'mysteriously unavailable' was a skill, you'd have a PhD by now. Keep it up, and your retirement plan will be kniiting sweaters for your pets."
        scene a7570 with dssa
        b "Oh, I forgot to ask... are you even allowed to have pets?"
        scene a7585 with dssr
        sas "[name] can soon join a support group if the assignment goes on any longer."
        scene a7571 with dssr
        b "You don't need a support group, you just need one outfit that won't make your mom pour another glass of wine."
        b "Your idea of conflict resolution is a pair of heels and a crop top."
        scene a7586 with dssr
        sas "When I came in here, I hardly recognized you without your usual statement neckline."
        scene a7587 with dssa
        b "I'm not sure what's more scandalous... Your book club picks or the divorce rate it inspires."
        scene a7588 with dssa
        sas "Your leggings are often so minimalist. They really redefine the concept of leaving nothing to the imagination."
        scene a7572 with dssr
        b "I've seen less tension in a courtroom than when you enter a room of married couples."
        scene a7573 with dssa
        b "Regarding the book club... I find it weird that you're wearing your 'mom-scandal' cleavages to a place your Mom doesn't even visit. Care to explain?"
        play sound "Music/Sfx/Punch.ogg"
        scene a7589 with vpunch
        sas "What a load of cra-"
        scene a7590 with dssa
        pause
        scene a7574 with dssr
        b "I win."
        scene a7591 with dssr
        emi "Are you two done?"
        scene a7592 with dssa
        sas "Mhm..."
        scene a7593 with dssa 
        sas "Are you and [name] a thing?"
        scene a7596 with dssr 
        b "No."
        scene a7597 with dssr 
        sas "I heard rumors but I wanted to confirm them with you."
        scene a7598 with dssa 
        if BellaOnIce5x0 is True:
            b "We decided not to go for it."
            scene a7597 with dssa 
            sas "Good call."
        else:
            b "No. There's nothing between us."
            scene a7597 with dssa 
            sas "I think that's for the better."
        scene a7598 with dssa 
        b "Why?"
        scene a7599 with dssa 
        sas "He's emotionally unavailable... and frankly, a little unhinged."
        scene a7607 with dssr
        "Bella grins."
        scene a7608 with dssa
        b "He's right up your alley, isn't he?"
        scene a7600 with dssr
        sas "Excuse me?"
        scene a7609 with dssr
        b "*Sensual* All those perfect, ivy-league guys don't stand a chance against someone who's as messy and chaotic as your 'Mama was mean to me' wardrobe."
        scene a7601 with dssr
        sas "Desiree? Did you cut away a part of her frontal lobe?"
        scene a7609 with dssr
        b "Keep pretending to be an angel, Sasha. We both know fallen angels like you thrive on a little heat... All it takes for you to remember how to fall is someone like him." 
        scene a7602 with dssr
        sas "This might be the dumbest thing you've ever said."
        scene a7609 with dssr
        b "I've seen the dates your Mom begs you to go on. The guys are... Chef's kiss... handsome, rich, succesful, sometimes even famous... yet, has anyone ever gotten a second date?"
        b "Because deep down... you'd ride the unhinged train straight to hell before you let Prince Fucking Charming hold your hand."
        scene a7610 with dssa
        b "But you're very polite... Maybe you'd let him watch."
        scene a7603 with dssr
        sas "You live in your own world."
        scene a7611 with dssr
        pause
        scene a7612 with dssa
        b "Don't we all?"
        scene a7613 with dssr
        pause 
        scene a7604 with dssa
        sas "It was fun. A few of yours were a little far stretched and didn't have the desired effect. But overall, a solid performance for a naked mole rat."
        scene a7605 with dssa
        b "It was fun, but considering the hourly rate I paid for your escort services, I expected a little more. Perhaps put that mouth to a better use next time."
    scene a7614 with dssr
    b "Thank you Emilio. Thank you Desi."
    scene a7615 with dssa
    b "I hope you both die in a very painful way."
    scene a7616 with dssa
    emi "You're welcome, honey."
    scene a7617 with dssa
    desi "Get home safe."
    scene a7618 with dssr
    b "You should ask Sonya for a hijab, maybe that'll finally stop you from inspiring divorce papers." 
    scene a7619 with dssr
    sas "I hope today is the day when, for once, I don't have to see the outline of your pussy through your leggings."
    scene a7620 with dssa
    "They stare at each other for a moment." 
    scene a7621 with dssa
    pause 
    scene a7622 with dssr
    pause 
    scene a7623 with dssa
    pause 
    scene a7624 with dssa
    emi "I'd offer you a cup of pure infant blood, but we don't serve that here."
    scene a7625 with dssr
    emi "Anything else your kind might like? Coffee? Perhaps a glass of water?"
    pause 
    scene a7626 with dssa
    inp "A glass of water will suffice."
    scene a7627 with dssr
    pause 
    scene black with Dissolve(2)
    with Pause(.5)
    jump ReverieEnd 

label ReverieEnd:
    scene a7462 with dssr 
    pause 
    scene a7463 with dssa 
    pause 
    scene a7464 with dssa 
    za "Is that yours?"
    scene a7465 with dssa
    d "Yeah."
    scene a7466 with dssa
    za "It's sixty percent dust, forty percent bike."
    scene a7469 with dssr
    d "It's been dead for a while."
    scene a7467 with dssa
    za "Take it to a shop. They'll fix it."
    scene a7469 with dssa
    d "No. It's too expensive and..."
    d "I just sometimes like sitting on it..."
    scene a7468 with dssr
    za "Any special wishes for your birthday?"
    scene a7469 with dssa
    d "I'm not celebrating. Don't get me anything."
    scene a7485 with dssr
    "Nami lets out an evil laugh."
    scene a7486 with dssa
    d "Listen to me."
    d "You're not going to throw a party!"
    scene a7486 with dssa
    n "Mh? Who me? Oh no! Of course not!"
    scene a7487 with dssr
    d "Cheeto... Please don't."
    scene a7488 with dssa
    n "We'll see... Alright?"
    scene a7470 with dssr
    n "You live with Zara. So obviously she'll get you something."
    "You sigh."
    scene a7471 with dssa
    d "A surf board if it's not too expensive..."
    n "*Mumbles* They're pretty expensive."
    scene a7472 with dssa
    za "Oh! I need one too! Perfect, yes. That's perfect!"
    scene a7473 with dssr
    pause 
    if NamiDate is True:
        scene a7474 with dssr
        pause 
        scene a7475 with dssa
        pause 
        scene a7476 with dssa
        pause 
        scene a7477 with dssa
        n "I heard there are couple games at the bar."
        n "I think it's time for Raven [name] and Phoenix Nami to make an entrance."
        scene a7478 with dssa
        d "I guess it is."
        scene a7479 with dssa
        pause
    scene a7480 with dssa
    za "We should head home in a few."
    za "Nadia will come over, and she'll need a few hours to get bar-ready."
    scene a7482 with dssa
    n "Me too."
    scene a7483 with dssr
    n "I'll go slip in and see if I can find my jewelry."
    scene a7484 with dssr
    pause
    if ZaraTeasing or ZaraInterested is True:
        scene a7490 with dssr
        pause 
        scene a7491 with dssa
        pause 
        scene a7492 with dssa
        pause 
        menu:
            "She's so beautiful.":
                $ Zara_Date = True 
                $ Dating_List.append("Zara")
                scene a7493 with dssa
                pause 
                scene a7494 with dssr
                "You guide Zara as she carefully sits up." 
                scene a7495 with dssr
                "Her legs and body cling to yours."
                stop music fadeout 8
                scene a7496 with dssr
                pause 
                scene a7497 with dssr
                pause
                scene a7498 with dssa
                pause 
                scene black with Dissolve(2)
                $ renpy.movie_cutscene("images/Animations/CH1-3/Outro_Reverie.webm", stop_music=False)
            "She's a friend... with benefits.":
                $ Zara_Friends_WB = True 
                $ FWB_List.append("Zara")
                scene black with Dissolve(2) 
                $ renpy.movie_cutscene("images/Animations/CH1-3/OutroNZ.webm", stop_music=False)
    else:
        scene a7489 with dssr
        pause
        scene black with Dissolve(2)
        $ renpy.movie_cutscene("images/Animations/CH1-3/OutroNZ.webm", stop_music=False)
    jump Season2_Chapter4
