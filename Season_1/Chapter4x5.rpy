label Chapter4x5:
    $ achievement.grant("FinishChapter4")
    $ achievement.sync()
    if miladate is True:
        $ MilaDate = True
    $ play_playlist(playlist_Ch4x5)
    show screen music_player_trigger
    scene ae1 with tleaf
    mi "Hey!"
    d "Hey."
    scene ae2 with dssr
    mi "What's wrong? You look a little unwell."
    scene ae3 with dssa
    d "I'm just exhausted."
    scene ae2 with dssa
    mi "We've got coffee."
    scene ae4 with dssa
    n "Oh yeah! I really need some coffee!"
    scene ae5 with dssa
    mi "Sure! Follow me."
    scene ae6 with dssb
    pause
    scene ae7 with dssa
    pause
    scene ae8 with dssr
    d "Hey."
    scene ae9 with dssa
    v "Hi!"
    scene ae10 with dssr
    pause
    scene ae11 with dssa
    v "*Giggles*"
    scene ae12 with dssa
    d "What?"
    scene ae13 with dssa
    v "I don't think you've ever smiled at me before."
    d "Did I smile?"
    scene ae14 with dssr
    d "I guess it's because I haven't seen you much lately."
    scene ae15 with dssa
    v "I got the feeling you were avoiding me a little."
    d "I was."
    scene ae16 with dssa
    pause
    scene ae17 with dssr
    d "Sorry."
    d "Don't take it too personally."
    scene ae18 with dssr
    v "Then why did you do it?"
    scene ae19 with dssa
    d "I'm not great at handling sensitive people."
    d "You're soft, it's the exact opposite of what I am."
    d "But I like that about you."
    d "It's just that there is a high risk of me accidentally hurting you and I think that is the last thing you need at the moment."
    scene ae20 with dssr
    "Victoria stares into the room."
    scene ae21 with dssa
    v "...The last thing I need right now is people avoiding me."
    v "Uncertainty is killing me, [name]."
    v "A sea of questions already plagues my thoughts... Please don't make me add 'Is he only here because of pity?' to them..."
    scene ae22 with dssa
    d "I'm not here because of pity."
    d "We all experience tragedies and the last thing I want is to waste my time with a person I don't like."
    scene ae23 with dssa
    d "Which certainly isn't you."
    scene ae24 with dssa
    d "I'm sorry I added another worry to your collection."
    scene ae25 with dssa
    d "What I said to you at the center... I didn't just say that..."
    scene ae26 with dssa
    d "I need you, Victoria."
    d "And I have to ask something of you."
    scene ae27 with dssa
    v "Sure."
    scene ae28 with dssa
    d "I want you and Bella to meet."
    scene ae29 with dssr
    v "Huh? We did meet."
    scene ae30 with dssb
    d "No, I mean really spend a few hours together."
    d "I'm sure she- yeah, I'm sure she'd like you."
    scene ae31 with dssa
    v "I didn't get that feeling when I spoke to her."
    scene ae30 with dssa
    d "It's just because she likes to play the untouchable little cunt."
    scene ae32 with dssa
    v "*whisper* That's a mean word."
    d "I'm mean."
    scene ae33 with dssa
    v "*Whisper* I know... *giggle*."
    scene ae34 with dssa
    v "But... Please promise me you're not going to avoid me anymore."
    v "If you want space just tell me so, but I want you to be upfront with me."
    scene ae35 with dssa
    d "From now on I will."
    d "No more fucking around."
    scene ae36 with dssa
    v "If Maja was here she'd SSSH you."
    d "And I'd gracefully ignore her."
    scene ae37 with dssa
    "She chuckles."
    scene ae38 with dssa
    pause
    scene ae39 with dssa
    v "From Monday onwards, I'll have therapy every single day."
    scene ae40 with dssa
    d "I see... And I assume you're asking me if I'll be there?"
    v "Not every time... but sometimes?"
    d "I'll definitely come with you on the first day."
    scene ae41 with dssa
    v "Thanks!"
    scene ae42 with dssr
    "You gently place her legs onto your lap, and she carefully observes your gentle strokes."
    scene ae44 with dssb
    v "I wish I could feel your touch."
    d "Someday you will."
    if BellaKiss03x is True:
        scene ae45 with dssr
        v "I've heard you and Bella kissed."
        scene ae46 with dssa
        d "Yes, we did."
        scene ae45 with dssa
        v "Is it serious?"
        scene ae46 with dssa
        d "I would never kiss someone if there wasn't at least a little seriousness behind it."
        if vicdate is True:
            scene ae45 with dssa
            v "What does this mean for our date?"
            menu:
                "Cancel the date with Victoria.":
                    $ VicDateCanceledBella4x5 = True
                    $ vicdate = False
                    scene ae46 with dssa
                    d "I think it would be best to put it on ice."
                    d "I guess, I'll have to figure out where this Bella thing leads me."
                    scene ae47 with dssr
                    v "O-okay."
                    scene ae51 with dssa
                    d "Hey."
                    d "We're cool, right?"
                    scene ae48 with dssa
                    v "I, of course, don't like it... but I'll respect your wish."
                    scene ae49 with dssa
                    v "And- And I hope it works out between you and Bella."
                    d "I still want to spend time with you."
                    scene ae50 with dssa
                    v "I'd like that."
                "Continue dating Victoria.":
                    $ VicDateContinuedBella4x5 = True
                    scene ae46 with dssa
                    d "I still want to get to know you on a... potentially romantic level."
                    scene ae47 with dssr
                    v "What about Bella?"
                    d "I'm just not sure... about anything."
                    scene ae50 with dssa
                    v "I will talk to Bella first."
                    v "I don't want to step on her toes."
                    scene ae51 with dssa
                    d "She'll say 'Do whatever you want, I don't care'... But she won't mean it."
                    scene ae50 with dssa
                    v "I don't want to hurt anyone."
                    v "You've gotta promise me that you'll tell me if things get too serious with her."
                    scene ae51 with dssa
                    d "I will."
    stop music fadeout 2.0
    scene ae45 with dssr
    $ persistent.unlockedImageRS59 = True
    $ persistent.unlockedImageVicCh4x58 = True
    d "Victoria, does the name 'Melanie Ceril' mean anything to you?"
    $ play_playlist(playlist_Ch4x5A)
    pause
    scene ae52 with dssr
    "She nods a few times."
    scene ae53 with dssr
    d "Your expression tells me that she's bad news."
    scene ae54 with dssa
    v "She almost drowned me in middle school."
    scene ae55 with dssa
    d "What?"
    scene ae54 with dssa
    v "We had a school trip to a waterpark and she held my head underwater until Zara intervened."
    scene ae55 with dssa
    d "Why?"
    scene ae56 with dssa
    v "She hated me for many reasons."
    v "I developed my breasts very early and... I think she wasn't as 'lucky'."
    scene ae55 with dssa
    d "That was the reason?"
    scene ae56 with dssa
    v "One of the reasons. She also hated that I smiled so much... She was also obsessed with a guy in our class."
    v "He liked me but I had no interest in romantic relationships at that time."
    v "And she saw that we were talking a lot and when she confronted him, he told her that I was hitting on him and never left him alone."
    scene ae54 with dssa
    v "The last thing she said to me was that she would stomp on my face with her heels and put them through my eyes."
    d "She seems unstable."
    scene ae57 with dssb
    v "I don't know... maybe she's just misunderstood."
    scene ae58 with dssr
    d "Don't be an idiot."
    d "Nobody normal speaks like that... I should know."
    scene ae60 with dssr
    v "Maja thought she was behind my accident."
    v "I am still a little scared."
    v "It's not like I could run away in my current condition."
    scene ae59 with dssa
    d "If she ever touches you, it'll be the last thing she ever does."
    scene ae61 with dssb
    "Victoria positions herself closer to you."
    v "What if you're not there?"
    d "I'm not the only one who has your back."
    scene ae62 with dssa
    v "Zara used to keep an eye on me."
    d "I'm really surprised to hear that. I didn't know you two knew each other that well."
    scene ae63 with dssr
    v "We weren't friends but she kept an eye on me because... I couldn't and still can't really defend myself."
    v "Once she even fought Melanie... I was so afraid she'd get hurt... Zara... Not Melanie."
    d "Did she get hurt?"
    scene ae64 with dssa
    v "Her lip was bleeding but Melanie looked worse."
    if BTY is True:
        d "(I'm still convinced that Bella would be a great addition.)"
        d "(As cunty as she is... She is very protective of the people she likes... Victoria might remind her of her lost little sister.)"
        d "(Giving Victoria an extra layer of protection.)"
    d "(People like this Ceril cunt are unpredictable. Even at my lowest point I could've never hurt someone as soft as Victoria.)"
    scene ae65 with dssb
    d "(I've gotta keep an eye on her and also talk with Mila and Nami about this.)"
    if vicdate or VicDateContinuedBella4x5 is True:
        scene ae66 with dssr
        v "I built a big binder of potential date destinations."
        v "If you-"
        scene ae67 with dssa
        d "Let me stop you right there..."
        d "A whole binder?"
        scene ae68 with dssa
        v "*Blush* I- uh... yes."
        scene ae67 with dssa
        d "Vic... All I want is a simple... date."
        scene ae68 with dssa
        v "You don't want to call it a date?"
        scene ae67 with dssa
        d "It's complicated."
        d "But...-"
        scene ae69 with dssa
        v "No no! My bad! I'm sorry. I didn't want to come on sooo strong!"
        v "I just really want you to like it."
        scene ae70 with dssa
        d "I like this here."
        d "No unnecessary noise... Just..."
        menu:
            "Give her a kiss.":
                $ KissedGirl = True
                $ persistent.unlockedImageVicCh4x59 = True
                $ VictoriaKiss4x5 = True
                scene ae71 with dssa
                pause
                scene ae72 with dssa
            "Don't kiss her.":
                scene ae72 with dssa
        d "A quiet, deep moment."
        d "I like it simple."
        scene ae73 with dssa
        v "Okay- then- then I'll research simple."
        scene ae74 with dssa
        d "No."
        d "How about you and I just get together here again? Just you and me."
        d "We'll wait 'till Maja is out and... you know, just hang out."
        scene ae75 with dssa
        v "*Whispers* I'd love that."
    scene ae66 with dssr
    v "I heard you're good at basketball."
    scene ae76 with dssa
    d "From whom?"
    scene ae66 with dssa
    v "I overheard some guys talking."
    scene ae77 with dssa
    v "One of them was talking you down, and I was about to give him a piece of my mind!"
    scene ae78 with dssa
    d "You can't please everyone. Don't even try."
    scene ae79 with dssr
    v "I really reeaaaally hope I'll be able to walk again before we leave college, and then we can play something together."
    scene ae80 with dssa
    d "You will."
    if RoRum is True:
        scene ae81 with dssa
        v "There-... *sigh*"
        v "Is this a good moment to ask you about your freak-out?"
        scene ae82 with dssa
        d "Yeeeah, sorry about that."
        d "I used to know a girl that was very important to me."
        d "She... well- she was my girlfriend."
        scene ae83 with dssa
        d "She went missing... and still is."
        d "That... Rubber you have, she had the exact same one."
        scene ae84 with dssa
        v "Oh. As a little child I won a whole bunch of them at a theme park."
        d "Yeah, I'm just fucked up in the head and kinda lost my cool."
        d "And I tend to read too much into things when it comes to Summer."
        scene ae85 with dssr
        v "Summer? The one you talked about when we first met?"
        d "Yeah."
        scene ae86 with dssa
        v "I'll help you find her!"
    scene ae87 with dssb
    pause
    scene ae88 with dssa
    d "How's Maja doing?"
    scene ae89 with dssa
    v "She's fine. I guess."
    v "I'm just worried that Maja's sacrificing everything for me..."
    scene ae90 with dssa
    d "Nami and I are here if you need us... Maja can take some days off."
    scene ae89 with dssa
    v "It's not just that."
    v "We have medical bills to pay. Our healthcare isn't covering it all."
    v "I can sometimes see how it's eating away at her."
    scene ae91 with dssr
    v "I want to help her so bad... but what can I even do?"
    v "I am so useless in this state."
    scene ae92 with dssa
    d "Not true."
    d "You have a very special voice."
    scene ae93 with dssa
    v "You always say it's too soft."
    scene ae94 with dssa
    d "Too soft for a brute like me."
    d "But I can't imagine a more perfect voice to listen to when trying to sleep."
    d "Maybe you can start reading audio books?"
    scene ae95 with dssa
    v "How would I even start?"
    d "I'll keep my eyes open."
    scene ae96 with dssa
    v "Thank you."
    scene ae97 with dssr
    v "Weird... How long Nami and Mila are taking in the kitchen."
    scene ae98 with dssa
    d "They're standing at the door eavesdropping."
    scene ae99 with vpunch
    n "How did you know?!"
    d "I know you."
    scene ae100 with vpunch
    mi "Hey [name]." #hug
    d "...I still need to get used to hugs."
    scene ae101 with dssa
    mi "That's a 'you' problem."
    scene ae102 with dssr
    mi "Do you want some coffee too?"
    scene ae103 with dssa
    d "Yeah."
    scene ae104 with dssa
    n "What up, VIC!?"
    v "What up, NAMI!?"
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Jaccuzi)
    scene ae105 with dssr
    pause
    scene ae106 with dssa
    pause
    scene ae107 with dssr
    pause
    d "What?"
    $ persistent.unlockedImageRS60 = True
    scene ae108 with dssa
    mi "You called Vic an idiot."
    d "So?"
    scene ae109 with dssa
    mi "That's good. She needs that."
    d "To be called an idiot?"
    scene ae110 with dssa
    mi "No, someone who doesn't treat her any different."
    mi "Many speak to her as if she's on her death bed."
    scene ae111 with dssr
    mi "Their voices are full of pity and it affects Vic negatively."
    scene ae112 with dssr
    d "You mentioned coffee."
    scene ae111 with dssa
    mi "Yup, lemme turn it on."
    scene ae113 with dssr
    mi "*Stretches* Ngggh..."
    scene ae114 with dssa
    pause
    scene ae115 with dssr
    d "You look fucked up."
    scene ae116 with dssa
    mi "I fucking hate working at that fucking place."
    scene ae118 with dssa
    pause
    scene ae117 with dssa
    mi "Sorry."
    scene ae119 with dssa
    d "All good."
    d "What is it that you work as?"
    scene ae120 with dssa
    mi "As a waitress."
    d "Oh yeah, that sucks."
    scene ae121 with dssa
    mi "I get payed barely enough to survive and sometimes work up to 11h."
    d "Welcome to the rat race."
    scene ae122 with dssr
    d "The tips must be nice, though."
    scene ae123 with dssa
    mi "Depends on my cleavage."
    scene ae124 with dssa
    d "No tips for you today."
    scene ae125 with dssb
    mi "Oh? I'm surprised you noticed it."
    scene ae126 with dssa
    d "I still analyze the people around me... and let's be real they're hard to overlook. And something looked off."
    if miladate is True:
        $ MilaBruise4x5 = True
        d "I also agreed to go out with you-"
        mi "No, no, no. You asked ME out... and I agreed to go out with you."
        d "True."
        scene ae127 with dssr
        mi "I'm still surprised you did."
        scene ae128 with dssa
        d "Me too."
        scene ae129 with dssa
        mi "What made you ask me out? Pity?"
        d "I just want to fuck you."
        scene ae130 with dssa
        mi "Come on! I'm trying to be serious here!"
        scene ae131 with dssa
        d "I don't know. Sometimes... Sometime-"
        scene ae132 with dssa
        mi "- Sometimes there isn't a logical explanation."
        d "Yeah, I guess."
        scene ae133 with dssa
        mi "Same reason why I said yes."
        scene ae134 with dssa
        mi "I don't really go on dates. But you're weird. Like uncomfortably weird sometimes... but that also makes you kinda interesting."
        mi "Or maybe I'm just going crazy."
        scene ae135 with dssr
        d "That's the more likely conclusion."
        scene ae136 with dssr
        "She gently straightens your collar."
        scene ae137 with dssa
        pause
        d "..."
        scene ae140 with dssa
        d "Mila."
        scene ae141 with dssr
        mi "*Whisper* Yes?"
        scene ae142 with vpunch
        d "Why do you have a bruise on your body?"
        scene ae143 with dssa
        mi "What?"
        scene ae142 with dssa
        d "I touched your hip and you flinched."
        d "Show me your hip."
        scene ae144 with dssr
        mi "[name], there's nothing."
        scene ae146 with dssr
        d "Mila."
        d "You look like a dog that pooped somewhere in the house."
        scene ae145 with dssa
        mi "*Whispers* [name]..."
        scene ae147x with dssb
        $ persistent.unlockedImageMilaCh4x511 = True
        pause
        scene ae147xx with dssr
        pause
        scene ae148 with dssr
        d "Who did this?"
        scene ae149 with dssr
        pause
        scene ae150 with dssa
        mi "...My mother."
        scene ae151 with dssa
        d "Why?"
        scene ae150 with dssa
        mi "I refused to 'lend' them money."
        mi "And alcohol makes them do stupid things... So she did what she always does... Threw something at me."
        mi "It happened to be an ash tray."
        scene ae152 with dssr
        d "A fucking ash tray?"
        scene ae153 with dssa
        pause
        scene ae154 with dssa
        mi "Please don't tell the others."
        scene ae155 with dssa
        pause
        scene ae156 with dssr
        pause
        scene ae157 with dssa
        d "I won't... This time."
        menu:
            "Kiss her":
                $ KissedGirl = True
                $ achievement.grant("KissMila")
                $ achievement.sync()
                $ MilaKiss4x5 = True
                $ persistent.unlockedImageMilaCh4x512 = True
                scene ae158 with dssa
                "You grab her head and kiss her."
                scene ae159 with dssb
                d "But if it happens again, Nami and I will take action."
            "Don't.":
                pass
                scene ae159 with dssb
                d "But if it happens again, Nami and I will take action."
        mi "...I just need to move out."
        d "We'll get that student house."
        scene black with Dissolve(2)
        with Pause(.5)
    scene ae160 with dssr
    mi "Do you have Aurora?"
    scene ae163 with dssa
    d "Aurora net?"
    scene ae160 with dssa
    mi "No no, Aurora, the social media app."
    scene ae163 with dssa
    d "No. Never heard of..."
    scene ae164 with dssa
    mi "Dude, everyone is on there."
    scene ae166 with dssr
    d "I see."
    pause
    scene ae167 with dssa
    mi "Some guy tried to tag you on an image."
    d "Mhm. So?"
    scene ae168 with dssa
    mi "Will you get the app?"
    scene ae169 with dssa
    d "No."
    scene ae170 with vpunch
    d "Wait."
    d "Scroll back."
    scene ae171 with dssa
    pause
    show ae1997x with dssr
    d "Elsa."
    mi "Do you know her?"
    scene ae1996x with dssb
    d "I used to."
    scene ae1997xx with dssr
    mi "She's a super famous model."
    d "Are you friends with her?"
    scene ae172 with dssa
    mi "No, her picture is trending, that's why she's there."
    d "I'll get the app, too."
    scene ae173 with dssa
    mi "Wow. She changed your mind fast."
    scene ae174 with dssa
    d "It's not really about her... but a social media app brings people you lost sight of together."
    scene ae175 with dssa
    mi "Is it about Summer?"
    scene ae176 with dssa
    d "Nami told you?"
    scene ae175 with dssa
    mi "Yeeeah, she kinda spilled the beans."
    scene ae176 with dssa
    d "Fucking Cheeto."
    show ae1997x with dssr
    $ persistent.unlockedImageKate3= True
    if BellaKiss3x5 is True:
        $ KissedGirl = True
        d "Who's that girl, Kate?"
        scene ae1998x with dssb
        mi "She and I were project partners in High School. She's a friend of mine."
        mi "Bella and Kate are on really bad terms, though."
        d "I heard she bullied Bella."
        mi "That's one side of the coin... Listen to both sides."
    else:
        scene ae1998x with dssb
        mi "I think you've seen Kate before?"
        d "Saw her..."
        mi "She and I were project partners in High School. She's a friend of mine."
        mi "Bella and Kate are on really bad terms, though."
    pause
    if miladate or miladateF is True:
        scene ae175 with dssa
        mi "[name]?"
        scene ae177 with dssa
        mi "Which one should I post?"
        scene ae1485x with dssb
        mi "This?"
        scene ae1486x with dssb
        mi "Or this one?"
        scene ae177 with dssr
        with Pause(.3)
        call screen MilaChoice4x5
        $ renpy.pause(20, hard=True)
        pause
    else:
        jump MilaContinue4x5

label MilaAu1:
    hide screen MilaChoice4x5
    $ MilaOrderly4x5 = True
    scene ae1485x with dssb
    pause
    jump MilaContinue4x5

label MilaAu2:
    $ persistent.unlockedImageMilaCh4x523 = True
    hide screen MilaChoice4x5
    $ MilaDaring4x5 = True
    scene ae1486x with dssb
    pause
    jump MilaContinue4x5

label MilaAu3:
    hide screen MilaChoice4x5
    if BellaKiss3x5 is True:
        $ MilaDaring4x5 = True
        scene ae1486x with dssb
    else:
        $ MilaOrderly4x5 = True
        scene ae1485x with dssb

    mi "Done."
    jump MilaContinue4x5

label MilaContinue4x5:
    hide screen MilaChoice4x5
    scene ae178 with dssb
    pause
    scene ae179 with dssa
    d "I noticed you're following a lot of golf stuff."
    scene ae180 with dssa
    mi "Yeah. It's mhhh- more or less the only sport I really like."
    menu:
        "Joke.":
            scene ae181 with dssa
            d "Brave of you to call it a sport."
            scene ae180 with vpunch
            mi "It's a sport!"
        "Serious.":
            scene ae182 with dssa
            d "Interesting."
    scene ae183 with dssa
    d "Does the college offer it?"
    scene ae184 with dssa
    mi "No."
    mi "The only place where you can seriously start is at the local golf club."
    mi "They also offer tennis, lacrosse and other activities."
    scene ae185 with dssa
    d "I think Noji wanted to go there with Nami and me."
    d "Is Bella there too?"
    scene ae186 with dssa
    mi "Yeah. Her mother is a Diamond member."
    mi "I will never be able to afford it."
    scene ae187 with dssa
    d "(The fact that she knows that Amber is a Diamond member is oddly specific.)"
    d "Can I get you in?"
    scene ae186 with dssa
    mi "Even if you could... it's not like you can bring me there multiple times a week."
    d "What does it cost?"
    mi "$850 a month for a silver member. Then you get access to the golf course."
    scene ae183 with dssr
    d "I see."
    d "That means that we can't afford it either."
    scene ae184 with dssr
    mi "Bella's mother has some pull. She knows Sasha's mother, who owns the club."
    d "Sasha is rich?"
    mi "Dude? One look at her should tell you that she's from a loaded family. She gets driven to the school in a limousine. And I think she isn't allowed outside without a bodyguard."
    d "I didn't know that."
    scene ae188 with dssr
    mi "Her name is Sasha Petrova. You knew that right? And that they own part of the college?"
    d "So that is what the P in ZPR stands for?"
    mi "Yup. Zane, Petrova, Revera."
    d "And Amber has some pull because?"
    scene ae189 with dssa
    mi "She went to college with Sasha's mother."
    mi "Ayua is a Zane."
    scene ae190 with dssa
    d "And who is a Revera?"
    scene ae189 with dssa
    mi "I think there's someone in the first team but... yeah, I don't know."
    mi "It's a weird clan of these three families."
    scene ae191 with dssr
    pause
    scene ae192 with dssb
    pause
    scene ae193 with dssr
    d "So how good are you at golf?"
    scene ae194 with dssr
    mi "Well, I actually hated golf... for a while."
    mi "Back as a child I only had a TV with three channels and one was always showing golf."
    scene ae195 with dssa
    mi "I was forced to watch it and dude... I hated it."
    mi "But curiosity made me want to try it."
    mi "I searched for a good stick in the woods and started shooting stones through the forest."
    scene ae196 with dssa
    d "That's cute."
    scene ae197 with dssa
    mi "*Chuckles* Well, it was all I had."
    mi "I have a pair of golf clubs now but yeah, no golf course to play on."
    scene ae196 with dssa
    d "I'll see what I can do."
    scene ae198 with dssa
    mi "No [name], it's alright."
    scene ae199 with dssa
    d "Fuck off."
    scene ae200 with dssr
    mi "Wow. That was rude."
    scene ae201 with dssa
    d "And I'll continue to be rude until you stop that crap."
    scene ae202 with dssr
    pause
    if miladate is True:
        scene ae204 with dssr
        pass
    else:
        scene ae203 with dssr
        pass
    d "...You don't always have to get things on your own... It's no sign of weakness to accept help."
    mi "Weird hearing that from you..."
    if miladate is True:
        scene ae205 with dssa
        d "We're all hypocrites."
        scene ae206 with dssa
        pause
        scene ae207 with dssa
        mi "*Breathy* I guess."
        scene ae208 with dssr
        d "Let's see what the others are up to."
    else:
        d "We're all hypocrites."
        scene ae209 with dssr
        d "Let's see what the others are up to."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch4x5)
    scene ae210 with dssb
    d "Yo."
    scene ae212 with dssr
    d "Mila wants to play golf."
    scene ae213 with dssa
    n "What? Really? Golf?"
    mi "Well-"
    scene ae212 with dssa
    d "The only place that offers it, is the country club we're going to visit."
    scene ae215 with dssr
    n "Cool. Come with us!"
    scene ae214 with dssa
    mi "No! I can't afford it."
    d "I'll talk to Amber."
    scene ae216 with vpunch
    mi "No! I don't want Bella's help!"
    d "Amber is not Bella."
    scene ae217 with dssa
    mi "No please... It's alright."
    scene ae219 with dssa
    v "I'll make you go."
    scene ae218 with dssa
    mi "Oh, how are you going to do that?"
    scene ae220 with vpunch
    v "Nami! Help me up! I need to slap some butt!"
    scene ae221 with dssa
    mi "Mhh... We'll see..."
    scene ae222 with dssr
    n "Yo, that reminds me..."
    n "Remember that book club Noji likes to go to?"
    scene ae223 with dssa
    d "Yeah."
    scene ae224 with dssa
    n "Soo... I offered to go with her."
    scene ae223 with dssa
    d "Why?!"
    scene ae225 with dssa
    n "We talked about this! That we'd include her more!"
    scene ae226 with dssa
    n "Anyways! She said something weird."
    scene ae227 with dssa
    pause
    scene ae228 with dssa
    n "She uh... told me not to ask you to come."
    scene ae229 with dssa
    d "Why would she do that?"
    scene ae230 with dssa
    n "No idea."
    n "She was really clear about it. 'Don't ask [name] to come with us.''"
    d "I'm in, bitch."
    scene ae231 with vpunch
    n "Nice!"
    scene ae233 with dssa
    d "She's gonna hate you for that."
    scene ae232 with dssa
    n "Dude, I really don't want to sit in that boring ass book club alone."
    n "I need you there!"
    n "Noji also gave me the book they're currently discussing."
    scene ae233 with dssa
    d "What is it?"
    scene ae232 with dssa
    n "It's a story about a Panda that got lost and befriended a butterfly."
    scene ae234 with dssa
    d "You're kidding me?"
    scene ae235 with dssa
    v "Sounds cute!"
    scene ae234 with dssa
    d "No wonder Noji's on her death bed."
    scene ae236 with vpunch
    n "DUDE! Don't joke about that!"
    scene ae237 with dssa
    d "You read it and then give me the important points."
    scene ae238 with dssr
    n "No way."
    n "We'll do 50/50."
    n "I read the first half for you, you the second half for me."
    scene ae239 with dssr
    d "Alright."
    scene ae240 with dssa
    mi "I know the book."
    n "You do?"
    scene ae241 with dssa
    mi "A little Panda named Tao Tao... As a child, I read the same stuff over and over again."
    n "You should come with us."
    scene ae242 with dssa
    mi "No thanks, haha."
    mi "A book club... No."
    scene ae238 with dssr
    n "Don't you ditch me!"
    d "We'll see."
    jump EveningPart2

label EveningPart2:
    scene ae243 with dssr
    v "Okay! Sooooo... Do we want to order Pizza?"
    n "Could we wait a little? We ate so much at Nick's."
    scene ae244 with dssr
    v "Sure!"
    v "But we can start drinking, right?"
    scene ae246 with vpunch
    n "Damn straight we can!"
    scene ae248 with dssr
    mi "We can start with some beer... and then later-"
    scene ae247 with vpunch
    v "-We drink this!"
    v "I got it from Maja."
    n "She got you that?"
    scene ae244 with dssr
    v "Yeah, after I told her [name] was going to come by... she told me he was going to need it to remove that... well, plank out of his butt."
    scene ae245 with dssa
    n "Maja is a smart woman!"
    scene ae249 with dssr
    d "Movie?"
    v "Sure!"
    v "What do we want to start with?"
    scene ae250 with dssr
    v "We have a very scary movie..."
    scene ae251 with dssa
    v "And a funny one."
    scene ae252 with dssa
    n "I'm for the scary one!"
    scene ae251 with dssa
    v "The funny one has lots of nudity, I think."
    scene ae253 with dssa
    n "Okay! The funny one!"
    scene ae254 with dssa
    mi "I'm for the scary one."
    v "[name]?"
    scene ae255 with dssa
    d "Let's watch the scary one."
    $ ScaryMovie4x5 = True
    if vicdate is True:
        jump SmVic4x5
    elif miladate is True:
        jump SmMila4x5
    else:
        jump SMovie4x5




label SmVic4x5:
    $ VicMovie4x5 = True
    scene ae256 with dssr
    "You feel Victoria slipping closer to you."
    menu:
        "Pull her onto your lap.":
            $ SVic4x5 = True
            scene ae257 with dssr
        "Don't do it.":
            jump SMovie4x5
    pause
    scene ae258 with dssr
    v "Oh no, black people always die first! Poor boy."
    scene ae259 with dssr
    mi "I have an idea."
    scene ae261 with dssa
    n "Every time someone dies we drink?"
    scene ae260 with dssa
    mi "Yes!"
    scene ae262 with dssa
    v "Let's start with these!"
    scene ae263 with dssa
    v "Can you hold the little glasses?"
    scene ae264 with dssa
    d "Yeah."
    scene ae265 with dssa
    pause
    scene ae266 with dssa
    d "Mila."
    scene ae267 with dssa
    mi "Thanks."
    scene ae268 with dssr
    d "Cheeto."
    scene ae269 with dssa
    n "Yo Vic?"
    v "Mhhh?"
    n "Weird question but... your boobs are real, right?"
    v "Uhh? What do you mean?"
    scene ae275 with dssa
    mi "She means if you've got fake boobs. Like silicone in there."
    v "Oh, no, no, Nami. They're real."
    scene ae276 with dssa
    mi "I know what you mean, Nami."
    mi "She has won the lottery of connective tissue."
    scene ae270 with dssr
    n "You're wearing no bra and they stay this perky... I'm so jealous."
    scene ae271 with dssa
    v "Don't be, Nami! I'm sure yours are amazing, too!"
    scene ae272 with dssa
    d "Cheeto take the damn drink."
    scene ae273 with dssa
    pause
    scene ae274 with dssa
    n "I'll need another one."
    scene ae277 with dssa
    d "Here Vic."
    scene ae278 with dssa
    "You slowly move the shot to her mouth."
    scene ae279 with dssa
    mi "Why are you guys drinking? Nobody died."
    d "Right..."
    scene ae280 with dssr
    d "Here Vic."
    scene ae281 with dssa
    d "Everyone served?"
    scene ae282 with dssr
    n "Mhhh... I wanted to be a movie star when I was little."
    scene ae286 with dssr
    mi "I once got invited to an audition."
    n "Really?!"
    scene ae287 with dssa
    mi "...Yeah, I left after I saw a black couch."
    scene ae288 with dssa
    n "Oh... HAHAHAHA!"
    scene ae289 with dssr
    v "I don't get it."
    d "Me neither."
    scene ae283 with dssa
    n "Okay... The black couch is pretty much a trademark of casting porn."
    scene ae290 with dssr
    v "Oh? They wanted you in a porno?"
    mi "Yup."
    v "Haha!"
    scene ae284 with dssr
    d "Can we watch the movie?"
    scene ae285 with dssa
    n "Sure poophead."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae291 with dssr
    pause
    scene ae292 with dssr
    n "See that's a dumb decision."
    scene ae293 with dssr
    mi "So dumb."
    scene ae294 with vpunch
    pause
    d "You're scared?"
    scene ae295 with dssr
    v "I thought there was a monster coming."
    scene ae296 with dssa
    n "The monster never appears this early."
    scene ae297 with dssa
    mi "Yeah, it's always a build u-"
    scene ae298 with vpunch
    v "AHHHH!"
    scene ae299 with dssa
    n "...I regret everything."
    mi "It looks so scary!"
    scene ae300 with dssa
    pause
    scene ae301 with dssr
    pause
    d "You've got popcorn in your cleavage."
    scene ae302 with dssa
    v "Do you want it?"
    $ persistent.unlockedImageVicCh4x60 = True
    menu:
        "Take the boob-corn.":
            $ VicBoobCorn4x5 = True
            scene ae303 with dssa
            pause
            scene ae304 with dssr
            d "*Whispers* Damn it... Now it's deeper in."
            v "*Whispers* I'm sure you can still reach it."
            scene ae305 with dssa
            "You push your hand between Victoria's full and soft boobs."
            scene ae306 with dssa
            d "Got it."
            "Vic chuckles."
        "Decline and pick a new one.":
            d "I'll pick a new one."
            v "Okay."
    scene ae307 with dssr
    v "Oh no, it's gonna hurt the little doggo?"
    scene ae308 with dssa
    n "I- Na see! Even monsters wouldn't hurt a good doggo!"
    scene ae314 with dssr
    mi "If he had killed the doggo, we'd have to drink five shots."
    scene ae309 with vpunch
    v "Nhh!"
    scene ae310 with dssa
    n "*Laughs* Nothing's happening."
    scene ae309 with dssa
    v "Better safe than sorry!"
    scene ae310 with dssa
    n "That also applies to condoms."
    scene ae315 with dssr
    mi "Remember that, [name]."
    scene ae311 with dssr
    n "I don't think you're on birth control, are ya Vic?"
    scene ae312 with dssa
    v "No, I'm not. I- I uh didn't think it'd be necessary today."
    scene ae313 with dssa
    d "Wait what? No what the- Vic, don't listen to these idiots."
    scene ae312 with dssa
    v "Good, I wasn't prepared!"
    scene ae315 with dssr
    mi "Are you on birth control, Nami?"
    n "Not yet, but I plan on getting it soon."
    scene ae316 with dssa
    mi "I'm on the pill, it helps to control your menstrual cycle."
    scene ae319 with dssr
    n "How does sex feel with and without a condom?"
    scene ae317 with dssr
    mi "No idea. I never had it without one."
    scene ae320 with dssr
    n "Hmm."
    n "I wonder if a dildo would be enough-"
    scene ae318 with dssr
    mi "No girl. There's a huge difference between a dildo and an actual penis."
    scene ae320 with dssr
    n "I really need one of those life-like dildos."
    scene ae321 with dssa
    v "Maja has one."
    scene ae322 with dssr
    stop music fadeout 3.0
    n "How do you know that?"
    scene ae321 with dssr
    $ play_playlist(playlist_GirlyCh4x)
    v "She has an entire box full of them."
    scene ae323 with dssa
    pause
    scene ae324 with dssr
    pause
    jump MajaToys4x5



label MajaToys4x5:
    scene ae325 with vpunch
    n "Stop the movie!"
    d "No! Nami!"
    scene ae326 with dssa
    "Mila giggles and follows Nami."
    d "That's super rude!"
    scene ae327 with dssa
    v "Where're they going?"
    scene ae328 with dssa
    d "They're looking for Maja's box."
    scene ae327 with dssa
    v "Oh."
    v "Can you carry me over there?"
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae386 with dssr
    pause
    scene ae387 with dssa
    d "Cheeto! Show some respect you fucker!"
    scene ae388 with dssa
    n "Vic, where's the box?"
    scene ae389 with vpunch
    n "WHAT'S IN THE BOX?!"
    scene ae390 with dssr
    v "It should be over there."
    scene ae391 with vpunch
    d "Mila!"
    scene ae392 with dssa
    mi "Sorry, I'm one of the bad girls."
    scene ae393 with dssa
    n "Mila! Look in there."
    n "Lots of stockings."
    scene ae394 with vpunch
    d "You fucking apes, don't be so rude!"
    scene ae395 with dssr
    pause
    scene ae396 with dssr
    v "Girls..."
    v "I wanna see it, too!"
    scene ae397 with dssr
    d "I can't believe that I am the sane one here..."
    scene ae398 with dssa
    mi "Found it!"
    scene ae399 with dssr
    n "The holy box of shame?!"
    mi "I wouldn't call it holy."
    scene ae400 with dssr
    d "Nami! Don't touch her fucking sex toys! That's really disrespectful."
    n "OH my god."
    scene ae401 with dssa
    mi "Wow. Look at this one."
    scene ae402 with dssa
    pause
    scene ae403 with dssa
    n "I like this one."
    $ persistent.unlockedImageMilaCh4x513 = True
    mi "It would kill your kitty."
    scene ae404 with dssa
    mi "This one is cute."
    scene ae405 with dssr
    v "I want to see them, too!"
    scene ae406 with dssa
    n "Here, look at this one."
    scene ae407 with dssa
    v "Uuh- it looks fancy."
    v "Look [name]-"
    scene ae408 with dssa
    "Vic accidentally rubs it against your cheek."
    scene ae409 with dssa
    d "Don't- touch me with that."
    v "Sorry."
    n "They are all clean, [name]."
    scene ae410 with dssa
    v "It's long... does it all fit into a vagina?"
    mi "Oh no. That's an anal toy. You put it in your butt."
    v "Oh! Doesn't it hurt?"
    scene ae411 with dssr
    mi "You start with them here-"
    v "Oh! So cute."
    scene ae412 with dssa
    mi "And you just go bigger and bigger until you've reached your desired size."
    scene ae413 with dssr
    n "What's this?"
    mi "I- think uuuh, you can put it on your nipple."
    scene ae414 with dssa
    n "A nipple pump?"
    mi "Yes."
    v "It looks cute. What does it do to your nipple?"
    scene ae416 with dssr
    mi "It makes it bigger. Maybe it gets a little more sensitive, too."
    scene ae415 with dssr
    n "[name]? Please say yes."
    d "I will not let you put that thing on my nipple."
    scene ae417 with vpunch
    mi "Oh god! Please do it! Please, please, pleaseeeee!"
    scene ae418 with dssr
    v "Yes! Do it!"
    menu:
        "Let them put it on your nipple.":
            $ persistent.unlockedImageNamiCh4x544 = True
            $ MCNipplePump = True
            $ persistent.unlockedImageVicCh4x61 = True
            d "Alright..."
            scene ae419 with dssa
            n "Wait- really?"
            d "Yes."
            n "Dude! I never expected you to say yes!"
            scene ae420 with dssa
            mi "*Laughs* Take off your shirt."
            scene ae421 with dssa
            d "Vic- I-"
            scene ae422 with dssa
            v "Let's take his shirt off."
            scene ae423 with dssr
            "The three girls surround you."
            scene ae424 with dssr
            pause
            scene ae425 with dssa
            mi "Guys have small nipples, I don't expect there to be a big effect."
            scene ae426 with dssa
            n "Ready?"
            d "Just do it."
            scene ae427 with dssa
            pause
            scene ae426 with dssa
            pause
            scene ae427 with dssa
            mi "Do you feel something?"
            scene ae426 with dssa
            d "A sucking motion."
            scene ae428 with dssa
            v "Do it harder."
            scene ae426 with dssa
            d "It feels weird."
            scene ae428 with dssa
            mi "Do it a couple more times."
            scene ae429 with dssa
            n "It sticks."
            mi "Pull it off."
            scene ae430 with vpunch #sfx plop
            v "Look! It got a little bigger."
            scene ae431 with dssa
            mi "I think it got quite a lot bigger- you should use it on someone with bigger nipples."
            scene ae456 with dssr
            n "Mila, maybe yours?"
            scene ae453 with dssr
            mi "Yeah, I will not flash my tits."
            n "It's just us... and [name]."
            mi "I'll pass."
        "No.":
            n "Pfff... Party pooper."
    scene ae452 with dssr
    d "Can I have a shot?"
    scene ae453 with dssa
    mi "Drink from the bottle."
    if MCNipplePump is True:
        scene ae454 with dssr
    else:
        scene ae455 with dssr
    pause #mila hält dir die flasche
    scene ae457 with dssr
    mi "Good boy."
    scene ae456 with dssr
    n "Vic, where was the shop she got these at?"
    v "Uhhhh, I don't know the street, but I can get you there."
    mi "I'll come with you guys."
    scene ae458 with dssr
    n "What collection do you have at home?"
    scene ae462 with dssa
    mi "I don't have a single toy."
    mi "I would like some, but my parents don't value privacy."
    scene ae461 with dssa
    v "I don't have one either."
    scene ae459 with dssr
    n "Here. It's yours."
    scene ae460 with dssa
    v "It's Maja's!"
    scene ae459 with dssa
    n "She has like four of them."
    scene ae460 with dssa
    v "Noo! I want to get my own."
    n "Alright, we will go the shop together then."
    scene ae441 with dssb
    v "You too, [name]."
    d "Sure."
    scene ae459 with dssr
    n "Waaaait, why would you say yes to that?"
    scene ae460 with dssa
    d "Get some leverage on you."
    d "Make some hints during breakfast to Noji."
    scene ae458 with dssb
    n "You're evil!"
    n "I'll buy you a toy too!"
    scene ae452 with dssr
    d "Alright, can we put Maja's stuff back and go back to the movie?"
    scene ae463 with dssa
    mi "First, you take another sip."
    d "I already had one, it's your turn."
    scene ae464 with dssa
    mi "Oh! I'm not the party pooper here. You need it more than we do."
    scene ae465 with dssa
    "You take another sip."
    scene ae463 with dssa
    d "- It tastes worse with every sip."
    scene ae466 with dssb
    n "The holy box has been returned... Let's get out of here."
    scene ae467 with dssb
    mi "Make sure it's exactly how we found it."
    scene ae468 with dssb
    pause
    scene ae469 with dssb
    pause
    stop music fadeout 2.0
    scene black with Dissolve(2)
    if VicMovie4x5 is True:
        jump SmVic4x5P2
    elif MilaMovie4x5 is True:
        jump SmMila4x5pt2
    else:
        jump Crossroad4x5


label SmVic4x5P2:
    $ play_playlist(playlist_Ch4x52)
    $ VicProtect4x5 = True
    scene ae470 with dssb
    pause
    scene ae471 with dssb
    "Victoria takes your hand and caresses it slightly."
    scene ae472 with dssa
    mi "Oh no! Creepy scene!"
    scene ae473 with dssa
    "She grabs your hand and holds it against her chest."
    scene ae474 with dssb
    d "(I'm not aroused but I can't deny that her breasts, or breasts in general, feel amazing.)"
    d "(I think there's some primitive force in straight males that makes breasts just feel... awesome.)"
    "You resist the underlying urge to remove your hand from her breast and just let it rest there."
    scene ae475 with dssa
    "As the movie intensifies, Victoria increases the pressure on your hand."
    d "(If she wasn't wearing a top, I'd have her entire breast in my hand...)"
    scene ae476 with dssb
    d "(...And me not minding it... Hell, me kind of wanting it confuses me.)"
    scene ae477 with dssa
    pause
    if BellaKiss3x5 is True:
        d "(I wonder what Bella's would feel like.)"
    scene ae474 with dssb
    "The movie calms down and Vic lowers the pressure but fixates your hand on her chest."
    scene ae478 with dssb
    pause
    d "(I can feel her nipple... She must be aroused.)"
    scene ae479 with dssa
    d "(I'm glad we aren't alone here... I don't know if I'm ready for what would come next... To see the disappointment in her eyes.)"
    if BellaKiss3x5 is False:
        d "(I feel guilty just by touching her... I'm so stupid.)"
    else:
        d "(I feel somewhat guilty for touching her...)"
    scene ae480 with dssb
    d "Yo, Cheeto, let's all drink a shot."
    scene ae481 with dssa
    n "Nobody died?"
    scene ae482 with dssb
    mi "[name] proposing a shot? You don't question that Nami! Drink!"
    scene ae483 with dssb
    pause
    scene ae489 with dssb
    "*Splatter sounds*"
    scene ae487 with dssa
    n "Is he dead?"
    d "Yeah."
    scene ae490 with vpunch
    v "More!"
    scene ae484 with dssb
    pause
    scene ae488 with dssb
    n "And this guy's dead, too."
    scene ae486 with dssr
    n "Oh boy."
    scene ae485 with dssr
    pause
    scene ae492 with dssr
    "*Screams*"
    scene ae491 with dssr
    d "Are you serious?"
    scene ae493 with dssa
    mi "They both died... Does this mean-"
    scene ae487 with dssb
    n "Yes... Two shots."
    scene ae491 with dssb
    d "Okay seriously... If we down these two... this evening might take a bad turn."
    scene ae493 with dssr
    mi "I don't want to vomit."
    scene ae490 with dssb
    v "I say we take them!"
    scene ae494 with dssr
    d "You're a bad influence."
    scene ae495 with vpunch
    v "*Tough* I am!"
    scene ae496 with dssa
    mi "It sounds really cute when you're trying to sound tough in your soft voice."
    scene ae497 with dssa
    v "My damn voice..."
    scene ae500 with dssa
    n "I bet you could make some money reading audio books."
    scene ae501 with dssa
    d "That's what I said."
    scene ae498 with dssb
    pause
    scene ae499 with dssa
    v "I feel it."
    scene ae502 with dssb
    mi "*Chuckles* Me too."
    d "I can see that."
    scene ae503 with dssa
    mi "I feel good now... But any more and I will feel reaaaally bad."
    scene ae504 with dssa
    d "I'll get us some water."
    scene ae505 with vpunch
    v "No... Stay! It's cozy."
    scene ae506 with dssb
    d "(These two seem... very touchy...)"
    d "(I should get up if I want to avoid an awkward turn of the evening.)"
    jump Crossroad4x5


label SmMila4x5:
    $ MilaMovie4x5 = True
    scene ae329 with dssr
    "Mila sits closer beside you."
    pause
    menu:
        "Put your arm around her.":
            $ MilaScaryMovieCuddle4x5 = True
            scene ae330 with dssr
            pause
        "Keep your distance.":
            jump SMovie4x5
    scene ae331 with dssr
    mi "*Whisper* Every time I watch a horror movie I can't stop thinking about it for a couple of days."
    scene ae332 with dssa
    d "Nami's the same."
    scene ae547 with dssb
    v "Oh no, black people always die first! Poor boy."
    scene ae333 with dssb
    mi "I have an idea."
    scene ae334 with dssr
    n "Every time someone dies we drink?"
    mi "Yes!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae335 with dssr
    v "Let's start with these!"
    scene ae336 with dssr
    v "Here! One for everyone!"
    scene ae337 with dssr
    pause
    scene ae338 with dssr
    n "Yo Vic?"
    v "Mhhh?"
    scene ae339 with dssa
    n "Weird question but... your boobs are real, right?"
    v "What do you mean?"
    scene ae343 with dssa
    mi "She means if you've got fake boobs. Like silicone in there."
    scene ae342 with dssr
    v "Oh, no no, Nami. They're real."
    scene ae343 with dssa
    mi "I know what you're getting at, Nami."
    mi "She has won the lottery of connective tissue."
    scene ae339 with dssr
    n "You're wearing no bra and they stay this perky... I'm so jealous."
    scene ae341 with dssa
    v "Don't be, Nami! I'm sure yours are amazing, too!"
    n "Mine are also not saggy but the size difference makes it so unbelievable."
    scene ae344 with dssa
    pause
    scene ae345 with dssa
    n "I'll need another one..."
    scene ae346 with dssr
    pause
    scene ae347 with dssr
    mi "Don't worry too much about tits."
    scene ae348 with dssa
    n "Coming from you... that's like a billionaire saying 'Don't worry too much about money'."
    scene ae349 with dssa
    mi "...Yeah, sorry."
    scene ae354 with vpunch
    v "All tiddies are great tiddies!"
    scene ae350 with dssr
    mi "I don't like her but..."
    mi "Besides Vic's godlike tiddies... Bella's are also pretty nice."
    scene ae355 with dssr
    n "What?"
    scene ae350 with dssa
    mi "She has relatively big tits but not too big... They also got a nice form."
    n "Who are you and what did you do to Bella-Hating Mila?!"
    scene ae351 with dssa
    mi "I still dislike her... But I can be objective."
    if BellaKiss3x5 is True:
        scene ae352 with dssa
        n "Have you seen her... jugs?"
        scene ae353 with dssa
        if bellagym is True:
            d "Yeah."
            n "When?"
            d "She stormed into my shower at the gym."
            scene ae356 with dssr
            n "..."
        else:
            d "It was pretty dark and I didn't really look at them."
            n "Who wouldn't take a look at boobs?!"
            d "I was busy touching them... and tucking them back in."
            scene ae356 with dssr
            n "..."
    scene ae357 with dssr
    v "Why does everyone always talk about boobs and butts but not about vaginas?"
    scene ae359 with dssr
    mi "*Chuckles* I think vaginas are more intimate than boobs."
    scene ae360 with dssa
    pause
    scene ae361 with dssa
    n "[name]..."
    n "You haven't complained yet."
    scene ae360 with dssa
    mi "Weird..."
    scene ae362 with dssr
    d "One way out of my comfort zone is listening to... this."
    n "Okay, okay..."
    if milagym is True:
        scene ae363 with dssa
        n "Boobs or ass?"
        scene ae360 with dssr
        if MMCBB03 is True:
            mi "He likes boobs."
        elif MMCPB03 is True:
            mi "He likes butts."
        elif MFAnal is True:
            mi "You didn't have a preference, right?"
        scene ae364 with dssr
        n "How do you know?"
        mi "I asked him."
        scene ae368 with dssr
        d "I totally forgot your pants incident."
        scene ae369 with vpunch
        mi "Hey no! PSSH!"
        scene ae358 with dssr
        v "What incident?"
        d "Her pants ripped while we were at the gym."
        scene ae561 with dssb
        mi "...So embarrassing."
        scene ae365 with dssr
        n "If I didn't know you, I would hate you."
        mi "That's a compliment!"
        scene ae366 with dssa
        n "How can you have big tits and a big ass while not being fat!?"
        n "What do I have?!"
        mi "You've got a nice big ass!"
        scene ae363 with dssa
        n "Thank you!"
        scene ae362 with dssr
        d "Stop fishing for compliments... It's embarrassing."
        scene ae564 with dssa
        n "Y-you are embarrassing!"
        d "That's well known."
    else:
        scene ae370 with dssr
        mi "[name]... Boobs or ass?"
        scene ae371 with dssa
        d "What I like more?"
        scene ae370 with dssa
        mi "Yeah."
        scene ae371 with dssa
        d "What if I like a penis?"
        scene ae372 with dssa
        mi "That would explain a lot."
        scene ae373 with dssa
        menu:
            "I like the look of a well formed butt.":
                pause
            "I like the look of some well formed breasts.":
                pause
            "I don't have a preference. I like them both.":
                pause
    scene ae374 with dssa
    d "Let's watch the movie..."
    n "Poophead."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae375 with dssb
    v "Oh no, it's gonna hurt the little doggo?"
    scene ae376 with dssa
    n "I- Na see! Even monsters wouldn't hurt a good doggo!"
    mi "If he had killed the doggo, we'd have to drink five shots."
    scene ae377 with dssa
    pause
    scene ae378 with vpunch
    v "Nhh!"
    n "Nothing's happening, haha."
    v "Better safe than sorry!"
    scene ae379 with dssa
    n "That also applies to condoms."
    scene ae381 with dssa
    mi "Are you on birth control, Nami?"
    scene ae380 with dssa
    n "Not yet but I plan on getting it soon."
    mi "I'm on the pill, it helps to control your menstrual cycle."
    n "How does sex feel with and without a condom?"
    mi "No idea. I never had it without one."
    scene ae382 with dssa
    n "Hmm."
    n "I wonder if a dildo would be enough-"
    scene ae383 with dssa
    mi "No girl. There's a huge difference between a dildo and an actual penis."
    scene ae384 with dssa
    n "I really need one of those life-like dildos."
    scene ae385 with dssa
    v "Maja has one."
    stop music fadeout 3.0
    n "How do you know that?"
    $ play_playlist(playlist_GirlyCh4x)
    v "She has an entire box full of them."
    scene ae323 with dssa
    pause
    scene ae324 with dssr
    pause
    jump MajaToys4x5

label SmMila4x5pt2:
    $ play_playlist(playlist_Ch4x52)
    scene ae1987x with dssb
    pause
    scene ae1988x with dssr
    pause
    scene ae1989x with dssr
    pause
    scene ae1990x with dssr
    "Mila moves her hand onto your thighs."
    scene ae1991x with dssr
    "As you try to focus on the movie, you feel her fingers gently circulating on the fabric of your pants."
    scene ae1992x with dssr
    pause
    scene ae1993x with dssr
    "You move your hand farther."
    d "(I think there is something primal in straight males that makes long legs just look so... alluring.)"
    "You resist the underlying urge to remove your hand from her leg and just let it rest there."
    scene ae1994x with dssr
    pause
    scene ae1995x with dssr
    "She moves your hand up to her inner thighs."
    d "(I'm confused that I don't mind it... Hell, I would even say want it.)"
    if BellaKiss3x5 is True:
        d "(I wonder how Bella's inner thighs would feel.)"
    else:
        d "(I feel guilty just by touching her... I'm so stupid.)"
    scene ae480 with dssb
    d "Yo, Cheeto, let's all drink a shot."
    scene ae481 with dssa
    n "Nobody died?"
    scene ae482 with dssb
    mi "[name] proposing a shot? You don't question that, Nami! Drink!"
    scene ae483 with dssb
    pause
    scene ae489 with dssb
    "*Splatter sounds*"
    scene ae487 with dssa
    n "Is he dead?"
    d "Yeah."
    scene ae490 with vpunch
    v "More!"
    scene ae484 with dssb
    pause
    scene ae488 with dssb
    n "And this guy's dead, too."
    scene ae486 with dssr
    n "Oh boy."
    scene ae485 with dssr
    pause
    scene ae492 with dssr
    "*Screams*"
    scene ae491 with dssr
    d "Are you serious?"
    scene ae493 with dssa
    mi "They both died... Does this mean-"
    scene ae487 with dssb
    n "Yes... Two shots."
    scene ae491 with dssb
    d "Okay seriously... If we down these two... this evening might take a bad turn."
    scene ae493 with dssr
    mi "I don't want to vomit."
    scene ae490 with dssb
    v "I say we take them!"
    scene ae494 with dssr
    d "You're a bad influence."
    scene ae495 with vpunch
    v "*Tough* I am!"
    scene ae496 with dssa
    mi "It's sounds really cute when you're trying to sound tough in your soft voice."
    scene ae497 with dssa
    v "My damn voice..."
    scene ae500 with dssa
    n "I bet you could make some money reading audio books."
    scene ae501 with dssa
    d "That's what I said."
    scene ae498 with dssb
    pause
    scene ae499 with dssa
    v "I feel it."
    scene ae502 with dssb
    mi "*Chuckles* Me too."
    d "I can see that."
    scene ae503 with dssa
    mi "I feel good now... But any more and I will feel reaaaally bad."
    scene ae504 with dssa
    d "I'll get us some water."
    scene ae505 with vpunch
    v "No... Stay! It's cozy."
    scene ae506 with dssb
    d "(These two seem... very touchy...)"
    d "(I should get up if I want to avoid an awkward turn of the evening.)"
    jump Crossroad4x5


label SMovie4x5:
    $ SoloMovie4x5 = True
    pause
    scene ae545 with dssb
    mi "*Whisper* Every time I watch a horror movie I can't stop thinking about it for a couple of days."
    scene ae546 with dssa
    d "Nami's the same."
    scene ae547 with dssb
    v "Oh no, black people always die first! Poor boy."
    scene ae548 with dssb
    mi "I have an idea."
    scene ae549 with dssa
    n "Every time someone dies we drink?"
    scene ae550 with dssa
    mi "Yes!"
    scene ae335 with dssb
    v "Let's start with these!"
    scene ae336 with dssa
    v "Here [name]."
    scene ae338 with dssa
    n "Yo Vic?"
    v "Mhhh?"
    scene ae339 with dssa
    n "Weird question but... your boobs are real, right?"
    scene ae342 with dssa
    v "What do you mean?"
    scene ae343 with dssb
    mi "She means if you got fake boobs. Like silicone in there."
    scene ae341 with dssb
    v "Oh, no no, Nami. They're real."
    scene ae343 with dssb
    mi "I know what you're getting at, Nami."
    mi "She has won the lottery of connective tissue."
    scene ae339 with dssb
    n "You're wearing no bra and they stay this perky... I'm so jealous."
    scene ae341 with dssa
    v "Don't be Nami! I'm sure yours are amazing, too!"
    scene ae339 with dssa
    n "Mine are also not saggy but the size difference makes it so unbelievable."
    scene ae344 with dssa
    pause
    scene ae345 with dssa
    n "I'll need another one."
    scene ae360 with dssb
    mi "Don't worry too much about tits."
    scene ae361 with dssa
    n "Coming from you... that's like a billionaire saying 'Don't worry too much about money'."
    scene ae359 with dssa
    mi "...Sorry."
    scene ae354 with vpunch
    v "All tiddies are great tiddies!"
    scene ae551 with dssb
    mi "I don't like her but..."
    mi "Besides Vic's godlike tiddies... Bella's are also pretty nice."
    scene ae552 with dssa
    n "What?"
    scene ae553 with dssa
    mi "I'm just being objective."
    mi "She has relatively big tits but not too big... They also got a nice form."
    scene ae554 with dssr
    n "Who are you and what did you do to Bella-Hating Mila?!"
    scene ae553 with dssr
    mi "I'm still not positive about her... But I can be objective."
    if BellaKiss3x5 is True:
        scene ae352 with dssb
        n "Have you seen her... jugs?"
        scene ae353 with dssa
        d "It was pretty dark and I didn't really look at them."
        scene ae554 with dssb
        n "Who wouldn't take a look at boobs?!"
        scene ae555 with dssa
        d "I was busy touching them... and tucking them back in."
        n "Oh."
    scene ae357 with dssb
    v "Why does everyone always talk about boobs but not about vaginas?"
    scene ae545 with dssb
    mi "I think vaginas are more intimate than boobs."
    scene ae556 with dssb
    pause #Nami sus
    d "What?"
    scene ae557 with dssa
    n "You haven't complained yet."
    mi "Weird..."
    scene ae558 with dssb
    d "One way out of my comfort zone is listening to... this."
    scene ae559 with dssa
    n "Okay, okay..."
    n "Tits or ass?"
    if milagym is True:
        if MMCBB03 is True:
            mi "He likes boobs."
        elif MMCPB03 is True:
            mi "He likes butts."
        elif MFEQ is True:
            mi "You didn't have a preference, right?"
        scene ae560 with dssb
        n "How do you know?"
        mi "I asked him."
        scene ae368 with dssb
        d "I totally forgot your pants incident."
        scene ae369 with dssa
        mi "Hey no! PSSH!"
        scene ae358 with dssb
        v "What incident?"
        d "Her pants ripped while we were at the gym."
        scene ae561 with dssr
        mi "...So embarrassing."
        scene ae365 with dssb
        n "If I didn't know you, I would hate you."
        scene ae562 with dssb
        mi "That's a compliment!"
        scene ae366 with dssr
        n "How can you have big tits, a big ass and still be relatively skinny!?"
        n "What do I have?!"
        scene ae563 with dssb
        mi "You've got a pretty great ass."
        scene ae363 with dssr
        n "Thank you!"
        scene ae362 with dssa
        d "Stop fishing for compliments... It's embarrassing."
        scene ae564 with vpunch
        n "Y-you're embarrassing!"
        d "That's well known."
    else:
        scene ae370 with dssb
        mi "[name]... Boobs or ass?"
        scene ae371 with dssa
        d "What I like more?"
        scene ae370 with dssa
        mi "Yeah."
        scene ae371 with dssa
        d "What if I like a penis?"
        scene ae372 with dssa
        mi "Then this would explain a lot."
        scene ae373 with dssa
        menu:
            "I like the look of a well formed butt.":
                $ McPrefButt4x5 = True
                scene ae372 with dssa
                mi "Noted."
            "I like the look of some well formed breasts.":
                $ McPrefBoobs4x5 = True
                scene ae372 with dssa
                mi "Noted."
            "I don't have a preference. I like them both.":
                $ McPrefBoth4x5 = True
                scene ae372 with dssa
                mi "Noted."
    scene ae364 with dssb
    n "I wanted to be a movie star when I was little."
    mi "I once got invited to an audition."
    scene ae366 with vpunch
    n "Really?!"
    mi "...Yeah, I left after I saw a black couch."
    scene ae367 with dssa
    n "*Laughs* Oh!"
    scene ae358 with dssa
    v "I don't get it."
    d "Me neither."
    scene ae343 with dssb
    mi "The black couch is a trademark of casting porn."
    scene ae357 with dssa
    v "Oh? They wanted you in a porno?"
    scene ae343 with dssr
    mi "Yup."
    d "Can we watch the movie?"
    scene ae282 with dssr
    n "Sure poophead."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae375 with dssb
    v "Oh no, it's gonna hurt the little doggo?"
    scene ae376 with dssa
    n "I- Na see! Even monsters wouldn't hurt a good doggo!"
    mi "If he had killed the doggo, we'd have to drink five shots."
    scene ae377 with dssa
    pause
    scene ae378 with vpunch
    v "Nhh!"
    n "Nothing's happening, haha."
    v "Better safe than sorry!"
    scene ae379 with dssa
    n "That also applies to condoms."
    scene ae381 with dssa
    mi "Are you on birth control, Nami?"
    scene ae380 with dssa
    n "Not yet but I plan on getting it soon."
    mi "I'm on the pill, it helps to control your menstrual cycle."
    n "How does sex feel with and without a condom?"
    mi "No idea. I never had it without one."
    scene ae382 with dssa
    n "Hmm."
    n "I wonder if a dildo would be enough-"
    scene ae383 with dssa
    mi "No girl. There's a huge difference between a dildo and an actual penis."
    scene ae384 with dssa
    n "I really need one of those life-like dildos."
    scene ae385 with dssa
    v "Maja has one."
    stop music fadeout 3.0
    n "How do you know that?"
    $ play_playlist(playlist_GirlyCh4x)
    v "She has an entire box full of them."
    scene ae323 with dssa
    pause
    scene ae324 with dssr
    pause
    jump MajaToys4x5





label Crossroad4x5:
    $ persistent.unlockedImageMilaCh4x514 = True
    scene ae507 with dssa
    v "Can we lay down for a little while?"
    d "Yeah."
    scene ae508 with dssa
    "As you try to get up, Victoria leans against you... slowly pushing you towards Mila."
    scene ae509 with vpunch
    n "I also want to be part of the cuddle session!"
    scene ae510 with dssb
    d "...Totally not uncomfortable."
    scene ae511 with dssa
    mi "Hey! As if my tiddies are that uncomfortable?"
    scene ae510 with dssa
    d "It's Vic's elbow in my side."
    v "Oops."
    scene ae512 with dssa
    v "I wonder what we should do..."
    scene ae513 with dssa
    mi "... Oh- How about we play some Truth or Dare?"
    d "Nah."
    scene ae514 with dssa
    n "Yes!"
    v "Three against one."
    scene ae515 with dssb
    mi "Nami! Truth or Dare."
    scene ae516 with dssb
    n "Truth!"
    scene ae517 with dssb
    mi "Do you have a fetish?"
    if bellameet is True:
        $ NamiFaceSitting = True
        scene ae518 with dssa
        n "Hmm, that changes from week to week, really."
    else:
        $ NamiFaceSitting = False
        scene ae518 with dssa
        n "Hmm, it always changes... but maybe risky things?"
        scene ae519 with dssa
        v "Did you already do that?"
        scene ae520 with dssa
        n "No. I'm still a virgin."
        v "Me too."
        scene ae521 with dssa
        n "I imagine that public stuff can quite exhilerating."
    scene ae516 with dssb
    n "Hmm, [name]! Truth or dare!"
    scene ae523 with dssb
    d "No way I'm going to do truth."
    d "Dare."
    scene ae524 with dssa
    n "Make out with Vic."
    menu:
        "Make out with Victoria.":
            $ KissedGirl = True
            jump VicMakeout4x5
        "Don't do it (Think of Bella.)" if BellaKiss3x5 is True:
            $ DKVDBB4x5 = True
            scene ae523 with dssa
            d "I'm sorry. I can't... I don't want to hurt Bella."
            v "It's okay [name]."
            d "And I'm actually really hungry."
            jump FourSomeAfterwards
        "Don't do it. (You don't want to.)":
            scene ae523 with dssa
            $ DKVD4x5 = True
            d "Sorry. But no... Not like this."
            n "*Sigh*"
            mi "Party pooper."
            d "I'm actually really hungry."
            jump FourSomeAfterwards


label VicMakeout4x5:
    $ VicDare4x5 = True
    stop music fadeout 2.0
    d "Alright."
    scene ae525 with dssb
    $ play_playlist(playlist_BigTiddyMila)
    "Nami turns Vic around..."
    pause
    scene ae526 with dssb
    pause
    scene ae527 with dssa
    "Victoria presses her soft lips on yours."
    scene ae528 with dssa
    pause
    scene ae529 with dssb
    with Pause(1)
    menu:
        "Caress Mila's thigh.":
            jump Foursome4x5A
        "Don't touch Mila.":
            scene ae527 with dssr
            mi "Alright! Dare is over!"
            scene ae526 with dssr
            pause
            scene black with Dissolve(2)
            with Pause(.5)
            jump FourSomeAfterwards

label FourSomeAfterwards:
    if Foursome4x5 is True:
        $ achievement.grant("Awkward4")
        $ achievement.sync()
        scene ae575 with dssb
        d "I'm hungry... shall we get some Pizza?"
        scene ae576 with dssr
        mi "And just ignore what happened?"
        scene ae577 with dssr
        d "Of course not."
        d "It would create awkwardness below the surface."
        d "We can still talk about it, but I prefer this discussion while eating pizza."
        scene ae579 with dssr
        n "I can't argue with that."
        scene ae578 with dssr
        mi "It sounds like a plan."
    else:
        pass
    scene ae580 with vpunch
    v "Okay! Pizza time!"
    scene ae581 with dssr
    v "It's already late. We'd have to go to the place to pick it up."
    scene ae582 with dssa
    n "[name] and I will get it."
    scene ae583 with dssb
    mi "Okay sure, we'll give you the money."
    scene ae584 with dssa
    n "No, this is on us."
    mi "It-"
    scene ae585 with dssr
    d "On us."
    scene ae586 with dssa
    mi "Fine. Thanks."
    if Foursome4x5 or VicDare4x5 is True:
        scene ae587 with dssa
        v "I think I need to change my underwear."
        mi "Lemme get you to your room."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Crossroads2)
    scene ae1342 with dssb
    pause
    scene ae1343 with dssa
    n "Dude."
    d "Mh?"
    scene ae1344 with dssa
    if Foursome4x5 is True:
        n "That escalated so hard."
        d "And you say you're not into girls?"
        scene ae1345 with dssa
        n "I sacrificed myself! I tried to push it further!"
        n "And you made out with Vic and Mila!"
        d "Mhm."
        scene ae1346 with dssb
        n "But... You didn't make out with me."
        scene ae1347 with dssa
        d "I think you and I making out would have ended whatever that was immediately."
    else:
        n "They're sooo horny!"
        scene ae1345 with dssa
        d "How can you tell?"
        scene ae1346 with dssb
        n "The way they play with their hair... the giggles... Trust me... The giggle always tells!"
        scene ae1347 with dssa
        d "I saw your body language too..."
    scene ae1348 with dssr
    d "Your feelings for me could get us into some deep shit someday."
    "Nami freezes."
    scene ae1349 with dssb
    n "My what for you?"
    scene ae1350 with dssb
    if NamiLove4x0 is True:
        d "We talked about it at the lake."
    else:
        $ NamiLove4x5a = True
        d "Do you think I'm an idiot?"
    d "It's obvious that there is more than just friendly love."
    scene ae1351 with dssa
    n "There- is... not."
    scene ae1352 with dssr
    d "I've accepted it. It doesn't make me think you are weird or anything..."
    d "No more than usual..."
    d "It's just in moments like these... you need to keep it under control."
    if Foursome4x5 is True:
        scene ae1353 with dssr
        d "If you would have kissed me, Mila would not have taken it-... You can imagine."
        scene ae1354 with dssa
        n "What about Vic?"
        scene ae1352 with dssb
        d "Vic is weird... She made me and Mila kiss."
    d "And you stopped denying the feelings part."
    scene ae1349 with dssa
    n "Fuck off."
    scene ae1355 with dssb
    d "Nami."
    scene ae1356 with dssa
    d "You're really important to me... It might not seem like it but I care a lot about your wellbeing."
    $ persistent.unlockedImageNamiCh4x549 = True
    if NamiCuddle04 and OeVaGe4x0 is True:
        d "If word got out about your... feelings... People could use it against us in the most cruel way."
    else:
        d "If word got out about your... feelings... People could use it against you in the most cruel way."
    "The Cheeto just stares into your eyes."
    if BellaKiss3x5 and Foursome4x5 is True:
        scene ae1357 with dssa
        d "I feel weird, though."
        scene ae1358 with dssa
        n "Bella?"
        scene ae1357 with dssa
        d "Mhm."
        scene ae1358 with dssa
        n "Do you love Bella?"
        scene ae1359 with dssr
        d "Not love... It's not there yet... But I'm into her."
        d "You know she and I kissed."
        d "And... I liked it."
        scene ae1360 with dssa
        n "Did you like what happened here?"
        scene ae1362 with dssb
        d "Maybe... Otherwise, I wouldn't have let it happen."
        scene ae1361 with dssa
        n "You're warming up to all of this."
    elif DKVDBB4x5 is True:
        scene ae1358 with dssa
        n "It must've taken a lot of willpower not to kiss Vic."
        scene ae1359 with dssb
        d "I like Bella... and I know kissing Victoria would hurt her."
    if Foursome4x5 is True:
        scene ae1358 with dssa
        n "Did you have a boner?"
        scene ae1357 with dssa
        d "No."
        scene ae1358 with dssa
        n "I'm afraid that was just another move to become normal."
        scene ae1359 with dssr
        d "It was. Drastic measures... but it's not like I disliked it."
        scene ae1361 with dssb
        n "At least Vic and Mila were wet."
        scene ae1362 with dssa
        pause
        scene ae1363 with dssa
        n "I actually don't know if they were aroused... I just think they'd be."
        scene ae1364 with dssr
        if NamiCuddle04 and OeVaGe4x0 is True:
            d "What about you?"
            n "Dude, my underwear is drenched."
        d "Lemme call Mila."
        scene ae1365 with vpunch
        n "What!? Why?"
        scene ae1366 with dssa
        d "We didn't ask what pizza they wanted."
        scene ae1367 with dssa
        if NamiCuddle04 and OeVaGe4x0 is True:
            n "Right, right... I thought you wanted to ask them if their panties were drenched."
        else:
            n "Right, right... I thought you wanted to ask them if they were aroused."
    else:
        scene ae1364 with dssr
        d "Let me call Mila."
        d "We didn't ask what pizza they wanted."
    scene ae1368 with dssb
    d "Hey."
    d "We didn't ask what pizza you wanted."
    mi "Vic wants a Salami."
    mi "I'd like a Diablo."
    d "Sure."
    pause
    scene ae1369 with dssb
    d "Diablo and Salami."
    scene ae1370 with dssa
    n "If I had to be some kind of pizza... Would I be more of a Diablo or a Salami?"
    scene ae1369 with dssa
    d "Definitely a salami."
    if BellaKiss3x5 and Foursome4x5 is True:
        scene ae1371 with dssa
        n "What will you do about Bella?"
        scene ae1372 with dssa
        d "Nothing?"
        d "I don't even know if we are dating. I- I have no idea what we are..."
        d "We kissed. We ended it. That was it."
        scene ae1373 with dssb
        n "How would you feel if she kissed someone else?"
        d "I probably wouldn't like it. But she and I aren't together."
        d "She is free to do whatever she wants."
        scene ae1374 with dssa
        n "This is a dumb situation... She's putting so much uncertainty on you."
        n "You really need to have a clear talk with her."
    stop music fadeout 2.0
    d "Let's get some pizza."
    jump JohnnyPizza

label JohnnyPizza:
    $ persistent.unlockedImageRS62 = True
    $ play_playlist(playlist_Ch4x5)
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae1375 with dssb
    pause
    scene ae1377 with dssb
    u "Welcome to Johnny's Pizza."
    u "May I take your order?"
    scene ae1376 with dssa
    n "We would like to have one Pizza Diablo."
    n "Two with Salami and one Pizza Tonno."
    u "Large or medium?"
    scene ae1378 with dssa
    d "All large."
    u "Of course."
    scene ae1379 with dssb
    u "Hey."
    d "Oh hey."
    scene ae1382 with dssr
    az "My name's Aziz, by the way."
    scene ae1383 with dssa
    d "I'm [name]."
    scene ae1384 with dssa
    az "And you are?"
    n "Nami!"
    az "You're a cute couple."
    scene ae1385 with dssb
    n "I think I will just go with it now."
    scene ae1386 with dssa
    n "We're indeed a cute couple!"
    scene ae1387 with dssr
    d "She's my roommate and we're not a couple."
    az "Oh. I see."
    scene ae1388 with dssr
    u "Oh hello! Are these friends of yours?"
    scene ae1389 with dssa
    az "Freshmen from the college. We don't know each other yet."
    scene ae1390 with dssa
    moll "It's nice to meet you! I am Aziz's Mom, Molly."
    scene ae1391 with dssr
    n "I'm Nami, nice to meet you Molly!"
    scene ae1392 with dssa
    pause
    scene ae1393 with dssr
    d "I'm [name]."
    scene ae1394 with dssa
    d "...Nami's roomie."
    if fitness is 2 or fitness is 1 and mobility is 1:
        $ MCCanidate = True
        scene ae1395 with dssa
        moll "[name]... Ah! The [name] that was on the list of potential candidates?"
        scene ae1396 with dssa
        az "Thanks for revealing classified information, Mom."
        moll "Sorry, sorry!"
        scene ae1397 with dssr
        d "How come I'm on the list?"
        scene ae1398 with dssr
        az "You made some impressive plays."
        az "We have a lot of players with high athletic abilities."
        az "But many of them lack an innovative brain."
        scene ae1399 with dssa
        az "The way you located their weak link and successfully got under their skin, got our attention."
        az "Also... Dwight likes you."
        scene ae1400 with dssb
        n "What about the girls team?"
        scene ae1401 with dssa
        az "The girls should be back next week."
        az "They had a team vacation at a wellness resort."
        scene ae1400 with dssa
        n "I want to impress them."
        scene ae1402 with dssa
        d "You will manage."
    scene ae1400 with dssa
    n "Do you always wear sunglasses?"
    scene ae1403 with dssb
    moll "Ugh... He has such beautiful eyes!"
    moll "I fear they will become part of your body at some point!"
    scene ae1404 with dssa
    az "They already are."
    if RoRum is True:
        scene ae1405 with dssa
        az "Did the reporter approach you again?"
        scene ae1406 with dssa
        d "No, I haven't seen her since."
        scene ae1407 with dssa
        moll "Don't tell me you're talking about that bitch Nicole?"
        scene ae1408 with dssa
        moll "I apologize for the harsh language."
        scene ae1409 with dssb
        n "You got approached by a reporter?"
        scene ae1410 with dssa
        d "Yeah... Before gym class."
        d "She asked me about Robin."
        scene ae1411 with vpunch
        moll "Ohhh! Is Robin your girlfriend?"
        scene ae1412 with dssa
        az "Mom! Come on? Be cool."
        scene ae1415 with dssa
        d "No, Robin isn't my girlfriend."
        d "There's just a rumor going around, she asked me about it, made some stuff up, and left again."
        scene ae1413 with dssa
        az "You can expect an article about this in the next College newspaper."
        scene ae1414 with dssa
        d "There is a college newspaper?"
        scene ae1413 with dssa
        az "It connects all the colleges from this state."
        az "She'll continue to spread it and build up on the rumor."
        scene ae1416 with dssr
        n "Isn't that against the law?"
        scene ae1417 with dssa
        az "She walks a thin grey line... Whenever she gets busted, she takes the article down, pays a fine... But the damage is done."
        scene ae1418 with dssb
        moll "Oh no... It reminds me of-"
        scene ae1419 with dssa
        az "Don't."
        scene ae1420 with dssa
        "She places her hand on her Son's shoulder."
    scene ae1421 with dssb
    u "Two large Gio's and one large Macci pizza."
    moll "That's ours."
    scene ae1422 with dssb
    az "See you two around."
    scene ae1423 with dssa
    moll "Goodbye [name] and Nami!"
    n "Bye! Have a good meal!"
    d "Bye."
    scene ae1424 with dssa
    n "Nice mommy."
    d "Mhm."
    if RoRum is True:
        scene ae1425 with dssb
        n "But man... Why do you never tell me anything?"
        d "She just approached me and asked one question, and then the guys made her go away."
        scene ae1426 with dssa
        n "Still! If a reporter approached me, I wouldn't stop talking about it!"
        scene ae1427 with dssa
        d "Yeah, but I don't care about stuff like that."
        d "I don't want to be famous or known at all."
        scene ae1428 with dssa
        n "Then stop fucking girls in public restrooms."
        scene ae1429 with dssr
        "The table next to you redirects their attention to you and Nami."
        pause
    if NiaDeal is True:
        scene ae1430 with dssr
        d "Someone who's number I haven't saved is calling me."
        scene ae1431 with dssa
        nia "Hi [name]. I got your number from the group chat."
        nia "Sorry if I'm disturbing you, but would it be okay with you if we met up tomorrow instead of Sunday?"
        scene ae1432 with dssa
        d "Yeah, I guess.."
        scene ae1433 with dssa
        nia "Great!"
        nia "Sorry for the short notice! Good night!"
        scene ae1434 with dssa
        d "It's alright. I'll see you then."
        scene ae1435 with dssb
        pause
        scene ae1436 with dssa
        d "I'm going to head over to Nia's tomorrow instead of Sunday."
        n "Oof... I've got no idea when we'll be home."
    else:
        scene ae1435 with dssb
        pause
    scene ae1437 with dssa
    u "Large Pizza Tonno, Diablo and two Salami!"
    d "Thank you."
    scene ae1438 with dssr
    n "Put mine in the middle so it keeps warm!"
    if Foursome4x5 is True:
        scene ae1439 with dssa
        d "Mila's in the middle."
        d "She needs to be in the best mood possible for what's to come..."
        scene ae1440 with dssa
        n "It'll get awkward."
        d "We'll get through it."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    jump Pizza4x5

label Pizza4x5:
    $ play_playlist(playlist_BigTiddyMila)
    if Foursome4x5 is True:
        $ NamiBi4x5 = True
        scene ae588 with dssb
        pause
        scene ae589 with dssa
        mi "Alright... Can we now talk about what happened?"
        scene ae590 with dssa
        d "I assume while Nami and I were getting pizza, you and Vic already exchanged some thoughts?"
        scene ae591 with dssa
        mi "It was mostly Vic saying how great you kiss."
        scene ae594 with dssb
        n "Well, I had no problems with what happened!"
        scene ae595 with dssa
        d "Of course not, you're a weirdo."
        scene ae598 with dssb
        v "I liked it too."
        scene ae599 with dssa
        v "But I feel bad that someone here might feel awkward now."
        scene ae592 with dssb
        mi "It... was awkward... I-It's now awkward. Back when we did it... It was nice."
        scene ae593 with dssa
        mi "The thing is I'm not really into girls."
        scene ae596 with dssb
        n "Me neither... Or so I thought."
        scene ae597 with dssa
        d "You are now?"
        scene ae596 with dssa
        n "I didn't dislike kissing Vic."
        scene ae600 with vpunch
        n "Wait! Vic! Come! Kiss me again."
        scene ae601 with dssa
        pause
        scene ae607 with dssb
        "You and Mila share an awkward look."
        scene ae602 with dssr
        pause
        scene ae604 with dssa
        n "Yeah, I don't dislike it."
        scene ae603 with vpunch
        $ persistent.unlockedImageVicCh4x63 = True
        n "I'M BI NOW!"
        scene ae617 with dssa
        v "I didn't dislike it either. But I like [name]."
        scene ae605 with dssa
        n "I get that."
        scene ae606 with dssa
        pause
        scene ae608 with dssr
        pause
        scene ae614 with dssr
        pause
        scene ae615 with dssa
        n "B-Boys! I mean boys in general! N-not [name]!"
        scene ae616 with dssb
        pause
        scene ae618 with dssa
        n "T-The problem I have with all of this is the reason [name] did it."
        n "He's pushing himself to be normal and I'm sure this will not end well."
        scene ae609 with dssr
        mi "Oh. Yeah [name], stop that... Go at your own pace."
        scene ae620 with dssb
        d "I did."
        scene ae619 with dssa
        n "Uh hu, from 'Don't touch me' to a foursome in a few days... Totally normal."
        scene ae620 with dssa
        d "I have to somehow widen my comfort zone."
        scene ae610 with dssb
        mi "To be honest, I get his point here."
        mi "In order to escape the comfort zone, you'll need to constantly attack it."
        n "Still..."
        if BellaKiss3x5 is True:
            scene ae611 with dssb
            mi "What I really don't like is that [name] kissed us even though he and Bella are... bonding?"
            scene ae612 with dssa
            d "We're not together."
            scene ae611 with dssa
            mi "Yeah, but it would break her heart, wouldn't it?"
            mi "She would of course play it cool but I know her. She wouldn't take it well."
            scene ae621 with dssb
            v "It's all my fault..."
            scene ae622 with dssa
            d "No Vic. I chose to kiss you."
            scene ae613 with dssa
            mi "I'm just saying... we're college freshmen and I assume we're going to experience a lot more than this... Maybe talk to her and put it on ice."
            mi "I see a lot of potential future disasters."
            scene ae621 with dssb
            v "Or you make it official."
            scene ae613 with dssb
            mi "...Or that."
    else:
        scene ae588 with dssb
        pause
    scene ae623 with dssb
    d "The pizza is good. It can almost rival Gio's."
    scene ae624 with dssb
    v "Gio's?"
    scene ae625 with dssa
    d "It's a place on the other side of the city."
    n "It's reaaaally good."
    n "But this one here has better cheese."
    if RoRum is True:
        $ MilaVicHelp = True
        scene ae626 with dssa
        mi "[name]? What exactly happened with Robin?"
        scene ae624 with dssa
        v "It must have happened right after you stormed out of class, right?"
        scene ae627 with dssb
        n "Huh?"
        n "Why did you storm out?"
        scene ae628 with dssa
        pause
        d "Victoria has an eraser."
        scene ae627 with dssa
        n "Oh no... Don't tell me it's the same rubby?"
        scene ae628 with dssa
        d "Yeah."
        scene ae629 with dssa
        d "And when Vic put it in my hand, I freaked out."
        scene ae627 with dssa
        n "That's not a sign whatsoever."
        scene ae630 with dssa
        d "I know that!"
        d "It just... really caught me off guard."
        scene ae631 with dssa
        d "And it showed me just how far I am from moving on."
        d "I'm still at the same place I was two years ago."
        scene ae632 with dssa
        mi "No, you're not."
        scene ae633 with dssa
        "Mila comes over."
        scene ae634 with dssa
        mi "I don't know exactly how you were two years ago but..."
        scene ae635 with dssa
        mi "Instead of being alone and isolated with your thoughts, you now have us."
        scene ae638 with dssb
        v "Mila is right!"
        v "We will always be there for you!"
        scene ae637 with dssb
        n "Remember what I said?"
        n "This is the best time to move on."
        n "So many new and awesome people that like you and want to help you."
        scene ae639 with dssb
        d "Mmm.."
        scene ae640 with dssa
        d "But do I even like you guys?"
        scene ae636 with vpunch
        mi "You suck dude."
    scene ae641 with dssa
    n "We met a guy from the first team at the Pizza place."
    n "Aziz was his name, I think."
    scene ae642 with dssb
    mi "I know him from elementary school."
    mi "He was two classes above me, though."
    scene ae643 with dssa
    n "How is he?"
    scene ae642 with dssa
    mi "I never really talked to him but he seemed cool."
    n "Was he wearing sunglasses back then?"
    scene ae644 with dssa
    mi "*Chuckles* No."
    mi "When I got to high school he was wearing them all the time."
    scene ae645 with dssa
    mi "No idea why."
    if MCCanidate is True:
        scene ae646 with dssb
        n "His mother accidentally revealed that [name] is on the list for the potential candidates for the first team."
        scene ae644 with dssb
        mi "Way to go!"
        scene ae647 with dssr
        v "That's so awesome!"
    scene ae648 with dssb
    n "Alright, let's watch the funny movie."
    n "I wanna see some tiddies... but first I need to pee."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae649 with dssb
    pause
    scene ae650 with dssr
    pause
    scene ae651 with dssa
    d "(Tomorrow I need to visit Emilio.)"
    scene ae652 with dssa
    d "(Maybe he can help me find some closure...)"
    scene ae653 with dssb
    mi "Why's college not like in the movies?"
    scene ae654 with dssa
    n "They never seem to have class."
    if RoRum is True:
        scene ae653 with dssa
        mi "[name]'s life seems comparable to this."
        mi "It's the first week and he's already got the reputation of a dude who bangs girls in public restrooms."
        scene ae654 with dssa
        n "True."
    scene ae656 with dssb
    n "I wish we had more parties!"
    d "Me too."
    scene ae657 with dssa
    "Nami shoots you a suspicious look."
    d "That way you'd be at a party and I'd have some peace."
    scene ae658 with dssa
    n "You suck... And you know I would drag you along!"
    scene ae659 with dssb
    v "When Maja was still a student she had lots of parties."
    v "I guess they will happen soon."
    scene ae653 with dssb
    mi "We've got a house warming party coming up for the bar."
    mi "And I'm sure we're all going to make some new friends there."
    scene ae654 with dssa
    n "I've been invited to some parties on another campus."
    scene ae655 with dssa
    mi "By whom?"
    n "People from [name] and mine's old high school."
    scene ae660 with dssb
    mi "Be careful with the other colleges."
    mi "I heard the rivalries are quite nasty... If [name] makes the first team, I could see them targeting you."
    n "Like?"
    mi "Try to bed you, film it and then publish it."
    scene ae661 with dssb
    n "That would mean I'd actually be interested in someone... and stupid enough to fall for that..."
    scene ae662 with dssa
    d "IF I make the first team."
    scene ae663 with dssa
    mi "You will. I believe in you."
    scene ae664 with dssa
    v "I haven't seen you play yet but I'm sure you will!"
    scene ae665 with dssb
    mi "But... I heard you pushed Kai, the son of one of the head coaches into a bookshelf."
    scene ae658 with dssb
    n "What?! When?"
    scene ae666 with dssb
    d "When I went to talk with Nadia."
    d "I'm sure he didn't even mean bad by it... but he shouldn't have touched me."
    scene ae667 with dssb
    n "You idiot..."
    n "Why are you making your own life so hard?"
    scene ae668 with dssa
    d "I don't give a fuck if he goes crying to his Daddy."
    d "As long as I perform well, and get more first team members on my side, I'll make it."
    scene ae667 with dssa
    n "Still... You need more impulse control."
    scene ae668 with dssa
    d "I'm working on it."
    scene ae665 with dssb
    mi "Kai's not a bad guy but... likes to play the knight in shining armor."
    scene ae666 with dssa
    d "If you do that you should have something to follow up besides: 'I'm gonna sue you.'"
    scene ae669 with vpunch
    v "I'm gonna sue you!"
    d "For what?"
    scene ae672 with dssa
    v "For having a nice butt!"
    scene ae670 with dssb
    "Nami and Mila giggle."
    mi "That was the movie."
    d "I missed pretty much everything."
    n "Come! All together."
    scene ae671 with dssb
    menu:
        "Ask Mila to go for a walk.":
            d "I'm getting kinda tired... Do you want to take a walk?"
            scene ae673 with dssb
            mi "Me?"
            scene ae674 with dssa
            d "I'm looking right at you."
            scene ae673 with dssa
            mi "Okay- sure!"
            scene ae675 with dssa
            n "Come Vic, let's take some pictures for Aurora."
            v "Sure!"
            scene ae679 with dssb
            stop music fadeout 2.0
            pause
            jump MilaWalk4x5
        "Ask Vic to roll on a walk.":
            d "I'm getting sleepy..."
            d "Vic, do you want to take a walk?"
            scene ae676 with dssb
            v "I would if I could."
            d "Come."
            scene ae675 with dssa
            n "Mila! Let's take some pics for Aurora."
            mi "Sure!"
            scene ae678 with dssb
            stop music fadeout 2.0
            pause
            jump VicWalk4x5
        "Take a walk (Nami).":
            d "I'm getting sleepy... I'm gonna take a walk."
            scene ae675 with dssb
            n "I'll come with you!"
            scene ae677 with dssa
            mi "Vic, we need more pictures."
            v "Sure!"
            stop music fadeout 2.0
            scene ae680 with dssb
            pause
            jump CheetoWalk4x5

label MilaWalk4x5:
    $ persistent.unlockedImageR6 = True
    $ play_playlist(playlist_Crossroads)
    $ NamiPeaceTreaty = False
    scene ae681 with dssb
    pause
    scene ae682 with dssa
    pause
    scene ae683 with dssb
    d "Shall we walk for a while?"
    scene ae684 with dssa
    mi "Yes."
    $ persistent.unlockedImageMilaCh4x515 = True
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae685 with dssb
    pause
    scene ae686 with dssa
    mi "W-we're not going into the forest, right?"
    d "Are you scared?"
    mi "Yes."
    scene ae687 with dssb
    pause
    scene ae688 with dssa
    d "Let's sit down for a moment."
    scene ae689 with dssb
    pause
    scene ae690 with dssr
    d "I can't let my comfort zone win."
    d "Whenever I think about spending time with someone other than Nami, it feels like a burden."
    scene ae691 with dssa
    if MilaDate is True:
        d "I like you, and I don't want to see you as a burden."
    else:
        d "I don't want to see you as a burden."
    scene ae692 with dssb
    mi "*Chuckles* You really need better ways to phrase this stuff."
    scene ae693 with dssa
    d "All you need to focus on is that I like you."
    scene ae692 with dssa
    mi "I like you too."
    scene ae694 with dssa
    mi "It can't be easy going from full isolation to... well, all of this."
    if MilaDate is True:
        mi "I talked with Nami about you... I was a little salty after you kept leaving me in the dark."
        mi "Communication is key."
    else:
        mi "But communication is key."
    scene ae695 with dssb
    mi "When she told me about you and how you spent the last few years..."
    mi "That's why I'm asking you to please tell me whenever there's something on your mind."
    mi "Just so that I can understand your motives."
    scene ae696 with dssa
    d "I'll try."
    scene ae697 with dssb
    pause
    if MilaDate is True:
        d "About our date."
        d "Let's have it the day after the bar opening."
        scene ae698 with dssa
        mi "Provided we're not too hungover."
        mi "...I will need to go to work that evening, though."
        scene ae699 with dssb
        d "No problem... I mean... We could always just go back to my place after the bar."
        scene ae700 with dssa
        "Mila smirks and raises her brow."
        scene ae701 with dssa
        mi "I'd like that."
    else:
        scene ae698 with dssa
        pause
    scene ae699 with dssa
    d "Do you need to work the entire week?"
    scene ae702 with dssa
    mi "Every single fucking day."
    if MilaDaring4x5 is True:
        menu:
            "Mention Garden of Venus to her. (Onlyfans.)":
                $ MilaVenus4x5ID = True
                scene ae703 with dssa
                d "You should make a Venus profile."
                scene ae704 with dssa
                if MilaDate is True:
                    mi "That's a weird thing to say to the girl you're about to date."
                else:
                    mi "That's a weird thing to say to a girl."
                scene ae705 with dssa
                d "Why?"
                d "I've seen pictures there that don't contain any real nudity."
                scene ae707 with dssa
                d "I'm sure your normal dress style would already be enough to gain some following."
                scene ae706 with dssa
                mi "It'd feel like I'm selling out my morals."
                scene ae708 with dssb
                "You get up from the bench."
                scene ae709 with dssb
                d "Ask the people who work 60 hours a week, get treated and paid like shit if morality matters."
                d "Meanwhile some skank not even half as attractive as you makes a few thousand from a picture."
                d "And now guess who's leading a more free and happier life."
                d "But hey... At least they can comfort themselves knowing that their morals are still intact. All while they head to their second job that day..."
                scene ae710 with dssa
                mi "...Maybe you're right."
                scene ae711 with dssa
                d "I'm not telling you what to do... I'm just giving you a different point of view."
                scene ae710 with dssa
                if MilaDate is True:
                    $ MilaVenus4x5 = True
                    mi "The fact that we're dating... or about to date and you'd still say this makes me wanna give it a go."
                    scene ae711 with dssa
                    d "It's not like I wouldn't also benefit from you leaving your job."
                else:
                    mi "I don't know... There're pros and cons..."
                scene ae712 with dssa
                d "You'd have much more time to focus on friends and golf."
                mi "...Sounds great."
                scene ae713 with dssa
                d "Remember the picture with the cleavage you posted to Aurora?"
                d "That's all you need to post on Venus... with the difference that you'll get paid for it."
                mi "...That could work."
                d "Just... don't post any other daring pictures to Aurora... otherwise there's not really a reason to subscribe to you."
                scene ae714 with dssa
                mi "I already feel dirty."
                d "Blame the bench."
                "You and Mila take in the view."
            "Don't and be on the watch for a different solution.":
                $ MilaJobLookout = True
                scene ae703 with dssa
                d "I'll keep my eyes open and see if we can find an alternative for you."
                scene ae704 with dssa
                mi "Trust me... I looked."
                scene ae705 with dssa
                d "You looked at normal jobs."
                d "I'll look for more exotic ones."
                scene ae707 with dssa
                d "I'm sure time will bring us something."
                scene ae708 with dssa
                "You get up from the bench."
    else:
        $ MilaJobLookout = True
        scene ae703 with dssa
        d "I'll keep my eyes open and see if we can find an alternative for you."
        scene ae704 with dssa
        mi "Trust me... I looked."
        scene ae705 with dssa
        d "You looked at normal jobs."
        d "I'll look for more exotic ones."
        scene ae707 with dssa
        d "I'm sure time will bring us something."
        scene ae708 with dssb
        "You get up from the bench."
    scene ae713 with dssb
    mi "Would you play golf with me?"
    d "I at least would give it a try, yeah."
    scene ae715 with dssa
    mi "I'll teach you!"
    scene ae716 with dssa
    pause
    scene ae717 with dssr
    mi "Is there something you wanted to talk to me about?"
    scene ae718 with dssr
    d "No."
    d "I just want to be here... with you."
    d "We don't necessarily need to talk."
    scene ae719 with dssa
    mi "It says a lot about two people if they can be together without a word being said."
    scene ae720 with dssa
    stop music fadeout 2.0
    pause
    $ play_playlist(playlist_WatchingStars)
    if MilaDate is True:
        scene ae721 with dssa
        pause
    scene ae722 with dssb
    d "Sometimes I... I don't know if it is a dream or an actual memory."
    d "...I hear my mother reading to me. Whenever I sit down and look up to the stars I can recall it."
    d "I think the book she read to me was about the universe."
    scene ae723 with dssb
    "Mila smiles as she snuggles against you."
    scene ae724 with dssr
    d "I... I don't know if it actually happened."
    scene ae725 with dssr
    mi "I'm sure it did."
    mi "And I'm sure she was a lovely person."
    scene ae724 with dssr
    d "I love Nojiko."
    d "I just sometimes wish I could've gotten to know my parents."
    scene ae725 with dssa
    mi "I'm sorry you never did."
    if MilaDate is True:
        scene ae720 with dssb
    else:
        scene ae721 with dssb
    d "I see Nojiko working all day long to support us."
    d "I can see it in her eyes how much she hates working at the hospital... The hours and the stress really get to her."
    d "I wish I could fulfill her dream of having her own little doctor's office."
    scene ae726 with dssa
    mi "Who says you can't?"
    mi "If I've learned one thing growing up poor..."
    mi "Nothing's going to happen if you don't do it yourself."
    scene ae727 with dssa
    d "It's my comfort zone."
    scene ae728 with dssa
    mi "I never experienced a comfort zone. I mean, how would you if you never feel comfortable."
    scene ae729 with dssa
    d "Then you also know that you're the only one capable of changing it."
    scene ae728 with dssa
    mi "And I'm so close to achieving it."
    scene ae729 with dssa
    d "In what way?"
    scene ae730 with dssb
    mi "I've always paid close attention to my spendings."
    mi "This way I managed to save a lot of money... At least enough to get my own place and keep it until college ends."
    d "That's nice."
    if MilaDate or BellaKiss3x5 is True:
        scene ae731 with dssb
        menu:
            "Put your hand on her butt.":
                $ MilaButt4x5 = True
                scene ae732 with dssa
            "Don't.":
                pass

    else:
        scene ae733 with dssa
    mi "I really hope we're all going to move into a place. That would cut down my costs even more."
    d "There might be a thing."
    scene ae734 with dssb
    mi "*Worried* ...What thing?"
    scene ae735 with dssb
    d "There might be a possibility that me and Nami are going to move into Zara's house."
    scene ae736 with dssa
    mi "Uhh- you don't have to... move there... you know?"
    scene ae735 with dssa
    d "True."
    scene ae736 with dssa
    mi "But you want to?"
    scene ae735 with dssa
    d "We'll see."
    d "Having my own place would be much better. I'm not independent enough to support Nojiko."
    scene ae737 with dssa
    mi "Don't worry. It'll happen."
    scene ae738 with dssa
    mi "Just do it at a healthy pace."
    d "I guess I need a job too."
    if MilaDaring4x5 is True:
        scene ae739 with dssa
        mi "Make a Venus account."
        "You let out a small laugh."
    scene ae740 with dssb
    pause
    if vicdate is False and (BellaKiss3x5 and MilaEnc03x) is True:
        scene ae776 with vpunch
        $ persistent.unlockedImageMilaCh4x517 = True
        "Suddenly, Mila steps towards you and presses her lips onto yours."
        pause
        menu:
            "Break the kiss.":
                $ MilaKissBreak4x5 = True
                $ McPa +=2
                scene ae777 with vpunch
                d "W-wow Mila... Stop."
                if BellaKiss3x5 and MilaEnc03x is True:
                    scene ae778 with dssb
                else:
                    scene ae779 with dssb
                pause
                scene ae780 with dssb
                mi "I- I'm so sorry! I- thought you gave me a sign- like- like the 'look'!"
                mi "Oh my god! I'm so sorry!"
                scene ae781 with dssa
                d "...It's alright... I'll take it as a compliment... Just please don't do it again."
                scene black with Dissolve(2)
                with Pause(.5)
            "Kiss her back.":
                jump MilaKiss4x5A
    elif MilaDate is True:
        menu:
            "Hold her hand.":
                $ KissedGirl = True
                jump MilaKiss4x5C
            "Don't do it.":
                jump MilaKiss4x5Con
    else:
        jump MilaKiss4x5Con

label MilaKiss4x5Con:
    scene ae763 with dssb
    d "I hope I'll make the playoffs and immediately get into the first team."
    scene ae764 with dssa
    mi "That's very rare."
    mi "Most get into the second team first... and a few months later they move up."
    scene ae765 with dssa
    d "I don't have that kind of time."
    scene ae767 with dssa
    mi "I think a job is inevitable."
    scene ae765 with dssa
    d "I will certainly not wait tables."
    scene ae767 with dssa
    mi "Yeah, don't!"
    mi "What about being a bartender?"
    scene ae765 with dssa
    d "I have no idea how to mix drinks."
    scene ae766 with dssa
    d "I should just rob people."
    d "Do the honest work of a criminal..."
    scene ae768 with dssa
    mi "I might actually have something for you."
    scene ae769 with dssa
    d "What?"
    mi "I have a friend who works at a small store in Prenz."
    mi "They're looking for help."
    scene ae769 with dssa
    d "...What would I need to do?"
    scene ae770 with dssa
    mi "Just help them with uhhh stuff."
    mi "I don't know! We could ask."
    scene ae771 with dssb
    d "*Sigh* Why couldn't you just say... 'Nope, got nothing.'"
    d "Now if I say 'no' it will leave a bad taste and I'll come across as lazy."
    scene ae772 with dssa
    mi "*Giggles* A reaaaally bad taste."
    scene ae773 with dssa
    "Carefully she places her head on your shoulder."
    scene ae774 with dssa
    d "Wanna go back?"
    scene ae775 with dssa
    if MilaKiss4x5 is True:
        mi "I could sit here forever... but yes, I guess we should."
    else:
        mi "Yeah, sure."
    $ achievement.grant("WatchingStarsMila")
    $ achievement.sync()
    scene black with Dissolve(2)
    with Pause(.5)
    if MilaKiss4x5 is True:
        $ MilaLike4x5 = True
        scene ae790 with dssb
        "Mila and you walk back to Victoria's house."
        scene ae785 with dssa
        "As you walk towards the entrance of the house, you realize how elegantly Mila moves her curves."
        scene ae786 with dssb
        "With every step, she swings her butt a little, resulting in her shorts sliding up. "
        scene ae787 with dssb
        "Her confident posture compliments her breasts and overall charisma."
        d "(...I like looking at her.  Maybe I do even like talking to her... Maybe I even like her?)"
        scene ae788 with dssa
        mi "Everything okay?"
        scene ae789 with dssa
        d "(I do like her.)"
    elif MilaKissBreak4x5 is True and MilaDate is False:
        scene ae789 with dssb
        "Mila and you walk back to Victoria's house."
        scene ae790 with dssa
        d "(That was a weird situation... I didn't give her any real signs of attraction... But she still kissed me out of nowhere.)"
        scene ae787 with dssb
        d "(I'll need to keep an eye on her.)"
        scene ae788 with dssa
        mi "Everything okay?"
    scene ae782 with dssb
    d "Wanna scare Vic and Nami?"
    scene ae783 with dssa
    mi "Yes!"
    scene ae784 with dssb
    d "Nami's very easy to scare...  Let's see."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch4x5)
    scene ae792 with dssb
    d "There they are..."
    scene ae791 with dssa
    mi "Vic's so cute."
    scene ae793 with dssb
    pause
    scene ae794 with dssa
    pause
    scene ae795 with dssb
    pause
    scene ae796 with dssa
    pause
    scene ae795 with dssa
    d "What are they doing?"
    mi "I have no idea."
    scene ae797 with dssa
    d "I'll go around the corner."
    scene ae798 with dssb
    pause
    scene ae799 with dssa
    pause
    scene ae800 with vpunch
    n "AAAAGH!"
    scene ae801 with vpunch
    "Nami's voice stops working mid-scream."
    scene ae802 with vpunch
    n "[name]! WE HAD A PEACE TREATY!"
    $ persistent.unlockedImageNamiCh41 = True
    n "YOU BROKE IT!"
    scene ae803 with dssa
    v "[name]! You meany!"
    scene ae804 with dssb
    n "YOU!"
    scene ae805 with vpunch
    n "THIS MEANS WAR!"
    scene ae806 with dssa
    v "How was it outside?"
    d "Pretty nice."
    scene ae810 with dssb
    mi "What were you two up to?"
    scene ae807 with dssb
    n "We talked about breasts."
    scene ae808 with dssa
    mi "I have some arguments."
    scene ae809 with dssa
    n "Two very big arguments, if I may say."
    scene ae811 with dssb
    mi "You may."
    $ persistent.unlockedImageNamiCh4x545 = True
    $ persistent.unlockedImageRLWSMila4x5 = True
    jump Ch4x5NachtPart3

label VicWalk4x5:
    $ persistent.unlockedImageVicCh4x65 = True
    $ persistent.unlockedImageR7 = True
    $ play_playlist(playlist_Crossroads)
    scene ae812 with dssb
    pause
    scene ae813 with dssa
    "You just stand there, staring into the night with Victoria on your arms."
    scene ae814 with dssb
    "A long exhale causes Victoria to look at you."
    scene ae815 with dssa
    v "Is everything okay?"
    scene ae814 with dssa
    d "Yes."
    scene ae816 with dssb
    d "Do you want to go up there?"
    v "Sure."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae817 with dssb
    pause
    scene ae818 with dssb
    v "The stars are twinkling so much tonight."
    d "I used to imagine that there was a big space fight happening and the stars reflected the light of the explosions."
    v "Poor aliens."
    scene ae820 with dssb
    pause
    scene ae819 with dssa
    v "I'm really glad you and Nami came by."
    scene ae821 with dssb
    d "Already sick of Mila?"
    scene ae822 with dssa
    v "*Chuckles* No."
    v "Mila's amazing. She's so selfless."
    scene ae823 with dssa
    d "That's not always a good thing."
    scene ae822 with dssa
    v "In my opinion it is."
    scene ae823 with dssa
    d "You need to have a healthy amount of selfishness or you'll get nowhere and people will take advantage of you."
    scene ae824 with dssa
    v "I just hope she's not doing it out of pity."
    d "I'm sure she isn't."
    scene ae823 with dssa
    d "You can be... fun."
    scene ae825 with dssa
    d "What's with all the flowers?"
    scene ae818 with dssb
    v "Oh... My parents used to dress me in flower dresses when they were still alive."
    v "Maja used to make fun of me as the 'Flower child'."
    scene ae826 with dssb
    v "I think it reminded her of them..."
    scene ae827 with dssa
    d "That's sweet of her."
    scene ae826 with dssa
    v "Yes."
    scene ae828 with dssb
    pause
    scene ae829 with dssb
    v "How's Bella?"
    scene ae830 with dssa
    d "What do you mean?"
    scene ae831 with dssa
    if BTY is True:
        v "She's so different around you."
    v "I saw her in college a few days ago... Watching you from afar."
    v "She looked so cute."
    scene ae832 with dssb
    v "How's she when you're alone with her?"
    scene ae833 with dssa
    d "We insult each other a lot."
    scene ae832 with dssa
    v "But it's not meant as a real insult, right?"
    scene ae833 with dssa
    if BellaKiss3x5 is True:
        d "Right."
    else:
        d "Most of them..."
    scene ae834 with dssb
    d "She's complex... Much more complex than most people give her credit for."
    d "But that's her own fault. She behaves irrationally and out of bitterness."
    d "Apparently she also had some history with Ceril."
    scene ae835 with dssb
    v "Oh."
    scene ae834 with dssa
    d "I'll introduce you to her."
    scene ae836 with dssa
    v "That would be nice."
    v "Can you put me on your lap and put your arm around me?"
    d "Are you cold?"
    scene ae837 with dssa
    v "No, but I'm yearning for your touch."
    scene ae838 with dssa
    d "'Yearning'."
    scene ae839 with dssb
    "Victoria giggles."
    scene ae840 with dssb
    pause
    d "(She smells nice.)"
    scene ae841 with dssa
    v "You smell great."
    scene ae842 with dssa
    d "...I just thought the same about you."
    scene ae843 with dssa
    if vicdate is True:
        v "I can't wait for our date..."
    v "Every day I wake up I think about you."
    scene ae844 with dssa
    d "I don't really get it."
    scene ae843 with dssa
    v "Me neither."
    v "Some things aren't meant to be understood. They simply are."
    scene ae846 with dssb
    v "Overthinking will get you nowhere."
    v "I already felt some sort of attraction to you when we first met... Before the accident."
    v "I didn't even need to go where we went... I just followed you for a block to see if we'd talk more."
    scene ae845 with dssa
    d "So... You would've never gone that way and crossed that street if it wasn't for me?"
    scene ae847 with dssb
    v "Yeah."
    scene ae848 with dssa
    "You keep quiet."
    scene ae847 with dssa
    v "It's okay... I appreciate the accident for what it is."
    scene ae849 with dssb
    d "That's such a weird thing to say."
    scene ae850 with dssa
    v "It completely changed the way I see the world... and- and as long as I can learn to walk again... I'll be fine."
    v "If it wasn't for the accident there's no way you and I would be sitting here right now."
    scene ae851 with dssa
    d "Yeah, you might've been sitting here with someone who is just a normal guy."
    scene ae852 with dssa
    v "You're a normal boy... with sad eyes."
    menu:
        "I don't want to be normal.":
            $ McHonest4x5 = True
            scene ae849 with dssa
            d "Normal is what made Summer's parents resent me."
            scene ae850 with dssa
            v "Don't take it personally."
            scene ae849 with dssa
            d "They told me to my face that I was nothing but shit."
            scene ae852 with dssa
            v "They obvi-"
            scene ae851 with dssa
            d "I know Vic. I know that I'm not shit... I know that they were the trash."
            stop music fadeout 3.0
            d "But still, I would've made peace with that trash for Summer."
        "That's all I want... A normal life... A normal mind.":
            $ McNormal4x5 = True
            scene ae852 with dssa
            v "And you'll get there."
            stop music fadeout 3.0
            if vicpromise is True:
                $ VicErh4x0 = True
                scene ae853 with dssa
                v "Just like I will regain the ability to walk."
    scene ae854 with dssb
    $ play_playlist(playlist_WatchingStars)
    d "Sometimes I... I don't know if it was a dream or an actual memory."
    d "...I hear my mother reading to me. Whenever I sit down and look up to the stars I can recall it."
    d "I think the book she read to me was about the universe."
    d "But... I don't know if it actually happened or not."
    v "That sounds beautiful!"
    d "I love Nojiko."
    d "I just sometimes wish I could've gotten to know my parents."
    v "I'm so sorry you never did..."
    v "I at least got to see mine for a brief period of time..."
    d "I see Nojiko working all day long to support us."
    d "I can see it in her eyes how much she hates working at the hospital... The hours and the stress really get to her."
    d "I wish I could fulfill her dream of having her own little doctor's office."
    v "You can!"
    v "It's important to... never give up..."
    $ persistent.unlockedImageVicCh4x64 = True
    pause
    scene ae853 with dssb
    v "I think it's nice that you and Nami are going to join a book club."
    scene ae849 with dssa
    d "Is it though?"
    scene ae853 with dssa
    v "Yes!"
    v "I've been reading my whole life and since I'm in the wheelchair, I do read a lot more."
    scene ae849 with dssa
    d "What're you reading?"
    scene ae855 with dssr
    v "Sex."
    scene ae856 with dssa
    d "What?"
    scene ae855 with dssa
    v "*Snobby voice* I've come to appreciate adult literature."
    "Victoria giggles."
    d "Really?"
    v "Yes."
    d "You're unpredictable."
    scene ae857 with dssa
    v "I'm cute... and people think all I do are cute things."
    scene ae858 with dssa
    v "But sometimes! Sometimes I do adult things!"
    menu:
        "Tell me about the book you're reading.":
            $ VicEroticBook4x5 = True
            scene ae860 with dssb
            v "It's about a wife who found her husband cheating... Got divorced and is now on a holiday trip with her best friend."
            scene ae861 with dssa
            d "And I assume they're having lots of fun there."
            scene ae860 with dssa
            v "I've yet to come to a part where they're having fun. At the moment it's just teasing and... Well... it's working."
            scene ae861 with dssa
            d "Do you imagine yourself in those situations?"
            scene ae859 with dssa
            v "*Blushes* Sometimes."
            v "There's so much I want to try out."
            v "I always thought you'd just put your dong in... And that's pretty much it."
            scene ae862 with dssa
            v "But those books taught me about foreplay and how intense it is... or can be."
            if vicdate and Foursome4x5 or VictoriaKiss4x5 or VicDare4x5 is True:
                menu:
                    "Tease Victoria a little.":
                        $ KissedGirl = True
                        jump VicTease4x5A
                    "Don't and enjoy the moment quietly.":
                        scene ae868 with dssa
                        d "Tell me more about it on our date."
                        jump VicWalkCon4x5
        "Don't ask further questions.":
            pass

label VicWalkCon4x5:
    if vicdate is False:
        scene ae869 with dssb
        v "And you really don't want to go out with me?"
        menu:
            "Reconsider and go out with her.":
                $ VicDateEntry2 = True
                if MilaDate is True:
                    scene ae870 with dssa
                    d "I'm already going out with Mila."
                    scene ae871 with dssa
                    v "A-And that's why you should go out with her first... and see where it goes."
                    scene ae872 with dssa
                    d "This sounds like a recipe for disaster."
                    scene ae871 with dssa
                    v "Y-you worry too much."
                    $ achievement.grant("DoubleAgent")
                    $ achievement.sync()
                else:
                    pass
                d "I'd like to go out with you."
                scene ae874 with dssb
                v "Great!"
            "Sorry, no. I just don't feel like it.":
                $ VicFriend4x5 = True
                scene ae872 with dssa
                v "...I understand."
                scene ae873 with dssr
                pause
                "You comfort her as you notice tears running down her face."
                scene ae874 with dssb
                "Victoria can't hold it anymore and starts crying."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae875 with dssb
    pause
    scene ae876 with dssa
    d "(Vic's falling asleep... She's getting heavier.)"
    scene ae877 with dssa
    d "Wanna go back?"
    scene ae878 with dssb
    v "Mhmmm..."
    scene ae879 with dssb
    pause
    $ achievement.grant("WatchingStarsVic")
    $ achievement.sync()
    stop music fadeout 3.0
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae880 with dssb
    pause
    scene ae881 with dssb
    v "Wait, wait..."
    v "Do you wanna scare them?"
    $ persistent.unlockedImageNamiCh4x545 = True
    d "Oh Nami is so easily scared... But I have a peace treaty with her."
    scene ae882 with dssa
    d "...Fuck it. I'll break it."
    stop music fadeout 2.0
    scene ae883 with dssb
    pause
    $ play_playlist(playlist_Ch4x5)
    scene ae884 with dssa
    d "There they are..."
    scene ae885 with dssb
    d "I'll put you down here."
    scene ae798 with dssb
    n "And then my trebuchets killed Nia's last fort... It was brutal!"
    scene ae799 with vpunch
    pause
    scene ae800 with vpunch
    "Nami enters a state of shock. No sound leaves her body."
    scene ae801 with vpunch
    "Nami makes a very weird, whistling sound."
    scene ae888 with vpunch
    n "Y-you BROKE THE PEACE!"
    scene ae886 with dssb
    n "You just made the biggest mistake of your life!"
    scene ae887 with dssa
    d "Sorry, not sorry."
    scene ae807 with dssb
    n "Oh... You will be."
    $ fitness +=1
    $ persistent.unlockedImageRLWSVic4x5 = True
    jump Ch4x5NachtPart3

label CheetoWalk4x5:
    $ persistent.unlockedImageR8 = True
    $ play_playlist(playlist_Crossroads)
    scene ae889 with dssb
    pause
    scene ae890 with dssr
    pause
    scene ae891 with dssa
    n "It's still so warm... I'm all sweaty."
    scene ae893 with dssa
    d "Let's not talk too much or I'll have to send you back inside."
    scene ae892 with dssa
    n "Wanna check out the area?"
    scene ae894 with dssr
    d "Let's go up there. Check out the forest."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae895 with dssb
    pause
    scene ae896 with dssb
    pause
    if Foursome4x5 is True:
        if BellaKiss3x5 is True:
            $ McPa +=2
            scene ae898 with dssa
            pause
            scene ae899 with dssa
            n "...So uhhh... Bella."
            scene ae902 with dssa
            "You shoot Nami a look... A clear display of you trying to avoid a conversation that will go nowhere."
            scene ae903 with dssa
            n "You and her are quite close... and as Mila said... it's kinda weird that you did this here with her still being in the picture."
            scene ae904 with dssa
            d "I don't know what I want, Nami."
            scene ae905 with dssa
            n "I'm not judging you..."
            scene ae906 with dssa
            pause
            scene ae907 with dssa
            n "But please keep in mind that a relationship that was formed on, quotation marks 'Betrayal', has a looming shadow over it."
            n "Just so that Vic or Mila don't get the wrong idea."
            scene ae908 with dssa
            d "You care too much about what other people think."
            scene ae909 with dssa
            n "I care about what friends think... and so should you."
            scene ae910 with dssa
            pause
            scene ae909 with dssa
            n "At least you should care about treating them well."
        else:
            $ McPa +=1
            scene ae897 with dssa
            pause
            scene ae900 with dssa
            n "It's funny how you're just you right now..."
            scene ae901 with dssa
            d "What? Did you have a stroke?"
            scene ae900 with dssa
            n "I mean... you just made out with two extremely attractive girls at once... I mean, of course you didn't get the third hot girl there..."
            scene ae902 with dssa
            d "I think the third one looked kind of weird."
            scene ae900 with vpunch
            n "You take that back!"
            scene ae905 with dssa
            n "But as I was saying... You just act like nothing happened."
    scene ae911 with dssb
    n "How's therapy going?"
    n "What do you guys talk about?"
    d "Summer... My past... Stuff like that."
    d "I've only had two sessions..."
    n "I see."
    stop music fadeout 2.0
    scene ae912 with dssb
    n "It's good that you're opening up."
    $ play_playlist(playlist_WatchingStars)
    scene ae913 with dssb
    pause
    scene ae914 with dssa
    d "...Right."
    scene ae915 with dssa
    n "What?"
    scene ae916 with dssa
    d "I have to- yeah, I have to break our deal."
    scene ae917 with dssa
    n "Which one? The one where we don't scare each other anymore?"
    scene ae916 with dssa
    d "No."
    d "The... The deal we made a long time ago."
    scene ae918 with dssa
    "Nami's face turns pale and she takes on a very weird posture."
    n "*Gulp*"
    scene ae919 with dssa
    n "Is that really necessary?"
    scene ae920 with dssa
    "You stand there for a moment, your mouth a little agape and unsure what to say."
    scene ae921 with dssb
    d "I lied to Amber... You are... You are partly responsible for the way I am."
    scene ae922 with dssa
    n "We- [name]... But it shouldn't matter what happened?"
    scene ae921 with dssa
    d "Nami... Try to understand that these things don't just vanish... They still affect me... They're a reason for my lack of impulse control."
    d "And I get the feeling, that all you do is an overcompensation... To make up for-"
    scene ae923 with vpunch
    n "It's not!"
    scene ae924 with dssb
    "You squat down"
    pause
    d "I hope it's not."
    scene ae925 with dssa
    n "It really isn't..."
    scene ae926 with dssa
    pause
    scene ae927 with dssa
    n "But if it helps... Talk about it with her."
    n "You know I would never be like that again."
    scene ae928 with dssa
    d "I know."
    scene ae929 with dssa
    n "And, and if Amber wants me there for a session, I would do it."
    scene ae930 with dssb
    pause
    scene ae931 with dssa
    pause
    if KoFuNa is True:
        scene ae932 with dssa
        pause
    scene ae933 with dssb
    pause
    scene ae934 with dssa
    d "I shouldn't have lied to Amber."
    d "I thought I could alter a few details and still get all the benefits..."
    scene ae935 with dssb
    d "But it's about more than just telling her things... It's about *sigh*... coming clean with myself..."
    scene ae936 with dssa
    n "As long as you don't come to a... weird conclusion."
    scene ae935 with dssa
    pause#
    scene ae937 with dssb
    d "Let's not totally ruin the mood."
    scene ae938 with dssb
    pause
    d "Sometimes I... I don't know if it was a dream or an actual memory."
    d "...I hear my mother reading to me... Whenever I sit down and look up to the stars I can recall it."
    d "I think the book she read to me was about the universe."
    d "But... I don't know if it actually happened or not."
    n "I remember something similar with my mom."
    d "I love Nojiko."
    n "So do I."
    d "I just sometimes wish I could've gotten to know my parents."
    n "...I used to cry at night about it..."
    d "Noji's working all day long to support us."
    d "I can see it in her eyes how much she hates working at the hospital... The hours and the stress really get to her."
    d "I wish I could help her fulfill her dream of opening her own little doctor's office."
    scene ae939 with dssr
    n "We will help her achieve that dream!"
    pause
    scene ae940 with vpunch
    n "YO!"
    "You twitch."
    n "A mosquito wanted to slurp me! You want some, mosquito?!"
    scene ae941 with vpunch
    n "Come here and get yaself some!"
    scene ae942 with dssa
    n "Yeah! That's what I thought! Bibiquito!"
    d "*Chuckle* Just shut up..."
    if NamiTni4x0 or NamiCuddle04 and NUE04 is True:
        scene ae943 with dssb
        d "(...I'm looking at her butt.)"
        scene ae944 with dssa
        d "(Since when do I do this?)"
        scene ae945 with dssa
        with Pause(.2)
        menu:
            "Slap her butt.":
                $ Cheeto_Butt_Slap_4x5 = True
                scene ae946 with dssa
                with Pause(.2)
                scene ae947 with vpunch
                pause
                scene ae955 with dssr
                n "Yo! Did you just slap my butt?"
                scene ae948 with vpunch
                "You slap her butt again."
                scene ae949 with dssa
                n "Do it again! I dare you!"
                menu:
                    "Do it again.":
                        $ Cheeto_Butt_Slap2_4x5 = True
                        scene ae950 with vpunch
                        pause
                        scene ae951 with dssr
                        pause
                        n "Do it again! I dare you!"
                        menu:
                            "Do it again.":
                                $ Cheeto_Butt_Slap3_4x5 = True
                                $ persistent.unlockedImageNamiCh4x546 = True
                                scene ae952 with vpunch
                                pause
                                scene ae954 with dssb
                                n "You actually did it."
                                scene ae957 with dssa
                                d "..."
                            "Don't do it again.":
                                scene ae953 with vpunch
                                n "Little chicken bibi!"
                    "Don't do it again.":
                        scene ae953 with vpunch
                        n "Little chicken!"
            "Don't do it.":
                pass
    scene ae958 with dssb
    pause
    scene ae959 with dssa
    pause
    scene ae960 with dssa
    pause
    scene ae961 with dssa
    d "What?"
    n "It's nice up here."
    scene ae963 with dssa
    d "Yeah."
    scene ae962 with dssa
    n "We should go on a hike someday."
    scene ae963 with dssa
    d "Stop adding stuff to my plate."
    scene ae964 with dssa
    n "Oh damn! Right, right!"
    scene ae965 with dssa
    pause
    menu:
        "Pull her closer.":
            $ persistent.unlockedImageNamiCh4x547 = True
            $ Nami_TNI_4x5 = True
            scene ae966 with dssr
            pause
            scene ae967 with dssr
            pause
            d "(Why does it feel so right...)"
            scene ae968 with dssa
            "Her little nose pokes yours, as her face approaches yours."
            scene ae969 with dssa
            "You gather all the sanity that's left in yourself to create some distance."
        "Don't pull her closer.":
            pass
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae970 with dssb
    pause
    scene ae971 with dssa
    d "Let's go back."
    scene ae972 with dssa
    n "Yes... I'm getting sleepy."
    scene ae973 with dssb
    stop music fadeout 2.0
    pause
    $ achievement.grant("WatchingStarsNami")
    $ achievement.sync()
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch4x5)
    jump Ch4x5NachtPart3








label Ch4x5NachtPart3:
    scene ae974 with dssb
    pause
    scene ae975 with dssb
    n "By the way... Where do [name] and I sleep?"
    scene ae982 with dssb
    mi "We thought about building a fort out of blankies and pillows."
    scene ae976 with vpunch
    n "Oh yes!"
    n "Remember dude?!"
    scene ae977 with dssa
    d "...I remember our forts."
    scene ae976 with dssa
    n "And, and we pretended that Moogle was our boss and gave us quests."
    scene ae979 with dssb
    v "What's a Moogle?"
    mi "A person who's not a wizard."
    d "It was a street cat... We used to play with it and it followed us everywhere."
    scene ae978 with dssr
    n "I wonder if Moogle's still alive..."
    n "Noji still has that cat tree she bought for him."
    scene ae980 with dssb
    v "I'm getting really tired..."
    scene ae981 with dssr
    n "Me too... It's been a long day."
    scene ae982 with vpunch
    mi "Time to build a fort!"
    scene ae983 with dssb
    mi "I'll get the pillows!"
    pause
    scene ae984 with dssr
    d "Cheeto, I need a hand."
    scene ae985 with dssr
    pause
    scene ae986 with vpunch
    pause
    scene ae987 with dssr
    v "Hey!"
    scene ae988 with dssr
    pause
    scene ae989 with vpunch
    pause
    scene ae990 with vpunch
    n "You're gonna pay for that!"
    if MilaKiss4x5 is True:
        $ McPa +=1
        scene ae991 with dssb
        pause
        scene ae992 with dssb
    n "Yo Mila! Where are you? I need your help beating up Vic with a pillow!"
    scene ae993 with dssr
    d "Cheeto, get your ass moving and get us some blankets."
    scene ae994 with dssr
    mi "Come Nami! I'll need help finding the blankies."
    scene ae995 with dssr
    pause
    if VicTiddyTease4x5 is True:
        $ McPa +=1
        scene ae996 with dssr
        pause
        scene ae997 with dssa
        d "I'm trying to build a fort here."
        scene ae998 with dssa
        v "And I'm trying to keep you from it!"
        scene ae999 with dssa
        "She kisses your forehead."
        scene ae1000 with dssa
        pause
        scene ae1001 with vpunch
        n "Hey you jerks!"
        n "Stop making out while we do all the work!"
        scene ae995 with dssr
        pause
    else:
        pass
    scene ae1003 with dssr
    pause
    scene ae1002 with dssa
    pause
    scene ae1004 with dssb
    mi "Get in!"
    d "I need to use the restroom."
    scene ae1005 with dssa
    mi "What're you doing, Nami?"
    scene ae1006 with dssa
    n "I miscalculated! I thought I could turn around in here but NO! Now I'm stuck in here forever!"
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    if BellaKiss3x5 and Foursome4x5 or VictoriaKiss4x5 or MilaKiss4x5 is True or McPa >1 or Foursome4x5 is True:
        play music "music/Suspense/A.W - Darkness Inside.ogg"
        $ McPa -=2
        $ Mc_Panic4x5 = True
        scene ae1109 with dssb
        pause
        scene ae1110 with dssb
        pause
        scene ae1111 with dssb
        pause
        scene ae1112 with dssa
        "Your breathing accelerates."
        scene ae1113 with dssr
        "Sweat breaks out."
        scene ae1114 with dssr
        "You gasp for air..."
        scene ae1115 with dssa
        "Your heart pounds through your chest."
        scene ae1117 with dssa
        pause
        scene ae1118 with dssa
        d "(Come on... Calm down... calm down... please...)"
        scene ae1119 with dssa
        d "(Not now...)"
        scene ae1120 with dssb
        pause
        scene ae1121 with dssb
        "You manage to calm your heart rate down."
        scene ae1122 with dssb
        d "(It'll stop... I just have to get through this...)"
        scene black with Dissolve(2)
        with Pause(.5)
        show text "You freshen up, and go back to the others." with dissolve
        stop music fadeout 3.0
        with Pause(2.5)
    $ play_playlist(playlist_BigTiddyMila)
    scene ae1007 with dssb
    d "Why are there clothes here?"
    scene ae1008 with dssa
    mi "Well... sleeping with clothes, in a more or less airtight and body filled fort is gonna suck."
    scene ae1009 with dssa
    v "It'll get really warm."
    scene ae1010 with dssa
    d "You guys still have clothes on... right?"
    scene ae1013 with dssa
    n "Underwear."
    scene ae1012 with dssa
    d "I might take the couch."
    scene ae1014 with vpunch
    mi "No way."
    scene ae1011 with dssr
    v "You'll get in here! It's a fort for us all!"
    scene ae1015 with dssr
    pause
    scene ae1016 with dssa
    d "Alright... I don't see an entrance."
    scene ae1017 with dssa
    mi "Nami, can you make some space?"
    scene ae1018 with dssa
    $ persistent.unlockedImageMilaCh4x518 = True
    n "S-sure."
    scene ae1019 with dssb
    pause
    d "I'm glad there's enough space here..."
    scene ae1020 with dssa
    d "... I guess that does it."
    scene ae1021 with dssa
    v "It really does..."
    scene ae1022 with dssa
    d "You're not wearing a bra?"
    scene ae1023 with dssa
    v "I'm wearing a strapless one."
    v "I can take it off if you want?"
    scene ae1022 with dssa
    d "No, no."
    scene ae1024 with dssb
    n "I'm not wearing one."
    menu:
        "Tiddy-Joke.":
            $ NTJ +=1
            scene ae1025 with dssa
            d "I mean... Why would you? There isn't much to fall out."
            scene ae1034 with vpunch
            n "WOW! YOU- WOW!"
            n "YOU SUCK!"
            scene ae1035 with dssa
            mi "You're so mean!"
            mi "Her breasts are amazing!"
            scene ae1034 with vpunch
            n "Tell him!"
            scene ae1038 with dssr
            v "That's soooo mean, [name]!"
            scene ae1039 with dssa
            d "I'm obviously joking... partially."
            scene ae1024 with vpunch
            n "I will make you eat your words one day!"
            scene ae1037 with dssa
            n "Or my tits!"
            scene ae1036 with dssa
            mi "*Laughs* Nami!"
        "Don't joke on Nami's expense.":
            $ Nami_SB +=1
            scene ae1025 with dssa
            d "You don't need to."
            n "...Why is that?"
            d "You've got some very good connective tissue."
            scene ae1027 with dssa
            "Nami squints her eyes even further..."
            scene ae1028 with dssa
            n "Thanks!"
            scene ae1029 with dssa
            mi "And here I am with just decent tissue."
            scene ae1030 with dssa
            n "Yeah but your tits are also gigantic!"
            scene ae1031 with dssa
            v "Much bigger than mine!"
            scene ae1032 with dssa
            mi "I don't think so... Yours are pretty big."
            scene ae1033 with dssa
            v "Yours are sooo much bigger."
            scene ae1029 with dssr
            mi "Hmm,  maybe a little."
    scene ae1046 with dssb
    n "I wonder how Summer's breasts would be..."
    scene ae1047 with dssa
    d "She started developing some... breasts when we last saw each other."
    scene ae1046 with dssa
    n "I bet she was also blessed by the boob gods."
    scene ae1044 with dssr
    v "Just like Bella."
    scene ae1048 with dssr
    $ persistent.unlockedImageVicCh4x67 = True
    n "They're not that great."
    scene ae1049 with dssa
    mi "Her tits are quite nice."
    scene ae1051 with dssa
    n "Come on girl... Back me up here..."
    scene ae1050 with dssa
    mi "Sorry hun."
    scene ae1042 with dssa
    v "I really want to get to know Bella."
    d "I also want you to get to know each other."
    mi "Why would you want that?"
    scene ae1041 with dssa
    d "Bella's a jerk, but she isn't two-faced."
    d "You and Bella would be great together too. If it wasn't for your history."
    scene ae1042 with dssa
    v "What isn't can still be!"
    v "I'll talk to her."
    scene ae1043 with dssr
    mi "Vic..."
    scene ae1052 with dssb
    mi "You can hang out with Bella... but Bella and I will never be friends."
    scene ae1053 with dssb
    v "If I can learn to walk again... then you can become friends with Bella."
    scene ae1054 with dssa
    mi "I don't want to become friends with her."
    scene ae1055 with dssb
    n "Anyways... Nadia."
    scene ae1056 with dssa
    mi "What about her?"
    scene ae1057 with dssa
    n "I like her."
    n "She's coming to my place soon for some gaming adventures."
    scene ae1058 with dssr
    mi "I like her too."
    mi "She can be a little weird at times but overall she's a nice girl."
    scene ae1045 with dssa
    v "Why is she weird?"
    scene ae1059 with dssb
    mi "She is uhh... a little too much into fantasy."
    scene ae1060 with dssa
    n "I like that about her."
    scene ae1061 with dssr
    mi "I was once at one of Nancy's parties and-"
    n "OH! We got invited to one."
    scene ae1062 with dssr
    mi "Be careful... It can get really weird real fast."
    scene ae1063 with dssr
    n "Why?"
    scene ae1064 with dssa
    mi "It's almost always just girls there... and it can turn 'weird' real fast."
    mi "If you're going there, [name]... You'd better be prepared."
    mi "It's like a bunch of horny farm girls."
    scene ae1065 with dssr
    n "Oh."
    n "But [name] didn't want to go anyways."
    scene ae1066 with dssa
    d "(She doesn't want me to go now...)"
    menu:
        "I'll go.":
            $ NancyParty4x5 = True
            scene ae1068 with dssa
            n "What? I thought you didn't want to?"
            scene ae1067 with dssa
            d "But Nancy asked me and I want to give it a try."
            scene ae1068 with dssa
            n "There will be other parties we can go to."
            scene ae1070 with dssa
            n "What Mila describes sounds stressful."
            scene ae1066 with dssa
            d "Hey, don't worry..."
            d "You can stay home and I'll go alone."
            scene ae1069 with dssa
            pause
            scene ae1068 with dssa
            n "...No."
            scene ae1071 with dssb
            mi "I mean... We can also go Vic?"
            scene ae1073 with dssa
            v "But- my chair won't be able to drive."
            scene ae1072 with dssb
            if vicdate is True:
                mi "I'm sure [name] will carry you around."
                v "Yay!"
            else:
                mi "I'm sure we'll find some hot farm boy to carry you around."
                v "*Giggles*"
        "Right, I didn't.":
            $ NancyParty4x5 = True
            scene ae1071 with dssb
            mi "If you decide to go... Vic and I might also come."
            scene ae1073 with dssa
            v "Yay!"
            v "But- my chair won't be able to drive."
            scene ae1072 with dssa
            if vicdate is True:
                mi "I'm sure [name] will carry you around."
                v "Yay!"
            else:
                mi "I'm sure we'll find some hot farm boy to carry you around."
                v "*Giggles*"
    scene ae1074 with dssb
    d "Can we sleep now?"
    if NiaDeal is True:
        d "I have to see Nia tomorr- today."
    scene ae1076 with dssa
    v "Alrighty!"
    scene ae1077 with dssb
    pause
    stop music fadeout 3.0
    jump Morning4x5




label Morning4x5:
    scene ae1078 with Dissolve(3.5)
    play music "music/SFX/ParkNature.ogg"
    pause
    scene ae1079 with dssb
    pause
    scene ae1080 with dssa
    pause
    scene ae1081 with dssr
    v "*Whisper* [name]?"
    d "Mhh?"
    v "*Whisper* I need to pee."
    scene ae1082 with dssr
    d "Should I wake up Mila?"
    v "You could also help me?"
    if UmB is True:
        scene ae1083 with dssb
    else:
        scene ae1083a with dssb
    pause
    scene black with Dissolve(2)
    if UmB is True:
        scene ae1084 with dssb
    else:
        scene ae1084a with dssb
    pause
    if UmB is True:
        scene ae1085 with dssb
    else:
        scene ae1085a with dssb
    pause
    scene ae1086 with dssb
    d "Do I just put you on there?"
    $ persistent.unlockedImageRS61 = True
    v "Yes, but you'll need to stabilize me at the beginning..."
    scene ae1087 with dssb
    v "And help me pull down my shorts."
    scene ae1088 with dssb
    pause
    scene ae1089 with dssb
    d "You'll need to get up again... Lean yourself on me and I'll pull them down."
    scene ae1090 with dssb
    "Victoria leans over your shoulder."
    pause
    scene ae1091 with dssa
    pause
    scene ae1094 with dssr
    "You put her back on the throne."
    scene ae1095 with dssb
    d "I like your confidence."
    scene ae1096 with dssa
    v "Is it confidence, though?"
    v "Or is it just me not caring anymore."
    scene ae1097 with dssb
    d "I think it's a mix between those two."
    scene ae1098 with dssa
    pause
    scene ae1099 with dssa
    d "Can you-"
    v "Yes, I can do it myself."
    scene ae1100 with dssb
    "Victoria cleans herself up."
    pause
    scene ae1101 with dssb
    pause
    scene ae1102 with dssb
    pause
    scene ae1103 with dssa
    pause
    scene ae1104 with dssa
    v "What're you thinking about?"
    scene ae1105 with dssa
    d "Nothing really."
    scene ae1103 with dssr
    pause
    if UmB is True:
        scene ae1106 with dssr
    else:
        scene ae1106a with dssr
    d "Ready?"
    if UmB is True:
        scene ae1107 with dssr
    else:
        scene ae1107a with dssr
    v "Yes!"
    scene ae1108 with dssb
    pause
    stop music fadeout 3.0
    scene ae1123 with dssb
    $ persistent.unlockedImageVicCh4x68 = True
    "You carry Victoria backwards outside the bathroom to close the door."
    $ play_playlist(playlist_Ch1Vic)
    scene ae1124 with dssr
    pause
    scene ae1125 with dssr
    v "Maja!"
    scene ae1126 with dssa
    maj "Hi honey."
    scene ae1127 with dssa
    v "You're back early!"
    scene ae1126 with dssa
    maj "I am."
    scene ae1127 with dssa
    v "What happened? Why are you back?"
    scene ae1128 with dssa
    maj "We all change as time goes on... The connection we once had was gone."
    scene ae1129 with dssb
    d "I need to pee. Would you mind taking her off my arms?"
    scene ae1130 with dssa
    maj "Sure."
    scene black with Dissolve(2)
    with Pause(.5)
    if UmB is True:
        scene ae1131 with dssb
    else:
        scene ae1131a with dssb
    "You leave the restroom a few minutes later."
    scene ae1132 with vpunch
    maj "You fucking creep."
    d "What?"
    $ persistent.unlockedImageMaja2 = True
    scene ae1133 with dssb
    maj "You went through my stuff."
    scene ae1134 with dssa
    d "The others did."
    scene ae1133 with dssa
    maj "Okay."
    if UmB is True:
        scene ae1135 with dssb
    else:
        scene ae1135a with dssb
    d "You believe me? Just like that?"
    if UmB is True:
        scene ae1136 with dssa
    else:
        scene ae1136a with dssa
    maj "Yeah... You're not the type for that."
    scene ae1137 with dssb
    maj "I know how girls can be when they get together in a group."
    maj "We get darey whenever friends are around... Be careful when big groups of girls get together."
    if Foursome4x5 is True:
        scene ae544 with pixellate
        d "...I can imagine."
    else:
        scene ae1138 with dssa
        pause
    scene ae1137 with dssa
    maj "Did you arrive with Mila?"
    scene ae1138 with dssa
    d "No, Nami and I arrived later at night."
    scene ae1139 with dssa
    pause
    scene ae1140 with dssb
    maj "You look different."
    d "Different how?"
    maj "More alive."
    maj "The first time I saw you... you looked awful. Kind of psychotic and dead inside."
    scene ae1141 with dssb
    maj "Don't get me wrong, you still look dead and psycho."
    maj "But not as much anymore."
    maj "I think it's the influence Victoria has on other people."
    scene ae1142 with dssa
    d "I won't deny that Vic has an influence on me... But you won't change without wanting so yourself."
    if BellaKiss3x5 is True:
        $ MajaBellaIn4x5 = True
        d "And... I think this is more Bella's doing than Victoria's."
        scene ae1143 with dssa
        maj "Bella?"
        d "Yeah."
    else:
        scene ae1141 with dssa
        maj "That's great to hear."
    pause
    if MCNipplePump is True:
        $ MajaFetishBDSM = True
        scene ae1144 with dssa
        pause
        scene ae1145 with dssa
        maj "Wait a minute!"
        scene ae1146 with dssr
        maj "Did you use my nipple pump?"
        scene ae1147 with dssa
        d "They made me do it."
        scene ae1148 with vpunch
        maj "You fucking spastics!"
        "Maja squeezes your nipple slightly between her two fingers."
        maj "Now I have to throw them away!"
        maj "I swear if I find out one of my toys entered you I-"
        scene ae1150 with vpunch
        d "What no?! No toy entered me!"
        scene ae1149 with dssb
        maj "I hope you're telling me the truth, otherwise I'll make you suffer."
        scene ae1150 with dssa
        d "...How?"
        scene ae1149 with dssa
        maj "Tie you up and make you squeal."
        scene ae1151 with vpunch
        d "Is that your fetish?"
        scene ae1152 with dssr
        maj "My- what? Dude? You can't just ask me that?"
        d "Why not? You just said you would tie me up."
        maj "Yeah, but I am a girl?! You don't ask a girl that!"
        d "I believe in real equality."
        scene ae1153 with dssb
        maj "...It's not my fetish but I like bondage and some soft BDSM."
        d "So it's safe to assume we didn't see your full collection."
        scene ae1154 with dssa
        maj "*chuckles* Not even half."
        scene ae1155 with dssb
        d "Don't tell them or they will try to find it."
        scene ae1156 with dssa
        maj "Those weirdos..."
        scene ae1157 with dssa
        d "They've got no respect."
    else:
        scene ae1154 with dssb
        pause
    scene ae1158 with dssa
    n "Morning!"
    d "Morning."
    scene ae1160 with dssb
    maj "Hello Nami."
    scene ae1159 with dssa
    $ persistent.unlockedImageNamiCh4x548 = True
    n "Huh! Maja!"
    n "It's great to see you!"
    n "How are you?"
    scene ae1160 with dssa
    maj "I am fine and you?"
    scene ae1161 with dssa
    n "I'm good!"
    n "Do we have some coffee?"
    maj "I'll pour some."
    scene ae1162 with dssr
    n "[name], yo!"
    if NiaDeal is True:
        $ MajaJoke4x5 = True
        scene ae1163 with dssa
        d "I'm thinking about canceling Nia."
        scene ae1164 with dssa
        n "You won't."
        scene ae1165 with dssa
        d "I won't... I gave her my word."
        scene ae1166 with dssa
        n "Use a condom, though."
        scene ae1167 with dssb
        d "We do have something in common Maja."
        d "We both have a disabled roommate."
        scene ae1168 with vpunch
        n "Wow! Cheap shot!"
    else:
        scene ae1163 with dssa
        d "Cheeto."
    $ persistent.unlockedImageMaja2 = True
    scene ae1169 with dssb
    mi "Good morning!"
    scene ae1170 with dssa
    maj "Morning Mila!"
    scene ae1171 with dssb
    pause
    scene ae1172 with dssa
    mi "Should we all have breakfast together?"
    scene ae1173 with dssb
    n "Sure!"
    scene ae1174 with dssa
    d "Where's Vic?"
    mi "In the living room."
    scene ae1175 with dssa
    d "I'll get her."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae1288 with dssb
    d "Hey, do you want me to carry you over?"
    scene ae1289 with dssb
    v "Yes."
    v "Everyone left and well... I couldn't follow."
    scene ae1290 with dssb
    pause
    d "Let me put your top on."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae1176 with dssb
    pause
    scene ae1177 with dssr
    maj "You look beautiful."
    scene ae1178 with dssa
    v "That's your doing!"
    scene ae1179 with dssa
    maj "Alright... Who'll go with me to the bakery?"
    scene ae1180 with dssa
    v "Me!"
    scene ae1181 with dssa
    n "Me too! I need some fresh air."
    n "And I need to inspect their selection of rolls."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Chapter1a)
    scene ae1182 with dssb
    pause
    scene ae1183 with dssr
    pause
    scene ae1184 with dssr
    mi "Thanks."
    scene ae1185 with dssb
    mi "Have you seen Miss Marla lately?"
    scene ae1186 with dssb
    d "Why?"
    scene ae1185 with dssa
    mi "She changed her hair and style. It looks nice on her."
    scene ae1186 with dssa
    d "I guess."
    scene ae1185 with dssa
    mi "Maybe it was due to the talk she had with Vic."
    scene ae1186 with dssa
    d "They had a talk?"
    scene ae1185 with dssa
    mi "Yes. Three days ago."
    if mmc is True:
        scene ae1188 with dssb
        pause
        scene ae1189 with dssa
        d "Did she say how it went?"
        scene ae1190 with dssa
        mi "Vic said it went well."
        scene ae1191 with dssa
        d "(Marla didn't look so great... I wonder if it was because of the talk.)"
        scene m1152 with pixellate
        pause
        d "(Amber must know... I'm sure Marla told her about it.)"
        d "(Bella could help me take a look at the files... It'd be interesting to see what they actually talked about.)"
        scene ae1192 with dssa
        d "I see."
    else:
        scene ae1192 with dssa
        d "That's nice, I guess."
    scene ae1194 with dssb
    mi "I respect Victoria for actively engaging with her."
    mi "You can't tell me that it's easy..."
    scene ae1193 with dssa
    d "It isn't."
    if MilaKissBreak4x5 is True and Foursome4x5 is False:
        scene ae1195 with dssa
        mi "I wanted to apologize for... kissing you."
        scene ae1196 with dssa
        d "No hard feelings... It just felt really wrong."
        scene ae1195 with dssa
        mi "*Sigh* Sorry."
        d "Why did you do it?"
        scene ae1195 with dssr
        mi "It just felt... right?"
        scene ae1195 with dssr
        d "No... There was something in the air since you heard about Bella and me."
        scene ae1201 with dssr
        d "Your body language has changed."
        scene ae1202 with dssa
        mi "It's nothing [name]... I was just stupid."
        "You raise a brow and take a sip from your coffee."
    elif MilaKiss4x5 is True:
        scene ae1198 with dssa
        mi "I liked our kiss."
        if BellaKiss3x5 is True:
            $ MiEH4x5 = True
            scene ae1197 with dssa
            d "I would've too if there wasn't this underlying feeling."
            scene ae1195 with dssa
            mi "... What do you mean?"
            scene ae1200 with dssa
            d "Since you heard about me and Bella... Your body language towards me has changed."
            d "It's in some way aggressive."
            scene ae1195 with dssa
            mi "Oh- uh... I didn't mean to come across like that."
            scene ae1196 with dssa
            d "But you did."
            scene ae1200a with vpunch
            mi "Is it so bad to not always be the one left empty handed? The one that always watches from the sidelines?!"
            scene ae1201 with dssa
            pause
            scene ae1202 with dssa
            mi "...Sorry."
            d "It's alright. I can imagine."
        else:
            scene ae1197 with dssa
            d "I liked it too."
            d "I would've preferred waiting for it to happen on our date..."
            mi "No no Mister... You don't always need to be in control."
            mi "Sometimes it's best to go with the flow."
            scene ae1200 with dssa
            d "It reminds of our first talk... Going with the flow has made you not approach the girl."
            scene ae1195 with dssa
            mi "...I was talking about 'love' related things."
            scene ae1201 with dssr
            d "And what you did was not 'going with the flow'. You took action."
            d "I respect that very much."
            mi "You really need to work on that."
            scene ae1202 with dssa
            d "Not as hard as your bra."
            scene ae1203 with vpunch
            mi "Wow!"
            scene ae1204 with dssr
            d "Hey, it could've been a compliment about your well developed breasts."
            mi "It sounded a lot like you were calling my boobs saggy!"
            d "I didn't mean that. I haven't seen them yet."
            scene ae1205 with dssa
            mi "*Smirks* Who says you ever will?"
    elif Foursome4x5 is True:
        scene ae1206 with dssb
        mi "I'm still in denial about last night."
        scene ae1207 with dssa
        d "It's not like much happened."
        d "It was just kissing."
        scene ae1208 with dssa
        mi "And touching... Lots of touching."
        scene ae1209 with dssb
        d "It was just in the spur of the moment."
        scene ae1210 with dssa
        mi "Right."
    scene ae1209 with dssr
    pause
    stop music fadeout 2.0
    d "They're taking their sweet time."
    if MilaKiss4x5 is True:
        $ persistent.unlockedImageR9 = True
        $ play_playlist(playlist_Crossroads2)
        scene ae1211 with dssb
        pause
        scene ae1212 with dssr
        pause
        scene ae1213 with dssa
        pause
        scene ae1214 with dssb
        pause
        scene ae1215 with dssr
        "She takes the mug out of your hand."
        scene ae1216 with dssb
        pause
        scene ae1217 with dssr
        pause
        scene ae1218 with dssr
        "She stares into your soul."
        scene ae1219 with dssb
        pause
        scene ae1220 with dssr
        mi "Tell me if I'm too heavy."
        scene ae1221 with dssr
        d "You're not."
        scene ae1222 with dssr
        "Mila closes in... Her nose slightly touching yours."
        scene ae1223 with dssr
        "She moves in closer, stops and creates a drumroll."
        scene ae1224 with dssr
        pause
        scene ae1225 with dssr
        "Mila guides your hand to her breast."
        scene ae1226 with dssa
        pause
        scene ae1228 with dssr
        "She disconnects the kiss."
        scene ae1227 with dssa
        mi "More coffee?"
        scene ae1228 with dssa
        d "Yeah."
        scene ae1229 with dssr
        "As Mila gets up, she 'accidentally' moves your head between her breasts."
        scene ae1230 with dssr
        pause
        scene ae1231 with dssr
        d "Huh."
        scene ae1232 with dssr
        mi "What?"
        d "I took a peek at your butt."
        scene ae1233 with dssa
        $ persistent.unlockedImageMilaCh4x520 = True
        mi "I never thought I'd be happy to hear those words... But here I am!"
        if milagym is True:
            scene ae1232 with dssa
            d "Actually... I also looked at it before when your pants ripped at the gym."
            scene ae1234 with dssa
            mi "Fuck... I hope you'll forget about it soon."
            scene ae1235 with dssa
            d "I'll never forget anything... Especially not potential blackmail material."
            scene ae1236 with dssa
            mi "HEY!"
            "You chuckle."
    else:
        scene ae1209 with dssa
        d "Probably Nami's fault."
        d "It takes ages for her to decide on the right rolls."
    $ persistent.unlockedImageMilaCh4x519 = True
    stop music fadeout 2.0
    if bellagym is True:
        $ BibiBellchen4x5 = True
        scene ae1237 with dssb
        d "Bella once mentioned that you did something to her... What was it?"
        $ play_playlist(playlist_AmbientBellchen)
        scene ae1238 with dssa
        pause
        scene ae1239 with dssb
        "Mila freezes."
        scene ae1240 with dssa
        mi "Uhh..."
        scene ae1241 with dssr
        mi "*sigh*"
        scene ae1242 with dssa
        mi "In middle school..."
        mi "Bella was kind of an outsider... Like me."
        mi "But we didn't speak or have anything to do with each other."
        scene ae1243 with dssb
        mi "And as you know, I was being bullied for being poor... and some other things."
        scene ae1244 with dssb
        mi "And I did something really horrible."
        scene ae1245 with dssb
        d "You joined them..."
        scene ae1246 with dssa
        mi "I said something mean..."
        mi "I was a little child... And if they bullied Bella they would stop bullying me, right?"
        mi "It made me feel like I was part of a group... But most importantly, it took me out of the crosshair."
        scene ae1247 with dssa
        mi "But it didn't go on for long."
        scene ae1271 with dssb
        mi "One day during lunch..."
        scene ae1272a with dssb
        mi "She sat there at the table with her little milk."
        $ persistent.unlockedImageBellaCh47 = True
        $ persistent.unlockedImageRS63 = True
        scene ae1272 with dssb
        pause
        scene ae1273 with dssa
        pause
        scene ae1274 with dssa
        pause
        mi "And Melanie picked on Bella because Amber complained about her to the school."
        scene ae1275 with vpunch
        pause
        scene ae1276 with dssb
        mi "And Melanie threw herself onto her back and Bella hit the table really hard..."
        scene ae1277 with dssb
        pause
        scene ae1278 with vpunch
        mi "She pulled her hair and made her fall from the chair."
        scene ae1279 with vpunch
        pause
        scene ae1280 with dssb
        mi "She started crying so much..."
        scene ae1281 with vpunch
        pause
        scene ae1282 with dssb
        mi "It broke my heart..."
        scene ae1283 with dssr
        pause
        scene ae1284 with dssa
        mi "I took all my pent up frustration, my pain, and all the courage I could muster..."
        scene ae1285 with vpunch
        mi "And stepped in."
        scene ae1286 with vpunch
        mi "Which put me back in the crosshair..."
        scene ae1287 with dssb
        mi "But at least I stood up for my principles..."
        scene ae1248 with dssb
        mi "I apologized to Bella hundreds of times... She never forgave me."
        mi "Bella and I are very different... but we did share a fate in middle school."
        mi "I think if I hadn't wronged her once, we could have become friends."
        scene ae1249 with dssb
        d "The people who picked on her... Was it that Mario guy?"
        scene ae1250 with dssb
        mi "No. He was actually a nice guy back then. He even defended me and Bella sometimes."
        mi "It was mostly just Melanie and her clique."
        d "How come you are so anti-Bella even though you knew what she was going through?"
        scene ae1251 with vpunch
        mi "I'm not anti her!"
        scene ae1252 with dssa
        d "You are."
        d "Recall our first conversations about her."
        scene ae1254 with dssa
        mi "Shit... I think I took it personal that she didn't accept my apology... and that she started to pick on me in high school."
        scene ae1255 with dssb
        mi "Then Bella met Ayua and the tables turned. Ayua was no one to joke with."
        scene ae1256 with dssa
        mi "Just in case you didn't know... Ayua's last name is Zane."
        mi "Main sponsor of our college."
        scene ae1257 with dssb
        d "I'm aware.."
        scene ae1255 with dssa
        mi "When Ayua came into the picture people let off Bella..."
        mi "It also helped that Bella became rather pretty."
        scene ae1258 with dssb
        mi "As you can imagine... Bella then started to pick on the people who picked on her."
        mi "When I say Bella is weird, I mean that she's obsessed with revenge."
        mi "In a very, very unhealthy way."
        scene ae1259 with dssa
        d "What did she do to you?"
        scene ae1260 with dssb
        mi "Besides calling me poor and stuff? Not much."
        mi "But she did do some 'things' to some of the other people that are-"
        scene ae1261 with dssr
        d "Don't tell me."
        d "I'll ask her myself."
        scene ae1262 with dssa
        mi "Yeah, I think that's for the best."
        scene ae1263 with dssr
        d "But... she isn't a bad person... Far from it."
        scene ae1264 with dssa
        mi "...I know."
        menu:
            "Neither are you.":
                $ MNABP4x5 = True
                if MilaKiss4x5 is True:
                    $ persistent.unlockedImageMilaCh4x521 = True
                    $ McPa +=1
                    scene ae1267 with dssr
                    pause
                    scene ae1268 with dssa
                    pause
                    scene ae1269 with dssr
                    pause
                    if UmB is False:
                        scene ae1270 with dssb
                    else:
                        scene ae1270a with dssb
                    pause
                else:
                    scene ae1266 with dssa
                    pause
            "Don't comfort her.":
                $ MTBP4x5 = True
                pass
    stop music fadeout 3.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch4x5)
    scene ae1291 with dssb
    maj "Mh."
    scene ae1292 with dssr
    v "What is it?"
    maj "Mail from ZPR."
    scene ae1293 with dssa
    maj "You also got one."
    scene ae1294 with dssa
    "Maja opens the envelope."
    scene ae1295 with dssa
    maj "Seems like I've got the job."
    scene ae1297 with dssr
    mi "As what?"
    maj "Assistant coach at your college."
    scene ae1298 with dssa
    mi "That's awesome!"
    scene ae1296 with dssr
    maj "I think we'll see each other a little more in the future."
    scene ae1299 with dssb
    "They all look at you."
    scene ae1300 with dssa
    d "Mh? Should I be excited?"
    scene ae1303 with dssa
    v "Yes!"
    scene ae1301 with dssa
    mi "YES!"
    scene ae1302 with vpunch
    n "*Chewing* MHMM!"
    scene ae1300 with dssb
    d "Yay."
    scene ae1304 with dssr
    maj "Vic, drink your juice."
    scene ae1305 with dssa
    v "I will!"
    scene ae1310 with dssr
    maj "Otherwise, I'll tell everyone here about your juice box incident in middle school."
    scene ae1307 with vpunch
    v "Nooo!"
    scene ae1308 with dssa
    pause
    scene ae1309 with dssa
    v "See! I'm drinking it!"
    scene ae1311 with dssb
    n "Want a roll?"
    scene ae1312 with dssa
    d "What?"
    d "You'd never give a roll away."
    scene ae1311 with dssa
    n "I feel generous today!"
    scene ae1314 with dssr
    maj "Thanks for the company guys."
    scene ae1315 with dssr
    maj "I need a really long bath... If I don't see you two when I get out, thanks for keeping Vic company."
    n "Sure!"
    scene ae1316 with dssb
    pause
    scene ae1317 with dssa
    pause
    scene ae1318 with dssr
    d "By the way... You guys fucked up."
    d "Maja knew someone went through her stuff."
    scene ae1319 with dssb
    mi "Oh no..."
    scene ae1320 with dssa
    d "I totally snitched you guys out."
    scene ae1324 with dssr
    n "Wow!"
    scene ae1321 with dssa
    mi "You should've taken the hit!"
    scene ae1322 with dssa
    d "No way I'd take that specific hit."
    d "As a guy, you'd never lose the 'creep' reputation."
    scene ae1325 with dssr
    n "We should apologize next time we see her..."
    if MCNipplePump is True:
        scene ae1323 with dssr
        mi "But it was sooooo funny."
        scene ae1326 with dssr
        v "It was!"
    scene ae1327 with dssr
    d "Alright Cheeto, we should go."
    if NiaDeal is True:
        d "I really need some sleep before I head to Nia."
        scene ae1328 with dssa
        n "Maybe it's better if you don't go."
        scene ae1329 with dssr
        "You raise a brow."
        scene ae1330 with dssa
        n "It could be too much... You're already pushing it."
        d "I'll be fine."
    if VictoriaKiss4x5 is True:
        scene ae1333 with dssa
        d "Vic, it was nice and thanks for the pizza."
    else:
        scene ae1332 with dssa
        d "Vic, it was nice and thanks for the pizza."
    scene ae1334 with dssr
    v "Thanks for coming by! It meant a lot to me."
    scene ae1335 with dssb
    n "Awwww. Goodbye sweety!"
    v "Bye Nami!"
    scene ae1336 with dssa
    if MilaDate is True:
        $ persistent.unlockedImageMilaCh4x522 = True
        d "I think we'll see each other very soon."
        scene ae1337 with dssr
        mi "I hope so."
        scene ae1338 with dssa
        pause
        scene ae1339 with dssr
        pause
        scene ae1340 with dssr
        mi "Don't worry. You'll get used to the touching..."
        mi "But seriously... Let's do something together soon."
        scene ae1341 with dssr
        d "Yeah, I'd like that."
    else:
        d "Bye Mila."
        scene ae1337 with dssr
        mi "Goodbye! Thanks for coming!"
    stop music fadeout 3.0
    scene black with Dissolve(2)
    with Pause(.5)
    jump End4x5

label End4x5:
    $ play_playlist(playlist_AmbientBella)
    scene ae1441 with dssb
    pause
    scene ae1442 with dssr
    "You take a deep breath."
    scene ae1443 with dssa
    n "Those birdies are loud as fuck."
    d "Sounds like you've got a hangover."
    scene ae1444 with vpunch
    n "YOU'll TAKE THAT BACK!"
    scene ae1445 with dssa
    n "I'm invincible! Alcohol WHO?! Am I right?!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae1446 with dssb
    pause
    scene ae1447 with dssa
    n "See, this is how my kind walks."
    scene ae1448 with dssb
    if OeVaGe4x0 and NamiCuddle04 or HcNaFrt or NamiCuddle04 and Nami_TNI_4x5 is True:
        $ persistent.unlockedImageR10 = True
        d "(Hmm...)"
        scene ae1449 with dssb
        d "(Something in my perception has changed.)" #cheeto
        d "(Nami's presence makes me feel comfortable... but this is different.)"
        scene ae1450 with dssr
        d "(I have a slight urge to look at her... A feeling in my belly.)"
        if NamiLove4x0 is True:
            d "(I'm aware that she's probably in love with me...)"
        else:
            d "(I suspect that she's in love with me.)"
        scene ae1451 with dssr
        d "(Do I also have feelings for her?)"
        d "(I'm confused... and overwhelmed.)"
        scene ae1452 with dssa
        n "Man... Carry me home..."
        "Nami's touch sent a shiver through your spine."
        scene ae1453 with dssr
        d "(There's more...)"
        scene ae1454 with vpunch
        n "Yo!"
        scene ae1455 with dssa
        d "Shut up Cheeto."
        d "I'm having an inner monologue."
        scene ae1456 with dssa
        n "About what?"
        scene ae1457 with dssa
        d "Confusion."
        scene ae1458 with dssb
        n "It happens! That roll I gave you wasn't for beginners."
        scene ae1459 with dssa
        d "What makes you think it's about some roll?"
        scene ae1460 with dssa
        pause
        scene ae1461 with dssa
        n "Dude. Life's about rolls!"
        scene ae1462 with dssa
        d "(It's those little things that make her special...)"
        d "(Her stupid humor.)"
        scene ae1463 with dssa
        n "Oh yeah! I can see it on your face!"
        n "You're thinking about rolls, aren't ya?!"
        scene ae1464 with dssa
        d "Yeah, a very special roll."
        scene ae1465 with dssa
        n "Oh! Was it the one with the poppies on top?"
        scene ae1466 with dssa
        d "Nah, the one that might have been dropped a few times when it was still a bibi roll..."
        scene ae1467 with dssa
        n "...Wait what?"
        scene ae1468 with dssr
        d "Our bus."
    else:
        d "(Hmm...)"
        scene ae1451 with dssb
        if (miladate or MilaDate) and VicDateEntry2 is True:
            d "(Mila and I are meeting up soon... And on top of that I also agreed to see Vic.)"
            scene ae1453 with dssr
            d "(I will have to decide sooner or later.)"
        if miladate is True:
            d "(Mila and I are meeting up soon..."
            scene ae1453 with dssr
            d "(I'll have to tell her about my... issue.)"
        elif vicdate is True:
            d "(Vic and I are going out soon... She'll definitely understand my issue.)"
            scene ae1453 with dssr
            d "(She's not one to judge.)"
        scene ae1454 with vpunch
        n "Yo!"
        scene ae1455 with dssa
        d "Shut up Cheeto."
        d "I'm having an inner monologue."
        scene ae1456 with dssa
        n "About what?"
        scene ae1457 with dssa
        d "Confusion."
        scene ae1458 with dssr
        n "It happens! That roll I gave you isn't for beginners."
        scene ae1459 with dssa
        d "What makes you think it's about some rolls?"
        scene ae1460 with dssa
        pause
        scene ae1461 with dssa
        n "Dude. Life's about rolls!"
        scene ae1462 with dssa
        d "(Her stupid humor.)"
        scene ae1463 with dssa
        n "Oh yeah! I can see it on your face!"
        n "You're thinking about rolls, aren't ya?!"
        scene ae1464 with dssa
        d "Yeah, a very special roll."
        scene ae1465 with dssa
        n "Oh! Was it the one with the poppies on top?"
        scene ae1467 with dssa
        n "I bet it was!"
        scene ae1468 with dssr
        d "Our bus."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae1469 with dssb
    n "Finally..."
    scene ae1470 with dssa
    n "I've never wanted to sleep this badly before!"
    n "Even the floor looks cozy!"
    scene ae1471 with dssa
    "She plops off her shoes."
    scene ae1472 with dssa
    n "NIGHTY!"
    d "Good night."
    scene ae1473 with dssa
    pause
    stop music fadeout 3.0
    if OeVaGe4x0 and NamiCuddle04 or HcNaFrt or NamiCuddle04 and Nami_TNI_4x5 is True:
        scene ae1474 with dssb
        d "(...I could just tell her how I feel? How I think I feel?)"
        d "(There's no need to play around... No need to add another thing to my mental luggage.)"
        menu:
            "Tell Nami about your change in perception.":
                $ KissedGirl = True
                $ persistent.unlockedImageR11 = True
                $ play_playlist(playlist_AmbientCheeto)
                $ NamiLove4x5 = True
                scene ae1476 with dssb
                pause
                scene ae1477 with dssa
                d "Cheeto?"
                scene ae1479 with dssr
                n "Yo?"
                scene ae1480 with dssr
                pause
                scene ae1481 with vpunch
                pause
                scene ae1482 with dssr
                "Nami freezes immediately."
                scene ae1483 with dssr
                "But regains her composure a few seconds later..."
                scene ae1484 with dssr
                "Nami pushes her tongue into your mouth, her arms around you, pulling you in closer."
                jump NamiKiss4x5A
            "Keep it to yourself for now.":
                $ NamiNoLove4x5 = True
                scene black with Dissolve(2)
                with Pause(.5)
                if BellaKiss3x5 is True:
                    jump BellaEnd4x5
                else:
                    jump EndScreen4x5
            "There's no change in perception.":
                $ Nami_No_Perception4x5 = True
                if BellaKiss3x5 is True:
                    jump BellaEnd4x5
                else:
                    scene black with Dissolve(2)
                    with Pause(.5)
                    jump EndScreen4x5
    else:
        if BellaKiss3x5 is True:
            jump BellaEnd4x5
        else:
            scene ae1474 with dssb
            d "I should go to bed... I have a long day ahead..."
            scene black with Dissolve(2)
            with Pause(.5)
            jump EndScreen4x5

label BellaEnd4x5:
    $ BellchenEnd4x5 = True
    $ persistent.unlockedImageCh4x51 = True
    if Nami_No_Perception4x5 or NamiNoLove4x5 is True:
        scene ae1475 with dssr
        "You make out a low, familiar rumble outside..."
    else:
        scene ae1490 with dssr
        "A low, familiar rumble pulls you out of it."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    hide screen music_player_trigger
    scene BellchenArrives4x5 with dssb
    $ renpy.pause(4.5, hard=True)
    with Pause(44.5)
    scene black with Dissolve(2)
    with Pause(.5)
    show screen music_player_trigger
    jump EndScreen4x5



label EndScreen4x5:
    $ persistent.unlockedImageBellaCh46 = True
    jump StartChapter5
