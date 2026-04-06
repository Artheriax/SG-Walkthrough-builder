label StartChapter5:
    $ achievement.grant("Chapter4x5Finished")
    $ achievement.sync()
    if BellaKiss3x5 is False:
        jump NamiIntro5x0
    else:
        pass
    hide screen phone_hotspot
    hide screen music_player_trigger
    scene BelIntro5 with dssb
    $ renpy.pause(4.5, hard=True)
    with Pause(87.5)
    $ play_playlist(playlist_AmbientBellchen)
    $ BellaDesert5x0 = True
    show screen music_player_trigger
    scene sa1 with dssb
    pause
    scene sa2 with dssa
    pause
    scene sa3 with dssa
    $ persistent.unlockedImageCh5_C_1 = True
    $ persistent.unlockedImageBellaCh5_1 = True
    "No words have been exchanged for the past 20 minutes. The only sound you hear is a distant airplane and how the wind tickles the grass."
    scene sa4 with dssr
    d "...I have no idea how we got here."
    d "It's all just... a blur of lights."
    #blur bibi sfx
    b "I drove without any goal in mind... I just stopped when I felt like we arrived at the right spot..."
    scene sa5 with dssb
    pause
    scene sa6 with dssr
    d "I must say... I was, and I'm still very surprised to see you."
    scene sa7 with dssa
    "She lets out a long sigh."
    scene sa8 with dssr
    b "I don't know what I'm doing anymore..."
    b "One day I feel like ripping your head off... The next day- well, the same... but with a little more care."
    scene sa9 with dssr
    b "There's no real reason why I'd think about you at all."
    b "I'm superior in every single way."
    scene sa10 with dssr
    "She climbs out of the car."
    scene sa11 with dssr
    pause
    scene sa12 with dssr
    pause
    scene sa13 with dssa
    pause
    scene sa14 with dssa
    pause
    scene sa15 with dssr
    pause
    scene sa16 with dssr
    d "I never thought I'd say this but... I kinda missed this stupid talk of yours."
    scene sa18 with dssb
    d "Where's the cancer car?"
    scene sa17 with dssa
    b "At home."
    b "I borrowed a friends car... I thought a convertible would fit this occassion more."
    scene sa19 with dssr
    d "It did."
    scene sa20 with dssa
    b "There's something so soothing about driving with the top down in the early morning hours."
    scene sa21 with dssr
    b "T-thank you for being here with me..."
    scene sa22 with dssr
    d "Did you just stutter?"
    scene sa23 with vpunch
    b "I DIDN'T STUTTER!"
    scene sa24 with dssr
    d "Little bibi started stuttering, ooohhh."
    scene sa25 with dssa
    b "What's a bibi?"
    d "It's a word for something baby like."
    scene sa26 with dssa
    b "You-"
    scene sa27 with vpunch
    d "Shut up for a second."
    scene sa28 with dssa
    d "I'm really glad you came by."
    scene sa29 with dssa
    pause
    scene sa30 with dssb
    if NamiLove4x5 is True:
        $ McPa +=2
        pause
        scene sa34 with vpunch
        d "(I kissed the Cheeto!)"
        "You feel your heart rate ramping up."
        scene sa35 with dssa
        d "(Not now! Not in front of Bella!)"
    else:
        d "(For the first time in a very long time... I feel warm... I feel like I arrived somewhere...)"
        scene sa31 with dssa
        d "(I haven't felt butterflies in my stomach in a very long time.)"
        scene sa32 with dssa
        d "(I can feel the way her body moves... She's aroused... I promise you, that someday I'll give you what you want...)"
        scene sa33 with dssa
        d "(I'll do anything to achieve it.)"
    scene sa36 with dssr
    pause
    d "Do you have something to drink in that car?"
    scene sa37 with dssr
    b "Not in this one."
    d "I'm really thirsty."
    scene sa39 with dssa
    pause
    scene sa40 with dssr
    pause
    scene sa41 with dssr
    pause
    scene sa42 with dssa
    pause
    scene sa43 with dssa
    pause
    scene sa44 with dssa
    "You swing her around and kiss her... passionately."
    scene sa45 with dssa
    d "(It feels amazing to kiss her... I actually feel something in my belly.)"
    scene sa46 with dssa
    if MilaKiss4x5 is True:
        d "(Mila's kiss was nice, but this is on another level.)"
    elif VictoriaKiss4x5 is True:
        d "(Kissing Victoria was nice... But this is just a different experience.)"
    scene sa48 with dssa
    pause
    scene sa49a with dssr
    b "Oof- you kissed me dizzy."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Crossroads)
    scene sa50 with Dissolve(2)
    pause
    scene sa51 with dssr
    d "What now?"
    b "Mh?"
    d "We keep doing stuff like this... Just to revert back a day later."
    scene sa50 with dssa
    b "Are you proposing a relationship?"
    d "We don't need to go that far-"
    b "Well, dude... There's not much in between."
    scene sa52 with dssa
    b "But... I also don't want a relationship... Like a serious one with a dude I have only known for a short period of time during my freshman year of college..."
    scene sa53 with dssa
    pause
    scene sa54 with dssa
    b "I really like you..."
    scene sa55 with dssr
    b "The thing is... There's no room for errors."
    scene sa56 with dssa
    b "If trust gets broken once... That's pretty much it... I can't forgive."
    scene sa57 with dssa
    d "Everyone can learn to forgive... But I agree."
    d "If trust gets broken between us... That's it."
    scene sa58 with dssr
    pause
    scene sa59 with dssa
    b "My recommendation?"
    scene sa60 with dssa
    d "Cheese fries?"
    scene sa61 with dssa
    b "Oh, fuck yeah!"
    scene sa62 with dssr
    pause
    scene sa63 with dssa
    b "But... seriously... let's just leave it like this... for now."
    scene sa64 with dssa
    pause
    menu:
        "I'm not saying we need to fly straight into a relationship... But we can start walking.":
            scene sa65 with dssr
            pause
            $ BellaNonExclusive5x0 = True
            scene sa66 with dssa
            b "I'm so afraid of fucking this up..."
            scene sa67 with dssa
            d "You most certainly will."
            scene sa68 with dssa
            pause
            d "It's just important that we communicate... and we can both head out of this at any time."
            scene sa69 with dssa
            b "That's the issue."
            b "What if one of us gets so attached and the other draws back all of a sudden?"
            b "Bonus points if it ends with ghosting."
            scene sa67 with dssa
            d "That's a risk we'd have to take."
            scene sa71 with dssa
            d "We just have to be open with each other."
            scene sa72 with dssa
            b "It's too risky... I don't want to be vulnerable... But I also don't want to stop seeing you."
            b "My offer is that we both date, but without any commitment to each other... I don't want to settle down in the first week, with the first guy that crossed my path."
            b "Especially not with a wildcard like you."
            scene sa73 with dssa
            b "*Whispers* I'm ready to keep exploring us. But no strings attached."
            scene sa74 with dssa
            pause
            if MilaKiss4x5 is True:
                menu:
                    "Tell her that you and Mila kissed.":
                        $ BTY2 = True
                        $ BellaMilaKiss5x0 = True
                        scene sa75 with dssa
                        d "To put all cards on the table... I think you should know that Mila and I kissed at Victoria's."
                        scene sa76 with dssa
                        b "...Did it mean anything to you?"
                        scene sa77 with dssa
                        d "You know me... I don't just kiss people."
                        scene sa78 with dssa
                        pause
                        scene sa79 with dssa
                        b "...I appreciate your honesty."
                        scene sa80 with dssa
                        b "And it really disgusts me... But we weren't exclusive."
                        scene sa81 with dssa
                        d "Correct."
                        scene sa84 with dssa
                        pause
                        scene sa85 with vpunch
                        "Bella hysterically jumps backwards."
                        scene sa86 with dssa
                        b "EWWW! You didn't shower from when you were there!"
                        b "There was probably still some poor people juice left on your lips! UGH!"
                        scene sa87 with dssa
                        d "...Fucking idiot."
                        scene sa88 with dssa
                        b "I can feel my future perspective fading! My bank account's being drained!"
                        scene sa89 with dssa
                        d "You know... Good call by not attaching any strings."
                    "Don't tell her.":
                        $ BDMK5x0 = True
                        pass
            elif VictoriaKiss4x5 is True:
                menu:
                    "Tell her that you and Victoria kissed.":
                        $ BellaVictoriaKiss5x0 = True
                        $ BTY2 = True
                        scene sa82 with dssr
                        b "Oh, I wouldn't say I'm surprised..."
                        b "Thank you for being honest with me."
                        scene sa83 with dssa
                        b "But this is what I'm talking about... The second we attach strings, the vulnerability becomes unbearable."
                    "Don't tell her.":
                        pass
            else:
                pass
        "No, I can't do it like this... Let's put 'us' on ice.":
            scene sa65 with dssr
            $ BellaOnIce5x0 = True
            $ BellaNoDating5x0 = True
            pause #schaut dich an
            "She stares into the sunrise."
            if bellathreat is False and bellasummer is True:
                scene sa66 with dssa
                b "I don't want that..."
                scene sa65 with dssr
                d "I need to know where I'm at."
                b "I can't tell you where we are..."
                d "And until we find out where we are... I don't want to continue like this."
                b "Okay."
            else:
                scene sa66 with dssa
                b "Okay."
                b "It's the right decision... We would never have worked out."
                scene sa65 with dssa
                d "I think we would... But timing can be a bitch."
            scene sa66 with dssa
            b "*sigh*"
            b "Will we still hang out?"
            scene sa67 with dssa
            d "Why?"
            scene sa69 with dssa
            b "Then not!"
            scene sa81 with dssr
            d "No seriously, I mean why? All we do is insult each other... then kiss."
            scene sa91 with dssa
            b "We can just- you know... keep insulting each other without the kissing?"
            scene sa90 with dssa
            d "I guess we can do that."
            scene sa92 with dssa
            b "The sad part is... Now you'll die a virgin."
            d "I doubt that."
            b "And we still have to go through with our plan against the Holgerson's."
            d "We need to come up with something new."
    scene black with Dissolve(2)
    with Pause(.5)
    if BellaNonExclusive5x0 is True:
        scene sa93 with dssb
        pause
        scene sa95 with dssa
        pause
        scene sa96 with dssa
        "Bella breathes quickly as you disconnect the kiss."
        d "We've gotta go... I'm really, really tired..."
        scene sa97 with dssa
        b "Same."
        b "Alright, let's go."
        scene sa98 with dssr
        "She locks her legs around you, hugs you tight, and pushes her face into your shoulder."
        b "Carry me."
        d "I have no idea where the next garbage dump is."
        scene sa94 with dssr
        b "*Whispers* It's your place."
        $ persistent.unlockedImageBellaCh5_2 = True
        d "I will bury your dead body somewhere in this wasteland."
    else:
        scene sa99 with dssb
        d "Let's head back. I desperately need some sleep."
        scene sa100 with dssa
        b "Alright."
        scene sa101 with dssr
        b "I've gotta stop for gas, though."
        scene sa102 with dssa
        pause
    $ persistent.unlockedImageR_CH5_1 = True
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ achievement.grant("ANightInTheDesert")
    $ achievement.sync()
    jump Gasstop5x0

label NamiIntro5x0:
    $ persistent.unlockedImageCh5_C_2 = True
    hide screen music_player_trigger
    scene CH5Intro with dissolve
    $ renpy.pause(4.5, hard=True)
    with Pause(35)
    $ play_playlist(playlist_Ch5_Sad_Cheeto)
    $ CheetoIntro5x0 = True
    show screen music_player_trigger
    $ persistent.unlockedImageNami_CH2_5 = True
    scene sb1609 with dssb
    pause
    scene sb1610 with dssr
    pause
    scene sb1611 with dssr
    d "For how long do you want to stay there?"
    scene sb1612 with dssr
    pause
    scene sb1613 with dssr
    pause
    scene sb1614 with dssa
    n "...You got one for me?"
    scene sb1615 with dssa
    pause
    scene sb1616 with dssa
    pause
    scene sb1617 with dssa
    pause
    scene sb1618 with vpunch
    "She flips away the cigarette bud."
    scene sb1619 with dssa
    pause
    scene sb1620 with dssa
    if NamiLove4x5 is True:
        n "...I think we're both here because..."
        scene sb1622 with dssr
        pause
        scene sb1621 with dssa
        d "Yeah."
        scene sb1622 with dssa
    else:
        n "May I ask what are you doing here?"
        scene sb1621 with dssr
        d "I needed some air..."
        scene sb1622 with dssa
    d "I couldn't sleep and I got this lingering feeling of dread..."
    d "As if something bad is about to happen."
    scene sb1623 with dssa
    n "I can relate..."
    scene sa286 with dssb
    pause
    if NamiLove4x5 is True:
        d "Do you want to talk about what happened?"
        scene sa288 with dssr
        pause
        scene sa289 with dssa
        n "Not really."
        scene sa295 with dssa
        d "Well, I do."
        scene sa296 with dssa
        n "Why did you do it?"
        scene sa298 with dssa
        d "Do what?"
        scene sa299 with dssr
        n "Kiss me."
        d "I don't know? It felt right."
        n "I wouldn't have seen that coming in a million years."
        scene sa300 with dssr
        pause
        scene sa301 with dssa
        n "I can't even look at you."
        scene sa302 with dssr
        n "I thought I... I don't know what happened."
        scene sa366 with dssa
        d "Stuff got real when I took initiative."
        d "And it scares the shit out of you."
        scene sa367 with dssa
        n "...It does."
        scene sa368 with dssa
        n "It was all fun and games... but now... I feel like we crossed a big, blinking, red line."
        scene sa369 with dssa
        d "We can always return."
        d "As long as you get your head out of your ass."
        $ play_playlist(playlist_Chapter1a)
        scene sa370 with vpunch
        d "Listen..."
        scene sa371 with dssa
        d "What I did was nothing compared to what you've been doing to me... It's just the fact that I did it, which creeps you out."
        if BellaKiss3x5 is True:
            d "You say Bella leaves me in the dark?"
            d "You do it a thousand times worse."
            d "I don't know what you feel for me."
            d "If it's all just a game... Or if you're actually in love with me."
            d "Our past doesn't make it any easier."
            scene sa372 with dssa
            pause
            d "The fact that you now pull back all of a sudden... It reminds of that time."
        else:
            d "I don't know what you feel for me."
            d "If it's all just a game... Or if you're actually in love with me."
            scene sa372 with dssa
            d "Our past doesn't make it any easier."
        scene sa373 with dssa
        n "I-"
        $ persistent.unlockedImageST_CH5_1 = True
        scene sa374 with vpunch
        d "And if I get the feeling that you're playing me... I'll never talk to you again."
        d "You'll become a ghost."
        $ persistent.unlockedImageNami_CH2_6 = True
        scene sa375 with vpunch
        n "I'm not playing anything!"
        d "I know how you are deep inside, Cheeto..."
        d "I'm certain you've changed but... there lies something within you most people would never see coming."
        scene sa376 with vpunch
        n "I'm not playing you! Or anyone else."
        n "I don't do that anymore!"
        scene sa377 with dssa
        d "I believe you."
        d "But I need you to be honest with me."
        scene sa378 with dssa
        pause
        scene sa379 with dssa
        d "What do you feel for me?"
        scene sa380 with dssa
        n "I- I don't know..."
        scene sa381 with dssr
        n "It all became so real when we kissed last night..."
        scene sa382 with dssr
        pause
        scene sa383 with dssa
        n "I just need time to think."
        pause
        menu:
            "You mean so much to me...":
                $ NamiLove5x0 = True
                scene sa385 with dssa
                d "You mean so much to me."
                d "But think about your next step very carefully."
            "Don't say it.":
                pass
    else:
        scene sa299 with dssa
        n "...You should really get some sleep."
        d "So should you."
        scene sa299 with dssa
        n "Yeah... I don't want to ruin my sleep rhythm again."
        scene sa381 with dssr
        n "Just... tell me if something's bothering you..."
        scene sa385 with dssr
        d "I will."
    if NiaDeal is True:
        jump Nia5x0
    else:
        jump CheetoHome5x0

label Gasstop5x0:
    $ play_playlist(playlist_Ch5_Gas)
    scene sa103 with dssb
    pause
    scene sa104 with dssr
    pause
    scene sa105 with dssr
    pause
    scene sa106 with dssa
    pause
    scene sa107 with dssa
    pause
    scene sa108 with dssr
    pause
    scene sa109 with dssa
    b "I'm gonna go pay... Need anything?"
    scene sa110 with dssa
    d "Just some water."
    scene sa111 with dssa
    pause
    scene sa112 with dssb
    "A bunch of loud motorcycles slowly drive into the station."
    scene sa113 with dssa
    pause
    scene sa114 with dssr
    pause
    scene sa115 with dssa
    pause
    scene sa116 with dssa
    u "Like what you see?"
    scene sa118 with dssr
    "You walk closer."
    scene sa117 with dssr
    "You wrap your hand around the leather handle... You feel how the weather and years have eaten away on it..."
    scene sa119 with dssr
    d "I'm not sure."
    scene sa120 with dssr
    u "That convertible is quite nice... It offers you a taste of freedom."
    scene sa121 with dssa
    u "But this..."
    u "This is the full dose."
    scene sa122 with dssa
    d "Maybe someday."
    scene sa123 with dssa
    pause
    d "Safe ride."
    u "See you on the street."
    if BellaNonExclusive5x0 is True:
        scene sa124 with dssr
        b "You're not getting a motorcycle."
        scene sa125 with dssr
        d "What if I do?"
        scene sa124 with dssr
        b "I will continue to withhold sex."
        scene sa126 with dssr
        d "Thanks for the water."
        scene sa127 with dssa
        pause
        scene sa128 with dssa
        pause
        scene sa129 with dssr
        d "And by the way, you withholding sex sounds like a win-win."
        scene sa130 with dssa
        b "You sound like a virgin."
        scene sa129 with dssa
        d "You put way too much emphasis on this virgin topic."
        d "Can't you come to terms with the fact that you're a bitch?"
        scene sa131 with dssa
        b "Oh please, calling you a virgin with a dead pocket rocket is what brings me happiness."
        scene sa132 with dssr
        d "Seeing you dead on the street would bring me happiness."
        scene sa133 with dssa
        b "I'm too good of a driver for that to happen."
        scene sa134 with dssa
        d "Famous last words."
    else:
        scene sa126 with dssr
        d "Thanks for the water."
        scene sa132 with dssr
        d "Alright, take me home."
    stop music fadeout 4.0
    scene sa134x with dssb
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_AmbientBellchen)
    scene sa135 with Dissolve(3)
    pause
    scene sa136 with dssr
    b "Here we are... But I should've called them... I don't know if they still have capacity."
    scene sa137 with dssa
    "You give her a clueless look."
    scene sa138 with dssa
    b "The homeless shelter here... You-"
    scene sa139 with dssa
    d "I'm gonna fucking smack you someday."
    scene sa140 with dssa
    b "You know... Calling you a virgin doesn't affect you... But for some reason that makes you furious."
    scene sa141 with dssa
    d "Because you're not just insulting me... But Nojiko who's been working her ass off."
    scene sa142 with dssa
    pause
    scene sa144 with dssa
    pause
    if BellaOnIce5x0 is True:
        scene sa148 with dssr
        pause
        scene sa149 with dssa
        pause
        scene sa150 with dssa
        "You look at her."
        scene sa144 with dssr
        d "Goodbye."
        scene sa143 with dssa
        b "...Bye."
        hide screen phone_hotspot
        hide screen music_player_trigger
        stop music fadeout 2.0
        scene black with Dissolve(2)
        with Pause(.5)
        jump NamiIntro5x0
    else:
        scene sa148 with dssr
        pause
        scene sa149 with dssr
        pause
        scene sa150 with dssa
        pause
        scene sa144 with dssr
        pause
        scene sa145 with dssa
        d "Do you want to come inside for a coffee?"
        scene sa146 with dssa
        b "Asking a girl inside for a 'coffee' can only mean one thing..."
        d "We're going to fuck hard."
        scene sa147 with vpunch
        b "That's what I want to hear!"
        scene black with Dissolve(2)
        with Pause(.5)
        jump HomeBella5x0

label HomeBella5x0:
    scene sa151 with dssb
    pause
    scene sa152 with dssr
    d "Hey."
    if NamiLove4x5 is True:
        scene sa153 with dssa
        m "Hey! Where were you two?"
        scene sa154 with dssr
        "Nojiko seemed to expect Nami and looks quite surprised at seeing Bella."
        m "Oh hi!"
        scene sa155 with dssa
        b "Hello."
        scene sa157 with dssa
        m "Where's Nami?"
        scene sa158 with dssa
        d "She's not here?"
        m "No."
        scene sa159 with dssa
        d "My phone's run out of battery. I'll plug it in real fast."
        scene sa160 with dssa
        d "You can go into the kitchen."
        scene sa161 with dssa
        m "Come, do you want some coffee?"
        scene sa162 with dssa
        b "Yes, please."
    else:
        scene sa153 with dssa
        m "Hey! Where were you?"
        scene sa154 with dssr
        pause
        m "Oh hi!"
        scene sa155 with dssa
        b "Hello."
        scene sa159 with dssa
        d "My phone's out of battery. I'll plug it in real fast."
        scene sa160 with dssa
        d "You can go into the kitchen."
        scene sa161 with dssa
        m "Come, do you want some coffee?"
        scene sa162 with dssa
        b "Yes, please."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sa163 with dssb
    b "I'm aware that it wasn't a very nice thing to do."
    b "I was just joking around."
    scene sa164 with dssa
    pause
    scene sa165 with dssa
    d "Your jokes suck."
    scene sa166 with dssa
    b "*whispers* Kinda like your dick."
    scene sa167 with dssb
    pause
    scene sa168 with dssa
    b "Oh, my Mama keeps wondering when you're going to join the country club."
    scene sa169 with dssa
    m "Oh well-"
    scene sa170 with dssa
    d "We can't afford it."
    scene sa171 with dssa
    b "It's not that expensive."
    scene sa172 with dssa
    d "You moron, have you lost all connection to reality?"
    scene sa174 with vpunch
    m "[name]!"
    scene sa175 with dssa
    d "It costs $700 a month... each."
    scene sa176 with dssa
    m "Oh. We can't afford that."
    scene sa168 with dssr
    b "I'll talk to my mama... She has some pull."
    scene sa167 with dssa
    pause
    m "May I ask... What are you two?"
    scene sa173 with dssr
    "You look at each other."
    d "We're uh..."
    scene sa177 with dssr
    b "We fool around."
    scene sa178 with dssr
    b "Nothing serious though."
    m "That's umm... okay... cool."
    scene sa184 with dssr
    d "*Whisper* We fool around?"
    d "*Whisper* Couldn't you have said it in a different way?"
    scene sa185 with dssa
    b "*Whisper* You're right... We don't even fool around. We sometimes just kiss."
    scene sa179 with dssr
    b "My bad."
    b "We act out plays for the kindergarten theater group."
    scene sa180 with dssa
    d "Drink your coffee and choke on it."
    scene sa181 with dssr
    b "*Leans over and Whispers* At least the coffee fucks me hard."
    scene sa182 with dssa
    m "Is it too strong?"
    scene sa183 with dssa
    b "*Blushes* N-No, it's still fine. I'm just not used to it."
    scene sa186 with dssr
    m "I'll go on my morning run and get us all some rolls."
    scene sa188 with dssr
    pause
    scene sa187 with dssa
    b "You know-"
    scene sa189 with dssa
    d "Shut up."
    $ persistent.unlockedImageBellaCh5_1 = True
    scene sa190 with dssa
    b "You don't even k-"
    scene sa191 with dssa
    d "I know exactly what you were about to say."
    scene sa192 with dssa
    b "I admit it... This simple way of living has its charm."
    scene sa193 with dssa
    "You roll your eyes."
    if NamiLove4x5 is False:
        scene sa194 with dssr
        n "*Sleepy* [name]? Can you make me a coffee?"
        scene sa195 with dssr
        pause
        n "Is this a bad dream?"
        d "Nope."
        scene sa199 with dssr
        pause
        scene sa198 with dssa
        b "Cute tits."
        scene sa196 with vpunch
        n "Fuck off!"
        scene sa200 with dssr
        b "Hey puberty cal-"
        scene sa201 with hpunch
        d "Shut the fuck up and drink your coffee."
        scene sa197 with dssr
        n "Ugh! What are you doing here?!"
        scene sa202 with dssr
        b "I'm getting fucked hard by [name]."
        b "His words, not mine."
        n "Disgusting!"
        n "Both of you!"
        scene sa204 with dssa
        pause
        scene sa205 with dssa
        b "Delightful."
        scene sa206 with dssr
        d "Shut up... Make peace with her."
        scene sa207 with dssa
        b "How about no?"
        scene sa208 with dssa
        d "Do it for me."
        "Bella hesitates."
        scene sa209 with dssa
        b "No."
        scene sa210 with dssa
        d "Please."
        scene sa209 with dssa
        b "I can't promise anything."
        b "Also! I'm not the one who's always on her ass! Whenever she sees me she gives me the stink eye!"
        scene sa207 with dssa
        b "Ain't nobody gives me the stink eye!"
        scene sa211 with dssa
        d "Then I'm withholding sex."
    scene sa212 with dssr
    pause
    scene sa213 with vpunch
    pause
    scene sa214 with vpunch
    "Bella tilted her chair a little too far and it slid away beneath her."
    scene sa215 with dssa
    b "Ouch."
    scene sa216 with dssa
    pause
    scene sa217 with dssa
    pause
    scene sa218 with dssr
    b "What's your plan today?"
    if NiaDeal is True:
        scene sa219 with dssa
        d "I'm meeting up with Nia."
        scene sa218 with dssa
        b "Who's that?"
        scene sa219 with dssa
        d "The redhead with the piercings. She hangs around with Nami."
        scene sa220 with dssa
        b "The camgirl?"
        scene sa221 with dssa
        d "That one, yeah."
        scene sa222 with dssa
        "Bella squints her eyes."
        scene sa224 with dssa
        b "I see."
        b "She asked me some weird questions when I ran into her in the gym showers."
        scene sa225 with dssa
        d "Yeah, she tends to do that. I think it's best to have a healthy distance from her when either one of you is nude."
        scene sa224 with dssa
        b "Did you see her nude?"
        scene sa225 with dssa
        if namigym is True:
            d "I only saw her butt... That also happened in the gym showers."
        else:
            d "Nah."
    else:
        scene sa225 with dssa
        d "Nothing really."
    d "And what're you up to?"
    scene sa226 with dssa
    b "I have a race in a few weeks. I'll head to the shop, fix some stuff."
    b "I'm also meeting up with friends later."
    scene sa227 with dssa
    pause
    scene sa228 with dssa
    pause
    scene sa229 with dssa
    pause
    scene sa230 with dssa
    "Bella slightly moans as your tongues wrestle with each other... Your hands slide down to her thighs and you squeeze them firmly..."
    scene sa231 with dssa
    pause
    scene sa232 with dssa
    b "We can work on the project in the evening..."
    scene sa233 with dssa
    d "Nah, I've seen enough of you today."
    scene sa234 with dssr
    m "I'm back."
    if NamiLove4x5 is False:
        scene sa235 with dssr
        m "Is Nami up?"
        scene sa236 with dssa
        d "Yeah, she's awake."
        scene sa235 with dssa
        m "I'll get her."
    else:
        scene sa235 with dssr
        m "I've got us all some rolls."
        m "I hope Nami comes back soon. They're still warm."
        d "I'll go get her. I know where she might be."
        stop music fadeout 2.0
        scene black with Dissolve(2)
        with Pause(.5)
        jump NamiLook5x0
    scene black with Dissolve(2)
    with Pause(.5)
    jump Breakfast5x0


label Breakfast5x0:
    $ play_playlist(playlist_Ch2_Coffee)
    scene sa237 with Dissolve(3)
    pause
    scene sa238 with dssr
    "You notice the Cheeto staring at you."
    d "(She looks happy. I wonder what would happen if I'd pat her head.)"
    scene sa239 with dssr
    m "Bella, what are your thoughts about college?"
    scene sa247 with dssr
    b "Uhm... You mean like in general or specifically ZPR?"
    scene sa249 with dssa
    m "The latter."
    scene sa250 with dssr
    b "It's nice."
    b "High quality staff, decent lectures and a big variety of sports teams."
    scene sa239 with dssr
    m "What sports do you play?"
    scene sa250 with dssr
    b "I play a bit of everything."
    b "I do, however, like football a lot."
    scene sa240 with dssr
    b "Nojiko was it, right?"
    scene sa239 with dssa
    m "Yes."
    scene sa240 with dssa
    b "You're dating Nick Benz?"
    scene sa239 with dssa
    m "I am, yes."
    scene sa251 with dssr
    b "I used to play in the same football team as Zara."
    b "Before she quit for tennis."
    d "Was she any good?"
    scene sa252 with dssa
    b "The best we had."
    d "Why did she quit?"
    scene sa253 with dssa
    b "...Reasons."
    scene sa241 with dssr
    m "Why aren't you eating?"
    scene sa242 with dssr
    n "...I'm not hungry."
    scene sa243 with dssa
    d "For the past 10 years, you've never not eaten breakfast."
    scene sa244 with dssa
    n "The company was better the past 10 years."
    scene sa245 with dssr
    pause
    scene sa246 with dssa
    b "Then you won't mind givi-"
    scene sa344 with vpunch
    n "You touch my rolls and I'll actually kill you!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene sa254 with dssb
    b "That was good. thank you very much."
    m "I'm glad you liked it."
    scene sa255 with dssa
    pause
    scene sa256 with dssb
    d "You can be nice?"
    b "I was raised like a Lady."
    b "I know how to behave. Especially around adults."
    scene sa257 with vpunch
    "Bella jumps you."
    scene sa258 with dssr
    pause
    scene sa259 with dssr
    b "It's just that I prefer to be the sailor."
    scene sa260 with dssr
    pause
    d "Again... Thanks for today."
    scene sa261 with dssr
    d "I'm glad you came by."
    d "I really need some sleep, though."
    scene sa262 with dssa
    b "I've been awake for 30 hours too... We can sleep together... At least for two to three hours."
    scene sa263 with dssa
    d "Alright, let's go and brush our teeths."
    if NamiLove4x5 is False:
        $ BellaSleepAtMC5x0 = True
        b "Give me some privacy for two minutes."
        jump CheetoStuff5x0
    else:
        stop music fadeout 2.0
        scene black with Dissolve(2)
        $ play_playlist(playlist_AmbientBellchen)
        with Pause(.5)
        jump BellaSleep5x0



label CheetoStuff5x0:
    scene sa345 with dssb
    n "Duuude..."
    d "What?"
    scene sa348 with dssr
    n "Where did that demon come from?! Nadia promised me she wouldn't play the Ouija board without me!"
    d "Shortly after we came back from Vic's, she arrived and... we drove into the sunrise."
    n "What? You were gone?"
    d "For like three hours."
    d "We drove to a nearby strip of desert and... just watched the sky."
    n "Sounds great."
    scene sa349 with dssr
    n "But with her? Ugh! She'd ruin it."
    n "But at least you wouldn't have to look for a strip of desert for too long... As her presence turns fertile farmland into wasteland..."
    scene sa350 with dssa
    n "Are you dating now?!"
    d "No, we're not."
    scene sa351 with dssa
    n "So everything is still as it used to be? I thought you wanted a clear answer?"
    scene sa352 with dssa
    d "I do have an answer. We're keeping it casual."
    d "Before I didn't know if we were dating, casual or heading into something more serious."
    d "Now I do... And now I can act accordingly."
    scene sa353 with dssr
    n "This isn't going to end well."
    d "Stop being such a bibi."
    scene sa354 with dssa
    d "Focus on the positive."
    pause
    scene sa356 with dssa
    n "Who are you?!"
    d "Someone that focuses on the positive on this specific matter."
    scene sa357 with dssa
    n "Well... Still better than an actual relationship."
    n "That would've been sooo stupid."
    scene sa359 with dssa
    d "Would it?"
    scene sa358 with dssa
    n "Dude, we're freshmen."
    n "You go into a serious relationship in the first month and think that's going to work out?"
    scene sa360 with dssr
    n "Have you seen the asses that walk around on campus?"
    n "Could you say no to them for years?"
    d "I could."
    scene sa361 with dssa
    n "...Well, wait until that wormy wakes up! Then- Then I'll ask you again!"
    scene sa362 with dssr
    n "And I'm also sure Bella jumps from one dick to another."
    scene sa363 with dssa
    d "Stop making shit up."
    scene sa362 with dssa
    n "I'm gonna ask the Ouija board about it..."
    scene sa364 with dssa
    pause
    scene sa365 with dssa
    "Nami leaves as she spots Bella."
    jump BellaSleep5x0


label NamiLook5x0:
    $ play_playlist(playlist_Jaccuzi)
    $ NamiLake5x0 = True
    scene sa276 with dssb
    pause
    scene sa277 with dssr
    pause
    scene sa276 with dssr
    pause
    scene sa278 with dssa
    pause
    scene sa279 with dssa
    pause
    scene sa280 with dssr
    pause
    scene sa281 with dssa
    d "Yo."
    scene sa282 with dssa
    n "...Yo."
    scene sa280 with dssa
    pause
    scene sa281 with dssa
    d "Do you wanna talk or just sit here in silence?"
    scene sa283 with dssr
    n "A little bit of silence until I feel like talking..."
    scene sa284 with dssa
    pause
    scene sa285 with dssa
    "The Cheeto gets up."
    scene sa286 with dssa
    "And slowly walks towards the shore."
    scene sa287 with dssa
    pause
    scene sa289 with dssr
    if BellaDesert5x0 is True:
        n "...Where were you?"
        scene sa288 with dssa
        d "I was with Bella."
        scene sa291 with dssa
        d "She came by shortly after we came back from Vic's... and I... I just had to go with her."
        scene sa292 with dssa
        pause
        scene sa293 with dssa
        n "Did you even think about my feelings?"
        n "I came over to your room to talk..."
        n "I needed someone to listen..."
        scene sa294 with dssa
        d "I'm sorry."
    else:
        n "I... needed to talk."
        scene sa288 with dssa
        d "Then why didn't you talk to me?"
        scene sa290 with dssa
        n "I was in your room... and I freaked out."
        n "I had to leave... Clear my head."
    if NamiLove4x5 is True:
        d "Do you want to talk about what happened?"
        scene sa288 with dssr
        pause
        scene sa289 with dssa
        n "Not really."
        scene sa295 with dssa
        d "Well, I do."
        scene sa296 with dssa
        n "Why did you do it?"
        scene sa298 with dssa
        d "Do what?"
        scene sa299 with dssr
        n "Kiss me."
        d "I don't know? It felt right."
        n "I wouldn't have seen that coming in a million years."
        scene sa300 with dssr
        pause
        scene sa301 with dssa
        n "I can't even look at you."
        scene sa302 with dssr
        n "I thought I... I don't know what happened."
        scene sa366 with dssa
        d "Stuff got real when I took initiative."
        d "And it scares the shit out of you."
        scene sa367 with dssa
        n "...It does."
        scene sa368 with dssa
        n "It was all fun and games... but now... I feel like we crossed a big, blinking, red line."
        scene sa369 with dssa
        d "We can always return."
        d "As long as you get your head out of your ass."
        $ play_playlist(playlist_Chapter1a)
        scene sa370 with vpunch
        d "Listen..."
        scene sa371 with dssa
        d "What I did was nothing compared to what you've been doing to me... It's just the fact that I did it, which creeps you out."
        if BellaKiss3x5 is True:
            d "You say Bella leaves me in the dark?"
            d "You do it a thousand times worse."
            d "I don't know what you feel for me."
            d "If it's all just a game... Or if you're actually in love with me."
            d "Our past doesn't make it any easier."
            scene sa372 with dssa
            pause
            d "The fact that you now pull back all of a sudden... It reminds of that time."
        else:
            d "I don't know what you feel for me."
            d "If it's all just a game... Or if you're actually in love with me."
            scene sa372 with dssa
            d "Our past doesn't make it any easier."
        scene sa373 with dssa
        n "I-"
        scene sa374 with vpunch
        d "And if I get the feeling that you're playing me... I'll never talk to you again."
        $ persistent.unlockedImageST_CH5_1 = True
        d "You'll become a ghost."
        scene sa375 with vpunch
        n "I'm not playing anything!"
        d "I know how you are deep inside, Cheeto..."
        d "I'm certain you've changed but... there lies something within you most people would never see coming."
        scene sa376 with vpunch
        n "I'm not playing you! Or anyone else."
        n "I don't do that anymore!"
        scene sa377 with dssa
        d "I believe you."
        d "But I need you to be honest with me."
        scene sa378 with dssa
        pause
        scene sa379 with dssa
        d "What do you feel for me?"
        scene sa380 with dssa
        n "I- I don't know..."
        scene sa381 with dssr
        n "It all became so real when we kissed last night..."
        scene sa382 with dssr
        pause
        scene sa383 with dssa
        n "I just need time to think."
        pause
        menu:
            "You mean so much to me...":
                $ NamiLove5x0 = True
                scene sa385 with dssa
                d "You mean so much to me."
                d "But think about your next step very carefully."
            "Don't, and keep some healthy distance.":
                scene sa384 with dssa
                d "I'll head back."
                d "Breakfast is ready... And the rolls are still a little warm."
    $ persistent.unlockedImageNami_CH2_6 = True
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    jump Breakfast5x0


label BellaSleep5x0:
    $ BellaSleepAtMC5x0 = True
    scene sa303 with dssb
    pause
    scene sa304 with dssa
    pause
    scene sa305 with dssr
    $ persistent.unlockedImageBellaCh5_3 = True
    d "(No matter how fucked up I might be...)"
    scene sa306 with dssa
    d "(I can't deny that her body is wonderful.)"
    scene sa307 with dssa
    pause
    scene sa308 with dssa
    pause
    scene sa309 with dssr
    pause
    scene sa311 with dssb
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene sa312 with dssr
    pause
    scene sa313 with dssb
    pause
    scene sa315 with dssr
    pause
    scene sa316 with dssr
    pause
    scene sa317 with dssa
    pause
    scene sa318 with dssr
    pause
    scene sa319 with dssa
    b "...My back hurts. Stupid brick bed."
    scene sa320 with dssa
    b "I should've gone home... Nothing's worse than getting up after just a few hours of sleep."
    b "Especially when you slept on some brick!"
    scene sa321 with dssa
    d "...Shut up, please."
    scene sa322 with dssa
    b "And on top of that I'm super horny."
    scene sa323 with dssa
    pause
    scene sa324 with dssa
    pause
    scene sa325 with dssr
    d "...Sorry."
    scene sa326 with dssa
    pause
    scene sa327 with dssa
    b "It's okay."
    scene sa328 with dssa
    d "(It's not.)"
    scene sa327a with dssa
    b "Oh fuck... I just remembered that I have a football game later."
    scene sa328a with dssa
    b "Do you want to come watch?"
    scene sa329a with dssa
    if NiaDeal is True:
        d "I'm seeing Nia later."
        b "Right."
    else:
        d "Maybe next time."
    d "I didn't know you played football."
    scene sa330a with dssr
    b "I've started playing at a very young age with my sister and Zara..."
    b "Then I quit... and recently started playing with the ZPR girls team."
    b "But I'm not actually playing for ZPR. Just friendly matches against other non-college Wollust teams."
    scene sa331a with dssa
    d "Is Zara still playing?"
    scene sa330a with dssa
    b "No. She quit."
    scene sa331a with dssa
    d "What do you think of her?"
    scene sa332a with dssr
    b "Zara's okay if you meet her far away from anything remotely competitive."
    b "Her competitive self gets on your nerves."
    b "But that's not her fault."
    scene sa333a with dssa
    d "Whose was it?"
    scene sa334a with dssa
    b "Her mother's."
    scene sa333a with dssa
    d "Please elaborate."
    scene sa334a with dssa
    b "Zara and I used to play in the same football club."
    b "And while her father was working all day, her Mother took her to the games."
    b "Whenever we had any major games... Well, as major as a child game can be... and Zara had a bad or even decent game."
    scene sb1796 with dssb
    b "She'd scream at her in front of everyone, tell her how useless she is and as if she's doing it on purpose to embarrass her."
    scene sb1795 with vpunch
    b "Sometimes she even just left her there..."
    scene sa334a with dssr
    b "We were like eight or nine"
    b "Like what the fuck... She'd just leave a little girl standing in the rain."
    b "She also didn't hesitate to get physical."
    scene sa335a with dssa
    b "It was the same story in the school. Zara had to bring home an A."
    b "Sometimes I didn't see her outside the entire Summer."
    scene sa336a with dssa
    b "I don't even want to imagine what toxicity she had to endure at home. In her Mother's eyes, she was never good enough."
    b "And her father was just working all day."
    b "To be honest, she could've turned out so much worse."
    scene sa337a with dssa
    d "...I see."
    scene sa338a with dssr
    pause
    scene sa339a with dssa
    b "I was glad to hear that her father divorced that bitch."
    b "But Zara and I haven't spoken much since."
    scene sa338a with dssa
    d "Were you friends?"
    scene sa339a with dssa
    b "Yeah. Zara was always nice to me... Well, to everyone as long as you gave your best."
    b "But after we both quit, our interests changed and we stopped being friends."
    scene sa340a with dssr
    pause
    scene sa341a with dssa
    d "Do you feel fit enough to drive?"
    scene sa329 with vpunch
    pause
    scene sa330 with dssa
    b "Yah... I just need to get dressed."
    scene sa331 with dssa
    pause
    scene sa332 with dssr
    pause
    scene sa333 with dssa
    b "Alright... I'm gonna get dressed."
    d "Yeah."
    scene sa334 with dssr
    pause
    scene sa335 with dssa
    pause
    scene sa336 with dssa
    pause
    scene sa337 with dssa
    b "Do we study later?"
    scene sa338 with dssa
    d "You asked me that before... No, we'll do it tomorrow."
    scene sa339 with dssa
    pause
    scene sa341 with dssr
    b "I'll leave now."
    scene sa340 with dssa
    d "Alright, I'll see you."
    scene sa341 with dssa
    b "Yeah."
    scene sa342 with dssa
    b "Bitch."
    $ persistent.unlockedImageR_CH5_2 = True
    scene sa343 with dssa
    pause
    stop music fadeout 3.0
    scene black with Dissolve(2)
    with Pause(.5)
    if NiaDeal is True:
        jump Nia5x0
    else:
        jump CheetoHome5x0



label Nia5x0:
    $ NiaVisit5x0 = True
    scene sb1789 with dssb
    pause
    scene sb1790 with dssa
    pause
    scene sb1791 with dssa
    d "Nia? I'm on the bus."
    d "I don't really know where to go."
    scene sb1792 with dssa
    nia "City center. Daytona Building. The one with the swirly architecture."
    scene sb1793 with dssa
    d "Alright. Noodle maps says I will be there in 25 minutes."
    scene sb1794 with dssa
    nia "Good!"
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch5_Nia)
    scene sb1 with dssb
    pause
    scene sb2 with dssa
    pause
    scene sb3 with dssr
    nia "Hey!"
    d "Hey."
    nia "Please come in!"
    scene sb4 with dssa
    d "That's..."
    scene sb5 with dssb
    d "...One hell of a place."
    scene sb6 with dssa
    nia "Thanks!"
    scene sb7 with dssr
    "You stare at the almost 25 meter high ceilings in awe."
    scene sb8 with dssa
    nia "Would you like something to drink?"
    scene sb9 with dssa
    d "I'd take a beer."
    scene sb10 with dssr
    pause
    scene sb11 with dssr
    d "Nice umm... Barrel."
    scene sb12 with dssa
    nia "Oh! It's full of lube."
    d "Really?"
    scene sb13 with dssa
    nia "Yes."
    scene sb14 with dssa
    nia "Your beer!"
    scene sb15 with dssa
    d "Thanks Nia."
    scene sb17 with dssa
    nia "Do you want a little tour?"
    scene sb16 with dssa
    d "Sure."
    scene sb18 with dssr
    nia "Well, this is the main room."
    scene sb19 with dssr
    d "Is that a stripper pole?"
    scene sb20 with dssa
    nia "Yes."
    nia "I personally don't use it anymore. I lost any interest in pole dancing."
    nia "But a few friends of mine still do it and sometimes when they're here, they show me their new moves."
    scene sb21 with dssa
    nia "My kitchen."
    scene sb22 with dssa
    d "You like to cook?"
    nia "I like to bake. I just love the look of a little muffin going all puffy."
    scene sb23 with dssr
    nia "Come, follow me."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb24 with dssb
    nia "This is where I spend most of my time."
    scene sb25 with dssa
    pause
    scene sb26 with dssr
    d "Cute little room."
    scene sb27 with dssr
    d "I could imagine feeling quite unwell in that gigantic main room."
    scene sb28 with dssr
    nia "Especially if you're alone for a long time... The main room can make you spiral into a bad place."
    nia "It's so big that you feel super insignificant and even more alone."
    scene sb29 with dssa
    nia "But it's great if you got a lot of people over."
    scene sb30 with dssr
    d "What's up with all those watertoys?"
    scene sb29 with dssr
    nia "Do you really want to know?"
    d "...I retract my question."
    scene sb31 with dssr
    "You raise your beer but suddenly stop."
    scene sb32 with dssa
    pause
    scene sb33 with dssr
    d "I knew someone who had a similar one."
    scene sb34 with dssa
    nia "No."
    scene sb35 with dssa
    stop music fadeout 4.0
    nia "It's Summer's."
    scene sb36 with dssr
    pause
    scene black with Dissolve(2)
    $ play_playlist(playlist_Chapter1)
    with Pause(.5)
    scene sb38 with dssb
    pause
    scene sb39 with dssr
    d "What do you mean it's Summer's?"
    scene sb40 with dssr
    nia "Umm, as you know we did go to the same high school & middle school."
    scene sb41 with dssa
    d "I've never seen you before."
    scene sb43 with dssa
    nia "It's because I looked totally different and we also never really talked."
    scene sb42 with dssa
    pause
    scene sb44 with dssr
    nia "Summer was my friend."
    scene sb45 with dssr
    pause
    scene sb46 with dssa
    d "I'm at a loss for words."
    scene sb47 with dssr
    "Nia gently takes the stuffed animal out of your hand."
    scene sb48 with dssa
    "She stares at it for a second."
    scene sb50 with dssr
    nia "Just when I got into middle school, I had a birthday party and invited a bunch of... so called friends over."
    scene sb51 with Dissolve(3)
    pause
    scene sb52 with dssr
    nia "But nobody showed up."
    nia "My Mom put so much work into baking all these cakes and stuff..."
    nia "She was so excited for me."
    scene sb53 with dssa
    nia "It crushed me in every... in every single way."
    nia "And what I found even worse was the look of pity in my mother's eyes... I've never felt so embarrassed."
    scene sb54 with dssa
    nia "Nobody showed up... Except for her."
    scene sb55 with dssr
    pause
    scene sb56 with dssa
    pause
    scene sb57 with dssa
    nia "While I was wailing, she told me that she'd be back soon."
    nia "I didn't expect her to come back. It was a really awkward situation with me crying and her looking... awkward."
    scene sb58 with dssb
    nia "But she did... And with her an army of stuffed animals."
    scene sb59x with dssa
    nia "She filled up the empty seats with different cuddly toys and we had a little party."
    scene sb59 with dssr
    pause
    scene sb60 with dssr
    nia "I'll never forget what she did for me that day."
    scene sb1738 with dssr
    s "And sometimes! Sometimes he tries to rough me up!"
    scene sb1739 with dssa
    nia "Oh no!"
    scene sb1740 with dssa
    s "And the worst part..."
    scene sb1742 with vpunch
    s "My FISTS OF THUNDER have no effect against him!"
    scene sb1741 with dssa
    s "But! I know his weakness."
    nia "*Whispers* What is it?"
    scene sb1743 with dssr
    s "A surprise kiss."
    s "Since I used the kiss of thunder, he loses every time."
    scene sb1744 with dssr
    s "But say... Why do I never see you with people?"
    scene sb1745 with dssa
    nia "Oh, umm... You see... I'm not very popular."
    scene sb1746 with dssa
    nia "As you can see..."
    scene sb1747 with dssa
    s "Being popular is for babies!"
    s "What you need is one good friend! And I'm your friend!"
    scene sb1748 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb49 with dssb
    nia "She told me to keep this one."
    scene sb62 with dssa
    nia "It's very precious to me."
    scene sb63 with dssa
    nia "She also told me about you... She was deeply, deeply in love with you."
    nia "And whenever I hear the words 'True love', I think of the tone her voice had that day."
    nia "The way her eyes sparkled... The glow surrounding her... She was on another plane of existence when she talked about you."
    scene sb64 with dssa
    pause
    scene sb65 with dssa
    nia "And after the party, I kind of depended on her... She was my best friend even though I'm pretty sure she didn't see me as her best friend."
    nia "But whenever she saw me, she came over and asked me how I've been."
    nia "She never judged my stutter, nor did she ever negatively comment on my stupid laugh."
    nia "When she suddenly didn't come to school anymore... It affected me a lot."
    scene sb66 with dssa
    nia "That was also the only time I ever spoke to you... I asked you where she was and... you just ignored me and walked away."
    nia "But I didn't take it personal because... I could see it in your eyes that something was terribly wrong."
    scene sb67 with dssa
    "Nia realizes that your eyes are watery."
    scene sb68 with dssr
    nia "Oh my god! I'm so stupid!"
    scene sb69 with dssa
    nia "I'm so sorry!"
    scene sb70 with dssr
    nia "I shouldn't have- oh god... I'm such an idiot!"
    nia "I totally ruined the mood."
    scene sb71 with dssa
    d "Yeah... You did."
    scene sb73 with dssr
    pause
    scene sb74 with dssr
    pause
    scene sb75 with dssa
    d "Is that... Is that Turoky 2?"
    scene sb76 with dssr
    nia "Umm... Yes."
    scene sb77 with dssa
    d "...I never managed to beat that fucking bug level"
    scene sb78 with dssa
    nia "I had to stop on the first level because I was so scared!"
    scene sb79 with dssa
    d "Let's play it..."
    nia "I heard they have a multiplayer mod... It's gonna be tough, though."
    scene sb80 with dssa
    d "Get us some more beer, and I'll set up the console."
    scene sb81 with vpunch
    nia "On my way!"
    scene sb82 with dssr
    d "You know you could've just gone past me, instead of over me?"
    scene sb83 with dssa
    nia "That's for babies!"
    scene sb84 with dssr
    "As you connect the console..."
    scene sb85 with dssa
    "You occasionally peek over to the cuddle toy."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    $ play_playlist(playlist_Ch5_Nia)
    with Pause(.5)
    scene sb86 with dssb
    nia "I hope that's enough!"
    d "Yeah, should be."
    scene sb87 with dssa
    pause
    scene sb88 with dssa
    d "Say, why is the entire shelf empty."
    nia "Oh, I just got it... I ordered it from E-Worm... No biggie..."
    scene sb89 with dssr
    "You sweep your finger over the shelf."
    scene sb90 with dssr
    d "There's dust on it... With a clean spot in the middle."
    scene sb91 with dssa
    nia "Damn, you're good."
    scene sb92 with dssa
    d "Nia... I'm here to get to know the real you."
    scene sb93 with dssr
    nia "It uh- uhm..."
    scene sb94 with dssa
    nia "It was full of sex toys... I thought they mig-"
    scene sb96 with dssa
    d "Hey, I want to get to know YOU, the real Nia... Not some made up Christian girl..."
    d "You're a cam girl... So stand by it."
    scene sb95 with dssa
    nia "I do!"
    scene sb97 with dssa
    nia "Usually..."
    scene sb98 with dssa
    nia "Okay! Sorry! I won't hide them again."
    scene sb99 with dssr
    nia "Aaaaand everything else I hid."
    scene sb100 with dssa
    nia "...If there's gonna be a next time."
    scene sb101 with dssa
    d "It depends on your dino killing performance."
    scene black with Dissolve(2) #long road GONNA FLY HIGH (NORA MUCKE)
    with Pause(.5)
    scene sb103 with dssb
    pause
    scene sb104 with dssr
    d "Are you ready?"
    scene sb105 with dssa
    nia "I haven't played the game in forever... and I remember it being super scary!"
    scene sb108 with dssr
    d "The game's kind of a loose end for me."
    d "...At least I get to solve this one."
    scene sb109 with dssa
    "She takes your hand."
    scene sb107 with dssa
    nia "Let's kill some dinos."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb110 with dssb
    pause
    scene sb111 with dssa
    d "Shit you weren't kidding... It's much harder."
    scene sb112 with dssa
    nia "Okay... You use the TEK BOW on these upper two, and I rush through the middle and kill the compys."
    scene sb113 with dssa
    pause
    scene sb114 with dssa
    nia "See! All we need is some good tactic."
    d "And we're almost at the end of level 1."
    scene sb115 with dssr
    nia "I remember when I was a little kid, and I asked my mother to play it with me."
    scene sb116 with dssa
    nia "She sat next to me, while I just pushed down the stick to move forward... I didn't look at the screen because I was too scared."
    scene sb117 with dssa
    nia "It's a very fond memory."
    scene sb118 with dssr
    d "(I hear some sadness in her voice... An almost unnoticeable layer.)"
    scene sb119 with dssa
    d "That sounds cute."
    scene sb120 with dssa
    d "...How's she these days?"
    scene sb121 with dssa
    nia "We uh- don't talk anymore."
    $ persistent.unlockedImageNia2 = True
    d "Why?"
    scene sb122 with dssa
    nia "My entire family abandoned me when they found out that I'm a cam girl."
    nia "I was no longer invited to family dinners or birthday parties."
    nia "My cousins stopped answering my texts, and they blocked me on most of the social media sites."
    nia "Except for that one creepy uncle who instead asked me for a link."
    scene sb123 with dssa
    nia "Until recently when they found out that I make a loooot of money."
    scene sb124 with dssa
    d "You're not gonna-"
    scene sb125 with dssa
    nia "I don't know... I miss them... I have no one else..."
    scene sb126 with dssa
    nia "They're my family... you know?"
    scene sb127 with dssr
    d "That shouldn't matter... They alienated you the second they heard about your work..."
    d "They only care about the money, not about the person behind it."
    scene sb128 with dssa
    nia "I know... But maybe if I-"
    scene sb129 with dssa
    d "No."
    scene sb130 with dssa
    d "Be- *sigh*."
    scene sb131 with dssr
    d "I can't tell you what to do... You know what's best."
    scene sb132 with dssa
    nia "Do I?"
    scene sb133 with dssa
    d "Probably not."
    scene sb134 with dssa
    nia "*Sigh*"
    scene sb135 with dssa
    nia "It can't hurt to meet up with them once."
    scene sb136 with dssa
    "You say nothing and only flick your brows."
    scene sb137 with dssr
    pause
    scene sb138 with dssa
    d "Raise your weapon, soldier. We've got some Dino's to fu-... kill."
    scene sb140 with dssa
    d "How did this cam girl stuff start? One day you just thought about undressing yourself in front of a camera?"
    scene sb141 with dssa
    nia "I always had a very high libido... And for a long time, I thought something was wrong with me..."
    nia "All those movies, TV series and news telling me that girls usually don't like sex."
    nia "...So why was it that I did? That my body reacted that way?"
    scene sb142 with dssa
    nia "I felt weirded out by my own body."
    scene sb143 with dssa
    nia "And what usually happens with urges we try to suppress... I got frustrated and then discovered porn... and after a while I found the thought exhilarating."
    scene sb144 with dssa
    d "For doing your own?"
    scene sb143 with dssa
    nia "Yes."
    scene sb145 with dssr
    nia "The day I blew out 18 candles on my birthday cake, I uploaded my first boob picture."
    d "I see."
    scene sb146 with dssr
    nia "While I love doing this... It had the unfortunate side effect of alienating me from a lot of social gatherings."
    nia "It's pretty much impossible to find a boyfriend with my line of work."
    nia "Don't get me wrong- many guys wanna sleep with me... But I really don't want to sleep with them."
    scene sb147 with dssr
    d "Yeah, you do strike me as someone who needs a little more."
    scene sb148 with dssr
    nia "Exactly. Trust is really hard to establish when I always suspect people of just wanting to fuck me."
    nia "That's why I never invite guys over, and if I meet up with a guy friend, I always choose public places so that he doesn't try to hit on me."
    d "Last time I checked I was a guy."
    scene sb149 with dssa
    nia "Yes! But you're sooo weird!"
    nia "You have never looked at my boobs."
    nia "Nor did you ever make any innuendos."
    scene sb150 with dssr
    d "Not true. I looked at your cleavage a few minutes ago... To be fair, it's hard to overlook."
    scene sb151 with dssr
    nia "I'd be lying if I said our history didn't also play a role..."
    nia "With you... I know that you're not here because you want to sleep with me."
    nia "You're actually here because you want to get to know me... Or because I kind of forced you to be here when we made the deal."
    scene sb152 with dssa
    d "What if my perception of you changes and someday I want to sleep with you?"
    scene sb153 with dssa
    nia "I hope so!"
    "You raise a brow."
    scene sb154 with dssa
    nia "It means you want to sleep with me because of who I am, and not just because you found me on the internet."
    nia "I have a lot of followers in the adult world and so many people see me as a trophy."
    nia "But yeah... It's a lonely field of work if you're not one of those lucky girls to find a guy to do it with."
    scene sb155 with vpunch
    d "Careful, dino on the left."
    scene sb156 with dssb
    pause
    nia "Could you be with a girl that does this?"
    menu:
        "Yeah, I think I'm pretty open minded when it comes to that.":
            $ Niqs5x0 = True
            scene sb157 with dssr
            d "But I lack experience, so I might change my mind later on."
        "It's a complex topic... It depends on a few factors.":
            $ NiqsV5x0 = True
            nia "Makes sense."
        "No, I wouldn't like it.":
            $ NiqsNo5x0 = True
            scene sb158 with dssr
            nia "That's cool."
            nia "And this is exactly why I invited you over."
            nia "You're honest with me."
    scene sb159 with dssa
    d "Would you ever want to stop doing it?"
    scene sb160 with dssa
    nia "Maybe? It's so much more than just work for me... I like it."
    nia "But, if I ever find the right guy and he really wants me to stop it... Maybe."
    nia "But then the question becomes... Is that the right guy for me?"
    scene sb161 with dssa
    nia "I'm studying architecture... So I could work in said field someday."
    scene sb162 with dssa
    d "Architecture?"
    scene sb164 with dssa
    nia "Yes! I love drawing... Okay I mostly draw lewd stuff but- BUT I can also draw very beautiful and detailed buildings when I'm not drawing a succubus getting-"
    nia "*Cough* Nevermind."
    scene sb162 with dssa
    menu:
        "I'd like to see some of your art some day.":
            $ ArtNia5x0 = True
            scene sb164 with dssa
            nia "Sure!"
        "Don't say it.":
            pass
    scene sb165 with dssr
    d "Level one done."
    d "Good job."
    scene sb166 with vpunch
    "She jumps up and hugs you."
    d "...Okay."
    d "Level two?"
    scene sb167 with dssr
    nia "Yes."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb236 with dssb
    pause
    scene sb237 with dssa
    d "I'm dead."
    d "Those turrets are fucking us."
    scene sb238 with dssa
    pause
    scene sb239 with dssa
    nia "Shit. I'm dead too."
    nia "We need to come up with a plan."
    scene sb240 with dssa
    pause
    scene sb241 with dssa
    nia "I can think better in this position."
    scene sb242 with dssa
    d "Well, I'm not gonna fuck with a running system."
    scene sb243 with dssr
    pause
    scene sb244 with vpunch
    nia "Okay! We leave the triceratops behind and do it on foot!"
    nia "We'll be much harder to hit... But we need to compensate for our lack of firepower with our aim."
    d "I doubt it's gonna work, but I don't have a better plan."
    scene black with tleaf
    with Pause(1)
    scene sb245 with tleaf
    pause
    if BellaKiss3x5 is True:
        scene sb246 with dssa
        nia "Are you and Bella... You know... Doing it?"
        scene sb245 with dssa
        pause
        scene sb247 with dssa
        nia "Was it too personal?"
        menu:
            "We're just project partners.":
                scene sb248 with dssr
                nia "Oh! I thought you were dating."
                d "No... We decided against it."
            "We're not serious." if BellaNonExclusive5x0 is True:
                scene sb248 with dssr
                nia "Like an open relationship?"
                scene sb249 with dssa
                d "No."
                d "We're just... I don't know... Nothing."
                d "We sometimes do stuff but without any real intent."#
                scene sb248 with dssa
                nia "So you do date others?"
                scene sb249 with dssa
                d "I could."
                scene sb250 with dssa
                nia "I bet Bella's really tight."
                scene sb251 with dssa
                d "Huh?"
                scene sb252 with vpunch
                nia "I- uh mean in behavior! L-like uhhhh- tight, cool behavior!"
            "Dismiss her question.":
                scene sb249 with dssa
                d "Yeah, I'd rather not talk about Bella."
                scene sb248 with dssa
                nia "Okay cool!"
    scene sb253 with dssr
    d "We're dead again... One life left."
    scene sb254 with dssr
    pause
    "She wiggles her butt back and forth."
    scene sb255 with dssa
    nia "Do you know what really helps me think?"
    scene sb256 with dssa
    d "I'm not sure I want to know the answer."
    scene sb257 with dssa
    nia "Classical music."
    scene sb258 with dssa
    d "Then put some on."
    scene sb259 with dssa
    nia "No."
    "She takes a dramatic pause."
    nia "I want to hear the screams of the dinos when our bullets pierce their dark hearts."
    scene sb260 with dssa
    d "Now we're talking, girl."
    scene sb258 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb168 with dssb
    pause
    d "(She's coming closer and closer...)"
    menu:
        "Deny her subtle advances and ask her to give you a little more space.":
            $ NiaDenied5x0 = True
            d "Would you mind giving me a little more space? It's hard to play properly."
            nia "Oh sorry! Sure!"
            jump NiaWin5x0
        "Pull her closer.":
            $ NiaInt5x0 = True
            scene sb169 with dssr
            "You pull her between your legs."
            scene sb170 with dssa
            nia "Now I'm glad that I don't have a penis or you could see me pitching a tent."
            scene sb171 with dssa
            pause
            scene sb172 with dssa
            nia "...Why would I say something like that..."
            scene sb173 with dssa
            d "(She's visibly tense... She certainly didn't see that coming.)"
            d "(But I can't properly play this way... I underestimated the size of her boobs.)"
            scene sb174 with dssa
            pause
            scene sb175 with dssa
            nia "Oh god! There's two up there!"
            d "I'll kill them!"
            scene sb176 with dssa
            pause
            scene sb177 with dssa
            pause
            scene sb178 with dssa
            d "I couldn't properly aim."
            scene sb179 with dssa
            nia "My boobs were in the way?"
            d "Yeah."
            scene sb180 with dssa
            nia "They tend to do that."
            scene sb180a with dssr
            nia "Oh god... I just remembered that I accidentally flashed my boobs to you during sports class..."
            scene sb181a with dssa
            d "I doubt you'd have a problem with that."
            scene sb180a with dssa
            nia "I didn't because it was you... But I was afraid of being the weirdo again."
            scene sb182a with dssa
            d "If I was you I'd been more afraid of getting my piercings caught up somewhere."
            scene sb183a with dssa
            nia "Ugggh... It's a hassle to get them out and back in... I only take my nipple piercings off. It doesn't take much time."
            scene sb184a with dssa
            d "I see, so you've got more piercings."
            scene sb185a with dssa
            nia "Yeah."
            scene sb186a with dssa
            nia "See."
            pause
            scene sb187a with dssa
            d "I see."
            scene sb188a with dssa
            $ persistent.unlockedImageNia3 = True
            nia "I also have a piercing further down."
            pause
            scene sb189a with dssr
            pause
            scene sb190a with dssr
            pause
            jump NiaLose5x0


label NiaLose5x0:
    scene sb181 with dssr
    pause
    scene sb182 with dssa
    d "We've been playing for five hours."
    scene sb183 with dssa
    nia "Oh shit- I need to make a post that I can't stream today."
    scene sb184 with dssa
    d "You don't need to cancel your work for me, I'll just leave when you stream."
    scene sb185 with dssr
    nia "*Quietly mumbles* Or you'll join me."
    d "Mh? What?"
    nia "Nooothing."
    scene sb186 with dssr
    pause
    scene sb187 with dssr
    d "Is that the streaming site?"
    scene sb188 with dssa
    nia "Yes."
    scene sb189 with dssr
    d "Aether."
    nia "I use Aether as my pseudonym."
    scene sb190 with dssa
    pause
    scene sb191 with dssa
    d "Wait."
    d "That girl, I've seen her before..."
    scene sb192 with dssa
    nia "She works at a cafe close to the college."
    scene ae2036a with dssr
    d "Right." #flashback
    scene sb192 with dssr
    nia "She faces the same problem I do... parents that wouldn't approve."
    nia "So she just works there as a cover."
    scene sb193 with dssr
    nia "Do you want to watch her stream?"
    scene sb194 with dssa
    d "No thanks."
    d "I'd imagine that this streaming stuff would get old really fast."
    scene sb195 with dssa
    nia "If you solely focus on the stream, yes... But I play games while streaming."
    nia "Last time I streamed, I played Age of Wormies with Nami."
    d "I thought the people were here for porn."
    scene sb196 with dssa
    nia "They don't see me play, the camera is positioned in a very particular angle while I sometimes switch up positions."
    scene sb197 with dssa
    pause
    scene sb198 with dssa
    nia "Ah."
    nia "These are some good friends of mine."
    scene sb199 with dssa
    d "Is that a private chat?"
    scene sb198 with dssa
    nia "Yes, but it's like a group chat. We're all in there."
    scene sb199 with dssa
    d "Are you talking about me there?"
    scene sb200 with vpunch
    nia "Huh? Where?"
    scene sb201 with dssa
    d "There. 'I'll ask the cute emo guy'."
    scene sb202 with dssa
    nia "..."
    scene sb203 with dssa
    nia "Umm, I just mentioned you... that you were coming to see me."
    scene sb204 with dssa
    d "What did you want to ask me?"
    scene sb205 with dssa
    nia "Nothing!"
    scene sb206 with dssr
    d "Nia... Remember our talk from earlier."
    scene sb207 with dssa
    nia "I really didn't want to ask you anything because I know you would've said no."
    nia "I just told them that I would ask you so they stopped asking."
    scene sb206 with dssa
    d "What is it?"
    scene sb208 with dssa
    nia "We're... *sigh* We've just been joking around lately that we should bring a guy in for us five to share."
    scene sb206 with dssa
    d "See. You can act socially decent and predict a very likely outcome."
    scene sb210 with dssa
    nia "Yes!"
    scene sb209 with dssa
    nia "Because that would be weird... Right?... Right?"
    scene sb211 with dssa
    "You raise your brows."
    scene sb212 with dssa
    nia "Yes weird... Super weird..."
    if Niqs5x0 or NiqsV5x0 is True:
        scene sb213 with dssr
        nia "...But in the off chance that you'd change your mind... I could introduce you."
        nia "Maybe they'll like you."
        scene sb214 with dssa
        d "Most likely not."
        if BellaNonExclusive5x0 and Niqs5x0 is True:
            $ NBS5x0 = True
            scene sb215 with dssr
            nia "And if Bella would be cool with it, she can-"
            d "I don't think you know Bella at all."
            scene sb216 with dssa
            nia "I don't... But hope dies last, huh?"
            scene sb217 with dssa
            d "I think she'd kill you all... then me... and then herself before she'd join one of these streams."
        else:
            pass
    scene black with Dissolve(2)
    with Pause(.5)
    jump NiaContinue5x0

label NiaWin5x0:
    scene sb220 with dssr
    "You two focus intensively on the game."
    scene sb221 with dssa
    nia "Oh god! There's two up there!"
    scene sb222 with dssa
    d "I'll kill them!"
    scene sb223 with dssr
    pause
    scene sb224 with dssr
    nia "Good shot!"
    scene sb225 with dssa
    nia "We really did it."
    scene sb226 with vpunch
    pause
    scene sb227 with dssa
    d "Good work, redhead."
    scene sb228 with dssa
    nia "Thanks! You too!"
    scene sb229 with dssa
    pause
    scene sb230 with vpunch
    pause
    scene sb231 with dssa
    pause
    scene sb232 with dssa
    pause
    scene sb234 with dssa
    nia "Next would be level three."
    scene sb233 with dssa
    d "We'll do it next time."
    d "We've already been playing for five hours."
    scene sb235 with vpunch
    nia "Oh shit! I need to make a post that I can't stream today."
    scene sb184 with dssa
    d "You don't to need cancel your work for me, I'll just leave when you stream."
    scene sb185 with dssr
    nia "*Quietly mumbles* Or you'll join me."
    d "Mh? What?"
    nia "Nooothing."
    scene sb186 with dssr
    pause
    scene sb187 with dssr
    d "Is that the streaming site?"
    scene sb188 with dssa
    nia "Yes."
    scene sb189 with dssr
    d "Aether."
    nia "I use Aether as my pseudonym."
    scene sb190 with dssa
    pause
    scene sb191 with dssa
    d "Wait."
    d "That girl, I've seen her before..."
    scene sb192 with dssa
    nia "She works at a cafe close to the college."
    scene ae2036a with dssr
    d "Right."
    scene sb192 with dssr
    nia "She faces the same problem I do... parents that wouldn't approve."
    nia "So she just works there as a cover."
    scene sb193 with dssr
    nia "Do you want to watch her stream."
    scene sb194 with dssa
    d "No thanks."
    jump NiaContinue5x0




label NiaContinue5x0:
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb261 with dssb
    pause
    scene sb263 with dssa
    $ persistent.unlockedImageST_CH5_2 = True
    nia "Nami says you should check your phone."
    scene sb264 with dssa
    pause
    #sms
    n "We're going to the book club today."
    n "Please be there."
    d "Alright."
    scene sb265 with dssa
    d "You never interacted with Nami in middle slash high school, right?"
    scene sb266 with dssa
    nia "Noo, she was popular, I was shy and nerdy."
    nia "And I got the feeling that she was kinda mean."
    scene sb267 with dssa
    d "She was."
    scene sb268 with dssa
    nia "She changed though?"
    scene sb269 with dssr
    d "Yeah... The Cheeto *sigh*... She changed a lot."
    scene sb270 with dssr
    nia "I remember that you and Nami weren't really cool with each other."
    nia "But nowadays when she talks about you, she's super cute... She says a lot of nice things."
    scene sb271 with dssa
    d "Did the Cheeto tell you to say that?"
    scene sb272 with dssa
    nia "Of course not."
    nia "I just asked her about you. How's it going and stuff."
    nia "I noticed that you two seem close."
    scene sb273 with dssa
    if NamiLove4x5 is True:
        d "...A little."
    else:
        d "At least closer than we used to be."
    scene sb274 with dssr
    d "I must say, you behaved relatively normal."
    d "Even though I think you were playing a role."
    scene sb275 with dssa
    nia "I wasn't. I mean I hid the sex toys, furniture and some posters."
    scene sb276 with vpunch
    nia "But besides that I was one hundred percent Nia!"
    scene sb277 with dssa
    nia "It's just that in public situations, where a lot of sensory perception blasts onto me, I can lose my cool and say weird stuff."
    nia "It can also happen when I get nervous... Which happens pretty fast."
    scene sb278 with dssr
    if NiaInt5x0 is True:
        d "Alright, we'll have to meet up again soon... We need to finish level two."
    else:
        d "Alright, we'll have to meet up again soon... We need to finish the game."
    scene sb279 with dssa
    nia "I'd love that."
    scene sb280 with dssa
    pause
    if Niqs5x0 is True:
        scene sb282 with vpunch
        nia "Wait!"
        scene sb283 with dssr
        nia "Would- uuhhhh- You ummm... have some drinks at a local bar before we continue playing next time?"
        scene sb284 with dssa
        d "(She's asking me out... Hmm.)"
        menu:
            "Agree to have some drinks with her.":
                $ NiaDate5x0 = True
                d "(She's weird... and a social outcast.)"
                d "(We also have some blurred history but... I enjoyed my time here.)"
                d "Yeah, we can have some drinks... and food."
                scene sb285 with dssa
                nia "Great! I uhm- wow great..."
                scene sb286 with dssa
                nia "Oh god! I'm blabbering!"
                scene sb287 with dssa
                d "I'll see you, have a nice stream."
                scene sb288 with dssa
                nia "Thanks! You too!"
                scene sb289 with dssa
                pause
                scene sb290 with dssa
                stop music fadeout 2.0
                nia "'You too'? Why did I say that?!"
                $ achievement.grant("NiaDateA")
                $ achievement.sync()
            "I'm sorry but I'll have to decline.":
                $ NiaNoDate5x0 = True
                scene sb291 with dssa
                nia "That's cool! Cool cool!"
                nia "Yeah!"
                scene sb292 with dssa
                pause
                scene sb291 with dssa
                nia "I'm being weird, huh?"
                scene sb293 with dssa
                d "A little."
                d "Anyways, I enjoyed it."
                d "I'll see you, and have a nice stream."
                scene sb294 with dssa
                nia "Thanks! You too!"
                scene sb289 with dssa
                pause
                scene sb290 with dssa
                stop music fadeout 2.0
                nia "'You too'? Why did I say that?!"
    else:
        scene sb281 with dssa
        d "Thanks, I enjoyed today."
        d "Good beer, by the way."
        scene sb294 with dssa
        nia "I enjoyed it too!"
        scene sb295 with dssa
        d "I'll see you, and have a nice stream."
        scene sb294 with dssa
        nia "Thanks! You too!"
        scene sb289 with dssa
        pause
        scene sb290 with dssa
        stop music fadeout 2.0
        nia "'You too'? Why did I say that?!"
    play music "music/Suspense/A.W - Darkness Inside.ogg"
    scene sb296 with dssb
    pause
    scene sb297 with dssr
    pause
    scene sb298 with dssr
    pause
    scene sb299 with dssr
    pause
    scene sb300 with dssr
    pause
    scene sb301 with dssr
    pause
    "*Faint whisper* All alone."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ achievement.grant("NiaBesuch")
    $ achievement.sync()
    jump CheetoHome5x0


label CheetoHome5x0:
    $ play_playlist(playlist_BellaDate)
    if NiaVisit5x0 is True:
        scene sb321 with dssb
        pause
        scene sb322 with dssa
        d "(I have no idea who's car that is... Probably Ayua's.)"
        scene sb303 with dssr
        pause
    else:
        if BellaDesert5x0 is True:
            scene sb1788xx with dssb
        else:
            scene sb1788x with dssb
        pause
        if BellaDesert5x0 is True:
            scene sb1789xx with dssa
        else:
            scene sb1789x with dssa
        "You hear some familiar and unfamiliar voices from the living room."
    scene sb305 with dssr
    pause
    scene sb306 with dssr
    n "Gotcha!"
    n "What happened then?"
    scene sb307 with dssa
    ev "I blocked him."
    n "Good."
    pause
    if BellaDesert5x0 and NamiLove4x5 is True:
        scene sb309 with dssa
    else:
        scene sb308 with dssr
    n "Yo."
    d "Yo."
    scene sb310 with dssa
    na "Hi [name]."
    scene sb311 with dssa
    d "Hey Nadia."
    scene sb314 with vpunch
    ev "Him?!"
    scene sb312 with dssa
    n "Uhhh... Yeah? Why?"
    d "Beanpole."
    scene sb315 with dssa
    ev "You stupid ass!"
    scene sb316 with dssa
    n "Did I miss something?"
    if NiaVisit5x0 is True:
        scene sb317 with dssr
        n "How was it at Nia's?"
        scene sb318 with dssa
        if NiaDate5x0 is True:
            d "It was good."
        else:
            d "It was alright."
    scene sb319 with dssr
    na "Will you join us?"
    scene sb320 with dssa
    d "Nah."
    scene black with Dissolve(2)
    with Pause(.5)
    show screen phone_hotspot
    if BellaDesert5x0 is True:
        scene sb1733 with dssr
        pause
        scene sb1733x with dssa
    else:
        scene sb1733t with dssr
    if MilaKiss4x5 and MilaDate is True:
        $ persistent.unlockedImageMilaCH5_1 = True
        show mi_c_1 with dssr
        pause
        show mi_c_2 with dssa
        pause
        show mi_c_3 with dssa
        pause
        show mi_c_4 with dssa
        pause
        show mi_c_5 with dssa
        pause
        show mi_c_6 with dssa
        pause
        show mi_c_7 with dssa
        pause
        $ MSGMilaDone = True
        if BellaDesert5x0 is True:
            scene sb1733_2 with dssa
        else:
            scene sb1733t_2 with dssa
        mi "Hi..."
        d "Hey..."
        d "Okay listen... I'm not sure what I want... or more likely what I could tolerate."
        d "I could say 'Yeah! Sure!' but then falter a few days after."
        d "I'm sorry, but I can't give you a real answer."
        mi "I think this is quite a real answer... It shows that you at least took some time to think about it."
        mi "So, how about this... You and I... Wednesday, just us two?"
        d "I'm sorry but Wednesday is bad... I have a personal thing to take care of."
        d "Thursday?"
        mi "I'll have to work, but we can meet up in the evening?"
        d "Alright."
        mi "Awesome. But remember to keep it cool! We don't want you to crash and burn."
        mi "Bye."
        d "Bye."
        scene sb1733x with dssa
        with Pause(.3)
        show mi_c_8 with dssa
        pause
        scene sa0 with dssr
        pause
        scene sb1733x with dssr
        with Pause(.3)
        show mi_c_8 with dssr
        show mi_c_9 with dssr
        pause
        show mi_c_10 with dssa
        pause
        $ MilaChat_CH5 = True
        if BellaDesert5x0 is True:
            scene sb1733 with dssa
        else:
            scene sb1733t with dssa
        show ptut_1 with dssa
        pause
        jump BellchenSunrise5x0


    elif vicdate and VictoriaKiss4x5 is True:
        if BellaDesert5x0 is True:
            scene sb1733x with dssa
        else:
            $ persistent.unlockedImageVicPic = True
            scene sb1733tx with dssr
            scene sb1733x with dssr
            show vi_c_1 with dssr
            pause
            show vi_c_2 with dssa
            pause
            show vi_c_3 with dssa
            pause
            show vi_c_4 with dssa
            pause
            show vi_c_5 with dssa
            pause
            show vi_c_6 with dssa
            pause
            scene vicboobies with dssr
            pause
            if BellaDesert5x0 is True:
                scene sb1733x with dssa
            else:
                scene sb1733tx with dssr
            show vi_c_7 with dssa
            pause
            show vi_c_8 with dssa
            pause
            show vi_c_9 with dssa
            pause
            show vi_c_10 with dssa
            pause
            scene sb1733x with dssa
            show vi_c_11 with dssa
            pause
            show vi_c_12 with dssa
            pause
            $ VicChat_CH5 = True
            show ptut_1 with dssa
            pause
            jump BellchenSunrise5x0
    else:
        jump BellchenSunrise5x0





label BellchenSunrise5x0:
    stop music fadeout 2.0
    scene black with Dissolve(2)
    $ play_playlist(playlist_Ch2_New)
    with Pause(.5)
    scene sb1729 with dssb
    pause
    "The sudden ring of your phone scares you out of sleep."
    scene sb1730 with dssr
    d "*Sigh*"
    scene sb1731 with dssa
    d "...Yes?"
    scene sb1681 with dssb
    b "It's me."
    scene sb1680 with dssa
    d "...What do you want?"
    scene sb1682 with vpunch
    b "Don't give me this attitude, bitch."
    scene sb1683 with dssa
    d "...Sorry... I'm so dead tired."
    scene sb1684 with dssa
    b "I got a call from Stefan Holgerson."
    scene sb1732 with dssr
    d "The father of Mario?"
    scene sb1684 with dssr
    b "Yes."
    b "He wants to see me."
    scene sb1685 with dssa
    b "He said there's something we need to discuss."
    scene sb1687 with dssa
    b "We need to meet up. Now."
    scene sb1688 with dssa
    d "*sigh* I just wanna fucking sleep..."
    scene sb1689 with dssa
    if bellameet is True:
        b "You can sleep in prison."
    scene sb1690 with dssr
    b "I'll send you the address. Meet me there."
    scene sb1691 with dssa
    d "Does a bus drive there?"
    scene sb1692 with dssr
    b "Get a car, you broke ass bitch!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene sa387 with dssr
    n "Where are you going?"
    scene sa388 with dssa
    d "I've gotta see Bella... But I don't know how to get there."
    scene sa389 with dssa
    na "Eva."
    scene sa390 with dssa
    na "You were about to leave. Take him with you."
    scene sa391 with vpunch
    ev "NO WAY!"
    ev "He insulted me!"
    scene sa392 with dssa
    d "I'm sure Bella would appreciate it."
    scene sa394 with vpunch
    ev "That's emotional blackmail!"
    scene sa395 with dssr
    d "Yeah."
    scene sa396 with dssa
    ev "Ugh! Fine."
    scene sa397 with dssr
    d "Thanks... Beanpole."
    scene sa398 with vpunch
    ev "YOU-"
    scene sa399 with dssa
    na "[name]! Be nicer to her!"
    scene sa400 with dssr
    d "I'm just fucking with you."
    d "Thanks Eva."
    scene sa401 with dssa
    pause
    scene sa402 with dssa
    d "(I'll see a lot of future potential in triggering her.)"
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb323 with dssb
    pause
    scene sb324 with dssa
    pause #booty
    scene sb325 with dssr
    "With every step she takes, her pants slide down even further."
    scene sb326 with dssa
    pause
    scene sb327 with dssr
    d "Don't you have pants that fit?"
    scene sb328 with dssa
    "She stops in her tracks and pulls her pants up."
    scene sb329 with dssa
    ev "Fuck you."
    scene sb330 with dssa
    d "I actually meant that question. Do you struggle finding clothes in your size?"
    scene sb331 with dssr
    "She ignores you and gets into her car."
    d "(Looking at her tall, skinny frame... I can imagine that shopping must suck.)"
    scene sb332 with dssr
    pause
    menu:
        "At least your car looks better than Bella's.":
            $ EvaCarCompliment5x0 = True
            scene sb333 with dssa
            ev "I don't like the looks of her car either. But it's also not her car."
            scene sb335 with dssa
            d "Not hers?"
            scene sb336 with dssr
            ev "She took it from some guy after she beat him, and now mostly drives it out of spite."
            scene sb334 with dssa
            d "The guy must be fuming."
            scene sb337 with dssa
            ev "Mhm."
        "Don't start a conversation with her.":
            scene sb334 with dssr
            pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb338 with dssb
    pause
    scene sb339 with dssa
    "She catches you looking at her arm."
    scene sb340 with dssa
    ev "Don't say anything wrong now."
    scene sb341 with dssa
    d "I didn't plan to."
    "You chuckle."
    scene sb343 with dssr
    d "Sorry."
    if BellaOnIce5x0 or BellaNonExclusive5x0 is True:
        scene sb342 with dssa
        ev "I don't get what Bella sees in you."
        ev "She deserves so much better."
        scene sb343 with dssa
        d "Every girl has that one female friend that just shit talks all the guys."
        scene sb342 with dssa
        ev "That's usually not me! But you're just an asshole."
        scene sb343 with dssa
        d "True."
    else:
        scene sb344 with dssa
        pause
    scene sb345 with dssr
    d "Are you good at racing?"
    scene sb346 with dssa
    ev "Yes."
    menu:
        "Trigger her a little.":
            $ EvaTrigger5x0 = True
            scene sb345 with dssa
            d "I guess being this light makes you go faster."
            scene sb347 with dssa
            "Her face squints together... Holding in her rage."
            d "Did you ever like fly-"
            scene sb348 with vpunch
            ev "FUCK OFF!"
            if BellaNonExclusive5x0 is True:
                ev "I will get Bella to dump your ass!"
        "Don't trigger her.":
            pass
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch5_ViceCity)
    scene sb352 with dssb
    pause
    scene sb349 with dssb
    pause
    scene sb350 with dssb
    pause
    scene sb353 with dssr
    b "Hey Eva?"
    scene sb359 with dssr
    ev "Hi."
    ev "I've got this bitch with me."
    scene sb360 with dssr
    b "How did that happen?"
    scene sb361 with dssa
    ev "I was at Nami's with Nadia."
    scene sb354 with dssr
    "Bella nods, but doesn't look at Eva."
    scene sb356 with dssr
    pause
    scene sb357 with dssr
    ev "And bitch..."
    scene sb362 with dssr
    ev "If we don't see each other before your next race..."
    ev "Be careful. Canyon races aren't a joke."
    scene sb363 with dssa
    ev "Qualify next year if necessary. Your time doesn't matter if you're dead."
    scene sb358 with dssr
    b "I'll manage."
    b "Thanks for bringing this bitch here."
    if BellaNonExclusive5x0 is True:
        scene sb364 with dssr
        ev "And... Use multiple condoms."
        ev "You don't want that anywhere near your skin."
    scene sb365 with dssr
    "You turn around and face Eva."
    scene sb366 with dssa
    d "Thanks for bringing me here, Eva."
    scene sb367 with dssb
    pause
    scene sb368 with dssa
    d "Tell me what he said."
    scene sb369 with dssa
    b "He-"
    scene sb368 with dssa
    d "And the tone of his voice. Little details that might give away what-"
    scene sb370 with vpunch
    b "Dude!"
    b "Shut up and listen!"
    scene sb371 with dssr
    pause
    scene sb372 with dssr
    b "He wants to see me... I don't have anymore details."
    scene sb373 with dssa
    d "How did he get your number?"
    scene sb374 with dssa
    b "I have no idea."
    if bellameet is True:
        b "What if Mila ratted us out?"
        scene sb375 with dssa
        d "For that to be even remotely possible, she would need to know that we did something in the first place."
    else:
        b "What if Mila ratted me out?"
        scene sb375 with dssa
        d "For that to be even remotely possible, she would need to know that you did something in the first place."
    scene sb376 with dssa
    b "I just don't get why they would sue her."
    b "It's obvious that she didn't do it."
    scene sb377 with dssr
    pause
    scene sb378 with dssa
    d "...I could think of something. But I'll need to test something first."
    d "Talk to the guy and see what happens."
    if bellameet is True:
        d "If they really knew it was us... We'd already be in cuffs."
    else:
        d "If they really knew it was you... You'd already be in cuffs."
    scene sb379 with dssa
    b "Yeah."
    scene sb380 with dssa
    d "Maybe he will just ask what your mother likes for dinner."
    scene sb381 with vpunch
    b "Don't ever say that again! You hear me cunt!?"
    scene sb382 with dssa
    "You smile at her."
    d "Keep me updated."
    scene sb383 with dssr
    d "Can you drive me back?"
    $ persistent.unlockedImageBellaCh5_4 = True
    if BellaNonExclusive5x0 is True:
        $ BelMilNMF5x0 = True
        scene sb384 with dssa
        b "No?"
        scene sb383 with dssa
        d "What do you mean 'No'?"
        #kisses you
        scene sb384 with dssa
        b "No way I'm driving you back."
        d "Stop fucking around and drive me back home."
        b "...Get in."
        scene sb663 with dssa
        b "The other side."
        d "Why?"
        scene sb664 with dssr
        b "You'll drive."
        scene sb665 with dssa
        d "Are you kidding me? I have never driven a car before."
        scene sb666 with dssa
        "She gets into the passengers side."
        scene sb667 with dssr
        "You get into the driver side."
        scene sb668 with dssr
        b "Alright... You see this?"
        scene sb675 with dssr
        b "This is the gear lever."
        b "That's how you change gears."
        scene sb670 with dssr
        d "What if I want to stay in one gear?"
        scene sb669 with dssa
        b "Then you're gonna kill the car."
        scene sb671 with dssa
        d "I think this monstrosity would benefit from a quick end."
        scene sb672 with vpunch
        b "Shut the fuck up and listen!"
        scene sb673 with dssr
        b "Put your foot on the clutch."
        d "Which one is it?"
        scene sb674 with dssa
        b "Left."
        b "Push it through and start the car."
        scene sb676 with dssr
        "The car starts, vibrates heavily and the loud exhaust pops."
        scene sb677 with dssa
        d "Oh boy..."
        scene sb678 with dssa
        b "I swear if you crash my car..."
        d "I'll kill us both."
        scene sb679 with dssa
        b "I don't trust you to drive this..."
        scene sb680 with dssr
        b "Now slowly release the clutch and it will roll forwards."
        scene sb681 with vpunch
        "The car jerks forward."
        scene sb682 with dssa
        pause
        scene sb683 with vpunch
        b "I SAID SLOWLY!"
        scene sb684 with vpunch
        d "I DID IT SLOWLY!"
        scene sb683 with vpunch
        b "OBVIOUSLY YOU DIDN'T OR IT WOULDN'T HAVE DIED!"
        b "Start it again."
        scene sb685 with dssa
        d "I can't properly move with your leg on mine!"
        scene sb686 with dssa
        b "There's no way I'll let you drive without me being able to reach the brake!"
        scene sb685 with dssa
        d "Alright- fuck this... I'm just gonna learn automatic."
        scene sb686 with dssa
        b "Stop being a bitch! The next time I'm gonna make you drive!"
        scene sb687 with dssa
        b "Move over, and I'll drive you to your shelter."
        scene sb688 with dssa
        d "Then let me get out! Why would you climb on me?!"
        scene sb689 with dssa
        pause
        scene sb690 with dssa
        pause
        scene sb691 with dssr
        "You get back into the passengers side."
        scene sb692 with dssr
        pause
        scene sb693 with dssa
        pause
        scene sb694 with vpunch
        $ play_playlist(playlist_Ch5_LostSoul)
        "Just as Bella is about to drive forward-"
        scene sb695 with dssa
        pause
        scene sb696 with dssr
        d "Police?"
        scene sb697 with dssa
        b "Mhm."
        scene sb696 with dssa
        d "...Is this car wanted?"
        scene sb697 with dssa
        b "Nope."
        scene sb698 with dssa
        pause
        scene sb699 with vpunch
        pause
        scene sb700 with dssa
        u "Is it a bad time?"
        scene sb701 with dssa
        b "What do you want?"
        scene sb702 with dssr
        u "Would you please get out of the vehicle?"
        scene sb703 with dssr
        b "What do you get out of harassing me? I should complain to your superiors."
        scene sb704 with dssa
        u "*Giggles* Ma'am, please cooperate or I will be forced to detain you."
        scene sb705 with dssa
        "Bella's lips curl in anger."
        scene sb706 with dssa
        "The officer peeks at you."
        scene sb707 with dssa
        u "I saw you on the drivers seat a few minutes ago, please show me your license."
        scene sb709 with dssr
        pause
        d "You didn't see me."
        scene sb708 with dssa
        u "I did."
        scene sb709 with dssa
        d "Good luck proving that."
        scene sb710 with dssa
        u "Follow me to my car."
        scene sb711 with dssa
        pause
        scene sb712 with dssr
        u "Give me your name."
        d "[name] Cyrus."
        scene sb713 with dssr
        u "Aww."
        scene sb714 with dssr
        u "An innocent little birdy."
        scene sb715 with dssr
        u "You should stay away from the wrong people."
        scene sb716 with dssa
        pause
        scene sb717 with dssa
        pause
        scene sb718 with vpunch
        "She smells you with some deep inhales."
        scene sb719 with dssa
        u "*Moans* You reek of trouble."
        scene sb720 with dssa
        pause
        scene sb721 with dssa
        u "Bella."
        scene sb722 with dssr
        u "*Giggles* We'll see each other again soon."
        stop music fadeout 3.0
        scene sb723 with dssr
        pause
        $ play_playlist(playlist_Ch5_ViceCity)
        scene sb724 with dssa
        pause
        scene sb725 with dssa
        d "What was that?"
        scene sb726 with dssa
        b "This stupid bitch has been on my ass for months now."
        b "She's a detective in a task force that specializes in illegal street racing."
        scene sb727 with dssa
        d "So she knows that-"
        b "Yes. But she can't prove it."
        d "Why you, out of all of them?"
        scene sb728 with dssa
        b "Because I'm Bella Von Halen."
        b "Imagine the fame she'd get if she brings down Amber Von Halen's daughter."
        scene sb729 with dssa
        d "You act like your Mom's a celebrity."
        scene sb730 with dssr
        b "In certain circles."
        scene sb731 with dssa
        d "She freaks me out... Especially because someone like her is a cop."
        scene sb732 with dssa
        b "She and her little sister are both totally fucked in the head."
        scene sb733 with dssr
        d "Who's her sister?"
        scene sb734 with dssr
        pause
        scene sb735 with dssa
        $ persistent.unlockedImageST_CH5_3 = True
        b "Melanie Ceril."
        scene sb736 with dssb
        pause
        d "Do you want to stay a little? Make out?"
        "She squints her eyes."
        scene sb736x with vpunch
        pause
        stop music fadeout 2.0
        scene black with Dissolve(2)
        $ play_playlist(playlist_AmbientBellchen)
        with Pause(.5)
        scene sb485a with dssb
        pause
        scene sb496x with dssr
        "Bella breathes heavily and moans."
        scene sb737 with dssr
        b "*Breathy whisper* I want you so bad..."
        scene sb738 with vpunch
        pause
        scene sb739 with dssr
        b "Do you think... Do you think beating you up might get you hard?"
        scene sb740 with dssa
        d "...No."
        scene sb741 with dssa
        b "Have you tried it?"
        scene sb742 with vpunch
        "She slams you backwards."
        b "Come on! Let's try it! I'm ready to do everything!"
        d "Bella... Why do you keep doing this to yourself?"
        d "You know-"
        scene sb743 with vpunch
        b "Because there's always a chance that it might work!"
        scene sb744 with dssa
        b "God..."
        scene sb745 with vpunch
        pause
        scene sb746 with dssr
        d "(Her grip is much stronger than usual. She must really be on edge.)"
        scene sb747 with dssr
        d "(I... I'd love to give her what she wants.)"
        scene sb748 with dssa
        b "...*Sigh* I'll drive you back."
        scene sb747 with dssa
        d "Not yet... Let's just lay like this for a while."
        scene sb749 with dssr
        pause
        scene sb750 with dssa
        $ persistent.unlockedImageR_CH5_3 = True
        b "Something else... Stop making fun of Eva's body."
        b "She already has to fight with it."
        d "Alright."
        d "You'll stop making fun of Mila. I'll stop making fun of Eva."
        d "Deal?"
        scene sb751 with dssa
        b "Deal."
        scene sb752 with dssr
        pause
        scene black with Dissolve(2)
        with Pause(.5)
        scene sb753 with dssb
        pause
        scene sb754 with dssa
        b "I need to go to the hairdresser..."
        scene sb755 with dssa
        d "I agree. You look horrible."
        scene sb756 with dssr
        pause
        scene sb757 with dssa
        pause
        play music "music/Suspense/Scott Buckley - Resonance.ogg"
        scene sb758 with vpunch
        b "What the... *Sigh*."
        scene sb759 with dssr
        pause
        scene sb760 with dssa
        pause
        scene sb761 with dssr
        u "I could spot this car a mile away."
        b "You're in my way, asshole."
        scene sb762 with dssr
        u "Bella, is that how you'd greet your friends?"
        scene sb766 with dssr
        b "Friends? I don't remember us being friends."
        b "I remember seeing you and your ugly Muppets lose multiple races."
        scene sb776 with dssr
        b "And with ugly I mean you."
        "He curls his lips."
        scene sb767 with dssa
        u "Oh, you know my offer still stands. We'll race and if I win we're going to fuck."
        scene sb768 with dssa
        b "Ugh! Not in a million years."
        scene sb763 with dssr
        u "Who's that?"
        "You can see his smile fade from his face as he realizes you're in the car."
        u "Don't tell me you've got a boyfriend now."
        scene sb769 with dssa
        b "I do."
        scene sb764 with dssr
        u "What does he drive?"
        scene sb765 with dssr
        d "I don't drive. I get chauffeured."
        scene sb775 with dssr
        u "Are you making fun of his social standing?!"
        scene sb776 with dssa
        d "(Two very bright lads.)"
        d "Yeah."
        scene sb764 with dssr
        u "How about this Bella... I'll fight him and whoever wins gets your ass."
        scene sb771 with dssr
        b "This guy is mentally retarded."
        d "I can tell."
        scene sb777 with dssr
        u "Get out!"
        scene sb773 with vpunch
        "Before you can reach for the door, Bella locks the car."
        scene sb774 with dssa
        pause
        scene sb770 with dssr
        b "You're starting to bore me... You've got three seconds to get away from the car."
        scene sb778 with dssa
        u "What? is he shitting himself?"
        scene sb779 with vpunch
        "Exactly three seconds later, Bella floors the pedal."
        scene sb780 with vpunch
        "The guy hits the ground."
        scene sb781 with dssa
        pause
        scene sb782 with dssb
        d "You hit him."
        scene sb783 with dssa
        "She laughs."
        scene sb784 with dssa
        stop music fadeout 2.0
        b "I warned them."
        scene sb786 with dssr
        $ play_playlist(playlist_Ch5_ViceCity)
        d "Who are they?"
        scene sb785 with dssa
        b "Some guys from the racing community."
        scene sb786 with dssa
        d "He seems to be into you."
        scene sb785 with dssa
        b "Lots of people are."
        scene sb786 with dssa
        d "Not gonna lie, I kinda enjoyed seeing his smile fade when he spotted me."
        scene sb787 with dssa
        b "He has a tendency to get jealous."
        b "Quite a few of them do."
        $ persistent.unlockedImageBellaCh5_5 = True
        if BellaNonExclusive5x0 is True:
            scene sb788 with dssa
            b "Which is why I'm not bringing you there."
            b "You'd only cause problems."
            scene sb789 with dssa
            d "Me? Causing problems? Please."
        else:
            scene sb789 with dssa
        d "You know, guys that put a lot of emphasis on their car are like horse girls."
        scene sb790 with dssa
        b "I agree."
        b "Most of them are kind of retarded."
        scene sb792 with dssa
        b "Still, I have friends in this community. Loyal friends I'd find nowhere else."
        scene sb791 with dssa
        d "Male and female?"
        scene sb792 with dssa
        b "Yes, both genders."
        scene sb793 with dssa
        d "I'm sure these guys will be mad the next time they see you."
        scene sb794 with dssa
        b "So?"
        b "I really don't care."
    else:
        scene sb384 with dssa
        b "No way I'm driving you back."
        d "Stop fucking around and drive me back home."
        b "Get in."
        scene sb663 with dssa
        b "The other side."
        d "Why?"
        scene sb664 with dssr
        b "You'll drive."
        scene sb665 with dssa
        d "Are you kidding me? I have never driven a car before."
        scene sb666 with dssa
        "She gets into the passengers site."
        scene sb667 with dssr
        "You get into the driver side."
        scene sb668 with dssr
        b "Alright... You see this?"
        scene sb675 with dssr
        b "This is the gear lever."
        b "That's how you change gears."
        scene sb670 with dssr
        d "What if I want to stay in one gear?"
        scene sb669 with dssa
        b "Then you're gonna kill the car."
        scene sb671 with dssa
        d "I think this monstrosity would benefit from a quick end."
        scene sb672 with vpunch
        b "Shut the fuck up and listen!"
        scene sb673 with dssr
        b "Put your foot on the clutch."
        d "Which one is it?"
        scene sb674 with dssa
        b "Left."
        b "Push it through and start the car."
        scene sb676 with dssr
        "The car starts, vibrates heavily and the loud exhaust pops."
        scene sb677 with dssa
        d "Oh boy..."
        scene sb678 with dssa
        b "I swear if you crash my car..."
        d "I'll kill us both."
        scene sb679 with dssa
        b "I don't trust you to drive this..."
        scene sb680 with dssr
        b "Now slowly release the clutch and it will roll forwards."
        scene sb681 with vpunch
        "The car jerks forward."
        scene sb682 with dssa
        pause
        scene sb683 with vpunch
        b "I SAID SLOWLY!"
        scene sb684 with vpunch
        d "I DID IT SLOWLY!"
        scene sb683 with vpunch
        b "OBVIOUSLY YOU DIDN'T OR IT WOULDN'T HAVE DIED!"
        b "Start it again."
        scene sb685 with dssa
        d "I can't properly move with your leg on mine!"
        scene sb686 with dssa
        b "There's no way I'll let you drive without me being able to reach the brake!"
        scene sb685 with dssa
        d "Alright- fuck this... I'm just gonna learn automatic."
        scene sb686 with dssa
        b "Stop being a bitch! The next time I'm gonna make you drive!"
        scene sb687 with dssa
        b "Move over, and I'll drive you to your shelter."
        scene sb688 with dssa
        d "Then let me get out! Why would you climb on me?!"
        scene sb689 with dssa
        pause
        scene sb690 with dssa
        pause
        scene sb691 with dssr
        "You get back into the passengers side."
        scene sb692 with dssr
        pause
        scene sb693 with dssa
        pause
        scene sb694 with vpunch
        $ play_playlist(playlist_Ch5_LostSoul)
        "Just as Bella is about to drive forward-"
        scene sb695 with dssa
        pause
        scene sb696 with dssr
        d "Police?"
        scene sb697 with dssa
        b "Mhm."
        scene sb696 with dssa
        d "...Is this car wanted?"
        scene sb697 with dssa
        b "Nope."
        scene sb698 with dssa
        pause
        scene sb699 with vpunch
        pause
        scene sb700 with dssa
        u "Is it a bad time?"
        scene sb701 with dssa
        b "What do you want?"
        scene sb702 with dssr
        u "Would you please get out of the vehicle?"
        scene sb703 with dssr
        b "What do you get out of harassing me? I should complain to your superiors."
        scene sb704 with dssa
        u "*Giggles* Ma'am, please cooperate or I will be forced to detain you."
        scene sb705 with dssa
        "Bella's lips curl in anger."
        scene sb706 with dssa
        "The officer peeks at you."
        scene sb707 with dssa
        u "I saw you on the drivers seat a few minutes ago, please show me your license."
        scene sb709 with dssr
        pause
        d "You didn't see me."
        scene sb708 with dssa
        u "I did."
        scene sb709 with dssa
        d "Good luck proving that."
        scene sb710 with dssa
        u "Follow me to my car."
        scene sb711 with dssa
        pause
        scene sb712 with dssr
        u "Give me your name."
        d "[name] Cyrus."
        scene sb713 with dssr
        u "Aww."
        scene sb714 with dssr
        u "An innocent little birdy."
        scene sb715 with dssr
        u "You should stay away from the wrong people."
        scene sb716 with dssa
        pause
        scene sb717 with dssa
        pause
        scene sb718 with vpunch
        "She smells you with some deep inhales."
        scene sb719 with dssa
        u "*Moans* You reek of trouble."
        scene sb720 with dssa
        pause
        scene sb721 with dssa
        u "Bella."
        scene sb722 with dssr
        u "*Giggles* We'll see each other again soon."
        stop music fadeout 2.0
        scene sb723 with dssr
        pause
        $ play_playlist(playlist_Ch5_ViceCity)
        scene sb724 with dssa
        pause
        scene sb725 with dssa
        d "What was that?"
        scene sb726 with dssa
        b "This stupid bitch has been on my ass for months now."
        b "She's a detective in a task force that specializes in illegal street racing."
        scene sb727 with dssa
        d "So she knows that-"
        b "Yes. But she can't prove it."
        d "Why you, out of all of them?"
        scene sb728 with dssa
        b "Because I'm Bella Von Halen."
        b "Imagine the fame she'd get if she brings down Amber Von Halen's daughter."
        scene sb729 with dssa
        d "You act like your Mom's a celebrity."
        scene sb730 with dssr
        b "In certain circles."
        scene sb731 with dssa
        d "She freaks me out... Especially because someone like her is a cop."
        scene sb732 with dssa
        b "She and her little sister are both totally fucked in the head."
        scene sb733 with dssr
        d "Who's her sister?"
        scene sb734 with dssr
        pause
        scene sb735 with dssa
        b "Melanie Ceril."
        $ persistent.unlockedImageST_CH5_3 = True
        scene sb736 with dssb
        pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb795 with dssb
    pause
    scene sb796 with dssr
    d "Again. Be careful with the Holgerson guy."
    d "And tell me before you go over."
    scene sb797 with dssa
    "She nods in a bored way."
    if BellaNonExclusive5x0 is True:
        scene sb798 with vpunch
        pause
        scene sb799 with dssa
        pause
        scene sb801 with dssa
        pause
        scene sb802 with dssa
        d "Bitch."
        scene sb803 with dssa
        pause
        scene sb804 with dssa
        "Her eyes follow you closely as you walk to the front door."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb805 with dssb
    m "Yes, I heard the car."
    scene sb806 with dssa
    n "See. I told you he'd be here any second."
    scene sb807 with dssr
    d "Hi."
    m "Hi."
    scene sb809 with dssa
    m "I've made some lasagna. It's in the oven."
    scene sb808 with dssa
    m "Nami and I will head to a boring book club."
    scene sb810 with dssr
    m "Go watch some TV. I saw a new Big Grey episode is airing."
    scene sb811 with dssa
    pause
    scene sb815 with dssr
    pause
    scene sb816 with dssa
    "Nojiko's eyes go back and forth between you and Nami."
    scene sb815 with dssa
    pause
    scene sb817 with dssa
    m "No... Why?"
    scene sb814 with dssa
    d "Well, it's always a good idea to invest into your education... by reading books about little Pandas."
    scene sb813 with dssa
    "She shoots a look at Nami."
    scene sb812 with vpunch
    n "He forced me to tell him!"
    n "He held multiple rolls hostage! I had no choice!"
    scene sb814 with dssa
    d "I'll take a quick shower, and I'm ready to go."
    scene sb818 with dssr
    pause
    scene sb819 with dssa
    pause
    scene sb820 with dssa
    n "...Awkward."
    scene sb821 with dssr
    pause
    scene sb822 with dssa
    n "So uh... how's work?"
    "Nojiko shakes her head slightly while staring at Nami."
    scene sb823 with dssa
    m "You have no idea what you have done."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch5_Cougar)
    scene sb386 with dssb
    pause
    scene sb387 with dssr
    n "Looks fancy."
    if NamiLove5x0 is False:
        scene sb388 with vpunch
        n "Yo, let's get ourselves a monocle."
    scene sb389 with dssa
    d "Who's hosting it?"
    n "No idea."
    scene sb390 with vpunch
    pause
    scene sb391 with dssa
    n "Oh shit."
    scene sb392 with dssa
    d "What?"
    scene sb391 with dssa
    n "We entered a cougars den."
    scene sb392 with dssr
    pause
    scene sb395 with dssr
    n "Oh... I get it now."
    n "Yeaaah, say the word and I'm getting you out of here."
    scene sb394 with dssa
    d "What's a cougar?"
    scene sb396 with vpunch
    u "Hello!"
    "A swarm of middle aged woman surround you and Nami."
    scene sb397 with dssr
    u "You must be [name] and Nami?!"
    scene sb398 with dssa
    u "He's so handsome!"
    scene sb399 with dssa
    u "If I was just a little younger!"
    scene sb400 with dssa
    u "*Giggles* Anna! Noji is going to kill you!"
    scene sb401 with dssa
    u "Give them some space you vultures!"
    scene sb402 with dssr
    pause
    scene sb403 with dssa
    n "Those are cougars."
    scene sb404 with dssa
    "You search for Nojiko..."
    scene sb405 with dssr
    "...And find her staring at you rather unwell."
    d "(I see... Horny, middle aged women.)"
    d "(They can be worse than teenage boys.)"
    scene sb406 with dssr
    "A tall, beautiful looking woman approaches you."
    scene sb407 with dssa
    mw "I am Jenna Willson. Nice to meet you [name]."
    scene sb408 with dssa
    mw "Ladies, we should definitely read something else next time, we don't want to bore our new members."
    scene sb409 with dssa
    mad "I'm Maddie Throne, nice to meet you."
    d "Hi, [name]... as known."
    scene sb410 with dssa
    anna "I'm Anna!"
    scene sb411 with dssr
    anna "You know who you should sit next to?"
    scene sb412 with dssa
    pause
    scene sb414 with dssr
    pause
    scene sb418 with dssr
    mika "Mikala, that's me."
    scene sb414 with dssr
    mika "Aww, Sasha and [name]."
    scene sb415 with dssa
    mika "Lovely."
    "You and Sasha share a very awkward look."
    scene sb417 with dssa
    pause
    scene sb419 with dssr
    m "Hey, hey, hey, don't embarrass the kids."
    scene sb420 with dssr
    "Nojiko walks across the room and sits down in her usual chair."
    scene sb421 with dssr
    pause
    scene sb422 with dssr
    pause
    scene sb423 with dssa
    pause
    scene sb424 with dssr
    pause
    scene sb425 with dssr
    pause
    scene sb426 with dssa
    n "Thanks!" #to Jen
    scene sb427 with dssa
    n "I think we're in a porno."
    scene sb428 with dssa
    d "You always think that."
    scene sb429 with dssa
    n "And this time I'm the cuckqueen. I'll be forced to watch from the side."
    scene sb430 with dssa
    n "But I can understand Noji now."
    scene sb431 with dssa
    n "It was a mistake to bring you here."
    n "Come I'll smuggle you out."
    scene sb432 with dssa
    d "No. It's too late for that."
    scene sb433 with dssa
    pause
    scene sb434 with dssa
    pause
    scene sb435 with vpunch
    "Nami gasps in shock and twitches wildly."
    scene sb436 with dssa
    kel "Hi. I'm Kelly."
    scene sb437 with dssr
    pause
    scene sb438 with dssr
    d "(Fancy. I should steal it.)"
    scene sb439 with dssr
    stop music fadeout 2.0
    pause
    $ play_playlist(playlist_Amber)
    scene sb440 with dssa #beyond
    pause
    scene sb441 with dssr
    pause
    scene sb442 with dssa
    am "Hello, I'm Amber."
    scene sb443 with dssa
    "You have no idea what to say and just awkwardly stare at her."
    scene sb444 with dssa
    d "Umm... I'm [name]. Nice to meet you?"
    scene sb445 with dssa
    d "(Oh, I see... She's protecting my privacy by acting like we don't know each other.)"
    scene sb446 with dssa
    am "I'm looking forward to having you here."
    scene sb447 with vpunch
    if bellameet is False:
        cl "How are your balls, dude?"
        scene sb448 with dssa
        am "Oh my god... Go away."
        scene sb449 with dssa
        cl "Sister, you should've seen what your daughter did to this poor, young man."
        scene sb451 with dssa
        "Amber rolls her eyes and goes away."
    else:
        cl "Oh? Isn't that Bella's boyfriend?"
        scene sb448 with dssa
        am "Claire. Shut up, okay?"
        scene sb450 with dssa
        cl "Ohh... Oh! I get it."
        scene sb451 with dssa
        d "And she's not my girlfriend."
    stop music fadeout 2.0
    scene sb452 with dssr
    pause
    $ play_playlist(playlist_Ch5_Cougar)
    scene sb453 with dssa
    n "Man, I think I dressed too slutty."
    scene sb457 with dssr
    rm "I'm Charlie, and let me welcome Nami and [name]."
    rm "And of course Adrianna."
    scene sb459 with dssa
    rm "Not all members are here today."
    scene sb495 with dssr
    n "Thanks for allowing us to join!"
    scene sb486 with dssr
    adri "...Yeah, so happy and I'm totally here on my own."
    scene sb477 with dssr
    "All eyes are now on you."
    scene sb478 with dssa
    d "Right... Provided the books are of interest."
    scene sb460 with dssr
    rm "Oh? Do you think our books would bore you?"
    scene sb461 with dssa
    d "I heard you're reading a book about a butterfly and a panda."
    scene sb462 with dssa
    rm "We are indeed."
    menu:
        "Pretty much sounds like 'I'm on my deathbed'":
            $ Deathbed5x0 = True
            scene sb463 with dssa
            "You hear a mixture of giggling and indignation."
            mw "I always said the book was boring..."
            scene sb465 with dssr
            rm "If it up to you, Jen, we would be reading some pornographic novel."
            mw "Mark my words, Charlie... The day will come when my vote wins."
            scene sb466 with dssr
            rm "But until then, we'll be reading something else."
        "I won't judge until I've read it.":
            $ WontJudge5x0 = True
            scene sb464 with dssa
            rm "Smart decision, boy."
            mw "He'll hate it."
            mw "Everyone here does."
            scene sb465 with dssr
            rm "As long as your proposals are rejected by the majority, you'll read what I give you."
    d "(There's quite some tension here. I shouldn't be surprised.)"
    scene sb468 with dssr
    d "(Little games of power between bored, middle aged women... This is a recipe for... interesting events.)"
    scene sb469 with dssr
    d "(I have to see how each woman here reacts to me... and then I can influence the right parts to strengthen my position.)"
    scene sb470 with dssr
    d "(And make this here a lot more enjoyable for me, Noji and Nami.)"
    scene sb472 with dssr
    pause
    scene sb467 with dssr
    rm "We're almost done with the book. Means, you three should just listen and get a general idea of how we do things here."
    scene sb476 with dssr
    "You notice a respectable amount of wine in the background."
    scene sb479 with dssr
    d "Pretend to like books for an excuse to drink wine?"
    scene sb471 with dssr
    anna "Pretty much that!"
    scene sb473 with dssr
    mad "He's not wrong..."
    scene sb474 with dssr
    sas "Some people here actually like books."
    scene sb475 with dssr
    kel "I'm with you, Sasha."
    scene sb467 with dssr
    rm "Nojiko, you didn't mention [name] was a troublemaker."
    scene sb480 with dssr
    d "If making a joke or speaking up is considered 'trouble', then it's a sign of an imbalance of power."
    scene sb487 with dssr
    d "One person that gives directions..."
    scene sb488 with dssa
    d "...and apparently decides what is and isn't allowed to be said."
    scene sb489 with dssa
    rm "I'm not so sure you'll fit in here with us."
    scene sb481 with dssr
    d "Does your position feel threatened?"
    scene sb550 with dssr
    m "[name]."
    scene sb490 with dssr
    rm "Why would I feel threatened by a little boy?"
    scene sb482 with dssr
    d "A power trip can do that to you."
    scene sb483 with vpunch
    mw "I love that boy!"
    mw "He fits right in with us!"
    scene sb1788 with dssr
    pause
    scene sb493 with dssr
    sg "Let's all calm down and proceed to read books... and drink lots of wine."
    scene sb494 with dssa
    sg "I'm Susan Gale."
    scene sb493 with dssa
    sg "You three should just listen today."
    scene sb497 with dssr
    n "Susan Gale? The Author?"
    scene sb498 with dssa
    sg "Yes."
    scene sb500 with dssa
    n "...*Whisper* Oh my gooooooddd...  A celebrity!"
    scene sb503 with dssr
    adri "Oh, you wrote the book about 'Why dildos are better than Man'."
    scene sb503x with dssa
    sg "Indeed."
    scene sb499 with vpunch
    n "Amazing piece of literature! I loved it!"
    scene sb497 with dssa
    sg "Thank you!"
    if Deathbed5x0 is True:

        scene sb508 with dssr
        "After your interaction with Charlie, Adrianna eyes you a little."
    scene sb549 with dssr
    "Nojiko shoots you a look."
    scene sb491 with dssr
    "Everyone gets a very generous glass of wine."
    scene sb492 with dssr
    n "*Whisper* This Charlie scares me."
    n "*Whisper* This is how I would imagine a vampire."
    n "*Whisper* When you're asleep... She'll fly through your open window disguised as a bat, transforms back, and sucks you dry."
    scene sb501 with dssr
    "Adrianna giggles."
    n "Oh. That came out wrong."
    scene sb510 with dssr
    "Susan clears her throat and starts reading the book."
    sg "The little panda said to the butterfly: 'Where are you going? The Summer festival is about to start.'"
    scene sb511 with dssa
    sg "But the butterfly didn't reply. His broken heart didn't let him. The butterfly fought to hold his tears back..."
    scene sb512 with dssa
    pause
    scene sb513 with dssa
    sg "'Why are you crying? The Panda asked. The Butterfly blushed.'"
    if NamiLove5x0 is True:
        scene sb514 with dssa
        n "*Whisper* We could be at home doing who knows what..."
        scene sb513 with dssa
        d "(Did she really just say that?)"
        "You peek over to the Cheeto, but her eyes are fixed at Susan, whose reading the book."
    scene sb515 with dssr
    pause
    scene sb516 with dssa
    sg "The butterfly wiggled it's way over and hugged the little panda-"
    scene sb517 with vpunch
    d "*Cough*!"
    scene sb518 with dssr
    "You continue to cough." #alle schauen
    scene sb519 with dssr
    d "*cough* S-sorry, wrong pipe..."
    scene sb520 with dssa
    sg "As I was saying, the little butterfly wiggled it's way over and hugged the little panda..."
    if NamiLove5x0 is False:
        scene sb527 with dssr
        n "*Whisper* Imagine a block of butter... with wings."
    else:
        scene sb528 with dssr
        pause
    scene sb521 with dssr
    rm "Sasha?"
    scene sb531 with dssa
    sas "I doubt that the author meant for such a complex explanation. The one we discussed last time."
    scene sb532 with dssa
    sas "People often read too much into minor things."
    scene sb522 with dssa
    rm "Susan?"
    scene sb523 with dssa
    sg "Sasha might be right but I doubt that the author didn't mean anything by it."
    m "It's hard to judge such a statement without knowing the authors personal life and circumstances."
    scene sb533 with dssr
    sas "Indeed."
    sas "It's in our nature to seek meaning in whatever life throws at us."
    scene sb534 with dssr
    mw "I'm with Sasha here... I don't see any deeper meaning."
    scene sb529 with dssr
    d "Imagine this place without alcohol."
    scene sb530 with dssa
    n "Oh god..."
    scene sb524 with dssr
    stop music fadeout 3.0
    rm "Adrianna?"
    scene sb504 with dssr
    $ play_playlist(playlist_GirlyCh4x)
    adri "Does the butterfly and the panda have a sexual relationship?"
    scene sb525 with dssr
    rm "W-what? No?"
    scene sb526 with dssa
    rm "Why would they?"
    scene sb535 with dssr
    mw "...The question should be..."
    scene sb536 with dssa
    mw "Why wouldn't they?"
    scene sb493 with dssr
    sg "I mean sometimes it does seem a little suspicious."
    scene sb542 with dssr
    cl "I agree. The way the butterfly swings it's wings so close to the panda's body."
    scene sb543 with dssa
    cl "I mean hello?! Make it even more obvious."
    scene sb544 with dssr
    am "*Whisper* Really?"
    scene sb552 with dssr
    kel "I think something as pure as this panda, would never-"
    scene sb546 with dssr
    anna "And what's up with all the wiggling?"
    anna "Why does the Butterfly wiggle all the time?"
    scene sb505 with dssr
    adri "It's trying to get laid."
    if Deathbed5x0 is True:
        scene sb506 with dssr
        pause
        scene sb507 with dssa
        pause
        scene sb508 with dssa
        pause
    scene sb547 with dssr
    mika "...Maybe it's true."
    scene sb548 with dssa
    m "No..."
    scene sb551 with dssr
    aliy "This explains a section from earlier in the book!"
    aliy "Ya'll remember when the butterfly watched the panda eating with another panda?"
    scene sb1092 with dssr
    adri "Maybe the butterfly is a cuckold?"
    scene sb553 with dssr
    kel "What's that?"
    scene sb509 with dssr
    adri "A person who likes to see their significant other get fucked by others."
    scene sb554 with dssr
    kel "That should be illegal. God does not-"
    scene sb537 with dssr
    mw "Like a voyeur... Dirty Butterfly."
    scene sb545 with dssr
    am "I wouldn't completely rule out, that if due to a previous trauma the butterfly might have suffered, a manifestation of a sexual fetish took place."
    scene sb538 with dssr
    sas "*Whispers* What is going on..."
    scene sb557 with vpunch
    rm "Okay! Enough! There's no such thing in this book!"
    rm "Back to the topic, please!"
    scene sb509 with dssr
    adri "I thought we were here to discuss books."
    scene sb558 with dssr
    rm "Yes! In an orderly and well-mannered fashion."
    scene sb559 with dssa
    rm "So please stop derailing the topic with such ridiculous thoughts."
    scene sb539 with dssr
    sas "...There are no ridiculous thoughts when it comes to a healthy discussion."
    scene sb540 with dssa
    sas "If one thought is deemed ridiculous... All are."
    scene sb541 with dssa
    "Charlie ignores Sasha and signals Susan to continue."
    scene sb560 with dssr
    pause
    scene sb561 with dssa
    sg "I'm totally lost now... Where was I?"
    scene sb562 with dssa
    sg "I can't stop picturing-"
    scene sb563 with vpunch
    rm "I don't want to hear it!"
    scene sb564 with dssa
    rm "We'll make a short pause... Everyone get their thoughts in order."
    scene sb555 with dssr
    kel "We can all just do a little prayer."
    mw "Kelly, drink some more wine... Your sober self makes me want to kill myself."
    scene sb556 with dssr
    kel "God does not look kindly on those who-"
    scene sb565 with vpunch
    stop music fadeout 4.0
    mw "Please! Somebody give her more wine!"
    scene sb567 with dssr
    d "(I should get in a few words with Noji.)"
    scene sb568 with dssr
    $ play_playlist(playlist_Ch5_Ghosts)
    m "Don't bullshit me! It's no coincidence that you came here today! You haven't been here in months!"
    m "So stay away!"
    scene sb568x with dssa
    "She gently moves a hair strand out of Noji's face."
    scene sb570x with dssa
    u "This isn't for you to decide."
    scene sb570 with dssa
    pause
    scene sb571 with dssa
    pause
    scene sb572 with dssr
    pause
    scene sb573 with dssa
    katie "Hi. I'm Katie."
    scene sb574 with dssa
    d "I'm [name]."
    scene sb574x with dssa
    katie "I'll see you around, [name]."
    d "(Noji and her seem to have some history. She's not happy at all.)"
    d "(She's got quite the presence, though.)"
    scene sb576 with dssr
    "Katie walks over to Nami and introduces herself."
    scene sb577 with dssa
    d "I hope you're not mad at me."
    scene sb579 with dssa
    m "I'm not."
    scene sb578 with dssa
    d "Maybe I have gone a little too-"
    scene sb580 with dssa
    m "I sometimes still think of you as a little boy that I need to protect."
    m "And considering what happened in the past, you can't blame me for that."
    scene sb581 with dssa
    m "But you're very much capable of doing it yourself."
    scene sb582 with dssa
    d "Is it true what I said?"
    scene sb581 with dssa
    m "Yes, Charlie controls the club."
    m "Many don't dare to speak up and just follow her along."
    scene sb582 with dssa
    d "What about you?"
    scene sb583 with dssa
    m "Charlie is my friend, but I speak up when necessary."
    scene sb584 with dssr
    n "You didn't speak up when she kept calling [name] a little boy."
    scene sb585 with dssa
    stop music fadeout 3.0
    m "If I had, Nami... Then [name] would've actually been a little boy."
    m "An adult that needed me to protect him."
    $ play_playlist(playlist_Ch5_Cougar2)
    scene sb586 with dssr
    rob "Hi!"
    scene sb587 with dssr
    mw "Hey Robin!"
    scene sb588 with dssa
    rob "Hi Jen!"
    scene sb589 with dssa
    rob "Hey Mom."
    scene sb590 with dssa
    rm "Robin, I thought you forgot about today."
    scene sb591 with dssa
    rob "I had to finish some papers."
    scene sb592 with dssr
    d "(So that's Robin's Mother...)"
    scene sb593 with dssr
    rob "Hey!"
    scene sb594 with dssa
    "You eye her for a moment..."
    d "Hi."
    scene sb595 with dssa
    n "Hey!"
    if RoRum is True:
        scene sb596 with dssa
        mw "Wait a second..."
        scene sb597 with dssa
        mw "Robin, you told us about a rumor going around at ZPR."
        scene sb598 with dssa
        mw "Is [name] the [name], Robin?"
        scene sb599 with dssa
        rob "Yeah..."
        scene sb600 with dssa
        "Charlotte shoots you a serious look."
        scene sb599 with dssa
        rob "It's just rumors... Wrong time, wrong place."
        scene sb601 with dssa
        rm "I hope that's true."
    scene sb602 with dssr
    rob "Hey!"
    scene sb603 with dssa
    sas "Hey."
    scene sb604 with dssa
    rob "I'm totally surprised to see [name]. I thought only Nami was joining."
    rob "What did I miss? Besides Nami, Adri and [name] joining."
    scene sb605 with dssa
    sas "[name] had an argument with your mother."
    scene sb606 with dssa
    rob "Oh."
    scene sb607 with dssa
    sas "Adrianna derailed the topic into a discussion about the sexual nature of the panda and butterfly's relationship."
    scene sb608 with dssr
    pause
    scene sb609 with dssa
    rob "*Whisper* They totally have one, right?"
    scene sb610 with dssa
    pause
    scene sb611 with dssr
    sas "What?"
    scene sb612 with dssr
    rob "I'll give you my thoughts on that later."
    scene sb643 with dssr
    n "So Robin!"
    n "What's your take? Is there any deeper meaning in this book?"
    scene sb613 with dssr
    rob "Hmm..."
    scene sb614 with dssa
    rob "It always depends on the chapter we're reading... I suddenly think 'Yes, there it is'... and then it's gone again."
    rob "Sasha and I had a discussion about it and... we came to the conclusion that there's no deeper meaning."
    scene sb644 with dssr
    n "I see."
    scene sb615 with dssr
    rob "It's so nice to have a male here again."
    scene sb616 with dssa
    sas "I disagree."
    scene sb617 with dssa
    d "I'm glad you're not the head of this club then."
    scene sb618 with dssa
    sas "You lack proper manners."
    sas "I doubt you can add anything worth while to this club."
    scene sb619 with dssr
    rob "Excuse her. She's a little on edge lately since the last two-"
    scene sb621 with dssa
    sas "I'm not."
    scene sb622 with dssa
    sas "I don't question [name]'s mental capacity... But I question his intentions. You've got no interest in books."
    scene sb620 with dssa
    d "Why else would I be here?"
    scene sb623 with dssa
    sas "You're bored? You're trying to prove something?"
    scene sb641 with dssr
    adri "Hey Sasha? Why are you talking about me?"
    scene sb624 with dssa
    sas "I'm not."
    scene sb642 with dssa
    adri "But that totally describes me."
    scene sb625 with dssr
    d "(I mean, she isn't wrong... I'm just here because Noji didn't want me here.)"
    scene sb626 with dssa
    d "I don't like your attitude, Sasha."
    scene sb642 with vpunch
    adri "Me neither!"
    scene sb626 with dssr
    d "And proper manners?"
    d "When did I act like a tool? All I did was question Charlie."
    scene sb627 with dssa
    sas "It's the way you did it. It could've been done a lot nicer without burning bridges."
    scene sb628 with dssa
    d "Yeah, but that would've been disingenuous."
    scene sb629 with dssa
    sas "Being polite isn't being disingenuous."
    scene sb630 with dssr
    sas "Make yourself a picture of the people before you start nonsense arguments that benefit no one."
    sas "Saying that Charlie is on a powertrip is hardly beneficial in any way... Except you want to stir up shit and make her feel worse."
    scene sb631 with dssa
    rob "*Whisper* He's not completely wrong."
    scene sb630 with dssa
    sas "Doesn't matter. We won't see him here again anyways. All he then accomplished was to make Charlie mad, which subconsciously will affect her actions in the future."
    scene sb633 with dssr
    d "I'm convinced that me speaking up will change this club for the better."
    scene sb632 with dssa
    "She shakes her head."
    scene sb634 with dssa
    d "You're too... Nah."
    d "Let actions speak for themselves. We'll get back to this."
    scene sb635 with dssa
    rob "So [name]... Do you have a favorite book or are you just getting into reading?"
    scene sb636 with dssa
    d "(She acts like nothing happened.)"
    d "I don't have a favorite, but I read a lot in the past."
    scene sb637 with dssr
    rob "Oh, which genre?"
    scene sb638 with dssa
    d "Mostly fantasy, biographies but also self improvement books."
    scene sb639 with dssa
    rob "Cool."
    rob "Sasha and I read a lot of romance and here and there a fantasy novel."
    scene sb640 with dssa
    rob "Sasha especially loves romance stories."
    scene sb645 with dssr
    n "I like... I have no idea... I never really got into reading."
    scene sb646 with dssa
    d "All you do is watch porn."
    scene sb647 with vpunch
    n "*Embarrassed* Bullshit! Dude!"
    scene sb648 with dssa
    stop music fadeout 3.5
    pause
    scene sb649 with dssr
    $ play_playlist(playlist_Ch1Bus)
    d "(Hmm, there's a little group... Let's see if I can lay a fundament of influence.)"
    d "(Time to turn every fiber in my body against me and turn on my charm...)"
    scene sb650 with dssr
    d "Good evening."
    scene sb651 with dssr
    mw "Ahh! [name]!"
    scene sb652 with dssa
    d "Miss Willson."
    scene sb828 with dssr
    d "Miss Gale."
    scene sb830 with dssr
    d "Miss Penelope."
    scene sb829 with dssr
    d "Miss Throne."
    scene sb653 with dssr
    mw "You do remember our names."
    d "It's hard to forget."
    scene sb833 with dssr
    sg "Oh my... A charmer."
    scene sb655 with dssr
    d "I'm not interested in making people like me."
    scene sb659 with dssa
    mw "We could tell... Charlie oof, not many would do that on their first day."
    pen "It was quite the show."
    d "May I ask you what you'd like to propose as the next book?"
    scene sb660 with dssr
    mw "Well..."
    mw "We're all adults here... and we'd like to read something more..."
    scene sb661 with dssa
    mw "Interesting."
    scene sb662 with dssa
    d "Pornographic."
    scene sb833 with dssa
    mw "Oh no, that's just Charlie's distorted view."
    scene sb831 with dssr
    pen "I guess that happens when a woman hasn't been touched in a long time."
    scene sb659 with dssr
    mw "If the fire stays out for too long... Everything may seem 'Pornographic.'"
    scene sb838 with dssr
    sg "We're just interested in some romance novels. They might feature some scenes of sexual intercourse but who says that's bad?"
    sg "It's human nature."
    scene sb831 with dssr
    pen "We're all like that, aren't we?"
    scene sb837 with dssr
    d "(...)"
    d "Sure."
    scene sb654 with dssr
    mw "The second I saw you, I knew you weren't a yes man."
    scene sb655 with dssr
    d "Where does Nojiko stand?"
    scene sb839 with dssr
    pen "Noji is one of us."
    pen "Sasha and Robin often refrain from voting."
    scene sb657 with dssr
    mw "I'm sure Robin would like to vote for us but doesn't want to risk the wrath of her mother."
    scene sb838 with dssr
    pen "Most here find it much easier to just let Charlie do... instead of arguing for hours."
    d "I don't like that approach."
    scene sb654 with dssr
    mw "We can tell, haha."
    scene sb845 with dssr
    d "(I bet if I now look over to Noji, I'll catch her looking over here.)"
    scene sb846 with dssa
    d "(Yup.)"
    scene sb841 with dssr
    d "(I've read about older women sometimes liking younger men... This could be the case here.)"
    scene sb842 with dssr
    d "(And it would make it extremely easy to spread my influence.)"
    d "(It's just a question of how far I'll decide to go.)"
    scene sb843 with dssa
    d "Can I get you four more wine?"
    scene sb844 with dssa
    sg "We'll never say no to more wine."
    scene sb847 with dssr
    pause
    scene sb848 with dssr
    d "(It's weird... Talking with them feels different... Weirdly familiar... I kinda enjoy it.)"
    scene sb849 with dssa
    d "(I don't get this familiar feeling when talking to girls at my age...)"
    scene sb850 with dssa
    n "Are you trying to tame the cougars?"
    scene sb851 with dssa
    d "I still don't know what cougar means."
    scene sb850 with dssa
    n "Older women preying on young men."
    scene sb851 with dssa
    d "Oh."
    scene sb852 with dssa
    d "Then yes, I'm trying to tame them."
    scene sb853 with dssa
    n "You wanna bang them?"
    scene sb854 with dssa
    d "Okay seriously... When did I ever want to bang anyone ever?"
    scene sb855 with dssa
    n "..."
    scene sb856 with dssa
    d "I want to spread my influence... Make this here a little more fun for us."
    d "And maybe get Noji on top."
    scene sb857 with dssa
    d "And before you say anything... I mean on top of the book club food chain."
    if NamiLove5x0 is False:
        stop music fadeout 2.0
        scene sb858 with dssa
        n "Suuure..."
    elif NamiLove5x0 is True:
        scene sb859 with dssa
        stop music fadeout 2.0
        n "I was about to say put me on top."
    $ play_playlist(playlist_RockPop)
    scene sb860 with vpunch
    u "Oh no! Am I late?!"
    scene sb861 with dssr
    u "I know, Charlie! I said I'd quit but here I am again. And yes, I won't change my mind, and no, I'll never be cool with your book choices."
    scene sb862 with dssr
    u "And no Anna, I didn't shoot any new movies."
    scene sb863 with dssr
    u "And of course I brought you a choco bar, Robin."
    scene sb864 with dssr
    rob "Thanks Emilia!"
    scene sb865 with dssa
    emilia "And I want to know everything about what went down with Jerry and Robert."
    scene sb866 with dssa
    emilia "Sasha, can't you stop seducing married men by literally just exisiting?!"
    scene sb867 with dssa
    pause
    scene sb868 with dssr
    rm "*Sigh* I thought we got rid of you for good, Emilia."
    scene sb869 with dssa
    emilia "My bestie talked me into staying."
    scene sb870 with dssa
    pause
    scene sb871 with dssa
    emilia "There she is... Look at her, aww."
    scene sb873 with dssr
    pause
    scene sb872 with dssa
    emilia "Heeey."
    scene sb874 with dssa
    m "Don't check your phone. I left you an angry voice message."
    scene sb875 with dssa
    emilia "Ohhh. Why? I said I'd come."
    scene sb874 with dssa
    m "That's not why."
    scene sb877 with dssa
    pause
    scene sb876 with dssa
    emilia "Oh."
    scene sb878 with dssr #maybe remove
    pause
    scene sb879 with dssa
    pause
    scene sb880 with dssa
    emilia "Would you look at that."
    emilia "A Zane is blessing us with her presence."
    emilia "How's William?"
    scene sb881 with dssa
    katie "You should ask him that."
    scene sb882 with dssr
    emilia "I wonder why you're here."
    emilia "It's been a year since you and Leia last came by."
    scene sb883 with dssa
    emilia "Is she here?"
    scene sb884 with dssa
    katie "No."
    scene sb885 with dssr
    emilia "Do you want to play a game?"
    scene sb886 with dssa
    katie "I don't."
    scene sb885 with dssa
    emilia "Let's play it anyways."
    scene sb888 with dssa
    emilia "Why would THE Katie Zane be here today after a year of absence..."
    emilia "Could it be that..."
    scene sb889 with vpunch
    n "Oh my god."
    n "Do you know who that is?"
    scene sb890 with dssa
    d "Who? The one that just came in?"
    scene sb891 with dssa
    n "Yes! The one that called Noji her bestie!"
    n "She's a retired pornstar and model."
    scene sb892 with dssa
    d "Okay?"
    scene sb893 with dssa
    n "From where does Noji know all these people?!"
    n "There are so many celebrities here!"
    n "Like this Anna is a figure skating champion! She was at the Olympics!"
    scene sb894 with dssa
    d "Do you know what I wonder about..."
    d "How long has Noji been coming here?"
    scene sb895 with dssa
    n "Forever. I remember her going to this club since we moved here."
    scene sb894 with dssa
    d "I'll be back in a second."
    scene sb896 with dssa
    pause
    scene sb897 with dssa
    emilia "Hi!"
    scene sb898 with dssa
    n "H-hi!"
    scene sb897 with dssa
    emilia "Aww! Why did your voice just crack, Nami?"
    n "You know my name?"
    scene sb899 with dssa
    emilia "Of course I do!"
    emilia "We haven't seen each other in a very long time."
    scene sb900 with dssr
    n "When did we see each other?"
    scene sb1672 with dssb
    pause
    d "Hey Kelly."
    scene sb1673 with dssa
    kel "Hi [name]!"
    scene sb1674 with dssa
    d "I have a super secret question for you."
    scene sb1675 with dssa
    kel "What is it?"
    scene sb1674 with dssa
    d "How long has Amber been a part of this club?"
    scene sb1676 with dssr
    kel "Oh. She was already a part before I joined."
    kel "And I joined last year in November."
    scene sb1677 with dssa
    d "Thanks."
    scene sb901 with dssb
    emilia "Wow, I usually only get recognized by guys."
    scene sb902 with dssa
    n "Don't tell Noji, though."
    scene sb903 with dssa
    d "Cheeto."
    scene sb904 with dssa
    emilia "Hello [name]."
    d "Hi."
    d "Do you have a minute?"
    scene sb905 with vpunch
    n "Don't be so rude!"
    scene sb906 with dssa
    pause
    scene sb907 with dssa
    d "I remember you."
    scene sb908 with dssa
    emilia "Don't tell me you watched those clips together."
    scene sb909 with vpunch
    n "Oh no! No!"
    scene sb910 with dssa
    d "You visited us on New Years Eve years ago."
    scene sb911 with dssa
    emilia "Wow, I'd never thought you'd remember that."
    scene sb912 with dssa
    d "I do remember because afterwards, I made some jokes about your breasts being as big as my head."
    "She laughs."
    scene sb915 with dssa
    d "You never came around afterwards, but you and Noji are apparently still bestie's."
    scene sb913 with dssa
    emilia "Yeah, we were just busy with work but Noji and I kept contact."
    scene sb917 with dssr
    d "(Bullshit.)"
    scene sb918 with dssa
    d "(The Cheeto doesn't pay enough attention to realize what's going on... But she's also lacking some information.)"
    scene sb919 with dssr
    d "(Noji knew Amber, but when they first met they acted like they didn't even know each other.)"
    scene sb920 with dssa
    d "(Is that the real reason why she doesn't want me here? Because she knew I might pay attention?)"
    scene sb921 with dssa
    d "Oh. Somebody's waiting for me."
    scene sb922 with dssr
    d "Here we go."
    scene sb923 with dssr
    mw "Thank you very much."
    scene sb924 with dssa
    mw "I didn't expect you to be such a nice boy."
    scene sb925 with dssa
    d "I'm not a nice boy."
    scene sb926 with dssr
    sg "I bet you aren't."
    scene sb927 with vpunch
    mw "Susan!" #giggles
    scene sb928 with dssr
    sg "*Giggles* What? I'm just joking around."
    scene sb929 with dssr
    pen "We're looking forward to having you and Nami here."
    scene sb930 with dssa
    d "Oh, Nami is amazing. She's like me. Doesn't take shit from anyone."
    scene sb931 with dssr
    mw "Maybe Noji did the right thing after all."
    scene sb932 with dssr
    d "Mh?"
    scene sb933 with dssr
    mw "Nevermind."
    scene sb934 with vpunch
    mw "Cheers."
    scene sb935 with dssr
    pause
    scene sb936 with dssa
    pause
    scene sb937 with dssa
    pause
    hide screen phone_hotspot
    scene black with Dissolve(1)
    with Pause(.5)
    stop music fadeout 2.0
    call screen SitChoice
    pause


label SitSasha:
    $ play_playlist(playlist_Ch5_ViceCity)
    $ SashaSit5x0 = True
    scene sb938 with dssr
    pause
    scene sb939 with dssa
    pause
    show screen phone_hotspot
    emilia "Oh no. Sasha's working her magic again."
    mika "See! They look so lovely together!"
    scene sb940 with dssa
    sas "Mikala, please refrain from that."
    mika "Bu-"
    scene sb941 with dssa
    sas "Otherwise, I'll get you kicked from this club."
    "Mikala presses her lips together and shyly looks away."
    scene sb942 with dssr
    pause
    scene sb943 with dssa
    pause
    scene sb944 with dssr
    sas "Would you mind sitting somewhere else?"
    sas "It's not that I don't want you here, it's just that the air in this room would be more comfortable if you were sitting a little further away."
    scene sb945 with dssa
    sas "And if you'd like to discuss something book related, we can do it from across the room."
    scene sb946 with dssa
    d "Thanks, but I'm good."
    scene sb947 with dssa
    pause
    d "You shouldn't care so much about what other people think."
    scene sb948 with dssa
    sas "I don't."
    scene sb949 with dssr
    d "Apparently you do."
    d "Or why does it bother you so much when they say we look lovely together?"
    scene sb950 with dssa
    sas "Because it's embarrassing, and I certainly don't think we look lovely together."
    scene sb951 with dssa
    d "Neither do I."
    d "You're way too stuck up."
    scene sb952 with vpunch
    sas "*Serious* I'm not stuck up."
    scene sb953 with dssr
    d "(Weak point spotted.)"
    scene sb954 with dssa
    d "Prove it by telling Nami that you hate rolls."
    scene sb955 with dssa
    sas "Listen..."
    sas "We can discuss the book, but I don't want to talk to you about personal topics."
    scene sb956 with dssa
    d "Great."
    d "What's the butterfly's personality?"
    scene sb957 with dssr
    pause
    scene sb958 with dssa
    sas "It's shy, and tries not to step on anyone's toes."
    scene sb959 with dssa
    "You let out a small laugh."
    scene sb960 with dssa
    d "Imagine it stepping on someone's toes with its little string like leg."
    scene sb961 with dssa
    sas "I think it could step on another butterflies foot."
    d "Why's it into the panda?"
    scene sb962 with dssr
    sas "It's never openly declared."
    sas "But they both come from different places, grew up with different socializations and... Opposites can attract each other."
    scene sb963 with dssa
    sas "But I don't see a future for them."
    scene sb964 with dssa
    d "I mean... It's a fucking Butterfly and a Panda."
    scene sb965 with dssa
    sas "And yet, they never lost hope."
    sas "They go against what's deemed morally accepted. They do what they want... What they think is right... No matter who might dare to lay rules upon them."
    scene sb966 with dssr
    pause
    scene sb972 with dssa
    d "Thanks."
    scene sb967 with dssr
    sas "Mh?"
    scene sb973 with dssr
    d "For giving me an insight into yourself or at least the self you'd like to be."
    scene sb968 with dssr
    sas "I didn't."
    scene sb972 with dssr
    d "As you said, we know nothing about their relationship..."
    scene sb973 with dssa
    d "It was your own observation, you immersed yourself and all what just spilled to the surface was you."
    scene sb969 with dssr
    sas "...Was that your intention?"
    scene sb970 with dssr
    d "No, I'm just observing. I have no interest in you besides discussing books."
    scene sb971 with dssa
    pause
    scene sb974 with dssa
    d "Say, why does this woman keep staring at me as if I'm so sort of threat."
    scene sb978 with dssr
    pause
    scene sb975 with dssr
    "Sasha says nothing, but shoots the woman a serious look."
    scene sb979 with dssr
    "For a while, the woman stares back at Sasha."
    scene sb980 with dssa
    "Until her shoulders relax, and she looks away into the room."
    scene sb975 with dssr
    d "Is she your bodyguard?"
    scene sb976 with dssa
    sas "I told you to stay on the topic of books."
    scene sb977 with dssa
    "Sasha grabs her wine, gets up, and walks over to Nojiko and Charlie."
    scene sb982 with dssr
    pause
    scene sb983 with vpunch
    "Jenna walks, no, almost sprints towards you."
    scene sb984 with dssa
    jen "Don't get your hopes up with our Sasha."
    d "I have no such interest in her."
    scene sb985 with dssa
    jen "You know... Our precious Sasha gets hit on a lot."
    jen "She's killed one marriage, and we had to kick two guys out not that long ago."
    scene sb986 with dssa
    d "I discussed the book with her, but then asked about that weird woman over there."
    scene sb981 with dssr
    jen "Inessa Petrova. That's Sasha's aunt and personal bodyguard."
    $ achievement.grant("SitWithSasha")
    $ achievement.sync()
    $ persistent.unlockedImageSasha5 = True
    jump ContinueBooky5x0

label SitCheeto:
    $ NamiSit5x0 = True
    $ play_playlist(playlist_Ch5_ViceCity)
    scene sb1625 with dssr
    pause
    show screen phone_hotspot
    if NamiLove5x0 is True:
        scene sb1626 with dssr
        pause
        scene sb1627 with dssa
    else:
        scene sb1628 with dssr
    n "The wine's good."
    scene sb1629 with dssa
    d "I agree."
    d "I'm a little bit tipsy."
    scene sb1630 with dssa
    n "This Katie makes Noji furious."
    scene sb1631 with dssa
    d "I've noticed."
    scene sb1630 with dssa
    n "You know her serious fight look... She's rocking it right now."
    scene sb1631 with dssa
    d "I mean look at this place... All these 'cougars' or what you called them are trying to top each other."
    d "This place here is probably more competitive than the upcoming basketball tryouts."
    scene sb1630 with dssa
    n "Yeah."
    n "Is that really Bella's Mom?"
    d "Yup."
    n "She's nice and has a super gentle voice."
    scene sb1633 with dssa
    n "...Talking about blonde bimbos..."
    n "Any news?"
    scene sb1632 with dssa
    d "Nope."
    n "Hmm..."
    if NiaDate5x0 is True:
        scene sb1634 with dssa
        d "I should probably tell you that I agreed to have some drinks with Nia in the near future."
        scene sb1636 with dssa
        n "Really? How so? I thought you disliked her."
        scene sb1635 with dssa
        d "Not anymore."
        d "And I have to admit that she hits some of my spots."
        scene sb1637 with dssa
        n "Huh? What spots?"
        scene sb1635 with dssa
        d "I like how she looks."
        if NamiLove5x0 is True:
            pass
        else:
            scene sb1638 with dssa
            n "Yeah, I like her look too."
            scene sb1637 with dssa
            n "Did she try anything?"
            scene sb1635 with dssa
            d "No, we sat close to each other, but nothing more."
    else:
        pass
    if Cheeto_Butt_Slap_4x5 is True:
        scene sb1639 with dssr
        n "...You're gonna tell Amber about... about... you know?"
        scene sb1640 with dssa
        d "In the next session."
        scene sb1641 with dssa
        n "Are you s-"
        scene sb1640 with dssa
        d "I made my decision... I have to do it."
        scene sb1642 with dssr
    else:
        scene sb1643 with dssr
    n "I'm gonna go get more wine."
    scene sb983 with vpunch
    "Jenna walks, no, almost sprints towards you."
    scene sb984 with dssa
    jen "Hey."
    d "Hi."
    scene sb986 with dssr
    d "Nami is sitting there."
    scene sb985 with dssa
    jen "I'll get back up when she returns."
    jump ContinueBooky5x0

label ContinueBooky5x0:
    scene sb987 with dssr
    jen "How's college?"
    scene sb988 with dssa
    d "It's fine."
    scene sb987 with dssa
    jen "Amber told us that you're Bella's project partner."
    scene sb988 with dssa
    d "Correct."
    scene sb989 with dssa
    jen "I love that girl."
    jen "Never ever have I seen such a dirty mouth before."
    scene sb990 with dssa
    d "She was here?"
    scene sb992 with dssa
    jen "Yes, for like one and half sessions."
    jen "She just came back for a second session to get drunk. She came in, got drunk, got up and left."
    jen "But I must admit that in the first session, she had some very interesting insights."
    jen "In the second session she was mostly arguing and shit talking Kelly."
    scene sb991 with dssr
    jen "On first glance Bella might not look like the brightest, but the girl has some brain."
    scene sb993 with dssa
    d "I doubt that."
    scene sb994 with dssa
    jen "You and Bella are just... partners?"
    if BellaNonExclusive5x0 is True:
        scene sb993 with dssa
        d "I assume Amber talked a little too much."
        scene sb994 with dssa
        jen "She didn't mention you, but I overheard that Bella was seeing someone."
        scene sb993 with dssa
        d "Well, could be me."
        scene sb995 with dssa
        jen "You must love drama."
        scene sb996 with dssa
        d "I don't. I prefer peace and silence."
        d "And the second Bella becomes an annoyance due to childish drama... She and I are done."
        scene sb997 with dssa
        jen "Ice cold."
        scene sb998 with dssa
        d "But we're not yet exclusive."
        scene sb997 with dssa
        jen "I see."
    else:
        scene sb993 with dssa
        d "Yeah, just partners."
        scene sb994 with dssa
        jen "She's so pretty... And there's nothing more at all?"
    menu:
        "I prefer woman a few years older than me.":
            $ MCMilfs5x0 = True
            scene sb999 with dssr
            d "I prefer woman a few years older than me."
            scene sb1000 with dssa
            "She doesn't say anything for a few moments."
            scene sb1001 with dssa
            jen "Oh? How much older?"
            scene sb1002 with dssa
            d "Around your age."
            "Jen just smiles."
            menu:
                "But I'm not talking about you specifically.":
                    $ NotJenna5x0 = True
                    scene sb1006 with dssa
                    pause
                    scene sb1007 with dssa
                    jen "Then who are you talking about?"
                    scene sb1008 with dssa
                    d "Someone else here has gotten my attention."
                    scene sb1009 with dssa
                    jen "I see."
                    scene sb1010 with dssa
                    pause
                    scene sb1011 with dssa
                    d "(I knew she'd react like this.)"
                    scene sb1012 with dssa
                    jen "So uh... Who's this someone else?"
                    scene sb1013 with dssa
                    d "Does it matter?"
                    scene sb1012 with dssa
                    jen "I'm just curious."
                    scene sb1014 with dssa
                    d "I'll keep it to myself for now."
                    d "If I told you, I'd risk the whole endeavor by you revealing it to the others."
                    "She flips her brows."
                "I'm talking about you, Jenna.":
                    $ JennaTalk5x0 = True
                    scene sb1003 with dssa
                    jen "Awww! How cute."
                    scene sb1004 with dssa
                    pause
                    scene sb1005 with dssa
                    jen "Maybe I can set you up with Robin."
        "Nope, nothing at all.":
            scene sb1001 with dssa
            jen "What a bummer."
            jen "But maybe we can set you up with Robin."
            scene sb1002 with dssa
            d "No thank you."
            scene sb1012 with dssa
            jen "What? Why not?"
            jen "Robin is such a sweet girl."
            scene sb1015 with dssr
            jen "Of course, there's her mother... But Robin turned out just fine considering the circumstances."
    scene sb1016 with dssr
    kel "Hello [name]."
    $ persistent.unlockedImageST_CH5_4 = True
    kel "I'd like to invite you to the church."
    scene sb1017 with dssa
    jen "Kelly, get the fuck away."
    scene sb1018 with dssr
    kel "You're invited too. God might forgive your sins."
    scene sb1019 with dssa
    jen "Might? Didn't you always say he will?"
    scene sb1020 with dssa
    kel "I'm not so sure anymore."
    scene sb1021 with dssa
    d "No thanks, Kelly."
    scene sb1022 with dssa
    kel "If you do change your mind [name], you know where to find me."
    scene sb1023 with dssr
    pause
    scene sb1024 with dssr
    jen "She's a nightmare when she's sober."
    scene sb1025 with dssr
    d "What happens when she drinks enough?"
    scene sb1026 with dssa
    jen "She loses her halo."
    jen "She becomes less annoying. But don't mistake her for an easy fling... even if she gets a little touchy... Which uhh... she does *shudders* She promised to not have sex before marriage."
    scene sb1029 with dssa
    d "I can see that she can become quite annoying, but I think you're unnecessarily rude to her."
    scene sb1028 with dssa
    jen "Yeah, this can come across wrong... You never witnessed the months, and I repeat... MONTHS, of her always berating me."
    scene sb1027 with vpunch
    jen "How I would face serious, no hellish, consequences if I didn't bring back the dress I stole."
    scene sb1030 with dssa
    "You glance over her expensive looking red dress."
    scene sb1031 with dssa
    jen "It's not this dress."
    scene sb1032 with dssa
    jen "I mean it's also stolen, yes... But not the dress we're talking about."
    scene sb1033 with dssa
    "She chugs down a respectable amout of wine in one go."
    scene sb1035 with dssa
    anna "Hey Jen! Emilia wants to see you."
    scene sb1036 with dssa
    jen "And why is that?"
    scene sb1037 with dssr
    anna "She said it's suuuuper important... You know about the... Thingy?"
    scene sb1038 with dssa
    jen "What thingy?"
    scene sb1039 with dssa
    anna "The thingy everyone keeps talking about... What really happened between Sasha and Robert."
    scene sb1040 with dssr
    jen "I'll be right back."
    scene sb1041 with dssa
    anna "Hi."
    scene sb1042 with dssa
    d "Hey."
    d "What really happened between Robert and Sasha?"
    scene sb1043 with dssa
    anna "Nothing. *Giggles*"
    scene sb1064 with dssr
    emilia "... but, how do I put this delicately..."
    emilia "By the end of the evening, the steak's juices weren't the only juices flowing."
    scene sb1065 with dssa
    "They laugh."
    scene sb1066 with dssa
    jen "Hey."
    scene sb1067 with dssa
    emilia "Hello Jen."
    jen "What's up?"
    scene sb1068 with dssa
    emilia "Not your ex husbands dick."
    jen "You had to go for that, huh? No warning, just- just straight in."
    scene sb1069 with dssr
    emilia "But seriously, I'm not sure what's up... So what's up?"
    scene sb1070 with dssr
    "Jenna let's out a sigh."
    scene sb1071 with dssa
    jen "Anna you little bitch."
    scene sb1072 with dssr
    adri "Why is it that these super religious girls always have gigantic tits?"
    scene sb1073 with dssa
    n "They always do, huh?"
    scene sb1074 with dssa
    adri "I think God tests them that way. See if with all the male attention, they can still maintain their virginity until marriage."
    n "Makes sense."
    scene sb1075 with dssa
    cl "And she's putting up a good fight."
    scene sb1076 with dssr
    n "I need to ask a friend of mine if she's religious."
    scene sb1077 with dssa
    adri "She has big tits?"
    scene sb1078 with vpunch
    n "Sooo big!"
    scene sb1079 with dssa
    adri "Maybe she's Jesus's daughter."
    scene sb1044 with dssr
    anna "And I never thought I'd actually win the gold medal! All those years of training finally paid off!"
    scene sb1045 with dssa
    d "Respect."
    scene sb1046 with dssr
    pause
    scene sb1047 with dssr
    d "(Okay, she's really into me and not nearly as restrained as the others.)"
    if NotJenna5x0 is True:
        scene sb1080 with dssr
        d "(And to no surprise... Jenna is peeking at us.)"
    menu:
        "Put your hand on Anna's.":
            $ AnnaSTG1 = True
            if NotJenna5x0 is True:
                $ JennaSTG1 = True
            scene sb1049 with dssa
            d "I could tell you do a lot of sports."
            scene sb1050 with dssa
            anna "Thank you!"
            scene sb1051 with dssa
            anna "I know I'm wearing this big sweater and it hides most of my body..."
            scene sb1052 with dssr
            d "Well, I'm sure someday you can show me a little more."
            d "(I need to be careful with how far I go. I don't actually want something to happen... Right?)"
            d "(I just want broaden my influence to strengthen my position.)"
            scene sb1054 with dssr
            "Anna squeezes your hand slightly and smiles at you."
            menu:
                "Take it further.":
                    $ AnnaSTG2 = True
                    scene sb1053 with dssr
                    "You squeeze her hand slightly too... Your fingers touch, rub and intertwine."
                    scene sb1081 with dssr
                    sg "I can't believe she's doing that... While Noji's here."
                    scene sb1082 with dssa
                    mad "I think it's just some innocent little touchy touch."
                    mad "I doubt Anna or [name] would actually do something inappropriate. That would be really questionable."
                    mad "She's more than double his age."
                    scene sb1083 with dssa
                    "Susan raises a brow and looks at Maddie amusingly."
                    scene sb1084 with dssa
                    sg "Jealous?"
                    scene sb1085 with vpunch
                    mad "Of course not."
                    scene sb1087 with dssa
                    jen "Let's stay over there."
                    sg "Why?"
                    scene sb1088 with dssa
                    jen "The last thing I want is Noji to quit the book club."
                    jen "I mean, I'd love to see Anna getting a well deserved whopping..."
                    jen "But let's be good girls once in a while and make sure Noji doesn't have to concern herself with this."
                    scene sb1055 with dssb
                    anna "I'd love to show you some of my tricks... I mastered every trick in the book, and my endurance on top- in the air... will leave you-"
                    scene sb1056 with dssa
                    anna "Gasping for air."
                    scene sb1057 with dssa
                    d "(Careful [name]...)"
                    scene sb1058 with dssa
                    d "Sure."
                    d "(So much for that...)"
                    scene sb1059 with dssa
                    anna "Let me type in my number... reaaaaal fast."
                    scene sb1060 with vpunch
                    pause
                    scene sb1061 with dssr
                    anna "Text me."
                    scene sb1062 with dssa
                    d "I might do that."
                "Don't take it further.":
                    "You remove your hand."
        "Don't put your hand on hers.":
            pass

    scene sb1089 with dssr
    rm "Alright."
    rm "Please take a seat and we'll continue."
    scene sb1090 with dssa
    rm "This time in an orderly fashion."
    scene sb1091 with dssa
    pause
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_GirlyCh4x)
    scene sb1095 with vpunch
    n "Which gives you... Scientifically proven... 3.35 seconds to pick up a roll that fell to the floor!"
    scene sb1096 with dssa
    n "EXCEPT! It's a crunchy roll! They're more resistant to damage and you have around 4.33 seconds!"
    scene sb1093 with dssa
    adri "Okay, but I want some special topping on my roll, why am I not allowed to put sprinkles on them?"
    scene sb1094 with dssa
    n "It's perversion to the highest degree! If it falls to the ground, you'll lose most of your sprinkles anyways!"
    scene sb1093 with dssa
    adri "Why do you expect it to fall to the floor in the first place?"
    scene sb1098 with dssr
    d "For a self proclaimed roll connoisseur you're pretty damn small minded."
    scene sb1097 with dssa
    n "I'll stick with tradition!"
    scene sb1102 with vpunch
    rm "It's a panda! He can eat it even after 3.5 seconds."
    scene sb1101 with dssa
    n "3.35!"
    scene sb1103 with dssa
    rm "Can we get back to the book?"
    scene sb1099 with dssr
    n "Mhm..."
    sg "The panda ate the roll he found on the ground."
    scene sb1100 with dssa
    n "*Muffled* Disgusting."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1678 with dssr
    anna "So I let the bathwater in and checked him for a hernia!"
    anna "Worst date ever!"
    scene sb1105 with dssr
    aliy "Nothing will ever top Charlie's Klaus date."
    scene sb1104 with vpunch
    rm "We're not going there again!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1117 with dssr
    sas "I didn't do anything."
    scene sb1118 with dssa
    emilia "Pheromones! That must be it!"
    scene sb1107 with dssr
    am "There might be more to it than what meets the eye."
    am "The fact that even Robert would dare to jeopardize his marriage to have a chance with Sasha, signals that there might be something psychological going on."
    scene sb1108 with dssa
    am "Maybe Robert was going through something we didn't know."
    scene sb1109 with dssr
    jen "We should squeeze Sasha out and make a perfume out of her."
    scene sb1125 with dssr
    kel "Sasha might just be blessed. Blessed by the lord himself to provide us with lots of beautiful children."
    scene sb1126 with dssa
    kel "Sasha, you should come with me to the church. We have a lot of proud Christian male members who would love to meet, marry and reproduce with you."
    scene sb1119 with dssr
    pause
    scene sb1110 with dssr
    jen "I can only advise all the married ladies here to keep their husbands far away from Sasha."
    emilia "You didn't flirt back at all?"
    scene sb1120 with dssr
    sas "I always just discuss the books and never do more."
    scene sb1121 with dssa
    sas "I ju-"
    scene sb1123 with dssa
    sas "I'd like to start a vote to ban male members."
    sas "[name] can stay but no more."
    scene sb1122 with dssa
    pause
    scene sb1124 with dssr
    "Nobody else raises their hand."
    scene sb1106 with dssr
    aliy "Close."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1128 with vpunch
    n "NGHGHH!"
    scene sb1129 with vpunch
    n "ARRRRGH!"
    scene sb1130 with dssr
    pause
    scene sb1131 with vpunch
    "Charlie slams Nami's arm on the table!"
    scene sb1132 with dssr
    n "Damn it!"
    scene sb1133 with dssr
    "Charlie claims her reward... The last wine flask."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1111 with vpunch
    jen "As if! Leia was totally responsible for it!"
    scene sb1114 with dssr
    katie "I don't recall."
    scene sb1111 with vpunch
    jen "Bitch! Just admit it!"
    jen "We would've never lost against your team!"
    scene sb1114 with dssr
    katie "We had a good team, a good coach, and I was at peak performance."
    scene sb1112 with dssr
    jen "Bullshit! Your teammates spent more time getting backshots from William than actually training!"
    scene sb1095x with dssr
    "Sasha and Adrianna share an awkward look."
    scene sb1115 with dssr
    katie "Whatever helps you cope."
    scene sb1116 with dssa
    katie "Loser."
    scene sb1113 with dssr
    "Jenna's fuming so hard, her body starts shaking a little."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1657 with dssr
    emilia "No. I only do Venus now."
    emilia "And as I said before... The woman with the highest potential to be a future pornstar in this room is-"
    scene sb1644 with vpunch
    rob "-Sasha?"
    scene sb1645 with dssa
    pause
    scene sb1658 with dssr
    emilia "Kelly."
    scene sb1660 with dssr
    kel "But why?"
    scene sb1661 with dssa
    emilia "...You have no idea why?"
    scene sb1662 with dssa
    kel "No."
    scene sb1659 with dssr
    emilia "You don't have two big ideas?"
    scene sb1663 with dssa
    kel "*Mumbles* Thus the heavens and the earth were completed in all their vast array..."
    scene sb1652 with dssa
    jen "Kelly... YOUR BOOBS!"
    scene sb1664 with vpunch
    kel "Oh!"
    kel "That's so..."
    scene sb1654 with dssr
    mad "How come you aren't pregnant yet, Kelly?"
    mad "You talk so much about Sasha getting eventually impregnated and blessing us with children..."
    mad "Why haven't you yet blessed us with your offspring?"
    scene sb1655 with dssa
    kel "I haven't found my husband yet."
    scene sb1656 with dssr
    mad "But you always say how your church has lots of fertile, god-fearing man."
    scene sb1665 with dssr
    kel "Yes... But... Umm... Yes..."
    scene sb1666 with dssa
    kel "But God is telling me that none of them are meant for me."
    scene sb1667 with dssa
    kel "Maybe he reserved them for Sasha."
    scene sb1646 with dssr
    sas "Kelly... Stop that. I'm serious."
    scene sb1653 with dssr
    adri "Kelly... Remember that she's a very talented martial artist..."
    adri "Antagonize Sasha a little more and you might meet your creator sooner rather than later."
    scene sb1647 with dssr
    kel "...You wouldn't hurt me, would you?"
    scene sb1648 with dssa
    sas "Then stop using me as a subject in your breeding fantasies..."
    scene sb1649 with dssa
    "Robin starts giggling."
    scene sb1650 with vpunch
    sas "Stop laughing!"
    scene sb1668 with dssr
    kel "I just want to add one last thing..."
    scene sb1669 with dssa
    kel "As being said in Genesis 1:28... 'Be fruitful and multiply'."
    scene sb1670 with dssa
    pause
    scene sb1671 with dssa
    kel "*Peeks at Sasha* Don't forget."
    scene sb1651 with dssr
    "Sasha's blue eyes pierce through Kelly's soul..."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    $ play_playlist(playlist_Ch5_ViceCity2)
    with Pause(.5)
    scene sb1134 with dssr
    rm "I'm done for today ladies."
    scene sb1136 with dssr
    rob "And Gentlemen."
    scene sb1135 with dssr
    rm "Oh, my bad. I forgot we now have a boy here."
    scene sb1137 with dssr
    rob "You shouldn't call him a boy. That's disrespectful."
    scene sb1138 with dssr
    pause
    scene sb1139 with dssr
    rob "Hey."
    scene sb1140 with dssr
    rob "Sooo uhh the thingy-"
    scene sb1141 with dssa
    d "I assume you're talking about the handcuff incident?"
    scene sb1142 with dssa
    rob "*Nods*"
    menu:
        "Let her off the hook... for a favor.":
            $ RobinOffHook5x0 = True
            $ RobinFavor5x0 = True
            $ achievement.grant("RobinFavorA")
            $ achievement.sync()
            scene sb1143 with dssa
            d "We're cool."
            d "I spoke to Nadia and Zara... and I told them that I don't hold a grudge."
            d "I'm not some little bitch. In the end, Nadia and Zara satisfied their need for revenge with- an admittedly pathetic attempt."
            scene sb1145 with dssa
            d "And you don't owe Zara anymore."
            d "But... To make up for it... You now owe me a favor."
            scene sb1144 with dssa
            rob "Thanks! And yes! I'll make it up to you! You'll see!"
            scene sb1146 with dssa
            pause
        "Let her off the hook.":
            $ RobinOffHook5x0 = True
            scene sb1145 with dssa
            d "We're cool."
            d "I spoke to Nadia and Zara... and I told them that I don't hold a grudge."
            d "I'm not some little bitch. In the end, Nadia and Zara satisfied their need for revenge with- an admittedly pathetic attempt."
            d "And you don't owe Zara anymore."
            scene sb1144 with dssa
            rob "Thank you! I'm really glad to hear it!"
        "Don't let her off the hook.":
            $ RobinOffHook5x0 = False
            scene sb1142 with dssa
            d "Robin... Just no."
            scene sb1148 with dssa
            rob "I'm so sorry!"
            rob "I really didn't mean to worry you!"
            scene sb1142 with dssa
            rob "I'll make it up to you."
            scene sb1150 with dssa
            d "Don't bother."
            scene sb1151 with dssr
            pause
            scene sb1152 with dssa
    menu:
        "Ask Sasha for a book recommendation.":
            if RobinOffHook5x0 is False:
                d "Sasha, apparently you read a lot... Do you have any recommendations?"
                scene sb1153 with dssa
                sas "I don't."
            else:
                $ SashaBook5x0 = True
                d "Sasha, apparently you read a lot... Do you have any recommendations?"
                scene sb1154 with dssa
                sas "It's Only Love."
                scene sb1155 with dssa
                d "Sounds like a book full of romance."
                scene sb1156 with dssa
                sas "I guess you'll have to find out."
        "Don't ask her.":
            pass
    if RobinOffHook5x0 is True:
        $ RobinBookInvite5x0 = True
        scene sb1157 with dssa
        rob "When a new book gets voted in, you and Nami should join me and Sasha afterwards."
        rob "We'll discuss it and share theories."
        scene sb1158 with dssr
        n "Thanks! We'll see."
        scene sb1159 with dssa
        pause
        scene sb1160 with dssa
        d "*Whisper* We're not gonna do that, right?"
        scene sb1161 with dssa
        n "*Whisper* Of course not."
    scene sb1162 with dssr
    "While Noji and Nami are still immersed in various conversations, you take the liberty to walk up the stairs to explore the upper areas."
    "Mostly to get away from their obnoxious, half-drunk laughter."
    stop music fadeout 2.0
    scene sb1163 with dssr
    pause
    play music "music/Suspense/A.W - Darkness Inside.ogg"
    scene sb1164 with dssr
    "You feel something creep up from inside..."
    scene sb1165 with dssa
    "Sweat starts pouring down your face, your heart rate increases significantly... Cortisol and adrenaline flood your body."
    scene sb1166 with dssr
    d "*Breathing heavily* (N-not here!)"
    scene sb1167 with dssb
    pause
    scene sb1168 with dssa
    d "(This one's bad- really fucking bad!)"
    scene sb1169 with dssr
    d "(I need to get out of here!)"
    scene sb1170 with dssr
    "You look around for some sort of exit."
    d "(Could I just jump down?)"
    scene sb1171 with dssb
    "The air feels stale and devoid of oxygen."
    scene sb1172 with dssa
    pause
    scene sb1173 with dssa
    pause
    scene sb1174 with dssr
    pause
    scene sb1175 with dssa
    "She pulls out a little unmarked bottle..."
    scene sb1176 with dssa
    pause
    scene sb1177 with dssa
    "She gently puts it on your tongue."
    scene sb1178 with dssa
    pause
    scene sb1179 with dssa
    sas "It takes a second..."
    if RobinOffHook5x0 is True:
        scene sb1180 with dssr
        "She gently squeezes your hand in a rhythmic beat."
        scene sb1181 with dssr
        pause
        scene sb1182 with dssb
        stop music fadeout 3.0
        pause
        $ Sertraline = True
        scene sb1183 with dssr
        $ play_playlist(playlist_AmbientCheeto)
        sas "Better?"
        "You nod."
        scene sb1184 with dssr
        pause
        scene sb1185 with dssr
        pause
        scene sb1186 with dssr
        d "...Where can I get these pills?"
        scene sb1187 with dssa
        sas "From a pharmacy."
        scene sb1189 with dssa
        d "No shit..."
        scene sb1191 with dssa
        pause
        scene sb1188 with dssa
        sas "They only help with the symptoms."
        scene sb1190 with dssa
        d "...Why do you have them?"
        scene sb1192 with dssa
        "Her gaze turns cold and she averts it."
        scene sb1193 with dssa
        d "Thanks."
        d "But I still need the name of those pills."
        scene sb1194 with dssa
        sas "Sertraline."
        scene sb1195 with dssa
        "You nod... and leave."
        scene sb1196 with dssr
        d "(This one was different from the others... So strong... It felt like my heart was going to burst.)"
        d "(I need to talk to Amber about this.)"
        $ persistent.unlockedImageSasha6 = True
    else:
        scene sb1182 with dssb
        stop music fadeout 3.0
        pause
        scene sb1197 with dssa
        "She gets up without saying another word."
        scene sb1198 with dssr
        d "(This one was different from the others... So strong... It felt like my heart was going to burst.)"
        d "(I need to talk to Amber about this.)"
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1199 with dssr
    pause
    scene sb1200 with dssa
    m "I saw it wasn't really your thing, [name]."
    scene sb1201 with dssa
    d "Noji..."
    d "If you try to drive me away again, I'm going to engage in coitus with Anna- or Jenna- Or both."
    scene sb1202 with vpunch
    m "WHAT?!" #nami im bg like OH BOY
    scene sb1203 with dssa
    $ persistent.unlockedImage_BookClub = True
    n "*Excited* Oh booooy."
    scene sb1204 with dssa
    d "Do you think I'm stupid?"
    scene sb1205 with dssa
    m "Of course not!"
    m "But [name] you-"
    scene sb1206 with dssa
    d "It's obvious that you don't want me there because of them."
    scene sb1207 with dssa
    m "That's not-..."
    scene sb1208 with vpunch
    m "Okay! Fine! Yes, I don't want you there because of them!"
    scene sb1209 with dssa
    d "Well, tough luck."
    d "You said it yourself, I'm an adult... Not a little boy that needs protection."
    scene sb1210 with dssa
    n "You should probably use protection, though."
    scene sb1211 with vpunch
    pause
    scene sb1212 with dssa
    n "..."
    scene sb1213 with dssr
    d "Sorry Noji, I'll stay."
    scene sb1214 with dssa
    m "It doesn't matter what I say, you won't change your mind anyways."
    scene sb1215 with dssa
    d "Correct."
    stop music fadeout 2.5
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch5_Sad_Cheeto)
    scene sb1216 with dssb
    pause
    scene sb1217 with dssr
    pause
    scene sb1218 with dssa
    d "Cheeto, don't wait for us."
    scene sb1219 with dssa
    n "No no, it's fine. I've got nowhere to be."
    scene sb1220 with dssa
    d "Cheeto... Let me speak to Noji alone."
    scene sb1221 with dssa
    n "Oh... Okay."
    scene sb1222 with dssb
    pause
    scene sb1223 with dssr
    d "I don't think you know how much my depression affects me."
    scene sb1224 with dssr
    m "You need to be a little more specific [name]... You don't really talk to me... I can only assume, and if I assume the wrong thing... It's going to be weird."
    scene sb1225 with dssr
    pause
    scene sb1226 with dssa
    d "About sex."
    scene sb1228 with dssa
    m "Oh."
    scene sb1227 with dssa
    m "Oh I... Umm... I figured as much."
    m "You never left any traces... I suspected it."
    m "Not like- others in the house..."
    scene sb1229 with dssa
    m "It's just that they can be like vultures with no inhibitions... They-"
    scene sb1230 with dssa
    d "It's okay."
    d "I can handle them."
    scene sb1231 with dssr
    m "..."
    scene sb1232 with dssa
    m "Let's go inside and I'll give you a massage."
    m "It's been a while."
    scene sb1233 with dssr
    pause
    scene sb1234 with dssr
    n "I had no key..."
    scene black with Dissolve(2)
    with Pause(.5)
    jump Ratmek5x0

label Ratmek5x0:
    scene sb1235 with dssb
    pause
    scene sb1236 with dssa
    "You hear something unusual as you approach the entrance to the living room."
    d "Do you hear that?"
    scene sb1237 with dssa
    "Nojiko and Nami try to listen..."
    m "Hear what?"
    scene sb1238 with dssa
    stop music fadeout 2.5
    pause
    scene sb1239 with dssr
    $ play_playlist(playlist_RockPop)
    d "Hear that."
    scene sb1240 with vpunch
    m "OH MY GOD!"
    scene sb1241 with vpunch
    n "THEY ARE EVERYWHERE!"
    scene sb1242 with dssr
    d "I thought they were only outside."
    scene sb1243 with dssr
    d "Who are you calling?"
    scene sb1244 with dssa
    m "*Stressed* An exterminator!"
    scene sb1245 with dssr
    n "I had heard them before in the wall!"
    scene sb1246 with dssa
    pause
    scene sb1247 with dssa
    n "It all makes sense now!"
    scene black with Dissolve(1)
    with Pause(.5)
    scene sb1254 with dssr
    n "Yo bitches! I'm back!"
    scene sb1255 with dssa
    n "Nadia! Get some tranq arrows ready! We're gonna get that dark featherlight before Nia comes on!"
    scene sb1256 with dssa
    pause
    scene sb1257 with dssa
    pause
    scene sb1258 with dssa
    n "What the-"
    scene sb1248 with vpunch
    n "MH?! YOU WANT SOME?!"
    scene sb1249 with dssa
    n "N-not you!"
    scene sb1250 with dssa
    n "Yes! You there!"
    scene sb1251 with dssa
    n "Come get ya self some, bibi!"
    scene sb1252 with vpunch
    with Pause(.5)
    scene sb1253 with vpunch
    n "*Runs away screeching*"
    stop music fadeout 2.5
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch5_ViceCity)
    scene sb1259 with dssb
    pause
    scene sb1260 with dssr
    dg "Good evening. I'm David Goggy, pest control."
    dg "I'll check out the house."
    scene sb1261 with dssr
    dg "Please wait outside."
    scene sb1262 with dssr
    d "I always saw them at the front porch..."
    scene sb1263 with dssr
    d "(Bella would never let me live that down... I'm actually living in a fucking garbage can.)"
    scene sb1264 with dssr
    pause
    scene sb1265 with dssr
    nic "Hey. I came as fast as I could."
    scene sb1266 with dssa
    m "Thanks for coming."
    scene sb1265 with dssa
    nic "Of course."
    scene sb1267 with dssa
    nic "How bad is it?"
    scene sb1268 with dssa
    n "BAD!"
    n "They had sleeper cells everywhere! And now we're being invaded!"
    scene sb1269 with dssa
    dg "The house needs to be quarantined."
    scene sb1270 with dssa
    m "Oh god..."
    scene sb1271 with dssa
    nic "Can we get to the clothes?"
    scene sb1272 with dssa
    dg "If you don't mind stepping through an army of mice."
    nic "Alright. Let's fill a few bags."
    scene sb1273 with dssr
    dg "Also, beware. There's a little mouse in there that's unreasonably aggressive."
    scene sb1274 with dssa
    dg "I wonder what got into that little fellow."
    scene sb1275 with dssa
    pause
    scene sb1276 with dssa
    nic "Zara? Get your car and drive over here. I sent you the address. Thanks."
    scene sb1277 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    if BellaNonExclusive5x0 is True:
        scene sb1734 with dssr
        pause
        scene sb1735 with dssr
        pause
        scene sb1736 with dssr
        pause
    else:
        scene sb1734t with dssr
        pause
        scene sb1735t with dssr
        pause
        scene sb1736t with dssr
        pause
    if BellaNonExclusive5x0 is True:
        scene sb1737 with dssr
        d "...That fucking bitch stole the Teddy."
    else:
        scene sb1736t with dssr
        pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1278 with dssb
    pause
    scene sb1279 with dssr
    za "What's going on?"
    scene sb1280 with dssa
    nic "They have a rodent infestation."
    scene sb1281 with dssa
    za "Eww."
    scene sb1282 with dssa
    za "Are they coming to stay at our place?"
    scene sb1283 with dssa
    nic "Yes."
    scene sb1284 with vpunch
    za "Alrighty!"
    scene sb1285 with dssr
    pause
    scene sb1286 with dssa
    pause
    scene sb1287 with vpunch #redo the previous 2
    pause
    scene sb1288 with dssr
    d "Hi."
    scene sb1289 with dssa
    za "It's so cool that you're moving in!"
    scene sb1290 with dssa
    d "We're not moving in, we're just staying for a few days."
    scene sb1289 with dssa
    za "We'll see about that!"
    scene sb1290x with dssr
    pause
    scene sb1291 with dssa
    d "...What are you doing?"
    scene sb1292 with dssa
    pause
    scene sb1293 with dssr
    d "I liked us better as soon-to-be enemies."
    scene sb1294 with dssa
    za "And now we're roomies!"
    scene sb1295 with dssr
    d "Why do you even sound so happy?"
    scene sb1296 with dssa
    za "We can train! ALL! DAY! LONG!"
    scene sb1297 with dssr
    d "*Mumbles* Oh boy..."
    scene sb1298 with dssr
    za "Do you need a hand, Nami?"
    scene sb1299 with dssa
    n "I'm good, thanks."
    $ persistent.unlockedImageST_CH5_5 = True
    if NamiLove4x5 is True:
        scene sb1300 with dssr
        n "...Why are you on his back?"
        scene sb1301 with dssa
        za "I don't know."
        za "He kneeled down and I let my intrusive thoughts win."
        scene sb1302 with dssa
        n "Mhhmmm..."
    scene sb1303 with dssr
    pause
    scene sb1304 with dssr
    d "*Sigh*"
    scene sb1305 with dssr
    d "(I don't want to leave...)"
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1306 with dssb
    nic "Ready?"
    scene sb1307 with dssa
    m "Yes."
    m "Thanks a lot again."
    nic "Always."
    scene sb1308 with dssr
    pause
    scene sb1309 with dssr
    nic "Hey."
    nic "Are you okay, [name]?"
    scene sb1310 with dssa
    d "Yeah."
    scene sb1311 with dssa
    nic "I know this situation is hard... Leaving your home is never easy."
    nic "I lost mine to a fire when I was a little younger than you."
    scene sb1312 with dssa
    d "I'm sorry to hear that."
    scene sb1313 with dssa
    nic "Nobody got hurt, but the sentimental value we give inanimate objects close to us is just as real."
    nic "It's gonna be alright."
    scene sb1314 with dssa
    nic "Come."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1315 with dssb
    nic "I'll get your things up to your rooms."
    scene sb1316 with dssa
    m "Nami, come and help us."
    scene sb1317 with dssa
    pause
    if NamiLove4x5 is True:
        scene sb1318 with dssa
        n "Uuhhh... Zara? We could need a hand."
        scene sb1319 with dssa
        za "Oh uh- I'll be with you in a minute or two."
        scene sb1320 with dssr
        pause
    scene sb1321 with dssr
    pause
    scene sb1322 with vpunch
    za "Hey."
    scene sb1323 with dssr
    za "Why are you so down?"
    scene sb1324 with dssa
    d "...Having to leave the place where you feel safe doesn't leave you in the best mood."
    scene sb1325 with vpunch
    za "I have an idea!"
    scene sb1326 with vpunch
    za "Let's go!" #grabs your hand
    za "We'll change into some sporty clothes!"
    d "I'm not in the mood to train."
    scene sb1327 with dssr
    za "Oh. We're not training..."
    stop music fadeout 2.5
    scene black with Dissolve(2)
    with Pause(.5)
    jump ZaraBasketball5x0

label ZaraBasketball5x0:
    $ play_playlist(playlist_Ch5_Zara)
    scene sb1328 with dssb
    pause
    scene sb1329 with dssr
    za "Have you ever played street basketball?"
    scene sb1330 with dssa
    d "Nah."
    scene sb1331 with dssa
    za "The most important rule is... No Blood? No Foul!"
    d "I like that."
    scene sb1332 with vpunch
    pause
    scene sb1333 with dssa
    pause
    scene sb1334 with dssa
    za "...I slipped."
    scene sb1335 with dssr
    za "It's 21 points exactly. If you go over, it resets to 15."
    scene sb1336 with dssa
    d "Alright... Let me give you a beating."
    scene sb1337 with dssr
    pause
    scene sb1338 with dssa
    pause
    scene sb1339 with vpunch
    pause
    scene sb1340 with dssr
    d "I was about to ask you if you were ready... But I guess that answers it."
    scene sb1341 with dssa
    za "I'm so gonna wipe the floor with you..."
    scene sb1342 with vpunch
    pause
    scene sb1343 with vpunch
    pause
    scene sb1344 with vpunch
    pause
    scene sb1345 with dssr
    pause
    scene sb1346 with dssa
    za "Do a half court!"
    scene sb1347 with dssa
    pause
    scene sb1348 with vpunch
    za "Nice!"
    scene sb1349 with dssr
    za "Aww, look at your little smile!"
    scene sb1350 with dssa
    d "Shut up."
    scene sb1351 with vpunch
    "She tackles you backwards with full force."
    scene sb1354 with dssr
    pause
    scene sb1355 with dssa
    za "That was for the headshot!"
    scene sb1356 with dssa
    d "That's fair."
    scene sb1357 with dssr
    pause
    scene sb1358 with dssr
    "The tall flood lights turn off."
    scene sb1359 with dssa
    pause
    scene sb1360 with dssr
    u "Hi."
    u "Do you guys wanna play against us?"
    "You and Zara share a look."
    za "Sure!"
    za "Just a warning, for us it's all or nothing."
    scene sb1361 with dssr
    u "Good, we see it the same way."
    scene sb1362 with dssr
    u "My name's Patrick."
    scene sb1363 with dssr
    pat "And this is my girlfriend Louise."
    scene sb1366 with dssr
    za "I'm Zara and this is [name]."
    scene sb1364 with dssr
    lou "Are you a couple?"
    scene sb1365 with dssa
    za "No, we're just friends."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1367 with dssb
    pause
    scene sb1368 with dssa
    pause
    scene sb1369 with vpunch
    $ persistent.unlockedImageST_CH5_6 = True
    "Her hand accidentally slaps against your junk."
    lou "Sorry."
    scene sb1370 with vpunch
    pause
    scene sb1371 with dssr
    d "That was a good pass."
    scene sb1372 with dssa
    pause
    scene sb1373 with dssa
    "You, Zara and the other couple play for almost 30 minutes."
    scene sb1374 with dssr
    pause
    scene sb1375 with vpunch
    pause
    scene sb1376 with vpunch
    pause
    scene sb1377 with dssa
    "Louise makes the basket beautifully."
    scene sb1378 with dssr
    "The fadeaway causes her to fall into you."
    scene sb1379 with dssa
    "She grins."
    scene sb1380 with dssr
    pause
    scene sb1381 with dssa
    pause
    scene sb1382 with dssr
    pause
    scene sb1383 with dssa
    "You put some healthy distance between you and her."
    scene sb1384 with dssr
    za "That small girl is much better than I expected... She's so fast."
    scene sb1385 with dssa
    d "We're still winning."
    scene sb1386 with dssa
    za "I tired myself out against you."
    scene sb1387 with dssr
    za "Match point?"
    scene sb1388 with dssa
    lou "Are you getting tired?"
    scene sb1389 with dssa
    za "Yeah, we had been playing for a while before you arrived... And today's just a friendly match... But next time we'll put something on the line."
    scene sb1388 with dssa
    lou "Like what?"
    scene sb1389 with dssa
    za "Honor and bragging rights."
    scene sb1390 with dssa
    pat "Alright, match point."
    scene sb1391 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1392 with vpunch
    pause
    scene sb1393 with vpunch
    pause
    scene sb1394 with vpunch
    "While crossing paths, Zara skillfully lays the ball in to your hands."
    menu:
        "Believe in Zara and pass to her.":
            $ ZaraBBallTrust5x0 = True
            scene sb1424 with dssa
            "You feint a throw and pass to Zara."
            scene sb1425 with vpunch
            "And she just so manages to make the basket."
            scene sb1398 with vpunch
            za "YES!"
            scene sb1399 with dssr
            d "...Umm."
            scene sb1400 with dssr
            "Her legs are locked tightly around you, leaving you no space to move."
            scene sb1401 with dssa
            za "I didn't see your pass coming... I almost fucked it up."
            scene sb1402 with dssa
            pause
            scene sb1403 with dssa
            $ play_playlist(playlist_Ch5_ViceCity)
            d "I believed in you."
            scene sb1404 with dssa
            pause
            scene sb1405 with dssa
            "Zara keeps staring at you with big eyes."
            scene sb1406 with dssr
            d "...Are you okay?"
            scene sb1407 with dssa
        "Make the basket yourself.":
            scene sb1395 with dssa
            pause
            scene sb1396 with dssa
            za "Nice!"
            scene sb1397 with vpunch
            pause
            scene sb1408 with dssr
    pat "Damn it... We underestimated you two."
    scene sb1409 with dssa
    lou "Does one of you play for a college team?"
    scene sb1410 with dssa
    za "He probably will. For ZPR."
    scene sb1411 with dssr
    lou "ZPR."
    scene sb1412 with dssa
    pat "We're at the MOR college."
    scene sb1413 with dssa
    za "Rivals."
    scene sb1414 with dssr
    pat "I think we'll see each other again, [name]."
    scene sb1415 with dssa
    d "I'm not in the first team yet."
    scene sb1416 with dssa
    pat "Neither am I."
    pat "And considering how you made every single throw... I'm really worried."
    scene sb1417 with dssa
    lou "We want a rematch."
    scene sb1418 with dssa
    za "You'll get it."
    scene sb1419 with dssa
    za "Here's my number."
    scene sb1420 with dssr
    lou "Thanks, we'll be in contact."
    scene sb1421 with dssr
    pause
    scene sb1422 with vpunch
    pause
    scene sb1423 with dssa
    pause
    if ZaraBBallTrust5x0 is False:
        stop music fadeout 2.5
    scene black with Dissolve(2)
    with Pause(.5)
    jump NickEvening5x0


label NickEvening5x0:
    if ZaraBBallTrust5x0 is False:
        $ play_playlist(playlist_AmbientCheeto)
    scene sb1426 with dssb
    za "We're back!"
    scene sb1427 with dssr
    nic "Where were you two?"
    scene sb1428 with dssa
    za "We played some basketball down the street."
    scene sb1429 with dssr
    pause
    scene sb1430 with dssa
    d "Oh. Hey."
    scene sb1431 with dssr
    pause
    scene sb1432 with dssa
    mi "Hey."
    scene sb1433 with dssa
    za "Hi Mila!"
    scene sb1434 with dssr
    mi "Hey Zara."
    scene sb1436 with dssr
    d "Can I take a shower?"
    scene sb1438 with dssr
    za "I'll take one too, I'll show you a bathroom."
    scene sb1437 with dssa
    d "(Mila looks pretty damn sad.)"
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1439 with dssb
    pause
    scene sb1440 with dssr
    n "It's good that you just left."
    scene sb1441 with dssr
    pause
    if MilaKiss4x5 is True:
        menu:
            "Give Mila a kiss on her head.":
                $ KissedGirl = True
                $ MilaLove5x0 = True
                if NamiLove4x5 is True:
                    scene sb1443 with dssa
                    pause
                else:
                    scene sb1442 with dssa
                    pause
                "Mila's eyes glow up a little."
            "Don't, she might not be in the mood.":
                pass
    scene sb1444 with dssa
    d "Hey, what brings you here?"
    scene sb1445 with dssa
    mi "I just lost it."
    mi "My father trashed half my room because he couldn't find his booze and thought I had taken it."
    scene sb1446 with vpunch
    mi "I'm done! Completely done!"
    scene sb1447 with dssa
    "She squints her face together, you're unsure if it's to contain her anger or prevent her from crying."
    scene sb1448 with dssa
    mi "I applied for a student house."
    mi "I-I'm here to tell you two that if you wanna move in with me... Now is the time... if not... Then okay, but I will make the move."
    scene sb1449 with dssa
    "You and Nami's eyes meet for a split second, but part ways equally as fast."
    scene sb1450 with dssa
    d "(Neither I nor the Cheeto knows what to say.)"
    scene sb1451 with dssa
    "You feel your heart pounding against your chest by the thought of moving out."
    scene sb1452 with dssa
    d "(I don't wanna leave Noji... I'm so-...)"
    d "(...I'm so afraid.)"
    scene sb1453 with dssa
    pause
    scene sb1454 with dssa
    d "We're moving with you."
    d "There's no better time than now... We had to leave our house because of an infestation..."
    scene sb1455 with dssa
    d "I will talk to Noji... Tell her to consider moving in with Nick."
    scene sb1456 with vpunch
    n "Yo! That's a big step... Like us movi-"
    scene sb1457 with dssa
    d "Cheeto... Now is not the time to be scared..."
    d "And believe me... I'm fucking scared as hell... My heart's been pounding through my chest... I'm so close to a panic attack."
    scene sb1458 with dssr
    "Mila's brows go up a little."
    pause
    scene sb1459 with dssa
    d "We're coming with you... Give us some details."
    scene sb1460 with dssa
    mi "I checked the houses, and they only have one left."
    mi "It's expensive... And we will probably need to work on the side... At least for a little."
    scene sb1461 with dssr
    n "Is the place at least nice?"
    scene sb1462 with dssa
    mi "Yes."
    scene sb1463 with dssr
    mi "It has space for four people, a big living room, a garage, a little garden..."
    mi "We can take a look at it in a few days."
    scene sb1464 with dssa
    mi "They told me that if I don't find some suitable roomies in the next two days, I would get paired up with random ones."
    mi "I wouldn't mind it... But I obviously would prefer you two."
    scene sb1466 with vpunch
    n "Alright! We're in!"
    scene sb1467 with dssa
    d "Cheeto... Calm down."
    scene sb1468 with dssa
    pause
    scene sb1469 with dssa
    d "A little more."
    scene sb1470 with dssa
    pause
    scene sb1471 with dssa
    mi "Thank you so much."
    scene sb1472 with dssr
    mi "We would probably move in around one to three weeks."
    mi "They'll need to prepare the house."
    mi "Nick offered me to stay here for the night..."
    if MilaKiss4x5 and MilaDate is True:
        scene sb1473 with dssa
        mi "Is it okay if I stay with you?"
        menu:
            "Would you mind staying with Nami tonight?":
                scene sb1474 with dssa
                mi "I don't mind."
                scene sb1477 with dssa
                n "Cool!"
            "Yeah, sure.":
                $ MilaSleep5x0 = True
                scene sb1475 with dssa
                mi "Great." #smiles
    else:
        scene sb1476 with dssa
        mi "Is it okay if we share a room?"
        scene sb1477 with dssa
        n "Of course!"
    scene sb1478 with dssr
    nic "Dinner is ready!"
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch5_Nia)
    scene sb1479 with tleaf
    pause
    scene sb1480 with dssa
    va "Oh my..."
    scene sb1481 with dssr
    pause
    scene sb1482 with dssa
    va "Aren't you a splendid specimen..."
    scene sb1483 with dssr
    mi "...What?"
    scene sb1484 with dssa
    va "Those curves..."
    scene sb1485 with dssa
    $ persistent.unlockedImageST_CH5_7 = True
    va "Your cute face..."
    scene sb1486 with dssa
    va "Your potential is limitless."
    scene sb1487 with dssr
    mi "Umm thanks?"
    scene sb1488 with dssa
    va "I'd like to see you nude someday..."
    scene sb1489 with dssa
    mi "...Who are you?"
    scene sb1490 with dssa
    d "Zara's weird sister."
    scene sb1491 with dssa
    va "[name], it's good to see you again."
    if VanessaImpressive4x0 or VanessaUndecided4x0 is True:
        scene sb1492 with dssr
        d "Almost nice to see you too."
        scene sb1493 with dssa
        va "Just almost?"
        scene sb1494 with dssa
        d "Just almost."
        scene sb1495 with dssa
        pause
    elif VanessaDislike4x0 is True:
        scene sb1496 with dssa
        d "I wish I could say the same."
        scene sb1497 with dssa
        va "You're not very nice... or smart."
    scene sb1499 with dssr
    pause
    scene sb1498 with dssa
    za "I stubbed my little toe..."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1500 with dssb
    pause
    scene sb1501 with dssa
    n "And that's why I suspect that the reason one of my rolls went missing was... Kidnapped by the mice... Taken away from it's roll family..."
    n "And then... killed, even though the ransom was paid."
    scene sb1502 with dssr
    "Vanessa chuckles."
    scene sb1515 with dssr
    m "That was an... interesting story, Nami."
    scene sb1538 with dssr
    d "*Whisper* You're a retard, you know that?"
    scene sb1539 with dssa
    n "*Whisper* Don't antagonize someone who just lost a roll... I've got nothing to lose!"
    scene sb1518 with dssr
    nic "Mila, how's college?"
    scene sb1519 with dssa
    mi "It's pretty good."
    scene sb1518 with dssa
    nic "What do you major in?"
    scene sb1519 with dssa
    mi "Business Sales and human resources."
    scene sb1518 with dssa
    nic "Cool, I also majored in Sales."
    scene sb1520 with dssr
    mi "Any tips?"
    scene sb1521 with dssr
    nic "Follow your heart and think outside the box."
    nic "You don't want to be just one of many."
    scene sb1522 with dssa
    mi "True."
    scene sb1534 with dssa
    va "Make use of your assets."
    scene sb1523 with dssr
    mi "You mean-"
    scene sb1537 with dssr
    va "Yes, your amazing breasts."
    scene sb1536 with dssr
    pause
    scene sb1525 with dssr
    nic "Do you play any sports?"
    scene sb1526 with dssa
    mi "Umm... Well, I'm looking into golf."
    scene sb1527 with dssa
    nic "Noji and I occasionally play it."
    scene sb1528 with dssa
    mi "I just don't have access to a course at the moment."
    scene sb1529 with dssa
    nic "Nojiko and I talked about the Petrova country club."
    nic "I can talk to Elena and I'm sure she'll let you play there."
    scene sb1530 with dssa
    mi "That's not necessary..."
    scene sb1517 with dssr
    nic "Mila. You're majoring in sales."
    nic "Take what you want."
    nic "And if an opportunity presents itself, leave your ego at the door and consider the bigger picture."
    scene sb1531 with dssr
    mi "You're right. Thank you."
    scene sb1503 with dssr
    pause
    scene sb1504 with dssa
    if MilaKiss4x5 is True:
        va "Say Mila... If it's not too personal."
        va "Are you dating [name]?"
        scene sb1505 with dssa
        mi "Umm-"
        scene sb1506 with dssa
        va "Your eyes are drawn to him."
        if MilaDate is True:
            scene sb1532 with dssr
            mi "We're testing the waters."
            scene sb1507 with dssr
            va "Yeah... I hear it in your voice..."
            va "He never seems to be fully in... Always only half."
            scene sb1508 with dssa
            va "What are you afraid of [name]?"
            va "Commitment?"
            scene sb1509 with dssa
            va "The touch of a woman?"
            scene sb1510 with dssa
            nic "Nessy, don't make me send you upstairs."
            d "(She precisely picks out the things that bother people.)"
            if MilaLike4x5 is True:
                d "(Mila already gave me that talk of not being 'really interested.')"
        else:
            scene sb1533 with dssr
            mi "We aren't dating."
            scene sb1535 with dssa
            va "And yet your eyes are drawn to him... Would you like to date him?"
            scene sb1534 with dssa
            mi "Sorry, but that's none of your business."
        scene sb1511 with dssr
        za "Seriously, stop asking people you don't know such personal questions."
        scene sb1512 with dssa
        va "Who says I don't know Mila?"
        scene sb1513 with dssa
        mi "I have never seen or spoken to you before."
        scene sb1514 with dssa
        va "And yet, I know so much about you... Miss Steiner."
        scene sb1513 with dssa
        pause
    else:
        va "Mila, I'd like to play a game of golf with you sometime."
        scene sb1505 with dssa
        mi "Umm, sure."
        scene sb1506 with dssa
        va "Give me your number after dinner."
    $ persistent.unlockedImageMilaCH5_2 = True
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1540 with dssr
    nic "We'll be heading to bed. We'll both need to be up early."
    scene sb1541 with dssr
    nic "[name], Nami, and Mila. If you need anything, don't hesitate to ask."
    scene sb1542 with dssr
    mi "I'll get ready for the night, too."
    scene sb1544 with dssa
    za "Same."
    stop music fadeout 2.5
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_AmbientCheeto)
    scene sb1543 with dssr
    pause
    if NamiLove5x0 is True:
        $ persistent.unlockedImageR_CH5_4 = True
        "You and the Cheeto stand there... No noise but the dripping water from the pool fountains."
        scene sb1555 with dssr
        pause
        scene sb1556 with dssa
        n "Can we talk?"
        scene sb1557 with dssa
        d "Mhm."
        scene sb1558 with dssr
        pause
        scene sb1559 with dssa
        n "...You're so important to me."
        n "And after what you said this morning... I don't want you to think that I'm-"
        scene sb1560 with dssr
        d "Cheeto... The problem is... What do you want?"
        d "You can't do this to me every fucking time... Act like you're about to jump me, then draw back... Repeat."
        d "What is it that you want?"
        scene sb1561 with dssa
        n "I want to be close to you... All the time."
        n "But if that doesn't work out... In any way or form... Raven [name] and Phoenix Nami are gone."
        scene sb1562 with dssa
        n "It scares me so much... I never really looked at the possible consequences... I'm so afraid of losing you."
        scene sb1563 with dssa
        d "I agree that this here is... it's insane..."
        scene sb1564 with dssa
        n "I know you... and I know me... If we go down this route... There's no turning back."
        n "We can pretend as if nothing could ever come between us... But that's not true."
        n "...What we're doing is so wrong."
        scene sb1565 with dssa
        d "Cheeto. We're doing nothing. We haven't even started anything."
        scene sb1566 with dssr
        n "We've touched the starting line."
        n "And our chances to just step away from a race that we are most likely about to lose are fading."
        scene sb1567 with dssa
        pause
        scene sb1568 with dssa
        n "Step away from the line, please."
        scene sb1569 with dssa
        pause
        d "Why don't you do it?"
        scene sb1571 with dssa
        n "I can't."
        scene sb1572 with dssa
        pause
        scene sb1573 with dssr
        "She steps on her toes and leans in closer."
        scene sb1574 with dssr
        n "*Whisper* I made my decision."
        n "Please be the sane one and step away."
        scene sb1575 with dssa
        pause
        menu:
            "Step away.":
                $ NamiStepAway5x0 = True
                scene sb1576 with dssa
                pause
                scene sb1577 with dssr
                pause
                scene sb1578 with dssr
                d "(The Cheeto is right.)"
                scene sb1579 with dssa
                d "(We can't do this now... Maybe someday... But not now. I'm not ready.)"
            "Start a race with impossible odds.":
                $ KissedGirl = True
                $ achievement.grant("ARaceWith")
                $ achievement.sync()
                $ RaceWithImpossibleOdds = True
                scene sb1580 with dssa
                pause
                scene sb1581 with dssa
                pause
                scene sb1582 with dssr
                pause
                "The kiss is slow and sensual..."
                "It feels like you're sharing a dream..."
                scene black with Dissolve(2)
                with Pause(.5)
        jump Chapter5End

    elif NamiLove5x0 is False and NamiLove4x5 is True:
        scene sb1545 with dssr
        pause
        scene sb1546 with dssa
        n "...Good night."
        scene sb1547 with dssa
        d "Good night, Cheeto."
    else:
        scene sb1545 with dssr
        pause
        scene sb1545 with dssa
        n "So we're moving, huh?"
        scene sb1547 with dssa
        d "Yeah... Apparently."
        scene sb1548 with dssa
        n "I might be happy after I get a hold of that terrifying feeling inside my belly."
        scene sb1549 with dssa
        pause
        scene sb1548 with dssa
        n "I was so surprised when she called me."
        scene sb1550 with vpunch
        n "We're grown ups now!"
        scene sb1551 with dssa
        d "We're soooo far away from being grown ups."
        d "The last thing you did was tell a story about a roll that had been kidnapped by a bunch of mice."
        scene sb1552 with dssa
        n "A real tragedy..."
        scene sb1553 with dssa
        d "Go to bed, Cheeto."
        if MilaSleep5x0 is True:
            n "Have fun with Mila."
            d "...Thanks."
    scene black with Dissolve(2)
    with Pause(.5)
    jump Chapter5End


label Chapter5End:
    scene sb1583 with dssb
    pause
    d "(Why did Nojiko and Amber act like they didn't know each other...)"
    d "(They've been going to the same, tightly packed book club for years.)"
    scene sb1584 with dssr
    d "(I'll ask Amber on our trip... That way she can't dodge the question.)"
    scene sb1585 with dssr
    d "(I'm trying to think of a reason why Noji would be playing games.)"
    d "(Is that why she didn't want me there?)"
    show j_1 with dssr
    pause
    show j_2 with dssr
    pause
    show j_3 with dssr
    pause
    show j_4 with dssr
    pause
    show j_5 with dssr
    pause
    show j_6 with dssr
    pause
    $ JeffChat5x0 = True
    stop music fadeout 2.0
    scene sb1585 with dssa
    pause
    $ play_playlist(playlist_AmbientBellchen)
    scene sb1586 with dssa
    d "Hey."
    scene sb1591 with dssr
    b "What's up?"
    "You take a second to answer."
    scene sb1586 with dssr
    d "I'll be living at Zara's for a while."
    d "We had a uh... a rodent infestation at home."
    pause
    d "I can't see you right now... But I just know you're smiling, cunt."
    scene sb1592 with dssr
    pause
    scene sb1587 with dssb
    pause
    scene sb1588 with dssa
    b "The old trash can didn't hold up, huh?"
    d "Fuck off..."
    scene sb1589 with dssa
    d "I'll see if I can get some info from Vanessa."
    d "Preferable before you go and see the Holgerson guy."
    scene sb1589_2 with dssr
    b "Some additional info would be good."
    if BellaNonExclusive5x0 or BellaOnIce5x0 is True:
        scene sb1595t with dssr
        b "Anything else?"
        scene sb1596t with dssa
        d "...No."
        scene sb1595t with dssa
        b "I'll see you tomorrow then."
        scene sb1596t with dssa
        d "Yeah, we'll need to get back to the project."
        scene sb1595t with dssa
        b "If we get a bad grade, I'm gonna complain about you."
        scene sb1596t with dssa
        d "Bye."
        scene sb1597 with dssr
        b "*Soft* Bye."
        scene sb1599 with dssa
        pause
        scene sb1600 with dssa
        b "What do you think of his voice?"
        scene sb1601 with dssa
        pause
        scene sb1602 with dssa
        b "I know he sometimes sounds like a bitch... A bitch with a rather deep voice."
        scene sb1603 with dssa
        pause
        b "...I like hearing it."
    else:
        scene sb1595 with dssr
        b "Is there anything else you want to get off your poor chest?"
        scene sb1596 with dssa
        d "No."
        d "But we'll need to get back to the project."
        scene sb1595 with dssa
        b "Yup."
        b "Bye."
        scene sb1596 with dssa
        d "Bye."
        scene sb1598 with dssr
        pause
        scene sb1599 with dssa
        pause
        scene sb1600 with dssa
        b "I know, despite his deep voice, he sometimes sounds like a bitch."
        scene sb1603 with dssa
        pause
    scene sb1604 with dssr
    pause
    scene sb1605 with dssa
    b "You should see him..."
    b "His eyes are quite pretty."
    scene sb1606 with dssr
    b "...Someday you will."
    scene sb1607 with dssa
    b "*Coughs* Where were we?"
    $ persistent.unlockedImageST_CH5_8 = True
    scene sb1608 with dssr
    pause
    if KissedGirl is False:
        $ achievement.grant("TheCursen")
        $ achievement.sync()
    else:
        pass
    hide screen music_player_trigger
    scene BellchenEndCH5 with dissolve
    $ renpy.pause(2.5, hard=True)
    with Pause(5)
    show screen music_player_trigger
    scene black with Dissolve(2)
    with Pause(.5)
    $ achievement.grant("FinishedSeason1")
    $ achievement.sync()
    jump MPS2
