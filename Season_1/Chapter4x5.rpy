label Chapter4x5:
    $ achievement.grant("FinishChapter4")
    if miladate is True:
        $ MilaDate = True
    mi "Hey!"
    d "Hey."
    mi "What's wrong? You look a little unwell."
    d "I'm just exhausted."
    mi "We've got coffee."
    n "Oh yeah! I really need some coffee!"
    mi "Sure! Follow me."
    d "Hey."
    v "Hi!"
    v "*Giggles*"
    d "What?"
    v "I don't think you've ever smiled at me before."
    d "Did I smile?"
    d "I guess it's because I haven't seen you much lately."
    v "I got the feeling you were avoiding me a little."
    d "I was."
    d "Sorry."
    d "Don't take it too personally."
    v "Then why did you do it?"
    d "I'm not great at handling sensitive people."
    d "You're soft, it's the exact opposite of what I am."
    d "But I like that about you."
    d "It's just that there is a high risk of me accidentally hurting you and I think that is the last thing you need at the moment."
    "Victoria stares into the room."
    v "...The last thing I need right now is people avoiding me."
    v "Uncertainty is killing me, [name]."
    v "A sea of questions already plagues my thoughts... Please don't make me add 'Is he only here because of pity?' to them..."
    d "I'm not here because of pity."
    d "We all experience tragedies and the last thing I want is to waste my time with a person I don't like."
    d "Which certainly isn't you."
    d "I'm sorry I added another worry to your collection."
    d "What I said to you at the center... I didn't just say that..."
    d "I need you, Victoria."
    d "And I have to ask something of you."
    v "Sure."
    d "I want you and Bella to meet."
    v "Huh? We did meet."
    d "No, I mean really spend a few hours together."
    d "I'm sure she- yeah, I'm sure she'd like you."
    v "I didn't get that feeling when I spoke to her."
    d "It's just because she likes to play the untouchable little cunt."
    v "*whisper* That's a mean word."
    d "I'm mean."
    v "*Whisper* I know... *giggle*."
    v "But... Please promise me you're not going to avoid me anymore."
    v "If you want space just tell me so, but I want you to be upfront with me."
    d "From now on I will."
    d "No more fucking around."
    v "If Maja was here she'd SSSH you."
    d "And I'd gracefully ignore her."
    "She chuckles."
    v "From Monday onwards, I'll have therapy every single day."
    d "I see... And I assume you're asking me if I'll be there?"
    v "Not every time... but sometimes?"
    d "I'll definitely come with you on the first day."
    v "Thanks!"
    "You gently place her legs onto your lap, and she carefully observes your gentle strokes."
    v "I wish I could feel your touch."
    d "Someday you will."
    if BellaKiss03x is True:
        v "I've heard you and Bella kissed."
        d "Yes, we did."
        v "Is it serious?"
        d "I would never kiss someone if there wasn't at least a little seriousness behind it."
        if vicdate is True:
            v "What does this mean for our date?"
            menu:
                "Cancel the date with Victoria.":
                    $ VicDateCanceledBella4x5 = True
                    $ vicdate = False
                    d "I think it would be best to put it on ice."
                    d "I guess, I'll have to figure out where this Bella thing leads me."
                    v "O-okay."
                    d "Hey."
                    d "We're cool, right?"
                    v "I, of course, don't like it... but I'll respect your wish."
                    v "And- And I hope it works out between you and Bella."
                    d "I still want to spend time with you."
                    v "I'd like that."
                "Continue dating Victoria.":
                    $ VicDateContinuedBella4x5 = True
                    d "I still want to get to know you on a... potentially romantic level."
                    v "What about Bella?"
                    d "I'm just not sure... about anything."
                    v "I will talk to Bella first."
                    v "I don't want to step on her toes."
                    d "She'll say 'Do whatever you want, I don't care'... But she won't mean it."
                    v "I don't want to hurt anyone."
                    v "You've gotta promise me that you'll tell me if things get too serious with her."
                    d "I will."
    $ persistent.unlockedImageRS59 = True
    $ persistent.unlockedImageVicCh4x58 = True
    d "Victoria, does the name 'Melanie Ceril' mean anything to you?"
    "She nods a few times."
    d "Your expression tells me that she's bad news."
    v "She almost drowned me in middle school."
    d "What?"
    v "We had a school trip to a waterpark and she held my head underwater until Zara intervened."
    d "Why?"
    v "She hated me for many reasons."
    v "I developed my breasts very early and... I think she wasn't as 'lucky'."
    d "That was the reason?"
    v "One of the reasons. She also hated that I smiled so much... She was also obsessed with a guy in our class."
    v "He liked me but I had no interest in romantic relationships at that time."
    v "And she saw that we were talking a lot and when she confronted him, he told her that I was hitting on him and never left him alone."
    v "The last thing she said to me was that she would stomp on my face with her heels and put them through my eyes."
    d "She seems unstable."
    v "I don't know... maybe she's just misunderstood."
    d "Don't be an idiot."
    d "Nobody normal speaks like that... I should know."
    v "Maja thought she was behind my accident."
    v "I am still a little scared."
    v "It's not like I could run away in my current condition."
    d "If she ever touches you, it'll be the last thing she ever does."
    "Victoria positions herself closer to you."
    v "What if you're not there?"
    d "I'm not the only one who has your back."
    v "Zara used to keep an eye on me."
    d "I'm really surprised to hear that. I didn't know you two knew each other that well."
    v "We weren't friends but she kept an eye on me because... I couldn't and still can't really defend myself."
    v "Once she even fought Melanie... I was so afraid she'd get hurt... Zara... Not Melanie."
    d "Did she get hurt?"
    v "Her lip was bleeding but Melanie looked worse."
    if BTY is True:
        d "(I'm still convinced that Bella would be a great addition.)"
        d "(As cunty as she is... She is very protective of the people she likes... Victoria might remind her of her lost little sister.)"
        d "(Giving Victoria an extra layer of protection.)"
    d "(People like this Ceril cunt are unpredictable. Even at my lowest point I could've never hurt someone as soft as Victoria.)"
    d "(I've gotta keep an eye on her and also talk with Mila and Nami about this.)"
    if vicdate or VicDateContinuedBella4x5 is True:
        v "I built a big binder of potential date destinations."
        v "If you-"
        d "Let me stop you right there..."
        d "A whole binder?"
        v "*Blush* I- uh... yes."
        d "Vic... All I want is a simple... date."
        v "You don't want to call it a date?"
        d "It's complicated."
        d "But...-"
        v "No no! My bad! I'm sorry. I didn't want to come on sooo strong!"
        v "I just really want you to like it."
        d "I like this here."
        d "No unnecessary noise... Just..."
        menu:
            "Give her a kiss.":
                $ KissedGirl = True
                $ persistent.unlockedImageVicCh4x59 = True
                $ VictoriaKiss4x5 = True
            "Don't kiss her.":
        d "A quiet, deep moment."
        d "I like it simple."
        v "Okay- then- then I'll research simple."
        d "No."
        d "How about you and I just get together here again? Just you and me."
        d "We'll wait 'till Maja is out and... you know, just hang out."
        v "*Whispers* I'd love that."
    v "I heard you're good at basketball."
    d "From whom?"
    v "I overheard some guys talking."
    v "One of them was talking you down, and I was about to give him a piece of my mind!"
    d "You can't please everyone. Don't even try."
    v "I really reeaaaally hope I'll be able to walk again before we leave college, and then we can play something together."
    d "You will."
    if RoRum is True:
        v "There-... *sigh*"
        v "Is this a good moment to ask you about your freak-out?"
        d "Yeeeah, sorry about that."
        d "I used to know a girl that was very important to me."
        d "She... well- she was my girlfriend."
        d "She went missing... and still is."
        d "That... Rubber you have, she had the exact same one."
        v "Oh. As a little child I won a whole bunch of them at a theme park."
        d "Yeah, I'm just fucked up in the head and kinda lost my cool."
        d "And I tend to read too much into things when it comes to Summer."
        v "Summer? The one you talked about when we first met?"
        d "Yeah."
        v "I'll help you find her!"
    d "How's Maja doing?"
    v "She's fine. I guess."
    v "I'm just worried that Maja's sacrificing everything for me..."
    d "Nami and I are here if you need us... Maja can take some days off."
    v "It's not just that."
    v "We have medical bills to pay. Our healthcare isn't covering it all."
    v "I can sometimes see how it's eating away at her."
    v "I want to help her so bad... but what can I even do?"
    v "I am so useless in this state."
    d "Not true."
    d "You have a very special voice."
    v "You always say it's too soft."
    d "Too soft for a brute like me."
    d "But I can't imagine a more perfect voice to listen to when trying to sleep."
    d "Maybe you can start reading audio books?"
    v "How would I even start?"
    d "I'll keep my eyes open."
    v "Thank you."
    v "Weird... How long Nami and Mila are taking in the kitchen."
    d "They're standing at the door eavesdropping."
    n "How did you know?!"
    d "I know you."
    mi "Hey [name]." #hug
    d "...I still need to get used to hugs."
    mi "That's a 'you' problem."
    mi "Do you want some coffee too?"
    d "Yeah."
    n "What up, VIC!?"
    v "What up, NAMI!?"
    d "What?"
    $ persistent.unlockedImageRS60 = True
    mi "You called Vic an idiot."
    d "So?"
    mi "That's good. She needs that."
    d "To be called an idiot?"
    mi "No, someone who doesn't treat her any different."
    mi "Many speak to her as if she's on her death bed."
    mi "Their voices are full of pity and it affects Vic negatively."
    d "You mentioned coffee."
    mi "Yup, lemme turn it on."
    mi "*Stretches* Ngggh..."
    d "You look fucked up."
    mi "I fucking hate working at that fucking place."
    mi "Sorry."
    d "All good."
    d "What is it that you work as?"
    mi "As a waitress."
    d "Oh yeah, that sucks."
    mi "I get payed barely enough to survive and sometimes work up to 11h."
    d "Welcome to the rat race."
    d "The tips must be nice, though."
    mi "Depends on my cleavage."
    d "No tips for you today."
    mi "Oh? I'm surprised you noticed it."
    d "I still analyze the people around me... and let's be real they're hard to overlook. And something looked off."
    if miladate is True:
        $ MilaBruise4x5 = True
        d "I also agreed to go out with you-"
        mi "No, no, no. You asked ME out... and I agreed to go out with you."
        d "True."
        mi "I'm still surprised you did."
        d "Me too."
        mi "What made you ask me out? Pity?"
        d "I just want to fuck you."
        mi "Come on! I'm trying to be serious here!"
        d "I don't know. Sometimes... Sometime-"
        mi "- Sometimes there isn't a logical explanation."
        d "Yeah, I guess."
        mi "Same reason why I said yes."
        mi "I don't really go on dates. But you're weird. Like uncomfortably weird sometimes... but that also makes you kinda interesting."
        mi "Or maybe I'm just going crazy."
        d "That's the more likely conclusion."
        "She gently straightens your collar."
        d "..."
        d "Mila."
        mi "*Whisper* Yes?"
        d "Why do you have a bruise on your body?"
        mi "What?"
        d "I touched your hip and you flinched."
        d "Show me your hip."
        mi "[name], there's nothing."
        d "Mila."
        d "You look like a dog that pooped somewhere in the house."
        mi "*Whispers* [name]..."
        $ persistent.unlockedImageMilaCh4x511 = True
        d "Who did this?"
        mi "...My mother."
        d "Why?"
        mi "I refused to 'lend' them money."
        mi "And alcohol makes them do stupid things... So she did what she always does... Threw something at me."
        mi "It happened to be an ash tray."
        d "A fucking ash tray?"
        mi "Please don't tell the others."
        d "I won't... This time."
        menu:
            "Kiss her":
                $ KissedGirl = True
                $ achievement.grant("KissMila")
                $ achievement.sync()
                $ MilaKiss4x5 = True
                $ persistent.unlockedImageMilaCh4x512 = True
                "You grab her head and kiss her."
                d "But if it happens again, Nami and I will take action."
            "Don't.":
                pass
                d "But if it happens again, Nami and I will take action."
        mi "...I just need to move out."
        d "We'll get that student house."
    mi "Do you have Aurora?"
    d "Aurora net?"
    mi "No no, Aurora, the social media app."
    d "No. Never heard of..."
    mi "Dude, everyone is on there."
    d "I see."
    mi "Some guy tried to tag you on an image."
    d "Mhm. So?"
    mi "Will you get the app?"
    d "No."
    d "Wait."
    d "Scroll back."
    d "Elsa."
    mi "Do you know her?"
    d "I used to."
    mi "She's a super famous model."
    d "Are you friends with her?"
    mi "No, her picture is trending, that's why she's there."
    d "I'll get the app, too."
    mi "Wow. She changed your mind fast."
    d "It's not really about her... but a social media app brings people you lost sight of together."
    mi "Is it about Summer?"
    d "Nami told you?"
    mi "Yeeeah, she kinda spilled the beans."
    d "Fucking Cheeto."
    $ persistent.unlockedImageKate3= True
    if BellaKiss3x5 is True:
        $ KissedGirl = True
        d "Who's that girl, Kate?"
        mi "She and I were project partners in High School. She's a friend of mine."
        mi "Bella and Kate are on really bad terms, though."
        d "I heard she bullied Bella."
        mi "That's one side of the coin... Listen to both sides."
    else:
        mi "I think you've seen Kate before?"
        d "Saw her..."
        mi "She and I were project partners in High School. She's a friend of mine."
        mi "Bella and Kate are on really bad terms, though."
    if miladate or miladateF is True:
        mi "[name]?"
        mi "Which one should I post?"
        mi "This?"
        mi "Or this one?"
        call screen MilaChoice4x5
        $ renpy.pause(20, hard=True)
    else:
        jump MilaContinue4x5

label MilaAu1:
    $ MilaOrderly4x5 = True
    jump MilaContinue4x5

label MilaAu2:
    $ persistent.unlockedImageMilaCh4x523 = True
    $ MilaDaring4x5 = True
    jump MilaContinue4x5

label MilaAu3:
    if BellaKiss3x5 is True:
        $ MilaDaring4x5 = True
    else:
        $ MilaOrderly4x5 = True

    mi "Done."
    jump MilaContinue4x5

label MilaContinue4x5:
    d "I noticed you're following a lot of golf stuff."
    mi "Yeah. It's mhhh- more or less the only sport I really like."
    menu:
        "Joke.":
            d "Brave of you to call it a sport."
            mi "It's a sport!"
        "Serious.":
            d "Interesting."
    d "Does the college offer it?"
    mi "No."
    mi "The only place where you can seriously start is at the local golf club."
    mi "They also offer tennis, lacrosse and other activities."
    d "I think Noji wanted to go there with Nami and me."
    d "Is Bella there too?"
    mi "Yeah. Her mother is a Diamond member."
    mi "I will never be able to afford it."
    d "(The fact that she knows that Amber is a Diamond member is oddly specific.)"
    d "Can I get you in?"
    mi "Even if you could... it's not like you can bring me there multiple times a week."
    d "What does it cost?"
    mi "$850 a month for a silver member. Then you get access to the golf course."
    d "I see."
    d "That means that we can't afford it either."
    mi "Bella's mother has some pull. She knows Sasha's mother, who owns the club."
    d "Sasha is rich?"
    mi "Dude? One look at her should tell you that she's from a loaded family. She gets driven to the school in a limousine. And I think she isn't allowed outside without a bodyguard."
    d "I didn't know that."
    mi "Her name is Sasha Petrova. You knew that right? And that they own part of the college?"
    d "So that is what the P in ZPR stands for?"
    mi "Yup. Zane, Petrova, Revera."
    d "And Amber has some pull because?"
    mi "She went to college with Sasha's mother."
    mi "Ayua is a Zane."
    d "And who is a Revera?"
    mi "I think there's someone in the first team but... yeah, I don't know."
    mi "It's a weird clan of these three families."
    d "So how good are you at golf?"
    mi "Well, I actually hated golf... for a while."
    mi "Back as a child I only had a TV with three channels and one was always showing golf."
    mi "I was forced to watch it and dude... I hated it."
    mi "But curiosity made me want to try it."
    mi "I searched for a good stick in the woods and started shooting stones through the forest."
    d "That's cute."
    mi "*Chuckles* Well, it was all I had."
    mi "I have a pair of golf clubs now but yeah, no golf course to play on."
    d "I'll see what I can do."
    mi "No [name], it's alright."
    d "Fuck off."
    mi "Wow. That was rude."
    d "And I'll continue to be rude until you stop that crap."
    if miladate is True:
        pass
    else:
        pass
    d "...You don't always have to get things on your own... It's no sign of weakness to accept help."
    mi "Weird hearing that from you..."
    if miladate is True:
        d "We're all hypocrites."
        mi "*Breathy* I guess."
        d "Let's see what the others are up to."
    else:
        d "We're all hypocrites."
        d "Let's see what the others are up to."
    d "Yo."
    d "Mila wants to play golf."
    n "What? Really? Golf?"
    mi "Well-"
    d "The only place that offers it, is the country club we're going to visit."
    n "Cool. Come with us!"
    mi "No! I can't afford it."
    d "I'll talk to Amber."
    mi "No! I don't want Bella's help!"
    d "Amber is not Bella."
    mi "No please... It's alright."
    v "I'll make you go."
    mi "Oh, how are you going to do that?"
    v "Nami! Help me up! I need to slap some butt!"
    mi "Mhh... We'll see..."
    n "Yo, that reminds me..."
    n "Remember that book club Noji likes to go to?"
    d "Yeah."
    n "Soo... I offered to go with her."
    d "Why?!"
    n "We talked about this! That we'd include her more!"
    n "Anyways! She said something weird."
    n "She uh... told me not to ask you to come."
    d "Why would she do that?"
    n "No idea."
    n "She was really clear about it. 'Don't ask [name] to come with us.''"
    d "I'm in, bitch."
    n "Nice!"
    d "She's gonna hate you for that."
    n "Dude, I really don't want to sit in that boring ass book club alone."
    n "I need you there!"
    n "Noji also gave me the book they're currently discussing."
    d "What is it?"
    n "It's a story about a Panda that got lost and befriended a butterfly."
    d "You're kidding me?"
    v "Sounds cute!"
    d "No wonder Noji's on her death bed."
    n "DUDE! Don't joke about that!"
    d "You read it and then give me the important points."
    n "No way."
    n "We'll do 50/50."
    n "I read the first half for you, you the second half for me."
    d "Alright."
    mi "I know the book."
    n "You do?"
    mi "A little Panda named Tao Tao... As a child, I read the same stuff over and over again."
    n "You should come with us."
    mi "No thanks, haha."
    mi "A book club... No."
    n "Don't you ditch me!"
    d "We'll see."
    jump EveningPart2

label EveningPart2:
    v "Okay! Sooooo... Do we want to order Pizza?"
    n "Could we wait a little? We ate so much at Nick's."
    v "Sure!"
    v "But we can start drinking, right?"
    n "Damn straight we can!"
    mi "We can start with some beer... and then later-"
    v "-We drink this!"
    v "I got it from Maja."
    n "She got you that?"
    v "Yeah, after I told her [name] was going to come by... she told me he was going to need it to remove that... well, plank out of his butt."
    n "Maja is a smart woman!"
    d "Movie?"
    v "Sure!"
    v "What do we want to start with?"
    v "We have a very scary movie..."
    v "And a funny one."
    n "I'm for the scary one!"
    v "The funny one has lots of nudity, I think."
    n "Okay! The funny one!"
    mi "I'm for the scary one."
    v "[name]?"
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
    "You feel Victoria slipping closer to you."
    menu:
        "Pull her onto your lap.":
            $ SVic4x5 = True
        "Don't do it.":
            jump SMovie4x5
    v "Oh no, black people always die first! Poor boy."
    mi "I have an idea."
    n "Every time someone dies we drink?"
    mi "Yes!"
    v "Let's start with these!"
    v "Can you hold the little glasses?"
    d "Yeah."
    d "Mila."
    mi "Thanks."
    d "Cheeto."
    n "Yo Vic?"
    v "Mhhh?"
    n "Weird question but... your boobs are real, right?"
    v "Uhh? What do you mean?"
    mi "She means if you've got fake boobs. Like silicone in there."
    v "Oh, no, no, Nami. They're real."
    mi "I know what you mean, Nami."
    mi "She has won the lottery of connective tissue."
    n "You're wearing no bra and they stay this perky... I'm so jealous."
    v "Don't be, Nami! I'm sure yours are amazing, too!"
    d "Cheeto take the damn drink."
    n "I'll need another one."
    d "Here Vic."
    "You slowly move the shot to her mouth."
    mi "Why are you guys drinking? Nobody died."
    d "Right..."
    d "Here Vic."
    d "Everyone served?"
    n "Mhhh... I wanted to be a movie star when I was little."
    mi "I once got invited to an audition."
    n "Really?!"
    mi "...Yeah, I left after I saw a black couch."
    n "Oh... HAHAHAHA!"
    v "I don't get it."
    d "Me neither."
    n "Okay... The black couch is pretty much a trademark of casting porn."
    v "Oh? They wanted you in a porno?"
    mi "Yup."
    v "Haha!"
    d "Can we watch the movie?"
    n "Sure poophead."
    n "See that's a dumb decision."
    mi "So dumb."
    d "You're scared?"
    v "I thought there was a monster coming."
    n "The monster never appears this early."
    mi "Yeah, it's always a build u-"
    v "AHHHH!"
    n "...I regret everything."
    mi "It looks so scary!"
    d "You've got popcorn in your cleavage."
    v "Do you want it?"
    $ persistent.unlockedImageVicCh4x60 = True
    menu:
        "Take the boob-corn.":
            $ VicBoobCorn4x5 = True
            d "*Whispers* Damn it... Now it's deeper in."
            v "*Whispers* I'm sure you can still reach it."
            "You push your hand between Victoria's full and soft boobs."
            d "Got it."
            "Vic chuckles."
        "Decline and pick a new one.":
            d "I'll pick a new one."
            v "Okay."
    v "Oh no, it's gonna hurt the little doggo?"
    n "I- Na see! Even monsters wouldn't hurt a good doggo!"
    mi "If he had killed the doggo, we'd have to drink five shots."
    v "Nhh!"
    n "*Laughs* Nothing's happening."
    v "Better safe than sorry!"
    n "That also applies to condoms."
    mi "Remember that, [name]."
    n "I don't think you're on birth control, are ya Vic?"
    v "No, I'm not. I- I uh didn't think it'd be necessary today."
    d "Wait what? No what the- Vic, don't listen to these idiots."
    v "Good, I wasn't prepared!"
    mi "Are you on birth control, Nami?"
    n "Not yet, but I plan on getting it soon."
    mi "I'm on the pill, it helps to control your menstrual cycle."
    n "How does sex feel with and without a condom?"
    mi "No idea. I never had it without one."
    n "Hmm."
    n "I wonder if a dildo would be enough-"
    mi "No girl. There's a huge difference between a dildo and an actual penis."
    n "I really need one of those life-like dildos."
    v "Maja has one."
    n "How do you know that?"
    v "She has an entire box full of them."
    jump MajaToys4x5



label MajaToys4x5:
    n "Stop the movie!"
    d "No! Nami!"
    "Mila giggles and follows Nami."
    d "That's super rude!"
    v "Where're they going?"
    d "They're looking for Maja's box."
    v "Oh."
    v "Can you carry me over there?"
    d "Cheeto! Show some respect you fucker!"
    n "Vic, where's the box?"
    n "WHAT'S IN THE BOX?!"
    v "It should be over there."
    d "Mila!"
    mi "Sorry, I'm one of the bad girls."
    n "Mila! Look in there."
    n "Lots of stockings."
    d "You fucking apes, don't be so rude!"
    v "Girls..."
    v "I wanna see it, too!"
    d "I can't believe that I am the sane one here..."
    mi "Found it!"
    n "The holy box of shame?!"
    mi "I wouldn't call it holy."
    d "Nami! Don't touch her fucking sex toys! That's really disrespectful."
    n "OH my god."
    mi "Wow. Look at this one."
    n "I like this one."
    $ persistent.unlockedImageMilaCh4x513 = True
    mi "It would kill your kitty."
    mi "This one is cute."
    v "I want to see them, too!"
    n "Here, look at this one."
    v "Uuh- it looks fancy."
    v "Look [name]-"
    "Vic accidentally rubs it against your cheek."
    d "Don't- touch me with that."
    v "Sorry."
    n "They are all clean, [name]."
    v "It's long... does it all fit into a vagina?"
    mi "Oh no. That's an anal toy. You put it in your butt."
    v "Oh! Doesn't it hurt?"
    mi "You start with them here-"
    v "Oh! So cute."
    mi "And you just go bigger and bigger until you've reached your desired size."
    n "What's this?"
    mi "I- think uuuh, you can put it on your nipple."
    n "A nipple pump?"
    mi "Yes."
    v "It looks cute. What does it do to your nipple?"
    mi "It makes it bigger. Maybe it gets a little more sensitive, too."
    n "[name]? Please say yes."
    d "I will not let you put that thing on my nipple."
    mi "Oh god! Please do it! Please, please, pleaseeeee!"
    v "Yes! Do it!"
    menu:
        "Let them put it on your nipple.":
            $ persistent.unlockedImageNamiCh4x544 = True
            $ MCNipplePump = True
            $ persistent.unlockedImageVicCh4x61 = True
            d "Alright..."
            n "Wait- really?"
            d "Yes."
            n "Dude! I never expected you to say yes!"
            mi "*Laughs* Take off your shirt."
            d "Vic- I-"
            v "Let's take his shirt off."
            "The three girls surround you."
            mi "Guys have small nipples, I don't expect there to be a big effect."
            n "Ready?"
            d "Just do it."
            mi "Do you feel something?"
            d "A sucking motion."
            v "Do it harder."
            d "It feels weird."
            mi "Do it a couple more times."
            n "It sticks."
            mi "Pull it off."
            v "Look! It got a little bigger."
            mi "I think it got quite a lot bigger- you should use it on someone with bigger nipples."
            n "Mila, maybe yours?"
            mi "Yeah, I will not flash my tits."
            n "It's just us... and [name]."
            mi "I'll pass."
        "No.":
            n "Pfff... Party pooper."
    d "Can I have a shot?"
    mi "Drink from the bottle."
    if MCNipplePump is True:
    else:
    mi "Good boy."
    n "Vic, where was the shop she got these at?"
    v "Uhhhh, I don't know the street, but I can get you there."
    mi "I'll come with you guys."
    n "What collection do you have at home?"
    mi "I don't have a single toy."
    mi "I would like some, but my parents don't value privacy."
    v "I don't have one either."
    n "Here. It's yours."
    v "It's Maja's!"
    n "She has like four of them."
    v "Noo! I want to get my own."
    n "Alright, we will go the shop together then."
    v "You too, [name]."
    d "Sure."
    n "Waaaait, why would you say yes to that?"
    d "Get some leverage on you."
    d "Make some hints during breakfast to Noji."
    n "You're evil!"
    n "I'll buy you a toy too!"
    d "Alright, can we put Maja's stuff back and go back to the movie?"
    mi "First, you take another sip."
    d "I already had one, it's your turn."
    mi "Oh! I'm not the party pooper here. You need it more than we do."
    "You take another sip."
    d "- It tastes worse with every sip."
    n "The holy box has been returned... Let's get out of here."
    mi "Make sure it's exactly how we found it."
    if VicMovie4x5 is True:
        jump SmVic4x5P2
    elif MilaMovie4x5 is True:
        jump SmMila4x5pt2
    else:
        jump Crossroad4x5


label SmVic4x5P2:
    $ VicProtect4x5 = True
    "Victoria takes your hand and caresses it slightly."
    mi "Oh no! Creepy scene!"
    "She grabs your hand and holds it against her chest."
    d "(I'm not aroused but I can't deny that her breasts, or breasts in general, feel amazing.)"
    d "(I think there's some primitive force in straight males that makes breasts just feel... awesome.)"
    "You resist the underlying urge to remove your hand from her breast and just let it rest there."
    "As the movie intensifies, Victoria increases the pressure on your hand."
    d "(If she wasn't wearing a top, I'd have her entire breast in my hand...)"
    d "(...And me not minding it... Hell, me kind of wanting it confuses me.)"
    if BellaKiss3x5 is True:
        d "(I wonder what Bella's would feel like.)"
    "The movie calms down and Vic lowers the pressure but fixates your hand on her chest."
    d "(I can feel her nipple... She must be aroused.)"
    d "(I'm glad we aren't alone here... I don't know if I'm ready for what would come next... To see the disappointment in her eyes.)"
    if BellaKiss3x5 is False:
        d "(I feel guilty just by touching her... I'm so stupid.)"
    else:
        d "(I feel somewhat guilty for touching her...)"
    d "Yo, Cheeto, let's all drink a shot."
    n "Nobody died?"
    mi "[name] proposing a shot? You don't question that Nami! Drink!"
    "*Splatter sounds*"
    n "Is he dead?"
    d "Yeah."
    v "More!"
    n "And this guy's dead, too."
    n "Oh boy."
    "*Screams*"
    d "Are you serious?"
    mi "They both died... Does this mean-"
    n "Yes... Two shots."
    d "Okay seriously... If we down these two... this evening might take a bad turn."
    mi "I don't want to vomit."
    v "I say we take them!"
    d "You're a bad influence."
    v "*Tough* I am!"
    mi "It sounds really cute when you're trying to sound tough in your soft voice."
    v "My damn voice..."
    n "I bet you could make some money reading audio books."
    d "That's what I said."
    v "I feel it."
    mi "*Chuckles* Me too."
    d "I can see that."
    mi "I feel good now... But any more and I will feel reaaaally bad."
    d "I'll get us some water."
    v "No... Stay! It's cozy."
    d "(These two seem... very touchy...)"
    d "(I should get up if I want to avoid an awkward turn of the evening.)"
    jump Crossroad4x5


label SmMila4x5:
    $ MilaMovie4x5 = True
    "Mila sits closer beside you."
    menu:
        "Put your arm around her.":
            $ MilaScaryMovieCuddle4x5 = True
        "Keep your distance.":
            jump SMovie4x5
    mi "*Whisper* Every time I watch a horror movie I can't stop thinking about it for a couple of days."
    d "Nami's the same."
    v "Oh no, black people always die first! Poor boy."
    mi "I have an idea."
    n "Every time someone dies we drink?"
    mi "Yes!"
    v "Let's start with these!"
    v "Here! One for everyone!"
    n "Yo Vic?"
    v "Mhhh?"
    n "Weird question but... your boobs are real, right?"
    v "What do you mean?"
    mi "She means if you've got fake boobs. Like silicone in there."
    v "Oh, no no, Nami. They're real."
    mi "I know what you're getting at, Nami."
    mi "She has won the lottery of connective tissue."
    n "You're wearing no bra and they stay this perky... I'm so jealous."
    v "Don't be, Nami! I'm sure yours are amazing, too!"
    n "Mine are also not saggy but the size difference makes it so unbelievable."
    n "I'll need another one..."
    mi "Don't worry too much about tits."
    n "Coming from you... that's like a billionaire saying 'Don't worry too much about money'."
    mi "...Yeah, sorry."
    v "All tiddies are great tiddies!"
    mi "I don't like her but..."
    mi "Besides Vic's godlike tiddies... Bella's are also pretty nice."
    n "What?"
    mi "She has relatively big tits but not too big... They also got a nice form."
    n "Who are you and what did you do to Bella-Hating Mila?!"
    mi "I still dislike her... But I can be objective."
    if BellaKiss3x5 is True:
        n "Have you seen her... jugs?"
        if bellagym is True:
            d "Yeah."
            n "When?"
            d "She stormed into my shower at the gym."
            n "..."
        else:
            d "It was pretty dark and I didn't really look at them."
            n "Who wouldn't take a look at boobs?!"
            d "I was busy touching them... and tucking them back in."
            n "..."
    v "Why does everyone always talk about boobs and butts but not about vaginas?"
    mi "*Chuckles* I think vaginas are more intimate than boobs."
    n "[name]..."
    n "You haven't complained yet."
    mi "Weird..."
    d "One way out of my comfort zone is listening to... this."
    n "Okay, okay..."
    if milagym is True:
        n "Boobs or ass?"
        if MMCBB03 is True:
            mi "He likes boobs."
        elif MMCPB03 is True:
            mi "He likes butts."
        elif MFAnal is True:
            mi "You didn't have a preference, right?"
        n "How do you know?"
        mi "I asked him."
        d "I totally forgot your pants incident."
        mi "Hey no! PSSH!"
        v "What incident?"
        d "Her pants ripped while we were at the gym."
        mi "...So embarrassing."
        n "If I didn't know you, I would hate you."
        mi "That's a compliment!"
        n "How can you have big tits and a big ass while not being fat!?"
        n "What do I have?!"
        mi "You've got a nice big ass!"
        n "Thank you!"
        d "Stop fishing for compliments... It's embarrassing."
        n "Y-you are embarrassing!"
        d "That's well known."
    else:
        mi "[name]... Boobs or ass?"
        d "What I like more?"
        mi "Yeah."
        d "What if I like a penis?"
        mi "That would explain a lot."
        menu:
            "I like the look of a well formed butt.":
            "I like the look of some well formed breasts.":
            "I don't have a preference. I like them both.":
    d "Let's watch the movie..."
    n "Poophead."
    v "Oh no, it's gonna hurt the little doggo?"
    n "I- Na see! Even monsters wouldn't hurt a good doggo!"
    mi "If he had killed the doggo, we'd have to drink five shots."
    v "Nhh!"
    n "Nothing's happening, haha."
    v "Better safe than sorry!"
    n "That also applies to condoms."
    mi "Are you on birth control, Nami?"
    n "Not yet but I plan on getting it soon."
    mi "I'm on the pill, it helps to control your menstrual cycle."
    n "How does sex feel with and without a condom?"
    mi "No idea. I never had it without one."
    n "Hmm."
    n "I wonder if a dildo would be enough-"
    mi "No girl. There's a huge difference between a dildo and an actual penis."
    n "I really need one of those life-like dildos."
    v "Maja has one."
    n "How do you know that?"
    v "She has an entire box full of them."
    jump MajaToys4x5

label SmMila4x5pt2:
    "Mila moves her hand onto your thighs."
    "As you try to focus on the movie, you feel her fingers gently circulating on the fabric of your pants."
    "You move your hand farther."
    d "(I think there is something primal in straight males that makes long legs just look so... alluring.)"
    "You resist the underlying urge to remove your hand from her leg and just let it rest there."
    "She moves your hand up to her inner thighs."
    d "(I'm confused that I don't mind it... Hell, I would even say want it.)"
    if BellaKiss3x5 is True:
        d "(I wonder how Bella's inner thighs would feel.)"
    else:
        d "(I feel guilty just by touching her... I'm so stupid.)"
    d "Yo, Cheeto, let's all drink a shot."
    n "Nobody died?"
    mi "[name] proposing a shot? You don't question that, Nami! Drink!"
    "*Splatter sounds*"
    n "Is he dead?"
    d "Yeah."
    v "More!"
    n "And this guy's dead, too."
    n "Oh boy."
    "*Screams*"
    d "Are you serious?"
    mi "They both died... Does this mean-"
    n "Yes... Two shots."
    d "Okay seriously... If we down these two... this evening might take a bad turn."
    mi "I don't want to vomit."
    v "I say we take them!"
    d "You're a bad influence."
    v "*Tough* I am!"
    mi "It's sounds really cute when you're trying to sound tough in your soft voice."
    v "My damn voice..."
    n "I bet you could make some money reading audio books."
    d "That's what I said."
    v "I feel it."
    mi "*Chuckles* Me too."
    d "I can see that."
    mi "I feel good now... But any more and I will feel reaaaally bad."
    d "I'll get us some water."
    v "No... Stay! It's cozy."
    d "(These two seem... very touchy...)"
    d "(I should get up if I want to avoid an awkward turn of the evening.)"
    jump Crossroad4x5


label SMovie4x5:
    $ SoloMovie4x5 = True
    mi "*Whisper* Every time I watch a horror movie I can't stop thinking about it for a couple of days."
    d "Nami's the same."
    v "Oh no, black people always die first! Poor boy."
    mi "I have an idea."
    n "Every time someone dies we drink?"
    mi "Yes!"
    v "Let's start with these!"
    v "Here [name]."
    n "Yo Vic?"
    v "Mhhh?"
    n "Weird question but... your boobs are real, right?"
    v "What do you mean?"
    mi "She means if you got fake boobs. Like silicone in there."
    v "Oh, no no, Nami. They're real."
    mi "I know what you're getting at, Nami."
    mi "She has won the lottery of connective tissue."
    n "You're wearing no bra and they stay this perky... I'm so jealous."
    v "Don't be Nami! I'm sure yours are amazing, too!"
    n "Mine are also not saggy but the size difference makes it so unbelievable."
    n "I'll need another one."
    mi "Don't worry too much about tits."
    n "Coming from you... that's like a billionaire saying 'Don't worry too much about money'."
    mi "...Sorry."
    v "All tiddies are great tiddies!"
    mi "I don't like her but..."
    mi "Besides Vic's godlike tiddies... Bella's are also pretty nice."
    n "What?"
    mi "I'm just being objective."
    mi "She has relatively big tits but not too big... They also got a nice form."
    n "Who are you and what did you do to Bella-Hating Mila?!"
    mi "I'm still not positive about her... But I can be objective."
    if BellaKiss3x5 is True:
        n "Have you seen her... jugs?"
        d "It was pretty dark and I didn't really look at them."
        n "Who wouldn't take a look at boobs?!"
        d "I was busy touching them... and tucking them back in."
        n "Oh."
    v "Why does everyone always talk about boobs but not about vaginas?"
    mi "I think vaginas are more intimate than boobs."
    d "What?"
    n "You haven't complained yet."
    mi "Weird..."
    d "One way out of my comfort zone is listening to... this."
    n "Okay, okay..."
    n "Tits or ass?"
    if milagym is True:
        if MMCBB03 is True:
            mi "He likes boobs."
        elif MMCPB03 is True:
            mi "He likes butts."
        elif MFEQ is True:
            mi "You didn't have a preference, right?"
        n "How do you know?"
        mi "I asked him."
        d "I totally forgot your pants incident."
        mi "Hey no! PSSH!"
        v "What incident?"
        d "Her pants ripped while we were at the gym."
        mi "...So embarrassing."
        n "If I didn't know you, I would hate you."
        mi "That's a compliment!"
        n "How can you have big tits, a big ass and still be relatively skinny!?"
        n "What do I have?!"
        mi "You've got a pretty great ass."
        n "Thank you!"
        d "Stop fishing for compliments... It's embarrassing."
        n "Y-you're embarrassing!"
        d "That's well known."
    else:
        mi "[name]... Boobs or ass?"
        d "What I like more?"
        mi "Yeah."
        d "What if I like a penis?"
        mi "Then this would explain a lot."
        menu:
            "I like the look of a well formed butt.":
                $ McPrefButt4x5 = True
                mi "Noted."
            "I like the look of some well formed breasts.":
                $ McPrefBoobs4x5 = True
                mi "Noted."
            "I don't have a preference. I like them both.":
                $ McPrefBoth4x5 = True
                mi "Noted."
    n "I wanted to be a movie star when I was little."
    mi "I once got invited to an audition."
    n "Really?!"
    mi "...Yeah, I left after I saw a black couch."
    n "*Laughs* Oh!"
    v "I don't get it."
    d "Me neither."
    mi "The black couch is a trademark of casting porn."
    v "Oh? They wanted you in a porno?"
    mi "Yup."
    d "Can we watch the movie?"
    n "Sure poophead."
    v "Oh no, it's gonna hurt the little doggo?"
    n "I- Na see! Even monsters wouldn't hurt a good doggo!"
    mi "If he had killed the doggo, we'd have to drink five shots."
    v "Nhh!"
    n "Nothing's happening, haha."
    v "Better safe than sorry!"
    n "That also applies to condoms."
    mi "Are you on birth control, Nami?"
    n "Not yet but I plan on getting it soon."
    mi "I'm on the pill, it helps to control your menstrual cycle."
    n "How does sex feel with and without a condom?"
    mi "No idea. I never had it without one."
    n "Hmm."
    n "I wonder if a dildo would be enough-"
    mi "No girl. There's a huge difference between a dildo and an actual penis."
    n "I really need one of those life-like dildos."
    v "Maja has one."
    n "How do you know that?"
    v "She has an entire box full of them."
    jump MajaToys4x5





label Crossroad4x5:
    $ persistent.unlockedImageMilaCh4x514 = True
    v "Can we lay down for a little while?"
    d "Yeah."
    "As you try to get up, Victoria leans against you... slowly pushing you towards Mila."
    n "I also want to be part of the cuddle session!"
    d "...Totally not uncomfortable."
    mi "Hey! As if my tiddies are that uncomfortable?"
    d "It's Vic's elbow in my side."
    v "Oops."
    v "I wonder what we should do..."
    mi "... Oh- How about we play some Truth or Dare?"
    d "Nah."
    n "Yes!"
    v "Three against one."
    mi "Nami! Truth or Dare."
    n "Truth!"
    mi "Do you have a fetish?"
    if bellameet is True:
        $ NamiFaceSitting = True
        n "Hmm, that changes from week to week, really."
    else:
        $ NamiFaceSitting = False
        n "Hmm, it always changes... but maybe risky things?"
        v "Did you already do that?"
        n "No. I'm still a virgin."
        v "Me too."
        n "I imagine that public stuff can quite exhilerating."
    n "Hmm, [name]! Truth or dare!"
    d "No way I'm going to do truth."
    d "Dare."
    n "Make out with Vic."
    menu:
        "Make out with Victoria.":
            $ KissedGirl = True
            jump VicMakeout4x5
        "Don't do it (Think of Bella.)" if BellaKiss3x5 is True:
            $ DKVDBB4x5 = True
            d "I'm sorry. I can't... I don't want to hurt Bella."
            v "It's okay [name]."
            d "And I'm actually really hungry."
            jump FourSomeAfterwards
        "Don't do it. (You don't want to.)":
            $ DKVD4x5 = True
            d "Sorry. But no... Not like this."
            n "*Sigh*"
            mi "Party pooper."
            d "I'm actually really hungry."
            jump FourSomeAfterwards


label VicMakeout4x5:
    $ VicDare4x5 = True
    d "Alright."
    "Nami turns Vic around..."
    "Victoria presses her soft lips on yours."
    menu:
        "Caress Mila's thigh.":
            jump Foursome4x5A
        "Don't touch Mila.":
            mi "Alright! Dare is over!"
            jump FourSomeAfterwards

label FourSomeAfterwards:
    if Foursome4x5 is True:
        $ achievement.grant("Awkward4")
        $ achievement.sync()
        d "I'm hungry... shall we get some Pizza?"
        mi "And just ignore what happened?"
        d "Of course not."
        d "It would create awkwardness below the surface."
        d "We can still talk about it, but I prefer this discussion while eating pizza."
        n "I can't argue with that."
        mi "It sounds like a plan."
    else:
        pass
    v "Okay! Pizza time!"
    v "It's already late. We'd have to go to the place to pick it up."
    n "[name] and I will get it."
    mi "Okay sure, we'll give you the money."
    n "No, this is on us."
    mi "It-"
    d "On us."
    mi "Fine. Thanks."
    if Foursome4x5 or VicDare4x5 is True:
        v "I think I need to change my underwear."
        mi "Lemme get you to your room."
    n "Dude."
    d "Mh?"
    if Foursome4x5 is True:
        n "That escalated so hard."
        d "And you say you're not into girls?"
        n "I sacrificed myself! I tried to push it further!"
        n "And you made out with Vic and Mila!"
        d "Mhm."
        n "But... You didn't make out with me."
        d "I think you and I making out would have ended whatever that was immediately."
    else:
        n "They're sooo horny!"
        d "How can you tell?"
        n "The way they play with their hair... the giggles... Trust me... The giggle always tells!"
        d "I saw your body language too..."
    d "Your feelings for me could get us into some deep shit someday."
    "Nami freezes."
    n "My what for you?"
    if NamiLove4x0 is True:
        d "We talked about it at the lake."
    else:
        $ NamiLove4x5a = True
        d "Do you think I'm an idiot?"
    d "It's obvious that there is more than just friendly love."
    n "There- is... not."
    d "I've accepted it. It doesn't make me think you are weird or anything..."
    d "No more than usual..."
    d "It's just in moments like these... you need to keep it under control."
    if Foursome4x5 is True:
        d "If you would have kissed me, Mila would not have taken it-... You can imagine."
        n "What about Vic?"
        d "Vic is weird... She made me and Mila kiss."
    d "And you stopped denying the feelings part."
    n "Fuck off."
    d "Nami."
    d "You're really important to me... It might not seem like it but I care a lot about your wellbeing."
    $ persistent.unlockedImageNamiCh4x549 = True
    if NamiCuddle04 and OeVaGe4x0 is True:
        d "If word got out about your... feelings... People could use it against us in the most cruel way."
    else:
        d "If word got out about your... feelings... People could use it against you in the most cruel way."
    "The Cheeto just stares into your eyes."
    if BellaKiss3x5 and Foursome4x5 is True:
        d "I feel weird, though."
        n "Bella?"
        d "Mhm."
        n "Do you love Bella?"
        d "Not love... It's not there yet... But I'm into her."
        d "You know she and I kissed."
        d "And... I liked it."
        n "Did you like what happened here?"
        d "Maybe... Otherwise, I wouldn't have let it happen."
        n "You're warming up to all of this."
    elif DKVDBB4x5 is True:
        n "It must've taken a lot of willpower not to kiss Vic."
        d "I like Bella... and I know kissing Victoria would hurt her."
    if Foursome4x5 is True:
        n "Did you have a boner?"
        d "No."
        n "I'm afraid that was just another move to become normal."
        d "It was. Drastic measures... but it's not like I disliked it."
        n "At least Vic and Mila were wet."
        n "I actually don't know if they were aroused... I just think they'd be."
        if NamiCuddle04 and OeVaGe4x0 is True:
            d "What about you?"
            n "Dude, my underwear is drenched."
        d "Lemme call Mila."
        n "What!? Why?"
        d "We didn't ask what pizza they wanted."
        if NamiCuddle04 and OeVaGe4x0 is True:
            n "Right, right... I thought you wanted to ask them if their panties were drenched."
        else:
            n "Right, right... I thought you wanted to ask them if they were aroused."
    else:
        d "Let me call Mila."
        d "We didn't ask what pizza they wanted."
    d "Hey."
    d "We didn't ask what pizza you wanted."
    mi "Vic wants a Salami."
    mi "I'd like a Diablo."
    d "Sure."
    d "Diablo and Salami."
    n "If I had to be some kind of pizza... Would I be more of a Diablo or a Salami?"
    d "Definitely a salami."
    if BellaKiss3x5 and Foursome4x5 is True:
        n "What will you do about Bella?"
        d "Nothing?"
        d "I don't even know if we are dating. I- I have no idea what we are..."
        d "We kissed. We ended it. That was it."
        n "How would you feel if she kissed someone else?"
        d "I probably wouldn't like it. But she and I aren't together."
        d "She is free to do whatever she wants."
        n "This is a dumb situation... She's putting so much uncertainty on you."
        n "You really need to have a clear talk with her."
    d "Let's get some pizza."
    jump JohnnyPizza

label JohnnyPizza:
    $ persistent.unlockedImageRS62 = True
    u "Welcome to Johnny's Pizza."
    u "May I take your order?"
    n "We would like to have one Pizza Diablo."
    n "Two with Salami and one Pizza Tonno."
    u "Large or medium?"
    d "All large."
    u "Of course."
    u "Hey."
    d "Oh hey."
    az "My name's Aziz, by the way."
    d "I'm [name]."
    az "And you are?"
    n "Nami!"
    az "You're a cute couple."
    n "I think I will just go with it now."
    n "We're indeed a cute couple!"
    d "She's my roommate and we're not a couple."
    az "Oh. I see."
    u "Oh hello! Are these friends of yours?"
    az "Freshmen from the college. We don't know each other yet."
    moll "It's nice to meet you! I am Aziz's Mom, Molly."
    n "I'm Nami, nice to meet you Molly!"
    d "I'm [name]."
    d "...Nami's roomie."
    if fitness is 2 or fitness is 1 and mobility is 1:
        $ MCCanidate = True
        moll "[name]... Ah! The [name] that was on the list of potential candidates?"
        az "Thanks for revealing classified information, Mom."
        moll "Sorry, sorry!"
        d "How come I'm on the list?"
        az "You made some impressive plays."
        az "We have a lot of players with high athletic abilities."
        az "But many of them lack an innovative brain."
        az "The way you located their weak link and successfully got under their skin, got our attention."
        az "Also... Dwight likes you."
        n "What about the girls team?"
        az "The girls should be back next week."
        az "They had a team vacation at a wellness resort."
        n "I want to impress them."
        d "You will manage."
    n "Do you always wear sunglasses?"
    moll "Ugh... He has such beautiful eyes!"
    moll "I fear they will become part of your body at some point!"
    az "They already are."
    if RoRum is True:
        az "Did the reporter approach you again?"
        d "No, I haven't seen her since."
        moll "Don't tell me you're talking about that bitch Nicole?"
        moll "I apologize for the harsh language."
        n "You got approached by a reporter?"
        d "Yeah... Before gym class."
        d "She asked me about Robin."
        moll "Ohhh! Is Robin your girlfriend?"
        az "Mom! Come on? Be cool."
        d "No, Robin isn't my girlfriend."
        d "There's just a rumor going around, she asked me about it, made some stuff up, and left again."
        az "You can expect an article about this in the next College newspaper."
        d "There is a college newspaper?"
        az "It connects all the colleges from this state."
        az "She'll continue to spread it and build up on the rumor."
        n "Isn't that against the law?"
        az "She walks a thin grey line... Whenever she gets busted, she takes the article down, pays a fine... But the damage is done."
        moll "Oh no... It reminds me of-"
        az "Don't."
        "She places her hand on her Son's shoulder."
    u "Two large Gio's and one large Macci pizza."
    moll "That's ours."
    az "See you two around."
    moll "Goodbye [name] and Nami!"
    n "Bye! Have a good meal!"
    d "Bye."
    n "Nice mommy."
    d "Mhm."
    if RoRum is True:
        n "But man... Why do you never tell me anything?"
        d "She just approached me and asked one question, and then the guys made her go away."
        n "Still! If a reporter approached me, I wouldn't stop talking about it!"
        d "Yeah, but I don't care about stuff like that."
        d "I don't want to be famous or known at all."
        n "Then stop fucking girls in public restrooms."
        "The table next to you redirects their attention to you and Nami."
    if NiaDeal is True:
        d "Someone who's number I haven't saved is calling me."
        nia "Hi [name]. I got your number from the group chat."
        nia "Sorry if I'm disturbing you, but would it be okay with you if we met up tomorrow instead of Sunday?"
        d "Yeah, I guess.."
        nia "Great!"
        nia "Sorry for the short notice! Good night!"
        d "It's alright. I'll see you then."
        d "I'm going to head over to Nia's tomorrow instead of Sunday."
        n "Oof... I've got no idea when we'll be home."
    else:
    u "Large Pizza Tonno, Diablo and two Salami!"
    d "Thank you."
    n "Put mine in the middle so it keeps warm!"
    if Foursome4x5 is True:
        d "Mila's in the middle."
        d "She needs to be in the best mood possible for what's to come..."
        n "It'll get awkward."
        d "We'll get through it."
    jump Pizza4x5

label Pizza4x5:
    if Foursome4x5 is True:
        $ NamiBi4x5 = True
        mi "Alright... Can we now talk about what happened?"
        d "I assume while Nami and I were getting pizza, you and Vic already exchanged some thoughts?"
        mi "It was mostly Vic saying how great you kiss."
        n "Well, I had no problems with what happened!"
        d "Of course not, you're a weirdo."
        v "I liked it too."
        v "But I feel bad that someone here might feel awkward now."
        mi "It... was awkward... I-It's now awkward. Back when we did it... It was nice."
        mi "The thing is I'm not really into girls."
        n "Me neither... Or so I thought."
        d "You are now?"
        n "I didn't dislike kissing Vic."
        n "Wait! Vic! Come! Kiss me again."
        "You and Mila share an awkward look."
        n "Yeah, I don't dislike it."
        $ persistent.unlockedImageVicCh4x63 = True
        n "I'M BI NOW!"
        v "I didn't dislike it either. But I like [name]."
        n "I get that."
        n "B-Boys! I mean boys in general! N-not [name]!"
        n "T-The problem I have with all of this is the reason [name] did it."
        n "He's pushing himself to be normal and I'm sure this will not end well."
        mi "Oh. Yeah [name], stop that... Go at your own pace."
        d "I did."
        n "Uh hu, from 'Don't touch me' to a foursome in a few days... Totally normal."
        d "I have to somehow widen my comfort zone."
        mi "To be honest, I get his point here."
        mi "In order to escape the comfort zone, you'll need to constantly attack it."
        n "Still..."
        if BellaKiss3x5 is True:
            mi "What I really don't like is that [name] kissed us even though he and Bella are... bonding?"
            d "We're not together."
            mi "Yeah, but it would break her heart, wouldn't it?"
            mi "She would of course play it cool but I know her. She wouldn't take it well."
            v "It's all my fault..."
            d "No Vic. I chose to kiss you."
            mi "I'm just saying... we're college freshmen and I assume we're going to experience a lot more than this... Maybe talk to her and put it on ice."
            mi "I see a lot of potential future disasters."
            v "Or you make it official."
            mi "...Or that."
    else:
    d "The pizza is good. It can almost rival Gio's."
    v "Gio's?"
    d "It's a place on the other side of the city."
    n "It's reaaaally good."
    n "But this one here has better cheese."
    if RoRum is True:
        $ MilaVicHelp = True
        mi "[name]? What exactly happened with Robin?"
        v "It must have happened right after you stormed out of class, right?"
        n "Huh?"
        n "Why did you storm out?"
        d "Victoria has an eraser."
        n "Oh no... Don't tell me it's the same rubby?"
        d "Yeah."
        d "And when Vic put it in my hand, I freaked out."
        n "That's not a sign whatsoever."
        d "I know that!"
        d "It just... really caught me off guard."
        d "And it showed me just how far I am from moving on."
        d "I'm still at the same place I was two years ago."
        mi "No, you're not."
        "Mila comes over."
        mi "I don't know exactly how you were two years ago but..."
        mi "Instead of being alone and isolated with your thoughts, you now have us."
        v "Mila is right!"
        v "We will always be there for you!"
        n "Remember what I said?"
        n "This is the best time to move on."
        n "So many new and awesome people that like you and want to help you."
        d "Mmm.."
        d "But do I even like you guys?"
        mi "You suck dude."
    n "We met a guy from the first team at the Pizza place."
    n "Aziz was his name, I think."
    mi "I know him from elementary school."
    mi "He was two classes above me, though."
    n "How is he?"
    mi "I never really talked to him but he seemed cool."
    n "Was he wearing sunglasses back then?"
    mi "*Chuckles* No."
    mi "When I got to high school he was wearing them all the time."
    mi "No idea why."
    if MCCanidate is True:
        n "His mother accidentally revealed that [name] is on the list for the potential candidates for the first team."
        mi "Way to go!"
        v "That's so awesome!"
    n "Alright, let's watch the funny movie."
    n "I wanna see some tiddies... but first I need to pee."
    d "(Tomorrow I need to visit Emilio.)"
    d "(Maybe he can help me find some closure...)"
    mi "Why's college not like in the movies?"
    n "They never seem to have class."
    if RoRum is True:
        mi "[name]'s life seems comparable to this."
        mi "It's the first week and he's already got the reputation of a dude who bangs girls in public restrooms."
        n "True."
    n "I wish we had more parties!"
    d "Me too."
    "Nami shoots you a suspicious look."
    d "That way you'd be at a party and I'd have some peace."
    n "You suck... And you know I would drag you along!"
    v "When Maja was still a student she had lots of parties."
    v "I guess they will happen soon."
    mi "We've got a house warming party coming up for the bar."
    mi "And I'm sure we're all going to make some new friends there."
    n "I've been invited to some parties on another campus."
    mi "By whom?"
    n "People from [name] and mine's old high school."
    mi "Be careful with the other colleges."
    mi "I heard the rivalries are quite nasty... If [name] makes the first team, I could see them targeting you."
    n "Like?"
    mi "Try to bed you, film it and then publish it."
    n "That would mean I'd actually be interested in someone... and stupid enough to fall for that..."
    d "IF I make the first team."
    mi "You will. I believe in you."
    v "I haven't seen you play yet but I'm sure you will!"
    mi "But... I heard you pushed Kai, the son of one of the head coaches into a bookshelf."
    n "What?! When?"
    d "When I went to talk with Nadia."
    d "I'm sure he didn't even mean bad by it... but he shouldn't have touched me."
    n "You idiot..."
    n "Why are you making your own life so hard?"
    d "I don't give a fuck if he goes crying to his Daddy."
    d "As long as I perform well, and get more first team members on my side, I'll make it."
    n "Still... You need more impulse control."
    d "I'm working on it."
    mi "Kai's not a bad guy but... likes to play the knight in shining armor."
    d "If you do that you should have something to follow up besides: 'I'm gonna sue you.'"
    v "I'm gonna sue you!"
    d "For what?"
    v "For having a nice butt!"
    "Nami and Mila giggle."
    mi "That was the movie."
    d "I missed pretty much everything."
    n "Come! All together."
    menu:
        "Ask Mila to go for a walk.":
            d "I'm getting kinda tired... Do you want to take a walk?"
            mi "Me?"
            d "I'm looking right at you."
            mi "Okay- sure!"
            n "Come Vic, let's take some pictures for Aurora."
            v "Sure!"
            jump MilaWalk4x5
        "Ask Vic to roll on a walk.":
            d "I'm getting sleepy..."
            d "Vic, do you want to take a walk?"
            v "I would if I could."
            d "Come."
            n "Mila! Let's take some pics for Aurora."
            mi "Sure!"
            jump VicWalk4x5
        "Take a walk (Nami).":
            d "I'm getting sleepy... I'm gonna take a walk."
            n "I'll come with you!"
            mi "Vic, we need more pictures."
            v "Sure!"
            jump CheetoWalk4x5

label MilaWalk4x5:
    $ persistent.unlockedImageR6 = True
    $ NamiPeaceTreaty = False
    d "Shall we walk for a while?"
    mi "Yes."
    $ persistent.unlockedImageMilaCh4x515 = True
    mi "W-we're not going into the forest, right?"
    d "Are you scared?"
    mi "Yes."
    d "Let's sit down for a moment."
    d "I can't let my comfort zone win."
    d "Whenever I think about spending time with someone other than Nami, it feels like a burden."
    if MilaDate is True:
        d "I like you, and I don't want to see you as a burden."
    else:
        d "I don't want to see you as a burden."
    mi "*Chuckles* You really need better ways to phrase this stuff."
    d "All you need to focus on is that I like you."
    mi "I like you too."
    mi "It can't be easy going from full isolation to... well, all of this."
    if MilaDate is True:
        mi "I talked with Nami about you... I was a little salty after you kept leaving me in the dark."
        mi "Communication is key."
    else:
        mi "But communication is key."
    mi "When she told me about you and how you spent the last few years..."
    mi "That's why I'm asking you to please tell me whenever there's something on your mind."
    mi "Just so that I can understand your motives."
    d "I'll try."
    if MilaDate is True:
        d "About our date."
        d "Let's have it the day after the bar opening."
        mi "Provided we're not too hungover."
        mi "...I will need to go to work that evening, though."
        d "No problem... I mean... We could always just go back to my place after the bar."
        "Mila smirks and raises her brow."
        mi "I'd like that."
    else:
    d "Do you need to work the entire week?"
    mi "Every single fucking day."
    if MilaDaring4x5 is True:
        menu:
            "Mention Garden of Venus to her. (Onlyfans.)":
                $ MilaVenus4x5ID = True
                d "You should make a Venus profile."
                if MilaDate is True:
                    mi "That's a weird thing to say to the girl you're about to date."
                else:
                    mi "That's a weird thing to say to a girl."
                d "Why?"
                d "I've seen pictures there that don't contain any real nudity."
                d "I'm sure your normal dress style would already be enough to gain some following."
                mi "It'd feel like I'm selling out my morals."
                "You get up from the bench."
                d "Ask the people who work 60 hours a week, get treated and paid like shit if morality matters."
                d "Meanwhile some skank not even half as attractive as you makes a few thousand from a picture."
                d "And now guess who's leading a more free and happier life."
                d "But hey... At least they can comfort themselves knowing that their morals are still intact. All while they head to their second job that day..."
                mi "...Maybe you're right."
                d "I'm not telling you what to do... I'm just giving you a different point of view."
                if MilaDate is True:
                    $ MilaVenus4x5 = True
                    mi "The fact that we're dating... or about to date and you'd still say this makes me wanna give it a go."
                    d "It's not like I wouldn't also benefit from you leaving your job."
                else:
                    mi "I don't know... There're pros and cons..."
                d "You'd have much more time to focus on friends and golf."
                mi "...Sounds great."
                d "Remember the picture with the cleavage you posted to Aurora?"
                d "That's all you need to post on Venus... with the difference that you'll get paid for it."
                mi "...That could work."
                d "Just... don't post any other daring pictures to Aurora... otherwise there's not really a reason to subscribe to you."
                mi "I already feel dirty."
                d "Blame the bench."
                "You and Mila take in the view."
            "Don't and be on the watch for a different solution.":
                $ MilaJobLookout = True
                d "I'll keep my eyes open and see if we can find an alternative for you."
                mi "Trust me... I looked."
                d "You looked at normal jobs."
                d "I'll look for more exotic ones."
                d "I'm sure time will bring us something."
                "You get up from the bench."
    else:
        $ MilaJobLookout = True
        d "I'll keep my eyes open and see if we can find an alternative for you."
        mi "Trust me... I looked."
        d "You looked at normal jobs."
        d "I'll look for more exotic ones."
        d "I'm sure time will bring us something."
        "You get up from the bench."
    mi "Would you play golf with me?"
    d "I at least would give it a try, yeah."
    mi "I'll teach you!"
    mi "Is there something you wanted to talk to me about?"
    d "No."
    d "I just want to be here... with you."
    d "We don't necessarily need to talk."
    mi "It says a lot about two people if they can be together without a word being said."
    if MilaDate is True:
    d "Sometimes I... I don't know if it is a dream or an actual memory."
    d "...I hear my mother reading to me. Whenever I sit down and look up to the stars I can recall it."
    d "I think the book she read to me was about the universe."
    "Mila smiles as she snuggles against you."
    d "I... I don't know if it actually happened."
    mi "I'm sure it did."
    mi "And I'm sure she was a lovely person."
    d "I love Nojiko."
    d "I just sometimes wish I could've gotten to know my parents."
    mi "I'm sorry you never did."
    if MilaDate is True:
    else:
    d "I see Nojiko working all day long to support us."
    d "I can see it in her eyes how much she hates working at the hospital... The hours and the stress really get to her."
    d "I wish I could fulfill her dream of having her own little doctor's office."
    mi "Who says you can't?"
    mi "If I've learned one thing growing up poor..."
    mi "Nothing's going to happen if you don't do it yourself."
    d "It's my comfort zone."
    mi "I never experienced a comfort zone. I mean, how would you if you never feel comfortable."
    d "Then you also know that you're the only one capable of changing it."
    mi "And I'm so close to achieving it."
    d "In what way?"
    mi "I've always paid close attention to my spendings."
    mi "This way I managed to save a lot of money... At least enough to get my own place and keep it until college ends."
    d "That's nice."
    if MilaDate or BellaKiss3x5 is True:
        menu:
            "Put your hand on her butt.":
                $ MilaButt4x5 = True
            "Don't.":
                pass

    else:
    mi "I really hope we're all going to move into a place. That would cut down my costs even more."
    d "There might be a thing."
    mi "*Worried* ...What thing?"
    d "There might be a possibility that me and Nami are going to move into Zara's house."
    mi "Uhh- you don't have to... move there... you know?"
    d "True."
    mi "But you want to?"
    d "We'll see."
    d "Having my own place would be much better. I'm not independent enough to support Nojiko."
    mi "Don't worry. It'll happen."
    mi "Just do it at a healthy pace."
    d "I guess I need a job too."
    if MilaDaring4x5 is True:
        mi "Make a Venus account."
        "You let out a small laugh."
    if vicdate is False and (BellaKiss3x5 and MilaEnc03x) is True:
        $ persistent.unlockedImageMilaCh4x517 = True
        "Suddenly, Mila steps towards you and presses her lips onto yours."
        menu:
            "Break the kiss.":
                $ MilaKissBreak4x5 = True
                $ McPa +=2
                d "W-wow Mila... Stop."
                if BellaKiss3x5 and MilaEnc03x is True:
                else:
                mi "I- I'm so sorry! I- thought you gave me a sign- like- like the 'look'!"
                mi "Oh my god! I'm so sorry!"
                d "...It's alright... I'll take it as a compliment... Just please don't do it again."
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
    d "I hope I'll make the playoffs and immediately get into the first team."
    mi "That's very rare."
    mi "Most get into the second team first... and a few months later they move up."
    d "I don't have that kind of time."
    mi "I think a job is inevitable."
    d "I will certainly not wait tables."
    mi "Yeah, don't!"
    mi "What about being a bartender?"
    d "I have no idea how to mix drinks."
    d "I should just rob people."
    d "Do the honest work of a criminal..."
    mi "I might actually have something for you."
    d "What?"
    mi "I have a friend who works at a small store in Prenz."
    mi "They're looking for help."
    d "...What would I need to do?"
    mi "Just help them with uhhh stuff."
    mi "I don't know! We could ask."
    d "*Sigh* Why couldn't you just say... 'Nope, got nothing.'"
    d "Now if I say 'no' it will leave a bad taste and I'll come across as lazy."
    mi "*Giggles* A reaaaally bad taste."
    "Carefully she places her head on your shoulder."
    d "Wanna go back?"
    if MilaKiss4x5 is True:
        mi "I could sit here forever... but yes, I guess we should."
    else:
        mi "Yeah, sure."
    $ achievement.grant("WatchingStarsMila")
    $ achievement.sync()
    if MilaKiss4x5 is True:
        $ MilaLike4x5 = True
        "Mila and you walk back to Victoria's house."
        "As you walk towards the entrance of the house, you realize how elegantly Mila moves her curves."
        "With every step, she swings her butt a little, resulting in her shorts sliding up. "
        "Her confident posture compliments her breasts and overall charisma."
        d "(...I like looking at her.  Maybe I do even like talking to her... Maybe I even like her?)"
        mi "Everything okay?"
        d "(I do like her.)"
    elif MilaKissBreak4x5 is True and MilaDate is False:
        "Mila and you walk back to Victoria's house."
        d "(That was a weird situation... I didn't give her any real signs of attraction... But she still kissed me out of nowhere.)"
        d "(I'll need to keep an eye on her.)"
        mi "Everything okay?"
    d "Wanna scare Vic and Nami?"
    mi "Yes!"
    d "Nami's very easy to scare...  Let's see."
    d "There they are..."
    mi "Vic's so cute."
    d "What are they doing?"
    mi "I have no idea."
    d "I'll go around the corner."
    n "AAAAGH!"
    "Nami's voice stops working mid-scream."
    n "[name]! WE HAD A PEACE TREATY!"
    $ persistent.unlockedImageNamiCh41 = True
    n "YOU BROKE IT!"
    v "[name]! You meany!"
    n "YOU!"
    n "THIS MEANS WAR!"
    v "How was it outside?"
    d "Pretty nice."
    mi "What were you two up to?"
    n "We talked about breasts."
    mi "I have some arguments."
    n "Two very big arguments, if I may say."
    mi "You may."
    $ persistent.unlockedImageNamiCh4x545 = True
    $ persistent.unlockedImageRLWSMila4x5 = True
    jump Ch4x5NachtPart3

label VicWalk4x5:
    $ persistent.unlockedImageVicCh4x65 = True
    $ persistent.unlockedImageR7 = True
    "You just stand there, staring into the night with Victoria on your arms."
    "A long exhale causes Victoria to look at you."
    v "Is everything okay?"
    d "Yes."
    d "Do you want to go up there?"
    v "Sure."
    v "The stars are twinkling so much tonight."
    d "I used to imagine that there was a big space fight happening and the stars reflected the light of the explosions."
    v "Poor aliens."
    v "I'm really glad you and Nami came by."
    d "Already sick of Mila?"
    v "*Chuckles* No."
    v "Mila's amazing. She's so selfless."
    d "That's not always a good thing."
    v "In my opinion it is."
    d "You need to have a healthy amount of selfishness or you'll get nowhere and people will take advantage of you."
    v "I just hope she's not doing it out of pity."
    d "I'm sure she isn't."
    d "You can be... fun."
    d "What's with all the flowers?"
    v "Oh... My parents used to dress me in flower dresses when they were still alive."
    v "Maja used to make fun of me as the 'Flower child'."
    v "I think it reminded her of them..."
    d "That's sweet of her."
    v "Yes."
    v "How's Bella?"
    d "What do you mean?"
    if BTY is True:
        v "She's so different around you."
    v "I saw her in college a few days ago... Watching you from afar."
    v "She looked so cute."
    v "How's she when you're alone with her?"
    d "We insult each other a lot."
    v "But it's not meant as a real insult, right?"
    if BellaKiss3x5 is True:
        d "Right."
    else:
        d "Most of them..."
    d "She's complex... Much more complex than most people give her credit for."
    d "But that's her own fault. She behaves irrationally and out of bitterness."
    d "Apparently she also had some history with Ceril."
    v "Oh."
    d "I'll introduce you to her."
    v "That would be nice."
    v "Can you put me on your lap and put your arm around me?"
    d "Are you cold?"
    v "No, but I'm yearning for your touch."
    d "'Yearning'."
    "Victoria giggles."
    d "(She smells nice.)"
    v "You smell great."
    d "...I just thought the same about you."
    if vicdate is True:
        v "I can't wait for our date..."
    v "Every day I wake up I think about you."
    d "I don't really get it."
    v "Me neither."
    v "Some things aren't meant to be understood. They simply are."
    v "Overthinking will get you nowhere."
    v "I already felt some sort of attraction to you when we first met... Before the accident."
    v "I didn't even need to go where we went... I just followed you for a block to see if we'd talk more."
    d "So... You would've never gone that way and crossed that street if it wasn't for me?"
    v "Yeah."
    "You keep quiet."
    v "It's okay... I appreciate the accident for what it is."
    d "That's such a weird thing to say."
    v "It completely changed the way I see the world... and- and as long as I can learn to walk again... I'll be fine."
    v "If it wasn't for the accident there's no way you and I would be sitting here right now."
    d "Yeah, you might've been sitting here with someone who is just a normal guy."
    v "You're a normal boy... with sad eyes."
    menu:
        "I don't want to be normal.":
            $ McHonest4x5 = True
            d "Normal is what made Summer's parents resent me."
            v "Don't take it personally."
            d "They told me to my face that I was nothing but shit."
            v "They obvi-"
            d "I know Vic. I know that I'm not shit... I know that they were the trash."
            d "But still, I would've made peace with that trash for Summer."
        "That's all I want... A normal life... A normal mind.":
            $ McNormal4x5 = True
            v "And you'll get there."
            if vicpromise is True:
                $ VicErh4x0 = True
                v "Just like I will regain the ability to walk."
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
    v "I think it's nice that you and Nami are going to join a book club."
    d "Is it though?"
    v "Yes!"
    v "I've been reading my whole life and since I'm in the wheelchair, I do read a lot more."
    d "What're you reading?"
    v "Sex."
    d "What?"
    v "*Snobby voice* I've come to appreciate adult literature."
    "Victoria giggles."
    d "Really?"
    v "Yes."
    d "You're unpredictable."
    v "I'm cute... and people think all I do are cute things."
    v "But sometimes! Sometimes I do adult things!"
    menu:
        "Tell me about the book you're reading.":
            $ VicEroticBook4x5 = True
            v "It's about a wife who found her husband cheating... Got divorced and is now on a holiday trip with her best friend."
            d "And I assume they're having lots of fun there."
            v "I've yet to come to a part where they're having fun. At the moment it's just teasing and... Well... it's working."
            d "Do you imagine yourself in those situations?"
            v "*Blushes* Sometimes."
            v "There's so much I want to try out."
            v "I always thought you'd just put your dong in... And that's pretty much it."
            v "But those books taught me about foreplay and how intense it is... or can be."
            if vicdate and Foursome4x5 or VictoriaKiss4x5 or VicDare4x5 is True:
                menu:
                    "Tease Victoria a little.":
                        $ KissedGirl = True
                        jump VicTease4x5A
                    "Don't and enjoy the moment quietly.":
                        d "Tell me more about it on our date."
                        jump VicWalkCon4x5
        "Don't ask further questions.":
            pass

label VicWalkCon4x5:
    if vicdate is False:
        v "And you really don't want to go out with me?"
        menu:
            "Reconsider and go out with her.":
                $ VicDateEntry2 = True
                if MilaDate is True:
                    d "I'm already going out with Mila."
                    v "A-And that's why you should go out with her first... and see where it goes."
                    d "This sounds like a recipe for disaster."
                    v "Y-you worry too much."
                    $ achievement.grant("DoubleAgent")
                    $ achievement.sync()
                else:
                    pass
                d "I'd like to go out with you."
                v "Great!"
            "Sorry, no. I just don't feel like it.":
                $ VicFriend4x5 = True
                v "...I understand."
                "You comfort her as you notice tears running down her face."
                "Victoria can't hold it anymore and starts crying."
    d "(Vic's falling asleep... She's getting heavier.)"
    d "Wanna go back?"
    v "Mhmmm..."
    $ achievement.grant("WatchingStarsVic")
    $ achievement.sync()
    v "Wait, wait..."
    v "Do you wanna scare them?"
    $ persistent.unlockedImageNamiCh4x545 = True
    d "Oh Nami is so easily scared... But I have a peace treaty with her."
    d "...Fuck it. I'll break it."
    d "There they are..."
    d "I'll put you down here."
    n "And then my trebuchets killed Nia's last fort... It was brutal!"
    "Nami enters a state of shock. No sound leaves her body."
    "Nami makes a very weird, whistling sound."
    n "Y-you BROKE THE PEACE!"
    n "You just made the biggest mistake of your life!"
    d "Sorry, not sorry."
    n "Oh... You will be."
    $ fitness +=1
    $ persistent.unlockedImageRLWSVic4x5 = True
    jump Ch4x5NachtPart3

label CheetoWalk4x5:
    $ persistent.unlockedImageR8 = True
    n "It's still so warm... I'm all sweaty."
    d "Let's not talk too much or I'll have to send you back inside."
    n "Wanna check out the area?"
    d "Let's go up there. Check out the forest."
    if Foursome4x5 is True:
        if BellaKiss3x5 is True:
            $ McPa +=2
            n "...So uhhh... Bella."
            "You shoot Nami a look... A clear display of you trying to avoid a conversation that will go nowhere."
            n "You and her are quite close... and as Mila said... it's kinda weird that you did this here with her still being in the picture."
            d "I don't know what I want, Nami."
            n "I'm not judging you..."
            n "But please keep in mind that a relationship that was formed on, quotation marks 'Betrayal', has a looming shadow over it."
            n "Just so that Vic or Mila don't get the wrong idea."
            d "You care too much about what other people think."
            n "I care about what friends think... and so should you."
            n "At least you should care about treating them well."
        else:
            $ McPa +=1
            n "It's funny how you're just you right now..."
            d "What? Did you have a stroke?"
            n "I mean... you just made out with two extremely attractive girls at once... I mean, of course you didn't get the third hot girl there..."
            d "I think the third one looked kind of weird."
            n "You take that back!"
            n "But as I was saying... You just act like nothing happened."
    n "How's therapy going?"
    n "What do you guys talk about?"
    d "Summer... My past... Stuff like that."
    d "I've only had two sessions..."
    n "I see."
    n "It's good that you're opening up."
    d "...Right."
    n "What?"
    d "I have to- yeah, I have to break our deal."
    n "Which one? The one where we don't scare each other anymore?"
    d "No."
    d "The... The deal we made a long time ago."
    "Nami's face turns pale and she takes on a very weird posture."
    n "*Gulp*"
    n "Is that really necessary?"
    "You stand there for a moment, your mouth a little agape and unsure what to say."
    d "I lied to Amber... You are... You are partly responsible for the way I am."
    n "We- [name]... But it shouldn't matter what happened?"
    d "Nami... Try to understand that these things don't just vanish... They still affect me... They're a reason for my lack of impulse control."
    d "And I get the feeling, that all you do is an overcompensation... To make up for-"
    n "It's not!"
    "You squat down"
    d "I hope it's not."
    n "It really isn't..."
    n "But if it helps... Talk about it with her."
    n "You know I would never be like that again."
    d "I know."
    n "And, and if Amber wants me there for a session, I would do it."
    if KoFuNa is True:
    d "I shouldn't have lied to Amber."
    d "I thought I could alter a few details and still get all the benefits..."
    d "But it's about more than just telling her things... It's about *sigh*... coming clean with myself..."
    n "As long as you don't come to a... weird conclusion."
    d "Let's not totally ruin the mood."
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
    n "We will help her achieve that dream!"
    n "YO!"
    "You twitch."
    n "A mosquito wanted to slurp me! You want some, mosquito?!"
    n "Come here and get yaself some!"
    n "Yeah! That's what I thought! Bibiquito!"
    d "*Chuckle* Just shut up..."
    if NamiTni4x0 or NamiCuddle04 and NUE04 is True:
        d "(...I'm looking at her butt.)"
        d "(Since when do I do this?)"
        menu:
            "Slap her butt.":
                $ Cheeto_Butt_Slap_4x5 = True
                n "Yo! Did you just slap my butt?"
                "You slap her butt again."
                n "Do it again! I dare you!"
                menu:
                    "Do it again.":
                        $ Cheeto_Butt_Slap2_4x5 = True
                        n "Do it again! I dare you!"
                        menu:
                            "Do it again.":
                                $ Cheeto_Butt_Slap3_4x5 = True
                                $ persistent.unlockedImageNamiCh4x546 = True
                                n "You actually did it."
                                d "..."
                            "Don't do it again.":
                                n "Little chicken bibi!"
                    "Don't do it again.":
                        n "Little chicken!"
            "Don't do it.":
                pass
    d "What?"
    n "It's nice up here."
    d "Yeah."
    n "We should go on a hike someday."
    d "Stop adding stuff to my plate."
    n "Oh damn! Right, right!"
    menu:
        "Pull her closer.":
            $ persistent.unlockedImageNamiCh4x547 = True
            $ Nami_TNI_4x5 = True
            d "(Why does it feel so right...)"
            "Her little nose pokes yours, as her face approaches yours."
            "You gather all the sanity that's left in yourself to create some distance."
        "Don't pull her closer.":
            pass
    d "Let's go back."
    n "Yes... I'm getting sleepy."
    $ achievement.grant("WatchingStarsNami")
    $ achievement.sync()
    jump Ch4x5NachtPart3








label Ch4x5NachtPart3:
    n "By the way... Where do [name] and I sleep?"
    mi "We thought about building a fort out of blankies and pillows."
    n "Oh yes!"
    n "Remember dude?!"
    d "...I remember our forts."
    n "And, and we pretended that Moogle was our boss and gave us quests."
    v "What's a Moogle?"
    mi "A person who's not a wizard."
    d "It was a street cat... We used to play with it and it followed us everywhere."
    n "I wonder if Moogle's still alive..."
    n "Noji still has that cat tree she bought for him."
    v "I'm getting really tired..."
    n "Me too... It's been a long day."
    mi "Time to build a fort!"
    mi "I'll get the pillows!"
    d "Cheeto, I need a hand."
    v "Hey!"
    n "You're gonna pay for that!"
    if MilaKiss4x5 is True:
        $ McPa +=1
    n "Yo Mila! Where are you? I need your help beating up Vic with a pillow!"
    d "Cheeto, get your ass moving and get us some blankets."
    mi "Come Nami! I'll need help finding the blankies."
    if VicTiddyTease4x5 is True:
        $ McPa +=1
        d "I'm trying to build a fort here."
        v "And I'm trying to keep you from it!"
        "She kisses your forehead."
        n "Hey you jerks!"
        n "Stop making out while we do all the work!"
    else:
        pass
    mi "Get in!"
    d "I need to use the restroom."
    mi "What're you doing, Nami?"
    n "I miscalculated! I thought I could turn around in here but NO! Now I'm stuck in here forever!"
    if BellaKiss3x5 and Foursome4x5 or VictoriaKiss4x5 or MilaKiss4x5 is True or McPa >1 or Foursome4x5 is True:
        $ McPa -=2
        $ Mc_Panic4x5 = True
        "Your breathing accelerates."
        "Sweat breaks out."
        "You gasp for air..."
        "Your heart pounds through your chest."
        d "(Come on... Calm down... calm down... please...)"
        d "(Not now...)"
        "You manage to calm your heart rate down."
        d "(It'll stop... I just have to get through this...)"
    d "Why are there clothes here?"
    mi "Well... sleeping with clothes, in a more or less airtight and body filled fort is gonna suck."
    v "It'll get really warm."
    d "You guys still have clothes on... right?"
    n "Underwear."
    d "I might take the couch."
    mi "No way."
    v "You'll get in here! It's a fort for us all!"
    d "Alright... I don't see an entrance."
    mi "Nami, can you make some space?"
    $ persistent.unlockedImageMilaCh4x518 = True
    n "S-sure."
    d "I'm glad there's enough space here..."
    d "... I guess that does it."
    v "It really does..."
    d "You're not wearing a bra?"
    v "I'm wearing a strapless one."
    v "I can take it off if you want?"
    d "No, no."
    n "I'm not wearing one."
    menu:
        "Tiddy-Joke.":
            $ NTJ +=1
            d "I mean... Why would you? There isn't much to fall out."
            n "WOW! YOU- WOW!"
            n "YOU SUCK!"
            mi "You're so mean!"
            mi "Her breasts are amazing!"
            n "Tell him!"
            v "That's soooo mean, [name]!"
            d "I'm obviously joking... partially."
            n "I will make you eat your words one day!"
            n "Or my tits!"
            mi "*Laughs* Nami!"
        "Don't joke on Nami's expense.":
            $ Nami_SB +=1
            d "You don't need to."
            n "...Why is that?"
            d "You've got some very good connective tissue."
            "Nami squints her eyes even further..."
            n "Thanks!"
            mi "And here I am with just decent tissue."
            n "Yeah but your tits are also gigantic!"
            v "Much bigger than mine!"
            mi "I don't think so... Yours are pretty big."
            v "Yours are sooo much bigger."
            mi "Hmm,  maybe a little."
    n "I wonder how Summer's breasts would be..."
    d "She started developing some... breasts when we last saw each other."
    n "I bet she was also blessed by the boob gods."
    v "Just like Bella."
    $ persistent.unlockedImageVicCh4x67 = True
    n "They're not that great."
    mi "Her tits are quite nice."
    n "Come on girl... Back me up here..."
    mi "Sorry hun."
    v "I really want to get to know Bella."
    d "I also want you to get to know each other."
    mi "Why would you want that?"
    d "Bella's a jerk, but she isn't two-faced."
    d "You and Bella would be great together too. If it wasn't for your history."
    v "What isn't can still be!"
    v "I'll talk to her."
    mi "Vic..."
    mi "You can hang out with Bella... but Bella and I will never be friends."
    v "If I can learn to walk again... then you can become friends with Bella."
    mi "I don't want to become friends with her."
    n "Anyways... Nadia."
    mi "What about her?"
    n "I like her."
    n "She's coming to my place soon for some gaming adventures."
    mi "I like her too."
    mi "She can be a little weird at times but overall she's a nice girl."
    v "Why is she weird?"
    mi "She is uhh... a little too much into fantasy."
    n "I like that about her."
    mi "I was once at one of Nancy's parties and-"
    n "OH! We got invited to one."
    mi "Be careful... It can get really weird real fast."
    n "Why?"
    mi "It's almost always just girls there... and it can turn 'weird' real fast."
    mi "If you're going there, [name]... You'd better be prepared."
    mi "It's like a bunch of horny farm girls."
    n "Oh."
    n "But [name] didn't want to go anyways."
    d "(She doesn't want me to go now...)"
    menu:
        "I'll go.":
            $ NancyParty4x5 = True
            n "What? I thought you didn't want to?"
            d "But Nancy asked me and I want to give it a try."
            n "There will be other parties we can go to."
            n "What Mila describes sounds stressful."
            d "Hey, don't worry..."
            d "You can stay home and I'll go alone."
            n "...No."
            mi "I mean... We can also go Vic?"
            v "But- my chair won't be able to drive."
            if vicdate is True:
                mi "I'm sure [name] will carry you around."
                v "Yay!"
            else:
                mi "I'm sure we'll find some hot farm boy to carry you around."
                v "*Giggles*"
        "Right, I didn't.":
            $ NancyParty4x5 = True
            mi "If you decide to go... Vic and I might also come."
            v "Yay!"
            v "But- my chair won't be able to drive."
            if vicdate is True:
                mi "I'm sure [name] will carry you around."
                v "Yay!"
            else:
                mi "I'm sure we'll find some hot farm boy to carry you around."
                v "*Giggles*"
    d "Can we sleep now?"
    if NiaDeal is True:
        d "I have to see Nia tomorr- today."
    v "Alrighty!"
    jump Morning4x5




label Morning4x5:
    v "*Whisper* [name]?"
    d "Mhh?"
    v "*Whisper* I need to pee."
    d "Should I wake up Mila?"
    v "You could also help me?"
    if UmB is True:
    else:
    if UmB is True:
    else:
    if UmB is True:
    else:
    d "Do I just put you on there?"
    $ persistent.unlockedImageRS61 = True
    v "Yes, but you'll need to stabilize me at the beginning..."
    v "And help me pull down my shorts."
    d "You'll need to get up again... Lean yourself on me and I'll pull them down."
    "Victoria leans over your shoulder."
    "You put her back on the throne."
    d "I like your confidence."
    v "Is it confidence, though?"
    v "Or is it just me not caring anymore."
    d "I think it's a mix between those two."
    d "Can you-"
    v "Yes, I can do it myself."
    "Victoria cleans herself up."
    v "What're you thinking about?"
    d "Nothing really."
    if UmB is True:
    else:
    d "Ready?"
    if UmB is True:
    else:
    v "Yes!"
    $ persistent.unlockedImageVicCh4x68 = True
    "You carry Victoria backwards outside the bathroom to close the door."
    v "Maja!"
    maj "Hi honey."
    v "You're back early!"
    maj "I am."
    v "What happened? Why are you back?"
    maj "We all change as time goes on... The connection we once had was gone."
    d "I need to pee. Would you mind taking her off my arms?"
    maj "Sure."
    if UmB is True:
    else:
    "You leave the restroom a few minutes later."
    maj "You fucking creep."
    d "What?"
    $ persistent.unlockedImageMaja2 = True
    maj "You went through my stuff."
    d "The others did."
    maj "Okay."
    if UmB is True:
    else:
    d "You believe me? Just like that?"
    if UmB is True:
    else:
    maj "Yeah... You're not the type for that."
    maj "I know how girls can be when they get together in a group."
    maj "We get darey whenever friends are around... Be careful when big groups of girls get together."
    if Foursome4x5 is True:
        d "...I can imagine."
    else:
    maj "Did you arrive with Mila?"
    d "No, Nami and I arrived later at night."
    maj "You look different."
    d "Different how?"
    maj "More alive."
    maj "The first time I saw you... you looked awful. Kind of psychotic and dead inside."
    maj "Don't get me wrong, you still look dead and psycho."
    maj "But not as much anymore."
    maj "I think it's the influence Victoria has on other people."
    d "I won't deny that Vic has an influence on me... But you won't change without wanting so yourself."
    if BellaKiss3x5 is True:
        $ MajaBellaIn4x5 = True
        d "And... I think this is more Bella's doing than Victoria's."
        maj "Bella?"
        d "Yeah."
    else:
        maj "That's great to hear."
    if MCNipplePump is True:
        $ MajaFetishBDSM = True
        maj "Wait a minute!"
        maj "Did you use my nipple pump?"
        d "They made me do it."
        maj "You fucking spastics!"
        "Maja squeezes your nipple slightly between her two fingers."
        maj "Now I have to throw them away!"
        maj "I swear if I find out one of my toys entered you I-"
        d "What no?! No toy entered me!"
        maj "I hope you're telling me the truth, otherwise I'll make you suffer."
        d "...How?"
        maj "Tie you up and make you squeal."
        d "Is that your fetish?"
        maj "My- what? Dude? You can't just ask me that?"
        d "Why not? You just said you would tie me up."
        maj "Yeah, but I am a girl?! You don't ask a girl that!"
        d "I believe in real equality."
        maj "...It's not my fetish but I like bondage and some soft BDSM."
        d "So it's safe to assume we didn't see your full collection."
        maj "*chuckles* Not even half."
        d "Don't tell them or they will try to find it."
        maj "Those weirdos..."
        d "They've got no respect."
    else:
    n "Morning!"
    d "Morning."
    maj "Hello Nami."
    $ persistent.unlockedImageNamiCh4x548 = True
    n "Huh! Maja!"
    n "It's great to see you!"
    n "How are you?"
    maj "I am fine and you?"
    n "I'm good!"
    n "Do we have some coffee?"
    maj "I'll pour some."
    n "[name], yo!"
    if NiaDeal is True:
        $ MajaJoke4x5 = True
        d "I'm thinking about canceling Nia."
        n "You won't."
        d "I won't... I gave her my word."
        n "Use a condom, though."
        d "We do have something in common Maja."
        d "We both have a disabled roommate."
        n "Wow! Cheap shot!"
    else:
        d "Cheeto."
    $ persistent.unlockedImageMaja2 = True
    mi "Good morning!"
    maj "Morning Mila!"
    mi "Should we all have breakfast together?"
    n "Sure!"
    d "Where's Vic?"
    mi "In the living room."
    d "I'll get her."
    d "Hey, do you want me to carry you over?"
    v "Yes."
    v "Everyone left and well... I couldn't follow."
    d "Let me put your top on."
    maj "You look beautiful."
    v "That's your doing!"
    maj "Alright... Who'll go with me to the bakery?"
    v "Me!"
    n "Me too! I need some fresh air."
    n "And I need to inspect their selection of rolls."
    mi "Thanks."
    mi "Have you seen Miss Marla lately?"
    d "Why?"
    mi "She changed her hair and style. It looks nice on her."
    d "I guess."
    mi "Maybe it was due to the talk she had with Vic."
    d "They had a talk?"
    mi "Yes. Three days ago."
    if mmc is True:
        d "Did she say how it went?"
        mi "Vic said it went well."
        d "(Marla didn't look so great... I wonder if it was because of the talk.)"
        d "(Amber must know... I'm sure Marla told her about it.)"
        d "(Bella could help me take a look at the files... It'd be interesting to see what they actually talked about.)"
        d "I see."
    else:
        d "That's nice, I guess."
    mi "I respect Victoria for actively engaging with her."
    mi "You can't tell me that it's easy..."
    d "It isn't."
    if MilaKissBreak4x5 is True and Foursome4x5 is False:
        mi "I wanted to apologize for... kissing you."
        d "No hard feelings... It just felt really wrong."
        mi "*Sigh* Sorry."
        d "Why did you do it?"
        mi "It just felt... right?"
        d "No... There was something in the air since you heard about Bella and me."
        d "Your body language has changed."
        mi "It's nothing [name]... I was just stupid."
        "You raise a brow and take a sip from your coffee."
    elif MilaKiss4x5 is True:
        mi "I liked our kiss."
        if BellaKiss3x5 is True:
            $ MiEH4x5 = True
            d "I would've too if there wasn't this underlying feeling."
            mi "... What do you mean?"
            d "Since you heard about me and Bella... Your body language towards me has changed."
            d "It's in some way aggressive."
            mi "Oh- uh... I didn't mean to come across like that."
            d "But you did."
            mi "Is it so bad to not always be the one left empty handed? The one that always watches from the sidelines?!"
            mi "...Sorry."
            d "It's alright. I can imagine."
        else:
            d "I liked it too."
            d "I would've preferred waiting for it to happen on our date..."
            mi "No no Mister... You don't always need to be in control."
            mi "Sometimes it's best to go with the flow."
            d "It reminds of our first talk... Going with the flow has made you not approach the girl."
            mi "...I was talking about 'love' related things."
            d "And what you did was not 'going with the flow'. You took action."
            d "I respect that very much."
            mi "You really need to work on that."
            d "Not as hard as your bra."
            mi "Wow!"
            d "Hey, it could've been a compliment about your well developed breasts."
            mi "It sounded a lot like you were calling my boobs saggy!"
            d "I didn't mean that. I haven't seen them yet."
            mi "*Smirks* Who says you ever will?"
    elif Foursome4x5 is True:
        mi "I'm still in denial about last night."
        d "It's not like much happened."
        d "It was just kissing."
        mi "And touching... Lots of touching."
        d "It was just in the spur of the moment."
        mi "Right."
    d "They're taking their sweet time."
    if MilaKiss4x5 is True:
        $ persistent.unlockedImageR9 = True
        "She takes the mug out of your hand."
        "She stares into your soul."
        mi "Tell me if I'm too heavy."
        d "You're not."
        "Mila closes in... Her nose slightly touching yours."
        "She moves in closer, stops and creates a drumroll."
        "Mila guides your hand to her breast."
        "She disconnects the kiss."
        mi "More coffee?"
        d "Yeah."
        "As Mila gets up, she 'accidentally' moves your head between her breasts."
        d "Huh."
        mi "What?"
        d "I took a peek at your butt."
        $ persistent.unlockedImageMilaCh4x520 = True
        mi "I never thought I'd be happy to hear those words... But here I am!"
        if milagym is True:
            d "Actually... I also looked at it before when your pants ripped at the gym."
            mi "Fuck... I hope you'll forget about it soon."
            d "I'll never forget anything... Especially not potential blackmail material."
            mi "HEY!"
            "You chuckle."
    else:
        d "Probably Nami's fault."
        d "It takes ages for her to decide on the right rolls."
    $ persistent.unlockedImageMilaCh4x519 = True
    if bellagym is True:
        $ BibiBellchen4x5 = True
        d "Bella once mentioned that you did something to her... What was it?"
        "Mila freezes."
        mi "Uhh..."
        mi "*sigh*"
        mi "In middle school..."
        mi "Bella was kind of an outsider... Like me."
        mi "But we didn't speak or have anything to do with each other."
        mi "And as you know, I was being bullied for being poor... and some other things."
        mi "And I did something really horrible."
        d "You joined them..."
        mi "I said something mean..."
        mi "I was a little child... And if they bullied Bella they would stop bullying me, right?"
        mi "It made me feel like I was part of a group... But most importantly, it took me out of the crosshair."
        mi "But it didn't go on for long."
        mi "One day during lunch..."
        mi "She sat there at the table with her little milk."
        $ persistent.unlockedImageBellaCh47 = True
        $ persistent.unlockedImageRS63 = True
        mi "And Melanie picked on Bella because Amber complained about her to the school."
        mi "And Melanie threw herself onto her back and Bella hit the table really hard..."
        mi "She pulled her hair and made her fall from the chair."
        mi "She started crying so much..."
        mi "It broke my heart..."
        mi "I took all my pent up frustration, my pain, and all the courage I could muster..."
        mi "And stepped in."
        mi "Which put me back in the crosshair..."
        mi "But at least I stood up for my principles..."
        mi "I apologized to Bella hundreds of times... She never forgave me."
        mi "Bella and I are very different... but we did share a fate in middle school."
        mi "I think if I hadn't wronged her once, we could have become friends."
        d "The people who picked on her... Was it that Mario guy?"
        mi "No. He was actually a nice guy back then. He even defended me and Bella sometimes."
        mi "It was mostly just Melanie and her clique."
        d "How come you are so anti-Bella even though you knew what she was going through?"
        mi "I'm not anti her!"
        d "You are."
        d "Recall our first conversations about her."
        mi "Shit... I think I took it personal that she didn't accept my apology... and that she started to pick on me in high school."
        mi "Then Bella met Ayua and the tables turned. Ayua was no one to joke with."
        mi "Just in case you didn't know... Ayua's last name is Zane."
        mi "Main sponsor of our college."
        d "I'm aware.."
        mi "When Ayua came into the picture people let off Bella..."
        mi "It also helped that Bella became rather pretty."
        mi "As you can imagine... Bella then started to pick on the people who picked on her."
        mi "When I say Bella is weird, I mean that she's obsessed with revenge."
        mi "In a very, very unhealthy way."
        d "What did she do to you?"
        mi "Besides calling me poor and stuff? Not much."
        mi "But she did do some 'things' to some of the other people that are-"
        d "Don't tell me."
        d "I'll ask her myself."
        mi "Yeah, I think that's for the best."
        d "But... she isn't a bad person... Far from it."
        mi "...I know."
        menu:
            "Neither are you.":
                $ MNABP4x5 = True
                if MilaKiss4x5 is True:
                    $ persistent.unlockedImageMilaCh4x521 = True
                    $ McPa +=1
                    if UmB is False:
                    else:
                else:
            "Don't comfort her.":
                $ MTBP4x5 = True
                pass
    maj "Mh."
    v "What is it?"
    maj "Mail from ZPR."
    maj "You also got one."
    "Maja opens the envelope."
    maj "Seems like I've got the job."
    mi "As what?"
    maj "Assistant coach at your college."
    mi "That's awesome!"
    maj "I think we'll see each other a little more in the future."
    "They all look at you."
    d "Mh? Should I be excited?"
    v "Yes!"
    mi "YES!"
    n "*Chewing* MHMM!"
    d "Yay."
    maj "Vic, drink your juice."
    v "I will!"
    maj "Otherwise, I'll tell everyone here about your juice box incident in middle school."
    v "Nooo!"
    v "See! I'm drinking it!"
    n "Want a roll?"
    d "What?"
    d "You'd never give a roll away."
    n "I feel generous today!"
    maj "Thanks for the company guys."
    maj "I need a really long bath... If I don't see you two when I get out, thanks for keeping Vic company."
    n "Sure!"
    d "By the way... You guys fucked up."
    d "Maja knew someone went through her stuff."
    mi "Oh no..."
    d "I totally snitched you guys out."
    n "Wow!"
    mi "You should've taken the hit!"
    d "No way I'd take that specific hit."
    d "As a guy, you'd never lose the 'creep' reputation."
    n "We should apologize next time we see her..."
    if MCNipplePump is True:
        mi "But it was sooooo funny."
        v "It was!"
    d "Alright Cheeto, we should go."
    if NiaDeal is True:
        d "I really need some sleep before I head to Nia."
        n "Maybe it's better if you don't go."
        "You raise a brow."
        n "It could be too much... You're already pushing it."
        d "I'll be fine."
    if VictoriaKiss4x5 is True:
        d "Vic, it was nice and thanks for the pizza."
    else:
        d "Vic, it was nice and thanks for the pizza."
    v "Thanks for coming by! It meant a lot to me."
    n "Awwww. Goodbye sweety!"
    v "Bye Nami!"
    if MilaDate is True:
        $ persistent.unlockedImageMilaCh4x522 = True
        d "I think we'll see each other very soon."
        mi "I hope so."
        mi "Don't worry. You'll get used to the touching..."
        mi "But seriously... Let's do something together soon."
        d "Yeah, I'd like that."
    else:
        d "Bye Mila."
        mi "Goodbye! Thanks for coming!"
    jump End4x5

label End4x5:
    "You take a deep breath."
    n "Those birdies are loud as fuck."
    d "Sounds like you've got a hangover."
    n "YOU'll TAKE THAT BACK!"
    n "I'm invincible! Alcohol WHO?! Am I right?!"
    n "See, this is how my kind walks."
    if OeVaGe4x0 and NamiCuddle04 or HcNaFrt or NamiCuddle04 and Nami_TNI_4x5 is True:
        $ persistent.unlockedImageR10 = True
        d "(Hmm...)"
        d "(Something in my perception has changed.)" #cheeto
        d "(Nami's presence makes me feel comfortable... but this is different.)"
        d "(I have a slight urge to look at her... A feeling in my belly.)"
        if NamiLove4x0 is True:
            d "(I'm aware that she's probably in love with me...)"
        else:
            d "(I suspect that she's in love with me.)"
        d "(Do I also have feelings for her?)"
        d "(I'm confused... and overwhelmed.)"
        n "Man... Carry me home..."
        "Nami's touch sent a shiver through your spine."
        d "(There's more...)"
        n "Yo!"
        d "Shut up Cheeto."
        d "I'm having an inner monologue."
        n "About what?"
        d "Confusion."
        n "It happens! That roll I gave you wasn't for beginners."
        d "What makes you think it's about some roll?"
        n "Dude. Life's about rolls!"
        d "(It's those little things that make her special...)"
        d "(Her stupid humor.)"
        n "Oh yeah! I can see it on your face!"
        n "You're thinking about rolls, aren't ya?!"
        d "Yeah, a very special roll."
        n "Oh! Was it the one with the poppies on top?"
        d "Nah, the one that might have been dropped a few times when it was still a bibi roll..."
        n "...Wait what?"
        d "Our bus."
    else:
        d "(Hmm...)"
        if (miladate or MilaDate) and VicDateEntry2 is True:
            d "(Mila and I are meeting up soon... And on top of that I also agreed to see Vic.)"
            d "(I will have to decide sooner or later.)"
        if miladate is True:
            d "(Mila and I are meeting up soon..."
            d "(I'll have to tell her about my... issue.)"
        elif vicdate is True:
            d "(Vic and I are going out soon... She'll definitely understand my issue.)"
            d "(She's not one to judge.)"
        n "Yo!"
        d "Shut up Cheeto."
        d "I'm having an inner monologue."
        n "About what?"
        d "Confusion."
        n "It happens! That roll I gave you isn't for beginners."
        d "What makes you think it's about some rolls?"
        n "Dude. Life's about rolls!"
        d "(Her stupid humor.)"
        n "Oh yeah! I can see it on your face!"
        n "You're thinking about rolls, aren't ya?!"
        d "Yeah, a very special roll."
        n "Oh! Was it the one with the poppies on top?"
        n "I bet it was!"
        d "Our bus."
    n "Finally..."
    n "I've never wanted to sleep this badly before!"
    n "Even the floor looks cozy!"
    "She plops off her shoes."
    n "NIGHTY!"
    d "Good night."
    if OeVaGe4x0 and NamiCuddle04 or HcNaFrt or NamiCuddle04 and Nami_TNI_4x5 is True:
        d "(...I could just tell her how I feel? How I think I feel?)"
        d "(There's no need to play around... No need to add another thing to my mental luggage.)"
        menu:
            "Tell Nami about your change in perception.":
                $ KissedGirl = True
                $ persistent.unlockedImageR11 = True
                $ NamiLove4x5 = True
                d "Cheeto?"
                n "Yo?"
                "Nami freezes immediately."
                "But regains her composure a few seconds later..."
                "Nami pushes her tongue into your mouth, her arms around you, pulling you in closer."
                jump NamiKiss4x5A
            "Keep it to yourself for now.":
                $ NamiNoLove4x5 = True
                if BellaKiss3x5 is True:
                    jump BellaEnd4x5
                else:
                    jump EndScreen4x5
            "There's no change in perception.":
                $ Nami_No_Perception4x5 = True
                if BellaKiss3x5 is True:
                    jump BellaEnd4x5
                else:
                    jump EndScreen4x5
    else:
        if BellaKiss3x5 is True:
            jump BellaEnd4x5
        else:
            d "I should go to bed... I have a long day ahead..."
            jump EndScreen4x5

label BellaEnd4x5:
    $ BellchenEnd4x5 = True
    $ persistent.unlockedImageCh4x51 = True
    if Nami_No_Perception4x5 or NamiNoLove4x5 is True:
        "You make out a low, familiar rumble outside..."
    else:
        "A low, familiar rumble pulls you out of it."
    $ renpy.pause(4.5, hard=True)
    jump EndScreen4x5



label EndScreen4x5:
    $ persistent.unlockedImageBellaCh46 = True
    jump StartChapter5
