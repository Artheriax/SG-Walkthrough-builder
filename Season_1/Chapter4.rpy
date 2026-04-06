label Chapter4alt:
    $ achievement.grant("FinishCh3x5")
    $ achievement.sync()
    define dssa = Dissolve(.45)
    define dssr = Dissolve(1)
    if BellaKiss03x is True:
        $ BellaKiss3x5 = True
    else:
        $ BellaKiss3x5 = False
    if BellaKiss03x is True:
        $ persistent.unlockedImageRS41 = True
        scene ac1 with dssb
        pause
        play music "music/Vesky - Departure.ogg"
        scene ac2 with dssa
        d "(Footsteps.)"
        scene ac3 with dssb
        pause
        d "I didn't expect to see you here."
        scene ac5 with dssb
        b "...Why are you such an idiot?"
        d "How did you know I was here?"
        scene black with Dissolve(2)
        with Pause(.5)
        scene ac219 with dssb
        pause
        scene ac220 with dssa
        "*Phone ringing*"
        scene ac222 with dssb
        b "Who's this?"
        scene ac208 with dssb
        rob "Hi Bella. It's Robin."
        b "Robin?"
        scene ac209 with dssa
        rob "Sorry if I'm disturbing you, but I think you might want to know something."
        scene ac222 with dssa
        b "What is it?"
        scene ac221 with dssa
        rob "[name] is currently handcuffed in the girls locker room."
        scene ac223 with vpunch
        b "What?!"
        scene ac210 with dssb
        rob "I just thought you might want to free him before he stays there for too long."
        b "Who did this?"
        rob "Ask him."
        b "What an idiot!"
        scene ac212 with dssb
        pause
        scene ac213 with dssb
        pause
        scene ac214 with dssa
        sas "And?"
        scene ac215 with dssa
        rob "She'll get him."
        scene ac216 with dssa
        sas "They won't be happy."
        scene ac217 with dssa
        rob "I don't care. He didn't deserve it."
        scene ac218 with dssa
        sas "Maybe he does..."
        stop music fadeout 2
        scene black with Dissolve(2)
        play music "music/VeskyBeyondTheWindow.ogg"
        with Pause(.5)
        scene ac226 with dssb
        am "Stefanie listen... The new dress looks amazing on you."
        am "You don't need to hide anything. Show what you've got and remember... You're not too old."
        scene ac227 with dssb
        pause
        scene ac228 with dssb
        am "Exactly."
        am "And I have someone for you..."
        am "We'll talk about it some time later."
        scene ac229 with dssa
        pause
        scene ac230 with dssa
        $ persistent.unlockedImageAmber8 = True
        am "Good. And promise me to live a little."
        scene ac231 with dssb
        am "Bella?"
        scene ac234 with dssb
        b "I've gotta see Ayua."
        scene ac232 with dssa
        "Amber gives her a smile."
        b "What?"
        scene ac233 with dssa
        am "Your voice is pitched higher, your shoulders are under tension and your brow twitches.... and besides that, you're going to see her anyways during your trip..."
        am "Say hi to [name] from me."
        scene ac235 with dssb
        "Bella rolls her eyes."
        stop music fadeout 2
        scene black with Dissolve(2)
        with Pause(.5)
        play music "music/Vesky - Departure.ogg"
        scene ac5 with dssb
        d "I see."
        b "So who did this?"
        d "Nadia and Zara."
        scene ac6 with dssb
        b "Nadia?! Why would she do that?"
        d "I made them look like fools and won the game... Also accidentally ripped Zara's Shirt."
        scene ac7 with dssa
        b "Haha... They don't take losing well."
        scene ac8 with dssa
        d "Do you want to free me?"
        scene ac7 with dssa
        b "Na, not yet."
        scene ac9 with dssa
        pause
        d "Why weren't you in college today?"
        scene ac10 with dssa
        b "What a stupid question."
        scene ac11 with dssa
        pause
        b "Did you tell them what happened?"
        d "No... but I guess Nami did."
        scene ac12 with dssa
        if UmB is True:
            b "You're not wearing the boxer shorts I bought for you."
            d "I only have one pair of them. I only want to wear them to special events."
        d "Mind cutting me loose? My arm hurts."
        scene ac13 with dssa
        b "*whisper* Not yet."
        scene ac14 with dssb
        pause
        scene ac15 with dssb
        pause
        d "I guess you're over your... breakdown?"
        scene ac16 with dssa
        "She passionately grabs your face and french kisses you."
        scene ac17 with dssa
        pause
        scene ac18 with dssa
        pause
        scene ac19 with dssb
        b "*sensual whisper* I like you..."
        scene ac20 with dssr
        b "I really do."
        b "But we cannot be together."
        scene ac21 with dssa
        d "I was about to say the same."
        d "We're-."
        scene ac22 with dssb
        b "Too broken..."
        b "And- I think we would just drag each other down further."
        d "I don't know if I'd say that... You're the reason I'm lighting up a little..."
        d "...But I agree. The second the honeymoon phase is over we'd destroy each other."
        scene ac23 with dssa
        pause
        d "(I can see it in her eyes... How she wished I didn't agree.)"
        scene ac24 with dssa
        b "Maybe someday... when we've dealt with our own issues."
        scene ac25 with dssa
        d "(And I can feel it in my stomach... Wishing I hadn't agreed.)"
        pause
        scene ac26 with dssb
        d "Your breast."
        scene ac27 with dssa
        "Bella looks down at her revealed boob..."
        scene ac28 with dssa
        "...and back up to you."
        scene ac29 with dssa
        pause
        scene ac30 with dssa
        pause
        scene ac31 with dssa
        pause
        scene ac32 with dssa
        "You carefully tuck her boob back in."
        scene ac34 with dssb
        pause
        scene ac35 with dssa
        d "I think I left my jacket in your car."
        scene ac36 with dssa
        b "*Whispers* It's mine now."
        scene ac37 with dssa
        pause
        scene ac38 with dssb
        pause
        scene ac39 with vpunch
        pause
        scene ac40 with dssb
        d "Thanks."
        b "I'm surprised you let them do it."
        scene ac41 with dssa
        d "I'm trying to change... you know. Less enemies... More neutrals."
        d "But they did something I can't let slide."
        b "What was it?"
        scene ac42 with dssa
        d "They used Nami to bait me."
        d "Robin came and told me Nami was having a heatstroke..."
        scene ac43 with dssb
        b "...Idiots."
        b "Especially Nadia should... *sigh*"
        b "I'll give them a mouthful."
        scene ac44 with dssa
        d "No, I'll handle it."
        scene ac43 with dssa
        b "Let me."
        b "You'll overdo it."
        d "That's how you make sure nobody retaliates."
        scene ac45 with dssa
        b "Let me... Please."
        scene ac46 with dssb
        pause
        d "...Fine."
        "Suddenly the door swings open."
        $ play_playlist(playlist_GirlyCh4x)
        scene ac47 with vpunch
        pause
        if RoRum is True:
            scene ac48 with dssb
            u "Oh my god... Seriously?"
            u "You must have an STD by now."
            scene ac49 with dssb
            u "Oh man! We missed the action!" #nora
            scene ac50 with dssb
            u "...Bella."
            scene ac52 with dssa
            b "I have no idea who you are."
            scene ac50 with dssa
            u "We went to high school together."
            scene ac52 with dssa
            b "Seems like you weren't important enough."
            scene ac51 with dssa
            u "Get off your high horse."
            scene ac53 with dssb
            b "Let's go."
            scene black with Dissolve(2)
            with Pause(.5)
            scene ac54 with dssb
            pause
            scene ac55 with dssb
            u "Here."
            scene ac56 with dssa
            u "It slid under one of the seats."
            scene ac57 with dssb
            pause
            d "On another note. Which one of you started the rumor about me and Robin?"
            scene ac58 with dssb
            u "We didn't tell anyone."
            d "Bullshit."
            d "You're the only ones that could've known."
            scene ac59 with dssb
            u "We didn't tell anyone!"
            scene ac61 with dssb
            b "Liar."
            scene ac60 with vpunch
            u "Shut up, moron."
            scene ac62 with dssb
            b "You want to get kicked in the face again?"
            scene ac59 with dssb
            u "Oh? You do remember me."
            scene ac63 with dssb
            d "I'll find out which one of you did."
            stop music fadeout 2.5
            scene black with Dissolve(2)
            with Pause(.5)
        else:
            scene ac48 with dssb
            u "Oh- wow!"
            u "Speak of the devil..."
            scene ac49 with dssb
            u "Oh man! We missed the action!" #nora
            scene ac50 with dssb
            u "...Bella."
            scene ac52 with dssa
            b "I have no idea who you are."
            scene ac49 with dssa
            u "We went to high school together."
            scene ac52 with dssa
            b "Seems like you weren't important enough."
            scene ac51 with dssa
            u "Get off your high horse."
            scene ac53 with dssb
            stop music fadeout 2.5
            b "Let's go."
        play music "music/VeskyThinkingOfYou.ogg"
        scene ac237 with dssb
        d "Who was that girl? I sense a lot of resentment."
        scene ac238 with dssa
        b "...She's one of those people that called me weird in middle school."
        if RoRum is True:
            d "You kicked her in the face?"
            scene ac239 with dssb
            b "One day I just had enough."
            b "But I don't want to talk about it."
        else:
            scene ac239 with dssb
        b "Home?"
        d "No, take me to the Library."
        scene ac240 with dssa
        b "Right, you nerds are going to play your virgin games."
        b "And remember. I'll talk to Nadia."
        d "You know that I'm not going to listen to you."
        $ persistent.unlockedImageBellaCh41 = True
        scene ac240b with dssa
        b "Then I'm withholding sex."
        scene ac240c with dssa
        b "*Chuckles.*"
        scene ac240d with dssa
        d "You're the only one who laughs at your jokes."
        scene ac241 with dssa
        pause
        scene ac243 with dssa
        b "...*Whisper* The fuck are you doing?"
        d "That was the last one."
        scene ac245 with dssa
        d "I'll confront Nadia about it... But I'll keep it cool."
        scene ac246 with dssa
        b "I'll be leaving in a few hours... I won't be home 'till Monday."
        d "Mhm."
        scene ac247 with dssa
        b "But I don't think it matters now anyways. There's nothing between us."
        scene ac248 with dssa
        d "There is something between us. We just both chose the wise option."
        scene ac249 with dssr
        b "Yup."
        scene ac250 with dssb
        d "Where is the library?"
        scene ac251 with dssa
        b "The high building there."
        scene ac252 with dssa
        d "Alright... Thanks."
        scene ac253 with dssb
        pause
        stop music fadeout 2.5
        scene black with tleaf
        with Pause(1)
        $ achievement.grant("BellaSave")
        $ achievement.sync()
        jump boardgame04
    else:
        $ persistent.unlockedImageRS42 = True
        $ FoundByMarla4x0 = True
        $ play_playlist(playlist_AmbientNamiLake)
        scene ac1 with dssb
        pause
        scene ac2 with dssa
        d "(Footsteps.)"
        scene ac48 with dssb
        $ play_playlist(playlist_GirlyCh4)
        u "What the..."
        u "Hahahaha!"
        $ persistent.unlockedImageKate1 = True
        scene ac64 with dssb
        if RoRum is True:
            u "Did your girlfriend find out you cheated on her with Robin and lock you to the wall?"
            d "I don't have a girlfriend."
            d "...And I would really appreciate it if you could unlock me."
        else:
            u "Who locked you up?"
            d "Does it matter?"
        scene ac65 with dssb
        u "Where is the key?"
        d "Should be on one of those seats."
        scene ac66 with dssb
        pause
        scene ac67 with dssb
        u "What do I get for it?"
        if RoRum is True:
            scene ac68 with dssa
            d "I don't slap you in the face for spreading that rumor?"
            scene ac69 with dssa
            u "We didn't spread any rumor."
            scene ac70 with dssa
            d "Bullshit. You were the only ones that knew."
            scene ac69 with dssa
            u "We didn't tell anyone... yet."
            scene ac71 with dssa
            u "I didn't say anything either."
            d "There was nobody else!"
            scene ac72 with dssa
            u "Maybe... that thingy?"
            u "No idea."
            u "We didn't tell anyone."
        scene ac73 with dssa
        d "Would you just unlock me?"
        if BTY is True:
            scene ac74 with dssa
            u "Sure... for a kiss."
            d "What?"
            u "Just a simple kiss and I'll unlock you."
            d "Forget it."
        scene ac75 with vpunch
        u "Nora?! What are you doing?"
        no "I'm changing? I thought we were going to run track?"
        scene ac76 with vpunch
        u "Yes, you moron!"
        u "But wait until he's left the room before you strip down!"
        no "Ohhh!"
        scene ac77 with dssa
        u "Here free him."
        scene ac78 with dssa
        pause
        scene ac79 with dssb
        d "What are you waiting for?"
        scene ac80 with dssa
        pause
        scene ac81 with dssr
        pause
        scene ac82 with dssa
        d "*sigh*."
        scene ac83 with dssa #Long way
        d "You should have opened the one that is around my arm..."
        scene ac84 with dssr
        no "I want to know how it feels!"
        scene ac85 with vpunch
        no "Miri! Look!"
        no "I'm a prisoner!"
        miri "You're a retard."
        scene ac86 with vpunch
        no "Do you think we could break the chain if we pulled hard enough?"
        scene ac87 with vpunch
        d "No. Your toothpick of an arm would break first."
        d "Now give me the key."
        scene ac88 with dssa
        pause
        scene ac89 with dssa
        pause
        scene ac90 with dssa
        no "That's funny!"
        no "Swing your arms, too!"
        scene ac91 with dssb
        miri "Nora! Give him the fucking key!"
        scene ac89 with dssb
        pause
        scene ac92 with dssa
        pause
        scene ac93 with vpunch
        pause
        scene ac94 with dssb
        pause
        scene ac95 with dssa
        pause
        scene ac96 with dssa
        pause
        scene ac97 with dssb
        d "...Are you fucking kidding me?"
        scene ac98 with dssa
        no "Kate... Where is the key?"
        scene ac99 with dssb
        kat "Did it go into the drain?"
        scene ac100 with vpunch
        d "You fucking idiot!"
        scene ac101 with vpunch
        miri "Goddamn it Nora! Do you always have to be a moron?!"
        no "Mama said you shouldn't call me that anymore!"
        scene ac102 with vpunch
        "Miriam pushes Nora onto the seat..."
        scene ac103 with vpunch
        "...Causing you to fall on top of her."
        pause
        scene ac104 with dssb
        miri "Oh! I didn't think this through..."
        scene ac105 with vpunch
        ma "What is going on here?!"
        scene ac106 with dssb
        pause
        scene ac107 with dssa
        d "It's not what it looks like."
        scene ac108 with dssa
        no "We're definitely not having sex!"
        scene ac109 with dssa
        miri "*whisper* Shut up you idiot!"
        scene ac110 with dssa
        kat "We found him locked to the wall."
        scene ac111 with dssa
        ma "I'm aware that he was locked to the wall."
        scene ac107 with dssb
        stop music fadeout 2
        d "How?"
        scene black with Dissolve(2)
        play music "music/TheIntangible/The Intangible - Encyclopedia of Frozen Dreams.ogg"
        with Pause(.5)
        scene ac198 with dssb
        ma "Are you sure?"
        ma "Okay... I will live a little."
        ma "We'll talk later..."
        scene ac200 with dssa
        pause
        scene ac201 with dssa
        pause
        scene ac202 with dssa
        $ persistent.unlockedImageMarla3 = True
        ma "Fine... Just a little more won't hurt... right?"
        scene ac204 with dssr
        ma "Marla?"
        scene ac208 with dssa
        rob "Hi Miss Marla. It's Robin."
        scene ac205 with dssa
        ma "Robin, how can I help you?"
        scene ac208 with dssa
        rob "Sorry if I'm disturbing you."
        scene ac209 with dssa
        rob "But [name] is currently handcuffed in one of the girls locker rooms."
        scene ac206 with vpunch
        ma "Excuse me?!"
        scene ac210 with dssa
        rob "I- it was just a little prank from some people... I'm just afraid that they might forget him there."
        scene ac211 with dssa
        ma "Who is responsible for this?"
        scene ac210 with dssa
        rob "I- I can't tell you."
        scene ac207 with dssb
        ma "...This boy."
        scene ac212 with dssb
        pause
        scene ac213 with dssb
        pause
        scene ac214 with dssa
        sas "And?"
        scene ac215 with dssa
        rob "She'll get him..."
        scene ac216 with dssa
        sas "They will find out."
        scene ac217 with dssa
        rob "I don't care. He didn't deserve it."
        scene ac218 with dssa
        sas "Maybe."
        stop music fadeout 2
        scene black with tleaf
        with Pause(.5)
        scene ac107 with tleaf
        $ play_playlist(playlist_GirlyCh4x)
        d "I see..."
        scene ac112 with dssa
        d "Unlock your legs!"
        no "But you might fall down."
        scene ac113 with vpunch
        d "THAT'S THE POINT!"
        scene ac114 with dssb
        $ persistent.unlockedImageTwins1 = True
        ma "I- I'm speechless."
        ma "Why are you cuffed together?!"
        scene ac115 with vpunch
        d "This IDIOT had the key and locked herself to me... AND THEN THREW THE KEY AWAY!"
        scene ac116 with dssa
        no "No need to scream! She might be old but she's right in front of you..."
        "Miss Marla shoots a look at Nora."
        scene ac124 with dssb
        kat "It's in the drain."
        scene ac125 with dssa
        ma "Could you reach it?"
        scene ac124 with dssa
        kat "No, I couldn't even see it."
        scene ac126 with dssa
        ma "Who locked you to the wall?"
        scene ac117 with dssa
        d "I can't remember."
        d "(This way I will get some leverage on Nadia and Zara... Might prove useful in the future.)"
        scene ac118 with dssa
        pause
        ma "Are you sure you want to go down this road?"
        scene ac119 with dssa
        d "I'm certain."
        scene ac126 with dssa
        ma "Who did it?"
        scene ac128 with dssb
        miri "We don't know."
        miri "We found him like this."
        scene ac120 with vpunch
        no "*gasps* We should..."
        no "Miri! We should re-open our detective's club and find out!"
        scene ac130 with dssb
        miri "...Just be quiet."
        scene ac115 with dssa
        d "Can we finally work on a solution to free me?!"
        scene ac121 with dssa
        no "You mean us."
        scene ac122 with dssa
        d "No. I think you belong in cuffs."
        scene ac123 with dssa
        no "I have these pink fluffy ones I really li-"
        scene ac131 with vpunch
        miri "Shut your mouth!"
        scene ac127 with dssb
        ma "I'll get the janitor."
        scene ac129 with dssb
        miri "Did you see her cleavage?"
        kat "So cringe."
        scene ac132 with dssb
        pause
        u "What the hell?"
        scene ac133 with dssb
        d "I fucking hate my life."
        if BTY is True:
            $ KateInsult = True
            scene ac134 with dssb
            kat "You should've just kissed me."
            d "Why would I even want to kiss you?"
            kat "Uhhh- Because I'm hot and I would've uncuffed you?"
            scene ac135 with dssa
            d "You're not hot and now get out of my face."
            scene ac136 with dssb
            u "What a fucking jerk you are."
        scene ac137 with dssb
        u "What is going on here?"
        scene ac138 with dssb
        u "Nora why are you cuffed to him?"
        scene ac139 with dssa
        u "Who even is he?"
        scene ac140 with dssb
        no "We're prisoners!"
        scene ac141 with dssa
        no "Right?"
        "You ignore her."
        scene ac142 with dssa
        mh "Ladies!"
        scene ac143 with dssa
        mh "[name]?"
        d "Coach."
        scene ac144 with dssa
        mh "What the... You know what... I don't even want to know..."
        scene ac145 with dssa
        mh "The new clothes are here, Ladies."
        mh "Let me warn you... They are revealing and very tight."
        mh "I propose the use of a bra and underwear."
        scene ac146 with dssa
        u "[name]?"
        u "The guy that beat Sai up?"
        scene ac147 with dssa
        u "Yeah, it's him."
        if RoRum is True:
            u "And apparently he also had a fling with Robin in a bathroom stall."
            scene ac148 with dssa
            u "I heard about that."
        scene ac149 with dssb
        no "[name], we need to train together now!"
        scene ac150 with dssb
        mh "What are you waiting for? Unlock yourselves."
        scene ac151 with dssa
        d "Do you think I'd still be here if we could?"
        mh "Where is the key?"
        scene ac152 with dssa
        no "In the drain!"
        scene ac153 with dssa
        mh "I'll get some help."
        d "I think Miss Marla is already looking for help."
        scene ac154 with dssa
        d "Can you stop doing that?!"
        scene ac155 with dssa
        pause
        scene ac156 with dssa
        d "Really?"
        scene ac157 with dssa
        miri "Don't tell her what to do."
        scene ac158 with vpunch
        mh "[name]? Was Stefanie already here?"
        d "Yes."
        scene ac159 with dssa
        mh "...I see."
        scene ac160 with dssa
        u "I have some lube here... You can try to wiggle out."
        scene ac162 with dssb
        kat "Why do you have lube with you?"
        scene ac161 with dssb
        "She smirks."
        scene ac163 with dssb
        "A circle of curious girls forms around you."
        scene ac164 with dssb
        u "[name]? Why did you and Sai fight?"# circle around you
        scene ac165 with dssa
        u "Did you really one punch him?"
        scene ac166 with dssa
        u "How did it feel?"
        scene ac167 with dssb
        u "Does it hurt when I touch it?"
        scene ac168 with dssa
        pause
        d "*sigh*"
        scene ac169 with dssa
        "For a moment you forget the cuffs and sit down..."
        scene ac170 with vpunch
        pause
        scene ac171 with vpunch
        no "*gasp*!"
        scene ac174 with dssb
        pause
        scene ac175 with dssa
        ma "He-"
        scene ac176 with dssb
        d "I'm cursed... I have to be!"
        "Miss Marla shakes her head."
        scene ac178 with dssa
        d "*Serious* Get off me."
        scene ac179 with dssa
        "The janitor inspects the cuffs."
        scene ac180 with dssa
        janitor "Yeah... I can't open that."
        scene ac181 with dssa
        ma "You can't?"
        scene ac182 with dssa
        janitor "This is a double locked police handcuff."
        janitor "The cops should have a universal key."
        scene ac183 with dssb
        ma "*sigh*."
        scene ac184 with dssb
        "You feel someone put something into your hand."
        scene ac186 with dssb
        d "(...It's a key.)"
        scene ac185 with dssb
        d "(She must've given Zara and Nadia the cuffs.)"
        scene ac187 with dssb
        d "Wait... Is... I found a second key!"
        miri "Where did you find it?"
        d "It was on the seat. I sat on it..."
        scene ac188 with dssa
        pause
        scene ac189 with dssa
        d "Thank god..."
        scene black with Dissolve(2)
        with Pause(.5)
        scene ac190 with dssb
        pause
        scene ac191 with dssa
        pause
        scene ac192 with dssa
        pause
        scene ac193 with dssb
        pause
        d "...I'll leave then."
        scene ac194 with dssa
        ma "Oh no. Nora and [name], you'll see me in my office on Tuesday."
        scene ac195 with dssa
        no "Why? Do we get an award for escaping the shackles?"
        scene ac196 with dssa
        ma "And you [name]. Take some time to rethink if you really don't want to tell me who cuffed you."
        scene ac195 with dssa
        no "Goodbye [name]!"
        scene black with tleaf
        with Pause(.5)
        scene ad1457 with tleaf
        d "Hi..."
        scene ad1459 with dssb
        ka "Can I help you?"
        scene ad1460 with dssa
        d "Yes, I need to find the library."
        scene ad1461 with dssa
        ka "You need an ID to borrow books."
        scene ad1458 with dssb
        d "I don't want to borrow books...  Just point me to the fucki-... direction... please."
        scene ad1462 with dssb
        ka "Walk to the end of the southwest floor, go north. Leave the building and head towards the building with the big windows."
        ka "You can't miss it from there."
        d "Thanks."
        scene ad1465 with dssb
        pause
        scene ad1466 with dssa
        d "Wait... What floor again?"
        scene ad1463 with dssb
        ka "*sigh*."
        scene ad1464 with dssa
        ka "Follow me."
        stop music fadeout 2.5
        scene black with tleaf
        with Pause(1)
        $ achievement.grant("NoraSave")
        $ achievement.sync()
        jump boardgame04




label boardgame04:
    $ play_playlist(playlist_NamiSad)
    scene ac416 with dssb
    pause
    scene ac417 with dssb
    n "Hmm, I think I got it... not."
    na "You will learn it as we play."
    so "I got it."
    scene ac419 with dssa
    n "Really?"
    so "I think so... yes."
    scene ac420 with dssb
    pause
    scene ac421 with dssa
    na "Oh, look who's here!"
    if BellaKiss3x5 is False:
        scene ac422 with dssb
        pause
        scene ac423 with dssb
        d "Thanks Karen."
        scene ac424 with dssa
        ka "You're welcome."
    else:
        pass
    scene ac425 with dssb
    n "Where the hell were you?!"
    d "I spent some time thinking."
    scene ac426 with dssb
    n "I was worried! At least tell me if you're just gonna leave out of the blue!"
    d "I'm sorry, Nami."
    scene ac427 with dssa
    d "I'm just glad to see you."
    scene ac428 with dssb
    nan "Okay [name]."
    nan "I'll explain it again."
    scene ac430 with dssb
    d "Wait a second, I'd like to talk to Nadia first."
    scene ac431 with dssa
    na "Sure."
    stop music fadeout 2.0
    scene black with tleaf
    with Pause(1)
    scene ac432 with dssb
    $ play_playlist(playlist_Ch1CollegeEnd)
    pause
    scene ac433 with dssb
    d "Let's make one thing clear."
    d "Never..."
    scene ac434 with dssa
    d "Never ever use Nami in any way against me again."
    scene ac435 with dssa
    na "You se- Nami? W-What do you mean with Nami?"
    d "You told Robin to tell me that Nami had a heatstroke!"
    scene ac436 with vpunch
    na "What? No! We didn't tell her how to do it!"
    na "We just said she should try to get you over there."
    scene ac437 with dssa
    na "I- I would never use the well being of a loved one against someone!"
    d "Stop crying."
    scene ac438 with dssa
    na "O-oh man... I-if someone had done that to me..."
    scene ac439 with dssb
    d "Nami is the most important person in my life-"
    scene ac440 with dssb
    u "Hey Nadia? Is this guy bothering you?"
    scene ac441 with dssa
    u "Leave her alone dude."
    scene ac442 with vpunch
    u "NGH!"
    scene ac443 with vpunch
    pause
    scene ac445 with dssr
    d "I'm really not in the mood to deal with some idiotic white knight!"
    scene ac446 with dssr
    na "W-wow! [name] stop."
    scene ac447 with dssa
    na "Kai, he wasn't bothering me."
    scene ac444 with dssb
    u "I should call the police! You assaulted me!"
    scene ac448 with dssr
    d "You wouldn't be talking if I assaulted you."
    scene ac449 with dssr
    "Nadia pushes you away."
    scene ac450 with dssr
    na "Sorry Kai, he didn't mean it."
    scene ac451 with dssa
    d "I totally meant it."
    na "Shut up, [name]!"
    scene ac452 with dssr
    "You stop Nadia."
    d "Did Zara tell Robin to do it?"
    scene ac453 with dssa
    na "Not that I know! I was there and would've said something!"
    na "We didn't even plan on stripping you or leaving you there at all."
    scene ac454 with dssa
    d "But you did."
    scene ac455 with dssa
    na "You showed no reaction to us! We had to do somethi-"
    scene ac456 with dssa
    d "Okay enough... So Robin is responsible for mentioning Nami?"
    scene ac457 with dssa
    na "...Not entirely... maybe. We were a little harsh when we told her to bait you..."
    scene ac458 with dssa
    d "Give me that banana."
    scene ac459 with dssb
    pause
    scene ac460 with dssa
    na "W-what?"
    d "I'm hungry."
    scene ac461 with dssa
    na "N-no! It's my banana!"
    scene ac462 with dssa
    "You stare at her."
    scene ac463 with dssb
    na "B-but... My banana..."
    scene ac464 with dssa
    pause
    menu:
        "Give her half of it.":
            $ NadiaBananaHalf04 = True
            scene ac467 with dssa
            pause
            scene ac468 with dssa
            na "...Thanks."
            scene ac469 with dssa
            pause
        "Keep it all for yourself.":
            scene ac465 with dssa
            pause
            pause
            scene ac466 with dssa
    scene ac470 with dssa
    na "Are we good?"
    scene ac472 with dssa
    d "I have done some terrible things to people before."
    scene ac473 with dssa
    na "...And bananas."
    scene ac472 with dssa
    d "It would be hypocritical to hold a grudge the second I get a taste of it myself."
    scene ac474 with dssa
    pause
    scene ac475 with dssa
    d "We're good."
    scene ac476 with dssa
    pause
    scene ac477 with vpunch
    pause
    stop music fadeout 2.5
    scene ac478 with dssb
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ac479 with dssb
    $ play_playlist(playlist_NamiSad)
    nan "Soo... Everyone will draw a card and gets a random class."
    scene ac480 with dssb
    nan "Today, we're playing a game that takes place in the future. So, as you can imagine most classes will have some futuristic skill sets."
    scene ac481 with dssb
    na "You know what, let's just play. They will learn as we go."
    scene ac483 with dssb
    "You notice Sonya looking at you."
    d "Hey Sonya."
    scene ac482 with dssa
    so "Hi [name]."
    scene ac485 with dssb
    na "Now that you're here [name]."
    scene ac484 with dssa
    na "I've made these."
    pause
    scene ac486 with dssa
    d "Oh... They look weirdly accurate."
    scene ac487 with dssa
    na "You should've seen Sonya earlier."
    scene ac488 with vpunch
    so "Hey! No!"
    n "Haha."
    n "She was playing with them."
    scene ac489 with vpunch
    so "I- I wasn't playing..."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ac490 with dssb
    pause
    scene ac491 with dssa
    so "*Whisper* B-but is that appropriate?"
    scene ac492 with dssa
    pause
    scene ac493 with dssr
    pause
    scene ac494 with vpunch
    pause
    scene ac495 with dssa
    n "Whatcha doing there?"
    so "N-nothing!"
    scene ac421 with dssb
    na "*Giggles* Okay, let off her."
    na "Let's get to everyone's class and abilities."
    stop music fadeout 2.5
    scene black with tleaf
    with Pause(1)
    jump TableTop4x5

label TableTop4x5:
    $ persistent.unlockedImageRS43 = True
    $ persistent.unlockedImageCh4x1 = True
    hide screen music_player_trigger
    scene DnDIntro with dissolve
    $ renpy.pause(4.0, hard=True)
    with Pause(76)
    scene ac254 with dssb
    show screen music_player_trigger
    play music "music/TheIntangible/The Intangible - Interdimensional Amity.ogg"
    pause
    scene ac255 with dssb
    na "ETA?"
    scene ac256 with dssa
    ai "15 minutes, Ma'am."
    scene ac255 with dssa
    na "Brief us."
    scene ac256 with dssa
    ai "A colony in the Venese-Systems has gone dark. No sign of life."
    ai "Investigate and secure potential survivors."
    scene ac257 with dssb
    nan "Threat level?"
    ai "Unknown."
    scene ac258 with dssb
    pause
    scene ac259 with dssa
    d "Dude..."
    n "Mh?"
    scene ac260 with vpunch
    pause
    d "Make them normal..."
    scene ac261 with dssa
    n "What?! That's my normal size!"
    d "It's not."
    scene ac262 with vpunch
    n "Hey! If I want to play as a big tiddy girl! THEN SO I WILL!"
    n "Right?"
    scene ac263 with dssb
    na "Sure. Customize yourself however you want."
    na "You could play as a female, [name]."
    n "I like your outfit."
    scene ac264 with dssa
    na "Thanks! You can be lucky and get different outfits in the end game reward."
    scene ac263 with dssa
    na "Okay, let's go over your skills."
    na "As a Technician you're the only one capable of engineering."
    na "You can get us access through locked doors, re-activate androids, robots and turrets."
    scene ac264 with dssa
    na "It's crucial that you stay alive."
    scene ac265 with dssb
    n "Soo cool!"
    scene ac267 with dssa
    pause
    scene ac266 with dssa
    n "Are you lookin' at me?!"
    scene ac268 with dssb
    pause
    scene ac269 with dssb
    na "[name], as an Agent you're the only one here with a realistic chance to deal critical damage."
    na "We don't know what we might face but taking out something dangerous quickly, is your job."
    scene ac270 with dssa
    na "You also got stealth abilities... The chance of you being detected is lower. But more about that later."
    scene ac271 with dssa
    d "I see."
    scene ac272 with dssb
    pause
    scene ac273 with vpunch
    d "...You were asking if I was looking at you?"
    scene ac274 with dssb
    so "And I can heal people?"
    na "Yes."
    scene ac275 with dssb
    na "We've got three states of being wounded."
    scene ac276 with dssb
    na "State 1, not life threatening and you're still at 85 to 99 percent functionality."
    scene ac277 with dssa
    na "State 2 is more critical. You need to either selfcare with a full medic pack."
    na "Or a Medic like Sonya can even heal you with a normal bandage."
    scene ac278 with dssa
    na "Level three injuries are life threatening and require immediate care."
    na "Only Sonya is capable of getting you out of the level three state... Otherwise..."
    scene ac279 with dssa
    na "...Death is certain."
    scene ac280 with dssb
    ai "Arriving in two."
    na "Get ready."
    stop music fadeout 2.5
    scene ac281 with dssb
    pause
    $ play_playlist(playlist_DarkAmbientDnDx)
    scene ac282 with dssb
    pause
    scene ac283 with dssb
    pause
    scene ac284 with dssa
    n "I'm scared."
    so "Me too."
    scene ac286 with dssb
    d "Where's badass Nami?"
    scene ac284 with dssb
    n "You see these tiddies? It means I'm badass by default!"
    scene ac287 with dssb
    na "Squad! Prepare for the arrival!" # Honor the brave hampus
    scene ac288 with dssb
    pause
    scene ac290 with dssb
    pause
    scene ac291 with dssb
    pause
    scene ac292 with dssb
    pause
    scene ac293 with dssb
    nan "Secure the area."
    scene ac294 with dssb
    "Sonya stays close to you as you secure the left side."
    scene ac296 with dssb
    d "Be on alert."
    scene ac297 with dssa
    pause
    scene ac298 with dssb
    d "Clear?"
    scene ac299 with dssb
    so "Clear."
    scene ac300 with dssb
    n "Clear."
    scene ac301 with dssb
    na "Clear."
    scene ac302 with dssb
    nan "Nothing unusual."
    scene ac303 with dssb
    na "Besides the fact that we couldn't reach anyone in the colony."
    scene ac304 with dssa
    d "It's too silent for a colony."
    so "The doors are all security locked."
    scene ac305 with dssa
    na "I think we can rule out an alien invasion."
    d "It's much smarter to infiltrate a society piece by piece instead of attacking it openly."
    n "I agree. If an attack had happened, the colony could've sent an emergency signal."
    scene ac306 with dssa
    d "I don't like this place."
    scene ac307 with dssa
    so "Why?"
    d "It's too open and perfect for an ambush."
    scene ac308 with dssb
    nan "And the fog hides potential threats."
    scene ac309 with dssa
    na "The fog is unusually thick."
    scene ac310 with dssa
    nan "Yeah, I was never here before... maybe it's a thing here?"
    scene ac311 with dssb
    n "Hey! I found something."
    na "What is it?"
    scene ac312 with dssb
    n "I managed to unlock the terminal and it grants us all an ability card!"
    na "Perfect!"
    scene ac313 with dssb
    pause
    scene ac314 with dssa
    pause
    scene ac315 with vpunch
    pause
    scene ac316 with dssb
    so "What is it?"
    scene ac317 with dssa
    d "I don't know... But be on high alert."
    so "I am."
    scene ac318 with dssb
    n "Hmm..."
    scene ac319 with dssa
    n "AH! Awww! Yes!"
    scene ac320 with dssb
    d "What did you get?"
    scene ac321 with dssb
    n "HIM!"
    scene ac322 with dssa
    "Beep Beep boop!"
    scene ac323 with dssa
    n "How cuuuute!"
    scene ac324 with dssb
    na "That's a really good card. It's under the 'Very Rare' equipment."
    scene ac325 with dssa
    "Nadia taps on the interface."
    scene ac326 with dssa
    pause
    scene ac327 with dssb
    na "Oh no!"
    na "I... *sigh* I got a glowstick deployer... Common trash."
    scene ac328 with dssb
    pause
    scene ac329 with dssa
    pause
    scene ac330 with dssa
    nan "I got five security beacons!"
    d "What can the-"
    scene ac331 with dssb
    nan "They act as motion detectors."
    nan "They light up and make a noise when a neutral or hostile entity enters its range."
    scene ac332 with dssb
    pause
    scene ac333 with dssa
    pause
    scene ac334 with dssa
    so "Oh."
    n "What did you get?"
    scene ac335 with dssa
    pause
    n "Oh fuck... No!"
    scene ac336 with dssa
    na "Oh! That's a very good item!"
    na "It can heal up to two injury states in an instant!"
    scene ac337 with dssb
    so "It only holds three charges, though."
    scene ac338 with dssb
    pause
    scene ac339 with dssb
    pause
    scene ac340 with dssa
    pause
    scene ac341 with dssa
    d "Hmm... Camouflage."
    scene ac342 with dssb
    na "Check your PA."
    scene ac343 with dssb
    pause
    d "Yeah, it added something."
    scene ac344 with dssb
    n "Try it out!"
    scene ac345 with dssb
    pause
    scene ac346 with dssa
    pause
    scene ac347 with dssb
    pause
    scene ac348 with dssa
    d "Uhh... It's hard to control your body when you can't see it..."
    n "Sure."
    scene ac349 with vpunch
    "BEEEP!"
    scene ac350 with dssa
    n "No no, he's no ghosty! You don't need to be afraid."
    scene ac351 with dssb
    n "...Don't misuse it to spy on me in the shower."
    scene ac352 with dssb
    pause
    na "All doors are security locked."
    scene ac353 with dssb
    na "Nami, see if you can open it."
    scene ac354 with dssb
    "BEEEP!"
    n "Mh? You want some oily snacks?"
    scene ac355 with dssa
    $ persistent.unlockedImageNamiCh41 = True
    $ persistent.unlockedImageRS44 = True
    "The little robot points at the door."
    n "Sure! Open it!"
    scene ac356 with dssb
    pause
    scene ac357 with dssa
    pause
    scene ac358 with dssb
    n "Good boy!"
    scene ac359 with dssa
    n "Who's a good boy?!"
    scene ac360 with vpunch
    n "YES EXACTLY! Yooou!"
    scene ac362 with dssb
    pause
    scene ac361 with vpunch
    n "HEY!"
    scene ac364 with dssb
    nan "*laughs*!"
    nan "The robot is a little pervert!"
    scene ac363 with dssa
    n "You gotta earn these tiddies first!"
    scene ac365 with dssb
    n "*Whisper* You can touch em anytime."
    d "*Whisper* I'll put that gun up your ass."
    scene ac366 with dssa
    n "*Whisper* Joke's on you... I like that."
    scene ac367 with dssa
    na "Alright... Get in position. We're going in."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ac368 with dssb
    pause
    na "Careful."
    d "Keep the ceiling in mind."
    scene ac369 with dssb
    n "What is this fog?"
    scene ac370 with dssa
    nan "No idea."
    scene ac369 with dssa
    so "I- I hope it's not poisonous."
    scene ac371 with dssb
    pause
    d "No sign of life."
    scene ac372 with dssb
    n "We can rule out a hardware problem."
    scene ac373 with dssb
    na "No sign of any extraterrestrial life either."
    scene ac374 with dssa
    pause
    scene ac375 with dssb
    "Everyone stares at Sonya."
    scene ac376 with dssb
    pause
    scene ac377 with dssb
    so "W-what is that?"
    na "It's a trap."
    $ play_playlist(playlist_DarkAmbientDnD)
    scene ac378 with dssb
    pause
    scene ac379 with dssb
    pause
    scene ac380 with dssb
    pause
    scene ac381  with dssb
    n "What's going on?"
    na "I think the power went offline."
    scene ac382 with dssb
    nan "More like got shut off."
    scene ac383 with dssb
    pause
    scene ac384 with dssa
    pause
    scene ac385 with dssb
    d "I hear... weird noises."
    scene ac386 with dssa
    n "The FUCK was that?!"
    scene ac387 with dssa
    pause
    scene ac388 with dssb
    pause
    scene ac389 with dssb
    pause
    scene ac390 with dssa
    pause
    scene ac391 with dssb
    so "We're... being hunted down."
    scene ac392 with dssa
    n "B-by what?"
    scene ac393 with dssb
    na "If it's hunting us..."
    scene ac394 with dssb
    na "It will come to us."
    scene ac395 with dssa
    pause
    scene ac396 with dssb
    pause
    scene ac397 with dssa
    pause
    scene ac398 with dssb
    d "What's the plan?"
    scene ac399 with dssb
    na "Power. We need to get the power back online."
    na "If-... When we encounter hostiles, we'll need the colonies defensive mechanisms."
    scene ac400 with dssb
    so "What are they?"
    scene ac401 with dssa
    na "I've got no idea. But maybe some androids."
    scene ac402 with dssb
    d "Let's proceed down the corridor."
    nan "Also... Shoot first, ask later."
    scene ac403 with dssb
    pause
    scene ac404 with dssb
    na "Clear."
    scene ac405 with dssb
    "Nancy throws a motion detector."
    scene ac406 with dssa
    nan "In case something's following us."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ac496 with tleaf
    d "Cheeto."
    d "Let's check this room."
    scene ac498 with dssb
    n "I open the door, you go in."
    scene ac497 with dssa
    d "Do it."
    scene ac499 with dssb
    pause
    scene ac500 with vpunch
    pause
    scene ac501 with dssb
    d "Clear."
    scene ac502 with dssa
    pause
    scene ac503 with dssa
    "You turn on the flashlight."
    scene ac504 with dssb
    d "(A map.)"
    scene ac505 with dssb
    d "Nadia, I've found a map."
    scene ac506 with dssa
    na "Let me see."
    scene ac507 with dssa
    na "Hmm, the power room is not far from here."
    scene ac508 with dssb
    nan "Nami, send your Robo to scout."
    scene ac509 with dssb
    n "What?! No!"
    n "He's so cute! I don't want him to get hurt."
    nan "It's either him or us."
    scene ac510 with vpunch
    n "Okay, then you go scout!"
    scene ac511 with vpunch
    nan "No! He goes!"
    scene ac512b with dssb
    "The little robot shakes his head wildly."
    scene ac513b with dssb
    "You leave the room again."
    scene ac514b with dssa
    d "*Sigh*"
    scene ac515b with dssb
    na "Mh?"
    scene ac516b with dssa
    d "We fucked up."
    scene ac517b with dssa
    $ persistent.unlockedImageCh4x2 = True
    d "We should've never let this room out of our sight..."
    stop music fadeout 2
    hide screen music_player_trigger
    scene Rebellion with dissolve
    $ renpy.pause(4.0, hard=True)
    with Pause(30)
    scene ad298 with vpunch
    show screen music_player_trigger
    play music "music/tabletop/Flee you fools.ogg"
    pause
    scene ad299 with vpunch
    "You take cover behind a stone table."
    pause
    scene ad300 with dssa
    "You get up and shoot at one of those black silhouettes."
    scene ad301 with vpunch
    pause
    scene ad302 with vpunch
    "A loud roar echoes through the room."
    d "There's a big one!"
    scene ad303 with dssb
    n "Holy shit!"
    scene ad304 with vpunch
    na "Get down!"
    scene ad305 with vpunch
    na "[name]! RUN! We can't win this!"
    $ persistent.unlockedImageRS48 = True
    scene ad306 with vpunch
    stop music fadeout 5.0
    "You all scatter in different directions."
    scene ad307 with dssb
    "Corner after corner you run without stopping."
    scene ad308 with dssa
    $ play_playlist(playlist_DarkAmbientDnD)
    "You pause for a moment, listening to the surroundings."
    scene ad309 with dssa
    d "(Something is approaching.)"
    scene ad310 with dssa
    "You jump behind the pillar and turn on the camouflage."
    scene ad311 with dssb
    pause
    scene ad312 with dssb
    pause
    scene ad313 with dssb
    d "(Why isn't he with Nami? I hope she's alright.)"
    scene ad314 with dssa
    d "Pss!"
    scene ad315 with dssa
    pause
    scene ad316 with vpunch
    "Suddenly, an Alien bursts into the room."
    scene ad317 with dssb
    pause
    scene ad318 with dssb
    pause
    scene ad319 with dssa
    pause
    scene ad320 with vpunch
    pause
    scene ad321 with dssa
    pause
    scene ad322 with dssa
    d "..."
    scene ad323 with dssa
    "The little robot beeps in a sad tone."
    d "*Sigh*"
    d "Get up. We need to move."
    scene ad325 with dssb
    pause
    scene ad326 with dssb
    "The robo grabs the alien's tongue."
    scene ad327 with dssb
    d "What are you doing? Leave his tongue alone."
    scene ad328 with dssb
    pause
    d "(I've gotta find the others. If they're smart they'll head towards the power room.)"
    scene ad329 with dssa
    "The robot beeps and holds his little arms up."
    d "I see. Stairs."
    scene ad330 with dssa
    "You grab the little robot and get up the stairs."
    scene black with tleaf
    with Pause(.5)
    scene ad332 with tleaf
    pause
    scene ad333 with dssb
    pause
    scene ad334 with dssa
    pause
    scene ad335 with dssa
    d "We're not alone."
    scene ad336 with dssa
    "Beep!"
    d "(My camouflage is still on cooldown.)"
    scene ad337 with dssb
    pause
    scene ad338 with dssa
    pause
    scene ad339 with vpunch
    pause
    scene ad340 with dssa
    pause
    scene ad341 with dssa
    "You try to get up before the alien attacks again."
    scene ad342 with vpunch
    pause
    scene ad343 with dssa
    pause
    scene ad344 with dssb
    pause
    d "Good to see you."
    scene ad345 with dssb
    na "Good to see you, too."
    scene ad346 with dssa
    na "It followed me here..."
    na "I just didn't know how many there were."
    scene ad347 with dssb
    d "Do you know what happened to the others?"
    scene ad348 with dssa
    na "No."
    na "You're the only one I've found."
    scene ad349 with dssa
    d "Let's go to the power room."
    scene ad350 with dssa
    na "Oh hey."
    scene ad351 with dssb
    "BEEP!"
    na "Where's Nami?"
    scene ad352 with dssa
    "*Sad beep*"
    scene ad353 with dssb
    na "Hmm, I've got no idea what he's saying."
    d "*Chuckles* Me neither."
    scene ad354 with dssb
    na "This way we get to the power room."
    scene ad355 with dssb
    d "Ready?"
    na "Yes."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad356 with dssb
    pause
    scene ad357 with dssa
    pause
    scene ad358 with dssb
    pause
    scene ad359 with dssb
    pause
    scene ad360 with dssb
    na "Clear on first sight."
    scene ad361 with dssb
    na "It seems like the others aren't here yet."
    d "Then we've gotta do it ourselves."
    scene ad362 with dssb
    na "We can't. We need Nami."
    scene ad363 with dssb
    d "What about him?"
    na "He needs Nami to access the main frame."
    scene ad364 with dssb
    d "I hope the Cheeto is still alive."
    scene ad365 with dssb
    na "But we can't just stay here. They might be in trouble."
    na "There should be two paths we can take."
    na "Path one... well, is the main hallway."
    scene ad366 with dssa
    na "We'd take some smaller side ways in order to minimise the chance of engaging hostiles."
    scene ad367 with dssa
    d "Path two is?"
    scene ad365 with dssa
    na "I uh... I don't know."
    na "The station scanner did scan this area but it's... different?"
    scene ad368 with dssb
    d "Different good or different bad?"
    scene ad369 with dssa
    na "Let's be real... It will be bad."
    scene ad370 with dssa
    d "We'll see when we get there."
    play music "music/Tabletop/proxima-centauri.ogg"
    scene ad371 with vpunch
    "BEEP!"
    scene ad372 with vpunch
    pause
    na "Put the gun down!"
    scene ad373 with dssa
    UnAi "OCE Special forces detected."
    scene ad374 with dssa
    na "An android with an AI."
    d "Aren't they forbidden?"
    na "Yes."
    scene ad375 with dssa
    UnAi "I'm not hostile."
    d "Yet."
    scene ad376 with dssb
    na "You shouldn't exist."
    scene ad377 with dssa
    UnAi "And yet... I do."
    scene ad376 with dssa
    na "Who created you?"
    UnAi "A colonist."
    d "Where's he?"
    UnAi "Unknown."
    na "What do you mean? You must know what happened."
    scene ad375 with dssb
    UnAi "The colony's emergency systems woke me up. The colony was about to run out of energy."
    UnAi "I've got no information regarding my creator's current state."
    d "He was gone?"
    scene ad378 with dssa
    UnAi "Everyone was."
    UnAi "Before the aliens arrived, I've not encountered a single biological form of life."
    scene ad379 with dssb
    d "What about non-biological?"
    UnAi "No. My protocols forbid me to activate synthetic or robotic life."
    scene ad380 with dssb
    na "Any other information?"
    UnAi "During the night, my scanners do occasionally detect something."
    na "Like what?"
    scene ad379 with dssb
    UnAi "Sounds of unknown origin."
    d "The aliens aren't responsible for the colony going dark?"
    UnAi "No."
    scene ad381 with dssb
    "You and Nadia share a look."
    scene ad382 with dssb
    na "What could it be?"
    scene ad383 with dssa
    UnAi "It's my mission to find out."
    scene ad384 with dssa
    d "Join us."
    scene ad385 with dssa
    UnAi "As you wish."
    scene ad384 with dssa
    d "What's your name?"
    na "Androids don't have nam-"
    scene ad385 with dssa
    cy "Cyphi."
    stop music fadeout 2.5
    scene black with Dissolve(2)
    with Pause(.5)
    jump PathOne4x0

label PathOne4x0:
    $ play_playlist(playlist_DarkAmbientDnD)
    scene ad386 with dssb
    d "Clear."
    scene ad387 with dssb
    na "Clear!"
    scene ad388 with vpunch
    na "NOT CLEAR!"
    scene ad389 with vpunch
    pause
    scene ad390 with dssb
    d "Was it only one?"
    na "Yes but we should move! They must've heard that."
    scene ad391 with vpunch
    "An alarm echoes from a nearby room."
    scene ad392 with dssa
    na "Nancy's motion detectors!"
    scene ad391 with dssa
    d "We're on the right path."
    d "Nadia! Cyphi! Go back and let me see if I can do something."
    scene ad392 with dssa
    na "What? No!"
    scene ad394 with dssb
    d "GO!"
    scene ad395 with dssa #ray phase
    pause
    stop music fadeout 2
    scene ad396 with dssb
    $ persistent.unlockedImageNadia6 = True
    d "(Four.)"
    play music "music/tabletop/Flee you fools.ogg"
    scene ad397 with dssb
    d "(I've got an idea.)"
    scene ad399 with dssb
    pause
    scene ad398 with vpunch
    "You punch the alien in the head."
    scene ad400 with vpunch
    "It turns around furiously..."
    scene ad401 with dssb
    "A third alien tries to break them up."
    scene ad402 with dssa
    pause
    scene ad403 with vpunch
    "You kill two of them with one shot."
    scene ad404 with dssa
    pause
    scene ad405 with dssb
    pause
    scene ad406 with vpunch
    "You immediately shoot the third one."
    scene ad407 with dssb
    pause
    "The last alien stares at you in pure terror."
    scene ad408 with dssb
    "It makes a big leap and runs away."
    scene ad409 with vpunch
    pause
    na "Watch where you're going."
    scene ad410 with dssa
    na "Is it the last one?"
    scene ad411 with dssa
    d "Out of this group? Yes."
    na "Do you want him or...?"
    scene ad412 with dssb
    menu:
        "Let Nadia kill the alien.":
            $ persistent.unlockedImageNadia7 = True
            $ LetNadiaHaveTheKill4x0 = True
            scene ad413 with dssa
            d "No. It's yours... I can't have all the fun."
            scene ad414 with vpunch
            pause
            scene ad422 with dssb
            na "Good work dealing with them."
        "Kill it yourself.":
            $ KilledTheAlienYourself = True
            scene ad415 with dssa
            d "Let's not waste our time with that grey boy."
            scene ad416 with vpunch
            pause #shot
        "Spare him.":
            $ AlienLeftALive = True
            d "The aliens aren't responsible for this... but we're still in combat with them."
            d "Let him live."
            scene ad420 with dssa
            na "Are you serious? He might just get his friends and come after us?"
            scene ad421 with dssa
            d "If that happens you and I get to have some fun."
            scene ad422 with dssa
            na "...The good type of fun?"
            d "No. The best type of fun."
            scene ad423 with dssa
            "Nadia chuckles."
            scene ad417 with dssa
            d "Hey, you can go."
            scene ad418 with dssa
            pause
            scene ad419 with dssa
            pause
    scene ad424 with dssb
    stop music fadeout 2
    d "So, Nancy must've come this way?"
    na "Yes."
    $ play_playlist(playlist_DarkAmbientDnD)
    scene ad425 with dssb
    d "And this is the other way?"
    na "The alien way..."
    scene ad426 with dssb
    d "The fun way."
    scene ad427 with dssb
    cy "I advise against this way. It wasn't created by the colonists nor by the aliens."
    scene ad428 with dssa
    d "I doubt the others would've taken this path anyway. The Cheeto is too big of a chicken."
    d "We'll check it out when we find them."
    scene ad429 with dssa
    na "I agree."
    if AlienLeftALive or LetNadiaHaveTheKill4x0 is True:
        scene ad430 with dssb
    else:
        scene ad431 with dssb
    d "What I find weird... the metal is bent to the inside."
    na "They came from... down there and entered the colony?"
    d "That's what I think."
    scene ad432 with dssb
    "The little robot tries to push you away from the entrance."
    d "Don't worry... We're not going down there... yet."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad434 with dssb
    na "Look!"
    d "All dead."
    d "Nancy?"
    scene ad435 with dssb
    na "No, it looks like they were in close combat."
    na "This one here is weird... Like it's ripped open."
    d "A third faction? The ones that are responsible for the colony?"
    scene ad436 with dssb
    na "We've gotta be careful."
    scene ad437 with vpunch
    "BEEP!"
    d "Mh?"
    na "What is it?"
    scene ad438 with dssb
    "The little robot drives to the green door."
    d "That little chicken never drives ahead..."
    scene ad439 with vpunch
    "BEEP!"
    cy "Lifeform detected. The room is not empty."
    d "Let me go in first."
    scene ad440 with dssb
    pause
    scene ad441 with dssb
    pause
    "You hear a quiet noise from the right."
    scene ad442 with dssb
    d "Nami!"
    scene ad443 with vpunch
    n "*GASP*!"
    scene ad444 with vpunch
    d "Wow wow!"
    scene ad445 with dssa
    n "O-oh my god!"
    scene ad446 with vpunch
    "Nami jumps into your arms."
    scene ad447 with dssb
    n "[name]! T-there's something i-in here!"
    scene ad448 with dssa
    d "What?"
    scene ad449 with dssa
    n "I-it came through the v-vent!"
    d "I don't see anything."
    scene ad450 with dssa
    na "Hey!"
    n "N-adia..."
    na "Did you kill the aliens outside?"
    n "N-no."
    scene ad451 with dssa
    d "She said there was something in here."
    scene ad452 with dssa
    cy "Your stress levels are off the charts."
    cy "I suggest calming down."
    scene ad453 with dssa
    n "...Who are you?"
    na "She's a synth."
    scene ad454 with dssa
    d "Cheeto, what killed them?"
    scene ad455 with dssb
    n "Dude! It was so scary!"
    n "When I ran away, the aliens followed me in here... and then I heard a noise and I realised I wasn't alone in this room."
    n "As soon as the aliens entered, it fucked them! L-like ripped them apart- a-and the noises it made! Dude!"
    scene ad456 with dssb
    d "Nadia, it seems like it was the same thing that killed the one we found."
    na "Yeah."
    scene ad457 with dssa
    d "Did you see Sonya? Nancy?"
    scene ad458 with dssa
    n "Nancy was right behind me but after a few corners I was alone."
    n "Sonya went right while Nancy and I went left."
    scene ad459 with dssa
    n "Even my Robo is gone..."
    scene ad460 with dssb
    d "He's here. I took care of him."
    scene ad461 with dssa
    n "Ohhh! You took care of our baby!"
    scene ad462 with dssb
    "*Happy beeping*"
    d "We need to get Nami to the power room."
    scene ad463 with dssb
    na "Yeah, let's go."
    scene ad464 with dssb
    d "Everything's going to be okay."
    scene ad465 with dssa
    n "Man... I was so scared..."
    n "I thought I'm a badass... but I- I couldn't move. I was frozen in fear."
    scene ad464 with dssa
    d "It happens."
    d "Did you see what it looked like?"
    scene ad465 with dssa
    n "No. I just hid there and- I was too scared to look... I just heard it screeching and the aliens screaming."
    scene ad464 with dssa
    d "Alright. Let's go."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad467 with dssb
    n "Hmm, one of the energy junctions is offline."
    "Beeeeeeeeeeeeeeeeeeeeep!"
    n "I know, I know!"
    scene ad468 with dssb
    n "It requires a manual restart."
    scene ad469 with dssb
    d "I'll go."
    scene ad470 with dssb
    n "Not alone!"
    d "I've got camouflage."
    n "Take my robo with you. He knows how to operate it."
    n "Your camouflage should work with him as he's small enough to be covered."
    scene ad472 with dssb
    na "As soon as the junction is restarted, change your radio frequency to 15.3.5.1.14."
    scene ad471 with dssb
    d "Got it."
    scene ad473 with dssb
    na "Also... See if you can find Sonya and Nancy."
    "You nod."
    scene ad473a with dssr
    na "Are you feeling better?"
    scene ad473b with dssa
    n "Yeah, the pill she gave me calmed me down."
    scene ad473a with dssa
    na "In this particular case it might've been better that you were frozen."
    scene ad473b with dssa
    n "Yeah, I think it would've killed me too."
    scene ad473c with dssr
    cy "Considering the creature's track record, there's a 98 percent chance it would have killed you."
    scene ad473d with dssa
    n "...Thanks."
    scene black with tleaf
    with Pause(.5)
    scene ad1467 with tleaf
    pause
    scene ad1468 with dssa
    pause
    scene ad1469 with dssa
    "*inaudible Alien noises.*"
    scene ad1470 with dssa
    pause
    scene ad1471 with dssa #sfx
    pause
    scene ad1472 with dssa
    d "(The air is unusually moist.)"
    scene ad1473 with dssa
    "Beep!"
    d "No... You touched me inappropriately."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad1476 with dssa
    "You make it down to an old pumping station... In hope you can avoid most of the alien patrols."
    scene ad1475 with dssb
    pause
    scene ad1477 with dssa
    d "(...If that's what I think it is we've got a big problem.)"
    scene ad1474 with vpunch
    pause
    $ persistent.unlockedImageRS54 = True
    d "(Yup... A fucking Sentinel.)"
    d "(I've got no interest in dealing with one.)"
    scene ad1478 with dssa
    mya "Human... The one... walking in the shadows."
    scene ad1479 with dssb
    pause
    scene ad1480 with dssa
    mya "I can sense your presence."
    scene ad1481 with dssb
    pause
    scene ad1482 with dssa #sfx
    pause
    scene ad1483 with dssa
    "Suddenly, an invisible force pulls you from the ground."
    scene ad1484 with dssa
    "BEEEP!"
    scene ad1485 with dssb
    pause
    scene ad1486 with dssa
    d "You speak my language."
    scene ad1487 with dssa
    mya "Your kind still communicates in a very primitive way."
    "*Sad* Beep."
    scene ad1488 with dssa
    d "Say... Are you friend... or foe?"
    scene ad1490 with dssb
    pause
    scene ad1491 with dssa
    mya "Neither."
    scene ad1492 with dssa
    d "Your alien friends... Did you kill them?"
    scene ad1493 with dssa
    mya "I'd never kill my kind."
    scene ad1494 with dssa
    mya "Your kind on the other hand..."
    scene ad1495 with dssa
    pause
    scene ad1496 with dssb
    "You can feel the small vibrations resonating from the blade."
    scene ad1497 with dssb
    d "You guys aren't responsible for the colony going dark. What is?"
    scene ad1498 with dssb
    mya "We've spent centuries trying to locate all ancient facilities."
    mya "Your kind was unlucky enough to build a colony right above one."
    mya "Its foundation had grown evil roots."
    scene ad1499 with dssa
    d "Stop speaking in riddles and tell me what's going on here."
    scene ad1500 with dssa
    mya "All facilities once inhibited something. And until now all facilities were empty except one."
    mya "The one that wasn't led to the fall of an entire star system."
    scene ad1501 with dssa
    d "...I heard the rumors."
    d "That's why you guys accepted the unfavorable peace treaty... You had to fight a war inside."
    d "And by being here, you're breaking said contract."
    scene ad1502 with dssa
    mya "This facility isn't empty either."
    d "The facility is beneath us?"
    scene ad1503 with dssa
    mya "Yes."
    scene ad1504 with dssb
    d "Alright... I kinda need to go."
    scene ad1505 with dssa
    mya "The energy junction you're looking for has been destroyed."
    scene ad1506 with dssa
    d "Why should I believe you?"
    scene ad1507 with dssa
    stop music fadeout 5.0
    mya "There's a much greater threat at work here..."
    scene ad1508 with dssa
    play music "music/TheIntangible/The Intangible - Interdimensional Amity.ogg"
    mya "As you hairy creatures like to say... The enemy of my enemy is my friend."
    scene ad1509 with vpunch #sfx
    pause
    scene ad1510 with dssb
    d "Let's pretend it is destroyed... How do we get online again?"
    mya "The ship we arrived in could power the entire colony."
    d "There's a reason you haven't done it yet."
    mya "There's something outside. It's roaming the area and cut our way to the ship."
    scene ad1511 with dssa
    d "Let's kill it."
    mya "It's not that easy."
    mya "You and your shadow walk might be the solution."
    scene ad1512 with dssa
    d "I have to brief my team."
    scene ad1513 with dssb
    mya "But before you do that..."
    play music "music/Suspense/Scott Buckley - Nightfall.ogg"
    scene ad1514 with vpunch
    pause
    scene ad1710 with dssa
    pause
    scene ad1711 with dssa
    pause
    scene ad1712 with dssa
    pause
    scene ad1714 with dssb
    pause
    scene ad1713 with dssa
    pause
    scene ad1715 with vpunch
    $ persistent.unlockedImageRS57 = True
    na "NANCY! I- I told you not to put these cards in here!"
    nan "I- t-thought it might be fun?!"
    scene ad1734 with vpunch
    "Nadia grabs Nancy and drags her a few feet away..."
    scene ad1735 with vpunch
    na "Do you want them to quit on their first day?!"
    na "We said we wouldn't use these cards!"
    scene ad1737 with dssa
    nan "I'm so sorry! I thought it might be fun..."
    scene ad1736 with dssb
    na "They will think, I'm a w-weirdo!"
    scene ad1738 with dssb
    nan "Sorry..."
    scene ad1716 with dssb
    na "Sorry sorry... Nancy just did a little prank."
    scene ad1717 with dssa
    d "You know we could hear you, right?"
    scene ad1718 with dssa
    n "What's up with these cards?"
    scene ad1719 with dssa
    na "Nothing Nami... Just a prank... Haha."
    "Nadia continues to do a really bad fake laugh."
    n "Come on! Tell us!"
    scene ad1720 with dssb
    nan "*sigh* These are my cards."
    d "They're not."
    scene ad1721 with vpunch
    nan "Well! It shouldn't matter whose cards they are!"
    d "Exactly... So tell us what's up with them."
    scene ad1722 with dssa
    na "...These cards add a different layer to the game."
    n "A spicy one?"
    scene ad1723 with dssa
    na "Yup."
    na "They add new events, enemies and actions... Sometimes of a sexual nature."
    scene ad1727 with dssa
    n "Then why aren't we playing with them?"
    scene ad1724 with vpunch
    na "Why? Would you want that?"
    scene ad1728 with dssa
    n "Sure!"
    d "Don't let the Cheeto near those cards."
    scene ad1729 with dssb
    n "Afraid of what I might do to you?"
    scene ad1730 with dssa
    stop music fadeout 2.0
    d "*Serious* Yes."
    scene ad1726 with dssb
    play music "music/TheIntangible/The Intangible - Interdimensional Amity.ogg"
    "After hearing your responses, Nadia visibly lightens up."
    scene ad1725 with dssa
    na "I- mean we can- maybe try them in the next session?"
    na "We won't be finishing this scenario today anyways."
    scene ad1731 with vpunch
    n "Yes!"
    scene ad1732 with dssa
    n "Right Sonya?"
    scene ad1733 with dssb
    so "Uuuh- Sure."
    scene ad1725 with dssa
    na "Yes... We'll decide before the next session."
    d "Now give me a normal card."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad1511 with dssa
    d "Let's kill it."
    mya "It's not that easy."
    mya "You and your shadow walk might be the solution."
    scene ad1512 with dssa
    d "I have to brief my team."
    scene ad1513 with dssb
    mya "But before you do that..."
    scene ad1515 with vpunch
    d "NRGH!"
    scene ad1516 with dssa
    d "...T-The fuck did you do?!"
    scene ad1517 with dssa
    mya "I've programmed a map of the entire station into your head... and you've been marked. My kind will not shoot on sight."
    mya "You and your team can meet us at the 4N exit."
    mya "It's closest to the ship."
    scene ad1518 with dssa
    d "Our scanners didn't detect any lifeforms outside."
    scene ad1519 with dssa
    mya "The creature isn't really alive... But it's not dead either."
    mya "We call it a biological accident."
    mya "It moves without making any noise, which is remarkable considering its size."
    if AlienLeftALive is True:
        scene ad1520 with dssa
        mya "Human, you showed mercy to one of my kind."
        mya "Thank you."
    scene ad1521 with dssb
    "You slowly start hovering back to the edge."
    scene ad1522 with dssa
    pause
    scene black with Dissolve(2)
    scene ad1523 with dssb
    pause
    scene ad1524 with vpunch
    cy "Unknown entity approaching!"
    scene ad1525 with dssb
    pause
    scene ad1526 with dssa
    d "Yo!"
    n "It's [name]!"
    cy "It's not! His biological markers have changed."
    scene ad1527 with dssa
    na "Identify yourself!"
    d "It's me you cunts."
    scene ad1528 with dssa
    "Beep!"
    scene ad1527 with dssa
    d "...It's us you cunts."
    scene ad1529 with dssb
    n "At least it sounds like [name]."
    scene ad1530 with dssa
    d "My markers might've changed from the touch of the alien."
    scene ad1531 with dssa
    n "What? Are you infected?!"
    scene ad1527 with dssb
    d "No! A Sentinel programmed a map into my head."
    scene ad1532 with dssb
    na "What? Why aren't you at the junction?"
    scene ad1533 with dssb
    d "Something came up..."
    scene ad1534 with dssb
    n "What do you mean, he touched you inappropriately?"
    scene ad1535 with dssa
    n "And you saw some big alien boobs and butt?"
    scene ad1536 with dssa
    n "Where did you take him?! To an alien strip club?!"
    scene ad1537 with dssb
    "You tell them about the talk with the Sentinel."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad1538 with dssb
    na "And you believe that?"
    scene ad1539 with dssa
    d "I do."
    scene ad1540 with dssa
    na "Based on what facts?"
    scene ad1541 with dssa
    d "My gut."
    scene ad1542 with vpunch
    n "Weirdo gut!"
    d "Shut up."
    scene ad1543 with dssa
    na "What now?"
    scene ad1544 with dssa
    n "We have to find Sonya and Nancy!"
    scene ad1545 with dssa
    na "We should lay a trap for the aliens."
    d "No. We'll work with them."
    na "We can't trust them!"
    scene ad1546 with dssa
    d "Nadia!"
    d "There's something here that kills both us and the aliens!"
    d "If we keep killing each other then whatever else is here is going to finish the survivor off!"
    d "And as Cyphi said, the aliens weren't responsible for the colony going dark."
    stop music fadeout 2.0
    scene ad1547 with dssa
    play music "music/Tabletop/proxima-centauri.ogg"
    na "It's easier to just shoot everything!"
    scene ad1548 with vpunch
    d "Maybe I should start with you."
    scene ad1549 with vpunch
    na "Oh? You wanna dance?"
    d "I wanna dance."
    scene ad1550 with dssb
    d "Trust me."
    scene ad1551 with dssa
    na "You haven't earned my trust yet."
    na "But... I admit that something here is not adding up."
    scene ad1552 with dssa
    pause
    scene ad1553 with dssa
    na "Fine... We'll go there."
    na "But if this turns out to be a trap from the aliens..."
    na "I'll kill you myself."
    scene ad1554 with dssb
    na "Cyphi, the second one of them acts a little too alien, kill it."
    scene ad1555 with dssa
    cy "As good as dead."
    stop music fadeout 2
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_DarkAmbientDnD)
    scene ad1556 with dssb
    pause
    scene ad1557 with dssa
    pause
    scene ad1558 with dssb
    pause
    scene ad1559 with dssb
    pause
    scene ad1561 with dssb
    pause
    scene ad1562 with dssb
    pause
    scene ad1563 with dssb
    pause
    scene ad1564 with dssb
    stop music fadeout 3.5
    "Nadia and the Sentinel give each other a nod after staring at each other for an eternity."
    play music "music/TheIntangible/The Intangible - Interdimensional Amity.ogg"
    mya "I'm glad we're able to join forces against an unknown entity."
    scene ad1566 with dssb
    na "What is 'it'?"
    mya "The creature outside is... unknown to us."
    scene ad1565 with dssa
    d "I thought you faced them before."
    mya "Yes, but not the specimen that is roaming the city."
    scene ad1567 with dssb
    n "I found-... or more like heard one."
    scene ad1568 with dssa
    mya "Yes, contact with one of my patrols vanished after they followed a red human into a room."
    scene ad1569 with dssb
    d "Alright, what's the plan?"
    scene ad1570 with dssb
    pause
    scene ad1571 with dssb
    na "*Whisper* The fuck is that?"
    n "*Whisper* Looks kinda cute."
    scene ad1572 with dssa
    mya "An engineer."
    scene ad1573 with dssa
    mya "Guide him to the ship and let him establish a connection."
    scene ad1574 with dssb
    d "What do I need to know about the creature?"
    scene ad1575 with vpunch
    "Suddenly the door bursts open and something enters."
    scene ad1576 with dssb
    pause
    scene ad1577 with dssb
    na "You've got people on the outside? And you're using them to communicate?"
    scene ad1578 with dssb
    mya "Multiple units are scattered throughout the city but without the ship I'm not able to create a psy connection."
    mya "Our Rah'zy are the only ones fast enough to dodge the creature."
    scene ad1579 with dssa
    d "Let's do it."
    scene ad1580
    n "Yo, I'm coming with you."
    scene ad1581 with dssa
    d "No, you've got no camouflage."
    scene ad1582 with dssa
    na "And we'll need you here to power up the rest of the station."
    scene ad1580 with dssa
    n "Man... What if the creature gets you?"
    d "It won't."
    scene ad1585 with dssb
    mya "You'll need this."
    scene ad1584 with dssa
    na "An upgrade to your class!"
    na "I think you can climb walls with it!"
    scene ad1586 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad1587 with dssb
    "You place the tiny alien on your shoulder."
    scene ad1588 with dssb
    "Beeeep!"
    n "Don't be jealous."
    scene ad1589 with dssa
    "Beep Beeep!"
    scene ad1590 with dssb
    n "Yeah, now that you say it... It's really wrinkly."
    scene ad1591 with dssb
    na "Okay, [name]... Be careful and... and meet us here later."
    scene ad1592 with dssa
    n "I will head down to the core... Provided I get some fire support."
    scene ad1593 with dssa
    na "Sentinel. We're missing two of our squad mates."
    scene ad1594 with dssb
    mya "We'll help locate their position."
    stop music fadeout 2
    scene black with tleaf
    with Pause(.5)
    $ persistent.unlockedImageCh4x3 = True
    hide screen music_player_trigger
    scene City with dissolve
    $ renpy.pause(6.0, hard=True)
    with Pause(26)
    $ persistent.unlockedImageRS55 = True
    play music "music/tabletop/Azula Wave - Emptiness.ogg"
    show screen music_player_trigger
    scene ad1595 with dssb
    d "(It's been only a few days but the vegetation is out of control.)"
    scene ad1596 with dssb
    d "(I'm certain by now that the fog is artificial.)"
    scene ad1597 with dssa
    "The tiny alien squeaks."
    d "Be quiet. We're not alone."
    scene ad1598 with dssb
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad1599 with dssb
    pause
    scene ad1600 with dssa
    pause
    scene ad1601 with dssa
    d "(Let's test it out.)"
    scene ad1602 with dssa
    pause
    scene ad1603 with dssa
    pause
    scene ad1604 with dssa
    pause
    scene ad1605 with dssb
    pause
    scene ad1606 with dssa
    "*Squeeks*."
    scene ad1607 with dssa
    d "...It's harder than it looks."
    scene ad1608 with dssb
    pause
    scene ad1609 with dssa
    d "(It's too quiet.)"
    scene ad1610 with dssb
    pause
    scene ad1611 with dssa
    "You feel a slight breeze of air."
    scene ad1612 with vpunch
    "-And you jump behind the pillar."
    scene ad1613 with dssb
    pause
    scene ad1614 with dssa
    pause
    scene ad1615 with dssa
    d "(As the Sentinel said, it moves quietly... but it still moves air.)"
    scene ad1616 with dssa
    pause
    scene ad1617 with dssa
    "You put your index finger on its little mouth before it can squeek."
    scene ad1618 with dssa
    pause
    scene ad1619 with dssa
    d "Fuck this."
    scene ad1620  with vpunch
    pause
    scene ad1621  with dssa
    pause
    scene ad1622  with dssa
    pause
    scene ad1623  with dssb
    "*Sad Squeek."
    scene ad1624  with dssa
    d "Friends of yours?"
    scene ad1625  with dssa
    pause
    scene ad1626  with vpunch
    "An alien scream echoes through the building."
    d "(It came from a lower level.)"
    scene ad1627  with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad1629 with vpunch
    pause
    scene ad1630 with dssa
    pause
    scene ad1631 with dssa
    pause
    scene ad1632 with vpunch
    pause
    scene ad1633 with dssa
    with Pause(.3)
    scene ad1634 with dssa
    pause
    scene ad1635 with dssb
    pause
    scene ad1636 with vpunch
    so "*Gulp* [name]!"
    scene ad1637 with dssa
    d "...Hey."
    scene ad1638 with dssa
    d "I see you've been taking care of yourself."
    scene ad1637 with dssa
    so "What's that on your shoulder?"
    scene ad1639 with dssb
    d "Oh... A little pet alien."
    scene ad1640 with dssb
    d "Just a little side note... We're now allied with them."
    d "Soo uh... you might wanna stop killing them."
    scene ad1641 with dssa
    so "...That explains why some of them were reluctant to shoot back."
    scene ad1642 with dssa
    so "Oh no..."
    scene ad1643 with dssb
    pause
    scene ad1644 with dssa
    d "Don't worry. We'll say we found them like this."
    scene ad1645 with vpunch
    "*Squeeks!"
    scene ad1646 with dssa
    d "If you tell them otherwise, she'll cut your little head off."
    $ persistent.unlockedImageSonya7 = True
    scene ad1647 with dssa
    so "*Sad* I won't, I promise..."
    scene ad1648 with vpunch
    "You press Sonya against the wall."
    scene ad1649 with dssb
    d "*Whisper* There's something outside."
    scene ad1650 with dssa
    so "W-what?"
    scene ad1649 with dssa
    d "I don't know but it's massive and moves quietly."
    scene ad1650 with dssa
    so "Where are the others? Are they okay?"
    scene ad1649 with dssa
    d "Yes, except for Nancy. I haven't seen her."
    scene ad1651 with dssa
    so "Me neither."
    d "We'll have to get to the alien ship."
    scene ad1652 with dssa
    so "What alien ship? I didn't see one."
    scene ad1653 with dssa
    d "It's hidden."
    d "And... well, it would've been good if we could've asked someone to show us where..."
    scene ad1654 with dssa
    so "...Sorry."
    scene ad1655 with dssa
    menu:
        "No. I'm proud of you.":
            $ SonyaProud4x0 = True
            scene ad1656 with dssa
            pause
        "Shit happens.":
            $ SonyaShitHappens4x0 = True
            pass
    scene ad1657 with dssa
    d "Come, we'll crawl across the floor and out of the building."
    scene ad1658 with dssa
    pause
    scene black with tleaf
    with Pause(.5)
    scene ad1702 with tleaf
    n "There's still something in the main station."
    scene ad1703 with dssa
    na "I hope it didn't get Nancy..."
    scene ad1704 with dssb
    na "Sentinel."
    na "You've faced this enemy before."
    na "What is it?"
    scene ad1705 with dssa
    mya "A parasitic lifeform once used to make plants grow."
    scene ad1704 with dssa
    na "What? Really?"
    scene ad1705 with dssa
    mya "Yes, our ancestors synthesized a very potent fertilizer for our fields."
    mya "Which formed a consciousness that grew below the surface."
    scene ad1704 with dssb
    na "Something like a hive mind?"
    mya "Yes."
    scene ad1706 with dssa
    na "We've got to locate Nancy..."
    scene ad1707 with dssa
    n "First we need energy in order to activate the colony's defense systems."
    scene ad1708 with dssa
    mya "If your friend is smart, she'll be near the power room."
    scene ad1709 with dssb
    n "Let's move there... I'll have to go there anyways."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad1659 with dssb
    d "And you're sure that they're in there?"
    scene ad1660 with dssa
    so "I saw them running."
    so "They must be hiding."
    scene ad1659 with dssa
    d "Yeah."
    scene ad1661 with dssa
    d "We gotta get to them."
    scene ad1662 with dssa
    so "It's getting dark."
    scene ad1661 with dssa
    d "Yeah, we need the colony online. I hope Nami and the others are at the power room."
    d "How come you avoided the big monster?"
    scene ad1663 with dssa
    so "I didn't know it existed."
    scene ad1664 with vpunch
    "*Squeeks*"
    scene ad1665 with dssa
    pause
    scene ad1666 with dssb
    d "...There's one."
    scene ad1667 with dssb
    "The little alien signals further away."
    scene ad1668 with dssb
    pause
    scene ad1670 with dssb
    "Sonya, you and the little alien make your way across the street."
    scene ad1669 with dssb
    pause
    scene ad1671 with dssb
    pause
    scene ad1672 with dssb
    pause
    scene ad1673 with dssb
    "The tiny alien squeeks and something that looks like a smile forms on the aliens face."
    scene ad1674 with dssa
    "The alien makes some noises."
    d "Yeah, we don't speak fish."
    scene ad1675 with dssa
    "*Squeeks repeatedly*"
    scene ad1677 with dssa
    d "The ship's behind that building?"
    scene ad1676 with dssa
    so "You can understand him?"
    scene ad1677 with dssa
    d "No... But for some reason I think that's what he said."
    scene ad1678 with dssa
    d "We'll need a diversion."
    scene ad1680 with dssa
    so "I'll do it."
    scene ad1679 with dssa
    d "I'd rather have them do it."
    scene ad1680 with dssa
    so "I'll help them."
    scene ad1679 with dssa
    d "Fine."
    scene ad1682 with dssa
    d "You see that house, get into it and shoot that motherfucker, then run out the back."
    d "I'll then run over and get that little thing to its ship."
    scene ad1683 with dssa
    so "You three, please come with me."
    scene ad1684 with vpunch
    "The aliens salutes."
    scene ad1686 with dssb
    d "They understand us?"
    scene ad1685 with dssa
    so "Uhh- I guess?"
    scene ad1687 with dssb
    "Sonya and the three aliens make their way towards the building."
    scene ad1688 with dssb
    d "You fish boys are ready?"
    scene ad1690 with dssa
    d "That's what I thought..."
    scene ad1701 with dssb
    "Sonya scans the street from a high building."
    scene ad1691 with dssb
    pause
    scene ad1692 with dssb
    d "Go go go."
    scene ad1693 with dssa
    pause
    scene ad1694 with dssa
    pause
    scene ad1695 with dssa
    d "Go go."
    scene ad1696 with dssa
    "You feel a slight burst of wind."
    scene ad1697 with Dissolve(4)
    pause
    scene ad1698 with dssa
    pause
    scene ad1699 with dssa
    d "Oh."
    scene ad1700 with dssb
    $ persistent.unlockedImageRS56 = True
    pause
    stop music fadeout 2
    $ achievement.grant("TabletopA")
    $ achievement.sync()
    scene black with tleaf
    with Pause(1)
    jump AfterGame








label AfterGame:
    $ play_playlist(playlist_AfterDND)
    scene ad1305 with tleaf
    na "Oh, time's up for today."
    scene ad1302 with dssa
    n "Man! that was fun!"
    scene ad1303 with dssa
    n "Now I want to know what happens to [name]!"
    scene ad1305 with dssb
    na "Are you okay, Sonya?"
    scene ad1306 with dssa
    so "It's just a little warm..."
    scene ad1307 with dssa
    d "Take something off."
    so "No."
    scene ad1308 with dssa
    so "But I really liked it, too."
    so "It was-"
    scene ad1312 with dssa
    na "I know what you mean."
    na "It can give you some sense of freedom?"
    scene ad1309 with dssa
    so "...Yah."
    scene ad1320 with dssb
    nan "I'm glad you liked it! I hope we'll see you here again!"
    nan "And even [name] can stay!"
    scene ad1321 with dssa
    d "What do you mean 'even'?"
    scene ad1322 with dssa
    nan "Well, you see... Many guys that join us just do it because they want to bed me or Nadia..."
    scene ad1323 with dssa
    nan "Okay... Mostly Nadia..."
    scene ad1324 with vpunch
    nan "OKAY only Nadia!"
    scene ad1322 with dssa
    nan "They act all interested but pretty much only pay attention to our cleavage."
    scene ad1324 with vpunch
    nan "...Okay! Her cleavage!"
    scene ad1325 with dssb
    nan "But you didn't seem like that kind of guy. You actually did a good job playing."
    nan "And I didn't even catch you once looking at ou...- her cleavage."
    scene ad1313 with dssb
    na "Many act overly horny in game... They grope us in the game and stuff."
    scene ad1310 with dssb
    n "How can you grope someone... in there?"
    scene ad1313 with dssb
    na "The Devil's heart cards can be saved up and then you can use them on others."
    scene ad1326 with dssb
    nan "While it can be funny... It's often really weird if it doesn't fit the situation."
    scene ad1327 with dssa
    nan "You're in the middle of a boss fight and suddenly someone uses their card to put a finger into your butt."
    "Nami laughs."
    d "Can I use these cards to kill Nami?"
    scene ad1310 with vpunch
    n "HEY!"
    scene ad1314 with dssa
    na "Yeah, there are game modes where you'll also play against others and you'll have to trick them."
    $ persistent.unlockedImageRS45 = True
    if NadiaBananaHalf04 is True:
        scene ad1316 with dssa
    else:
        scene ad1315 with dssa
    d "Cool, I'd like to play one of those someday."
    scene ad1328 with dssa
    nan "Please don't... She gets so competitive."
    scene ad1329 with vpunch
    na "I'm not!"
    scene ad1330 with dssa
    nan "You should see her play Wormies of the void..."
    scene ad1331 with dssa
    n "Wormies of the void? I play that, too!"
    scene ad1317 with vpunch
    na "Awesome!"
    scene ad1318 with dssa
    na "You too?"
    scene ad1335 with dssb
    d "I have no idea what that is."
    scene ad1336 with dssa
    n "The five versus five game I showed you once."
    scene ad1337 with dssa
    n "You know? The one where-"
    scene ad1338 with dssa
    d "...The one where you sometimes scream insults into your headset and bang on your keyboard?"
    scene ad1339 with dssa
    n "...No."
    scene ad1319 with dssb
    na "Haha, I get that, Nami."
    na "Sometimes your teammates are so bad."
    scene ad1340 with vpunch
    n "Sooooo bad!"
    scene ad1327 with dssb
    nan "We need one more and we can compete!"
    scene ad1332 with dssb
    na "We have e-sports at our college."
    scene ad1333 with dssa
    n "REALLY?!"
    scene ad1332 with dssa
    na "Yes, and if you join we only need one more girl to compete."
    scene ad1341
    n "Count me in!"
    scene ad1341 with dssa
    d "What about sports?"
    scene ad1332 with dssb
    na "You will still have enough time, Nami."
    na "I also handle this, basketball, swimming and dancing."
    scene ad1320 with dssa
    nan "Sonya? How good are you at PC gaming?"
    scene ad1344 with dssa
    so "I don't own a PC."
    nan "Oh."
    scene ad1334 with dssa
    na "We might be able to arrange something."
    scene ad1343 with dssb
    n "Where are the restrooms? I really need to pee."
    scene ad1345 with dssb
    na "Come, I'll show you."
    scene ad1346 with dssa
    so "I- I also have to."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad1347 with dssb
    pause
    scene ad1348 with dssa
    pause
    scene ad1349 with dssb
    nan "Did you really like it?"
    scene ad1350 with dssa
    d "Mh? You mean the board game?"
    "She nods."
    scene ad1351 with dssa
    d "Yeah, it was fun."
    scene ad1352 with dssa
    nan "By the way... Would you and Nami like to help out at my family's farm?"
    scene ad1353 with dssa
    d "Where did this come from?"
    scene ad1354 with dssa
    nan "Well..."
    nan "We work a little and then we party and play games."
    scene ad1355 with dssa
    nan "If you, Nami and even Sonya would like to, we can do things like this there much more often."
    scene ad1356 with dssa
    d "I've gotta ask Nami first."
    scene ad1358 with dssb
    nan "Do you need her permission to go to a party?"
    scene ad1357 with dssa
    nan "I'm just kidding. But remember, it's not just work, we also party."
    scene ad1359 with dssb
    d "Yeah, that's the part that drives me away."
    scene ad1360 with dssa
    nan "The party?"
    scene ad1361 with dssa
    d "I'm not the most social person."
    scene ad1360 with dssa
    nan "I didn't get that from you."
    scene ad1361 with dssa
    d "Then you need to work on your people skills."
    scene ad1362 with dssa
    nan "That was rude."
    scene ad1363 with dssa
    d "I didn't mean to insult you. It was just an observation."
    scene ad1364 with dssa
    d "But yeah, I am not made for bigger parties."
    scene ad1365 with vpunch
    n "Did I hear parties?"
    scene ad1367 with dssb
    nan "I invited [name] to the barn."
    $ persistent.unlockedImageNancy3 = True
    nan "And Nami, you and Sonya are obviously invited too."
    scene ad1368 with dssa
    nan "It's just that... [name] doesn't like parties."
    scene ad1366 with dssb
    n "Oh come on, [name]! It sounds fun!"
    scene ad1369 with dssb
    na "It is."
    d "I'll get something to drink."
    scene black with tleaf
    with Pause(.5)
    scene ad1370 with dssb
    pause
    scene ad1371 with dssb
    d "(I wonder if I should get a tattoo someday...)"
    scene ad1372 with dssa
    pause
    scene ad1373 with dssa
    pause
    scene ad1374 with dssb
    d "Hmm."
    scene ad1375 with dssa
    na "Hey."
    scene ad1376 with dssb
    na "[name], I am also not into partying but it's really cool there." #check intangible mucke
    na "No overly rude, drunk people or other douches."
    scene ad1377 with dssa
    na "*Mumbles* Except for yourself."
    scene ad1378 with dssa
    d "I'll give it a try."
    na "Good."
    scene ad1379 with dssa
    d "But just because the Cheeto would be bothering me with no end in sight."
    scene ad1380 with dssa
    pause
    scene ad1381 with dssa
    na "How did you get out of the handcuffs?"
    $ persistent.unlockedImageNadia8 = True
    scene ad1382 with dssb
    if FoundByMarla4x0 is True:
        $ NadiaFavour4x5 = True
        d "Another class found me."
        scene ad1383 with dssa
        pause
        scene ad1384 with dssb
        na "Oh? Which class?"
        d "Those two black twins are in it."
        scene ad1385 with dssb
        na "Oh! Nora and Miriam, yeah."
        na "We would've gotten you in an hour anyways."
        scene ad1386 with dssa
        d "You said you'd get me tomorrow morning."
        scene ad1387 with dssa
        na "We just said that to scare you... We wouldn't leave you there for an entire night."
        d "Miss Marla was there too."
        scene ad1391 with vpunch
        na "What?!"
        scene ad1392 with dssa
        d "Calm down, I didn't tell her that it was you and Zara."
        scene ad1391 with dssa
        na "Then what did you tell her?"
        scene ad1395 with dssa
        d "I didn't say anything... and now I have to go to her office on Tuesday."
        scene ad1396 with dssa
        na "I'm so sorry! We really didn't want to cause this kind of trouble for you!"
        na "I-if you want you can tell them it was me... Just leave Zara out of it, okay?"
        scene ad1389 with dssa
        d "No, I won't tell them... But I'd like a favor from you in return."
        scene ad1396 with dssa
        na "Which one?"
        scene ad1395 with dssa
        d "We'll get to that... Just remember that you owe me."
        scene ad1397 with dssa
        na "Okay."
        scene ad1398 with dssb
        na "And- again... I'm really sorry."
        scene ad1399 with dssa
        d "No hard feelings."
        scene ad1398 with dssa
        na "You won't retaliate?"
        d "Maybe I'll give you a little push here and there... But I won't retaliate in a major way."
        "She squints her eyes."
        d "I'm serious. No vengeance."
        $ achievement.grant("NadiaFavor")
        $ achievement.sync()
    else:
        $ NaIntVer = True
        d "Bella found me."
        scene ad1383 with dssa
        pause
        scene ad1384 with dssb
        na "Huh? How did she-..."
        scene ad1385 with dssa
        na "Robin."
        scene ad1386 with dssa
        pause
        scene ad1385 with dssa
        na "...What did she do to you?"
        "You give her a look."
        scene ad1387 with dssb
        na "You can't tell me that she didn't at least use this situation a little."
        d "We just kissed..."
        scene ad1389 with dssa
        d "And agreed that we cannot be together."
        scene ad1388 with dssa
        na "*Sad voice* Why not?"
        scene ad1389 with dssa
        d "She and I are... We aren't a matching puzzle piece. We are the same piece."
        scene ad1390 with dssa
        "She watches you for a few seconds."
        scene ad1388 with dssa
        na "Did you have a traumatic experience?"
        scene ad1389 with dssa
        d "I don't know you well enough."
        scene ad1388 with dssa
        na "Sure, no problem."
    scene ad1400 with dssb
    na "Still, thank you for taking this seriously... This board game thingy."
    na "I really appreciate it."
    d "You seem to take it very serious?"
    scene ad1401 with dssb
    na "I just love it. I love fantasy and the ability to form- j-just everything I want in my head."
    na "It's... It's just nice having some people who stay in character and take it serious."
    scene ad1402 with dssa
    d "That sounds like you've had bad experiences in the past."
    "She lets out a laugh."
    scene ad1403 with dssa
    na "Yah..."
    scene ad1404 with dssb
    ci "Am I too late?"
    scene ad1405 with dssa
    $ persistent.unlockedImageCindy2 = True
    na "Hey Cindy. And yes... We just stopped a few minutes ago."
    scene ad1406 with dssb
    ci "Oh well, next time then."
    scene ad1407 with dssb
    ci "Hello [name]."
    scene ad1408 with dssa
    d "Miss- I forgot your name."
    scene ad1407 with dssa
    ci "Cindy Mueller."
    scene ad1408 with dssa
    d "Miss Mueller."
    scene ad1409 with dssb
    pause
    scene ad1402 with dssb
    d "You're playing board games with a professor?"
    scene ad1401 with dssa
    na "Why not? You're never too old for games."
    scene ad1410 with dssb
    u "Hey Nadia."
    na "Hi!"
    scene ad1402 with dssb
    d "Alright, I'll see you... sometime."
    scene ad1401 with dssa
    na "At the barn."
    scene ad1402 with dssa
    d "Right... maybe."
    stop music fadeout 2
    scene black with tleaf
    with Pause(.5)
    scene ad1411 with tleaf
    play music "music/Ambience/vesky - We Are Just Stars.ogg"
    n "That was fun!"
    d "Mhm."
    scene ad1412 with dssb
    n "We should do this again!"
    d "Mhm."
    scene ad1413 with vpunch
    n "Answer with more than MHM!"
    scene ad1414 with dssa
    d "It was fun and we should really do it again."
    scene ad1415 with dssa
    n "...I am proud of you."
    n "Soon you will be a gamer like me!"
    scene ad1416 with dssa
    d "I have no time for gaming... I need to focus on sports."
    scene ad1417 with dssb
    so "I found it very cool, too."
    scene ad1418 with dssa
    n "How was it in your country? Did you also do stuff like this with your friends?"
    scene ad1419 with dssa
    so "Oh uh... I had to go home right after school."
    scene ad1420 with dssa
    n "Well! That changes now!"
    n "You're part of our gang now!"
    $ persistent.unlockedImageSonya8 = True
    scene ad1421 with dssb
    d "We will be known as the disabled kids."
    stop music fadeout 2
    scene black with tleaf
    jump NamiHome04


label NamiHome04:
    $ play_playlist(playlist_GirlyCh4)
    scene ad1422 with dssb
    n "I'm tired..."
    d "Me too."
    if NSIHR is True:
        scene ad1423 with dssb
        n "Will you sleep in my room again?"
        scene ad1424 with dssa
        d "Again?"
        scene ad1423 with dssa
        n "Yeah? Why not?"
        scene ad1424 with dssa
        d "It's weird."
        scene ad1425 with dssa
        n "It wasn't weird... until you kneaded my tiddy."
        d "I didn't knead your tiddy! Stop saying that!"
        scene ad1426 with dssa
        n "Sure! Tell that Nojiko!"
        "You give her a confused look."
        scene ad1427 with vpunch
        n "I don't know what I'm saying!"
        scene ad1428 with dssa
        pause
        scene ad1429 with dssa
        n "So... yes or no?"
        menu:
            "Yes, let's sleep together.":
                $ NUE04 = True
                scene ad1430 with vpunch
                n "Good!"
                scene ad1431 with dssa
                n "But no tiddy-"
                scene ad1432 with vpunch
                d "Don't you say it!"
                n "*Giggle*."
                scene ad1433 with dssb
                d "We need ground rules."
                scene ad1434 with dssa
                n "For what?"
                scene ad1433 with dssa
                d "...Yeah, I wonder for what."
                d "Like you can't sleep topless."
                scene ad1435 with dssa
                n "*Giggles.*"
                scene ad1436 with dssa
                n "Get out of my room."
                n "I sleep like I want, comprende?"
                n "We'll lock the door."
                d "I just think that the negative aspects outweigh the positives."
                scene ad1437 with dssa
                n "You know what? I'm sick of it!"
                scene ad1438 with dssa
                n "Noji is constantly saying this bullshit!"
                n "And the only thing she is accomplishing with it is that you don't feel comfortable with me anymore!"
                scene ad1439 with dssa
                n "There was a time where I could just lay on top of you and none of us would think it was weird!"
                scene ad1440 with dssa
                d "You're right. She is pushing us in a direction that makes everything seem weird..."
                scene ad1441 with dssa
                n "Exactly!"
                n "I don't want us to grow apart just because she is delusional."
                scene ad1442 with dssa
                d "I don't want that either... You're weird.... sometimes... but she isn't helping."
                scene ad1443 with dssb
                d "You're my most trusted person."
                scene ad1444 with dssa
                pause
                scene ad1445 with dssa
                n "And you're my most trusted person."
                scene ad1447 with dssa
                n "From now on we don't give a shit about the things Noji says, okay?"
                d "Deal."
                scene ad1448 with vpunch #sfx klatsch
                pause
                scene ad1449 with vpunch
                n "ARGH!"
            "No, let's not do it again.":
                scene ad1438 with dssa
                n "Is it because of Noji?"
                d "May-"
                n "You know what? I'm sick of it!"
                n "Noji is constantly saying this bullshit!"
                n "And the only thing she is accomplishing with it is that you don't feel comfortable with me anymore!"
                scene ad1439 with dssa
                n "There was a time where I could just lay on top of you and none of us would think it was weird!"
                scene ad1440 with dssa
                d "You're right. She is pushing us in a direction that makes everything seem weird..."
                scene ad1441 with dssa
                n "Exactly!"
                n "I don't want us to grow apart just because she is delusional."
                scene ad1442 with dssa
                d "I don't want that either... You are weird.... sometimes... but she isn't helping."
                scene ad1443 with dssb
                d "You're my most trusted person."
                scene ad1444 with dssa
                pause
                scene ad1445 with dssa
                n "And you're my most trusted person."
                scene ad1444 with dssa
                d "I just don't want to make it weird."
                scene ad1446 with dssa
                n "*Sigh* Whatever."
    scene ad1450 with dssb
    pause
    d "Do you want to hang out?"
    scene ad1451 with dssa
    pause
    scene ad1452 with dssa
    n "You never ask me to hang out."
    d "I just did."
    scene ad1453 with dssa
    n "...What's going on?"
    scene ad1454 with dssa
    d "I'm just glad you're here."
    scene ad1455 with dssa
    n "Uhhhhh... Are you dying?"
    d "No. I'm just glad you aren't."
    scene ad1456 with dssa
    n "You're creeping me out."
    n "I'll go take a shower and then we can do something... Weirdo."
    scene black with tleaf
    with Pause(.5)
    scene ad1 with dssb
    pause
    scene ad2 with dssb
    pause
    scene ad3 with dssb
    d "Seriously?"
    scene ad4 with dssa
    n "What?"
    scene ad3 with dssa
    d "Please change it."
    scene ad5 with dssb
    pause
    scene ad6 with dssa
    n "Oh come on... Just because she always had this hairstyle, I'm now forbidden to have it?"
    n "An important part of letting go is to let all the connections go."
    scene ad7 with dssb
    n "This is just a hairstyle."
    scene ad8 with dssa
    d "What now?"
    scene ad9 with dssa
    n "We can go to the lake?"
    d "Hmm, why not."
    scene ad10 with dssa
    n "Wait wait! Let me take a picture!"
    d "For what?"
    n "I'm creating a photo book."
    d "Oh? You got the camera?"
    scene ad11 with dssb
    n "Yup! I finally had enough money! 18 months of saving up and not buying games!"
    scene ad12 with dssb
    n "Smile!"
    scene ad13 with dssa
    pause
    scene ad14 with dssb
    n "We'll work on that."
    scene ad15 with dssa
    d "Alright, let's go change."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad16 with dssb
    pause
    scene ad17 with dssa
    pause
    scene ad18 with dssa
    d "Dude..."
    scene ad19 with dssa
    n "What?"
    scene ad20 with vpunch
    n "Hahaha!"
    scene ad21 with dssb
    d "They are way too small!"
    d "When was the last time I went to the lake?"
    scene ad22 with dssb
    n "Several years ago."
    n "I was always there with Noji..."
    scene ad23 with dssa
    pause
    scene ad24 with dssa
    n "These shorts make him look big."
    d "I can't wear them..."
    scene ad25 with dssa
    n "Of course you can, it's just us."
    scene ad26 with dssa
    n "Nobody ever goes to that lake."
    scene ad26 with vpunch
    d "Then stop staring at it!"
    scene ad39 with vpunch
    n "I'm trying!"
    scene ad27 with dssa
    pause
    scene ad28 with dssa
    n "What do you think of my bikini?"
    scene ad29 with dssb
    pause
    scene ad30 with dssb
    pause
    scene ad31 with dssa
    d "Pretty revealing."
    d "I wonder what Noji-"
    scene ad32 with vpunch
    n "[name], I couldn't care less about Noji's opinion."
    n "If I want to wear a sexy bikini, I'll do it. I'm an adult."
    n "And besides that, it's just us there!"
    scene ad33 with dssa
    d "Exactly, that's why I am wondering why you would want to wear it."
    $ persistent.unlockedImageRS46 = True
    scene ad34 with dssa
    n "Do you think I am sexy?"
    scene ad35 with dssa
    d "*sigh* Oh my god..."
    d "We're not even at the lake and you're going full Cheeto again."
    scene ad36 with dssa
    n "...Should we pack some snacks?"
    d "Just some beers."
    scene ad37 with dssa
    n "How about some Meeresrauschen?"
    n "Oh and get the ball."
    d "I need a towel."
    scene ad38 with dssa
    n "No no, I gotcha. I've got a big one for us."
    stop music fadeout 2
    scene black with tleaf
    $ play_playlist(playlist_AmbientNamiLake)
    with Pause(.5)
    scene ad41 with tleaf
    d "A big one, huh?"
    n "It looked a lot bigger in my hands."
    n "It's not that bad."
    scene ad42 with dssb
    pause
    scene ad43 with dssb
    d "What?"
    scene ad44 with dssa
    n "Nothing."
    scene ad45 with dssb
    n "Here." #beer
    scene ad46 with dssb
    d "Cheers."
    n "Cheers."
    scene ad47 with dssb
    pause
    scene ad48 with dssa
    n "I've missed coming here with you."
    d "Yeah, me too."
    scene ad49 with dssb
    if BellaKiss3x5 is True:
        n "Any news about you and Bella?"
        scene ad50 with dssa
        d "I saw her before the board game."
        scene ad51 with dssa
        n "Oh?"
        n "That's why you were late?"
        scene ad52 with dssa
        d "No, something else."
        d "But... she and I kissed again."
        d "And we decided to end it before there was no turning back."
        scene ad53 with dssa
        n "Huh?! Why?"
        scene ad52 with dssa
        d "We aren't ready."
        d "The second we leave the honeymoon phase we would destroy each other."
        scene ad53 with dssa
        n "I'm sorry to hear that."
        d "No, you're not."
        scene ad54 with dssb
        n "Yes, I am."
        n "I saw that even against all logic, she was good for you."
        n "She was able to do something no one else could have done."
        n "And I'm thankful for that."
        n "Your well being is more precious to me than any sort of rivalry could ever be."
        scene ad55 with dssa
        d "Are you drunk?"
        scene ad56 with dssa
        n "But uhm... 'We aren't ready' implies that you've got some feelings for her?"
        menu:
            "Yeah, I think I do have feelings for her.":
                $ McBellaFeelings4x0 = True
                scene ad57 with dssa
                pause
                scene ad58 with dssa
                n "*Gulp* I see."
                scene ad59 with dssa
                n "*Cough* Well uh, but you made the right choice... You two would definitely destroy each other."
            "I'm not sure...":
                scene ad60 with dssa
                n "Yeah, you two don't really fit, I guess."
                d "We do. We really go with each other but yeah, it would be so toxic."
    else:
        n "So uh... Bella and you are over?"
        scene ad50 with dssa
        d "There was never really anything."
        scene ad51 with dssa
        n "Would you tell me what you were doing?"
        scene ad53 with dssa
        d "Not yet."
    d "Come, time to get in there."
    jump LakeBall04

label LakeBall04:
    scene ad61 with dssb
    pause
    scene ad62 with dssa
    n "Damn, the water is cold!"
    scene ad63 with dssa
    d "I like it."
    scene ad64 with vpunch
    n "MAN! I am looking forward to our competitions!"
    n "It's time for me to leave an ever lasting impression!"
    scene ad65 with dssa
    pause
    scene ad66 with dssb
    pause
    if McBellaFeelings4x0 is True:
        d "(I'd like to bring Bella here someday.)"
    elif vicdate is True:
        d "(I bet Victoria would like it here... I should bring her here someday.)"
    elif miladate or miladateF is True:
        d "(I should invite Mila to this place... I bet she'd like that.)"
    else:
        d "(I'm here with exactly who I'm supposed to be.)"
    scene ad67 with dssa
    pause
    scene ad68 with dssa
    pause
    scene ad69 with dssa
    pause
    scene ad70 with dssb
    n "[name]! Let's go back a little, it's too deep here."
    scene ad71 with dssb
    n "Oh my God... here she comes..."
    scene ad72 with dssa
    n "The number one player-"
    scene ad73 with dssa
    n "Known under her alias, Phoenix!"
    scene ad74 with dssa
    n "Due to her fiery nature and her incredible dribbling skills-"
    scene ad75 with vpunch
    pause
    scene ad76 with dssa
    pause
    scene ad77 with dssa
    n "That was a dick move..."
    d "Phoenix Nami has fallen."
    scene ad78 with vpunch
    n "*Narrator voice* What is this?!"
    scene ad79 with dssa
    n "The phoenix rises from her ashes and tackles the enemy!"
    scene ad80 with vpunch
    pause
    scene ad81 with dssa
    pause
    scene ad82 with dssa
    pause
    scene ad83 with dssb
    "You sit down on the cold and stony ground."
    scene ad85 with dssr
    n "Wow! You definitely got stronger!"
    d "I never realized what a lightweight you are."
    scene ad86 with dssa
    d "The ball is floating away."
    n "We'll get it later."
    scene ad87 with dssa
    n "Man, for the first time I actually feel awkward sitting on top of you."
    n "Your-"
    scene ad88 with vpunch
    d "Goddamnit, Nami!"
    scene ad89 with dssb
    d "Thanks for ruining this moment."
    n "Shouldn't you be used to it by now?"
    d "I'll never get used to it."
    scene ad90 with dssb
    n "You will."
    n "*whisper* At some point, you will just submit to me."
    scene ad92 with dssb
    "You raise a single brow."
    d "I doubt that."
    d "Okay. You need to get down."
    scene ad93 with dssa
    n "If I didn't know any better... I would say I felt something funny."
    d "Shut up now and let's play some ball."
    scene ad94 with dssb
    n "Wow wow wow- what was that?"
    scene ad95 with dssb
    d "Nami... I am not dead down there, you know?"
    scene ad96 with dssa
    n "You said you wouldn't be able to get a... you know?"
    scene ad97 with dssa
    d "Nami, I said no random girl could ever do it... and it wasn't a boner!"
    d "You are my most trusted person in the world- *sigh*."
    d "Don't sit on me again."
    scene ad98 with dssa
    n "But I felt something!"
    n "And it never happened before? What changed?"
    scene ad99 with dssa
    d "Nothing changed! It's not- God- fuck off!"
    pause
    scene ad100 with vpunch
    d "Stop smiling!"
    scene ad101 with dssb
    n "How can you expect me not to smile!"
    d "Nothing happened!"
    scene ad102 with vpunch
    n "Phoenix Nami strikes again!"
    scene ad103 with dssa
    n "Or more like... rises again... am I right?"
    d "I'll ask Noji to throw you out of the house."
    scene ad104 with dssa
    n "*Content* I see, I see..."
    scene ad105 with dssa
    d "What?"
    scene ad106 with dssa
    n "The only reason why you'd want me out of the house, is so that you and I-"
    scene ad107 with dssa
    d "Don't say it!"
    n "- can bang in peace."
    scene ad108 with vpunch
    n "Au!"
    scene ad109 with dssb
    pause
    scene ad110 with dssa
    d "Get in position."
    scene ad111 with dssb
    n "*playfully* Which one do you prefer? Heh? Heh?"
    scene ad112 with vpunch
    d "Oh my god! I will drown you!"
    scene ad113 with dssb
    n "*Laughs* Okay! I'll stop! I'll stop!"
    scene ad114 with dssb
    n "You and I should train in our free time."
    d "Well, we pretty much just throw the ball back and forth."
    scene ad115 with dssa
    n "Don't forget that we also have other sport tournaments."
    n "For example swimming."
    n "And we have a lake right here dude."
    scene ad116 with dssa
    d "Yeah... Not a bad idea."
    scene ad117 with dssa
    n "Phoenix Nami and Raven [name]!"
    scene ad118 with vpunch
    pause
    scene ad119 with dssb
    d "I mainly want to focus on basketball."
    d "But the athletic abilities that some other sport could provide me shouldn't be underestimated."
    scene ad120 with dssa
    n "Swimming is really good for your endurance."
    n "Or sex."
    scene ad121 with dssa
    d "I don't think you build up actual athletic endurance during sex."
    scene ad122 with dssa
    n "I'm pretty sure you do."
    n "I guess there is only one way to find out..."
    scene ad123 with vpunch
    d "YOU SAID YOU WOULD STOP!"
    scene ad124 with vpunch
    n "I DIDN'T EVEN SAY YOU AND ME!"
    scene ad125 with dssa
    n "YOU THOUGHT THAT! I'M INNOCENT!"
    scene ad126 with dssa
    d "You damn Cheeto!"
    n "Come, let's get out of the water and drink!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad127 with dssb
    pause
    scene ad129 with dssa
    n "Do you want a beer?"
    d "Yeah."
    scene ad130 with dssa
    pause
    scene ad131 with dssb
    n "I liked that you took leadership in the last game."
    d "Mh?"
    scene ad132 with dssa
    n "At college."
    scene ad133 with dssa
    d "Oh... Well, you saw my team... Somebody had to take the wheel."
    scene ad134 with dssa
    n "It reminds me of past days."
    n "You always took leadership."
    scene ad135 with dssb
    n "I'm sure you would've made captain in high school."
    scene ad136 with dssb
    d "It doesn't matter anymore."
    scene ad137 with dssa
    n "I'm glad you didn't lose that part of you... Even though you can be super cocky."
    scene ad138 with dssa
    pause
    scene ad139 with dssr
    n "But... please do me a favour."
    n "Take it easier..."
    n "I know what you're doing."
    scene ad140 with dssa
    d "Winning? Succeeding?"
    scene ad139 with dssa
    n "When we sat outside before your date with Bella... You said you wanted to be normal again."
    scene ad140 with dssa
    d "And... that is what I'm trying to do."
    scene ad141 with dssa
    n "Exactly... So, please try to take it easy or you'll burnout."
    d "Burnout from what? Social contact?"
    scene ad142 with dssb
    n "Yes."
    n "You'll come crashing down at some point."
    menu:
        "Hold Nami in your arms.":
            if bellameet is False:
                $ NamiTni4x0 = True
            $ NamiCuddle04 = True
            scene ad143 with dssa
            d "You look like you're freezing."
            scene ad144 with dssa
            n "The lake was super cold."
            scene ad145 with dssa
            pause
            scene ad146 with dssa
            d "Better?"
            scene ad147 with dssa
            n "Y-yeah."
            scene ad148 with dssa
            d "That was the first time I've heard you stutter from a touch."
            scene ad149 with dssa
            n "Normally, I'm the one who forces myself on you... That came out wrong."
            n "I was just caught a little off guard."
            scene ad150 with dssa
            n "But it is nice."
            scene ad151 with dssa
            pause
            scene ad152 with dssb
            d "I'm glad you and I did this today."
            d "I missed this."
            n "Me too."
            scene ad153 with dssa
            n "We should go here more often."
            scene ad154 with dssb
            pause
            scene ad155 with dssb
            pause
        "Keep a reasonable distance.":
            scene ad157 with dssb
            pause
            scene ad156 with dssb
            pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad158 with dssb
    pause
    scene ad159 with dssa
    d "Noji's calling."
    scene ad160 with dssa
    d "Yes?"
    m "Hey [name]."
    m "Is Nami with you?"
    scene ad161 with dssa
    d "Yes, we're at the lake."
    scene ad162 with dssa
    n "Put it on speaker."
    scene ad163 with dssa
    m "How nice!"
    m "I'm just calling to let you both know, we will be having dinner at Nick's this evening"
    d "This evening?"
    m "Yes, I know... it's a little spontaneous."
    d "Umm, sure... We'll be there."
    m "Great, I'll see you two at home in two hours."
    scene ad165 with dssb
    n "So... we have to cancel on Vic and Mila?"
    scene ad166 with dssa
    d "No, I think we can go after the dinner."
    scene ad167 with dssa
    n "We should sleep at their place then."
    d "If we have to."
    scene ad168 with dssb
    d "Are we going to drink them all?"
    n "Ye."
    d "Let's not."
    scene ad169 with dssa
    n "But- what if that Nick guy is horrible and his kids are even worse! We need to get through the night!"
    n "Safety first! So drink!"
    scene ad170 with dssa
    n "Wanna see something funny?"
    d "No."
    scene ad171 with dssa
    pause
    scene ad172 with dssa
    n "Magic!"
    if BellaKiss03x is True:
        scene ad173 with dssa
        n "Wait... I just realized something. Bella was the first girl you kissed since Summer, right?"
        scene ad174 with dssa
        d "Yeah."
        scene ad175 with dssa
        n "Damn, if only Summer knew who replaced her."
        scene ad176 with dssa
        d "Nobody can ever replace her."
        d "And... if I should ever open up to someone again, I'm not looking for a replacement, I'm looking for something new and unique."
        scene ad177 with dssa
        n "I didn't mean it like that... I meant-"
        scene ad178 with dssa
        d "I know what you meant."
        d "I think Summer would have liked Bella."
        scene ad179 with dssa
        n "I think Summer would have beaten Bella up."
        scene ad180 with dssb
        d "Summer only ever beat boys up."
        n "Still, I wonder how things would be if she was still here."
    else:
        scene ad173 with dssa
        n "Man..."
        n "I wonder how things would be if Summer was still here."
    scene ad181 with dssb
    d "I assume you and I wouldn't be close."
    n "I would probably have ran away and been so depressed that I would sell body..."
    d "Summer would've looked for you."
    n "As if."
    scene ad182 with dssb
    d "Stop demonizing her."
    if BellaKiss3x5 is True:
        $ NamiLove4x0 = True
        d "Is this the right moment to ask you about-"
        n "No."
        d "Well, I don't give a fuck. Let's make it the right moment."
        n "Dude, I don-"
        scene ad184 with vpunch
        d "Are you in love with me?"
        n "What?"
        d "Simple question."
        scene ad185 with dssa
        n "Not a simple answer."
        scene ad186 with vpunch
        d "Nami? What the hell?"
        n "Do you really want to ruin this here?"
        scene ad187 with dssb
        d "Nami, I just want to know if something is... going on."
        scene ad188 with dssa
        n "Dude..."
        d "Well, you dodging the question pretty much answers it."
        scene ad189 with vpunch
        n "Nothing- *sigh* Yo-You suck! Fuck you!"
        n "*Sigh*"
        scene ad190 with dssa
        pause
        scene ad191 with dssa
    else:
        pass
        scene ad191 with dssb
    d "Alright... Let's pack up. The sun is setting."
    n "I'm actually a little drunk."
    d "I'm not going to carry you."
    n "I don't need ya! I'm a big girl!"
    scene ad193 with vpunch
    d "Seems like nobody told your boobs."
    scene ad194 with vpunch
    n "WOW! DUDE!"
    d "That was a brutal one, huh?"
    n "Dude, I- Oh my god!"
    d "You know I'm just joking."
    scene ad195 with dssb
    d "Come. You can sulk on the way back."
    scene ad196 with dssa
    n "Oh... By the way, your wound is fading out."
    scene ad197 with dssa
    d "I thought you were about to punch me."
    n "Someday... Someday..."
    scene ad198 with dssa
    n "I'll make you a new one soon."
    d "Let's not talk on the way back. I want to enjoy the tranquility of nature a little longer."
    stop music fadeout 2
    scene black with tleaf
    play music "music/TheIntangible/The Intangible - Encyclopedia of Frozen Dreams.ogg"
    with Pause(.5)
    scene ad200 with tleaf
    pause
    scene ad201 with dssa
    n "[name]!"
    d "What?"
    scene ad202 with dssa
    n "What the hell should I even wear?"
    n "Noji didn't say if we should go classy or-"
    scene ad203 with dssa
    d "As if it matters what we wear."
    d "Just use what you're wearing."
    scene ad204 with dssb
    n "What do you think of this top?"
    $ persistent.unlockedImageNamiCh42 = True
    d "You ask about the top but you show me your butt."
    d "...The top looks good."
    scene ad205 with dssa
    n "Thaaaank you!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad206 with dssb
    pause
    d "(I have to see this Emilio. Bella said he could get information... Maybe he can give me some peace of mind.)"
    scene ad207 with dssb
    pause
    if BellaKiss3x5 is True:
        scene ad208 with dssb
    elif miladate is True:
        $ MilaDate = True
        scene ad209 with dssb
    elif vicdate is True:
        scene ad210 with dssb
    pause
    scene ad211 with dssb
    pause
    scene ad212 with dssa
    n "Yo, what are you doing in the dark?"
    scene ad213 with dssb
    pause
    menu:
        "You look beautiful.":
            $ NamiBeautiful4x0 = True
            scene ad214 with dssa
            pause
            scene ad215 with dssa
            n "...What do you want?"
            d "Nothing. I just wanted you to know that."
            scene ad216 with dssa
            n "Uh hu."
        "Don't say it.":
            pass
    scene ad217 with dssb
    m "Ah! There you two are."
    m "You two look great."
    scene ad218 with dssa
    n "I love your dress!"
    scene ad219 with dssa
    m "Thanks honey."
    scene ad220 with dssb
    d "I hope they have enough food."
    scene ad221 with dssa
    n "I'm starving, too."
    d "Oh god... Imagine if they're vegans."
    scene ad222 with vpunch
    n "No! I need some meat!"
    scene ad223 with dssa
    m "Okay... Nami, [name]."
    scene ad224 with dssb
    m "This is important to me... Please... behave."
    scene ad225 with vpunch
    n "Do you know who you're talking to?! [name] and I mark the pinnacle of-"
    scene ad226 with dssa
    n "Oh. I get it."
    scene ad227 with dssa
    m "Okay."
    m "Where are my keys?"
    scene ad228 with dssa
    d "In your hand."
    m "Oh."
    scene ad229 with dssa
    n "Shall we?"
    m "Yes."
    stop music fadeout 2
    scene black with tleaf
    with Pause(.5)
    jump NicksHouse4

label NicksHouse4:
    $ play_playlist(playlist_NamiSad)
    scene ad230 with tleaf
    n "I think it was called Spaghetti Bondage."
    scene ad231 with dssa
    m "Nami... Please don't talk about anything like that when we're there."
    scene ad232 with dssa
    d "Cheeto... Just shut up."
    n "You two are just afraid of the truth."
    scene ad233 with dssa
    n "Koenigsberg?"
    n "Noji... is Nick loaded?"
    scene ad234 with dssa
    m "Nami. He might have a little more money."
    scene ad235 with dssb
    n "Na, a little more money- pfff."
    n "The people that live in this part of the city don't just have a little more money."
    scene ad236 with vpunch
    n "[name]! Noji has a millionaire boyfriend!"
    scene ad237 with dssa
    d "(It's not that far away from Bella's.)"
    scene ad239 with dssa
    n "Man, I can't wait to see their house!"
    scene ad240 with dssb
    n "Noji, be honest."
    n "Is he actually a good guy or are you dating him because of the money?"
    scene ad241 with dssa
    m "Nami! I'm seriously offended that you would even ask me that!"
    n "Sorry."
    scene ad242 with dssa
    m "Here we are."
    scene ad243 with dssb
    pause
    scene ad244 with dssa
    d "Don't worry, we'll behave."
    scene ad245 with dssa
    "She gives you a nervous smile."
    stop music fadeout 2
    scene black with Dissolve(2)
    $ play_playlist(playlist_GirlyCh4)
    with Pause(.5)
    "Nojiko rings and the door automatically opens."
    scene ad246 with dssb
    pause
    scene ad247 with vpunch
    n "DUDE LOOK!"
    d "Believe it or not Nami... But I see the big ass bike in the middle of the room."
    scene ad248 with dssb
    pause
    scene ad249 with dssa
    n "Yeah! You know it!"
    $ persistent.unlockedImageRS47 = True
    n "How badass do I look?"
    d "Like a three and a half."
    scene ad250 with dssa
    n "I'll take it!"
    scene ad251 with vpunch
    m "Nami! Are you insane?! Get off the bike!"
    scene ad252 with dssb
    ni "Hey! Welcome!"
    scene ad253 with dssb
    ni "I'm glad you could make it."
    scene ad254 with dssb
    ni "Hi! You must be Nami."
    scene ad255 with dssa
    n "Yep! Nice to meet you!"
    scene ad256 with dssb
    ni "And the infamous [name]. Nojiko told me a lot about you."
    ni "It's nice to meet you."
    scene ad257 with dssb
    d "Nice to meet you too."
    scene ad258 with dssa
    ni "Please follow me to the dining room."
    scene ad259 with dssb
    n "Dude... Look at this fucking house."
    n "Imagine if we lived here."
    scene ad260 with vpunch
    u "No fucking way."
    scene ad261 with dssb
    pause
    n "Oh Hi!"
    scene ad262 with dssa
    za "Hi Nami."
    scene ad263 with dssa
    za "I had no idea it was you two."
    za "To be honest, I expected Asians."
    scene ad264 with dssb
    d "Surprise."
    scene ad265 with dssb
    za "...But certainly not you."
    scene ad266 with dssa
    "You all stare awkwardly at each other."
    scene ad267 with dssa
    za "Why are you on the bike?"
    scene ad268 with dssb
    n "Uhhh- [name] told me to do it."
    scene ad269 with vpunch
    d "Shut up Cheeto."
    scene ad270 with dssa
    za "Follow me to the dining room."
    stop music fadeout 3
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Diner)
    scene ad271 with dssb
    pause
    scene ad272 with dssa
    za "Dad, do I need to get something from the cellar?"
    ni "I think we've got everything."
    scene ad273 with dssa
    ni "Unless [name] or Nami want to drink something special?"
    scene ad274 with dssa
    n "Umm-"
    d "No, we're good."
    scene ad275 with dssa
    u "So... those are [name] and Nami?"
    scene ad276 with dssb
    pause
    scene ad277 with dssa
    pause
    play music "music/Suspense/Scott Buckley - Nightfall.ogg"
    scene ad278 with dssb
    pause
    d "(Wait a second... That's Mario's girlfriend! Our target.)"
    scene ad279 with dssa
    u "Zara, look."
    u "He's just staring at me."
    za "Oh, [name]. I feel hurt that you didn't completely lose it for me."
    scene ad280 with dssa
    d "No, that's not it. I just thought, I had seen you before."
    scene ad281 with dssa
    u "Unlikely."
    u "I don't think we share the same social circles."
    scene ad282 with dssa
    za "Vanessa, no need to go that far."
    scene ad283 with dssb
    va "It wasn't meant as an insult."
    va "After all... He might soon be a part of us."
    scene ad284 with dssb
    za "Don't mind her. Sometimes she can be a little pretentious."
    scene ad285 with dssa
    n "A little? She's wearing a fucking tiara..."
    scene ad286 with dssa
    d "It's all good."
    d "And she's right, she and I don't share the same social circle."
    scene ad287 with dssa
    n "Now I feel seriously underdressed."
    scene ad288 with dssa
    n "Even you are better dressed than me!"
    stop music fadeout 2
    d "I'm always better dressed than you."
    $ play_playlist(playlist_Diner)
    scene ad289 with dssb
    pause
    scene ad290 with dssb
    ni "I see you all have met."
    scene ad291 with dssa
    za "Nami, [name] and I are in the same year at college."
    za "So, we already knew each other before this."
    scene ad292 with dssa
    ni "That's great!"
    ni "[name], Nami do you want a drink? A cocktail, a rum, a gin and tonic?"
    scene ad293 with dssa
    d "I'll take a rum."
    n "Me too!"
    stop music fadeout 3
    ni "Coming right up."
    scene ad294 with dssa
    d "Gimme a second."
    play music "music/TheIntangible/The Intangible - Encyclopedia of Frozen Dreams.ogg"
    scene ad295 with dssb
    pause
    scene ad296 with dssb
    d "(Come on... Pick up.)"
    scene black with tleaf
    if BYF is False:
        scene ad1739 with tleaf
        pause
        scene ad1742 with dssa
    else:
        scene ad1740 with tleaf
        pause
        scene ad1741 with dssa
    b "Yes?"
    d "Bella."
    b "That's my name."
    d "Nojiko is dating Mario's girlfriend's father."
    scene ad1744 with dssa
    b "Seriously?"
    scene ad1745 with dssb
    d "Yes."
    d "We're at their place right now."
    scene ad1746 with dssa
    b "Wow! Finally, you can do something too!"
    scene ad297 with dssb
    d "*sigh* This shit has gotten much more complicated..."
    d "And thanks for telling me that Zara is her sister."
    b "I thought you knew."
    scene ad298a with vpunch
    za "Hi, this is Zara, who am I speaking to?"
    b "Bella."
    za "Hi Bella."
    scene ad299a with dssb
    "You swirl Zara around."
    scene ad300a with dssb
    pause
    scene ad474 with dssb
    "Zara stares at you with an anxious look."
    scene ad475 with dssa
    za "...I didn't know you and [name] had something going on."
    if BellaKiss03x is True:
        za "Except for the romantic kiss under the moonlight."
    scene ad1747 with dssb
    b "Whatever, put [name] back on."
    scene ad476 with dssa
    za "No, dinner is ready."
    b "Just put him bac-"
    scene ad477 with dssa
    "Zara hangs up."
    scene ad478 with dssb
    m "What are they doing there?"
    scene ad479 with dssa
    va "I think it's some sort of mating ritual."
    scene ad480 with dssb
    pause
    d "My phone."
    scene ad481 with vpunch
    "You pull her towards you."
    scene ad482 with dssb
    za "...For a second I thought you'd let me fall."
    d "It took everything I had not to do it."
    scene ad483 with dssb
    za "Bella..."
    za "She is a good friend of Nadia's."
    stop music fadeout 2
    scene ad484 with dssb
    "You say nothing."
    $ play_playlist(playlist_Diner)
    za "Lighten up."
    scene ad485 with dssb
    d "You said dinner's ready?"
    scene ad486 with dssb
    za "It's not."
    za "But we're having drinks."
    scene ad487 with dssa
    d "I'm starving."
    scene ad488 with dssa
    za "You're just here to eat, huh?"
    d "Yes... And to support Noji."
    scene ad489 with dssb
    ni "And?"
    scene ad490 with dssa
    n "Tastes- *cough*- strong."
    ni "Let me get you something else."
    ni "Some mild wine?"
    n "Yes please."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad491 with dssb
    ni "Zara told me you two are going for the first team in basketball?"
    scene ad496 with dssb
    n "[name] is."
    n "I'm good at basketball but I don't think I'm good enough for the first team."
    scene ad497 with dssa
    n "I still have to find my passion."
    scene ad498 with dssa
    d "(Shit, the coaches wanted to meet us at eight.)"
    scene ad492 with dssb
    m "Everything alright, [name]?"
    d "Umm, actually I will have to leave for an hour at eight."
    scene ad493 with dssb
    m "Why?"
    d "The coaches wanted to see us."
    scene ad494 with dssa
    n "Me too?"
    scene ad495 with dssa
    d "No no. Just a few guys."
    scene ad499 with dssb
    za "Why?"
    scene ad500 with dssa
    d "I am not at liberty to say."
    ni "I see."
    scene ad502 with dssa
    ni "Then let me take this from you, and you can just take a car out of the garage."
    d "I don't know how to drive."
    ni "Oh."
    scene ad501 with dssb
    za "I'll drive him."
    scene ad503 with dssb
    ni "Theeeen- I'll take this from you."
    scene ad504 with dssa
    d "Do I get my rum back?"
    ni "Oh! Of course, haha."
    scene ad509 with dssb
    n "*whisper* What's it about?"
    d "*whisper* Extra training outside the school hours."
    scene ad505 with dssa
    za "So... Nojiko."
    za "You're a doctor, right?"
    m "Yes."
    scene ad506 with dssa
    za "That's a very prestigious job."
    ni "She is the best doctor I have ever seen."
    scene ad507 with dssb
    ni "The other doc blatantly said they might have to amputate my leg."
    ni "And I'm so glad that she came in and told them to get lost."
    scene ad510 with dssb
    n "What happened? I- mean the accident."
    scene ad511 with dssa
    ni "Somebody cut me off, and I flew across the intersection."
    scene ad510 with dssa
    n "Damn, I am sorry to hear that."
    scene ad512 with dssa
    d "It wasn't some elderly lady named Marla, huh?"
    scene ad513 with dssa
    "Zara and Nami let out a laugh."
    ni "No, it was some young guy on his phone."
    scene ad508 with dssb
    ni "But it was a small price to pay for what came next."
    scene ad506 with dssb
    za "And that's why we forbid you from riding a motorcycle ever again."
    m "And I hope you're taking your meds."
    scene ad514 with dssb
    va "We made sure of it."
    scene ad515 with dssa
    za "Ah! [name]-"
    scene ad516 with dssa
    $ persistent.unlockedImageRS49 = True
    va "Little sister, how is your relationship with [name]?"
    za "What?"
    va "You look a little eager to prove your worth."
    scene ad521 with dssb
    za "I'm not?"
    scene ad517 with dssb
    va "Oh! I know the look."
    va "If I recall correctly... You told me about someone named [name] that played you like a fool and then ripped your top open."
    va "Don't tell me it was him."
    za "I don't need to prove myself to anyone."
    scene ad518 with dssa
    va "A competitive person like you can't stand being underestimated."
    va "I can see the desire burning."
    scene ad519 with dssa
    za "Shut up- I."
    ni "Enough."
    scene ad520 with dssa
    "Zara gives you an angry look."
    scene ad522 with dssb
    "-And gets up."
    scene ad523 with dssb
    pause
    scene ad524 with dssa
    d "Don't tell me you hold a grudge?"
    scene ad526 with dssb
    za "Why would I? It's not like you matter."
    scene ad525 with dssa
    d "You really do hold a grudge."
    d "You handcuffed me into the locker room. We are even."
    scene ad527 with vpunch
    za "We are not."
    za "We are even when I fucking destroy you."
    scene ad528 with dssa
    d "Listen to me Zara."
    d "What I did to you was certainly not the nicest thing in the world."
    scene ad529 with dssa
    d "And I'm sorry for accidentally ripping your shirt."
    d "But you used the most important person in my life as bait."
    scene ad530 with dssa
    d "If it wasn't for the fact that I'm trying to be a better person, and your father was dating Noji, I would've retaliated in a way that would make your little stunt look like it was nothing."
    d "And I'll tell you the same thing I told Nadia."
    scene ad531 with dssa
    d "Never! Never ever use Nami or any person I love against me ever again!"
    d "Or I'll make sure you regret it."
    scene ad532 with dssa
    za "Maybe we did overdo it a little."
    d "You think so?"
    scene ad533 with dssa
    za "Yeah... okay... We both did something... uncool."
    scene ad534 with dssb
    za "I'm sorry, but we didn't tell Robin to use Nami as bait... We we're harsh... but well..."
    scene ad535 with dssa
    d "And I'm sorry for ripping your shirt and embarrassing you."
    scene ad536 with dssa
    pause
    scene ad537 with dssa
    d "You've got a tennis court in your garden?"
    scene ad538 with dssa
    za "How did you know?"
    d "The floodlights."
    scene ad539 with dssb
    d "One month from now... One on One, Best out of three."
    scene ad540 with dssa
    d "Winner keeps the right to stand up tall."
    scene ad541 with dssa
    za "Let's add a 'Loser' has to announce publicly that the other person is superior in everything."
    scene ad542 with vpunch
    za "Deal!"
    scene ad543 with dssa
    pause
    scene ad544 with dssa
    n "Dude, you never played Tennis before! She'll definitely win."
    scene ad545 with dssb
    d "She most likely will."
    d "But it is a small price to pay for a few relationship points."
    d "Her holding a grudge on me could have a negative influence on Noji's and Nick's relationship. And Noji's happiness is much more important to me."
    scene ad546 with dssa
    d "To her, I now symbolize something exciting. A challenge, something she's looking forward to."
    scene ad547 with dssr
    n "...This is what I was talking about at the lake."
    $ persistent.unlockedImageNamiCh43 = True
    n "Your plate is already so full! Stop adding more!"
    scene ad548 with dssa
    d "I'm okay Nami."
    scene ad547 with dssa
    n "For a few days, yes! But you can't force yourself to be your old you again!"
    scene ad548 with dssa
    d "What else am I supposed to do?! Walk around like a fucking corpse and hope it gets better?!"
    d "Wait till after the 500th session with Amber, and I might be back on track!"
    scene ad549 with dssa
    d "I need- *sigh* I need distraction!"
    scene ad550 with dssa
    n "You're just fighting symptoms!"
    "You make an angry fist... and sigh loudly."
    scene ad551 with dssb
    d "*Calm voice* Then tell me what else am I supposed to do...?"
    scene ad552 with dssb
    n "M-maybe just slower, you know? Don't make anymore plans and, I know this sounds contradicting... but don't make anymore acquaintances."
    n "At least for a while..."
    n "No wait... An acquaintance is fine... but no more meetings and plans."
    scene ad553 with dssb
    n "Please."
    d "I'll see what I can do."
    n "This Zara tennis thingy is the last one."
    scene ad554 with dssb
    n "...Imagine if you'd actually beat her."
    scene ad555 with dssa
    d "I'm not going down without a fight."
    d "Little does she know, I'm just as competitive but often just don't care enough."
    scene ad556 with dssa
    n "As Noji said, let's go to that tennis club and become badasses!"
    d "And there we have another plan added to my plate..."
    scene ad557 with dssa
    n "...Shit."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad558 with dssb
    n "This looks amazing!"
    n "You cooked this all by yourself?"
    scene ad559 with dssb
    ni "Thanks! I did indeed."
    scene ad564 with dssb
    za "We helped!"
    scene ad565 with dssa
    ni "You two only stood in my way, bombarding me with questions."
    scene ad571 with dssb
    ni "Nami, may I ask you what your plans are after college?"
    scene ad570 with dssa
    n "Umm- I actually haven't really thought about it."
    n "Uh- yeah... No idea."
    scene ad571 with dssa
    ni "I see. Well, you've got a lifetime to figure it out."
    scene ad572 with dssb
    ni "And you [name]?"
    scene ad573 with dssa
    d "Same here. I try to focus on what is right in front of me."
    scene ad560 with dssb
    ni "Which can work out, but here and there you should raise your head and check you're still on the right course."
    scene ad561 with dssb
    m "What about you two?"
    scene ad574 with dssb
    va "I will never need to work. I'll see where life takes me."
    scene ad575 with dssb
    m "I see."
    m "And you, Zara?"
    scene ad566 with dssb
    za "I will go pro after college."
    za "Most likely in Tennis or some other sport."
    scene ad567 with dssa
    za "It's hard to choose when you're excellent at everything."
    za "And that's why you will lose."
    scene ad568 with dssa
    ni "What do you mean?"
    za "[name] challenged me."
    ni "Bad move [name]."
    scene ad569 with dssa
    d "I'll be fine."
    ni "What sport?"
    za "Tennis."
    scene ad576 with dssb
    za "You know what?"
    za "How about we do three different tournaments? So nobody can go *dull voice* 'But sport X is my weakness, mimimi.'"
    scene ad577 with dssb
    d "Like what?"
    scene ad578 with dssa
    za "Tennis will be the first."
    za "You choose the second."
    scene ad579 with dssa
    d "Surfing."
    scene ad580 with dssa
    za "...The beach isn't that far away, so- okay, yeah."
    za "But I have never surfed before."
    scene ad581 with dssa
    d "Me neither, and that makes it fair."
    scene ad582 with dssa
    za "Okay... The last one: A Triathlon."
    d "I'm in."
    scene ad583 with dssb
    "Zara gives you a sassy smile."
    ni "But please keep it friendly, okay?"
    scene ad584 with dssa
    za "It's all good, dad."
    za "I'll win anyways."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad585 with dssb
    ni "I hope you all liked the food."
    scene ad586 with dssb
    n "It was amazing!"
    scene ad587 with dssa
    d "It was pretty good."
    ni "Great!"
    scene ad588 with dssb
    ni "Vanessa, Zara, bring [name] and Nami to the garden."
    ni "I hope you're all up for some... well... more drinks."
    scene ad562 with dssb
    m "For me without alcohol please."
    ni "You're not staying overnight?"
    scene ad563 with dssa
    m "Oh- uhm, well, I need to get [name] and Nami home."
    scene ad570 with dssb
    n "[name] and I will head to Victoria's later."
    n "They invited us to stay the night."
    m "Oh, I see."
    scene ad566 with dssa
    za "Okay, follow me."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad589 with dssb
    za "Okay... You two be honest with me."
    za "How high is the chance that Nojiko and Nick are actually going to marry?"
    scene ad590 with dssb
    n "I have no idea how their relationship is going."
    scene ad592 with dssb
    za "Judging by what my Dad says, it's great."
    scene ad593 with dssa
    d "Noji thinks the same."
    scene ad591 with dssb
    n "That means we'll most likely see each other a lot more often."
    za "Yup."
    za "Even though-"
    scene ad594 with dssa
    d "Don't say it."
    scene ad595 with dssb
    za "Huh?"
    d "I've spent so much time around Bella, I know when a bratty girl tries to act superior."
    scene ad596 with dssa
    za "Haha."
    za "I am just joking, though."
    scene ad597 with dssa
    za "Money and status don't define an individual."
    n "Tha-"
    scene ad598 with dssa
    d "She isn't done. Wait for the but."
    scene ad597 with dssa
    za "BUT- their actions, skills and ambitions do."
    za "At least you sometimes use your brain."
    scene ad599 with dssb
    d "Don't forget I managed to play you and Nadia like fools."
    "Zara looks at you for a second with an unreadable expression."
    scene ad600 with dssa
    za "Do I need to lock you up in the locker room again?"
    scene ad603 with vpunch
    n "The what?"
    scene ad601 with dssb
    za "He didn't tell you?"
    scene ad602 with dssa
    n "Uhh- No. He didn't tell me."
    scene ad601 with dssa
    za "Nadia and I handcuffed him in the locker room."
    scene ad604 with dssb
    n "Is that why you were late to the board game?"
    d "Yeah."
    scene ad605 with dssa
    n "Why didn't you tell me?"
    scene ad606 with dssa
    d "It was irrelevant. I got out early."
    scene ad614 with dssb
    za "How did you free yourself?"
    if BellaKiss3x5 is True:
        scene ad615 with dssa
        d "Robin called Bella and told her about it."
        d "So she came and released me.."
        scene ad612 with dssb
        za "She released you right away? Or did she take advantage of the situation?"
        scene ad607 with dssa
        n "Nooo! Please! Not this."
        scene ad610 with dssa
        za "Oh, you don't like Bella?"
        n "Not at all."
        za "Are you the one she fooled with the uniform."
        scene ad608 with dssa
        "Nami says nothing."
        scene ad610 with dssb
        za "Yeah, your look says it all."
        za "Man... that must suck, Nami."
        za "[name] dating the girl you most likely despise."
        menu:
            "Correct her and say you and Bella aren't dating.":
                $ MCxBLNoDate4x0 = True
                scene ad611 with dssb
                d "Bella and I aren't dating."
                scene ad612 with dssa
                za "Oh, and the kiss you two shared was totally friendly, huh?."
                d "A one time thing."
                za "Mhm."
            "Stay quiet.":
                $ McxBLDate4x0 = True
                pass
    else:
        $ ZaraFavour4x0 = True
        scene ad611 with dssb
        d "I was found by Nora, Miriam and Kate."
        za "Oh."
        d "I now probably have a detention."
        scene ad616 with dssb
        za "Shit. Sorry."
        za "Did they get Marla?"
        d "She appeared later, but Nora cuffed herself to me and lost the key."
        scene ad617 with vpunch
        za "Hahaha!? No way?!"
        scene ad618 with dssa
        d "Yap."
        d "Then Marla came in and found me and Nora... who was only wearing a thong, locked together."
        za "I- don't know what to say... haha..."
        scene ad606 with dssb
        n "..."
        scene ad620 with dssb
        d "Apparently Robin called her."
        scene ad619 with dssa
        za "Did you-"
        scene ad620 with dssa
        d "Na, I didn't tell her."
        scene ad621 with dssa
        za "Oh. I didn't mean for that to happen..."
        za "I owe you one."
    scene ad613 with dssa
    za "But if it makes you feel better Nami."
    za "I'm also not the biggest fan of the guy my sister is dating."
    scene ad622 with dssb
    d "Mario."
    za "Oh? You know him?"
    d "Met him."
    scene ad623 with dssa
    n "When did you meet him?"
    d "Remember the guys that made fun of Mila?"
    scene ad624 with dssb
    za "Mila?"
    za "Mila Steiner?"
    d "Yeah."
    scene ad625 with dssb
    za "Her body is... damn."
    scene ad626 with dssb
    va "Just take whatever you like."
    scene ad627 with dssb
    n "I like your eyes."
    n "It's heterochromia, right?"
    scene ad628 with dssb
    va "Indeed."
    scene ad629 with dssb
    za "Where are you two heading afterwards?"
    n "We are going to visit Victoria and Mila."
    za "Victoria. She and I have gone to all of the same schools since Elementary. She's a nice girl."
    scene ad630 with dssa
    va "I remember her. Cute little girl. Lots of potential."
    scene ad631 with dssa
    za "Nami, are you dating someone? Or do you have a crush?"
    scene ad591 with dssb
    n "Not at the moment. "
    n "You?"
    scene ad631 with dssa
    za "No, dating would get in the way of my goals."
    scene ad607 with dssb
    n "You and Nadia seem to be good friends?"
    scene ad631 with dssa
    za "She is my best friend and enemy at the same time."
    scene ad632 with dssa
    za "We are both weirdly competitive, and that gives our relationship a very nice and interesting dynamic."
    d "It's half past seven."
    scene ad634 with dssa
    za "I'll drive you in five minutes."
    scene ad642 with dssb
    n "You will come back here, right?"
    scene ad635 with dssb
    d "Yeah, provided someone picks me up."
    scene ad634 with dssa
    za "*sigh* Is it so hard to get a driver's license?"
    d "If you don't have the money, yes."
    if bellameet is True:
        scene ad633 with dssa
        va "Uh hu."
    scene ad636 with dssa
    za "Start working."
    scene ad637 with dssa
    d "I have no interest in getting a driver's license right now."
    scene ad638 with dssa
    va "I'll pay for your license if you manage to win two out of three tournaments."
    scene ad639 with dssa
    za "Seriously? You're betting against me?"
    va "When did I ever bet on you?"
    za "Touche."
    scene ad640 with dssb
    za "Alright [name], let's go."
    scene ad641 with dssb
    n "But come back, okay?"
    d "For the second time... I will."
    scene ad645 with dssb
    pause
    scene ad643 with dssa
    d "(Something's not right. She's not like Bella described her at all.)"
    scene ad644 with dssa
    d "(She chooses her words very carefully.)"
    d "(I'll ask Bella about it on Monday.)"
    scene black with tleaf
    with Pause(.5)
    scene ad646 with tleaf
    pause
    scene ad647 with dssa
    d "What can you tell me about Vanessa?"
    za "Oh- don't tell me you're falling for her?"
    scene ad648 with dssb
    d "I'm not."
    d "Just curious, she seems a little strange."
    scene ad649 with dssa
    za "Hmm, na- if you want to get to know her, speak with her."
    za "But don't get your hopes up."
    za "She prefers a different social circle."
    scene ad650 with dssa
    d "And you?"
    scene ad651 with dssa
    za "I prefer people that are ambitious."
    scene ad652 with dssa
    za "Now get in."
    stop music fadeout 2
    scene black with tleaf
    with Pause(.5)
    play music "music/TheIntangible/The Intangible - Encyclopedia of Frozen Dreams.ogg"
    scene ad1284 with tleaf
    "Zara suddenly stops the car."
    scene ad1285 with dssa
    za "Tell me why you are meeting up with the coaches."
    scene ad1284 with dssa
    d "I can't."
    scene ad1285 with dssa
    za "Private training outside the school hours, obviously."
    scene ad1286 with dssb
    za "But why..."
    za "Miss Hill and Mister Stahl seem to be up to something."
    scene ad1287 with dssb
    za "By the way... We're here."
    scene ad1288 with dssa
    d "Thanks."
    d "Will you pick me up after we're done?"
    scene ad1289 with dssa
    za "Nah, I'll come with you."
    d "What?"
    za "I wanna know what's going on."
    scene black with dssb
    with Pause(.5)
    scene ad1080 with dssb
    pause
    scene ad1081 with dssb
    pause
    scene ad1082 with dssb
    pause
    scene ad1083 with dssb
    stop music fadeout 3
    $ persistent.unlockedImageHill5 = True
    "You take a deep breath."
    $ play_playlist(playlist_Ch1CollegeEnd)
    scene ad1084 with vpunch
    j "Bro!"
    scene ad1085 with vpunch
    d "Hey."
    scene ad1086 with dssb
    mh "What are you doing here, Zara?"
    scene ad1091 with dssb
    za "Oh, I just want to know what [name] is up to."
    scene ad1092 with dssa
    j "Why?"
    scene ad1093 with dssa
    za "Curiosity."
    scene ad1087 with dssb
    mh "*Sigh*."
    za "Now that I'm already here I can join, right?"
    scene ad1088 with dssb
    ms "I respect your ambition."
    ms "You can join the exercises but when we start playing, you're on the sideline."
    scene ad1094 with dssa
    za "I don't mind that. It'd be unfair to these... Let's call them boys."
    scene ad1095 with dssa
    ms "Alright, Spaghetti go change."
    scene ad1097 with dssa
    za "What about me?"
    scene ad1096 with dssa
    d "And where do we change?"
    scene ad1098 with dssb
    mh "The building across the fields."
    scene ad1089 with dssb
    sai "Why do we even have to change? It's an unofficial training..."
    scene ad1090 with dssa
    ms "It's a sign of union. You're a team and I'll make sure to burn it into everyone's head."
    scene ad1098 with dssb
    za "Let's go!"
    scene ad1099 with dssa
    pause
    scene ad1100 with dssb
    pause
    scene ad1102 with dssb
    pause
    scene ad1103 with dssa
    pause
    scene ad1104 with dssb
    pause
    scene ad1105 with vpunch
    pause
    scene ad1106 with vpunch
    za "Wuaah-"
    scene ad1107 with vpunch
    za "I only slightly tackled you!"
    d "That's how you make sure nobody retaliates... But I also didn't expect you to go flying... You're pretty light."
    menu:
        "Carry her.":
            $ ZaraCarry4x0 = True
            scene ad1110 with dssb
            pause
            scene ad1109 with dssb
            d "Don't tell anyone."
            scene ad1111 with dssb
            za "...I accept your apology."
        "Don't carry her and tell her to get up.":
            $ ZaraR +=1
            scene ad1108 with dssa
            d "Get up."
            scene ad1112 with dssa
            za "*Whisper* Asshole."
    scene black with dssb
    with Pause(.5)
    scene ad1113 with dssb
    pause
    scene ad1114 with dssb
    za "I should've worn a bra."
    scene ad1115 with dssb
    pause
    scene ad1116 with vpunch
    za "Keep your hands away from my body this time."
    scene ad1117 with dssa
    d "It was traumatising enough to have your... pancake on my face."
    scene ad1118 with vpunch
    za "My Pancake? I don't have pancake boobs!"
    za "You know you enjoyed it. Didn't you?"
    scene ad1119 with dssa
    d "I would have... with some syrup."
    scene ad1120 with dssb
    pause
    scene ad1121 with dssb
    mh "Hop on!"
    scene ad1122 with dssb
    pause
    scene ad1123 with dssb
    mh "Hold on!"
    scene ad1124 with vpunch
    pause
    scene ad1125 with dssa
    pause
    scene ad1126 with vpunch
    za "ARGH!"
    scene ad1127 with dssa
    d "Nrgh..."
    scene ad1128 with dssr
    mh "I was in the wrong- mode..."
    scene ad1129 with dssr
    za "Why did I pick the back spot... I'm flat... My boobs are actual pancakes now!"
    scene ad1132 with dssr
    mh "I've never taken people with me on that thing... Stupid race mode."
    menu:
        "Drive it yourself.":
            $ persistent.unlockedImageHill4 = True
            scene ad1131 with dssb
            $ McQuadDrive4x0 = True
            d "Let me drive."
            scene ad1132 with dssa
            mh "Why would I let you drive it?"
            scene ad1133 with dssb
            d "Because I'm not the one who almost killed us."
            d "(And I really wanna try this out.)"
            scene ad1134 with dssa
            mh "...Students are robust. They can take some damage."
            scene ad1135 with dssa
            za "Ready... I guess."
            scene ad1136 with dssb
            pause
            scene ad1137 with dssb
            pause
            scene ad1138 with dssb
            pause
            scene ad1139 with dssb
            za "[name]! Slow down a little, will you?"
            scene ad1140 with dssb
            pause
        "Don't and let Miss Hill drive it.":
            $ persistent.unlockedImageHill2 = True
            scene ad1131 with dssb
            $ HillQuadDrive4x0 = True
            d "This time... put it into 'Old people' mode."
            scene ad1132 with dssa
            mh "I got this... I just miscalculated."
            scene ad1142 with dssb
            d "...What're you doing?"
            scene ad1143 with dssa
            za "Safety first."
            scene ad1144 with dssb
            with Pause(.4)
            menu:
                "Put your arms around Miss Hill's waist.":
                    $ persistent.unlockedImageHill2 = True
                    $ HillWaist4x0 = True
                    scene ad1153 with dssa
                    mh "Ready?"
                    d "Yeah."
                    scene ad1154 with vpunch
                    d "WAIT! YOU DIDN'T CHANGE THE MODE!"
                    scene ad1155 with dssa
                    mh "Oh!"
                    scene ad1149 with dssb
                    pause
                    scene ad1150 with dssa
                    pause
                    scene ad1152 with dssb
                    pause
                "Put your arms up higher and close to her breasts.":
                    $ persistent.unlockedImageHill3 = True
                    $ HillBoobs4x0 = True
                    scene ad1145 with dssa
                    pause
                    scene ad1146 with dssa
                    mh "...[name], your arms."
                    d "Yeah, I'm not taking the risk of falling off... And it's not my fault that you're the size of a little wormy."
                    scene ad1145 with dssa
                    mh "I'll take that last one personal."
                    mh "Ready?"
                    d "Yeah."
                    scene ad1147 with vpunch
                    d "WAIT! YOU DIDN'T CHANGE THE MODE!"
                    scene ad1148 with dssa
                    mh "Oh!"
                    pause #click sfx
                    scene ad1149 with dssb
                    pause
                    scene ad1150 with dssa
                    pause
                    scene ad1151 with dssa
                    pause
            scene ad1157 with dssa
            pause
    scene ad1141 with dssa
    ms "Alright, everyone come here."
    scene ad1158 with dssb
    dam "Sup [name]."
    d "Hey Trey, Damian."
    scene ad1159 with dssb
    ms "Alright..."
    ms "The reason why we're doing this here is... We are going against the first team."
    scene ad1173 with dssb
    pause
    scene ad1175 with dssa
    j "Our own first team?"
    scene ad1159 with dssb
    ms "Yes. If we manage to beat the first team in a friendly but real match, yours and our chances of joining the team will massively improve."
    scene ad1160 with dssa
    j "The chances of tha-"
    scene ad1161 with dssa
    ms "-of that happening are slim, yes."
    ms "And that's why the effect that comes with a win is so much bigger."
    scene ad1162 with dssa
    mh "If we at least give them a serious challenge... we'll make sure that everyone at least makes the second team."
    scene ad1176 with dssb
    za "Now I am mad that we girls don't get the chance."
    scene ad1177 with dssa
    mh "I have to ask you to keep quiet about it."
    scene ad1176 with dssa
    za "I won't snitch."
    za "But still, us girls also deserve a chance like that."
    scene ad1163 with dssb
    ms "Life isn't fair."
    scene ad1164 with dssa
    mh "But judging by what I heard about you Zara, you should have no problem joining the girls team."
    scene ad1176 with dssb
    za "Of course not, but I'm not going for the basketball team. But, there are some girls I'd like to see on the team."
    scene ad1166 with dssb
    mh "Our plan is to beat our top athletes."
    scene ad1165 with dssa
    mh "And to make this possible, every single one here has to go beyond his limits."
    scene ad1167 with dssa
    ms "And most importantly, play as a team."
    ms "The good part is... Dwight, Aziz and Jazz won't be a part of it... Otherwise, this would be impossible."
    scene ad1168 with dssa
    ms "Bilbo, don't take it personally, but you won't be a starter."
    dam "But... will I get to play?"
    scene ad1170 with dssa
    ms "We'll see."
    scene ad1169 with dssb
    ms "Time to warm up, girls."
    ms "Start circling the field."
    scene ad1171 with dssb
    j "How many rounds?"
    scene ad1172 with dssa
    mh "Until we say it's enough."
    scene black with tleaf
    with Pause(.5)
    scene ad1178 with dssa
    j "So Nojiko is dating her father?"
    d "Yeah."
    scene ad1179 with dssb
    t "You're living the dream!"
    d "Mh?"
    t "Zara is smoking hot... and her sister..."
    t "Dude."
    scene ad1180 with dssa
    d "I have no such interest in her."
    scene ad1181 with dssa
    t "You're weird man."
    t "To me it appears you have no such interest in anyone."
    scene ad1182 with dssa
    d "That's true."
    scene ad1183 with dssb
    if BellaKiss3x5 is True:
        j "Except for Bella."
        j "People say they saw you guys kissing earlier today."
    else:
        $ NoraRumor = True
        j "There's a weird rumor going around... That you and Nora had intercourse."
        d "Not true."
        scene ad1184 with dssa
        j "Man, people really need to shut the fuck up... All these childish rumors."
        d "It's alright. I don't make much of it."
    scene ad1185 with dssb
    j "Damian, try to keep up!"
    scene ad1186 with dssa
    dam "I have to use twice the stamina to cover the same distance!"
    scene ad1188 with dssb
    $ persistent.unlockedImageZara8 = True
    d "(Zara is far ahead and shows no sign of slowing down.)"
    scene ad1189 with dssb
    d "(I will have to improve a lot if I want to have a chance against her.)"
    scene ad1190 with dssb
    pause
    scene ad1191 with dssa
    mh "What about a mustache?"
    mh "We give Zara a mustache and she may pass as a guy?"
    scene ad1192 with dssa
    ms "Hmm... we would still need to hide her breasts."
    scene black with Dissolve(2)
    show text "8 rounds later." with dissolve
    with Pause(2)
    scene ad1193 with vpunch
    mh "That's enough."
    scene ad1194 with dssb
    "Heavy breathing."
    scene ad1195 with dssb
    za "What a bunch of wusses."
    scene ad1196 with dssb
    mh "Ladies, get up."
    scene ad1197 with dssa
    j "Coach- *breathing*- This was too much."
    mh "Was it? Now you know what's awaiting you."
    scene ad1198 with dssb
    ms "Today was just an introduction, we'll end this with a few simple exercises."
    ms "And we've got one big advantage on our side."
    d "Which is?"
    scene ad1199 with dssa
    ms "They won't take us seriously."
    scene ad1200 with dssb
    mh "Spaghetti, you see... while the first team has some great players, many of them are quite cocky."
    mh "When we announce the game, they will laugh at us... and that's when we have to take our shot."
    scene ad1204 with dssb
    d "If this 'plan' succeeds... Does this mean you two are going to join the first team's coaching squad?"
    ms "Yes."
    scene ad1205 with dssa
    t "But how? Aren't there rules in place?"
    scene ad1203 with dssb
    ms "Since when does ZPR care about rules?"
    scene ad1202 with dssa
    t "I don't know? I don't know them."
    ms "Rules are more like guidelines."
    scene ad1201 with dssb
    mh "The results matter."
    mh "And the highest level of ZPR has our backs."
    scene ad1207 with dssb
    mh "There is a lot on the line for everyone here."
    mh "Don't forget that membership of the first team includes some nice benefits."
    scene ad1206 with dssb
    sai "Like what?"
    scene ad1207 with dssb
    mh "Thanks to the bill that has passed a few years ago, every athlete now owns his own image and likeness."
    scene ad1208 with dssa
    mh "Profitable sponsorships can be acquired."
    mh "An unofficial perk is the 'Athletes favor'. The top athletes can afford more missteps outside the field before serious consequences follow."
    scene ad1209 with dssa
    mh "And of course, you will be able to skip a class or course for training."
    scene ad1210 with dssb
    ms "*Whisper* And the girls... Well, being in the first team... that should explain itself."
    scene ad1211 with vpunch #sfx
    pause #hill klatsch seinen arm
    scene ad1212 with dssb
    d "The 'Athletes favor' doesn't sound so bad."
    scene ad1213 with dssa
    mh "For a troublemaker like you? Certainly not."
    t "The sponsorships... how much money are we talking about?"
    mh "That depends on the deal."
    scene ad1214 with dssb
    d "(This could be the solution to help Nojiko out.)"
    d "(She mentioned that we're kinda struggling with money since I started therapy.)"
    scene ad1215 with dssb
    d "(And I seriously do not want to get a fucking part time job.)"
    d "(I need to improve even further.)"
    scene ad1216 with dssa
    d "(And there is one person I could ask for help...)"
    d "(It hurts my pride... but the wellbeing of Nojiko and Nami is much more important.)"
    scene ad1217 with dssb
    pause
    scene ad1218 with dssb
    pause
    scene ad1219 with dssb
    j "Me, Dex and some others play a lot of street basketball in our hood. I'd like you to come by."
    scene ad1220 with dssa
    d "It sounds like there's some hidden agenda."
    scene ad1219 with dssa
    j "There is."
    j "Dex and Jazz are both in the first team and have quite the influence."
    j "I don't know what it is, but I feel like you and I have some synergy."
    scene ad1221 with dssa
    d "Maybe you just need to hit the can."
    "He lets out a laugh."
    scene ad1222 with vpunch
    d "I'll think about it."
    scene ad1223 with dssa
    pause
    scene ad1224 with vpunch
    j "Did you play in high school?"
    scene ad1225 with dssa
    d "Yeah, I did. But I quit the team shortly into the first season."
    scene ad1226 with vpunch
    j "Why's that?"
    d "Personal reasons."
    scene ad1227 with dssb
    j "I didn't want to dig, sorry."
    d "All good."
    d "I would've made team captain."
    scene ad1228 with dssb
    j "What school were you in?"
    d "Tropics something... I forgot the full name."
    j "Yo, I remember you guys were favorites, and then all of a sudden the team fell apart."
    scene ad1229 with dssb
    d "I was the team... The others were mostly average."
    scene ad1230 with vpunch
    pause
    scene ad1231 with dssa
    d "My uncle used to play it with me."
    scene ad1232 with dssa
    d "He more or less taught me what I had to know."
    scene ad1234 with vpunch #sfx
    pause
    scene ad1233 with dssb
    j "My father used to play with me when I was young."
    scene ad1235 with vpunch #sfx
    pause
    scene ad1236 with dssb
    j "I just can't seem to hit those three pointers..."
    scene ad1237 with dssa
    j "Whenever I cross the line and go for the three point basket... I lose my cool. I can't hit them."
    scene ad1238 with dssa
    d "You don't need to."
    scene ad1239 with dssa
    d "Focus on your strengths. Your team is there to balance out your weaknesses."
    scene ad1240 with vpunch
    pause
    scene ad1250 with vpunch
    pause
    scene ad1243 with dssa
    d "But if you have to throw one..."
    d "Do it like you mean it."
    scene ad1244 with vpunch
    pause
    scene ad1245 with dssa
    pause
    scene ad1246 with dssa
    pause
    scene ad1247 with dssa
    d "Did it go in?"
    j "Almost."
    scene ad1248 with dssa
    d "That would've been sick, huh?"
    scene ad1249 with vpunch
    j "Fuck yeah, hahaha."
    scene black with dssb
    with Pause(.5)
    scene ad1251 with dssb
    pause
    scene ad1252 with dssb
    ms "Okay ladies, we'll see each other every day at the same time."
    ms "Except for the day of the bar opening."
    mh "And now get out of here."
    stop music fadeout 2
    scene black with tleaf
    with Pause(.5)
    play music "music/TheIntangible/The Intangible - Encyclopedia of Frozen Dreams.ogg"
    scene ad1253 with tleaf
    j "Bye [name]."
    d "See ya, guys."
    scene ad1254 with dssb
    pause
    scene ad1255 with dssb
    za "Sometimes, I wish I was a dude."
    scene ad1256 with dssa
    d "Because of the higher threshold of athletic performance?"
    scene ad1257 with dssa
    za "Yes."
    scene ad1258 with dssa
    za "But thennnn... I remember that we girls have boobs."
    d "Must be nice."
    scene ad1259 with dssb
    za "They really are."
    scene black with dssb
    with Pause(.5)
    scene ad1260 with dssb
    pause
    scene ad1261 with dssb
    pause
    scene ad1262 with dssa
    d "Zara."
    za "Mh?"
    scene ad1264 with dssb
    d "...Can you teach me?"
    scene ad1263 with dssa
    za "I really don't want to teach you how to kiss..."
    scene ad1264 with dssa
    d "I need to improve... in everything."
    scene ad1265 with dssa
    za "You want me to train you?"
    scene ad1266 with dssb
    d "Yes."
    scene ad1267 with dssb
    za "*Chuckles* dude, we have a bet going on!"
    za "Why would I train my enemy?"
    scene ad1268 with dssa
    d "I get it."
    d "You aren't good enough to train me and still win."
    scene ad1269 with dssa
    za "I obviously get that you're trying to bait me here... And I'm sure you could do a lot better..."
    scene ad1270 with dssa
    za "But what do I get in return?"
    scene ad1271 with dssb
    d "I don't know? What do you want?"
    scene ad1272 with vpunch
    za "Hmm- AH!"
    scene ad1273 with dssa
    za "There is this sorority I'd like to prank."
    za "Have you ever heard of the Jackson & Schwartz college?"
    d "No."
    scene ad1274 with dssb
    za "My sister and her boyfriend go there and you need some serious money to be accepted."
    za "Anyways, I dislike a few girls there and I'm planning an act of vengeance."
    za "And you will help me and more or less do what I tell you to do."
    scene ad1275 with dssa
    d "I will not say yes until I know what you want me to do."
    scene ad1276 with dssa
    za "You are heading to Victoria later, right?"
    d "Mhm."
    za "Ask her about Melanie Ceril."
    scene ad1277 with dssa
    d "And what will she say?"
    scene ad1278 with dssa
    za "You'll see."
    za "But she's my main target."
    scene ad1279 with dssb
    za "Give me your answer after you speak to Vici."
    if BellaKiss3x5 is True:
        za "And little Bella also has some history with her."
    scene ad1280 with dssa
    za "Let's head back before my sister turns Nami into a weirdo."
    scene ad1281 with dssa
    d "Nami's already a weirdo."
    za "Trust me... Vanessa is weirder."
    scene ad1282 with dssa
    d "Hard to believe."
    za "Do you wanna bet on who's weirder?"
    scene ad1283 with dssb
    d "That would be too easy."
    za "Hehe."
    $ persistent.unlockedImageRS53 = True
    if BellaKiss3x5 is True:
        scene ad777xx with tleaf
        pause
        scene ad777x with dssr
        pause
    scene black with tleaf
    jump AfterTraining


label AfterTraining:
    with Pause(.5)
    scene ad653 with tleaf
    pause
    scene ad654 with dssb
    pause
    scene ad655 with dssa
    n "Hey!"
    scene ad656 with dssa
    d "Cheeto."
    d "How was it?"
    scene ad657 with dssb
    n "Noji and Nick tried to entertain us and failed miserably."
    d "Poor wormy."
    scene ad658 with dssa
    n "Next time take me with you..."
    scene ad659 with dssb
    ni "Zara, you stayed?"
    scene ad662 with dssb
    za "I joined their training."
    scene ad663 with dssa
    za "I'm a dude now."
    scene ad664 with dssa
    va "That explains some things."
    scene ad665 with dssa
    n "Really? Could I have joined, too?"
    d "You would have died."
    scene ad666 with dssb
    n "I'm more in shape than you are!"
    n "Next time I'll come with you."
    scene ad667 with dssa
    d "No, next time I'll go alone."
    scene ad668 with dssa
    za "Not if you want me to honor our deal."
    n "What deal?"
    scene ad669 with dssa
    za "I'm his personal trainer now."
    scene ad660 with dssb
    ni "Seriously?"
    ni "I thought you two were on different sides? I'm glad you aren't, though."
    scene ad670 with dssb
    za "Oh we still are."
    za "But I gain no satisfaction from beating some loser."
    za "That's why I will try to make him strong to give me at least a little bit of a challenge."
    scene ad671 with dssa
    n "What if he beats you?"
    scene ad672 with dssa
    "Zara lets out a small laugh."
    za "Unlikely."
    n "But what if?"
    scene ad673 with dssa
    za "I'll kill myself."
    ni "Zara..."
    scene ad674 with dssa
    za "I am joking... I'll kill [name]."
    scene ad680 with dssb
    va "If [name] actually beats you, you would jump him... but not to kill him."
    scene ad681 with dssa
    ni "Vanessa..."
    za "Yeah, fuck off!"
    scene ad661 with dssb
    m "At least [name] and Zara have something in common, even though it seems to be of a competitive nature."
    m "Just please don't let it escalate."
    scene ad675 with dssb
    za "I'm cool. If [name] beats me fair and square, I will not lose it."
    za "I'm gonna cry... A lot... But I will not lose it."
    scene ad676 with dssb
    pause
    scene ad677 with dssa
    ni "You two seem to have a nice relationship."
    scene ad678 with dssa
    n "We do, right?"
    d "Yeah, I guess."
    scene ad682 with dssb
    m "Anyways..."
    scene ad683 with dssa
    pause
    scene ad687 with dssb
    d "When do we wanna head to Vic and Mila?"
    scene ad688 with dssa
    za "Not that soon."
    scene ad689 with dssa
    d "Mh?"
    scene ad688 with dssa
    za "I declined a party invitation in order to be here for you people."
    scene ad684 with dssb
    va "How about we do something actually entertaining? Let's play a double."
    scene ad685 with dssa
    za "Who with whom?"
    scene ad684 with dssa
    va "Nami and I against you and [name]."
    va "Even though I'd like to see [name] go against you, I don't want to spoil the surprise when your real match begins."
    scene ad686 with dssb
    ni "And I will start cleaning some dishes. Nojiko, if you want you can watch the kids."
    m "No no, I will help you do the dishes and let the kids play in peace."
    scene ad690 with vpunch
    n "Let's go then!"
    scene ad691 with dssa
    za "You two might want to change, too."
    za "You don't want to be all sweaty when you head to Vic."
    za "I have a few tennis outfits."
    scene ad684 with dssb
    va "[name], come with me. I'll give you one of my dad's outfits."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad692 with dssb
    pause
    scene ad693 with dssb
    va "You may undress."
    scene ad694 with dssa
    pause
    $ persistent.unlockedImageRS50 = True
    if UmB is True:
        scene ad695 with dssb
        va "I am surprised. That's a fine fabric."
        va "I didn't take you for someone with a sense of fashion."
        $ VaAla = True
        d "I didn't buy it myself."
        scene ad696 with dssa
        va "Who did?"
        d "A friend."
        scene ad697 with dssb
        va "What friend?"
        scene ad698 with dssa
        d "Are you always like this?"
        scene ad697 with dssa
        va "Nojiko and my dad are dating, of course I would want to learn all about you."
        scene ad699 with dssa
        va "...It has to be a girl, unless... you are gay?"
        scene ad700 with dssa
        va "But you don't give me a gay vibe- so yes... A girl... a girl that has most likely seen you in underwear... or in even less."
        va "Maybe I should've led with this question... Do you have a girlfriend?"
        scene ad701 with dssa
        d "I don't."
        va "Zara mentioned the name Bella..."
        "Before you can answer, she puts her index finger on your mouth."
        scene ad702 with dssa
        va "Bella von Halen?"
        va "You would fit into her social circle..."
        scene ad703 with dssa
        va "Now it makes sense."
        va "When I asked her about a boyfriend- she also replied with a 'no' and had the same expression on her face."
        va "It was the same story with her... I was just asking the wrong question."
        scene ad704 with dssa
        va "Do you have a crush on someone, [name]?"
        menu:
            "Yes.":
                scene ad705 with dssa
                "Vanessa smiles."
                va "Same as Bella."
            "You know the answer":
                $ VaInt = True
                scene ad706 with dssa
                va "*whisper* I do indeed."
            "No.":
                $ McNoCrush4x0 = True
                scene ad705 with dssa
                "She just smiles."
    else:
        $ VanessaShopping4 = True
        scene ad712 with dssb
        va "I have never seen such an atrocious fabric before."
        d "It's a normal fabric."
        "Vanessa chuckles."
        scene ad713 with dssa
        va "Here, touch my dress."
        scene ad714 with dssb
        pause
        d "And what am I supposed to feel?"
        scene ad715 with dssa
        va "The fine stitching, the quality materials, and how sensual it feels on the skin."
        scene ad716 with dssa
        d "I think in order to feel that I'd need to wear it."
        scene ad697 with dssa
        va "The problem is that you never experienced a real fabric before."
        scene ad717 with dssb
        pause
        scene ad718 with dssa
        va "Wednesday, 7PM, you'll meet me on Acadia Avenue."
        scene ad719 with dssa
        d "The what?"
        scene ad718 with dssa
        va "It's a shopping street."
        d "I'll pass."
        scene ad720 with dssa
        va "This is not up for discussion. I cannot let you run around like this..."
        va "I cannot risk you bringing shame on us."
        menu:
            "If something as irrelevant as wearing some low quality underwear brings shame to your family, then your family didn't have any real status in the first place.":
                $ VaBew = True
                scene ad721 with dssa
                "Vanessa stares at you."
                scene ad723 with dssa
                "After a second of silence, her serious face fades into a smile."
                scene ad724 with dssa
                va "Touche."
                va "My offer still stands."
            "Alright, if I have to.":
                $ VaUeb = True
                pass
    scene ad707 with dssa
    va "And now turn around, I've gotta change, too."
    scene ad708 with dssa
    play music "music/Suspense/Scott Buckley - Nightfall.ogg"
    d "(Something is seriously wrong. I think Vanessa is playing Bella like a fool.)"
    d "(That girl behind me is no airhead.)"
    scene ad709 with dssb
    d "(The way she speaks and moves... an elegant articulation if I have ever seen one.)"
    d "(There is no trace of insecurity in her voice, nothing superficial and every thing she says seems to have a purpose.)"
    scene ad710 with dssb
    d "(I just hope she didn't manage to trick Bella into saying more than she should have...)"
    scene ad711 with dssb
    va "I am surprised you haven't peeked yet."
    d "I'm not some creep."
    $ persistent.unlockedImageVanessa1 = True
    va "Then you may turn around."
    stop music fadeout 2
    $ persistent.unlockedImageCh4x4 = True
    scene black with Dissolve(1)
    hide screen music_player_trigger
    scene Over with dissolve
    $ renpy.pause(4.0, hard=True)
    with Pause(28.35)
    scene ad725 with dssb
    show screen music_player_trigger
    play music "music/TheIntangible/The Intangible - Encyclopedia of Frozen Dreams.ogg"
    d "If I may ask, isn't that underwear a very uncomfortable choice for a tennis match?"
    scene ad726 with dssa
    va "I get why you would think that... After all it's lingerie."
    va "But a thong is pretty much the most comfortable underwear for sports."
    scene ad727 with dssb
    va "Next to wearing no underwear at all."
    va "Nami will be able to confirm this later."
    scene ad728 with dssa
    "You raise your brows and keep silent."
    scene ad729 with dssa
    va "Nami is wearing a normal panty and it will slip weirdly between her cheeks."
    d "I get it."
    scene ad730 with dssb
    pause
    scene ad731 with vpunch
    "Suddenly Zara bursts into the room."
    za "How long can it take to change an outfit?!"
    scene ad732 with dssb
    pause
    scene ad733 with dssb
    za "Did I interrupt anything?"
    scene ad734 with dssa
    va "I don't know."
    va "Maybe [name] was about to put the moves on me- or maybe he wasn't."
    scene ad735 with vpunch
    va "We'll never find out, thanks to you."
    scene ad736 with dssa
    "Zara seems to be lost for words."
    za "Just change so we can play!"
    scene ad737 with dssa
    va "What do you think I was doing? I mean... I am naked here."
    scene ad738 with dssb
    za "I can see that."
    scene ad739 with dssa
    za "[name], come."
    scene ad740 with dssa
    va "He can stay."
    scene ad741 with dssa
    za "Ooooh no. He won't stay."
    scene ad742 with dssa
    d "I'm changed, and our conversation is over. I can't think of any reason to stay."
    scene ad740 with dssa
    va "Then you and my sister can adjourn to the field."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad782 with dssb
    za "What the fuck was that?"
    scene ad783 with dssa
    d "Nothing happened."
    scene ad782 with dssa
    za "So she was standing there topless and in lingerie because she felt like it?"
    scene ad783 with dssa
    d "Yes."
    scene ad784 with dssa
    za "Yeah, that sounds like her."
    scene ad785 with dssa
    za "Don't take it too far or you'll burn yourself."
    scene ad786 with dssa
    d "She seems to be a smart girl."
    scene ad787 with dssa
    za "A smart girl?"
    za "She's the most intelligent person I know."
    scene ad788 with dssb
    d "(Damn it, Bella.)"
    d "(She's too arrogant to realize when something big is in front of her.)"
    d "Hey, I gotta call someone real fast."
    scene ad789 with dssa
    za "Make it quick."
    scene ad790 with dssa
    pause
    scene ad1748 with dssb
    b "Yes?"
    scene ad1749 with dssa
    d "Do not interact with Vanessa anymore."
    scene ad1748 with dssa
    b "Why?"
    scene ad1749 with dssb
    d "She is not the airhead you think she is."
    scene ad1750 with dssb
    b "Dude, I spent more than one evening with her- I think I-"
    d "Bella! Trust me, okay?"
    scene ad1751 with dssb
    if BTY is True:
        b "Okay."
    else:
        b "...Okay"
    d "Until Monday then."
    scene ad1752 with dssa
    b "Yeah."
    scene ad1753 with dssa
    pause
    scene ad1754 with dssa
    $ persistent.unlockedImageAyua3 = True
    $ persistent.unlockedImageBellaCh42 = True
    ay "...Do you have any nudes of [name]?"
    scene ad1756 with dssa
    pause
    scene ad1755 with dssa
    ay "Is that a 'no'?"
    scene black with tleaf
    with Pause(.5)

label Tennis04:
    $ persistent.unlockedImageRS51 = True
    $ play_playlist(playlist_GirlyCh4x)
    scene ad743 with tleaf
    pause
    scene ad744 with dssa
    n "What took you so long?"
    scene ad745 with dssb
    za "My sister was giving him a strip show."
    n "What?"
    scene ad746 with dssa
    d "She was just trying to intimidate me a little."
    d "Don't worry."
    scene ad750 with dssa
    n "She seems to have a problem with us."
    scene ad747 with dssa
    za "Give her some time..."
    scene ad748 with dssb
    pause
    scene ad749 with dssa
    va "Alright Nami, we'll take this side."
    scene ad751 with dssb
    va "And Zara... this is a friendly game."
    scene ad752 with dssb
    n "I bet my arm is going to hurt after this."
    scene ad753 with dssa
    za "Okay, listen [name] and Nami."
    scene ad754 with dssb
    za "Do you know how a double is played?"
    n "N-"
    za "As expected."
    scene ad755 with dssb
    za "[name], I will be in the front and you will be a few meters behind me."
    scene ad756 with dssa
    n "Meters?"
    scene ad757 with dssa
    za "Yeah, we use real metrics here."
    za "In a double, each member takes a side."
    scene ad758 with dssa
    za "I'll do left and stay in the front. You will do the opposite."
    scene ad759 with dssb
    va "Nami, I'd say you mark the front in our team."
    va "I'll take the back."
    scene ad758 with dssa
    za "Let's position ourselves."
    scene ad762 with dssa
    za "And [name], try not to shoot that ball against my backside."
    scene ad760 with dssb
    va "Don't worry Nami, I won't hit you."
    scene ad761 with dssb
    za "Let's not lose."
    d "Then try to keep up."
    scene ad762 with dssa
    za "[name] serves."
    d "I do what? Serve drinks?"
    scene ad763 with dssa
    za "Here, do it."
    za "You've seen tennis before on TV?"
    scene ad764 with dssb
    d "Yes, but who pays attention to that?"
    za "Just hit the ball..."
    scene ad765 with dssb
    pause
    scene ad766 with vpunch
    pause
    scene ad811 with vpunch
    pause
    scene ad767 with vpunch
    za "Ngh!"
    scene ad812 with dssb
    va "That was a good one."
    n "Thanks!"
    scene ad768 with dssb
    za "Did you play before?"
    scene ad813 with dssb
    n "No, I really didn't."
    scene ad769 with dssa
    za "Serve."
    scene ad778 with vpunch
    pause
    za "You got it [name]!"
    if fitness == 2 or mobility == 1:
        $ ZaraSp +=1
        scene ad770 with dssb
        za "What was that? Hahaha!"
        scene ad818 with dssb
        va "I missed the ball."
        scene ad771 with dssb
        za "Oh yeah, you did."
        scene ad818 with dssb
        va "I now remember why I don't play anything with you anymore."
        scene ad774 with dssb
        za "...Sorry."
    else:
        $ ZaraSp -=1
        scene ad772 with dssb
        za "*sigh*"
        za "You suck."
        d "It's my first time playing tennis, so fuck off."
        scene ad775 with dssa
        za "You didn't get to the ball in time because you lack general fitness!"
        scene ad814 with vpunch
        n "Give him some slack!"
        "Zara ignores Nami."
        scene ad818 with dssb
        va "Now I remember why I don't play anything with you anymore."
        scene ad773 with dssb
        za "...*sigh*"
        za "Sorry [name]."
    scene ad776 with dssb
    d "Where does this desperate need to prove yourself come from?"
    scene ad777 with dssa
    za "I just like being the best."
    scene ad819 with dssb
    "Vanessa raises her brows at her sister's words.	"
    scene ad820 with dssa
    va "Sure... and there is no other reason right? No deep insecurities?"
    scene ad780 with vpunch
    "Zara gives Vanessa a death stare."
    za "Shut the fuck up."
    scene ad821 with dssb
    va "I didn't mean to irritate you."
    scene ad781 with vpunch
    za "Okay listen you-"
    scene ad791 with dssb
    menu:
        "Throw the ball at Zara's head.":
            $ ZZWDBI = True
            $ McCoZa4x0 = True
            scene ad792 with dssb
            za "It's-"
            play music "music/Suspense/Scott Buckley - Nightfall.ogg"
            scene ad793 with vpunch
            pause
            scene ad794 with dssb
            za "What the..."
            scene ad795 with vpunch
            d "Get your head out of your ass, Zara!"
            d "We've got a game to play!"
            scene ad796 with dssb
            pause
            scene ad827 with dssa
            pause
            scene ad828 with dssa
            pause
            scene ad796 with dssa
            "She stares at you in disbelief."
            scene ad797 with dssa
            za "What did you just say to me?"
            scene ad798 with dssa
            d "You want to go pro someday?!"
            scene ad799 with vpunch
            d "Don't make me laugh."
            scene ad800 with vpunch
            "You push her backwards."
            scene ad801 with vpunch
            pause
            scene ad802 with dssb
            if ZaraSp ==-1:
                d "Look at you! Crying like a little bitch because it doesn't go your way!"
            else:
                d "A real leader doesn't put other people down!"
            scene ad803 with dssb
            d "You want to train me? Then man the fuck up and start being a real leader or I will have to look for someone that can."
            scene ad804 with dssa
            pause
            scene ad805 with dssa
            pause
            scene ad808 with dssa
            za "You serve."
            scene ad809 with dssb
            "You nod."
            $ play_playlist(playlist_GirlyCh4x)
        "Can we just keep playing?":
            $ McNoCoZa4x0 = True
            za "Then serve!"
            d "What's the matter with you, cunt?"
            "Zara inhales deeply."
            scene ad809 with dssb
            za "*sigh* Sorry, okay?"
            scene ad810 with dssb
            za "She just knows how to press my buttons."
            scene ad822 with dssb
            va "And I do indeed love pressing them."
            scene ad823 with dssa
            va "But I also have to apologize sister."
            va "I shouldn't do this in front of our guests."
            scene ad824 with dssa
            d "Ready Nami?"
            scene ad812 with vpunch
            n "Yes!"
    scene ad779 with vpunch
    "You throw the ball into the air-"
    if fitness == 2 or mobility == 1:
        $ ZaraSp +=1
        "And perfectly hit it."
        scene ad817 with vpunch
        pause
        n "DAMN!"
        scene ad769 with dssa
        za "That was a good one."
        d "Thanks."
    else:
        scene ad816 with vpunch
        n "Ngh!"
        pause
        d "Damn..."
        scene ad825 with dssb
        va "You're too passive."
        scene ad826 with dssa
        za "...We will tackle that."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad849 with dssb
    "Heavy breathing."
    za "Okay [name], match point... Please give it everything you got."
    scene ad831 with vpunch
    if fitness is 2 or mobility is 1:
        "Nami serves the ball."
        scene ad838 with vpunch
        pause #zara
        scene ad829 with vpunch
        pause
        scene ad839 with vpunch
        pause
        scene ad830 with vpunch
        pause
        $ persistent.unlockedImageVanessa4 = True
        "At the last possible second, you jump to the right and manage to hit the ball back."
        scene ad832 with vpunch
        va "Ah-."
        scene ad833 with dssa
        va "Bummer."
        scene ad843 with vpunch
        za "Nice one!"
        d "That was a close call."
        scene ad844 with dssb
        za "Close calls are what make life exciting!"
        scene ad845 with vpunch
        za "FUCK, I LOVE WINNING!"
        scene ad846 with dssa
        va "You okay up there?"
        za "I was never better!"
        scene ad847 with dssa
        d "My hand."
        scene ad848 with dssb
        za "Oops."
        scene ad835 with dssb
        $ persistent.unlockedImageNamiCh44 = True
        va "You played good Nami. I think you've got talent."
        scene ad837 with dssb
        va "Don't leave your potential unused."
        n "Thank you!"
        scene ad835 with dssb
        va "It's a bummer I didn't manage to get the last ball there."
        n "It was a very hard to catch ball, we did good."
    else:
        "Nami serves the ball."
        scene ad832 with vpunch
        pause
        scene ad829 with vpunch
        pause
        scene ad839 with vpunch
        pause
        scene ad830 with vpunch
        pause
        "Nami's stroke makes an unexpected turn and you miss the ball by a lot."
        n "YES!"
        scene ad834 with dssb
        va "Great stroke, Nami!"
        scene ad841 with dssb
        "Zara closes her eyes."
        d "My bad."
        scene ad840 with dssa
        za "Of course it was your bad..."
        scene ad842 with dssb
        za "But... we will work on it... It was an excellent counter from Nami."
        scene ad835 with dssb
        $ persistent.unlockedImageNamiCh44 = True
        va "You've got talent."
        scene ad837 with dssb
        va "Don't leave your potential unused."
        n "Thank you!"
    za "I need to honor my after game routine. I'm gonna head into the jacuzzi."
    scene ad836 with dssb
    va "We all go."
    va "[name] and Nami need to be refreshed for their visit later."
    scene ad850 with dssb
    n "We don't have any swimwear."
    va "We never wear swimwear in there."
    n "Oh."
    va "So, will you two join us?"
    scene ad851 with dssb
    n "Yes- right- yes? - Nami mumbles while she looks at you."
    d "Why not."
    za "Great, follow me."
    scene ad852 with dssb
    stop music fadeout 3
    va "[name]? Do you mind helping me with the drinks?"
    scene ad853 with dssa
    $ play_playlist(playlist_AmbientNamiLake)
    d "I actually do not like being alone with you, but I'll help you with the drinks."
    scene ad854 with dssa
    za "Wow, cold blooded."
    scene ad855 with dssa
    va "That's not a nice thing to say."
    scene ad856 with dssa
    za "Nami, let's go."
    scene ad858 with dssb
    pause
    scene ad857 with dssa
    d "Don't take it the wrong way, but I feel like you're trying to play me."
    scene ad859 with dssa
    va "What makes you think that?"
    scene ad860 with dssa
    pause
    scene ad861 with dssa
    pause
    scene ad862 with dssb
    va "Okay... I'll cut the act."
    va "I just like pushing people a little."
    scene ad863 with dssa
    if ZZWDBI is True:
        va "And I wasn't sure about you when we first met."
        scene ad864 with dssa
        va "You stared at me like some simp."
        scene ad866 with dssa
        va "Not that I'm not used to being stared at... I mean, look at me."
        scene ad867 with dssb
        va "Don't take it personally."
        va "I do have my doubts about most members of the weaker sex."
        d "Males are the weaker sex?"
        scene ad870 with dssb
        va "Of course."
        va "What do you have from being physically strong if you are already under the spell of a woman?"
        scene ad868 with dssb
        va "But you didn't fall for my body. So please excuse my behavior from earlier."
        va "And I changed my mind. I do respect you."
        va "Not many people manage to put my sister in her place."
    else:
        va "I wasn't sure about you when we first met."
        scene ad864 with dssa
        va "You stared at me like some simp."
        scene ad866 with dssa
        va "Not that I'm not used to being stared at... I mean, look at me."
        scene ad867 with dssa
        va "Don't take it personally."
        va "But I do have my doubts about most members of the weaker sex."
        d "Males are the weaker sex?"
        scene ad870 with dssb
        va "Of course."
        va "What do you have from being physically strong if you are already under the spell of a woman?"
        scene ad868 with dssb
        va "But you didn't fall for my body. So please excuse my behavior from earlier."
    scene ad869 with dssb
    va "Follow me."
    scene black with tleaf
    with Pause(.5)
    jump Jacuzzi4x0


label Jacuzzi4x0:
    $ persistent.unlockedImageRS52 = True
    scene ad1290 with tleaf
    m "Hey you two."
    scene ad1291 with dssb
    ni "Coming for drinks?"
    va "Yes, we're honoring Zara's post game routine and are heading into the jacuzzi."
    scene ad1292 with dssb
    m "You don't have any swim wear, do you [name]?"
    scene ad1293 with dssa
    va "We do not use swim wear in the jacuzzi."
    scene ad1294 with dssa
    m "But- is- uh that okay?"
    scene ad1299 with dssb
    va "Why wouldn't it be, Nojiko?"
    va "Is there something wrong with a naked body?"
    scene ad1295 with dssb
    ni "Vanessa."
    scene ad1297 with dssa
    m "It's alright, Nick."
    scene ad1298 with dssa
    m "I guess there's nothing wrong with a naked body, no."
    scene ad1300 with dssb
    va "You too are invited."
    scene ad1301 with dssa
    m "Thanks but I'll pass."
    stop music fadeout 2
    scene black with tleaf
    with Pause(.5)
    $ play_playlist(playlist_Jaccuzi)
    scene ad871 with dssb
    pause #Nami and Zara in
    scene ad872 with dssa
    pause
    scene ad873 with dssa
    pause
    scene ad874 with dssa
    "All eyes follow you as you sit down."
    scene ad875 with dssa
    d "What?"
    scene ad876 with dssb
    za "*Giggles* Nothing."
    scene ad877 with dssb
    va "Just take whatever drink you want."
    scene ad878 with dssb
    va "There is no alcohol in them."
    scene ad879 with dssb
    n "Why not?"
    scene ad883 with dssb
    za "After a workout, you shouldn't consume anything toxic."
    za "We're here to cleanse our mind and body."
    scene ad884 with dssa
    pause
    scene ad880 with dssb
    n "Oh gawd... This is so nice."
    n "I wish we had a jacuzzi at home."
    scene ad885 with dssa
    za "Who knows... maybe you two are going to move in at some point."
    n "If Noji and Nick go the extra step?"
    za "Yes."
    scene ad881 with dssb
    n "Would Nick even want that?"
    scene ad886 with dssb
    za "Our house has more than enough rooms."
    scene ad888 with dssb
    va "And Dad would probably like having another male in the house."
    scene ad887 with dssb
    za "Oh yeah."
    scene ad882 with dssb
    n "What do you mean?"
    scene ad887 with dssb
    za "Dad always kind of wanted a son, too."
    n "I see. I see."
    scene ad890 with dssb
    za "You're so quiet, [name]."
    scene ad891 with dssa
    d "I prefer to speak when necessary, and not waste time with useless filler talk."
    scene ad892 with dssb
    za "Man, you sound like her."
    scene ad893 with dssb
    "Vanessa gives you an approving nod."
    scene ad894 with dssa
    n "*whisper* I now know why they go in here without swim wear."
    scene ad895 with dssa
    d "*whisper* I guess because of those bubbly bois we are sitting on?"
    scene ad896 with dssa
    n "*Whisper* Yes... No matter how I sit, I feel it."
    scene ad899 with dssa
    za "Cross your legs if the bubblies are getting too much Nami."
    scene ad900 with dssa
    va "Or sit like an unladylike brute, like my sister."
    scene ad899 with dssa
    za "And you two should learn how to whisper properly."
    scene ad897 with dssb
    n "...They're really strong, aren't they?"
    scene ad889 with dssb
    va "You should position your pelvis away from the main impact zone."
    va "Then it's okay."
    d "Please don't."
    scene ad890 with dssa
    za "What?"
    scene ad898 with dssb
    n "[name] doesn't like talking about spicy stuff."
    scene ad901 with dssb
    za "A prude? Huh, I didn't expect that."
    scene ad902 with dssa
    d "I'm not a prude..."
    scene ad903 with dssb
    d "I just don't like hearing about Nami's pelvis... And Nami sit normally and get your ass down..."
    scene ad904 with dssb
    va "Why don't you like hearing about it?"
    scene ad905 with dssa
    va "Nami has a very erotic body."
    scene ad906 with dssa
    pause
    scene ad907 with dssa
    va "It's nothing to be disgusted about... it's beautiful."
    scene ad908 with dssa
    pause
    scene ad909 with dssb
    za "Keep it in your pants, Vanessa."
    scene ad907 with dssb
    va "Your body is a temple, Nami."
    va "He might be [name], but every male should honor it."
    scene ad909 with dssb
    za "Vanessa, stop being weird... Not everyone shares your weirdo views."
    scene ad910 with dssa
    n "What views exactly?"
    scene ad911 with dssb
    za "She thinks males are the weaker sex."
    scene ad912 with dssa
    va "I think most males are weaker."
    scene ad913 with dssa
    va "A womans weapons are so effective against a simple minded male."
    scene ad914 with dssa
    va "Our perky breasts..."
    scene ad915 with dssa
    $ persistent.unlockedImageVanessa5 = True
    va "Our fine lines that lead directly to our intoxicating vagina."
    scene ad916 with dssa
    va "Use your weapons wisely and the world is yours."
    scene ad918 with dssa
    pause
    scene ad917 with dssa
    va "Except if the male is like [name]. I haven't been able to decrypt him yet, and he didn't show any reaction towards my body."
    scene ad919 with dssa
    za "Maybe you're just unattractive to him?"
    scene ad920 with dssa
    va "No, there is no male that finds me unattractive. The events surrounding [name] go deeper."
    scene ad921 with dssa
    $ persistent.unlockedImageNamiCh45 = True
    va "...Even girls seem to lose themselves in my presence."
    scene ad922 with dssa
    d "Is she always like that?"
    scene ad923 with dssa
    za "You have no idea."
    za "And still, she refuses to bed her boyfriend."
    scene ad921 with dssa
    n "How long have you two been together?"
    va "For around a year now."
    n "And he puts up with that?"
    scene ad914 with dssa
    va "Yes, he knows the wait will be worth it."
    scene ad915 with dssa
    va "Besides that... We just don't have actual intercourse at the moment."
    va "We do petting and other things."
    scene ad924 with dssa
    za "*Laughs* You just reminded me about the butt plug."
    scene ad925 with dssa
    n "What about it?"
    scene ad926 with dssa
    za "She makes her boyfriend wear a butt plug."
    scene ad930 with dssa
    va "Zara. This is private information. I do not want anyone knowing about it."
    va "If word got out, it would cause immense pain to him."
    scene ad931 with dssa
    va "I do hope you two will keep quiet about it."
    if bellameet is True:
        d "(...Saw that plug in action.)"
    scene ad932 with dssa
    n "Of course."
    scene ad926 with dssb
    za "Yeah, I apologize."
    scene ad927 with dssa
    za "But still... *Giggles* It's damn funny."
    scene ad933 with dssb
    n "As long as he likes it, I don't see the problem."
    n "Does he like it?"
    scene ad935 with dssa
    va "At first no..."
    scene ad936 with dssa
    va "But my lady parts can be very convincing."
    scene ad934 with dssa
    n "Man, you're really something."
    scene ad937 with dssa
    va "He just needs to know who is in control."
    scene ad938 with dssa
    va "And... I hear some excitement in your voice, Nami."
    va "You two seem close, but not close enough to talk about the interesting things in life?"
    scene ad939 with dssa
    d "It's weird."
    scene ad940 with dssa
    va "It's not. Zara and I talk about everything."
    scene ad928 with dssb
    za "You talk. I listen, and occasionally give you a friendly nod."
    scene ad941 with dssb
    d "I'm a male."
    scene ad942 with dssa
    va "Yes, you've got a penis, but why does this keep you from being open with her?"
    scene ad929 with dssb
    za "I get his point, though."
    scene ad942 with dssa
    va "Me too. But why care about the rules people with simpler minds have made up?"
    scene ad943 with dssr
    va "If you two want to experience a real bond of trust, you'll need to open up a little, [name]."
    scene ad944 with dssa
    d "If I had known that this supposedly relaxing jacuzzi bath would turn into this, I would have passed."
    scene ad945 with dssa
    va "Don't worry Nami, he will loosen up."
    scene ad947 with dssa
    za "Just like your boyfriend, thanks to the butt plug. Hahaha."
    "Nami chuckles."
    scene ad948 with dssa
    za "Sorry, sorry, I just couldn't resist."
    scene ad949 with dssb
    va "Somedays... I'm also wearing one."
    n "You are?!"
    scene ad949 with dssa
    va "While I do like to remind my boyfriend of who's in charge."
    va "I'm still by his side and I want him to know that I would go through the same for him."
    scene ad950 with dssa
    n "Does it hurt?"
    scene ad949 with dssa
    va "Not at all, no."
    va "I don't wear it often. It's just a spontaneous act."
    scene ad951 with dssa
    "Nami moves closer to Vanessa."
    n "Which material is the best for beginners?"
    scene ad952 with dssa
    va "I'll give you some tips one day."
    scene ad953 with dssb
    pause
    scene ad954 with dssa
    pause
    scene ad955 with dssa
    za "Seems like you and I are in the same position."
    za "A person that likes to talk about the weirdest things while you sit there like:"
    scene ad956 with dssa
    pause
    scene ad957 with dssa
    "You chuckle."
    d "Yeah, pretty much."
    d "But you were right... Vanessa is on another level."
    scene ad958 with dssb
    za "Who's older, you or Nami?"
    scene ad959 with dssa
    d "Nami. Around a year older."
    scene ad958 with dssa
    za "Why is she red?"
    scene ad959 with dssa
    d "That you'll have to ask her parents."
    scene ad960 with dssa
    za "What happened to yours?"
    scene ad961 with dssa
    d "They died in a car accident."
    scene ad960 with dssa
    za "And Nami's?"
    scene ad961 with dssa
    d "Believe it or not... The same."
    d "What happened to your mother?"
    scene ad962 with dssa
    za "She repeatedly cheated on Dad."
    scene ad963 with dssa
    d "Are you still in contact?"
    scene ad964 with dssa
    za "Barely."
    za "Vanessa and I can't forgive her for what she tried to do."
    d "Like?"
    if fitness == 2 or mobility == 1:
        $ InfZaraMom = True
        scene ad965 with dssa
        za "She tried to frame Dad when we were younger."
        za "When he discovered that she was cheating and wanted a divorce, she tried to convince Vanessa and I that Dad had touched us inappropriately."
        za "We were children and easy to influence."
        scene ad966 with dssa
        za "I almost caved and started to believe it when Vanessa talked some sense into me."
        za "She was always a few years above everyone else."
        scene ad967 with dssa
        za "And I... was easy to influence."
    else:
        scene ad968 with dssa
        za "Sorry. That's private."
        d "I understand."
    scene ad969 with dssb
    n "Man... the bubble thingies are everywhere!"
    n "And being on my knees destroys the comfortable aspect."
    scene ad972 with dssa
    n "[name], can I sit on your leg?"
    d "Dude... You're nude."
    scene ad973 with dssb
    n "It's just a leg!"
    n "Just for a short while."
    $ persistent.unlockedImageZara6 = True
    menu:
        "Fine.":
            $ persistent.unlockedImageNamiCh46x = True
            $ NamiTni4x0 = True
            $ OeVaGe4x0 = True
            scene ad974 with dssa
            n "Thanks!"
            scene ad976 with dssr
            za "Alright, I am gonna head to the shower now."
            za "Make sure to say bye before you leave."
            n "Of course!"
            scene ad977 with dssr
            va "I will also head out."
            va "You two can stay a little longer."
            va "I'll prepare one of the restrooms for you two."
            scene ad982 with dssr
            pause
            scene ad981 with dssa
            n "Even besides the bubbly bois, a jacuzzi is so nice."
            d "It really is..."
            scene ad983 with dssa
            n "Imagine if we really moved in here!"
            n "We could use it whenever we liked!"
            scene ad984 with dssa
            n "But Mila wouldn't like that."
            scene ad985 with dssa
            d "She's really looking forward to moving out."
            scene ad986 with dssa
            n "*sigh*."
            scene ad987 with dssa
            d "Nami, you're slipping into my lap."
            n "Yeah."
            scene ad988 with dssa
            d "Yeah? Sit on top of-"
            scene ad989 with dssa
            "Nami slips into your lap."
            scene ad990 with dssa
            n "See... not that bad."
            scene ad991 with dssa
            d "Which negates the entire point in the first place."
            d "You didn't want to sit on the bubbly bois but now you're on them again."
            scene ad992 with dssa
            n "No, the bubbly is at my butt."
            d "*sigh* I hate you."
            scene ad993 with dssb
            n "I really wish you would open up a little to me!"
            n "Just like Vanessa said!"
            scene ad994 with dssa
            d "Don't get influenced by what she says."
            if NamiCuddle04 is True:
                scene ad995 with dssa
                d "But, it's not bad... Kinda like at the lake today."
                scene ad996 with dssa
                n "Yeah... kinda."
                n "You also held me there, though..."
                scene ad997 with dssa
                d "I just wanted your beer."
                scene ad998 with dssa
                n "...And we were wearing clothes."
                n "But not a lot more..."
                scene ad999 with dssa
                pause
                scene ad1000 with dssa
                n "I like that. It makes me feel protected."
                scene ad1001 with dssa
            pause
            scene ad1002 with dssb
            n "So... you really felt something today at the lake?"
            d "Nami. Don't ruin this here."
            scene ad1003 with dssa
            n "I'm serious!"
            n "It would be a huge step!"
            scene ad1004 with dssr
            d "*sigh*."
            d "I don't know dude..."
            scene ad1005 with dssa
            n "Okay, let me try something."
            scene ad1004 with dssa
            d "No!"
            d "Just for your information, I can still drown you in this jacuzzi."
            menu:
                "Sorry Cheeto... No.":
                    $ persistent.unlockedImageNamiCh46 = True
                    $ NamiTni4x0 = True
                    $ HcNaFrt = True
                #   hide screen music_player_trigger
                    scene ad1015 with dssb
                    "You lift the Cheeto from your lap."
                    scene ad1016 with dssa #blink
                    d "I'll place you somewhere far away from me."
                    n "So... there was life in it?!"
                    scene ad1017 with dssa
                    d "Yes, if you had kept going, maybe he would have showed a reaction."
                    scene ad1018 with dssa #blink
                    n "Then why did you stop it prematurely?"
                    n "Now we are only at 'maybe' instead of 'proven'!"
                    n "You fucking idiot!"
                    scene ad1021 with vpunch
                    d "Nami... Trust me when I say... You might be capable of it... but it certainly won't work if you force it."
                    scene ad1022 with dssa
                    pause
                    scene ad1023 with dssa
                    pause
                    n "Phoenix Nami at it again!"
                    n "I'm just glad it's not medical."
                    scene ad1024 with dssb
                    d "And now that it is proven, we won't have to do it again."
                    scene ad1025 with dssb #blink
                    n "Oh no... it isn't proven yet."
                    n "The next time we will go all the way..."
                    d "Or... a counter offer... I'll start avoiding you from now on."
                    scene ad1027 with dssa
                    n "-Hey... Not funny."
                    d "It wasn't a joke."
                    d "While I do appreciate your enthusiasm and your will to 'help' me."
                    d "I do find it very uncomfortable... Especially in such a risky environment."
                    scene ad1028 with dssa
                    menu:
                        "Comfort her and pull her towards you.":
                            $ persistent.unlockedImageNamiCh47 = True
                            $ NamiTni4x0 = True
                            scene ad1030 with dssb
                            d "(I don't know what it is...)"
                            d "(She's clearly misbehaving... and just a fool in general.)"
                            d "(But... I'd be lying if I said I didn't like her close to me.)"
                            scene ad1031 with dssa
                            d "(The way her skin feels...)"
                            d "(*Sigh* I'm losing it.)"
                            scene ad1032 with dssa
                            "You grab Nami's hand."
                            n "Mh?"
                            scene ad1033 with dssb
                            pause
                            d "(Nami's body language changed. She is nervous.)"
                            scene ad1034 with dssa
                            d "You're tense."
                            scene ad1035 with dssa
                            n "Noji is right around the corner and we are in a jacuzzi..."
                            scene ad1034 with dssa
                            d "I thought we wouldn't give a damn about that anymore?"
                            scene ad1036 with dssa
                            n "...Right. But it takes some time getting used to."
                            scene ad1034 with dssa
                            d "You have done much worse before, literally two minutes ago."
                            d "It's not the act that makes you nervous. It's who initiates it."
                            d "When you initiate it, you get a sense of control. With that control, you get to decide how far the situation goes."
                            d "But what can you control now?"
                            scene ad1040 with vpunch
                            n "*whisper* I'm always in control."
                            scene ad1041 with dssa
                            d "*whisper* We'll see about that, Cheeto."
                        "Let her calm down.":
                            pass
                    scene ad1042 with dssb
                    d "I'm gonna get out."
                    scene ad1043 with dssb
                    n "Mhm, I will... uuh follow soon."
                    scene ad1044 with dssb
                    pause
                    scene ad1045 with dssa
                    pause
                    scene ad1047 with dssa
                    n "*whisper* Bubbly... where are..."
                    scene ad1048 with vpunch
                    n "*gasps* AH- there you are..."
                    scene ad1049 with dssa
                    pause
                    stop music fadeout 2
                    scene black with Dissolve(2)
                "Put an end to it.":
                    $ KoFuNa = True
                    scene ad1053 with vpunch
                    d "Enough of this!"
                    d "It's one thing that you want to help me but you're taking it too far."
                    scene ad1053 with dssa
                    d "Stop it... Seriously."
                    scene ad1052 with dssa
                    n "Yes... Sorry."
                    scene ad1054 with dssa
                    menu:
                        "Comfort her.":
                            $ persistent.unlockedImageNamiCh47 = True
                            scene ad1030 with dssb
                            pause
                            scene ad1032 with dssa
                            d "Come over here..."
                            scene ad1033 with dssa
                            pause
                            scene ad1034 with dssa
                            d "Please don't do something like that again."
                            scene ad1035 with dssa
                            n "I promise."
                            d "Thanks."
                            d "Now please get up. I want to get out."
                            scene ad1043 with dssb
                            n "Mhm, I will... uuh follow soon."
                            scene ad1044 with dssb
                            pause
                            scene ad1045 with dssa
                            pause
                            scene ad1047 with dssa
                            n "*whisper* Bubbly... where are..."
                            scene ad1048 with vpunch
                            n "*gasps* AH- there you are..."
                            scene ad1049 with dssa
                            pause
                            scene black with Dissolve(2)
                        "Don't comfort her.":
                            $ NamiTni4x0 = False
                            n "I am gonna get out to escape the awkwardness..."
                            scene ad1052 with dssb
                            n "I'm really sorry."
            stop music fadeout 2
            scene black with Dissolve(2)
            jump VicHouse04
        "No, sit on the edge.":
            n "Then I am going to get out!"
            scene ad976 with dssb
            za "Alright, it's time for me to get out before I get all wrinkly."
            za "Make sure to say bye before you leave."
            n "Of course!"
            scene ad978 with dssb
            va "You two can stay a little longer."
            va "I'll prepare a restroom for you two."
            scene ad1042 with dssb
            d "I'm also heading out."
            scene ad1043 with dssb
            n "Mhm, I will... uuh follow soon."
            scene ad1044 with dssb
            pause
            scene ad1045 with dssa
            pause
            scene ad1047 with dssa
            n "*whisper* Bubbly... where are..."
            scene ad1048 with vpunch
            n "*gasps* AH- there you are..."
            scene ad1049 with dssa
            pause
            stop music fadeout 2
            scene black with Dissolve(2)

label VicHouse04:
    $ play_playlist(playlist_Diner)
    $ persistent.unlockedImageZara7 = True
    scene ad1057 with dssb
    m "[name]!"
    scene ad1058 with dssa
    d "*sigh* The jacuzzi made me tired."
    scene ad1059 with dssb
    za "That's what it's for."
    scene ad1060 with dssb
    za "You have a nice workout, then you jump into the jacuzzi, AND THEN a quick shower and right into bed."
    za "You will sleep like an angel."
    scene ad1061 with dssb
    d "Knowing that I will beat you in every discipline makes me sleep like an angel."
    scene ad1062 with dssa
    pause
    scene ad1063 with dssa
    "Zara starts giggling a little."
    za "I will drink your tears to refill my electrolytes."
    scene ad1064 with dssa
    n "That was amazing!"
    scene ad1065 with dssa
    n "But we should head to Victoria's now."
    scene ad1066 with dssb
    n "Thanks a lot for the food Nick, it was amazing!"
    d "Yes, it was very good."
    scene ad1067 with dssa
    ni "I am glad you two liked it."
    scene ad1068 with dssb
    ni "Zara, are you driving them?"
    scene ad1069 with dssa
    d "No, it's okay, we'll take the bus."
    scene ad1070 with dssa
    ni "Are you sure?"
    scene ad1071 with dssa
    $ persistent.unlockedImageNojiko3 = True
    n "Yeah, you all drank a little."
    scene ad1072 with dssa
    m "Please be careful."
    scene ad1073 with dssa
    n "Yes Noji."
    scene ad1074 with dssa
    d "Where'd you get that fluff? Don't tell me it's from your belly button..."
    scene ad1075 with vpunch
    za "*Laughs* No! It's from your shirt!"
    d "Even worse... You stole my property."
    scene ad1076 with dssb
    n "Bye Zara and thank you for the game and especially for the jacuzzi!"
    scene ad1077 with dssa
    za "It was a pleasure!"
    scene ad1078 with dssb
    d "I'll see you."
    scene ad1079 with dssa
    za "Yeah."
    stop music fadeout 2
    scene black with tleaf
    with Pause(.5)
    play music "music/TheIntangible/The Intangible - Encyclopedia of Frozen Dreams.ogg"
    scene ad1757 with tleaf
    pause
    scene ad1758 with dssb
    n "*sings* Phoenix Nami- at it again... flying through the world-... Na, that needs to be different."
    scene ad1759 with dssa
    d "Are you creating a song about yourself?"
    scene ad1760 with dssa
    n "Yes."
    scene ad1761 with dssa
    d "Nice."
    scene ad1762 with dssa
    n "*sings* Wormy [name]... and Phoenix Nami... fighting crime-... or doing crimes?"
    scene ad1763 with vpunch
    n "WHAT ARE WE?! The good or the bad?"
    scene ad1764 with dssa
    d "I thought I was Raven [name]?"
    scene ad1765 with dssb
    n "Oh right."
    n "*sings* Raven [name] and Wormy Nami-... No what! I'm a phoenix!"
    scene ad1766 with dssb
    n "Aaaah... I am tired."
    scene ad1767 with dssa
    d "Let's just cancel and go to bed."
    scene ad1768 with dssa
    n "No, we promised."
    scene ad1767 with dssa
    d "I didn't promise anything."
    scene ad1768 with dssa
    n "We're going!"
    scene ad1769 with dssb
    pause
    scene ad1770 with dssb
    pause
    scene ad1771 with dssb
    pause
    scene black with tleaf
    with Pause(.5)
    scene ad1773 with tleaf
    pause
    scene ad1774 with dssa
    n "What do you think of Vanessa?"
    scene ad1775 with dssa
    menu:
        "I find her quite impressive.":
             $ VanessaImpressive4x0 = True
             d "I've never seen someone like her before. She's quite the presence."
             scene ad1776 with dssa
             n "Are you into her?"
             scene ad1777 with dssa
             d "I don't fall easily... but I can't deny that she left an impression."
        "I don't know yet. We would need to see her more often and under different circumstances.":
            $ VanessaUndecided4x0 = True
            pass
        "I don't like her.":
            $ VanessaDislike4x0 = True
            pass
    scene ad1776 with dssa
    n "Yeah... But man... she's... something else."
    scene ad1777 with dssa
    d "At some point in the jacuzzi, I thought you were about to kiss."
    scene ad1776 with dssa
    n "Me too, dude."
    scene ad1778 with dssb
    n "Nobody has ever looked at me like that before... Like holy shit."
    d "It seems like she had quite the impact on you."
    scene ad1779 with dssa
    n "Yeah... I still get shivers..."
    scene ad1781 with dssa
    pause
    scene ad1780 with dssa
    n "There was one weird moment, though."
    n "While you and Zara were gone... Vanessa asked me about my earring."
    d "So?"
    scene ad1782 with dssa
    n "Sasha did the same... and she has the exact same one... Just the other side."
    n "As if they once were a pair."
    scene ad1783 with dssa
    d "Just tell them where you bought them."
    scene ad1784 with dssb
    n "Don't you remember?"
    scene ad1785 with dssa
    d "No."
    scene ad1784 with dssa
    n "I told you that I got this one from that woman many years ago."
    scene ad1785 with dssa
    d "I'm certain that my past me didn't listen to you talk about earrings."
    scene ad1780 with dssa
    n "Isn't it weird?"
    d "Who was that woman?"
    scene ad1782 with dssa
    n "I don't know? She appeared when you and Summer ditched me again, and I was crying on a bench."
    d "When was that?"
    scene ad1784 with dssa
    n "Easily eight years ago."
    d "Well, just ask Sasha where she got hers from."
    scene ad1786 with dssb
    n "Vanessa said they somehow seemed familiar."
    if BellaKiss3x5 is False:
        scene ad1788 with dssa
        d "I know a detective club that could help you... Nora's detective club."
        scene ad1787 with dssa
        n "Who?"
        scene ad1788 with dssa
        d "Nevermind... The joke only works if you were there."
    scene ad1789 with dssb
    pause
    if NamiTni4x0 is True:
        scene ad1790 with dssa
        d "(I feel so comfortable around her... I never told her this but her presence is a blessing.)"
        d "(I know that I would miss her sometimes annoying personality if she wasn't around.)"
        scene ad1791 with dssa
        d "(Sometimes I wish that time stood still and we could hang around forever... Someday she'll find a guy and I might find a girl and then we're only going to see each other on holidays.)"
        scene ad1792 with dssa
        d "(You always come through for me.)"
        scene ad1793 with dssa
        pause
        d "(What if...)"
        scene ad1794 with vpunch
        d "(...Whatever thought just crossed my mind is simply crazy.)"
        scene ad1795 with dssa
        d "(And yet feels weirdly right.)"
    else:
        scene ad1790 with dssa
        pause
        scene ad1793 with dssa
        pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ad1796 with dssb
    $ persistent.unlockedImageNamiCh48 = True
    d "Next stop is ours."
    scene ad1797 with dssa
    n "I hope they've got some coffee..."
    scene ad1798 with dssb
    pause
    scene ad1799 with dssa
    pause
    scene ad1800 with dssb
    pause
    scene ad1801 with dssa
    pause
    stop music
    scene black with Dissolve(2)
    with Pause(.5)
    hide screen music_player_trigger
    if BellaKiss3x5 is True:
        $ persistent.unlockedImageRS58 = True
        $ persistent.unlockedImageCh4x5 = True
        show text "Meanwhile." with Dissolve(2)
        with Pause(1)
        scene Mama with dissolve
        $ renpy.pause(4.0, hard=True)
        with Pause(63)
        scene black with dissolve
    jump Chapter4x5
