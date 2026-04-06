label chapter3x5:
    default preferences.show_empty_window = False
    define md = Character('Maitre dhotel' , color="#11D7EE")
    define mf = Character('Stefan Holgerson' , color="#513fEE")
    define el = Character('Elsa' , color="#481f5E")
    define bre = Character('Brenda' , color="#A44932")
    define bart = Character('Bartender' , color="#C58932")
    define mik = Character('Mikey' , color="#6E5C47")
    define sak = Character('Saki' , color="#ECFF00")
    define rep = Character('Reporter' , color="#00FFF0")
    define nico = Character('Nicole' , color="#00FFF0")
    define zar = Character('Zara' , color="#FF6800")
    define jak = Character('Jake' , color="#FF9DE9")
    define dwi = Character('Dwight' , color="#6CA2FF")
    define dex = Character('Dex' , color="#424BC8")
    define az = Character('Aziz' , color="#FF3E18")
    define jaz = Character('Jazz' , color="#FFB600")
    define lar = Character('Larry' , color="#00FF8F")
    define dssb = Dissolve(1.5)
    define flash = Fade(.25, 0.0, .75, color="#fff")
    $ persistent.unlockedImageS1 = True
    $ persistent.unlockedImageR1 = True
    $ BMCL = False
    $ BMCLN = False
    $ bellad = 0
    $ achievement.grant("FinishedCH3")
    $ achievement.sync()
    scene ab1 with Dissolve(3)
    show screen music_player_trigger
    $ play_playlist(playlist_BellchenDinnerx)
    d "...Hey."
    scene ab2 with dssa
    b "...Hey."
    scene ab3 with dssa
    "You both stand there for a few seconds in awkward silence."
    if BYF is True:
        $ bellalove +=2
        scene ab4 with dssb
        d "I got you this..."
        d "It's uh... a little fucked up."
        scene ab5 with dssb
        pause
        scene ab6 with dssa
        b "How- did you know that?"
        scene ab7 with dssa
        d "Know what?"
        scene ab6 with dssa
        b "That I like yellow flowers."
        scene ab7 with dssa
        d "You do? I didn't know that... I just picked one."
        scene ab6 with dssa
        b "...Thank you."
    else:
        pass
    scene ab8 with dssb
    d "We should go in."
    scene ab9 with dssa
    b "Yeah."
    scene black with Dissolve(3)
    with Pause(.5)
    scene ab10 with dssb
    pause
    scene ab11 with dssb
    b "Good evening."
    md "Good evening, Miss von Halen." # Maître d'hôtel
    md "Your table is almost ready."
    scene ab12 with dssa
    md "Would you like to take a seat in the lounge, meanwhile?"
    b "Sure."
    scene ab13 with dssb
    pause
    scene ab14 with dssa
    d "This is really not my type of restaurant."
    scene ab16 with dssa
    b "You prefer a 24/7 street diner?"
    scene ab15 with dssa
    d "Actually, yeah."
    scene ab16 with dssa
    b "Me too. People here have sticks up their asses."
    b "The food portions are also way too small."
    scene ab17 with dssb
    d "So, he is here?"
    b "Yeah, he is."
    d "What's our plan?"
    b "What? You don't have one?"
    d "No."
    scene ab18 with dssa
    b "That was your job!"
    scene ab19 with dssa
    d "Well... it's not easy to come up with something, when you don't know the environment."
    d "Let's just do a reconnaissance mission today."
    d "That was the initial plan anyways... to study his schedule and the people around him."
    scene ab20 with dssa
    b "Okay."
    if MCBL == 1:
        scene ab21 with dssa
        pause
        scene ab22 with dssa
        pause
        scene ab23 with dssa
        pause
        scene ab24 with vpunch
        "You both awkwardly turn away."
        $ BMCL = True
        scene ab25 with dssb
        pause
        scene ab26 with dssa
        pause
        scene ab25 with dssb
        menu:
            "Touch her foot back.":
                scene ab27 with dssb
                pause
                scene ab25 with dssa
                pause
                scene ab26 with dssa
                pause
                scene ab25 with dssa
                pause
                scene ab27 with dssa
                pause
                scene ab28 with vpunch
                b "Dude! Stop making everything weird!"
                d "You touched me first!"
                b "It was an accident!"
                scene ab29 with dssa
                d "Oh and the other two times were also on accident?"
                scene ab28 with dssa
                b "Y-Yes!"
                scene ab30 with vpunch
                "Bella pushes you away from her."
                scene ab31 with vpunch
                "You push her towards the corner of the couch."
                jump table3x5
            "Don't touch her foot back.":
                pass
                jump table3x5
    else:
        jump table3x5


label table3x5:
    scene ab32 with dssb
    md "Your table is ready, Miss von Halen."
    b "Thanks."
    scene black with Dissolve(2)
    with Pause(2)
    scene ab33 with dssb
    pause
    scene ab34 with dssb
    pause
    scene ab38 with dssb
    pause
    scene ab39 with dssa
    md "Do the lady and gentleman know what drink they want to order?"
    scene ab40 with dssa
    b "We would like today's special. Non-alcoholic."
    md "Of course."
    scene ab41 with dssa
    pause
    scene ab42 with dssa
    d "They look pretentious."
    scene ab40 with dssb
    b "They are."
    scene ab35 with dssb
    pause
    d "Is the blonde one his wife?"
    scene ab40 with dssa
    b "No. His wife isn't the most outgoing person."
    scene ab44 with dssb
    md "Here are your drinks."
    scene ab43 with dssa
    b "Thanks."
    if BMCL is True:
        scene ab45 with dssa
        "Bella stares at you with a weird expression."
        d "Hm?"
        scene ab46 with vpunch
        b "You're ruining everything!"
        scene ab47 with dssa
        d "What?"
        scene ab46 with dssa
        b "W-why are you making this so complicated?!"
        b "*Whisper* We're here to fuck this guy over!"
        scene ab48 with dssa
        b "Stop looking at me like that!"
        scene ab49 with dssa
        d "I am not even looking at you! You disgusting thing!"
        scene ab50 with vpunch
        b "YOU are disgusting!"
        b "No wonder you're still a virgin!"
        b "Who on earth would even consider having sex with you!?"
        b "Nobody is that desperate!"
        "You brush her comments off and your eyes wander through the restaurant."
    scene ab51 with vpunch
    mf "Ah! If it isn't the beautiful Bella!"
    d "(Her mouth just twitched. She must really hate him.)"
    b "Mr. Holgerson."
    mf "For you it's Stefan."
    scene ab52 with dssa
    mf "And who is your date?"
    scene ab53 with dssa
    d "I am [name]."
    scene ab54 with dssa
    mf "[name]... your family name is...?"
    scene ab53 with dssa
    d "Does it matter? Cyrus."
    scene ab54 with dssa
    mf "Cyrus..."
    "He slightly shakes his head."
    mf "I don't know any Cyrus."
    scene ab53 with dssa
    d "It's a big city."
    scene ab54 with dssa
    mf "It certainly is."
    scene ab55 with dssa
    mf "Bella, I don't see you here very often."
    scene ab56 with dssa
    b "I prefer people who don't have sticks up their asses."
    scene ab58 with dssa
    mf "Haha, as honest as ever!"
    if bellameet is True:
        mf "I'm assuming you've heard about the burglary at my house."
        scene ab57 with dssa
        b "My mother mentioned it, yes."
        scene ab58 with dssa
        mf "It's a tragedy... that heirloom was worth a lot to my family."
        mf "But we already have a suspect... I forgot her name, but she looks like someone who works on the street."
        mf "And we believe she wasn't alone. Someone like her couldn't have pulled it off alone."
    mf "I hope you will enrich us with your presence at our gala, next week. Saturday, to be precise."
    scene ab57 with dssa
    b "I'll think about it."
    scene ab59 with dssb
    mf "Very well, I wish you two a great evening."
    b "You too... Stefan."
    scene ab60 with dssa
    "Bella starts breathing faster."
    d "Calm down."
    scene ab61 with dssa
    b "He touched my hand."
    scene ab62 with dssa
    d "If you lose your cool after a simple touch, we can scrap this whole operation."
    scene ab61 with dssa
    b "Why?"
    scene ab62 with dssa
    d "Have you forgotten our plan already?"
    d "What do you think will happen when you have to spend a few hours with them when we copy the keys?"
    scene ab63 with dssa
    b "*whisper* Fuck.."
    b "If he ends up touching me somewhere I don't want... I won't stay cool."
    d "I would never expect that from you."
    scene ab64 with dssa
    d "What gala was he talking about, by the way?"
    scene ab65 with dssa
    b "They host multiple galas throughout the year."
    scene ab66 with dssa
    d "Should we go to one?"
    scene ab67 with dssa
    b "We?"
    d "Yeah, to acquire information."
    scene ab65 with dssa
    b "...Fine, but I can't get you in there. These galas are invite-only."
    b "If I wasn't invited, even my mom couldn't have gotten me in."
    b "It will be the first one I attend, actually. I always came up with excuses not to go."
    scene ab66 with dssa
    d "Okay... tell me who the other people at his table are."
    scene ab37 with dssa
    b "That is Brenda Vosolvo. The one with the glasses."
    b "She is a professor at one of our rival colleges."
    scene ab36 with dssa
    b "The blonde one is Genevieve Coate."
    scene ab35 with dssa
    b "I've heard that she abandoned her family after giving birth to a dwarf."
    d "Dwarf as in... the little people?" #
    b "I guess?"
    b "I don't know who the other guy at the table is."
    scene ab69 with dssb
    md "Do you wish to order?"
    scene ab70 with dssa
    pause
    scene ab69 with dssa
    b "Yes. I'd like the 15."
    scene ab70 with dssa
    d "The 96 for me, please."
    md "Of course."
    scene ab71 with dssa
    d "Nadia invited me and Nami to a board game meet up."
    scene ab72 with dssa
    b "Oh god... Really?"
    b "She's such a nerd."
    scene ab71 with dssa
    d "I've never thought she was a nerd."
    scene ab72 with dssa
    b "As if you'd know anything about her."
    scene ab73 with dssa
    b "Was Nancy there too?"
    scene ab74 with dssa
    d "Yes."
    scene ab75 with dssa
    b "She is... nice."
    if MCBL is 1:
        scene ab76 with dssa
        b "Does Nami know?"
        d "Know what?"
        b "That... thing.."
        scene ab77 with dssa
        d "What thing?"
        scene ab78 with dssa
        b "Stop playing dumb! I won't say it!"
        d "You sometimes remind me of a 3rd grader."
        scene ab79 with dssa
        b "Because of my flawless, youthful and juicy skin?"
        scene ab80 with dssa
        pause
    scene ab81 with dssb
    pause
    scene ab82 with dssa
    pause
    scene ab84 with dssa
    pause
    scene ab82 with dssa
    pause
    scene ab81 with dssa
    pause
    scene ab83 with dssa
    b "Oh god! I didn't know anyone could stare this disgustingly at someone!"
    "You ignore her words."
    scene ab84 with dssa
    pause
    scene ab85 with dssa
    b "And he juuust keeeeps staring... Creep."
    b "She's out of your league, don't even bother."
    scene ab86 with vpunch
    d "(...Shit.)"
    scene ab87 with dssa
    u "[name]? You're... you're [name] Cyrus, right?"
    scene ab88 with dssa
    d "Elsa?"
    scene ab87 with dssa
    el "It's been so long. I... I thought I'd never see you again, afte-..."
    scene ab89 with dssa
    d "You don't need to mention 'it'."
    "She nods."
    scene ab90 with dssa
    u "Our table is ready."
    scene ab91 with dssa
    el "Have a nice evening you two."
    d "...Thanks."
    scene ab92 with dssb
    b "What was 'it'?"
    scene ab93 with dssa
    d "None of your fucking business."
    scene ab94 with dssa
    b "Whatever... {size=-5}I'll find out.{/size}"
    scene ab95 with dssa
    d "Why are you so obsessed with me?"
    scene ab96 with dssa
    b "I-I'm not obsessed with you!"
    d "You act like you couldn't care less about me, but the second there is some information to gain you get two little lactation stains on your dress."
    scene ab97 with vpunch
    b "Lactation stains?!"
    scene ab98 with dssa
    d "What now? We're here to gather info..."
    scene ab99 with dssa
    pause
    scene ab100 with dssb
    b "I got it from Emilio."
    b "We insert it into a phone, and it slurps out all the data."
    d "So... we need to get his phone?"
    scene ab101 with dssb
    b "I don't think we'll have a chance to get it."
    b "Her phone though..."
    scene ab37 with dssa
    pause
    scene ab101 with dssa
    b "I know how to get under her skin..."
    d "Does she even matter?"
    scene ab103 with dssa
    b "How would I know?! It's a start, at least. And we'll get his phone number without him knowing..."
    scene ab104 with dssb
    d "That makes no sense. Amber should have his number... you could get it from her."
    d "But still... How do we get her phone?"
    scene ab105 with dssa
    "'...The bathroom.' *You both say at the same time.*"
    b "Hehe."
    scene ab107 with dssa
    d "She's been drinking a lot..."
    scene ab106 with dssa
    b "She'll need to hit the ladies room soon..."
    scene ab107 with dssa
    d "...And that's when we intercept her."
    scene ab106 with dssa
    b "We have to somehow predict when she will go to the ladies room."
    scene ab107 with dssa
    d "Right. I'll keep an eye on her body-language then."
    scene ab106 with dssa
    b "When she's inside the restroom, I'll find a way to distract her."
    b "I will position her with her back towards another stall."
    b "...Then you'll slide under it, grab her phone, insert the USB-C and extract the data."
    scene ab92 with dssa
    d "I'll have to go into the ladies room?"
    b "Yes."
    scene ab93 with dssa
    d "There's no way she won't notice me grabbing her phone from the purse."
    scene ab92 with dssa
    b "She'll be distracted... trust me."
    scene ab38 with dssb
    "You barely exchange another word until the food arrives."
    scene ab109 with dssb
    d "These portions are... small."
    b "That's why I hate places like this."
    b "Look at this..."
    d "...And cost a fortune."
    scene ab110 with dssa
    b "Being poor must suck."
    scene ab111 with dssa
    d "We're not poor."
    scene ab110 with dssa
    b "I saw your house."
    scene ab111 with dssa
    d "It's a normal house! What the fuck is your problem?"
    scene ab110 with dssa
    b "And the normal person is a poor person."
    scene ab111 with dssa
    d "I don't get your sorry ass."
    d "You always shit on these rich people, but you behave exactly like them."
    scene ab110 with dssa
    b "I do not."
    d "Yes you do."
    scene ab113 with vpunch
    b "I was joking! For fuck's sake!"
    scene ab114 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ab115 with dssb
    d "She's moving her legs a lot more frequently now."
    d "I think it's almost time."
    scene ab116 with dssa
    b "I'll go ahead."
    b "Wait 15 seconds, then follow her."
    scene ab117 with dssb
    pause
    scene ab118 with dssa
    d "(Elsa...)"
    scene ab119 with dssa
    pause
    stop music fadeout 2.5
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_AmbientBella)
    scene ab1406 with dssb
    el "I just want one!"
    scene ab1407 with dssa
    s "Why just one, Ely?"
    scene ab1408 with dssa
    el "You know my mommy! She'll get mad when I eat more than two scoops."
    scene ab1409 with dssa
    s "Here! I'll buy one more for you!"
    scene ab1410 with dssa
    el "No! She will find out during the weekly weighing!"
    scene ab1411 with dssr
    d "She will not find out, Ely!"
    scene ab1412 with dssr
    s "Two scoopies won't even show."
    scene ab1413 with dssa
    el "No... I don't want to be punished again."
    scene ab1414 with dssa
    d "Let's go then."
    scene ab1415 with dssa
    pause
    scene ab1416 with dssa
    s "Moogle! Come!"
    scene ab1417 with dssr
    pause
    scene ab1418 with dssr
    pause #alle essen Eis auf ner bank
    scene ab1419 with dssr
    el "My mama says you're a bad influence, [name]."
    scene ab1420 with dssa
    s "*Chuckles*"
    scene ab1421 with dssa
    d "Summer's the bad one!"
    scene ab1422 with dssa
    s "No, I'm the cool one!"
    scene ab1423 with dssr
    el "Mama said that you're blind from love."
    el "And that you'll end up in a trailer park and drink lots of beer."
    scene ab1424 with dssa
    s "...Good to know how my aunt speaks about me behind my back."
    scene ab1425 with dssr
    pause
    scene ab1426 with dssa
    d "Lick?"
    scene ab1427 with dssa
    pause
    scene ab1428 with dssb
    pause
    scene ab119 with dssb
    "You snap back to the present."
    scene ab120 with vpunch
    d "(It's time.)"
    scene ab123 with dssb
    d "*whisper* Bella?"
    scene ab121 with dssb
    pause
    $ persistent.unlockedImageBella18 = True
    scene ab122 with dssb
    b "*whisper* Come in."
    scene ab124 with dssa
    d "*whisper* Where is she?"
    b "*whisper* In there."
    d "*whisper* What now?"
    scene ab125 with dssa
    b "*Whisper* Get in there, slide under, grab her purse and connect the thing."
    b "*whisper* But wait 'til it happens."
    d "*whisper* Until what happens?"
    scene ab126 with vpunch
    "*Toilet flushing sound*"
    stop music fadeout 2.5
    b "*whisper* Go!"
    play music "music/Suspense/Scott Buckley - Nightfall.ogg"
    scene ab127 with dssa
    pause
    scene ab128 with dssa
    pause
    scene ab129 with dssa
    bre "Bella."
    scene ab130 with dssr
    b "Brenda."
    scene ab131 with dssa
    pause
    b "*Whisper* I'm sorry..."
    scene ab132 with dssa
    b "Ah! That reminds me... is Thomas still banging that 20 year old model? Or is that over?" #
    scene ab133 with vpunch
    bre "...What did you just say?"
    scene ab134 with dssa
    b "I asked if he still prefers her toned, young body-"
    scene ab135 with vpunch
    bre "How dare y-you say that to me! - She screams while her entire body is shaking like a leaf"
    scene ab136 with dssa
    bre "You d-dumb bitch! You have n-no idea what happened!"
    scene ab137 with dssa
    b "Judging by his happy nature, which suddenly emerged after this incident... I-"
    scene ab138 with vpunch
    bre "SHUT UP! SHUUUUUT UP! - She screams hysterically."
    scene ab139 with dssa
    d "(Mh..)"
    scene ab140 with dssa
    pause
    scene ab141 with dssa
    "The phone beeps."
    scene ab142 with dssa
    pause
    scene ab143 with vpunch
    pause
    scene ab144 with vpunch
    bre "And- and you! You're the-e last one who-"
    scene ab145 with dssa
    b "ALRIGHT!"
    b "Are you done?"
    scene ab146 with dssa
    bre "You... you are a terrible person!"
    bre "TERRIBLE!"
    stop music fadeout 2.0
    scene ab147 with dssa
    pause
    $ play_playlist(playlist_Jaccuzi)
    scene ab148 with dssr
    pause
    scene ab149 with dssa
    b "...Fuck."
    scene ab150 with dssr
    pause
    scene ab151 with dssa
    b "...Did it work?"
    scene ab152 with dssa
    d "Yes."
    scene ab153 with dssr
    b "We... should finish up and leave."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ab157 with dssb
    bre "I said I want the whole flask!"
    bart "Y-yes Ma'am."
    scene ab154 with dssb
    pause
    scene ab155 with dssa
    b "Eat up and we'll leave."
    scene ab156 with dssa
    d "There is not much of it- but at least it tastes good."
    stop music fadeout 2.0
    scene black with Dissolve(3)
    with Pause(.5)
    play music "music/TheIntangible/The Intangible - Encyclopedia of Frozen Dreams.ogg"
    scene ab158 with dssb
    pause
    scene ab159 with dssb
    pause
    scene ab160 with dssa
    pause
    scene ab161 with dssb
    pause
    scene ab162 with dssa
    d "I'm surprised you're taking it so bad."
    scene ab163 with dssa
    b "...She didn't deserve that. She never did anything to me... but I still did it without hesitation."
    if BTY is True:
        scene ab165 with dssa
    else:
        scene ab162 with dssa
    d "Don't go down this path of self-recrimination. It's done. We cannot go back and change it."
    if MCBL is 1 and BTY is True:
        menu:
            "...You'll most likely meet her again. If it really bothers you this much... keep an eye out for an opportunity to help her and redeem yourself.":
                $ WBIH = True
                scene ab164 with dssa
                b "...I guess."
            "Don't suggest Bella to try and redeem herself.":
                pass
    scene ab166 with dssa
    stop music fadeout 4.0
    d "Lets get away from here and check what we got."
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_AmbientBella)
    if BTY is True:
        $ persistent.unlockedImageR4 = True
        scene ab167 with dssb
        d "I'm still starving."
        scene ab168 with dssa
        pause
        scene ab169 with dssa
        b "Wanna get some burgers?"
        scene ab168 with dssa
        d "Yeah."
        scene black with Dissolve(2)
        with Pause(.5)
        scene ab170 with dssb
        d "So much better."
        b "Oh yeah."
        scene ab171 with dssa
        b "Do you have my cheeseburger?"
        scene ab172 with dssa
        d "Oh- yeah, it's in here."
        scene ab173 with dssa
        b "Nothing tops a good burger."
        scene ab174 with dssa
        pause
        scene black with Dissolve(2)
        with Pause(.5)
        scene ab175 with dssb
        pause
        scene ab176 with dssb
        $ persistent.unlockedImageBella19 = True
        b "Here, taste this fry."
        if MCBL == 1:
            scene ab178 with dssa
            pause
        else:
            scene ab177 with dssa
            pause
        scene ab179 with dssa
        "She observes you carefully as you eat the fry."
        scene ab180 with dssa
        d "Cheesy."
        b "Yeah, I love these cheese fries."
        scene ab181 with dssa
        b "So damn unhealthy but worth the incoming heart attack."
        scene ab183 with dssa
        pause
        scene ab182 with dssa
        b "...I really like this summer night feeling."
        b "The temperature drops in the evening, but you still get a nice warm breeze."
        scene ab184 with dssa
        d "I know what you mean."
        d "When I was still seeking solitude, I sometimes left the house at night and just walked through the nearby woods or sat near the lake."
        scene ab186 with dssa
        b "Our lives are so busy with all this college shit and all the things that come with it."
        b "Sometimes I just drive aimlessly for hours..."
        b "I just drive along the highway at night... The strong contrasts of the street lights and cars paired with the night sky."
        b "Eventually the cars become fewer and fewer... and the shiny small lights fade away."
        b "It reminds me of my family's holiday drives, when I was younger. I remember sitting in the back watching my father drive through the night..."
        b "And then I just stop at some point... and watch the sunrise."
        scene ab184 with dssa
        "You both sit there in silence for a moment."
        b "I haven't done that in a while..."
        d "It sounds nice."
        scene ab188 with dssb
        d "Plain fry?"
        if MCBL == 1:
            scene ab191 with dssa
            b "Why not."
            scene ab192 with dssa
        else:
            scene ab189 with dssa
            b "Why not."
            scene ab190 with dssa
        pause
        scene ab193 with dssb
        pause
        scene ab194 with dssa
        pause
        if MCBL ==1:
            scene ab195 with dssa
            d "That's yours."
            scene ab196 with dssa
            b "Yeah."
            scene ab197 with dssa
            pause
        else:
            scene ab195 with dssa
            b "Oh. That's yours."
            d "Yeah, keep it."
        scene ab198 with dssa
        d "How can you drink that?"
        scene ab199 with dssa
        b "Been drinking it since I can remember."
        scene ab198 with dssa
        pause
        stop music fadeout 2.0
        scene black with Dissolve(2)
        with Pause(.5)
        hide screen music_player_trigger
        scene BellchenBurger with dissolve
        $ renpy.pause(4.5, hard=True)
        with Pause(27)
        show screen music_player_trigger
        scene ab1377 with dssb
        play music "music/VeskyThinkingOfYou.ogg"
        b "When I was younger my sister and I used to put fries in whatever sauce we could find."
        b "We created little bets- on who would go farther."
        scene ab1378 with dssa
        d "Who won?"
        scene ab1379 with dssa
        b "I ate a fry with shaving cream."
        scene ab1380 with dssa
        d "Funny what you would consider a 'sauce'."
        scene ab1381 with dssa
        b "But she topped me by putting a fry into my lotion, then into the dogs drinking bowl and lastly covered it with a little bit of spiderweb."
        "Bella lightens up as she speaks of her little sister."
        scene ab1382 with dssa
        b "She puked... but she left the bathroom with her head held high."
        scene ab1383 with dssa
        "Bella chuckles with some sadness in her laugh."
        scene ab1384 with dssb
        d "We never did something like this. We more or less just played hide and seek, etc. all day long."
        b "We did this, too. But indoors."
        d "Have you been living in that house your entire life?"
        scene ab1385 with dssb
        b "Yeah."
        scene ab1386 with dssa
        d "Are you planning on moving out in the near future?"
        scene ab1387 with dssa
        b "No."
        b "I don't want to leave yet."
        b "Ayua and some others asked me about sharing a student house... but no thanks."
        b "I don't like living with that many people under one roof."
        b "At home it is just me and my Mama."
        scene ab1388 with dssa
        d "I've been thinking about moving out."
        scene ab1389 with dssa
        b "Well, you live in a trash can."
        scene ab1390 with dssa
        d "Fu-"
        b "Sorry- unnecessary comment."
        d "90 percent of what you say is unnecessary."
        scene ab1391 with dssa
        pause
        scene ab1392 with dssa
        d "But I might be moving in with Nami, Mila and someone else at some point."
        b "In those 4-room houses?"
        d "Yeah."
        scene ab1393 with dssa
        b "They suck... So yeah! It's still an upgrade for you."
        scene ab1394 with dssa
        d "I despise you, you know that?"
        scene ab1395 with dssb
        b "Sure..."
        scene ab1384 with dssb
        d "We should finish up and check what we've got."
        b "Yes, but not here. Let's do it somewhere more private."
        b "Give me the garbage... I saw a trash bin over there."
        scene ab200 with dssb
        pause
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(2)
    $ play_playlist(playlist_Jaccuzi)
    scene ab201 with Dissolve(2)
    d "This place here has an eerie aura to it."
    scene ab203 with dssa
    b "Perfect for the shady things we are doing."
    scene ab202 with dssa
    d "I like it."
    scene ab204 with dssa
    pause
    scene ab205 with dssa
    b "Fucking high heels..."
    scene ab206 with dssa
    d "What now?"
    scene ab207 with dssa
    b "Lighten up."
    scene ab208 with dssa
    pause
    if MCBL == 1:
        scene ab209 with vpunch
        "Bella twitches as you grab her foot."
        scene ab210 with dssa
        pause
        scene ab211 with dssa
        d "I am actually glad I don't have to wear something like that."
        d "Does it hurt a lot?"
        scene ab210 with dssa
        b "I didn't wear them for too long today... but they are very sore."
        scene ab213 with dssa
        b "Why? Do you want to give me a foot massage?"
        scene ab212 with dssa
        d "No."
        scene ab214 with dssa
        d "Let's do what we came here for."
    scene ab215 with dssa
    b "I have a tablet somewhere in the back."
    scene ab216 with dssa
    b "Not with your dirty shoes you dipshit!"
    scene ab217 with dssa
    pause
    scene ab218 with dssa
    b "Make some room."
    d "At least wait until I've actually made some room!"
    scene ab219 with dssa
    b "It's not like there's much space here!"
    scene ab220 with dssa
    "You look at each other for a second."
    scene ab229 with dssa
    d "...So?"
    b "Some folders... Pictures, Calendar, Videos..."
    scene ab230 with dssa
    b "Pictures first."
    scene ab219x with dssa
    pause
    scene ab219xy with dssa
    pause
    scene ab219x1 with dssa
    pause
    scene ab219xy2 with dssa
    d "Is he the guy that cheated on her?"
    b "Mhm."
    scene ab225 with dssa
    d "They looked happy."
    scene ab226 with dssa
    b "...That's why you should never trust anyone."
    b "Someday, they'll stab you in the back."
    scene ab227 with dssa
    d "Very pessimistic."
    b "It's smart."
    d "Making mistakes and learning from them is smart... but being too afraid of getting hurt to even take a risk."
    scene ab226 with dssa
    b "Can you fuck off and be on the lookout for something of value?"
    d "Click on chats."
    scene ab228 with dssa
    d "The chat with her ex."
    b "It seems like they married in college... That's way too soon."
    d "People change a lot in their 20s and early 30s."
    d "Does she have a chat with Stefan Holgerson?"
    scene ab229 with dssa
    b "Yes here."
    d "What does it say?"
    b "She was talking to him about Thomas."
    scene ab230 with dssa
    d "Is he using that situation to his advantage?"
    b "Not really. He came up with some ideas to help her."
    scene ab231 with dssa
    b "Like he listed some destinations that they both would like and could visit to reconnect."
    d "So we got nothing."
    scene ab232 with dssb
    pause
    d "*sigh* I need some air."
    scene ab233 with dssb
    "You sit on the front of her car for a minute until you make out a little trail in the distance."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ab240 with dssb
    stop music fadeout 4.0
    "You keep walking until the trail goes up a hill, which leads to an outlook on the top."
    scene ab241 with dssb
    play music "music/Vesky - Departure.ogg"
    pause
    scene ab242 with dssa
    pause
    $ persistent.unlockedImageBella20 = True
    "You hear Bella coming up behind you, as she steps on some twigs and vegetation."
    scene ab243 with dssa
    "She watches you carefully, but doesn't know what to do."
    scene ab242 with dssb
    pause
    scene ab244 with dssb
    pause
    scene ab245 with dssb
    "You both stay quiet and observe the bright moon and the little stars surrounding it."
    "Since Bella arrived, an unnatural quietness has laid itself over the outlook, complemented by a light breeze."
    scene ab246 with dssa
    d "Today was just a waste of time."
    d "We acquired nothing... Even worse... We crushed that woman for nothing."
    scene ab247 with dssa
    b "This whole plan was just dumb."
    b "What did we even expect to accomplish?"
    scene ab246 with dssa
    d "Our only chance is his girlfriend. If she's really as stupid as you said, then she is the only way."
    scene ab248 with dssa
    b "And we go-.. I got invited to a gala."
    d "Right, I forgot about that."
    scene ab249 with dssb
    if MCBL >=1 and BTY is True:
        b "...Still, we might not have accomplished much... but- we're a good team."
        menu:
            "Yeah, we are a good team.":
                hide screen music_player_trigger
                $ KissedGirl = True
                $ persistent.unlockedImageBella23 = True
                stop music fadeout 2.0
                scene black with Dissolve(1.5)
                $ bellalove +=3
                $ BellaKiss03x = True
                scene BellaK with dissolve
                $ renpy.pause(4.5, hard=True)
                with Pause(53.5)
                show screen music_player_trigger
                play music "music/QuietRomance/Beza - Save Myself.ogg"
                scene ab253 with dssb
                pause
                scene ab255 with dssb
                pause
                scene ab257 with vpunch
                b "I... wh-what did we just do!?"
                scene ab258 with dssa
                d "You started it!"
                scene ab259 with vpunch
                b "You star-..."
                scene ab260 with dssa
                b "Damn it! Why did I do that?!"
                d "Because you like me."
                scene ab261 with vpunch
                b "I can't like you! I'm- I'm way out of your league!"
                scene ab262 with dssa
                d "Apparently not."
                scene ab261 with dssa
                b "Y-you!"
                scene ab262 with dssa
                d "Me?"
                "Bella stares at you, her eyes moving rapidly."
                d "(The way she's looking at me... she's actually making me uncomfortable.)"
                scene ab1396 with vpunch
                "(You kiss her out of pure awkwardness.)"
                b "MmMmn!"
                scene ab1397 with dssb
                "The first few seconds are rough, animalistic even. You both push your bodies against each other."
                scene ab1398 with dssb
                pause
                "It's more like you're battling. Both Bella and you are trying to lead, her tongue wrestling with yours."
                scene ab1399 with dssa
                pause
                scene ab1400 with dssb
                "After a while, the rough, passionate kiss turns gentler and gentler... until you finally split your lips from each other."
                pause
                scene ab263 with vpunch
                pause
                b "Home... I- I need to get home."
                scene ab264 with dssa
                pause
                scene black with Dissolve(2)
                with Pause(.5)
                scene ab265 with dssb
                b "...Get out."
                scene ab266 with dssa
                pause
                scene ab267 with dssa
                pause
                scene ab268 with dssa
                pause
                scene ab269 with dssa
                $ persistent.unlockedImageR5 = True
                b "*Mumbling* Fuck my life."
                $ achievement.grant("KissBellchen")
                $ achievement.sync()
                scene black with Dissolve(3)
                with Pause(.5)
                jump HomeNami03BK
            "Disagree":
                $ BellaKiss03x = False
                $ bella -=3
                scene ab246 with dssa
                d "Doing one mission together won't make us a good team."
                scene ab247 with dssa
                b "Whatever..."
                scene ab246 with dssa
                d "Next stop? Home?"
                scene ab249 with dssa
                b "Yes."
                scene ab250 with dssa
                d "Well, thanks for the food..."
                b "Yep."
                scene ab248 with dssa
                b "We'll figure out what to do next..."
                scene black with Dissolve(2)
                with Pause(.5)
                jump HomeNami03BK
    else:
        scene ab246 with dssa
        d "Next stop? home?"
        scene ab249 with dssa
        b "Yes."
        scene ab250 with dssa
        d "Well, thanks for the food..."
        b "Yep."
        scene ab248 with dssa
        b "We'll figure out what to do next..."
        scene black with Dissolve(2)
        with Pause(.5)
        jump HomeNami03BK


label HomeNami03BK:
    stop music fadeout 2.0
    if BellaKiss03x is True:
        $ play_playlist(playlist_NamiSad)
        scene ab270 with dssb
        pause
        scene ab271 with vpunch
        "*Door creaking*"
        scene ab273 with dssb
        pause
        scene ab274 with dssa
        n "[name]?"
        scene ab273 with dssa
        d "(...)"
        scene ab275 with dssb
        n "[name]?"
        d "Y-yeah."
        scene ab276 with dssb
        n "Are you alright?"
        d "I, uh, I guess- No... No, I am not alright."
        scene ab277 with dssa
        n "Oh God, what happened?!"
        d "I-... Well- you-"
        scene ab278 with vpunch
        $ persistent.unlockedImageNami18 = True
        n "Why are you stuttering?! What happened?!"
        scene ab279 with dssb
        n "Here, sit down."
        scene ab280 with dssa
        pause
        scene ab281 with dssa
        n "What happened?"
        scene ab282 with vpunch
        d "We kissed..."
        scene ab283 with dssa
        "For a moment she is lost for words."
        n "K-kissed?"
        n "As in... lips on lips?"
        scene ab284 with dssa
        d "As in tongue to tongue."
        scene ab285 with dssa
        pause
        n "I- I don't know what to say."
        scene ab286 with dssa
        d "Oh God! She's horrible! I- Oh god... why?!"
        scene ab287 with dssa
        n "I think we should get super drunk... L-like right now!"
        d "Yes please.."
        scene ab288 with dssa
        n "I'll get us some beers."
        scene ab289 with vpunch
        "You drop onto the couch, still incapable of processing what has happened."
        "Meanwhile..."
        scene black with Dissolve(2)
        with Pause(.5)
        scene ab1401 with Dissolve(2)
        pause
        "The other half isn't doing much better."
        scene black with Dissolve(2)
        with Pause(.5)
        if fitness == 1:
            scene ab290f with dssb
        elif fitness == 2:
            scene ab290f2 with dssb
        elif fitness == 0:
            scene ab290 with dssb
        n "Tell me exactly what happened and... what else you guys did."
        scene ab291 with dssa
        d "*sigh* We stole data from a woman who seems to be a friend of the Holgersons."
        scene ab292 with dssa
        n "Why are you collecting data about them?"
        scene ab291 with dssa
        d "Someday I'll tell you..."
        scene ab293 with dssa
        n "I want to-"
        scene ab294 with vpunch
        d "Nami!"
        d "Someday- alright?"
        scene ab295 with dssa
        n "*sigh* Okay."
        scene ab296 with dssa
        pause
        scene ab297 with dssb
        n "How did it turn into... making out with her?"
        scene ab298 with dssa
        d "I kinda realized that we were wasting our time."
        d "I needed some fresh air, so I found a hill... I could show you the place, by the way. It has a nice view."
        d "She followed me... And- we stood there in silence for a while..."
        d "Then we looked at each other... she touched my hand... and the way the wind tousled her hair... *sigh*"
        scene ab300 with dssa
        d "And then she just kissed me."
        scene ab299 with dssa
        n "She kissed you?"
        n "Did... you kiss her back or was it only from her side?"
        scene ab301 with dssa
        d "I kissed her back."
        scene ab302 with dssa
        n "I... see."
        scene ab303 with dssb
        d "Are you okay?"
        scene ab304 with dssa
        "For a few seconds, you see Nami desperately trying to hold her tears back..."
        scene ab305 with vpunch
        "- But finally breaks."
        "She violently sobs as she presses her face into your chest."
        scene ab306 with dssa
        "You put your arms around her shaky body to comfort her."
        n "S-sorry... I... I don't know why I'm-..."
        d "Nami... I think you and I need to have a serious talk."
        d "...Without any sort of bullshit."
        n "-Not necessary."
        scene ab307 with dssa
        d "It is. Seems like there are some... unspoken truths, between us."
        d "I hate seeing you torture yourself just to make me feel better."
        d "You expect me to be honest with you... but that goes both ways."
        n "I will..."
        scene ab308 with dssa
        n "...Sorry man... I'm so dumb."
        d "Yeah."
        scene ab309 with dssb
        d "It seems like we both need another beer right now."
        n "Yes."
        scene ab310 with dssa
        d "I love you, Nami. Never forget that."
        scene ab311 with dssa
        n "I love you, too."
        scene ab310 with dssa
        d "I'll be right back."
        stop music fadeout 2.0
        scene black with Dissolve(2)
        with Pause(2)
        $ play_playlist(playlist_GirlyPop)
        scene ab312 with dssb
        n "Cheers."
        scene ab313 with dssa
        pause
        scene ab314 with dssa
        "You can feel Nami staring at you."
        scene ab315 with dssa
        n "Sooo uhhh... How was it... the kiss?"
        scene ab316 with dssa
        d "Nami? You just broke down-."
        scene ab317 with dssa
        n "I can take it... or more like I need to learn to take it."
        scene ab318 with dssa
        d "It was wet."
        n "N-"
        d "How can I be falling for that thing?"
        scene ab320 with dssa
        n "I don't understand it either... Victoria, Mila... so many great girls around you and you pick... that?"
        scene ab321 with dssa
        d "I didn't pick anything!"
        scene ab322 with dssa
        d "Besides... She isn't that bad."
        n "You called her a 'thing' a moment ago... and now you say that she isn't that bad."
        d "Maybe it was... Yeah, maybe it was just that moment... a moment that is forever gone and we'll never do it again."
        scene ab319 with dssa
        n "I doubt that."
        scene ab323 with dssa
        d "By the way... you won't believe who I met at the diner."
        scene ab324 with dssa
        n "Is this a guessing game?"
        d "Elsa."
        scene ab325 with vpunch
        n "Wow! Ely?!"
        scene ab326 with dssa
        "You nod."
        scene ab325 with dssa
        n "How is she?!"
        scene ab326 with dssa
        d "Good, I guess."
        d "I mean she is able to eat there, so she's probably well off."
        scene ab325 with dssa
        n "Did you talk?"
        scene ab326 with dssa
        d "Yeah, for a short while."
        scene ab320 with dssa
        n "I wonder if she still remembers me.."
        d "If she remembered me, she should remember you too."
        scene ab319 with dssa
        n "Everybody from where we used to live remembers you..."
        scene ab328 with dssa
        n "Look..."
        scene ab329 with dssa
        pause
        scene abmila1 with dssb
        $ persistent.unlockedImageMila3 = True
        $ persistent.unlockedImageVic2 = True
        n "I get so insecure when I see those four."
        d "Don't you mean two?"
        n "Count again."
        pause
        n "...I'm talking about their boobs."
        scene ab328 with dssa
        n "Look at those full and perfectly shaped boobs..."
        scene ab327 with dssa
        menu:
            "I like smaller boobs":
                $ MCPKT = True
                $ nami +=1
                $ mila -=1
                scene ab330 with dssa
                n "*Singing* Youuu like my tiddies!"
                d "Not yours! Yours are eww!"
                scene ab324 with dssa
                n "YOU are ewww!"
            "Big boobs are certainly... not bad":
                $ MCPGT = True
                $ mila +=1
                $ vici +=1
                scene ab323 with dssb
                pause
                d "What?"
            "I like Bella's size":
                $ MCPKB = True
                $ nami -=1
                scene ab331 with vpunch
                n "Dude! No! No talking about- NO!"
                d "Alright! Chill!"
        scene black with Dissolve(2)
        with Pause(.5)
        scene ab332 with dssb
        n "...Do you think Nojiko is doing it with Nick?"
        scene ab333 with dssa
        d "I don't know."
        scene ab334 with dssa
        n "Hehe... Noji... What a prude."
        d "Maybe she isn't a prude."
        scene ab335 with dssa
        n "Nojiko? She is totally a prude!"
        scene ab336 with dssa
        n "Or maybe she has some really dirty fetishes."
        scene ab337 with dssa
        d "I do not like the direction this is taking."
        scene ab336 with vpunch
        n "Think about it!"
        n "She's always so formal and uptight... And do you know why?"
        n "Because she's super dirty!"
        scene ab338 with dssa
        n "...Let's check her room."
        d "No?"
        n "I bet she has a secret trapdoor to a sex dungeon."
        d "*sigh*"
        scene ab339 with vpunch
        n "Case closed. You're welcome."
        scene ab336 with dssa
        n "By the way, since Mila mentioned those student houses... I'm kinda warming up to the idea."
        n "Imagine not having to answer to Nojiko ever again."
        scene ab337 with dssa
        d "I think you're wrong if you expect Noji to stop caring."
        scene ab340 with dssa
        n "Dude, I can't even order toys! I'm always afraid that she'll open the package!"
        d "Plea-"
        scene ab341 with dssa
        n "I only have one toy and- and you should see my bookmarks!"
        d "I hate you."
        scene ab342 with dssa
        n "Don't be like that... you should be glad that I'm so open with you."
        scene ab343 with dssa
        d "I am glad that you and I can talk about anything, too."
        d "But your sex life is something I really don't want to hear about."
        scene ab345 with dssa
        n "...I see."
        scene ab339 with vpunch
        n "You want more than just hearing about it, huh?"
        scene ab346 with dssa
        n "The way your hand is on my thigh... busted!"
        d "Shut up, idiot."
        menu:
            "But I do like your legs.":
                scene ab347 with dssa
                $ NamiThighs3x5 = True
                n "Oh? You do?"
                d "Mhm."
                scene ab348 with dssa
                n "I don't like my legs."
                n "My thighs are a little too thick."
                d "They're proportional though. They go well with the rest of your body."
                scene ab350 with dssa
                n "What about my feet?"
                menu:
                    "Nothing against yours, but I really don't like feet in general.":
                        scene ab351 with dssa
                        $ McFeet = False
                        n "Oh, I see."
                    "They're smooth. Relatively nice, I guess.":
                        scene ab352 with dssa
                        d "They're smooth. Relatively nice, I guess."
                        $ McFeet = True
                        pause
            "Don't compliment her thighs.":
                pass
    else:
        $ persistent.unlockedImageNami18 = True
        $ play_playlist(playlist_NamiSad)
        scene ab270 with dssb
        pause
        scene ab271 with vpunch
        "*Door creaking*"
        scene ab273 with dssb
        pause
        scene ab274 with dssa
        n "[name]?"
        d "Yes?"
        scene ab420 with dssa
        n "Already here? How did it go?"
        d "Uh- okay, I guess."
        scene ab419 with dssa
        n "I am just surprised you're already home."
        d "Yeah, we finished our mission early."
        n "Want a beer?"
        d "Yeah."
        $ play_playlist(playlist_GirlyPop)
        scene ab312 with dssb
        n "Cheers."
        scene ab313 with dssa
        pause
        scene ab314 with dssa
        d "What did you do today?"
        scene ab315 with dssa
        n "Played some games... got into a heated discussion on a forum..."
        scene ab314 with dssa
        d "Sounds like your typical day."
        scene ab315 with dssa
        n "Yup. How was the date with Bella?"
        scene ab316 with dssa
        d "It was not a date!"
        scene ab320 with dssa
        n "If you say so."
        scene ab321 with dssa
        d "Well, we did what we had to do and left."
        scene ab322 with dssa
        n "How was the food?"
        d "It was a fancy ass restaurant. They had good food."
        n "Let's go there someday."
        d "It's way too expensive."
        scene ab324 with dssa
        n "I'm talking about when you and I are rich!"
        scene ab323 with dssa
        d "By the way... You won't believe who I met there."
        scene ab324 with dssa
        n "Is this a guessing game?"
        d "Elsa."
        scene ab325 with vpunch
        n "Wow! Elsa?!"
        scene ab326 with dssa
        "You nod."
        scene ab325 with dssa
        n "How is she?!"
        scene ab326 with dssa
        d "Good, I guess."
        d "I mean she is able to eat there, so she's probably well off."
        scene ab325 with dssa
        n "Did you talk?"
        d "Yeah, for a short while."
        scene ab328 with dssa
        n "I wonder if she still remembers me.."
        scene ab327 with dssa
        d "If she remembered me, she should remember you too."
        scene ab328 with dssa
        n "Everybody from where we used to live remembers you..."
        scene ab329 with dssa
        n "Look..."
        scene abmila1 with dssb
        n "I get so insecure when I see those four."
        d "You mean two?"
        n "Count again."
        n "...I am talking about their boobs.."
        n "Look at those full and perfectly shaped boobs..."
        menu:
            "I like smaller boobs":
                $ MCPKT = True
                $ nami +=1
                $ mila -=1
                scene ab330 with dssa
                n "*Singing* Youuu like my tiddies!"
                d "Not yours! Yours are eww!"
                scene ab324 with dssa
                n "You are ewww!"
            "Big boobs are certainly not bad":
                $ MCPGT = True
                $ mila +=1
                $ vici +=1
                scene ab323 with dssb
                pause
                d "What?"
            "I like Bella's size":
                $ MCPKB = True
                $ nami -=1
                scene ab331 with vpunch
                n "Dude! No! No talking about- NO!"
                d "Alright! Chill!"
        scene black with Dissolve(2)
        with Pause(.5)
        scene ab332 with dssb
        n "...Do you think Noji is fucking Nick?"
        scene ab333 with dssa
        d "I don't know."
        scene ab334 with dssa
        n "Hehe... Nojiko... What a prude."
        d "Maybe she isn't a prude."
        scene ab335 with dssa
        n "Noji? She is totally a prude!"
        scene ab336 with dssa
        n "Or maybe she has some really dirty fetishes."
        scene ab337 with dssa
        d "I do not like the direction this is taking."
        scene ab336 with vpunch
        n "Think about it!"
        n "She's always so formal and uptight... And do you know why?"
        n "Because she's super dirty!"
        scene ab338 with dssa
        n "...Let's check her room."
        d "No?"
        n "I bet she has a secret trapdoor to a sex dungeon."
        d "*sigh*"
        scene ab339 with vpunch
        n "Case closed. You're welcome."
        scene ab336 with dssa
        n "By the way, since Mila mentioned these student houses... I am kinda warming up to the idea."
        n "Imagine not having to answer to Nojiko ever again."
        scene ab337 with dssa
        d "I think you're wrong when you expect Nojiko to stop caring."
        scene ab340 with dssa
        n "Dude, I can't even order sex toys! I'm always afraid that she'll open the package!"
        d "Plea-"
        scene ab341 with dssa
        n "I only have one toy and- and you should see my bookmarks!"
        d "I hate you."
        scene ab342 with dssa
        n "Don't be like that... you should be glad that I'm so open with you."
        scene ab343 with dssa
        d "I am glad that you and I can talk about anything, too."
        d "But your sex life is something I really don't want to hear about."
        scene ab345 with dssa
        n "...I see."
        scene ab339 with vpunch
        n "You want more than just hearing about it, huh?"
        scene ab346 with dssa
        n "The way your hand is on my thighs... busted!"
        d "Shut up, idiot."
        menu:
            "But I do like your legs.":
                scene ab347 with dssa
                $ NamiThighs3x5 = True
                n "Oh? You do?"
                d "Mhm."
                scene ab348 with dssa
                n "I don't like my legs."
                n "My thighs are a little too thick."
                d "They're proportional though. They go well with the rest of your body."
                scene ab350 with dssa
                n "What about my feet?"
                menu:
                    "Nothing against yours, but I really don't like feet in general.":
                        scene ab351 with dssa
                        $ McFeet = False
                        n "Oh, I see."
                    "They're smooth. Relatively nice, I guess.":
                        scene ab352 with dssa
                        d "They're smooth. Relatively nice, I guess."
                        $ McFeet = True
                        pause
            "Don't compliment her thighs.":
                pass
    scene black with Dissolve(2)
    with Pause(.5)
    scene ab353 with dssb
    pause
    scene ab354 with dssa
    pause
    scene ab355 with dssa
    n "I have another one."
    d "*sigh*."
    scene ab356 with dssa
    n "Would you rather fight two big dogs that only have three legs or three cats that have eight legs?"
    d "Definitely the dogs."
    scene ab357 with dssa
    n "Man... spider-cats would be so creepy."
    scene ab358 with vpunch
    "*Door squeak*"
    stop music fadeout 2.0
    scene ab359 with dssb
    play music "music/TheIntangible/The Intangible - Encyclopedia of Frozen Dreams.ogg"
    n "*GASP!"
    scene ab360 with dssa
    m "Oh [name]... You're already her-"
    scene ab361 with dssa
    m "Are you two drinking on a workday?"
    n "Those could be anyone's..."
    scene ab362 with dssa
    "Nojiko quietly sits next to you and Nami."
    scene ab363 with dssa
    d "Hard day?"
    scene ab364 with dssa
    m "..Ha- haha.."
    m "I hate it. I hate seeing the same faces every day."
    scene ab365 with dssa
    n "Thanks, I guess...?"
    scene ab366 with dssa
    m "Ohh no! Not you two! But the faces at work.."
    scene ab367 with dssa
    d "Well, quit your job?"
    scene ab368 with dssa
    m "Ohhh... Why didn't I think of that?"
    scene ab369 with dssa
    m "I just wish I had taken the risk of opening my own small Doctor's Office."
    d "It's never too late."
    scene ab368 with dssa
    m "Who knows where life will take us."
    scene ab370 with dssa
    n "This might be the alcohol speaking... but [name] and I could go work somewhere part time."
    d "(Fuck you Nami! Please, just be quiet.)"
    scene ab371 with dssa
    m "Well... We're struggling a little since [name] started his therapy."
    d "I can sto-"
    scene ab372 with vpunch
    m "No!"
    scene ab373 with dssa
    n "[name] and I will find some work on the side, right?"
    scene ab374 with dssa
    d "*annoyed* ...Sure."
    scene ab375 with dssb
    m "*sigh* I love you two."
    m "I think I would've gone insane already if it wasn't for you two."
    scene ab376 with dssa
    n "You need a hobby... or just something that counts as stress relief."
    m "I started writing a book.."
    n "I mea-"
    scene ab377 with dssa
    "You interrupt Nami."
    d "That's great."
    d "Show us the first draft when it's done."
    scene ab378 with dssa
    m "I don't think you'd like the genre."
    n "Is it something dirty? *giggle*"
    m "Nami... It's a children's book."
    if BellaKiss03x is True:
        scene ab379 with dssa
        n "Nojiko."
        n "[name] kissed Bella."
        scene ab381 with vpunch
        m "Oh! Really?!"
        scene ab380 with dssa
        d "Aa-h... Let's not talk about this."
        scene ab382 with dssa
        m "I am so happy for you, [name]!"
        scene ab380 with dssa
        d "It was a spur of the moment thing... I don't like her, and she doesn't like me... end of story."
        scene ab383 with dssa
        "Nami and Nojiko share a look."
        m "*whisper* Sure."
    scene ab384 with dssa
    m "[name], how were your first sessions with Amber?"
    d "They were alright, I guess."
    d "But- the next session might be different."
    m "How so?"
    d "She wants to visit the cabin with me."
    scene ab385 with dssa
    n "The cabin? The one deep in the woods?"
    d "Yeah, the one where... you know."
    scene ab386 with dssb
    m "Oh, that's a six hour drive away."
    m "I wonder what she has in store for you."
    m "Did you also get that teddy bear from her?"
    d "Mhm, apparently it was hers..."
    scene ab387 with dssa
    m "It will be alright."
    scene ab388 with dssa
    m "Also, Nami... Besides writing a book I did indeed think about picking up a hobby."
    scene ab389 with dssa
    n "Which one?"
    scene ab393 with dssa
    m "Tennis. The first time I brought [name] to Amber, I saw a logo on the back wall of her office."
    m "Later I asked her about it, and she offered to bring me to the tennis club. I might take her up on that."
    n "Is it expensive?"
    m "Amber said that she could get me a discount- if I list her as the one who referred me."
    scene ab390 with dssa
    n "We'll have tennis tournaments in the future, [name]."
    n "Maybe it wouldn't be so bad to pick it up?"
    scene ab391 with dssa
    d "We should concentrate on just a few of them."
    d "Focus on our strengths, you know."
    scene ab390 with dssa
    n "We could still give it a try, play for fun... and with Nojiko too!"
    scene ab392 with dssa
    m "I'd love to play with you two!"
    m "I'll ask Amber if I can take the two of you with me to the club and then we'll see."
    scene ab394 with dssa
    "Nami and Nojiko delve into other random topics, and while you're staring at the ceiling... your mind starts drifting away."
    stop music fadeout 3.0
    scene black with Dissolve(2)
    jump School03ND

label School03ND:
    with Pause(.5)
    play music "music/bird.mp3"
    scene ab395 with Dissolve(2)
    pause
    scene ab396 with dssb
    pause
    scene ab397 with dssb
    pause
    scene ab398 with dssb
    pause
    scene ab399 with dssa
    pause
    scene ab400 with dssa
    pause
    d "My head..."
    pause
    m "Good morning."
    scene ab402 with dssa
    n "...Morning."
    m "You look like you're hungover."
    n "I am..."
    scene ab403 with dssa
    m "You two have an hour to get ready."
    n "Can't we stay home for today?"
    scene ab404 with dssb
    m "No way in hell would I let the two of you stay home. Drinking in the middle of the week..."
    scene ab405 with dssb
    n "My head..."
    if BellaKiss03x is True:
        scene ab406 with dssa
        d "I don't want to see Bella..."
        n "Shut up."
        n "I really don't want to hear about her... not in my current state."
    scene ab407 with dssa
    d "I'll go shower."
    n "Let me go first."
    d "Fine... but leave me some hot water..."
    scene ab408 with dssa
    n "Thanks."
    scene ab409 with dssb
    pause
    scene ab410 with dssb
    m "Here. Coffee."
    d "Thanks."
    scene ab411 with dssa
    m "You should shave."
    scene ab413 with dssa
    d "I'm too lazy for that, today."
    scene ab411 with dssa
    m "Does your head hurt?"
    d "Totally."
    m "You deserve that."
    d "I know."
    scene ab414 with dssa
    m "How's college?"
    d "Okay, I guess."
    $ persistent.unlockedImageNojiko2 = True
    if BellaKiss03x is True:
        scene ab415 with dssa
        m "And what are your plans with Bella?"
        d "What?"
        m "You two took a big step yesterday and I... You see... Amber is your therapist."
        m "I hope that things go well between you and Bella."
        scene ab416 with dssa
        d "I don't want Bella. I don't want any relationship right now."
        m "I know." #careass
        m "Just be honest with her, okay?"
        d "Mhm."
        scene ab417 with dssa
        m "And always remember to use protection."
        d "Please don't turn into a second Nami."
    else:
        scene ab415 with dssa
        m "And have you already met some nice girls?"
        d "I... think so?"
        m "You know you can bring them here, right?"
        scene ab416 with dssa
        d "...I don't plan on bringing anyone home ever."
        m "Juuuust in case..."
        m "Who knows who you might meet."
        scene ab417 with dssa
        m "Just always remember to use protection."
        d "Please don't turn into a second Nami."
    scene ab418 with dssa
    m "Speaking about Nami... She should be done showering by now."
    m "I'll get ready, too."
    scene ab417 with dssa
    m "Have a nice day!"
    d "Thanks, you too."
    stop music fadeout 2.5
    scene black with Dissolve(3)
    with Pause(.5)
    play music "music/CityStreet.ogg"
    scene ab421 with dssb
    pause
    scene ab422 with dssa
    n "Why do you look so grumpy?"
    scene ab423 with vpunch
    d "The water was ice cold! You showered way too long!"
    scene ab424 with dssa
    n "My head was hurting, and the warm water felt amazing!"
    scene ab423 with vpunch
    d "Fuck you!"
    scene ab425 with dssa
    d "That was the last time, I ever let you shower first."
    n "Next time just join me!"
    scene ab426 with dssa
    $ persistent.unlockedImageSonya5 = True
    so "M-Morning."
    scene ab427 with dssa
    n "Morning Sonya!"
    d "Morning."
    stop music fadeout 2.5
    scene ab1404 with dssb
    pause
    scene ab1405 with dssa
    $ play_playlist(playlist_Ch4x52)
    pause
    scene ab428 with dssb
    pause
    scene ab429 with dssa
    n "I like your pants."
    so "Uhm... T-thanks."
    scene ab432 with dssa
    nia "Morning!"
    $ persistent.unlockedImageNia2 = True
    nia "Today is the day!"
    scene ab433 with dssa
    n "What day?"
    nia "Today we enter the last two weeks before the tryouts. Coaches and players will all be watching us."
    n "Oh? I remember someone mentioning a first team."
    n "And of course, today we are hungover."
    scene ab435 with dssa
    nia "Ohhh... poor wormy."
    scene ab436 with dssa
    nia "Hey [name]."
    if namigym is True:
        d "Hey."
        scene ab437 with dssa
        nia "How are you?"
        d "I have a hangover."
        nia "Do you want to know my secret to get rid of a hangover?"
        scene ab438 with dssa
        d "Nah, I'm good."
    else:
        scene ab438 with dssa
        d "Hi."
    scene ab439 with dssa
    pause
    scene ab440 with dssa
    nia "Your ass must look amazing in those pants!"
    scene ab441 with vpunch
    n "Wolke!"
    nia "Oh... sorry! I didn't mean to say that out loud."
    scene ab442 with dssa
    so "It's fine."
    scene ab444 with dssa
    d "Wolke?"
    n "It's our safeword."
    n "Whenever she acts in a socially inappropriate way, I'll let her know."
    if namigym is False:
        scene ab446 with dssa
        d "I didn't know you were so close already."
        scene ab445 with dssb
        nia "We don't know each other that well, but we're slowly heading there."
        "Nami nods."
    else:
        scene ab446 with dssa
        d "I see."
    scene ab447 with dssb
    "You arrive at the station near the college."
    scene black with Dissolve(3)
    with Pause(.5)
    scene ee400 with dssb
    pause
    scene ee401 with dssa
    n "And they don't realize that you are playing while streaming?"
    scene ee403 with dssr
    nia "Not unless I accidentally squeak because I got a good drop."
    nia "And the trebuchet is still much better!"
    scene ee402 with dssa
    n "Tzz! I prefer the normal catapults!"
    scene ee404 with dssr
    nia "There is only one way to settle this! Age of Wormies 2 match to the death!"
    scene ee405 with dssa
    n "You're on!"
    scene ee407 with dssr
    pause
    scene ee406 with dssa
    pause
    scene ee408 with dssa
    d "Are you going to join today's gym lesson?"
    scene ee409 with dssa
    so "Yes. I got these pants here."
    scene ee410 with dssa
    d "They're pretty tight."
    scene ee411 with dssr
    so "I know. The person that got me these, didn't know what he was doing."
    d "At least the chances of you dying from a heatstroke aren't as high."
    scene ee412 with dssr
    n "Do you have a short top, Sonya?"
    scene ee413 with dssa
    so "No, I'll use the one I'm wearing."
    scene ee414 with dssa
    n "Girl, you're going to die!"
    n "It's supposed to be 36°C today!"
    n "I have another shirt with me. I'll give it to you, okay?"
    scene ee415 with dssr
    "She says nothing for a moment."
    scene ee416 with dssr
    so "Okay. Thank you, Nami."
    scene ee417 with dssr
    so "I'm really excited for today."
    scene ee418 with dssa
    d "Mh?"
    scene ee417 with dssa
    so "I mean-"
    scene ee418 with dssa
    d "Oh, you mean the board game?"
    scene ee419 with dssa
    so "Yes."
    scene ee418 with dssa
    d "That's great."
    d "You're already being more social than I was in the past years."
    scene ee421 with dssb
    pause
    mi "Did it get approved?"
    scene ee422 with dssa
    ka "No, it got declined again."
    scene ee426 with dssr
    mi "I don't understand..."
    scene ee423 with dssr
    ka "Hmm..."
    scene ee424 with dssr
    ka "And... it's approved."
    scene ee427 with dssr
    mi "Huh?"
    scene ee428 with dssa
    ka "You have the money for the card, right?"
    scene ee427 with dssa
    mi "Yes, of course."
    scene ee424 with dssr
    ka "Just pay me back in cash each month. I switched it to my card."
    mi "Thank you, Karen!"
    scene ee425 with dssr
    ka "You're welcome, Mila."
    scene ee429 with dssr
    pause
    scene ee430 with dssr
    mi "Hey girls, and [name]."
    scene ee431 with vpunch
    n "Yo Mila!"
    "The Cheeto hits Mila in the boobs..."
    scene ee432 with vpunch
    "...And Nia in the face."
    scene ee433 with vpunch
    n "Damn! No! I'm so sorry! Oh no!"
    scene ee434 with dssr
    mi "My boobi..."
    n "I'm sorry Mila's boobi!"
    scene ee435 with dssr
    n "Everything okay, Nia?"
    scene ee436 with dssa
    nia "Yeah, I'm fine."
    scene ee437 with dssr
    mi "Hi Sonya."
    scene ee438 with dssa
    so "Hi Mila."
    scene ee440 with dssa
    if miladateF or miladate is True:
        mi "How are you, [name]? You look kinda-"
        scene ee443 with dssa
        d "Brutally abused?"
        scene ee440 with dssa
        mi "Not the words I would have chosen, but yeah."
        scene ee443 with dssa
        mi "I heard you went on a date with Bella."
        scene ee442 with dssa
        d "It wasn't really a date. It was business related."
        scene ee444 with dssr
        mi "What kind of business could you have with her?"
        scene ee445 with dssa
        d "Well... We're working on something. But let's not talk about this."
        scene ee444 with dssa
        mi "I'll definitely ask again."
        scene ee445 with dssa
        d "And I'll definitely dodge the question again."
    else:
        mi "[name], you look kinda wasted."
        scene ee443 with dssa
        d "I do?"
        scene ee440 with dssa
        mi "Seems like Nami can hold her liquor better than you."
    scene ee446 with dssa
    har "Good morning."
    scene ee447 with dssa
    mi "Good morning, Miss Harrison."
    $ persistent.unlockedImageHari2 = True
    scene ee448 with dssa
    har "We have benches everywhere in the building. There's no need to sit on the stairs, where people need to pass through."
    scene ee449 with dssr
    "She smiles, and goes her way."
    scene ee450 with dssa
    mi "She's probably the hottest professor we have."
    scene ee451 with dssr
    nia "Cindy is also very cute."
    nia "We should head to class though."
    if BellaKiss03x is False:
        scene ab1361 with dssb
        d "Give me a second."
        scene ab1363 with dssa
        d "Hey."
        scene ab1362 with dssa
        pause
        scene ab1364 with dssa
        b "Hi."
        scene ab1365 with dssa
        d "Are we going to your place today?"
        scene ab1366 with dssa
        b "No, there is a racer slash tuning meetup in another state, I'll be leaving in the afternoon."
        d "I see."
        scene ab1367 with dssa
        b "We'll continue next week."
        "You nod."
    if AyuaSparring is True:
        scene ab1368 with vpunch
        ay "[name]!"
        ay "Sunday!"
        scene ab1369 with dssa
        d "Sunday?"
        ay "Sunday, you will come to our studio."
        scene ab1370 with dssa
        d "I'd rather not set a date."
        d "Can't I just stop by spontaneously?"
        scene ab1371 with dssa
        ay "No."
        ay "I will be in the studio 'til around 8pm. Shoot me a message before you arrive."
        scene ab1372 with dssb
        d "Okay."
        "Ayua stares at you."
        d "What?"
        scene ab1373 with vpunch
        ay "You don't even know where the studio is!"
        d "I will just use Noodle maps."
        scene ab1375 with dssa
        ay "We'll see..."
    scene black with Dissolve(2)
    with Pause(.5)
    $ persistent.unlockedImageSonya1 = True
    scene sba786 with dssb
    pause
    scene sba787 with dssa
    d "(I don't feel like sitting next to Nia today... Not when I'm hungover.)"
    scene sba788 with dssa
    d "Hmm."
    scene sba789 with dssr
    d "Hey Vic. Do you mind if I sit here?"
    scene sba790 with dssa
    mi "Of course not!"
    scene sba792 with dssr
    "Victoria's eyes light up as you lay your hand upon her shoulder."
    scene sba791 with dssa
    pause
    scene sba814 with dssr
    pause
    scene sba793 with dssr
    v "Why don't you want to sit next to her?"
    scene sba794 with dssa
    d "I can't take her today... Not in my current state."
    scene sba793 with dssa
    v "She's friends with Nami, right?"
    scene sba793 with dssa
    d "Yeah."
    scene sba795 with dssa
    v "She looks sooo fancy with those piercings!"
    v "I bet she's nice!"
    scene sba796 with dssa
    d "She is."
    if namigym is True:
        $ VicNia3x5 = True
        d "She's just socially awkward."
    d "And she is a cam girl."
    scene sba804 with dssr
    mi "What? For real?"
    d "Yeah, Nami told me."
    scene sba797 with dssr
    v "What's a cam girl?"
    v "Is it like a saleswoman for cameras?"
    scene sba799 with dssa
    mi "No sweety."
    mi "She gets naked in front of her cam."
    scene sba797 with dssa
    v "And then what?"
    scene sba799 with dssa
    mi "S-"
    scene sba797 with dssa
    v "Oh! She masturbates?"
    scene sba799 with dssa
    mi "Yes."
    scene sba800 with dssa
    v "I bet she gets a lot of compliments about her fancy piercings!"
    scene sba799 with dssr
    mi "I don't think the people watching focus on them."
    scene sba797 with dssa
    v "I know they're there to look at her vagina and breasts!"
    scene sba805 with dssr
    mi "Selling your body like that? That's pretty sad."
    scene sba801 with dssr
    v "I have to disagree, Mila. I think people can do whatever they want as long as it makes them happy and doesn't hurt anyone else."
    scene sba802 with dssa
    mi "Yeah bu-"
    scene sba801 with dssa
    v "No. I don't think you should degrade others just because they have different beliefs or tastes."
    scene sba803 with dssa
    v "It's the diversity of it all that makes life so interesting."
    v "So please, don't talk her down because she likes to show her body on camera."
    v "I bet yours would look amazing on camera too!"
    scene sba805 with dssr
    $ persistent.unlockedImageVicCh2_x1 = True
    mi "She gets naked for some spare change, though."
    scene sba806 with dssa
    d "No. Nami said that she makes around $900 a session. We're talking about high five figures a month."
    scene sba807 with vpunch
    mi "WHAT?!"
    scene sba811 with dssr
    har "Is there a problem, Mila?"
    scene sba812 with dssa
    mi "No, I'm sorry."
    scene sba811 with dssa
    har "Please get ready to focus on the lesson."
    scene sba809 with dssr
    mi "So much money?"
    scene sba808 with dssa
    d "That's what she said."
    scene sba810 with dssa
    pause
    scene sba813 with dssa
    har "Good morning, let's begin, shall we?"
    scene black with Dissolve(2)
    with Pause(.5)
    scene ab505 with dssa
    pause
    menu:
        "Touch Victoria's hand.":
            scene ab507 with dssa
            $ vici +=1
            pause
            scene ab508 with dssa
            pause
            scene ab507 with dssa
            pause
            scene ab509 with dssa
            $ RoRum = True
            $ SNtay = True
            $ vicbes = True
            scene ab507 with dssa
            pause
            scene ab510 with dssa
            "Victoria turns your hand around and your fingers intertwine."
            d "*Whisper* Do you have something in your hand? It feels a little rough."
            scene ab514 with vpunch
            $ persistent.unlockedImageVic3 = True
            play music "music/Suspense/Scott Buckley - Resonance.ogg"
            pause
            scene sba815 with vpunch
            pause
            scene sba816 with dssr
            pause
            scene sba817 with dssa
            d "I need to use the restroom."
            scene black with Dissolve(2)
            with Pause(.5)
            scene ab520 with dssb
            d "*Fast breathing*"
            scene ab521 with dssb
            d "*Mumbles* F-Fuck!"
            scene ab522 with dssa
            d "*mumbles* L-Leave me the fuck alone...!"
            scene ab523 with vpunch
            d "*GASP*"
            scene ab524 with dssb
            rob "[name]?"
            rob "What's wrong?"
            scene ab525 with dssa
            d "What are you doing here?"
            scene ab524 with dssa
            rob "You're in the ladies room."
            scene ab526 with dssa
            d "I- *Cough* I see."
            scene ab527 with vpunch
            rob "No, no, no!"
            scene ab528 with dssa
            rob "What's going on?"
            scene ab529 with dssa
            "Unknown female voices echo through the entrance."
            scene ab530 with dssa
            "Robin violently pushes you into the stall."
            scene ab531 with dssa
            u "I'm telling you, I saw them! The swimsuits this year..."
            scene ab532 with dssa
            u "Are they really that revealing?"
            scene ab531 with dssa
            u "I feel sorry for the girls with some serious cleavage."
            scene ab533 with dssa
            u "And here I thought the normal sport outfits were bad."
            u "Hehe, we'll get to see a bunch of boobs this year."
            scene ab534 with dssa
            u "Damn straight."
            scene ab535 with dssa
            pause
            scene ab536 with dssa
            rob "*whisper* Now I'm glad that I don't have serious cleavage."
            scene ab537 with dssa
            "You hear a third person entering the conversation."
            u "*inaudible* - tell you... he punched that guy!"
            u "As if!"
            scene ab538 with dssa
            u "That emo guy seriously punched him?"
            scene ab539 with dssa
            rob "*whisper* I pray they don't open this stall..."
            d "Whisper* You didn't lock it?"
            rob "*Whisper* I was nervous!"
            scene ab538 with dssa
            u "That's what they say... and they say Sai had to get help from Thomas otherwise he would've been beaten into the hospital."
            u "Not gonna lie, it's about time that jerk got a beating."
            scene ab540 with dssa
            $ persistent.unlockedImageRobin2 = True
            rob "*whisper* Are they talking about you?"
            "You nod."
            scene ab541 with dssa
            u "It's sad that he looks like that."
            u "Oh! I think I saw him today... He looks kinda... unique now."
            if fitness == 2:
                $ GTMIH = True
                u "And you can see he's been hitting the gym lately"
                u "Maybe I should claim him before someone else realizes he's gonna be some delicious candy at some point."
            scene ab543 with dssa
            u "Isn't that blonde chick with him?"
            u "Bella?"
            u "What Bella?"
            scene ab544 with dssa
            u "Von Halen."
            u "No way. She's a moron. I've heard some things about her... I'm telling you, she's crazy."
            u "I went to high school with her... such a weirdo."
            scene ab545 with dssa
            if BellaKiss03x is True:
                d "*Angry whisper* Lies."
                rob "Shhh... I know."
            else:
                rob "Sorry."
            scene ab537 with dssa
            u "She might look acceptable... but nobody would ever take her for a serious girlfriend."
            u "Haha, right?? They might use her once and throw her away."
            u "Let's go before the old hag gives us detention."
            scene ab546 with dssb
            pause
            scene ab547 with vpunch
            u "Uhm-?"
            scene ab548 with dssa
            u "What's the matter?"
            scene ab549 with vpunch
            $ persistent.unlockedImageS3 = True
            u "Holy shit!"
            rob "I-It's not what it looks like."
            u "Hahahaha!"
            scene ab550 with dssb
            u "Banging in the restroom during official hours... Respect."
            scene ab551 with dssb
            pause
            scene ab552 with dssa
            rob "We didn't do anything!"
            u "Uhuh- sure."
            d "Let's go."
            rob "We-"
            d "Keep walking."
            if fitness == 2:
                scene ab553 with dssa
                u "He must've heard everything we said."
                scene ab554 with dssa
                u "Great. That breaks the ice."
            scene ab555 with dssa
            u "Pretty bold of those two. *Chuckles*"
            scene ab556 with dssa
            u "Hey!"
            $ achievement.grant("RobinRumor")
            $ achievement.sync()
            jump VicHand
        "Don't touch her hand.":
            pass
            jump VicNoHand

label VicNoHand:
    scene black with Dissolve(2)
    with Pause(.5)
    scene ab502 with dssb
    har "Please let me know once you've reached the first checkpoint on your assignments."
    scene sba845 with dssr
    pause
    scene sba846 with dssr
    mi "Vic, I'll see you later, okay?"
    scene sba847 with dssa
    v "Sure!"
    v "I need to see Miss Marla anyway."
    scene sba848 with dssa
    v "Bye, [name]!"
    d "See you, Vic."
    scene sba849 with dssa
    v "Will you help me find Miss Marla, Trey?"
    t "Sure."
    scene sba850 with dssr
    pause
    $ persistent.unlockedImageMila4 = True
    scene sba851 with dssr
    if milagym is True:
        $ MiPark = True
        mi "So, are you going to visit us this weekend?"
        scene sba828 with dssa
        d "You mean the thing at Victoria's?"
        scene sba832 with dssa
        mi "Yes, exactly."
        scene sba833 with dssa
        d "Well, yeah... I think I can take a look."
        d "But I might ask Nami, too."
        scene sba834 with dssa
        mi "Sure!"
    else:
        mi "Would you like to come to Victoria's place tomorrow?"
        scene sba828 with dssa
        d "Umm..."
        scene sba832 with dssa
        mi "We're just gonna hang out a little."
        mi "I told Maja to take the weekend off and I would take care of Vic."
        mi "You should come over."
        scene sba834 with dssa
        mi "I bet Victoria would love to see you."
        scene sba835 with dssa
        d "Yeah, I might come over."
        scene sba834 with dssa
        mi "Bring some pajamas!"
        scene sba835 with dssa
        d "I have to stay overnight?"
        scene sba832 with dssa
        mi "No, of course not but if you want- I think Victoria would like that."
        if milagym is False:
            mi "We three could watch scary movies, eat pizza and tell funny stories."
            mi "And you can ask Nami if she wants to come by, too."
        else:
            mi "Ask Nami, too!"
        scene sba828 with dssa
        d "I'll ask her."
    if miladate or miladateF is True:
        $ MiPark = True
        mi "Any idea of when we could hang out?"
        scene sba829 with dssa
        d "Hmm well, I guess the weekend is out of the question."
        d "And I'm guessing we'll be invited to meet Nojiko's boyfriend one of these evenings."
        d "I guess someday next week."
        scene sba832 with dssa
        mi "Just let me know in advance; I'm working four days this week, so I'll need to clear my schedule."
        scene sba830 with dssa
        d "You don't need to take a day off."
        d "We'll just do it whenever you have time."
        scene sba831 with dssa
        mi "Are you sure you really want to hang out?"
        scene sba830 with dssa
        d "I know I-"
        scene sba831 with dssa
        mi "Yeah, I don't know, it comes across like it's actually not really what you want."
        mi "Maybe you-"
        scene sba836 with dssr
        d "You know... I had a very emotional situation with Victoria just a few days ago."
        d "Where I told her that I probably need her more than I think."
        d "And... I said this in a moment of pure clarity and vulnerability."
        scene sba837 with dssa
        d "It's... you need to understand where I'm coming from"
        d "I was in a place of complete solitude... Pretty much isolating myself from everyone."
        d "Every time I am in a social interaction, it feels like my energy is getting drained."
        scene sba843 with dssr
        mi "It started sweet and took a bad turn."
        scene sba844 with dssa
        d "What I am saying is... We should just do something spontaneous."
        d "If we set a date, there is a high chance that I'll call it off."
        d "The sheer existence of a set time or a social commitment drains my energy."
        scene sba843 with dssa
        mi "I get it."
        mi "Sooo... We just hang out spontaneously."
        d "Mhm."
        scene sba839 with dssr
        mi "Great, we have around an hour 'til we have to go to the gym class."
        mi "Let's hang out."
        scene sba840 with dssr
        pause
        scene sba841 with dssa
        d "Touche."
        "Mila gives you a cute smile."
        scene sba842 with dssa
        mi "This doesn't replace an actual first date though."
        mi "Come, I'll show you a nice place."
    if BellaKiss03x is True:
        jump MarlaConc
    elif MiPark is True:
        jump Milapark
    else:
        jump Ch3x5sport



label VicHand:
    stop music fadeout 2.0
    scene black with Dissolve(2.5)
    with Pause(.5)
    $ play_playlist(playlist_BellaDate)
    $ persistent.unlockedImageMila4 = True
    scene sba819 with dssb
    "As you enter the auditorium again, the others are just about to leave."
    scene sba821 with dssr
    d "Mila, what can I do for you?"
    scene sba822 with dssa
    mi "How did you know it was me?"
    scene sba821 with dssa
    d "You're the only one besides Nami and Bella that would sneak up on me."
    scene sba823 with dssa
    mi "Would you mind telling me what just happened?"
    scene sba824 with dssr
    d "Some other time, okay?"
    scene sba825 with dssa
    mi "Okay, sure."
    scene sba824 with dssa
    d "Where is Victoria? I must have scared her a bit."
    scene sba826 with dssa
    mi "Yeah, you should probably talk to her about it."
    mi "She went to see Miss Marla."
    scene sba827 with dssa
    if milagym is True:
        mi "So, are you going to visit us this weekend?"
        scene sba828 with dssa
        d "You mean the thing at Victoria's?"
        scene sba832 with dssa
        mi "Yes, exactly."
        scene sba833 with dssa
        d "Well, yeah... I think I can take a look."
        d "But I might ask Nami, too."
        scene sba834 with dssa
        mi "Sure!"
    else:
        mi "Would you like to come to Victoria's place tomorrow?"
        scene sba828 with dssa
        d "Umm..."
        scene sba832 with dssa
        mi "We're just gonna hang out a little."
        mi "I told Maja to take the weekend off and I would take care of Vic."
        mi "You should come over."
        scene sba834 with dssa
        mi "I bet Victoria would love to see you."
        scene sba835 with dssa
        d "Yeah, I might come over."
        scene sba834 with dssa
        mi "Bring some pajamas!"
        scene sba835 with dssa
        d "I have to stay overnight?"
        scene sba832 with dssa
        mi "No, of course not but if you want- I think Victoria would like that."
        mi "We three could watch scary movies, eat pizza and tell funny stories."
        mi "And you can ask Nami if she wants to come by, too."
        scene sba828 with dssa
        d "I'll ask her."
    if miladate or miladateF is True:
        $ MiPark = True
        mi "Any idea of when we could hang out?"
        scene sba829 with dssa
        d "Hmm well, I guess the weekend is out of the question."
        d "And I'm guessing we'll be invited to meet Nojiko's boyfriend one of these evenings."
        d "I guess someday next week."
        scene sba832 with dssa
        mi "Just let me know in advance; I'm working four days this week, so I'll need to clear my schedule."
        scene sba830 with dssa
        d "You don't need to take a day off."
        d "We'll just do it whenever you have time."
        scene sba831 with dssa
        mi "Are you sure you really want to hang out?"
        scene sba830 with dssa
        d "I know I-"
        scene sba831 with dssa
        mi "Yeah, I don't know, it comes across like it's actually not really what you want."
        mi "Maybe you-"
        scene sba836 with dssr
        d "You know... I had a very emotional situation with Victoria just a few days ago."
        d "Where I told her that I probably need her more than I think."
        d "And... I said this in a moment of pure clarity and vulnerability."
        scene sba837 with dssa
        d "It's... you need to understand where I'm coming from"
        d "I was in a place of complete solitude... Pretty much isolating myself from everyone."
        d "Every time I am in a social interaction, it feels like my energy is getting drained."
        scene sba843 with dssr
        mi "It started sweet and took a bad turn."
        scene sba844 with dssa
        d "What I am saying is... We should just do something spontaneous."
        d "If we set a date, there is a high chance that I'll call it off."
        d "The sheer existence of a set time or a social commitment drains my energy."
        scene sba843 with dssa
        mi "I get it."
        mi "Sooo... We just hang out spontaneously."
        d "Mhm."
        scene sba839 with dssr
        mi "Great, we have around an hour 'til we have to go to the gym class."
        mi "Let's hang out."
        scene sba840 with dssr
        pause
        scene sba841 with dssa
        d "Touche."
        "Mila gives you a cute smile."
        scene sba842 with dssa
        mi "This doesn't replace an actual first date though."
        mi "Come, I'll show you a nice place."
    else:
        $ MiPark = True
        scene sba831 with dssa
        mi "You still look a little... worried."
        mi "We still have some time before we have to get to the next class."
        mi "Come-"
        scene sba830 with dssa
        d "It's okay, Mila."
        scene sba836 with dssr
        mi "No. Whatever happened was freaky and I think you could use some company."
        "You look at each other."
        scene sba838 with dssa
        mi "I won't take no for an answer."
        d "I call this rape."
        scene sba839 with dssr
        mi "Call it whatever you want."
        scene sba840 with dssr
        pause
        scene sba841 with dssa
        d "Alright."
        "She chuckles."
    if BellaKiss03x is True:
        jump MarlaConc
    elif MiPark is True:
        jump Milapark
    else:
        jump Ch3x5sport


label MarlaConc:
    scene ab587 with vpunch
    ma "Excuse me, do you have a moment to talk?"
    if MiPark is True:
        ma "Mila, please wait outside."
    scene ab588 with dssa
    d "Okay. And you are?"
    scene ab589 with dssa
    ma "What?"
    ma "I'm Miss Marla?"
    scene ab590 with dssa
    d "Oh. I didn't recognize you."
    scene ab589 with dssa
    ma "Did something happen between you and Bella?"
    scene ab590 with dssa
    d "Why do you ask?"
    scene ab591 with dssa
    ma "Because she isn't here, and I called her mother... and as it seems Bella is refusing to come here."
    scene ab592 with dssb
    "You stare into the room for a while."
    scene ab593 with dssa
    ma "What happened? - She says in a serious tone."
    menu:
        "Tell her you and Bella kissed":
            $ McBSteKiss = True
            $ marla +=1
            scene ab594 with dssa
            d "We kissed."
            "Taken off guard by your response, Miss Marla gives you a very surprised look."
            scene ab595 with dssa
            ma "What?"
            scene ab596 with dssa
            d "I don't like to repeat myself."
            scene ab597 with dssa
            ma "But- why wouldn't she come to class?"
            scene ab596 with dssa
            d "Because she lacks emotional conflict resolution skills."
            scene ab598 with dssa
            ma "*sigh* And here I thought something really bad had happened."
            $ persistent.unlockedImageMarla2 = True
            scene ab599 with dssb
            d "Could- could you give me a different partner?"
            scene ab600 with dssa
            ma "Why? I thought the two of you were bonding?"
            scene ab599 with dssa
            d "And that's the problem."
            scene ab600 with dssa
            ma "*Annoyed sigh*."
            ma "No, I won't give you a different partner."
            scene ab601 with dssb
            menu:
                "How are you doing?":
                    $ MaFrWGD = True
                    scene ab602 with dssb
                    ma "Me?"
                    d "Yes."
                    scene ab603 with dssa
                    ma "I... I'm fine. Thanks for asking."
                    menu:
                        "I like the new haircut.":
                            if AMMC is True:
                                scene ab604 with dssa
                                ma "Thank you..."
                                ma "Well... you should thank Amber for that."
                                scene ab605 with dssa
                                d "It's good to know that therapy is helping someone, at least."
                                scene ab606 with dssa
                                ma "Is it because you had to see the 'accident'?"
                                scene ab607 with dssa
                                d "I don't know. I'm not good at emotional conflict resolution either."
                                scene ab606 with dssa
                                ma "I will talk to Amber about... something."
                                scene ab608 with dssa
                                d "About what exactly?"
                                "Miss Marla gazes into the room thoughtfully."
                                scene ab609 with dssa
                                ma "[name]... you are part of my- problems."
                                scene ab610 with dssa
                                ma "I want us to have a therapy session together."
                                scene ab611 with dssa
                                d "Does Amber do that?"
                                scene ab610 with dssa
                                ma "I am sure she will when I ask her."
                                scene ab611 with dssa
                                d "I see."
                            else:
                                scene ab604 with dssa
                                ma "Thank you, [name]."
                            scene ab601 with dssa
                            d "Have a nice day."
                        "Have a nice day.":
                            scene ab601 with dssa
                            ma "You, too."
                "Don't ask her how she is doing.":
                    pass
        "Don't tell her about it.":
            $ MDKATK = True
            scene ab596 with dssa
            d "I can't say."
            d "I actually thought we were sailing pretty smooth."
            scene ab597 with dssa
            ma "Then it has nothing to do with you?"
            d "I can't think of anything at least."
            scene ab598 with dssa
            ma "*sigh*"
            scene ab611 with dssa
            ma "I see."
            scene ab601 with dssb
            menu:
                "How are you doing?":
                    $ MaFrWGD = True
                    scene ab602 with dssb
                    ma "Me?"
                    d "Yes."
                    scene ab603 with dssa
                    ma "I... I'm fine. Thanks for asking."
                    menu:
                        "I like the new haircut.":
                            if AMMC is True:
                                scene ab604 with dssa
                                ma "Thank you..."
                                ma "Well... you should thank Amber for that."
                                scene ab605 with dssa
                                d "It's good to know that therapy is helping someone, at least."
                                scene ab606 with dssa
                                ma "Is it because you had to see the 'accident'?"
                                scene ab607 with dssa
                                d "I don't know. I'm not good at emotional conflict resolution either."
                                scene ab606 with dssa
                                ma "I will talk to Amber about... something."
                                scene ab608 with dssa
                                d "About what exactly?"
                                "Miss Marla gazes into the room thoughtfully."
                                scene ab609 with dssa
                                ma "[name]... you are part of my- problems."
                                scene ab610 with dssa
                                ma "I want us to have a therapy session together."
                                scene ab611 with dssa
                                d "Does Amber do that?"
                                scene ab610 with dssa
                                ma "I am sure she will when I ask her."
                                scene ab611 with dssa
                                d "I see."
                            else:
                                scene ab604 with dssa
                                ma "Thank you, [name]."
                            scene ab601 with dssa
                            d "Have a nice day."
                        "Have a nice day.":
                            scene ab601 with dssa
                            ma "You, too."
                "Don't ask her how she is doing.":
                    pass
    scene black with Dissolve(2)
    with Pause(.5)
    if MiPark is True:
        jump Milapark
    else:
        jump Ch3x5sport

label Milapark:
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    scene ee190 with dssb
    pause
    $ play_playlist(playlist_QuietRomance)
    $ persistent.unlockedImageS2 = True
    play sound "music/bird.mp3"
    scene ee191 with dssr
    pause
    scene ee192 with dssa
    d "It's quiet here."
    scene ee193 with dssa
    mi "Nadia showed it to me."
    scene ee194 with dssa
    d "I didn't know you two were friends."
    scene ee193 with dssa
    mi "We're more like acquaintances."
    mi "I'd find her here sometimes... Reading her books or drawing and writing into her secret notebook."
    scene ee195 with dssa
    d "A secret notebook?"
    scene ee193 with dssa
    mi "Yeah. She's got quite a few of them."
    mi "I went to high school with her. She managed to fill quite a few."
    scene ee196 with dssr
    d "What's in them?"
    scene ee197 with dssa
    mi "I don't think anyone besides Ayua and Bella know."
    mi "To be honest, I'm not even sure if they know."
    mi "She defends them with her life."
    scene ee198 with dssr
    mi "There was a guy in high school that tried to grab it from her."
    scene ee199 with dssa
    mi "I have never seen someone go from super cutie-calm to hyper aggressive so quickly."
    mi "Like... she scared me."
    scene ee200 with dssa
    d "That doesn't mean much... You're scared easily."
    scene ee201 with vpunch
    mi "Hey!"
    scene ee202 with dssa
    mi "I mean yes! But hey!"
    scene ee203 with dssa
    d "Whatever is in those notebooks seems to be very personal."
    scene ee204 with dssa
    mi "One hundred percent. Sometimes she'd tear up when writing in it."
    scene ee205 with dssa
    d "She invited me and Nami to play a board game."
    scene ee206 with dssa
    pause
    scene ee207 with dssa
    mi "She did invite me a few times too, but I had to work right after class."
    scene ee208 with dssa
    mi "She's really into fantasy... Maybe even a little too much."
    d "What do you mean?"
    scene ee209 with dssr
    mi "Well, she-... no. It's not my place to tell you this."
    scene ee211 with dssa
    mi "You might find out at some point."
    scene ee213 with dssa
    "A warm breeze gusts through the leaves."
    scene ee214 with dssa
    "Mila's hair falls softly around her face. She has an ethereal glow about her as she stares into the distance."
    scene ee215 with dssa
    "You can't help but smile just looking at her."
    scene ee216 with dssa
    pause
    scene ee217 with dssa
    mi "It suits you..."
    scene ee219 with dssr
    mi "Your smile."
    mi "I like it."
    scene ee220 with dssr
    mi "Have you and Nami talked about moving out again?"
    scene ee221 with dssa
    d "She said she was warming up to the idea."
    scene ee220 with dssa
    mi "It would be a dream come true to move in with you, Nami, and someone else."
    scene ee222 with dssa
    mi "Finally away from ho-... that place I'm living in."
    d "I can't imagine not feeling comfortable at home."
    scene ee223 with dssr
    mi "I wasn't lucky enough to be born into an intact family."
    mi "You know... My mum really is a prostitute."
    scene ee224 with dssa
    d "Oh?"
    $ persistent.unlockedImageMilaCH2_2 = True
    scene ee225 with dssa
    mi "Mhm... And I have a-"
    scene ee226 with dssr
    mi "Never mind... I'll tell you about it when we know each other a little better."
    scene ee227 with dssa
    d "Sure. No pressure."
    scene ee228 with dssa
    pause
    scene ee229 with dssa
    mi "Do you want to know what my dream is?"
    scene ee228 with dssa
    d "Yeah."
    scene ee230 with dssr
    mi "I want to be a pilot... or at least have my own plane to fly with."
    scene ee231 with dssa
    d "I didn't see that coming."
    scene ee230 with dssa
    mi "I want to be free. I want to go some place where nobody drags me down."
    scene ee232 with dssa
    mi "Where I can be myself..."
    scene ee233 with dssa
    d "You can't be yourself here?"
    scene ee234 with dssa
    "She takes a second."
    scene ee235 with dssa
    mi "I want to go some place where nobody knows me as the daughter of a whore."
    mi "This all here... It's cursed ground."
    $ persistent.unlockedImageMila5 = True
    scene ee236 with dssa
    if bellagym is True:
        d "By the way... Did you do something to Bella at some point?"
        scene ee237 with dssa
        mi "Huh?"
        scene ee239 with dssa
        d "She said-"
        scene ee240 with dssa
        mi "I know what she's referring to."
        mi "And I apologized to her so many times. She didn't accept. There is nothing else I can do."
        scene ee241 with dssa
        d "What happened?"
        scene ee240 with dssa
        mi "I-"
        scene ee242 with dssa
        mi "Let's not kill the mood, please. I don't want to talk about it... not now, and not here."
        scene ee243 with dssa
        d "(Hmm, so there is more to it than just Bella being an ass.)"
    if miladate is True:
        pause
        scene ee243 with dssa
        pause
        scene ee244 with dssa
        mi "May I ask you something personal?"
        d "It depends. But go ahead."
        scene ee237 with dssa
        mi "Were you in a relationship before?"
        d "Yeah, I was. And you?"
        scene ee245 with dssa
        mi "It's hard to say if I ever was in one."
        mi "I dated a guy for one and a half months but that didn't work out so well."
        scene ee246 with dssa
        d "What happened?"
        scene ee247 with dssa
        mi "I think it goes back to... my mother."
        mi "I took my time and didn't sleep with him. I kept delaying it because... because I wanted to proof something to myself."
        scene ee246 with dssa
        d "You should change the way you dress, then. It's very promiscuous and might give some the wrong idea."
        scene ee248 with dssr
        mi "I want to keep dressing like this."
        mi "And just because I dress provocatively doesn't mean I'm easy."
        mi "I'm not some... prostitute."
        scene ee249 with dssa
        d "(The job of her mother and the social repercussion it brings must have affected her a lot.)"
        d "As long as you don't get paid for sex, you're not a prostitute."
        scene ee250 with dssa
        mi "You know what I mean."
        scene ee249 with dssa
        d "So, you're a virgin?"
        scene ee251 with dssa
        "Mila chuckles."
        mi "I am not a virgin."
        mi "Are you?"
        scene ee252 with dssa
        d "Yeah."
        scene ee253 with dssa
        "Mila slightly bites her lip."
        scene ee254 with dssa
        mi "And don't you think that we are going to sleep together after the date."
        scene ee255 with dssa
        d "I didn't think of it."
        scene ee254 with dssa
        mi "Just a heads-up."
        scene ee255 with dssa
        d "Even if you wanted to, I couldn't."
        scene ee256 with dssa
        mi "Why?"
        scene ee257 with dssa
        d "I'll tell you about it when we actually go out."
        scene ee256 with dssa
        mi "Now I'm worried."
    scene ee258 with dssa
    mi "Let me promise you something..."
    mi "If I ever get my pilot license and a plane... I'll give you a free-flight-with-Mila coupon."
    scene ee259 with dssa
    d "That sounds nice. I'll take it."
    scene ee260 with dssa
    pause
    scene ee261 with dssr
    pause
    scene ee262 with dssr
    pause
    mi "We should head back or we'll be late."
    stop sound fadeout 2.0
    jump Ch3x5sport


label Ch3x5sport:
    stop music fadeout 2.5
    play music "music/VeskyBeyondTheWindow.ogg"
    scene black with Dissolve(2)
    with Pause(.5)
    if BellaKiss03x is True:
        $ Bzh = True
        scene ab662 with dssb
        pause
        scene ab663 with dssb
        pause
        scene ab664 with dssa
        am "Bella? Why are you still here?"
        scene ab662 with dssb
        am "Bella?"
        scene ab665 with dssb
        b "Mh."
        scene ab666 with dssa
        am "W-What's wrong?"
        scene ab667 with dssa
        b "Leave me alone..."
        am "Why aren't you at the college?"
        scene ab669 with dssa
        "Bella inhales, sighs loudly and buries her face into her pillow."
        scene ab670 with dssa
        am "...The date with [name]."
        am "It didn't go so well, mh?"
        scene ab671 with dssb
        am "Honey..."
        b "It's not... *sigh*"
        b "Can you please just leave?"
        scene ab672 with dssa
        am "*sigh*"
        am "Give it some time. It will get better."
        scene ab673 with dssb
        am "I am off to work."
        stop music fadeout 2.5
    scene black with Dissolve(2)
    with Pause(.5)
    # show screen tooltip_LVROOF with blinds
    $ persistent.unlockedImageMusicOUT = True
    pause
    # hide screen tooltip_LVROOF with blinds
    $ play_playlist(playlist_GirlyPop)
    scene ab674 with dssb
    $ persistent.unlockedImageL1 = True
    n "Yeah, I stopped following them when they started to share this political bullshit."
    scene ab675 with dssa
    na "I know what you mean."
    scene ab677 with dssa
    so "Are we still doing this today?"
    scene ab676 with dssa
    na "Of course."
    na "I will take you with me afterwards."
    scene ab677 with dssa
    so "Thanks."
    scene ab678 with dssa
    pause
    scene ab679 with dssa
    pause
    scene ab680 with dssa
    pause
    scene ab682 with dssa
    pause
    scene ab683 with dssa
    mh "Good day, ladies."
    scene ab684 with dssa
    mh "The official ZPR training uniforms are here."
    scene ab685 with dssa
    n "Oh! Uniforms! I knew it!"
    scene black with Dissolve(3)
    with Pause(.5)
    scene ab686 with dssb
    na "Miss Hill."
    na "Whoever designed this needs to be fired."
    mi "The cleavage really is too much."
    scene ab689 with dssa
    mh "I know."
    mh "That's why everyone here should wear a bra with it."
    scene ab687 with dssa
    rob "The pants aren't much better."
    rob "It feels like they're inside of me..."
    $ persistent.unlockedImageSasha3 = True
    if BellaKiss03x is True:
        scene ab688 with dssa
    else:
        scene ab758 with dssa
    pause
    n "Who the hell designed these?"
    scene ab689 with dssa
    mh "We got three different designs from ZPR's design team."
    mh "Our top female athletes and members of the first team could vote for a design."
    scene ab690 with dssa
    mh "...And they chose this one."
    mh "I'll send a letter to them asking for a new design but don't get your hopes up."
    scene ab691 with dssa
    nia "I have nothing against dressing sexy... but how are the guys supposed to play properly when we look like this?"
    nia "Their poor boners!"
    scene ab692 with dssa
    nia "I changed my mind! I like these uniforms."
    scene ab693 with dssa
    n "I am more worried about how we should play in them."
    n "Are you okay Sonya?"
    scene ab694 with dssa
    $ persistent.unlockedImageSonya6 = True
    so "This makes me very uncomfortable."
    scene ab693 with dssa
    n "For the first time in my life... I'm glad I have small boobs."
    scene ab695 with dssb
    ay "Morning!"
    na "Morning, Ayua!"
    scene ab697 with dssb
    sas "That doesn't count."
    scene ab698 with dssa
    ay "Whyyyy not?!"
    scene ab699 with dssa
    sas "It's not even partially white."
    ay "But-"
    scene ab700 with dssa
    sas "I did let you off by agreeing to half-white."
    sas "Last chance."
    scene ab701 with dssa
    ay "Okay! Hardass! I'll visit Emilio again!"
    if BellaKiss03x is True:
        scene ab702 with dssa
        na "Ayua? Where is Bella?"
        scene ab703 with dssa
        ay "I have no idea... She isn't answering my texts."
        scene ab704 with dssa
        ay "Nami, do you know anything? I mean she went out with [name]."
        scene ab705 with dssa
        n "Uhm... Well..."
        scene ab706 with dssa
        na "What do you know, huuh?"
        scene ab707 with dssa
        n "They kissed."
        scene ab708 with dssb
        "Ayua and Nadia stare at Nami as if they've just seen a ghost."
        scene ab710 with dssa
        ay "A-are you telling us-"
        na "That Bella made out with [name]?"
        scene ab707 with dssa
        n "Yup."
        n "Why do you think we got drunk later?"
        scene ab711 with vpunch
        ay "Dibs on being Bella's bridesmaid!"
        na "I'll be her bridesmaid!"
        scene ab712 with dssa
        ay "You will have to fight me for it!"
        if RoRum is True:
            scene ab713 with dssa
            na "Talking about [name]... I saw him enter the ladies bathroom today."
            n "What?"
            na "Is [name] a creep?"
            scene ab714 with dssb
            rob "Oh, that was my fault."
            rob "I found [name] in the hallway and... he didn't look good. I wanted to speak to him in private and accidentally pushed him into the ladies bathroom."
            scene ab715 with dssa
            na "Oh, I was getting ready to have Ayua kick his ass."
            ay "Fight your own fights!"
            scene ab721 with dssa
            n "What was wrong with him?"
            scene ab716 with dssa
            rob "I can't say... He is not the most open person."
            n "Mhh, I will speak to him later."
            scene ab717 with dssa
            n "Hey, I'm Nami."
            scene ab718 with dssa
            sas "I'm Sasha."
            scene ab719 with dssa
            n "Where did you get tha-"
            scene ab722 with dssa
            "Nami stops mid-sentence."
            scene ab723 with dssa
            n "I am sorry... It might be a sensitive topic."
            scene ab720 with dssa
            "Sasha gives her a smile."
            scene ab725 with dssa
            ay "Do you think they did more than kissing?"
            scene ab724 with dssa
            na "No way."
            na "Bella would never go so far o-"
            scene ab725 with dssa
            ay "What?"
            na "I wasn't even able to predict those two dating. My opinion doesn't hold a lot of water right now."
            scene ab727 with dssa
            n "As I wanted to say... No way [name] went further than kissing."
            if miladate is True:
                $ Mkaykb = True
                scene ab728 with dssb
                mi "Uh- [name] kissing?"
                scene ab730 with dssa
                n "[name] and Bella made out."
                mi "Oh."
                "Mila takes an unusually long pause."
                mi "Good for them."
            else:
                scene ab729 with dssb
                mi "[name] kissed someone?"
                scene ab730 with dssa
                n "Bella."
                mi "Wow."
            scene ab731 with dssa
            mi "I... didn't see that coming."
            scene ab732 with dssa
            na "No one here did."
            scene ab733 with dssa
            ay "What is so special about [name], Nami?"
            scene ab734 with dssa
            n "Uh- I don't know?"
            scene ab735 with dssa
            nia "Maybe sweet emo-boy has a reaaaally big penis."
            ay "Did you see his thing?"
            scene ab736 with dssa
            nia "No."
            nia "But Nami must be familiar with his penis."
            scene ab737 with dssa
            pause
            scene ab741 with dssa
            pause
            scene ab742 with vpunch
            n "Why the hell are y'all looking at me?! I'm not familiar with his... thing!"
            scene ab738 with dssa
            ay "So you've never seen it before."
            scene ab737 with dssa
            n "Of course I have seen it."
            scene ab739 with dssa
            mi "*whisper* How big is it?"
            scene ab742 with dssa
            n "It's-"
            scene ab743 with vpunch
            n "W-wait! NO!"
            n "I will not tell you weirdos about his thing!"
            scene ab740 with dssa
            nia "It must be gigantic!"
            nia "Maybe if the guys also got super tight uniforms and we can confirm his whopping penis!"
            rob "Size isn't everything."
            scene ab743 with dssa
            n "Enough with the talk about his penis!"
            nia "*giggle*"
            scene ab744 with dssa
            nia "But Robin..."
            nia "Is it true that you had sex with [name] in the bathroom?"
            scene ab746 with vpunch
            n "What?!"
            scene ab750 with vpunch
            rob "What?!"
            scene ab745 with dssa
            nia "Uhhh- That's what the people on the campus say?"
            rob "No! Nothing happened!"
            scene ab747 with dssa
            n "What are they saying?"
            nia "That they found [name] and Robin in a stall. Apparently Robin was doing him cowgirl style."
            scene ab751 with vpunch
            rob "*Screams* We were completely dressed!"
            scene ab748 with dssa
            n "I thought you just pushed him into the restroom to talk?"
            scene ab752 with dssa
            rob "Y-yes! But- we then heard voices and I pushed him into the stall!"
            rob "And I had to sit on his lap so they wouldn't see our feet!"
            rob "Nothing else happened!"
            scene ab753 with dssa
            sas "Robin. Calm down."
            scene ab754 with dssa
            n "So you weren't naked?"
            scene ab755 with vpunch
            rob "NO! Ask [name]!"
            scene ab749 with dssa
            n "Okay- Sorry."
            scene ab756 with dssa
            "Sasha grabs Robin and whispers something into her ear."
            scene ab757 with dssa
            pause
            n "I gotta talk to [name]."
    else:
        if RoRum is True:
            na "Talking about [name]... I saw him in enter the ladies bathroom today."
            n "What?"
            na "Is [name] a creep?"
            n "He is no cre-"
            scene ab714 with dssb
            rob "Oh! That was uhm my fault."
            rob "I- uhh talked with him because he didn't look good."
            scene ab759 with dssa
            b "That's common knowledge."
            ay "Stop it, Bella."
            scene ab716 with dssa
            rob "He had something on his mind- Or at least he was startled by something."
            scene ab744 with dssa
            nia "But Robin..."
            nia "Is it true that you had sex with [name] in the bathroom?"
            if BellaKiss03x is False and MCBL >=1 and BTY is True:
                scene ab760 with vpunch
                b "What?!"
            scene ab747 with vpunch
            rob "What?!"
            scene ab745 with dssa
            nia "Uhhh- That's what the people on the campus say?"
            rob "No! Nothing happened!"
            scene ab747 with dssa
            n "What are they saying?"
            nia "That they found [name] and Robin in a stall. Apparently Robin was doing him cowgirl style."
            scene ab751 with vpunch
            rob "*Screams* We were completely dressed!"
            scene ab748 with dssa
            n "I thought you just pushed him into the restroom to talk?"
            scene ab752 with dssa
            rob "Y-yes! But we then heard voices and I pushed him into the stall!"
            rob "And I had to sit on his lap so they wouldn't see our feet!"
            rob "Nothing else happened!"
            scene ab753 with dssa
            sas "Robin. Calm down."
            scene ab754 with dssa
            n "So you weren't naked?"
            scene ab755 with vpunch
            rob "NO! Ask [name]!"
            scene ab749 with dssa
            n "Okay- Sorry."
            scene ab756 with dssa
            "Sasha grabs Robin and whispers something into her ear."
            scene ab757 with dssa
            pause
            if BellaKiss03x is False and MCBL >=1 and BTY is True:
                scene ab761 with dssa
                b "What a fucking joke."
                pause
                scene ab763 with dssa
                $ persistent.unlockedImageBella21 = True
                rob "What the..."
                na "*sigh* Don't worry, Robin."
                rob "What's her problem? It almost sounds like she is-.. Oh."
                scene ab764 with dssa
                if BTY is True:
                    sas "She's in love."
                else:
                    sas "She could be in love."
                scene ab765 with dssa
                ay "I think they really are in love."
                scene ab767 with dssa
                n "Wow, wow, wow!"
                n "Bella might be in love with him! But I doubt that he is in love with her."
                rob "I think they're a sweet couple."
                scene ab768 with dssa
                n "Nooo! Eww."
                scene ab770 with dssa
                na "Hey! Don't be like that Nami."
                na "I think they're great together, too."
                scene ab773 with dssa
                nia "Bella is always so angry... and [name] is hot... I think we should lock them in a room for two days and let them bang it out."
                scene ab774 with dssa
                n "No sex with [name]!"
                scene ab777 with vpunch
                ay "...Now I want to have sex with [name]!"
                scene ab778 with vpunch
                n "What?!"
                scene ab777 with vpunch
                ay "You said I can't have it! Now I want it!"
                scene ab778 with vpunch
                n "No!"
                scene ab777 with vpunch
                ay "Yes!"
                scene ab765 with dssa
                ay "I bet [name] has a big thing."
                scene ab768 with vpunch
                n "Ugh! No talking about [name]'s thing!"
                scene ab762 with dssa
                b "I bet he has a little clit-like thing."
                scene ab767 with vpunch
                n "He certainly doesn't!"
                scene ab762 with dssa
                b "Oh? And you know that how?"
                scene ab767 with dssa
                n "Because we share a bathroom?"
                scene ab766 with dssa
                ay "Did you see his erect penis?"
                scene ab767 with dssa
                n "Wh- no!"
                scene ab769 with dssa
                ay "Only the erect penis size matters."
                scene ab770 with dssa
                na "True."
                scene ab771 with dssa
                rob "Grower was it, right? When it grows a lot in the aroused state?"
                nia "Yes and the opposite is a Shower."
                scene ab772 with dssa
                na "That sounds disgusting."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ab782 with dssb
    pause
    scene ab783 with dssa
    rep "You got it?!"
    scene ab784 with dssa
    mik "Yes, boss."
    rep "SAKI!"
    scene ab785 with dssa
    sak "Y-es?"
    scene ab786 with dssa
    rep "Didn't we talk about this?"
    scene ab787 with dssa
    sak "I don't feel comf-"
    scene ab788 with vpunch
    pause
    scene ab789 with dssa
    pause
    scene ab790 with dssa
    nico "Saki- If I wanted someone to write on a fucking yellow notepad- I could have hired that homeless dude across the street!"
    scene ab791 with dssa
    nico "I hired you because of your assets! If you cannot provide me with that asset, you're worthless to me. And I'll send you and your family back to whatever shithole you come from!"
    sak "I- I was born here."
    scene ab792 with vpunch
    nico "So Saki... Be a nice girl and do what mommy Nicole tells you."
    "Nicole pauses."
    scene ab794 with dssa
    nico "Are you a good girl Saki?"
    scene ab793 with dssa
    sak "Yes, I am."
    scene ab798 with dssb #REC postwork
    nico "Good morning to all our viewers!"
    nico "We are here on the campus of the Sovereign Vipers!"
    nico "Last year the team didn't make it into the playoffs due to not fulfilling the regulations... And because certain team member had an unhealthy liking for cocaine."
    scene ab799 with dssa
    nico "But with its new sponsor, the tides might have changed."
    nico "We are excited to see the newcomers this year and who knows what hidden gem they have in store for us."
    scene ab800 with dssa
    nico "We are in for an interesting season!"
    if RoRum is True:
        $ ConfSto = True
        nico "And not just because of the upcoming games."
        nico "My inside sources have revealed that there is already a sex scandal!"
        nico "Two freshmen were already caught having sex in a bathroom stall."
        nico "We of course value privacy a lot..."
        scene ab801 with dssb
        pause
        scene ab802 with dssa
        pause
        scene ab803 with vpunch
        nico "Here we have one of the students-"
        nico "Excuse me!"
        nico "[name] Cyrus- What is the intent behind your actions?"
        scene ab804 with dssa
        "You and Trey give each other a confused look."
        scene ab805 with dssa
        nico "Is it a personal goal of yours to have sexual intercourse with as many females as possible?"
        scene ab806 with dssa
        "You just stare at her, not knowing what is going on."
        scene ab807 with dssa
        nico "Write down that he nodded."
        d "I didn't nod."
        play music "music/Suspense/Scott Buckley - Resonance.ogg"
        scene ab808 with vpunch
        u "HEY!"
        scene ab809 with dssa
        u "Get the fuck out of here!"
        scene ab810 with dssb
        pause
        "Nicole slowly turns to the guy."
        scene ab811 with dssa
        nico "Or what?"
        nico "You'll kick me out?"
        scene ab812 with dssa
        u "We'll rough you up... and then we'll kick you out."
        scene ab813 with dssa
        pause
        scene ab814 with dssa
        "Nicole slides her glasses down."
        scene ab815 with dssb
        nico "I'm sure we'll meet again."
        scene ab816 with dssb
        pause
        scene ab817 with dssb
        d "What was that about?"
    else:
        play music "music/Suspense/Scott Buckley - Resonance.ogg"
        scene ab808 with vpunch
        u "HEY!"
        scene ab809 with dssa
        u "Get the fuck out of here!"
        scene ab810 with dssb
        pause
        "Nicole slowly turns to the guy."
        scene ab811 with dssa
        nico "Or what?"
        nico "You'll kick me out?"
        scene ab812 with dssa
        u "We'll rough you up... and then we'll kick you out."
        scene ab813 with dssa
        pause
        scene ab814 with dssa
        "Nicole slides her glasses between her breasts."
        scene ab816 with dssb
        pause
        scene ab817 with dssb
        d "What was that about?"
    scene ab819 with dssa
    $ persistent.unlockedImageMusicEly = True
    # show screen tooltip_NewSong with blinds
    pause
    # hide screen tooltip_NewSong with blinds
    u "That cunt is always on the hunt for the next scandal. Literally anything that will bring in the viewers and destroy your whole image."
    u "That bitch has no boundaries and would destroy your life without blinking an eye."
    u "Be careful who you bed- and where."
    scene ab818 with dssa
    d "That sounds personal. What did she do to you?"
    u "It is indeed personal."
    if fitness is 2 or fitness is 1 and mobility is 1:
        scene ab820 with dssb
    else:
        scene ab821 with dssb
    u "You boys make sure to keep your distance. Don't let those tits fool you."
    u "She has destroyed more than enough lives already."
    stop music fadeout 2.5
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_GirlyPop)
    scene ab1429 with dssb
    pause
    scene ab1433 with dssa
    pause
    scene ab1430 with dssb
    pause
    scene ab1431 with dssb
    pause
    scene ab1432 with dssa
    pause
    if RoRum is True:
        scene ab822 with dssb
        t "Is it true that you did Robin?"
        scene ab823 with dssa
        d "What?"
        t "The whole campus is talking about it."
        d "It is not true."
    else:
        scene ab822 with dssb
        t "What the fuck was that?"
        scene ab823 with dssa
        d "No idea. But that reporter is trouble."
    scene ab824 with dssa
    zar "Hey you two."
    scene ab825 with dssa
    zar "You can start stretching here with us."
    t "Stretching is for puss bois."
    scene ab826 with dssa
    zar "Shut up, meat head."
    scene ab827 with dssa
    mh "Trey. I think you will be good with Zara."
    d "I will go-"
    scene ab828 with vpunch
    mh "Not so fast."
    scene ab829 with dssa #Clean out the weights
    mh "No- Sasha here needs a partner."
    scene ab830 with dssa
    sas "I'm uncomfortable doing this with a male."
    scene ab831 with dssa
    mh "I am not asking you two to dry hump."
    mh "Get some good stretches in and that's it."
    d "I think she can handle herself- and I can just copy Nami."
    scene ab832 with dssa
    mi "Don't forget to breathe!"
    scene ab833 with dssa
    n "I c- can't!"
    pause #augenbrauen hoch
    stop music fadeout 2.5
    scene ab834 with dssb
    $ persistent.unlockedImageMusicCant = True
    pause
    $ play_playlist(playlist_BellchenDinnerx)
    d "*sigh*"
    scene ab835 with dssa
    sas "I am already warmed up."
    scene ab836 with dssa
    d "Then just introduce me to some stuff."
    d "Things I can also do at home on my own."
    scene ab837 with dssb
    "Sasha goes into the 'plank'."
    sas "Follow my lead."
    scene ab838 with dssa
    pause
    scene ab839 with dssa
    d "Am I doing it correctly?"
    scene ab840 with dssa
    pause
    scene ab841 with dssa
    sas "Your derrière is too high in the air."
    scene ab842 with dssa
    d "My what?"
    scene ab843 with dssa
    sas "Your butt."
    scene ab844 with dssa
    d "*chuckles* Derrière- haha..."
    "You get in position."
    scene ab845 with vpunch
    n "Yo! In one week- plank duel!"
    scene ab846 with dssa
    n "If I- argh- w-win, you'll get me some cake!"
    scene ab847 with dssa
    mi "Nami, concentrate."
    scene ab848 with dssa
    d "It hurts."
    scene ab849 with dssa
    sas "That's the point."
    scene ab850 with vpunch
    "You drop to the floor."
    scene ab851 with dssa
    t "I- can't!"
    scene ab852 with vpunch
    zar "You're an embarrassment to this college!"
    scene ab853 with dssa
    zar "If you even make it into the second team, I'm transferring to another college!"
    scene ab854 with dssa
    d "What now?"
    scene ab855 with dssa
    pause
    scene ab856 with dssa
    "You try to mimic her pose."
    scene ab857 with dssa
    pause
    scene ab858 with vpunch
    pause
    scene ab859 with dssa
    "Sasha gently grabs your leg and straightens it."
    scene ab860 with vpunch
    "You gasp and grab her hand."
    scene ab861 with dssa
    d "It hurts-"
    scene ab862 with dssa
    d "-a lot."
    scene ab863 with dssa
    pause
    scene ab864 with dssa
    "Sasha gently straightens it again- not as much this time."
    scene ab865 with dssa
    d "No more."
    "She nods slightly."
    scene ab866 with dssa
    pause
    scene ab867 with dssa
    "Sasha gently pushes her hand down- slightly grabbing your thigh."
    scene ab868 with dssa
    d "I'm sorry I grabbed you like that before."
    scene ab869 with dssa
    sas "I should've considered your current state before over-stretching it."
    sas "You were already struggling doing it on your own- I don't know why I thought pushing would help."
    scene ab870 with dssa
    d "It did help- well, now it helps- you're doing it more gently."
    scene ab909 with dssb
    lay "Sasha, don't kill him before the season even starts."
    scene ab871 with dssa
    sas "Only the strong survive."
    scene ab873 with dssa
    ay "You're one to talk."
    ay "I am still waiting for you to beat me once."
    scene ab872 with dssa
    sas "It's only a matter of time until I beat you."
    sas "...I never give up."
    scene ab874 with dssb
    ay "*whisper* I know you don't..."
    scene ab875 with dssa
    sas "The other leg."
    scene ab876 with dssa
    d "Why are you staring at my crotch?"
    scene ab877 with dssa
    ay "...No reason."
    scene ab878 with dssa
    ay "Yo Layla, when is the official opening of the bar?"
    scene ab910 with dssb
    lay "On Monday. My Mom is currently appealing to the dean about giving the students time off to celebrate it."
    scene ab911 with dssa
    ay "That means Monday- big party at the bar?"
    scene ab910 with dssa
    lay "Yes."
    scene ab879 with dssb
    ay "Sasha, you will be there too."
    scene ab880 with dssa
    sas "I might not make it."
    scene ab881 with dssa
    $ persistent.unlockedImageAyua2 = True
    ay "Oh. This wasn't a question. You will be there you old bookworm."
    scene ab883 with vpunch
    "Ayua punches her on the shoulder-"
    "- causing Sasha to over-straighten your leg."
    ay "Oops."
    scene ab853 with dssb
    za "Are you crying?"
    t "...N-o."
    scene ab870 with dssb
    d "How long is it gonna be until this stops hurting so much?"
    scene ab884 with dssa
    sas "Depends on how consistent you are."
    scene ab885 with dssa
    sas "If you do it only twice a week, don't expect much."
    scene ab886 with dssb
    pause
    scene ab887 with dssb
    sas "Now this."
    d "Are you trying to kill me?"
    scene ab888 with dssa
    sas "*Whisper* I'd rather not say."
    $ persistent.unlockedImageSasha4 = True
    scene ab889 with dssb
    pause
    scene ab891 with vpunch
    "You swing back to get into position-"
    scene ab892 with vpunch
    pause
    scene ab893 with dssb
    pause
    scene ab894 with dssa
    d "Sorry. I should probably stick to the basics."
    scene ab909 with dssb
    lay "You need to pay more attention as a trainer."
    scene ab895 with dssb
    sas "Being forced into a position you don't want to be in is- unfortunate for both sides."
    scene ab896 with dssb
    sas "I apologize for not being able to help you."
    scene ab897 with dssa
    d "It's alright. And you did help me, you're very flexible- it shows me what is possible."
    d "And I want to be more flexible."
    scene ab898 with dssa
    sas "What is the driving force behind this?"
    scene ab900 with dssa
    sas "What is the - 'reason'?"
    d "Muscles are worthless if you're unable to use them to their full extent."
    scene ab901 with dssa
    sas "They look good."
    scene ab902 with dssa
    d "I don't care about looks."
    sas "Then what is it that you desire-"
    scene ab903 with vpunch
    "You deflect the incoming basketball."
    scene ab904 with dssa
    pause
    scene ab905 with dssb
    rob "Oh god! I am so sorry!"
    scene ab909 with dssa
    lay "That was one hell of a reflex."
    scene ab906 with dssb
    if mobility is 1:
        d "Seems like we're even now."
        scene ab907 with dssa
        sas "Seems like it."
    else:
        d "Close call."
        scene ab908 with dssa
        sas "Thank you."
    scene ab910 with dssa
    lay "There is a yoga course twice a week if you're really interested in getting more flexible."
    scene ab911 with dssa
    d "I can just join it?"
    scene ab910 with dssa
    lay "Yes. If you don't have a problem with being made fun of because you would be the only guy there. But if your goal is to get more flexible..."
    lay "...With suitable trainers, this is the place."
    lay "Talk to me on Wednesday if you still want to go there."
    scene ab912 with dssa
    lay "But let me warn you... The girls there are not so fond about boys."
    scene ab913 with dssa
    d "Why?"
    scene ab912 with dssa
    lay "Let's say... 99 percent of the guys that join this course are there to perv."
    lay "So keep it in your pants."
    scene ab914 with dssa
    d "I'll be there."
    scene ab915 with dssa
    d "Thanks for your help, Sasha."
    "Sasha nods."
    if BellaKiss03x is False:
        scene ab916 with dssb
        d "Hey."
        scene ab917 with dssa
        b "Oh! I am so sorry."
        scene ab918 with dssa
        d "...What?"
        scene ab919 with dssa
        b "I couldn't find your balls in there."
        scene ab920 with dssa
        "Bella then chuckles at her own joke."
        d "You laugh at your own jokes?"
        scene ab921 with dssa
        b "Sometimes, even I am surprised at how funny I can be."
        d "Can we scrap today's work assignment?"
        if BTY is False:
            scene ab923 with dssb
        else:
            scene ab924 with dssb
        b "I already told you I would leave in the afternoon."
        b "And you got your nerd meet-up, right?"
        d "Don't act like you never played it with them."
        scene ab925 with dssb
        b "Nadia invited me once and kept yelling at me for not understanding the hundreds of rules."
        $ persistent.unlockedImageBella22 = True
        if RoRum and bellagym is True:
            b "I am surprised you got it up for Robin, though."
            d "Fuck off."
            d "It's obviously a lie."
            scene ab928 with dssb
            b "I know. If you didn't get it up for me... you certainly wouldn't for her."
            scene ab929 with dssa
            d "I think there is a higher chance of me sleeping with Robin than with you."
            scene ab930 with dssa
            b "Ohhh nooo. I am heart broken."
            d "(Squeezing and teasing her breasts to me in public... Her moves are getting more... desperate?)"
            d "(I should probably talk to her about it... or let it go on a while longer.)"
        b "It seems like you redirected your eyes onto a new target."
        scene ab931 with dssa
        d "I didn't expect you to be such a jealous worm."
        b "Jealous?!"
        d "Yes."
        scene ab932 with dssa
        b "I am no-"
        scene ab933 with dssa
        "You just leave her standing."
    scene ab934 with dssb
    d "Yo."
    scene ab935 with dssa
    n "Y-yo."
    n "You came here to see me getting stretched out, huh? Huh?"
    d "I fucking hate you."
    scene ab936 with dssa
    n "Hah-a--aaargh- I am funny."
    scene ab937 with dssa
    mi "You are so much stiffer than you look."
    scene ab938 with dssa
    n "I sit too much in front of my PC and last time I wanted to do some yoga... I found some beer instead."
    d "Two weeks from now... flex-duel."
    scene ab939 with vpunch
    n "YOU'RE ON!"
    scene ab940 with vpunch
    na "Zaaraaaaa!"
    scene ab941 with dssa
    zar "Nadia!"
    scene ab942 with vpunch
    pause#hug
    scene ab944 with dssb
    d "You're still alive?"
    t "I don't know... Is Victoria here?"
    t "I might need to borrow her chair."
    scene ab945 with dssa
    d "I do wonder where Victoria is..."
    scene ab946 with dssa
    mi "She is with Miss Marla- she wanted to speak to her."
    mi "Victoria will join us in the next session."
    stop music fadeout 2.0
    $ play_playlist(playlist_RockPop)
    scene ab947 with dssb
    "Trey and you sit down on the stairs."
    scene ab948 with dssb
    t "So they are here..."
    d "Who?"
    t "The first team."
    scene ab949 with dssa
    d "And why is that a problem?"
    scene ab950 with dssa
    t "You remember what the coach said? That we are all on the team?"
    d "Yeah."
    scene ab951 with dssa
    t "That was bullshit."
    d "Why would he say it then?"
    t "Because he is an ass."
    scene ab952 with dssa
    t "They want us to believe that everyone at least makes the third team so they can see who has the right spirit, even when they think it is a sure thing."
    t "There are multiple teams here, buddy."
    scene ab953 with dssa
    t "One team unisex, nobody takes them seriously and they play more or less for fun."
    t "And then it starts with the third team... Good enough to be selected but still at the bottom."
    scene ab955 with dssa
    t "The second team... Basically just a limbo."
    t "And of course the first team."
    t "I asked a buddy of mine and he said there aren't many spots on the team."
    scene ab955 with dssa
    t "We need to step our game up if we want to get in."
    scene ab954 with dssa
    d "I like a challenge."
    scene ab956 with vpunch
    u "Ahh, Jake! Look what we got here!"
    jak "Babies!"
    scene ab957 with dssa
    u "You two babies want into the team?"
    t "We-"
    if RoRum is True:
        scene ab958 with dssa
        u "That's the guy that banged the chick on the toilet?"
        u "Seems like it."
        scene ab961 with dssa
        u "Nice."
    else:
        u "Ay, this guy here has an ice cold stare."
        scene ab961 with dssa
        jak "Oh... we got a dangerous boy over here, huh?"
    scene ab962 with dssa
    n "Yo, what are-"
    scene ab963 with vpunch
    zar "Stay here and stretch with us."
    scene ab965 with dssa
    n "What?"
    zar "Stay out of it."
    scene ab966 with dssa
    n "They might be picking on [name]!"
    scene ab968 with dssa
    zar "If you go over there and make a scene, you will ruin [name]'s chances for the team."
    zar "Is that want you want?"
    scene ab967 with dssa
    n "No! O-of course not- but-"
    scene ab968 with dssa
    zar "Guys are jerks and if you go over there you will make [name] look like the biggest pussy in the world."
    scene ab969 with dssa
    zar "And he will never overcome the fact that a girl had to defend him."
    n "*sigh*."
    scene ab970 with dssa
    na "She is right."
    scene ab971 with dssa
    nan "Boys are going to be boys. You need to let them work it out."
    scene ab972 with dssb
    pause
    scene ab974 with dssb
    u "Are these the freshmen??"
    scene ab975 with dssa
    jak "Two of them."
    scene ab976 with dssa
    pause
    scene ab977 with dssa
    u "Show me your ass."
    t "What?"
    scene ab978 with dssa
    u "I want to see your ass."
    t "My- ass?"
    scene ab979 with dssa
    u "Guys! Inspection!"
    scene ab980 with vpunch
    t "Yo- what-"
    scene ab981 with dssa
    u "Mhm mhm..."
    u "Quite a few punctures."
    scene ab982 with dssa
    u "You think steroids will get you on to the team?"
    scene ab983 with dssa
    u "No, the only way on to this glorious team is with hard work and dedication."
    scene ab984 with vpunch
    play sound "music/SFX/Slap.mp3"
    pause
    scene ab1003 with dssb
    u "-and dedication."
    scene ab982 with dssa
    u "Think about it the next time you grab the needle."
    scene ab985 with dssa
    u "And... you can thank me later for not letting Larry do the inspection."
    u "He likes to... 'look' a little deeper."
    scene ab986 with dssb
    pause
    scene ab987 with dssb
    pause
    scene ab988 with vpunch
    pause
    scene ab989 with dssb
    u "*Whisper* I like you."
    scene ab1004 with dssb
    nia "Are they gonna kiss?"
    ay "I'd like to see that."
    scene ab990 with vpunch
    ms "Dwight, stop turning [name] into one of your bitches."
    scene ab991 with dssa
    dwi "Coach- oh... You're not a coach yet... Sorry my bad."
    dwi "You're gonna go for it again?"
    scene ab992 with dssa
    ms "Bet your ass on it."
    scene ab993 with dssb
    ms "Spaghetti! Juicebox! Get over here, you're not ready for this stage yet."
    scene ab994 with dssa
    t "...They violated me."
    d "Be glad it wasn't Larry."
    scene ab995 with dssb
    u "Second class coach Stahl."
    scene ab996 with dssa
    ms "I am surprised you were able to cross the bridge between our world and hell."
    scene ab997 with dssa
    u "I heard you and Miss Silicone are trying to get into the first league."
    scene ab998 with dssa
    ms "We are the first league."
    scene ab999 with dssa
    u "You are nothing. You didn't make it on to the first team last year and you won't make it this year."
    u "You just aren't made for this!"
    scene ab1000 with dssa
    u "But maybe you get a shot as an assistant if you cut that disgusting pubic hair off your face."
    scene ab1001 with dssb
    t "Who was that?"
    scene ab1002 with dssa
    ms "She is part of the first team's coaching squad."
    ms "Fucking cunt."
    scene ab1005 with dssa
    t "It seems like we are not the only ones with internal rivals."
    scene ab1006 with vpunch
    nan "It makes you wonder what is really going on between the professors and the faculty staff, huh?"
    nan "They always act so professional in front of us students... but who knows how much they compete with each other really?"
    scene ab1007 with dssa
    t "The old hag Marla is probably most hated."
    scene ab1008 with dssb
    mh "Everyone! Get your asses over here!"
    scene ab1009 with dssa
    ms "Nami, Zara, Nadia, get over here."
    scene ab1010 with dssb
    mh "Are you okay?"
    scene ab1011 with dssa
    ms "I am great!"
    scene ab1012 with dssa
    mh "The only time you call students by their real name is when you're mad... Mad as fuck."
    mh "Let me take an educated guess."
    mh "Cunt Glitter and her faithful steed swung by??"
    scene ab1013 with dssa
    ms "It doesn't matter."
    scene ab1014 with dssa
    mh "We're getting up there this year and I have a plan on how we do that."
    scene ab1015 with dssa
    ms "I am all ears."
    scene ab1016 with dssb
    pause
    scene ab1017 with dssa
    n "Everything okay?"
    d "Mh?"
    scene ab1018 with dssa
    n "Just asking away."
    d "I am good."
    if RoRum is True:
        scene ab1019 with dssa
        n "What is this rumor about you and Robin?"
        d "It's a lie."
        d "Robin and I just hid in the stall. Nothing happened."
        d "Those fucking lying bitches."
        scene ab1018 with dssa
        n "Who found you?"
        d "I don't know them- but I will find out who came up with that shit."
    scene ab1020 with dssb
    j "Morning."
    t "Sup bro."
    scene ab1021 with dssa
    j "Oh, I see."
    j "Seems like classes for the first players started."
    scene ab1022 with dssa
    u "Yo!"
    scene ab1023 with vpunch
    u "My MAN! Great to see you!"
    j "What's up Dex!"
    scene ab1024 with dssa
    dex "I hope you are in top form, not many free spots on the team this year."
    dex "Hell, even the second team is full of decent players."
    dex "*Whisper* And I will talk to the coaches and put in a good word for you."
    scene ab1025 with dssa
    j "Thanks bro."
    scene ab1026 with vpunch
    n "Busted! You cheater!"
    scene ab1027 with dssa
    j "It's not cheating. That's how the world works, Nami."
    if fitness == 2 or fitness == 1 and mobility == 1:
        $ JeffTeamHelp = True
        j "Just like my boy Dex helps me, I will help [name] and Trey."
    scene ab1028 with dssa
    dam "Hi guys."
    j "Ahh- Damian!"
    $ persistent.unlockedImageNancy2 = True
    scene ab1029 with dssa
    d "Hey."
    scene ab1030 with dssa
    dam "The players, huh."
    scene ab1031 with dssa
    t "Makes you wonder where all the female players are."
    scene ab1032 with dssa
    zar "If you are talking about the cheerleaders, they are in a meeting."
    scene ab1035 with dssa
    n "Do you want to be one of them?"
    scene ab1033 with dssa
    zar "No?! The only girls who join the cheerleaders are the ones that didn't make it into the first team."
    scene ab1035 with dssa
    n "So there is also a woman's first team?"
    scene ab1034 with dssa
    na "Of course."
    scene ab1036 with dssa ####Load in again and do the rest.
    j "Bro... You aiming high?"
    scene ab1036x with dssa
    d "You mean if I want to go for the first team?"
    scene ab1036 with dssa
    j "Yeah."
    scene ab1036x with dssa
    d "Yeah, I am going for it."
    scene ab1036x2 with dssa
    $ JGW = 0
    if fitness == 2:
        $ JGW +=1
        j "I see you have been taking care of yourself."
        j "I can already spot some little gains."
        j "I am proud of you."
    elif fitness == 1 and mobility == 1:
        $ JGW +=1
        j "I see you have been taking care of yourself."
        j "I can already spot some little gains."
        j "I am proud of you."
    scene ab1037 with dssa
    dam "I want to go for it, too."
    scene ab1038 with dssa
    j "Seriously?"
    dam "Hey man! Just because I am a dwarf doesn't mean I'm useless!"
    scene ab1039 with dssa
    j "Don't get me wrong, I can imagine a lot of uses for someone like you."
    scene ab1040 with dssa
    d "What is needed to get into the team?"
    j "Impress the coaches... Get good with the first team... and beat everyone in the second team."
    j "If you get a yes from captain Dwight, Dex and Aziz, you are pretty much in."
    j "They can build up enough pressure on a coach."
    scene ab1041 with dssa
    t "Fuck man... I am afraid not all of us will get into the second team after the tryouts."
    t "What if I land in the third team?!"
    scene ab1042 with dssa
    ms "Only the strong survive."
    ms "Now get in line."
    scene ab1043 with dssa
    d "How good is our first team?"
    ms "It's the first year we are able to compete in the real league."
    ms "We managed to beat all the teams in the lower league... but we're playing with the big boys now."
    ms "All the other teams are currently looking down at us, which gives us the role of the underdog."
    scene ab1044 with dssa
    n "What about the females?"
    scene ab1045 with dssa
    dam "Are they hot?"
    scene ab1046 with vpunch
    ms "What do you think, Bilbo?"
    ms "They are our top female athletes."
    ms "Now go build a line!"
    scene ab1047 with dssb
    pause
    scene ab1048 with vpunch
    n "Yo, I will go first league, too!"
    scene ab1049 with dssa
    d "I was sure you were about to say that it is too much work."
    scene ab1050 with dssa
    n "We can be lazy when we hold that trophy in our hands!"
    scene ab1051 with dssa
    zar "You mean when I hold it in my hand, and you have the honor to stand beside me?"
    scene ab1052 with dssa
    na "You are just holding it because my shoe was untied, and I had to tie it."
    scene ab1053 with dssa
    n "If someone is holding the trophy it's the star play-"
    scene ab1054 with dssa
    zar "*Laughs* Nami... Oh Nami..."
    scene ab1055 with dssa
    zar "You might be able to beat her-"
    scene ab1056 with dssa
    na "Me? I am better than you!"
    scene ab1057 with dssa
    zar "I am literally better in everything!"
    scene ab1058 with dssa
    pause
    scene ab1059 with dssa
    za "You suck."
    scene ab1060 with dssa
    na "You suck."
    scene ab1058a with vpunch
    zar "NO YOU SUCK!"
    na "NO YOU!"
    scene ab1061 with vpunch
    mh "Alright, Ladies."
    mh "Save it for on the field."
    scene ab1062 with dssb
    n "I will beat them both!"
    scene ab1063 with dssa
    d "Do it smart."
    d "I can sense a huge rivalry between Zara and Nadia."
    d "Use it to your advantage."
    if RoRum is True:
        scene ab1064 with dssa
        rob "Hey, can we talk?"
        d "I assume it is about the stupid rumors?"
        rob "Yes."
        scene ab1065 with dssb
        rob "Let's uh- get out for a second?"
        scene black with Dissolve(2)
        with Pause(.5)
        scene ab1339 with dssb
        d "Do you know who started them?"
        rob "It has to be one of those girls that busted us."
        d "Busted? There was nothing to bust."
        scene ab1341 with dssa
        rob "Well- we were hiding in a bathroom stall."
        rob "...Shit."
        d "I will find out who did that."
        scene ab1342 with dssa
        rob "Okay... We should maybe talk to a professor... explain the situation..."
        scene ab1344 with flash
        nico "Oh... that's a good one. *chuckles*"
        scene ab1345 with dssb
        nico "Angles are a bitch... Feeling up her butt in public... Tzz."
        scene ab1343 with dssb
        rob "I bet it has already gotten back to the dean.."
        d "Miss Harrison should be able to back us. She saw me leaving in... a weird condition."
        rob "Okay."
        scene black with Dissolve(2)
        with Pause(.5)
    scene ab1066 with dssb
    dam "I wasn't made for basketball, man."
    scene ab1066 with dssa
    d "You're tiny."
    scene ab1067 with dssa
    dam "Thanks, Captain Obvious."
    scene ab1068 with dssa
    d "That can be an advantage."
    d "A lurch like Jeff couldn't catch you."
    j "Hey!"
    scene ab1069 with dssa
    dam "I'm probably not even gonna make the third team..."
    scene ab1070 with dssa
    n "Not with that attitude, Damian!"
    n "Be strong and confident."
    scene ab1071 with dssb
    d "I'll tell you something, my strength is to shoot and make those baskets."
    d "Back in the days I used to be quite good at shooting three pointers. I can hit targets from a mile away."
    d "My uncle used to train me when I was little and I dominated in high school basketball... But I quit half a year in."
    scene ab1072 with dssa
    n "He is not lying. I saw it myself when I watched his games. He has talent."
    n "He would have made the high school basketball team as a starter if... something wouldn't have happened. "
    scene ab1073 with dssa
    d "You're small and fast."
    d "There might not be a lot of free spaces... but there is also the chance to replace someone that is currently on the team."
    d "And even if you hit the third team... You can always get out of there."
    scene ab1074 with vpunch
    d "I want onto the team and so do you. Let's work together."
    scene ab1075 with dssa
    "Damian lightens up."
    d "(As much as I love riding solo... you're unable to develop your full potential alone. Surround yourself with people that have the same level of ambitions.)"
    scene ab1076 with dssa
    t "I might not be the fastest or tallest..."
    scene ab1077 with vpunch
    t "But I have a strong core stability and a high jump, nobody gets past me without working his way through."
    scene ab1078 with dssb
    j "I might have Dex on my side but that's not a guarantee to get in."
    scene ab1079 with vpunch
    j "Let's work together boys."
    scene ab1080 with dssb
    j "We're all gonna make it."
    scene ab1081 with dssb
    n "Man, I wish we girls had such a cohesion."
    scene ab1082 with dssa
    zar "Friendships between guys are different... Most likely a lot less backstabbery than girl friendships."
    scene ab1081 with dssa
    n "Yeah, I have experience with female friends ditching me."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ab1099 with vpunch
    pause
    scene ab1083 with dssa
    ms "Malcom, what was that?"
    scene ab1100 with dssa
    j "Seriously? Malcom?"
    ms "Let me ask again: What was that??"
    scene ab1101 with dssa
    j "I just missed. I am a little bit out of practice, Coach."
    scene ab1085 with dssa
    ms "Bilbo, get going!"
    dam "*Mumbles* Man.."
    scene ab1098 with vpunch #soundeffect
    pause
    ms "Spaghetti, your turn."
    scene ab1036xx with vpunch
    with Pause(.6)
    ms "Good one."
    scene ab1095 with vpunch
    with Pause(.7)
    scene ab1096 with vpunch
    with Pause(.7)
    scene ab1097 with vpunch
    with Pause(.7)
    scene ab1084 with dssb
    ms "*sigh*."
    scene ab1085 with dssa
    mh "My plan is not going to work if we can't fill the key positions with suitable players!"
    scene ab1086 with dssa
    ms "It's not a plan, it's a suicide mission!"
    scene ab1087 with dssa
    mh "And that's the only way for us to get up there."
    mh "Cunt Glitter will do everything to prevent us from joining."
    mh "There is no other way."
    scene ab1088 with dssb
    mh "We have to beat or at least make the first team sweat for their lives in a scrimmage to get our foot in the door."
    mh "I talked to Miss Zane, and she gave me the green light. There is no going back now."
    mh "The second team is... fine... but we need better players."
    scene ab1089 with dssa
    ms "And how do we plan on doing that? Look what we got here!"
    mh "Don't be like that."
    scene ab1090 with dssa
    mh "Jeff, if he gets through the defense, is going to close the deal."
    scene ab1091 with dssa
    mh "Bilb-... Damian, they won't take him seriously. But I saw him run. Fast and agile. And... his reason to join the team is personal. It could prove very useful."
    scene ab1092 with dssa
    mh "Spaghetti... he knows how to make baskets. We got one for the free throws, three pointers and all or nothing plays."
    scene ab1093 with dssa
    mh "Juicebox... with the right training he will be able to slow down a guy built like Henry. He just needs to improve his jump."
    scene ab1094 with dssa
    mh "Sai, not a team player but he knows how to throw an unexpected counter and has incredible dribbling skills."
    scene ab1102 with dssb
    mh "And there are a lot of other freshmen this year. After the open tryouts we will have a functional second team."
    scene ab1103 with dssa
    ms "We need to train them outside school hours."
    scene ab1104 with dssb
    mh "Hehe, I bet they will like that."
    ms "Spaghetti, Bilbo, Gypsy, Malcolm, Juicebox."
    ms "Move your asses over here."
    scene ab1106 with dssa
    sai "What's with the shitty nicknames?"
    scene ab1107 with dssa
    ms "You got a problem with the way I handle the team?"
    scene ab1108 with dssa
    sai "...No."
    scene ab1109 with dssa
    mh "Every evening except on Sundays, you five will attend training outside official hours."
    scene ab1111 with dssa
    t "What?"
    scene ab1109 with dssa
    mh "We will train every day for the next two weeks."
    scene ab1112 with dssa
    j "Why? Don't we-"
    scene ab1109 with dssb
    mh "You all want to make it into the second team? And the chance to make the first team?"
    mh "Then make sure to be here at 8pm every day."
    scene ab1106 with dssa
    sai "I don't want to spend every evening here!"
    scene ab1110 with dssb
    mh "Then you are off the team."
    scene ab1106 with dssa
    sai "What? Hey, this is bullshit. You can't make us attend training outside official hours!"
    scene ab1110 with dssa
    mh "We are not forcing you to come."
    mh "But you also won't make it on to the team."
    scene ab1113 with dssa
    d "What is this really about?"
    scene ab1109 with dssa
    mh "Tomorrow evening, we will discuss what is necessary."
    mh "I expect you all to be there."
    scene ab1114 with dssa
    j "Of course, Coach."
    scene ab1116 with dssb
    mh "Alright ladies."
    mh "Zara, Nadia, Sai, Nancy and Robin, one team."
    mh "Juicebox, Spaghetti, Mila, Nia and Bilbo, the other team."
    scene ab1115 with dssa
    ms "The rest of you apes follow me to the outside yard."
    scene ab1117 with dssb
    n "Maaan- I hoped to play with you..."
    scene ab1118 with dssa
    d "We can play together some other time. Just the two of us."
    scene ab1119 with dssa
    n "Yes! I'd really like that."
    scene ab1120 with dssa
    mh "Every team has 5 minutes to come up with a strategy."
    scene ab1121 with dssa
    t "So what do we do?"
    scene ab1122 with dssa
    nia "We should go full offensive!"
    scene ab1124 with dssa
    mi "No, we should be defensive."
    scene ab1123 with dssa
    dam "Well they do have some pretty good players."
    scene ab1125 with dssa
    pause
    scene ab1126 with dssa
    t "Any idea?"
    scene ab1127 with dssa
    d "They have some high risk players."
    d "And we can't match their athletic ability."
    d "I'd say we pick out their weakest link and break it."
    scene ab1128 with dssa
    d "And that would be Zara and Nadia. Those two together are an explosive mixture."
    t "How do we break it?"
    d "Let's fuel the fire."
    scene ab1129 with vpunch
    d "*Louder voice* No, no, Trey... I think Nadia has a lot more to offer than Zara."
    t "*whisper* DUDE?"
    scene ab1130 with dssa
    zar "What did you just say?"
    na "Are you alright up there!?"
    d "But... now that you say it... I see what you mean."
    scene ab1131 with dssa
    zar "Fuck off you weirdo!"
    na "Yeah, shut up, [name]!"
    scene ab1132 with vpunch
    t "What are you doing?!"
    scene ab1133 with dssa
    d "I am winning."
    d "Stare at their asses."
    scene ab1134 with vpunch
    t "What? No- they will hate me!"
    d "Temporarily."
    $ persistent.unlockedImageNadia5 = True
    scene ab1135 with dssa
    pause
    scene ab1137 with dssb
    pause
    scene ab1138 with vpunch
    zar "You fucking creeps!"
    na "Disgusting!"
    scene ab1136 with dssb
    d "Except for you, Damian and me, we pretty much suck."
    scene ab1139 with dssa
    nia "Hey!"
    nia "I don't suck!"
    scene ab1140 with dssa
    d "You don't?"
    nia "Yes, I do- but I don't suck at sports."
    scene ab1141 with dssa
    d "That means you will be useful this game?"
    scene ab1142 with dssa
    nia "No."
    nia "I have a show tonight. I can't have any bruises."
    scene ab1142 with dssa
    d "Okay listen... Nia-"
    scene ab1146 with dssa
    nia "BUT- I will make an exception."
    nia "If you come by my place on Sunday, I will give everything I have."
    nia "Deal?"
    menu:
        "Deal.":
            $ NiaDeal = True
            scene ab1147 with vpunch
            nia "Great! - She screams out enthusiastically."
        "No deal.":
            scene ab1148 with dssa
            nia "As you wish."
            pause
    scene ab1149 with dssa
    d "I'll go point guard."
    t "I'll go small forward."
    scene ab1150 with dssa
    dam "Where should I go?"
    d "You should stay a little more offensive than defensive."
    d "I think it won't be easy to pass to you when you are blocked by someone."
    d "You need the ball before they reach you."
    scene ab1151 with dssa
    mi "And me?"
    d "If we are on offense, you stand in the corner or beneath the basket."
    d "On defense, just block Nancy."
    mi "Okay."
    if miladate or miladateF is True:
        $ MPhob = True
        scene ab1152 with dssa
        d "And don't be afraid of the ball, okay?"
        mi "I- can't."
        d "Why?"
        scene ab1153 with dssa
        mi "I- kinda blackout when something gets thrown or shot my way."
        mi "I am sorry."
        d "I see."
        scene ab1154 with dssa
        mi "I will still try my best."
        menu:
            "Be encouraging.":
                $ MilaEnc03x = True
                d "I know. - You say in a soft voice."
            "Leave it be.":
                pass
    else:
        pass
    scene ab1156 with dssa
    ms "Both captains come to the middle."
    scene ab1157 with dssa
    na "I am the captain!"
    scene ab1158 with dssa
    zar "Haha, no."
    scene ab1159 with dssa
    pause
    scene ab1160 with vpunch
    zar "I am!"
    scene ab1160 with vpunch
    na "I AM!"
    scene ab1161 with dssa
    nan "No, I am!"
    scene ab1162 with dssa
    pause
    scene ab1163 with dssa
    nan "*whisper* Sorry."
    scene ab1164 with dssb
    mh "Zara, you're the captain."
    scene ab1165 with dssb
    pause
    scene ab1166 with dssa
    pause
    d "Don't worry."
    scene ab1167 with dssb
    d "I'll take into account that you are a woman and will go easy on you."
    scene ab1168 with dssa
    zar "I will destroy you, you son of a bitch."
    scene ab1167 with dssa
    d "(A little more and those two will forget why they are even here.)"
    d "(Their only goal will be to destroy me, and we will win the game.)"
    scene ab1170 with vpunch
    "Suddenly, Mila drags you away from the middle."
    scene ab1169 with dssa
    mi "Umm- did you really just say that?"
    d "Mh?"
    mi "That thing about her being a woman?"
    scene ab1170 with dssa
    d "Oh, don't take it the wrong way. I am winning us the game."
    d "It's just to put them off their game. I do not really think that."
    scene ab1171 with dssa
    mi "You shouldn't say that so loud... others might get the wrong impression."
    stop music fadeout 3.0
    "You nod."
    scene ab1172 with dssa
    $ play_playlist(playlist_RockPop)
    mh "I want to see a fair game."
    $ persistent.unlockedImageS4 = True
    scene ab1173 with vpunch
    "You and Zara both jump up-"
    scene ab1174 with dssa
    "But Zara jumps much higher."
    scene ab1175 with dssa
    "But was too eager and flips the ball towards your team mate, Damian."
    scene ab1176 with vpunch
    "Zara immediately goes into close body contact."
    scene ab1177 with dssa
    "Nadia makes her way towards Damian and he passes to Nia."
    scene ab1178 with vpunch
    "Nadia suddenly sprints after the ball-"
    $ persistent.unlockedImageNadia3 = True
    $ persistent.unlockedImageNadia4 = True
    if NiaDeal is True:
        $ HillImpressed = True
        $ NiaSynergy = True
        scene ab1179 with vpunch
        "Nia jumps forward and catches the ball."
        scene ab1180 with vpunch
        "She feints a pass and is able to leave Sai behind her-"
        scene ab1181 with dssa
        "-Nia makes a sharp turn and throws the ball over Zara towards you-"
        scene ab1182 with dssb
        pause
        scene ab1183 with dssa
        "- giving you a perfect opening for a long shot."
        scene ab1184 with dssa
        "You enter a deep moment of focus."
        scene ab1185 with dssa
        "You shoot the ball across the field-"
        scene ab1186 with vpunch
        "And you beautifully hit a half court shot."
        scene ab1187 with dssa
        mh "That was impressive!"
        mh "Good one, Spaghetti!"
        scene ab1188 with dssb
        nia "Good job!"
        d "You too."
    else:
        $ MStahlSaiTalk03x = True
        scene ab1189 with vpunch
        "Nia misses the ball by an inch and Nadia swoops in-."
        scene ab1190 with dssa
        "She passes to Sai-"
        scene ab1191 with dssa
        "- who outruns Damian."
        scene ab1192 with dssa
        "Nadia runs into a perfect opening."
        scene ab1193 with dssa
        na "Pass!"
        scene ab1191 with dssa
        "But instead of passing Sai tries to go for it-"
        scene ab1194 with dssa
        "And gets intercepted by Trey."
        mh "Sai! Get your head out of your ass! This is a team game!"
    scene ab1195 with dssb
    n "So unfair..."
    n "I want to play with them!"
    scene ab1196 with dssa
    so "I don't think I can play that."
    scene ab1197 with dssa
    n "What do you mean?"
    scene ab1198 with dssa
    so "Moving so fast and agile."
    scene ab1197 with dssa
    n "You just need training."
    scene ab1198 with dssa
    so "Shouldn't we go outside?"
    scene ab1195 with dssa
    n "In a second."
    scene ab1199 with vpunch
    sas "Nami?"
    n "Uh yes?"
    scene ab1200 with dssb
    sas "Can I ask you something."
    scene ab1201 with vpunch
    ay "YO!"
    ay "How are you?"
    scene ab1202 with dssa
    sas "I was decent until some ape disturbed my balance."
    scene ab1203 with dssa
    ay "Careful with your words or I'll repeat the beating you got in our last session."
    scene ab1202 with dssa
    sas "Get off."
    scene ab1204 with dssa
    ay "Hey Nami! You look great!"
    ay "And so do you Sonya."
    scene ab1209 with dssa
    so "Th-anks."
    scene ab1208 with dssa
    n "You seem happy all of a sudden?"
    scene ab1205 with dssa
    ay "Yes! I have no idea why."
    ay "Sometimes, I get all excited and can't wait to get out into the world!"
    scene ab1206 with dssa
    ay "And girl... those 'uniforms'. Look at this! Half my boob is out."
    n "Yes, Miss Hill is already asking for a new design."
    scene ab1205 with dssa
    ay "Haha... yeah. Good luck getting through Katie Zane."
    scene ab1208 with dssa
    n "Who?"
    ay "My aunt, Katie Zane. The lead designer of ZPR?"
    scene ab1209 with dssa
    so "I guess that means there isn't much chance they'll change?"
    scene ab1210 with dssa
    ay "Not really, no."
    scene ab1211 with dssa
    ay "And didn't the first team vote for this anyways?"
    ay "It's pretty much their fault."
    scene ab1213 with vpunch
    "Nadia passes back to Zara."
    scene ab1214 with dssa
    "They outplay Nia- and make their move towards the hoop."
    scene ab1215 with dssa
    pause
    scene ab1216 with dssa
    "You notice Zara moving into your direction with the intent to run behind you."
    scene ab1217 with dssa
    d "(Nadia will most likely pass back to her- it's a risky move but I will pretend that I didn't see her and try to intercept the ball out of the blue.)"
    scene ab1219 with vpunch
    "As expected, Nadia falls for it and passes to Zara-"
    scene ab1218 with dssa
    "In the blink of an eye you turn around and intercept the ball with your fingertips."
    scene ab1220 with dssa
    "You pretend to make a fast step forward-"
    scene ab1221 with vpunch
    "-but you take a step back instead, and an angry flying Zara misses you."
    scene ab1222 with dssa
    "You give her a smile."
    scene ab1223 with dssa
    "Which enrages her even more."
    d "(She has reached her limit and should be easy to beat now.)"
    scene ab1224 with dssa
    "You pass to Trey-"
    scene ab1225 with dssa
    "Who passes to Damian-"
    scene ab1226 with dssa
    "Who does a steep pass into Nia."
    scene ab1227 with dssa
    "Nia goes for it..."
    scene ab1228 with vpunch
    "And scores!"
    scene ab1229 with dssa
    mh "Very, very good!"
    scene ab1230 with dssa
    mh "Mila? I get you don't really have an interest in Basketball?"
    scene ab1232 with dssa
    mi "No, not at all."
    mh "Alright, get out-"
    scene ab1231 with dssa
    mh "Nami! Get in!"
    scene ab1212 with vpunch
    n "YES!"
    if miladate or miladateF is True:
        scene ab1233 with dssb
        "Mila leaves the court with a long face."
        scene ab1234 with dssa
        d "Hey- don't be discouraged. You did well... for a mannequin."
        scene ab1235 with dssa
        "She chuckles a little."
        scene ab1236 with dssa
        d "Don't be so hard on yourself. It's just not your cup of tea."
        scene ab1237 with dssa
        "Mila is positively surprised by your sudden act of kindness."
    scene ab1239 with dssb
    n "Yo!"
    d "Time to beat em."
    scene ab1240 with vpunch
    play sound "music/SFX/Slap.mp3"
    pause
    scene ab1241 with dssa
    nia "NAMI!"
    scene ab1242 with dssa
    n "NIA! Finally we are all in the same damn team!"
    scene ab1243 with dssa
    n "Man, Zara seems pissed at you."
    d "It's the reason we're winning."
    scene ab1244 with dssa
    n "And with me you sealed the deal!"
    scene ab1245 with vpunch
    "Zara passes back to Sai, who observes the situation for a moment-"
    scene ab1246 with dssa
    "-and passes to Robin."
    scene ab1247 with dssa
    "Robin seems clueless but decides to pass to Nadia who leaves Nia behind her."
    "Nami goes into attack mode and tries to block Nadia-"
    scene ab1248 with dssa
    "- who is forced to pass back to Robin."
    scene ab1249 with vpunch
    "You grab Damian-"
    d "Run past me!"
    scene ab1250 with dssa
    "Damian immediately follows up-"
    scene ab1251 with dssa
    "-and Robin makes the mistake of completely missing Damian and passing to Zara."
    scene ab1252 with vpunch
    "Mid air, Damian intercepts the ball and passes to Nia."
    scene ab1253 with dssa
    "Nia hastly looks around and-"
    scene ab1254 with dssa
    "-does pass back to you-"
    scene ab1255 with dssa
    "But Zara was already on her way towards you, predicting Nia's pass-"
    scene ab1256 with dssa
    "You manage to guide the ball towards Nami-"
    "-But Zara crashes into you, causing you to lose balance."
    scene ab1257 with dssa
    d "(You're going down with me!)"
    "As you try to grab Zara- all you manage to grab is her top strap-"
    play music "music/Suspense/Scott Buckley - Resonance.ogg"
    scene ab1258 with vpunch
    "- ripping it apart."
    scene ab1259 with vpunch
    "Zara redirects her fall right on top of you in order to hide her now revealed breast. Her sweaty and soft boob is pushed into the side of your face as you hit the ground."
    scene ab1260 with dssb
    za "What the fuck dude?!"
    scene ab1261 with dssa
    "You try to push her off- but Zara holds you down in order to use you as a cover."
    scene ab1262 with dssa
    $ persistent.unlockedImageZara2 = True
    "Meanwhile, Nia, Nami, and Damian managed to score again."
    "Giving you the win as Coach Hill notices the accident that occurred."
    $ persistent.unlockedImageMusicDTTS = True
    # show screen tooltip_DTTS with blinds
    pause
    # hide screen tooltip_DTTS with blinds
    scene ab1263 with dssa
    mh "Good job team."
    mh "I am glad to see that there are some first chemistries forming for when we have to play some actual 20 minute halves."
    mh "Keep in mind, this is all to prepare you for the open tryouts."
    scene ab1265 with vpunch
    zar "*shaky voice* This piece of shit ripped my top apart!"
    scene ab1266 with dssa
    mh "There was no reason for you to go in like that in the first place. You obviously planned on crashing into him, and you paid for it."
    scene ab1267 with dssb
    mh "May I talk to you two in the changing room?"
    scene ab1268 with dssb
    t "It worked out."
    scene ab1269 with dssb
    pause
    scene ab1270 with dssa
    t "But damn- they are so pissed at us... well, at you."
    t "I don't know if that was worth it."
    scene ab1271 with dssa
    d "It was."
    d "Those two are highly competitive people. They are going to want revenge by beating us... or me."
    d "And... if they really have an interest in getting better, they won't see what I did as bad- they might even be impressed."
    scene ab1272 with dssa
    t "Did you rip her top on purpose?"
    d "No, it was an accident."
    scene ab1273 with dssb
    dam "Good job, dudes."
    scene ab1274 with dssa
    d "You did well, too. Thanks for following my words earlier."
    d "I suspected Robin would primarily focus on me and that's why I had to stay passive."
    scene ab1273 with dssa
    dam "Worked out great."
    scene ab1275 with dssb
    n "I love winning! Even though I didn't get to play much..."
    scene ab1276 with dssb
    n "We should be teamed up more often."
    scene ab1277 with dssa
    d "I agree."
    d "You and I have good chemistry."
    scene ab1278 with dssa
    if namigym is True:
        nia "I told you guys that at the gym!"
    if NiaDeal is True:
        scene ab1280 with dssa
        d "Ours isn't bad either."
        nia "Indeed! - Nia says nervously."
    scene ab1279 with dssa
    nia "But the tryouts won't be unisex."
    n "Damn..."
    nia "We can also arrange some fun tournaments."
    if NiaDeal is True:
        scene ab1281 with vpunch
        $ persistent.unlockedImageNia4 = True
        "To everyone's surprise, you put your arm around Nia and drag her a little closer."
        d "Thanks for putting the work in."
        scene ab1282 with dssa
        nia "I gave you my word."
        nia "Will you honor yours?"
        d "Yes."
        scene ab1283 with dssa
        nia "Sunday? You can come over if you want."
        d "I'll be there."
        "Nia smiles."
        scene ab1284 with dssa
    else:
        scene ab1285 with dssa
    stop music fadeout 3.5
    "You three make your way to the locker rooms."
    scene ab1286 with dssb
    az "What do you think?"
    scene ab1287 with dssb
    dwi "Mhh? - he moans."
    az "Did you even listen?"
    scene ab1289 with dssb
    dwi "I'm still drunk... and colorblind."
    scene ab1290 with dssa
    dex "I can see colors again... but my eyes are still super sensitive to light."
    scene ab1291 with dssa
    jaz "I made some notes about the boys and girls down there."
    scene ab1292 with dssa
    az "Henry and the others are on the outside court, right?"
    scene ab1289 with dssa
    dwi "Yeah, too many freshmen this year."
    scene ab1293 with dssa
    jak "Where is our other half?"
    scene ab1294 with dssa
    jaz "The girls are still at the resort. They managed to persuade the dean to give them another two days."
    jaz "They asked me to give them a quick overview of the new girls and their potential."
    scene ab1293 with dssa
    jak "How did they get the extra two days? Nude pics?"
    scene ab1291 with dssb
    jaz "Most likely."
    scene ab1295 with dssa
    dwi "The last time I sent the dean a nude I got suspended for a week."
    scene ab1297 with dssa
    dwi "Larry didn't you take the pic of me? The one with the bow around my schlong?"
    lar "Yeh, haha."
    scene black with Dissolve(2)
    with Pause(.5)

label End03x5:
    scene ab1298 with dssb
    d "We need to concentrate on the tryouts."
    t "That won't be easy."
    scene ab1299 with dssa
    d "If it was easy, there would be no fun to it."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ab1300 with vpunch
    play music "music/Vesky - Aurora.ogg"
    rob "[name], something is wrong with Nami!"
    scene ab1302 with dssa
    d "Wh-at? What's wrong with her?"
    scene ab1301 with dssb
    rob "I- think a heat stroke or some sort-"
    rob "She is in the girl's changing room!"
    scene ab1303 with vpunch
    "In your rush, you push Robin out of your way."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ab1304 with dssb
    d "Nami-.. *sigh*."
    scene ab1305 with dssb
    "You let out a small laugh."
    scene ab1306 with dssa
    play music "music/Suspense/Scott Buckley - Nightfall.ogg"
    d "Actions have consequences."
    scene ab1307 with vpunch
    "Zara and Nadia burst out of the shadows and handcuff your left arm."
    scene ab1308 with dssa
    "She locks the other half into one of the towel holder metal rings on the wall."
    scene ab1309 with dssb
    "You don't even bother to react."
    scene ab1310 with dssa
    na "*sensual whisper* Indeed they do..."
    scene ab1312 with dssb
    zar "I am not gonna lie, [name]... I am impressed and ashamed that you managed to play us that easily."
    scene ab1313 with dssb
    na "We really need to get this hate out of our system."
    scene ab1314 with dssa
    d "I understand. (I'll let them do it. It's a small price to pay for a win and a few relationship points.)"
    scene ab1315 with dssa
    if RoRum is True:
        rob "I am so sorry, [name]..."
    else:
        rob "I'm sorry, [name]..."
    d "It's okay."
    scene ab1316 with dssa
    na "You can go now Robin and you don't owe me anymore."
    if RoRum is True:
        scene ab1319 with dssa
        za "Unless you want to do something else with him here... while he is all tied up."
        scene ab1317 with vpunch
        rob "You don't really believe that, do you?!"
        scene ab1320 with dssa
        za "Robin. I was joking... Sorry."
    scene ab1318 with dssa
    pause
    zar "Do you know what we're going to do with you?"
    scene ab1321 with dssa
    d "Only one way to find out."
    "You stare at them."
    scene ab1322 with dssa
    zar "Get naked."
    "You still just stare at them."
    scene ab1323 with dssb
    na "*Whisper* Completely or should we let him leave his boxers on?"
    scene ab1324 with dssa
    zar "*Whisper* I think we should leave him in his boxers... I don't want to get sued."
    scene ab1325 with dssa
    na "[name], make it easy and strip down to your boxers."
    d "That's like asking a victim to rob himself."
    scene ab1326 with dssa
    "They both share a look."
    na "*sigh*"
    scene ab1327 with dssa
    pause
    scene ab1329 with dssa
    pause
    scene ab1328 with dssa
    pause
    scene ab1330 with dssa
    "They both nod repeatedly."
    $ persistent.unlockedImageNadia5 = True
    scene ab1331 with dssa
    na "Yup, that's it. Have a good night."
    scene ab1332 with dssa
    "You say nothing and stare in front of you."
    scene ab1333 with dssb
    pause
    scene ab1335 with dssa
    "You hear one of Zara's high heels drop to the floor."
    scene ab1334 with dssb
    za "If you ever try to play me like that again-"
    scene ab1336 with dssa
    za "I'll make you eat them."
    scene ab1337 with dssa
    $ persistent.unlockedImageS5 = True
    na "The girls from the other classes should find you in the evening..."
    na "If not we'll get you tomorrow... and if you somehow manage to free yourself... You're happily invited to our meet up in the afternoon."
    scene ab1338 with dssa
    pause
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    jump Chapter4alt
