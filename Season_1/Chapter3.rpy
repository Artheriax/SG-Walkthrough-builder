

label startch3:
    $ achievement.grant("Chapter2Done")
    $ achievement.sync()
    $ play_playlist(playlist_AmbientCheeto)
    scene c1 with Dissolve(3)
    d "(I can feel her lips trembling.)"
    v "I-"
    scene c2 with vpunch
    may "Oh Victoria..."
    v "M-Maja."
    scene c3 with dissolve
    may "Ohh Victoria, sweetheart!"
    scene c4 with Dissolve(2)
    may "*whisper* We're here for you."
    v "Than-k you."
    may "Don't worry, everything is going to be fine."
    v "Mh-hm."
    scene c5 with dissolve
    u "*giggle* Good evening."
    scene c6 with dissolve
    u "You must be Victoria Frohn. Hi."
    v "*visibly nervous* Yes... that's me."
    scene c7 with dissolve
    u "Oh, you don't need to be nervous.  If it helps, you can return to your group cuddling session, and I'll come back in two minutes."
    scene c8 with dissolve
    v "I- am good."
    u "Victoria, let me introduce you to my team."
    $ persistent.unlockedImageCeli1 = True
    scene c9 with dissolve
    v "Maj-a can you t-two wait here?"
    scene c10 with dissolve
    may "I'll be here, don't worry."
    scene c11 with dissolve
    d "I will wait, too."
    scene c13 with dissolve
    v "Tha-nks."
    scene c14 with Dissolve(2)
    may "..I think I misjudged you."
    "You stay silent."
    may "Do you know what I thought about you at first?"
    scene c15 with dissolve
    d "I don't want to know."
    scene c16 with dissolve
    may "Why are you suddenly so reluctant?"
    scene c15 with dissolve
    d "I... feel extremely vulnerable right now."
    may "We-"
    scene c17 with Dissolve(1.2)
    d "And... I assume you've heard what I told her..."
    may "I did."
    d "*sigh*."
    scene c18 with dissolve
    may "I won't make fun of you if you-"
    d "That's not the part that worries me."
    scene c19 with dissolve
    may "Then which is it?"
    d "I may have burdened myself with something I can't carry."
    scene c20 with dissolve
    may "What do you think happened to Victoria just a few minutes ago?"
    may "She wasn't able to carry her burden alone."
    may "And, I- wasn't strong enough to help her by myself."
    scene c21 with dissolve
    may "But... together we can all help each other... because, just like you said to Victoria a few minutes ago..."
    if vicpromise is True:
        scene c22 with dissolve
        may "[name]. You're not alone."
        scene c23 with dissolve
        menu:
            "Hold her hand.":
                scene c24 with dissolve
                $ majalove +=1
                "You slowly nod."
            "Remove her hand.":
                scene c25 with dissolve
                d "But I feel alone.."
                pause
    else:
        scene c22 with dissolve
        may "[name]. You're not alone."
        scene c25 with dissolve
        d "Then why do I feel so alone?"
    scene c26 with dissolve
    d "...Where are your parents?"
    scene c27 with dissolve
    may "They're both dead."
    may "Our parents were in their mid 40s when I was born... and even older when Vic was born."
    may "My mother died when she was 67, and my dad died a week before his 65th birthday."
    scene c29 with dissolve
    "You stay silent."
    scene c30 with dissolve
    may "Do you still have your parents?"
    menu:
        "Tell her":
            $ maja +=2
            scene c31 with dissolve
            d "I lost my parents at the age of three... So did Nami."
            scene c32 with dissolve
            may "I am sorry to hear that."
            scene c31 with dissolve
            d  "It doesn't matter. I can't remember them anyway."
            scene c32 with dissolve
            may "Still, children shouldn't grow up without their parents."
            scene c31 with dissolve
            d "That depends on the parents."
        "Don't tell her":
            scene c31 with dissolve
            d "I don't want to talk about this."
            scene c32 with dissolve
            may "I understand. Sorry that I asked."
    if vicdate is True:
        scene c33 with dissolve
        "Maja lets out a little laugh."
        d "Mh?"
        may "I didn't know what to think when Victoria told me that she was about to go on a date with you."
        may "She was so happy. Telling me things she wanted to do with you."
        d "A weird thing to tell you."
        scene c34 with dissolve
        may "Oh no... Not those types of- things."
        if vicpromise is True:
            $ persistent.unlockedImageVic5 = True
            scene c35 with dissolve
            may "She was daydreaming about the date."
            scene c36 with Dissolve(2.4)
            may "She was imagining you in some nice clothes... a nice dinner, later a quick ice cream and then she stopped for a second."
            may "She was just staring into the room... Her smile did vanish for a second but immediately came back and vanished again... her lips were trembling, slightly."
            scene c37 with dissolve
            may "Then she started to smile again and asked me... 'Do you think he'd kiss me'?"
            scene c38 with Dissolve(2.4)
            may "Her eyes were glowing... Like I have never seen before..."
            d "And... What did you say?"
            may "*Maja stays quiet for a second* I told her that she has to find that out by herself... and that if it happens... she should just enjoy the moment."
            "You both go silent again."
            d "Is there a reason why you shared such an intimate moment with me?"
            scene c39 with dissolve
            may "To be honest? No."
            may "I think it just touched me. It's a side I haven't seen from her before and I'm getting all mushy from it."
            "*She takes a deep breath*"
        scene c40 with dissolve
        may "Please.. don't break her heart."
    else:
        pass
    scene c41 with Dissolve(2)
    u "Miss Frohn?"
    may "Yes?"
    cel "My name is Celina. My boss wants to see you to go over some documents you need to sign."
    scene c44 with dissolve
    may "Of course."
    scene c45 with Dissolve(3)
    "You let out a long *sigh*."
    d "(My mind is blank and overflowing with thoughts at the same time... I don't know what to think about all this.)"
    d "(How did I get so deeply involved with these people?)"
    scene c47 with dissolve
    d "(Instead of wasting my time here, I could take a look around.)"
    "You can hear Victoria's soft voice in the distance."
    scene c48 with dissolve
    pause
    if vicdate is True:
        scene c49 with dissolve
        d "(I am starting to like her smile... It annoyed me at first... but it... somehow radiates warmth and youth.)"
        scene c50 with dissolve
        d "(I can't help but wonder what would've happened if Noji didn't send me to the bakery...)"
        scene c52 with dissolve
        d "(A life changing event because of some bread rolls..)"
        scene c53 with dissolve
        d "(Victoria somehow resembles the opposite of... Summer... Her blonde bright hair, the brown/yellow eyes and her soft, melodic voice.)"
        scene c54 with dissolve
        d "I wonder where this journey will take us."
        scene c55 with dissolve
        d "I can't get past this feeling that our paths were meant to cross."
        scene c57 with Dissolve(2)
        pause
        if vicdate is True:
            scene c60 with Dissolve(2)
            d "(I sincerely hope you will be able to walk again.)"
    else:
        scene c57 with Dissolve(2)
        pause
        scene c60 with Dissolve(2)
        pause
    $ persistent.unlockedImageVic1 = True
    stop music fadeout 3.0
    scene black with Dissolve(2)
    with Pause(0.5)
    $ play_playlist(playlist_Ch4x5v)
    scene m1 with Dissolve(2)
    pause
    scene m2 with dissolve
    d "Hey!"
    scene m3 with dissolve
    n "Hey."
    n "Where were you?"
    scene m4 with dissolve
    d "I had to meet up with Victoria."
    scene m6 with dissolve
    n "Ohhhh! Tell me everything!"
    d "She was about to break down... All shaky and stuff."
    n "Oh what?! Why?"
    scene m7 with dissolve
    d "*Exhausted sigh*"
    d "She was at the physiotherapy center and... couldn't handle it."
    d "Maja called me."
    scene m8 with dissolve
    n "Maja?"
    d "Mhm."
    scene m9 with dissolve
    n "How did it go?"
    d "For Victoria, good."
    n "And for you?"
    scene m10 with dissolve
    $ Nhl = True
    jump NHL3
label NHL3:
    with Pause(.7)
    scene m11 with dissolve
    if vicpromise is True:
        d "I might have burdened myself with something I can't carry."
        n "If you need help, I can take care of her, too."
        d "No, it has to be me. Maja couldn't help her either."
        scene m12 with dissolve
        n "Then let me try to help you at least."
    else:
        d "I'm fine."
    scene m13 with dissolve
    n "Nojiko called and said she'll be home late."
    n "Should we order some food?"
    d "Pizza?"
    if bellameet is True:
        if Nhl is True:
            play music "music/Suspense/Scott Buckley - Resonance.ogg"
            scene m14 with vpunch
            n "Pizza!? Why not caviar and a flask of Katie's Sky, year 1965!?"
            pause
            scene m15 with dissolve
            d "Mhhh!?"
            $ persistent.unlockedImageNami3 = True
            n "Where the fuck did you get that 10k from!?"
            scene m16 with dissolve
            d "You searched my room?!"
            scene m17 with dissolve
            n "Yes! I did!"
            scene m19 with dissolve
            d "Nami what the fuck!?"
            d "You're a person I'm supposed to trust!"
            scene m18 with dissolve
            n "[name]... I-"
            scene m20 with dissolve
            d "No! Nami this- this is-"
            scene m21 with dissolve
            n "Listen! I only did it because I care about you!"
            scene m20 with dissolve
            d "Oh shut up! You're a fuck-"
            "You push her away."
            scene m22 with dissolve
            n "[name]! Just imagine if I left the house in the middle of the night to do who knows what!"
            n "You would do the exact same thing to make sure I didn't do something stupid!"
            scene m23 with dissolve
            d "I-"
            d "Just leave me alone.."
            scene m24 with vpunch
            "As you leave you brush against her shoulder."
            scene black with Dissolve(1.5)
            with Pause(0.5)
            stop music fadeout 4.0
            d "*sigh* (I can't believe that she would go so far..)"
            d "(...I mean, I guess in some way I can understand why she did it...)"
            d "(I would've probably done the same at some point if she acted all weird and vanished without saying why.)"
            jump NE3
        else:
            scene m25 with dissolve
            "As you stare at the ground... you can feel the mood of the room change... A glare is piercing through your body."
            scene m26 with dissolve
            n "Mind answering me something - she says in a serious tone."
            d "Mh?"
            play music "music/Suspense/Scott Buckley - Resonance.ogg"
            n "Where the fuck did you get that 10k from!?"
            scene m27 with vpunch
            d "You searched my room?!"
            scene m28 with dissolve
            n "...I was worried about you. I-"
            scene m27 with dissolve
            d "Nami what the fuck!?"
            scene m28 with vpunch
            d "You're a person I'm supposed to trust!"
            scene m30 with dissolve
            n "TRUST?! You don't even talk to me!"
            scene m31 with dissolve
            d "No! Nami this- this is-"
            scene m21 with dissolve
            n "Listen! I only did it because I care about you!"
            scene m20 with dissolve
            d "Oh shut up! You're a fuck-"
            "You push her away."
            scene m22 with dissolve
            n "[name]! Just imagine if I left the house in the middle of the night to do who knows what!"
            n "You would do the exact same thing to make sure I didn't do something stupid!"
            scene m23 with dissolve
            d "I-"
            d "Just leave me alone.."
            scene m24 with vpunch
            "As you leave, you brush against her shoulder."
            scene black with Dissolve(1.5)
            with Pause(0.5)
            stop music fadeout 3.0
            d "*sigh* (I can't believe that she would go so far..)"
            d "(... I mean, I guess in some way I can understand why she did it...)"
            d "(I would've probably done the same at some point if she acted all weird and vanished without saying why.)"
    else:
        jump pizza03

label pizza03:
    scene m34 with dissolve
    n "Sure! On me!"
    scene m36 with dissolve
    n "Hello!"
    n "I'd like to order some pizzas... one with tuna and one with... pineapple."
    scene m39 with dissolve
    d "For me one with shrimps and one with salami."
    scene m38 with dissolve
    n "Yea, and uhhh- one with shrimps and another one with salami."
    scene m42 with dissolve
    n "Uhh... Yes, I have a bonus card."
    scene m43 with dissolve
    n "Mhm... interesting.."
    scene m44 with vpunch
    "You grab Nami's tongue."
    "Nami nods slightly as she listens to the person on the phone."
    scene m45 with dissolve
    d "Nami!"
    scene m47 with dissolve
    d "Damn Cheeto!"
    scene m48 with dissolve
    n "And they glow in the dark?"
    n "Uhm yeah- just put them in there... My card number is four, eight, fifteen, sixteen, twenty-three and uh- forty-two!"
    n "The address is Treptow 4."
    n "Thanks."
    scene m49 with dissolve
    pause
    scene m50 with dissolve
    pause
    scene m51 with dissolve
    d "Idiot."
    scene m52 with dissolve
    d "And what glows in the dark?"
    scene m53 with dissolve
    n "Some dinosaur action figures."
    scene m54 with dissolve
    d "What the hell?"
    scene m53 with dissolve
    n "What? You know I collect these types of things."
    scene m54 with dissolve
    d "You're a nerd."
    scene m53 with dissolve
    n "And?"
    scene m54 with dissolve
    d "It was just an observation."
    scene m53 with dissolve
    n "I thought about something."
    n "And because you're here now..."
    scene m54 with dissolve
    d "...What?"
    scene m53 with dissolve
    n "Let's watch a porno."
    scene m54 with dissolve
    d "..."
    n "..."
    d "I'll be in my room."
    scene m56 with vpunch
    n "NO! SIT!"
    scene m57 with dissolve
    d "Nami! I don't want to watch that. Especially not with you!"
    n "It's for academic purposes!"
    scene m58 with dissolve
    d "What's academic about it?!"
    scene m57 with dissolve
    n "Everything in there is academic for someone like you!"
    n "You can even choose the movie!"
    d "*sigh*"
    d "Can't we just watch a normal movie?"
    scene m59 with dissolve
    n "[name]."
    scene m60 with dissolve
    n "I can either give you a very long speech about why we're gonna watch a porno, or you save us both some time and we just watch a porno."
    d "Nope."
    scene m56 with dissolve
    n "*sigh*"
    n "Alright!"
    n "Then what should we watch...?"
    scene m57 with dissolve
    d "Medium-sized grey - Wormy Effect?"
    n "We have seen that movie like 20 times."
    d "It's a good movie."
    scene m63 with Dissolve(2)
    n "*sigh*... I am too hungry to argue anymore..."
    scene black with Dissolve(1.5)
    with Pause(.5)
    scene m119 with dissolve
    n "I love this pizza!"
    scene m120 with dissolve
    d "It's the only good one around here."
    scene m121 with dissolve
    n "*Moans*"
    scene m122 with dissolve
    n "Sowh Ih Thoughwt-"
    d "Eat before you speak!"
    scene m123 with dissolve
    n "Mhhhhm!"
    scene m124 with dissolve
    pause
    scene m125 with dissolve
    n "Okay... So I thought about my revenge."
    scene m126 with dissolve
    d "Against Bella?"
    scene m125 with dissolve
    n "Yes."
    scene m127 with dissolve
    d "I think it's better if we wait a little."
    scene m128 with dissolve
    n "What? Why?"
    d "She and I are working on something."
    n "On what?"
    "You say nothing."
    scene m125 with dissolve
    n "Oh come on! Tell me!"
    scene m127 with dissolve
    d "Not yet... I will tell you when the time is right."
    scene m129 with dissolve
    n "You make me delay my revenge... and then you dare to not even give me the reason?"
    scene m134 with dissolve
    n "You know... I'll let it slide... for now... Just because you stayed at home that night."
    scene m131 with dissolve
    "You take a sip from your beer."
    scene m136 with dissolve
    n "So... I found this really weird porn site."
    scene m135 with vpunch
    d "Nami! We're eating for fuck's sake.."
    scene m136 with dissolve
    n "They were eating something, too.."
    scene m135 with dissolve
    "You give her an annoyed look."
    scene m132 with dissolve
    n "Hamhm."
    scene m129 with dissolve
    n "Mind answering me something?"
    d "Is it something dirty?"
    scene m136 with dissolve
    n "No. But serious."
    d "*sigh*"
    scene m134 with dissolve
    n "Can you get an erection?"
    scene m135 with dissolve
    d "What the hell is wrong with you?"
    scene m137 with dissolve
    n "What? I am just curious."
    d "Shut up."
    scene m138 with dissolve
    n "Morning wood?"
    scene m139 with dissolve
    d "I haven't had that in a while."
    scene m140 with dissolve
    n "So... If you saw boobs... Would that make you-"
    scene m139 with dissolve
    d "No."
    scene m138 with dissolve
    n "What would?"
    d "I don't know. I guess physical attraction doesn't do it for me. It's not enough."
    d "I need mental stimulation, too."
    scene m141 with dissolve
    n "Like dirty talk?"
    scene m143 with dissolve
    d "No... I thi-... *sigh* I think 'she' has to be special. The thought of being with her has to do it."
    scene m137 with dissolve
    n "How far did you two go?"
    d "*You stay silent for a moment* Just kissing."
    n "Nothing further?"
    scene m135 with dissolve
    d "No, the only chance to go further got lost when you sent Jane after us.."
    n "The cabin incident?"
    "You nod."
    scene m142 with dissolve
    n "*whisper* Sorry."
    scene m139 with dissolve
    d "The person has to be special. Otherwise I see no reason why I would want to be intimate with her."
    d "It would only be a waste of time- it would leave me with a feeling of emptiness."
    scene m138 with dissolve
    n "Same here."
    scene m139 with dissolve
    d "I'm actually surprised you're a virgin."
    n "Why?"
    d "You always had these clowns around you in high school."
    scene m136 with dissolve
    n "To do my homework... and other chores."
    n "I would never consider sleeping with horny, desperate 'nice' guys."
    n "But it's going to be a real challenge to get you laid."
    n "I like that!"
    scene m135 with dissolve
    d "Why are you in sport clothes?"
    scene m142 with dissolve
    n "I planned on doing yoga.."
    n "But... then I saw we still had some beer left."
    scene m139 with dissolve
    "*Yawns*"
    d "Anyways, I'm going to bed."
    scene m150 with dissolve
    n "Already? I thought we would hang out a bit."
    scene m151 with dissolve
    d "Not today, all this social activity made me exhausted."
    scene m152 with dissolve
    n "*mumbles* Night."
    stop music fadeout 3.0
    scene black with Dissolve(1.5)
    jump school03
label NE3:
    $ play_playlist(playlist_AmbientCheeto)
    scene black with Dissolve(1.5)
    show text "1 hour later." with Dissolve(1.5)
    with Pause(0.5)
    hide text with Dissolve(1.5)
    scene m152s with Dissolve(2)
    "*knock knock*."
    d "*Sigh*."
    "*knock* *knock*."
    scene m153 with Dissolve(2)
    d "Yes.."
    scene m154 with dissolve
    n "I got some pizza for you."
    d "I didn't want any."
    scene m156 with dissolve
    d "Can you leave?"
    scene m155 with dissolve
    n "I'm so sorry."
    scene m156 with dissolve
    d "Everyone feels sorry after the fact."
    scene m155 with dissolve
    n "I- was just so worried when you met up with Bella.."
    scene m156 with dissolve
    "You say nothing."
    scene m155 with dissolve
    n "I don't want to lose you!"
    scene m157 with dissolve
    n "Wha- what if you do something illegal and you end up in prison.."
    n "I- I mean... I don't think you got that money in a legal way."
    scene m158 with vpunch
    n "I can't lose you!"
    d "Can't?"
    scene m160 with dissolve
    n "I can't! Don't you get that?!"
    d "I am a burden, Nami."
    "Her head is shaking while she is trying not to break down... Her lips are pressed together, trembling... and her eyes are moving rapidly."
    scene m161 with dissolve
    n "I- I'm trying so hard not to lose you, and it feels like you're getting further away from me every day!"
    menu:
        "Tell Nami what you and Bella did":
            $ namilove +=1
            $ NKAB = True
            scene m162 with dissolve
            d "Bella and I fucked up the car of this guy who insulted and bullied Mila."
            d "After that we broke into his house and stole a family heirloom... and the cash."
            scene m163 with dissolve
            n "You could go to prison for a long time if they find out it was you!"
            scene m162 with dissolve
            d "They won't."
            scene m163 with dissolve
            n "What if Bella throws you under the bus!?"
            if bellasummer is True:
                d "In some twisted way... I trust her."
                n "How? She's literally the worst human being I have met in a long time! If not ever!?"
                d "It's a feeling."
            else:
                d "It's a risk I was willing to take."
                n "[name]! No!"
            d "Nami... Stop worrying about me."
            scene m164 with dissolve
            d "You have your own life and your own problems."
            scene m165 with dissolve
            n "Wow."
            scene m166 with dissolve
            "She takes a few steps back as she nods multiple times."
            scene m167 with dissolve
            n "You clearly have no idea what a big part of my life you are."
            scene m168 with dissolve
            n "But good to know that I am not one of yours."
        "Don't tell her.":
            $ NKAB = False
            $ namilove -=1
            d "Stop worrying about me."
            scene m164 with dissolve
            d "You have your own life."
            scene m165 with dissolve
            n "Wow."
            scene m166 with dissolve
            pause
            scene m167 with dissolve
            n "You clearly have no idea what a big part of my life you are."
            scene m168 with dissolve
            n "But good to know that I'm not one of yours."
    scene m169 with vpunch
    pause
    scene black with Dissolve(1.5)
    with Pause(.5)
    scene m170 with Dissolve(2)
    d "(I can't sleep...)"
    d "*sigh* Stupid Nami."
    menu:
        "Go to her room":
            scene c71 with Dissolve(3)
            "You slowly open her bedroom door."
            scene c72 with dissolve
            d "(Looks like she's asleep.)"
            pause
            scene c73 with dissolve
            with Pause(0.5)
            scene c74 with dissolve
            menu:
                "Join her in bed.":
                    $ NSIHR = True
                    "You slowly make your way towards Nami's bed."
                    scene c77 with Dissolve(2)
                    d "*whisper* You're the most important person in my life right now."
                    d "I love you, Nami... You know that..."
                    "She grabs your hand and squeezes it slightly."
                    d "But... if you keep doing stuff like this... I will lose my trust in you."
                    d "And you know it's built on a rocky foundation."
                    scene c76 with dissolve
                    n "*whisper* It won't happen again. I swear."
                    scene c78 with Dissolve(1.5)
                    stop music fadeout 3.0
                    scene black with Dissolve(2.5)
                    with Pause(0.5)
                    $ play_playlist(playlist_Jaccuzi)
                    scene sba945x with dssb
                    pause
                    scene sba946x with dssr
                    pause
                    scene sba947x with dssr
                    pause
                    scene sba948x with dssa
                    n "Morning."
                    d "Morning."
                    scene sba949x with dssr
                    n "How did you sleep?"
                    scene sba950x with dssa
                    d "Pretty good to be honest."
                    scene sba951x with dssr
                    n "It was because we spooned! It made us feel protected."
                    scene sba952x with dssa
                    n "But... it also painfully made me aware of the fact that I don't have a boyfriend to do this with on a regular basis."
                    scene sba953x with dssr
                    n "You and I should do this more often."
                    scene sba954x with dssa
                    d "Sleep together?"
                    n "Mhm."
                    d "You know Noji's rules."
                    scene sba955x with dssa
                    n "Who cares what she says?"
                    scene sba956x with dssa
                    d "I do. I'd like to keep the peace."
                    scene sba957x with dssa
                    n "*Sigh*"
                    n "I want to move out."
                    scene sba958x with dssa
                    d "You keep saying that but you're too chicken to do it."
                    scene sba959x with vpunch
                    n "OH YEAH!? WATCH ME!"
                    scene sba961x with dssr
                    d "I'll go and sleep for a little longer..."
                    scene sba960x with dssa
                    n "I'm going to the gym with Jeff."
                    n "And I'm already late. I should've left ten minutes ago."
                    scene sba962x with dssr
                    pause
                    d "Cheeto?"
                    scene sba963x with dssa
                    n "Yo?"
                    scene sba964x with dssa
                    d "You swore to respect my privacy from now on."
                    scene sba963x with dssa
                    n "I know."
                    scene sba965x with dssa
                    n "And I meant it!"
                    scene sba966x with dssa
                    n "*Whisper*...Mostly."
                "Leave.":
                    scene c75 with dissolve
                    d "*sigh*.."
                    scene c112 with Dissolve(2)
                    pause
                    stop music fadeout 2.0
                    scene c113 with dissolve
                    pause
                    jump school03
        "Go to bed.":
            d "*sigh*.."
            stop music fadeout 2.0
            scene black with Dissolve(1.5)
            jump school03
label school03:
    $ play_playlist(playlist_Ch2_New)
    if NSIHR is False:
        scene black with Dissolve(2.5)
        show text "The next morning" with Dissolve(1.8)
        with Pause(0.5)
        hide text with Dissolve(1.5)
        scene ax1 with vpunch
    else:
        scene black with Dissolve(2)
        with Pause(.5)
        scene ax1 with dssb
    "BRRRR BRRR BRR"
    "You wake up to your phone ringing."
    t "Yo bro! You're coming with us to that new bar later?"
    d "(To a bar? I haven't been to a bar before.)"
    t "Nami is coming, too!"
    if NSIHR is False and bellameet is True:
        with Pause(0.5)
        d "I don't care what she does."
        t "Trouble in paradise?"
        d"It doesn't matter."
        t "Your call... but if you want to talk, hit me up."
    else:
        d "I'll think about it."
        t "All I can ask for!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1749 with dssb
    pause
    $ persistent.unlockedImageNojiko4 = True
    scene sb1750 with dssa
    d "Morning."
    scene sb1751 with dssa
    m "Morning."
    if vicdate is True:
        scene sb1752 with dssa
        m "What's going on? You look like you got something on your mind."
        scene sb1753 with dssa
        d "It's about the date with Victoria."
        scene sb1752 with dssa
        m "Oh... What about it?"
        scene sb1754 with dssr
        d "It's been so long I don't know what to I-"
        scene sb1755 with dssa
        m "Okay, I'll stop you there."
        scene sb1756 with dssa
        m "Well... You weren't 'able' to collect a lot of experiences yet... but you have to start somewhere."
        scene sb1757 with dssa
        d "But where do I take her? What do I do with her?"
        scene sb1758 with dssr
        m "Haha, oh [name]... What you should do with her... well, that is something you have to figure out for yourself."
        m "But I can give you some tips on the 'where'."
        m "Have you spoken with Nami about it?"
        scene sb1759 with dssa
        d "I don't want to involve her... She's too much."
        scene sb1760 with dssa
        m "The same reason why I won't tell her about Nick yet."
        scene sb1761 with dssa
        d "Soo... His name is Nick."
        "*She nods*"
        scene sb1762 with dssr
        m "You should taste this coffee. He got me those beans."
        scene sb1763 with dssa
        d "...It's been only a few days and I am getting pulled into this exhausting world."
        "Noji lets out a small laugh."
        scene sb1764 with dssr
        m "The problem with isolation is that you get used to it. You'll feel exhausted when you spend time around people but there is no way around that."
        m "You have to get through this first wave of exhaustion in order to get out of it."
        scene sb1765 with dssa
        d "*Sigh*"
    else:
        scene sb1752 with dssa
        m "How are you doing?"
        scene sb1753 with dssa
        d "I'm fine."
        scene sb1762 with dssr
        m "You should taste this coffee. Nick gave it to me."
        scene sb1761 with dssa
        d "Nick? Is that his name?"
        scene sb1762 with dssa
        m "Oh yes... Right... I haven't told you his name yet."
    scene sb1766 with dssr
    pause
    scene sb1767 with dssr
    m "Here."
    scene sb1768 with dssa
    pause
    m "Tell me what you think of it."
    scene sb1770 with dssr
    pause
    scene sb1771 with dssr
    d "Tastes weird."
    m "It's a good coffee."
    scene sb1772 with dssr
    d "The fact that it's expensive doesn't make it good."
    m "*sigh*."
    scene sb1773 with dssa
    m "He told me his daughters are excited to meet you two."
    scene sb1774 with dssa
    d "So you said yes to his invitation??"
    scene sb1775 with dssa
    m "Not yet but I will."
    m "And Nick told them about you two and they are very excited."
    scene sb1776 with dssr
    d "Do you know them?"
    m "One. I have only met Vanessa. She visited him when he had the accident."
    m "She was... interesting to say the least."
    m "Jeff came for Nami this morning."
    d "I know. I saw her post."
    scene sb1777 with dssa
    m "Oh! You use Aurora, too?"
    scene sb1778 with dssa
    d "I'm aware of it but I don't use it."
    scene sb1779 with dssa
    m "Nick is always sending me funny memes, but I don't know how to reply."
    m "I'll send you some funny pictures later."
    scene sb1780 with dssa
    d "...Please don't."
    scene sb1781 with dssa
    m "I am going to shower. Have a sweet day."
    d "You too."
    scene sb1782 with dssa
    "Your phone rings."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sb1783 with dssb
    pause
    b "After your therapy session today we will go out and buy some clothes."
    d "I have a therapy session today?"
    scene sb1784 with dssa
    b "Yes. My mother will call you today."
    d "How do you know all this?"
    b "I might've accidentally looked into some files..."
    scene sb1785 with dssr
    d "You know that it's illegal to look into those files."
    b "Oh no... Anyways."
    d "(Wait. I don't have a file yet.)"
    b "You got one, but there's nothing in there... But I also saw you in Marl-..."
    d "What?"
    d "Don't tell me Miss Marla is one of your mother's clients..."
    scene sb1786 with dssr
    b "Maybe."
    d "I see. For how long?"
    scene sb1787 with dssr
    b "Not that long."
    b "But don't you dare tell anybody that."
    d "I won't."
    scene sb1786 with dssr
    d "(Her mother could get into some deep shit because of her.)"
    d "(I just acquired a valuable asset to keep Bella in check.)"
    d "(And the fact that Miss Marla has to attend therapy sessions is valuable, too.)"
    pause
    scene black with Dissolve(2)
    with Pause(0.5)
    scene c116 with dssb
    pause
    scene c117 with dissolve
    d "Hmm."
    $ persistent.unlockedImageSonya2 = True
    d "(Looks like her boyfriend? Brother?)"
    scene c118 with dissolve
    d "(Oh. The way he is scanning the people around him and his sister...)"
    scene c119 with dissolve
    pause
    scene c120 with dissolve
    "Sonya sits down and stares motionless out of the window."
    scene c121 with dissolve
    menu:
        "Sit next to Sonya.":
            $ sonyatalk = True
            d "(Hehe... Let's provoke him a little.)"
            scene c122 with dissolve
            d "Hey Sonya."
            scene c123 with dissolve
            so "Hi."
            scene c122 with dissolve
            d "Mind if I sit here?"
            scene c124 with dissolve
            so "Uh-"
            scene c126 with dissolve
            d "Thanks."
            d "How are you?"
            scene c125 with dissolve
            so "Good and you?"
            scene c126 with dissolve
            d "I am good, too."
            scene c127 with dissolve
            pause
            d "Was that your boyfriend?"
            so "My brother."
            d "Ahh, I see."
            scene c128 with dissolve
            so "I don't think it's a g-good idea that you sit with me."
            d "Is this about your brother?"
            scene c129 with dissolve
            so "Yes."
            scene c130 with dissolve
            d "Mhm, let me ask you a question, Sonya."
            d "You are most likely going to finish your degree here, right?"
            scene c131 with dissolve
            so "Yes."
            scene c130 with dissolve
            d "...Someday you'll have to make a decision."
            scene c132 with dissolve
            "You both quietly stare into the distance."
            scene c133 with Dissolve(2)
            $ persistent.unlockedImageSonya3 = True
            pause
        "Don't sit with her":
            pass
    scene black with Dissolve(3)
    with Pause(.5)
    scene c137 with Dissolve(2.4)
    pause
    scene c139 with dissolve
    d "(ZRP... I wonder what that stands for.)"
    scene c141 with vpunch
    u "Hello?!"
    scene c142 with dissolve
    d "Mh? Are you speaking to me?"
    scene c143 with dissolve
    u "Yes duh?"
    "You give her a confused look."
    u "Your ID?"
    d "I don't have an ID."
    scene c144 with vpunch
    u "That means you're not a student at this university, and you have to find your ID or leave immediately!"
    d "Wha-"
    scene c145 with dissolve
    ay "He is a student here."
    scene c146 with dissolve
    u "Show me your ID!"
    scene c148 with dissolve
    pause
    scene c149 with dissolve
    u "If he has no ID he can't-"
    scene c150 with dissolve
    ma "Karen."
    ma "[name] is a student here. It seems like he never got an ID, but I can assure you that he is a student here."
    scene c152 with dissolve
    b "I have never seen this guy before and well, I don't know if I can learn properly... knowing that this university just lets anyone in without an ID."
    scene c151 with dissolve
    ma "Bella!"
    scene c154 with dissolve
    ka "He has to get an ID. These are the rules."
    d "Then where do I get one?"
    scene c155 with dissolve
    ka "You will meet me after school in room 432 B, okay?"
    d "...Okay."
    scene c153 with dissolve
    b "*giggle.*"
    scene c159 with dissolve
    ka "Sunglasses are not allowed inside the facilities."
    scene c160 with dissolve
    pause
    scene c161 with dissolve
    "Bella lets out a snide laugh."
    ka "Excuse me!?"
    scene c162 with dissolve
    "Ayua also makes her way into the newly built college facilities."
    scene c163 with dissolve
    ma "[name]. Wait."
    scene c164 with dissolve
    d "Yes?"
    scene c163 with dissolve
    ma "Between you and Bella. How did it go?"
    scene c164 with dissolve
    d "Nothing I can't handle."
    scene c163 with dissolve
    ma "I did put you two together on purpose."
    scene c164 with dissolve
    d "I thought as much."
    $ persistent.unlockedImageKaren1 = True
    scene c163 with dissolve
    ma "I've known Bella since she was twelve."
    scene c164 with dissolve
    d "Were you her teacher?"
    scene c163 with dissolve
    ma "No. Her mother and I are friends."
    scene c164 with dissolve
    d "Amber."
    d "She's nice."
    scene c165 with dissolve
    ma "She's a very kind person."
    ma "Can you please keep me updated on Bella's behavior?"
    d "Maybe you made a mistake. What if I am the bad influence?"
    "She says nothing."
    scene c166 with dissolve
    ma "Please keep me updated. I care about her."
    d "*sigh* Mhm."
    scene c167 with dissolve
    d "But I guess I'm getting to her."
    scene c168 with dissolve
    ma "Oh really?"
    ma "I'm very glad to hear that."
    scene c169 with dissolve
    d "(If she only knew that we're planning on destroying someone else's family...)"
    stop music fadeout 2.0
    with Pause(.5)
    scene c170 with Dissolve(2)
    $ play_playlist(playlist_Ch1CollegeBella)
    d "(What a pathetic, empty trophy case.)"
    scene c171 with dissolve
    u "Depressing, isn't it?"
    scene c172 with dssr
    pause
    d "Exactly what I thought."
    scene c173 with dissolve
    u "This year is a turning point for this college."
    d "They managed to suck badly all these years... Why would this year be any different?"
    scene c174 with dissolve
    u "Because I am here."
    scene c175 with dissolve
    d "Good to know, Rambo."
    stop music fadeout 2.0
    $ persistent.unlockedImageZara1 = True
    scene c176 with dissolve
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_BellaDate)
    scene ca1 with dssb
    pause
    scene ca2 with dssr
    mi "*sigh*"
    scene ca3 with dssr
    "With empty and bland eyes, Mila stares into the room after successfully rearranging the table."
    scene ca4 with dssr
    pause
    scene ca5 with dssr
    pause
    scene ca6 with vpunch
    mi "*Gasp*!"
    scene ca7 with vpunch
    "Mila twitches so hard, she sends her cup of tea flying."
    scene ca8 with dssr
    mi "I fucking hate my life..."
    scene ca9 with dssr
    d "Hey."
    d "Sorry for sneaking up on you."
    d "But you looked a little... Emotionally occupied."
    scene ca10 with dssa
    mi "Yeah... I haven't slept much..."
    d "I can see that."
    scene ca11 with dssa
    mi "Fuck you."
    scene ca12 with dssa
    "She exhales strongly."
    scene ca13 with dssa
    pause
    scene ca14 with dssa
    "She tries to fight it as hard as she can but it's no use... Little tears start streaming down her face."
    ay "What's wrong with Mila?"
    ay "I should go talk to her."
    ma "No, let [name] handle it."
    ay "Why? He could be the reason she is crying."
    $ persistent.unlockedImageMila1 = True
    $ MilaComfort03 = True
    $ milalove +=1
    $ ayua +=1
    $ marla +=1
    scene ca15 with dssa
    "Mila weeps as her tears run down her face."
    scene ca16 with dssa
    mi "*Crying* I haven't done anything..."
    if bellameet is True:
        d "(Fuck.)"
    scene ca17 with dssr
    d "Hey. Look at me and tell me what's going on."
    scene ca19 with dssa
    mi "O-okay... Fuck!"
    ay "Huh. I think those two are sweet together."
    ma "Hmm."
    if bellameet is True:
        mi "I... got charged with burglary and vandalism.."
        scene ca20 with dssa
        d "(That was fast...)"
        d "*You give her a surprised look* What did you do?"
        scene ca21 with vpunch
        mi "Nothing of course!"
        scene ca22 with dssa
        d "I don't understand..."
        scene ca23 with dssa
        mi "The Holgersons."
        scene ca24 with dssa
        d "Who are they? (I can't let her know that I know them.)"
        scene ca23 with dssa
        mi "Remember the guys that made fun of me?"
        scene ca24 with dssa
        d "Yes."
        scene ca25 with dssa
        mi "One of them."
        d "You didn't do anything?"
        scene ca27 with vpunch
        mi "For the last time! No!"
        scene ca26 with dssa
        d "(I need to find a solution... Fast.)"
        d "(The money Bella stole from Mario. I could try to cheer her up...)"
        scene ca28 with dssa
        mi "I just- *Sigh* Let's not talk about it..."
        scene ca29 with dssr
        menu:
            "Ask her out for dinner (with Mario's money).":
                $ mila +=2
                scene ca30 with dssa
                d "Do you want to go to a restaurant and uh... eat something?"
                scene ca31 with dssa
                mi "Are you asking me out?"
                menu:
                    "Yes, I am.":
                        if vicdate is True:
                            $ miladateF = True
                            scene ca33 with dssa
                            mi "Well, I'll have to decline..."
                            scene ca34 with dssr
                            mi "Not because I don't want to... but because you are going out with Vic."
                            mi "You two need to figure out where you're at."
                            scene ca35 with dssa
                            d "I see, but I would still like to invite you to dinner... as friends."
                        else:
                            pass
                            $ achievement.grant("MilaDatePlan")
                            $ achievement.sync()
                            $ milalove +=1
                            $ miladate = True
                    "Only as friends":
                        $ miladateF = True
                scene ca36 with dssa
                mi "I can't afford to eat out... Sorry."
                scene ca37 with dssa
                d "It's on me."
                scene ca36 with dssa
                mi "I don't feel well when other people pay for me."
                d "(She has that silly pride... I guess she feels like a parasite when someone offers her something.)"
                mi "We could go and take a walk if you want."
                scene ca38 with dssa
                d "Mila... Fuck your pride."
                d "We'll go out and eat something."
                scene ca39 with dssa
                mi "I-"
                scene ca38 with dssa
                d "No. Listen to me... I really want to do this fo-... with you."
                scene ca40 with dssa
                mi "Okay... Thanks."
                mi "I am looking forward to it."
            "Don't ask her out.":
                $ miladate = False
                d "(No, there are better ways to invest this money... Even though a lunch wouldn't have put a dent in it.)"
    else:
        mi "I'm being sued with vandalism."
        scene ca20 with dssa
        d "Oh. Did you do it?"
        scene ca21 with dssa
        mi "Of course not!"
        scene ca22 with dssa
        d "Who sued you?"
        scene ca23 with dssa
        mi "Do you remember the guys that approached us after we left the cafe the other day?"
        scene ca24 with dssa
        d "Yeah."
        scene ca22 with dssa
        mi "One of them."
        scene ca26 with dssa
        d "(Did Bella cause this?)"
        d "You should be fine, I think?"
        scene ca27 with vpunch
        mi "I'm not fine at all!"
        mi "How am I going to prove that I didn't do anything!"
        scene ca26 with dssa
        d "How are they going to prove you did?"
        scene ca27 with dssa
        mi "I don't know?"
        mi "What if they bribe someone?"
        scene ca26 with dssa
        d "I don't know them so I can't-"
        scene ca28 with dssa
        mi "I just- *Sigh* Let's not talk about it..."
        d "Alright."
        mi "Do you know what's fun to talk about?"
        mi "Food."
        scene ca29 with dssr
        menu:
            "Ask her out for dinner to talk about food.":
                $ mila +=2
                scene ca30 with dssa
                d "Do you want to go to a restaurant and uh... eat something?"
                scene ca31 with dssa
                mi "Are you asking me out?"
                scene ca32 with dssr
                menu:
                    "Maybe.":
                        if vicdate is True:
                            $ miladateF = True
                            scene ca33 with dssa
                            mi "Well, I'll have to decline..."
                            scene ca34 with dssr
                            mi "Not because I don't want to... but because you are going out with Vic."
                            mi "You two need to figure out where you're at."
                            scene ca35 with dssa
                            d "I see, but I would still like to invite you to dinner... as friends."
                        else:
                            $ achievement.grant("MilaDatePlan")
                            $ achievement.sync()
                            pass
                            $ milalove +=1
                            $ miladate = True
                    "Only as friends":
                        $ miladateF = True
                scene ca36 with dssa
                mi "I can't afford to eat out... Sorry."
                scene ca37 with dssa
                d "It's on me."
                scene ca36 with dssa
                mi "I don't feel well when other people pay for me."
                d "(She has that silly pride... I guess she feels like a parasite when someone offers her something.)"
                mi "We could go and take a walk if you want."
                scene ca38 with dssa
                d "Mila. Fuck your pride."
                d "We'll go out and eat something."
                scene ca39 with dssa
                mi "I-"
                scene ca38 with dssa
                d "No. Listen to me. I really want to do this fo- with you."
                scene ca40 with dssa
                mi "Okay... Thanks."
                mi "I am looking forward to it."
            "Don't ask her out.":
                $ miladate = False
                scene ca30 with dssa
                d "Food is indeed a fun topic to talk about."
                d "But eating away your problems has never worked out."
    scene ca41 with dssr
    mi "The other thing that's making me crazy are my parents... They're keeping me up at night with their constant screaming and breaking stuff."
    mi "I just... I just need to move out but I won't be able to afford my own place in a million years."
    scene ca42 with dssr
    n "Move in with me and [name] when we move to a student shared flat."
    scene ca43 with vpunch
    mi "Oh really?!"
    scene ca44 with dssa
    n "Oh- uhhh, I was joking... Sorry."
    mi "Oh..."
    scene ca45 with dssa
    n "Or... was I?"
    scene ca46 with dssa
    d "We have no money either."
    if bellameet is True:
        scene ca48 with dssa
        "Nami raises her brows."
        n "...Right. No money."
    scene ca47 with dssa
    n "They are not that expensive... If everyone got a part-time job, we could easily afford it."
    scene ca49 with dssr
    mi "If this ever turns into a serious idea..."
    scene ca51 with dssa
    n "You will be the first one we will ask!"
    scene ca50 with dssa
    mi "Thanks!"
    scene ca52 with dssr
    d "I have to go. Later."
    mi "Later [name]!"
    stop music fadeout 3.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_AmbientBella)
    scene sba918 with dssb
    b "Hey."
    d "Hi."
    b "Don't you want to ask me how it went?"
    scene sba919 with dssa
    d "...How was she?"
    b "15 more minutes and I swear I would've killed that fucking girl."
    d "Was it that bad?"
    scene sba920 with dssr
    d "In the picture you sent me, I couldn't discern which of you was actually the pretentious one."
    scene sba921 with dssa
    b "Don't compare me to those people!"
    scene sba922 with dssr
    b "That dumbo can't talk about anything but fashion and how she used to buy this and that-"
    if bellameet is True:
        $ persistent.unlockedImageBella3 = True
        scene sba923 with vpunch
        b "ARRGH!"
        "She presses your face against her chest."
        scene sba924 with vpunch
        b "*gasp*"
        scene sba925 with dssa
        d "What the fuck are you doing?!"
        scene sba926 with dssr
        b "I- I am so sorry! I- I don't know why I just did that!"
        d "Keep it together..."
        scene sba927 with dssa
        b "*Whisper* Yes..."
    scene sba928 with dssr
    b "*sigh* I was so close to banging her head onto the counter."
    scene sba929 with dssa
    b "I hope our plan succeeds. I hate wasting my time with those people."
    scene sba930 with dssa
    d "It will."
    d "Assuming you don't fuck it up."
    scene sba929 with dssa
    b "What's there to fuck up?"
    b "I have to befriend a pretentious doll, that's it."
    if bellameet is True:
        scene sba930 with dssa
        d "Maybe we could use her as our scapegoat."
        scene sba929 with dssa
        b "I don't think so. There is no reason why she would steal from him. It's not like her family is poor."
        scene sba930 with dssa
        d "I really need to get Mila out of there."
        scene sba931 with dssa
        b "Ohhh, are you in love with her?"
        scene sba932 with dssa
        "You ignore her."
        scene sba931 with dssa
        b "You know that if you two get together your finances won't multiply?"
        b "Zero times zero is stil-"
        scene sba932 with dssa
        d "They charged her with burglary and vandalism."
        scene sba933 with dssa
        b "That was fast."
        scene sba932 with dssa
        d "But there is no way they could convict her... She'll have an alibi."
        scene sba934 with dssr
        b "Don't you think it's weird how fast they acted?"
        scene sba935 with dssa
        d "What are you getting at?"
        scene sba934 with dssa
        b "They obviously know it wasn't her and she clearly isn't the type for it."
        b "I'm just saying... We have to be careful."
        b "And if they want Mila convicted... Then she will be convicted."
        scene sba935 with dssa
        d "Wha-"
        scene sba936 with dssa
        b "Never underestimate the power of money."
        b "Especially when the enemy is a girl whose family has literally negative influence."
    scene sba937 with dssr
    v "Hi!"
    scene sba938 with dssa
    d "Oh, hey Vic."
    scene sba939 with dssa
    v "How are you?"
    scene sba940 with dssa
    d "I'm fine and you?"
    scene sba941 with dssa
    v "Good, good!"
    scene sba942 with dssa
    v "Hi!"
    scene sba943 with dssa
    b "Hi."
    if vicdate is True:
        scene sba944 with dssr
        v "Sooo, I talked to Maja and I now know where we could go on our date!"
        scene sba946 with dssr
        d "That's good."
        d "Do you have a certain time in mind?"
        scene sba945 with dssa
        v "Soon, soon! I have to prepare some stuff first!"
        scene sba946 with dssa
        d "Okay, sure."
        scene sba950 with dssr
        b "We have to work."
        d "And?"
        scene sba951 with dssa
        b "I'm just saying that you two can go play on the playground some other time."
        scene sba947 with dssr
        "Vic just gives Bella genuine smile."
        scene sba948 with dssa
        v "And you have a nice day too, Bella."
        scene sba952 with dssr
        b "Thanks? You too, I guess."
        scene sba953 with dssr
        pause
        scene sba954 with dssa
        b "She is so going to do the sea star."
        d "The what?"
        scene sba955 with dssa
        b "She just lays there on her back... I mean, what else can she do?"
        scene sba956 with dssa
        d "You're talking about sex?"
        scene sba957 with dssa
        b "No, I'm talking about farming, idiot."
        scene sba958 with dssr
        pause
        scene sba959 with dssa
        b "I think in all my years, I have never seen a guy who's as much of a virgin as you are."
        scene sba960 with dssa
        b "But at least you're not some desperate dude... I'll give you that."
        if bellasummer is True:
            scene sba961 with dssr
            b "Is it because of Summer?"
            scene sba962 with dssa
            "You say nothing."
            scene sba961 with dssa
            b "So it is."
            scene sba963 with dssr
            b "My Mama will help you. She'll get you out of there."
    scene sba964 with dssr
    d "I'm going to class."
    scene sba965 with dssr
    pause
    stop music fadeout 3.0
    scene black with Dissolve(1.5)
    with Pause(.5)
    $ play_playlist(playlist_Chapter1a)
    scene c300 with Dissolve(1.5)
    har "Please choose your seats."
    scene c301 with dissolve
    d "(I will sit somewhere where no one bothers me.)"
    scene c303 with dissolve
    pause
    scene c304 with dissolve
    pause
    scene c305 with dissolve
    pause
    scene c306 with dissolve
    u "Hey Bella."
    scene c307 with dissolve
    b "...Hey Robin."
    if bellalove >=1:
        scene c309 with dissolve
        pause
        scene c310 with dissolve
        pause
    scene black with Dissolve(1.5)
    with Pause(.5)
    scene c311 with Dissolve(1)
    "Brrr."
    scene c311x with dssa
    show noji_1 with dssa
    pause
    show noji_2 with dssa
    pause
    show noji_3 with dssa
    pause
    scene mm11 with Dissolve(1)
    $ NojiChatCh3 = True
    d "(Hmm...)"
    d "(That's the bitch that gave me the stink eye when I interrupted him and Nami.)"
    stop music fadeout 3.0
    nia "Hi."
    scene c313 with vpunch
    $ play_playlist(playlist_Ch4x52)
    d "*gasp*!"
    scene c314 with dissolve
    nia "Hmm.."#eye squint
    nia "*whisper* Only guilty people are scared that easily."
    scene c315 with dissolve
    pause
    scene c316 with dssr
    pause
    scene c317 with dssr
    pause
    scene c318 with dssr
    d "*whisper* I'd rather sit alone."
    scene c319 with dissolve
    nia "*whisper* Are you an emo?"
    d "No?"
    scene c318 with dissolve
    nia "But you look like one."
    d "I don't."
    scene c320 with dissolve
    nia "I am one too."
    scene c321 with dissolve
    d "I told you I am not an emo."
    scene c320 with dissolve
    nia "When I am cosplaying something gothy I always turn emo."
    nia "You know... I get all weird."
    scene c322 with dissolve
    nia "And, and... I tend to do emo things."
    pause
    scene c323 with dissolve
    nia "...Now I remember where I know you from."
    nia "You went to the Tropics High School!"
    nia "I was there, too."
    scene c336 with dissolve
    d "I have never seen you before."
    scene c335 with dissolve
    nia "I wasn't as outgoing as I am now... Gawd... Back in high school I didn't have any confidence."
    nia "I remember you because you always got into fights."
    scene c328 with dissolve
    har "Today, we will take a first look into the depths of biological gene manipulation."
    scene c335 with dissolve
    nia "And you have that uhh- hot red haired friend.."
    nia "Man. I'd love to get choked by her."
    scene c337 with dissolve
    nia "*whisper* Choke me harder mommy..."
    d "What is wrong-"
    scene c329 with vpunch
    har "Hey! Pay attention to the class [name] and Nia!"
    if bellalove >=1:
        scene c330 with dssr
        pause
        scene c331 with dssr
        pause
    else:
        scene c331 with dssr
        pause
    stop music fadeout 3.0
    scene black with Dissolve(2)
    with Pause(.5)
    scene c338 with dssb
    $ play_playlist(playlist_Jaccuzi)
    with Pause(.7)
    scene c340 with vpunch
    har "Excuse me?"
    d "Yes?"
    $ persistent.unlockedImageHari1 = True
    scene c341 with dissolve
    har "You can leave...?"
    scene c342 with dissolve
    d "[name]."
    scene c343 with dissolve
    har "Or can I do something for you, [name]?"
    scene c344 with dissolve
    d "No."
    scene c346 with dissolve
    har "Okay, have a nice day."
    scene c347 with dissolve
    d "Mhm."
    scene c348 with dissolve
    "You pack up your stuff and prepare to meet Bella in front of the building."
    scene c349 with dissolve
    sai "Wow, careful there."
    d "You're in my way."
    scene c350 with dissolve
    stop music fadeout 2.0
    sai "Oh, and what are you gonna do about it?"
    $ play_playlist(playlist_RockPop)
    scene ma1 with dssb
    pause
    scene ma2 with vpunch
    pause
    scene ma3 with dssa
    pause
    scene ma4 with dssa
    pause
    scene ma5 with vpunch
    "You block his incoming punch."
    scene ma6 with vpunch
    pause
    scene ma7 with vpunch
    pause
    scene ma8 with dssa
    d "I'll rip you apart."
    scene ma9 with dssr
    pause
    scene ma10 with vpunch
    pause
    scene ma11 with dssr
    d "Son of a bitch."
    scene ma12 with vpunch
    pause
    scene ma13 with dssr
    pause
    scene ma14 with dssa
    u "Get lost!"
    scene ma16 with dssa
    "You start walking towards them... but suddenly, a door opens."
    scene ma18 with dssb
    pause
    scene ma19 with dssr
    "You turn around and walk the other way."
    stop music fadeout 2.5
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_GirlyPop)
    scene c352 with Dissolve(2)
    pause
    scene c353 with dissolve
    b "Finally! You-"
    scene c354 with dissolve
    b "What happened to you?"
    scene c355 with dissolve
    d "Nothing."
    scene c356 with dssr
    b "Who did you get into a fight with?"
    d "I forgot his name."
    scene c357 with dssr
    b "Oh, this bitch with the sunglasses?"
    scene c359 with dssa
    d "Mhm."
    d "I could've handled him but... *Moan* his friend came out of nowhere and hit me from behind."
    scene c360 with dissolve
    sai "Bet on it."
    scene c361 with dissolve
    "Your eyes meet."
    scene c362 with dissolve
    $ persistent.unlockedImageBella4 = True
    b "He looks worse."
    scene c363 with dissolve
    d "...Told you I could've handled him."
    scene c364 with dssr
    "Nami randomly hums."
    scene c365 with dssr
    pause
    scene c367 with dssa
    pause
    scene c366 with dssr
    n "What the-?"
    scene c368 with vpunch
    n "WHAT HAPPENED?!"
    scene c369 with vpunch
    n "DID YOU DO THAT?!"
    scene c370 with dissolve
    "Bella is stunned for a second due to Nami's sudden push."
    scene c371 with vpunch
    b "How about you shut the fuck up before I give you a taste?!"
    scene c372 with vpunch
    "You intercept her blow in the air."
    d "Nami?! She obviously didn't do anything!"
    scene c373 with dissolve
    n "T-then who? *She stutters nervously*"
    d "It doesn't matter."
    scene c375 with dissolve
    n "It does matter! I don't want to go through this again!"
    scene c376 with dissolve
    d "Nami- listen... It won't happen again, I promise."
    n "You can't promise that."
    scene c377 with dissolve
    d "You have to trust me on that."
    d "What happened- back then- won't happen again."
    d "I'll see you at home, okay?"
    scene c378 with Dissolve(2)
    b "...She was really going to punch me."
    b "For fucking nothing."
    scene c379 with dissolve
    d "Don't blame her."
    d "It's not her fault... It's mine... I put her through some stuff in the past."
    scene c378 with dissolve
    b "Why didn't you just tell her what happened?"
    scene c379 with dissolve
    d "It was my first move."
    b "What?"
    d "This guy won't stop harassing me. Especially after I punched him. This guy has the hots for Nami."
    d "I can use this to my advantage. If I had told her what he did, she would never speak to him again, and I'd lose a valuable asset."
    scene c380 with dissolve
    d "But he doesn't know that I am in control."
    scene c381 with dissolve
    b "But there is the risk that she might fall for him?"
    scene c380 with dissolve
    d "No. I can always tell her what he did and Nami despises people who treat me bad."
    scene c382 with dissolve
    "Bella puts her hand on your chest."
    b "If... you plan on avenging yourself I-"
    scene c383 with vpunch
    d "Do you like me?"
    scene c384 with dissolve
    b "What?!"
    scene c383 with dissolve
    d "I saw it in your eyes. The moment you saw that I got into a fight you looked kinda worried."
    scene c385 with dissolve
    b "Whatever you're smoking. Stop it."
    d "You can't hide an initial body reaction."
    scene c386 with vpunch
    b "And if you don't shut up now, I will show you what a real fight looks like!"
    "You give her a subtle smile."
    scene c386 with vpunch
    b "Fuck you!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene c387 with dssb
    pause
    scene c388 with dssr
    pause
    scene sba921x with dssa
    ay "Hey! If it isn't my favorite couple."
    scene sba922x with dssr
    b "Shut up."
    scene sba923x with dssr
    d "Nami was looking for you."
    scene sba924x with dssa
    ay "What happened to you?"
    d "A little fight."
    scene sba925x with dssa
    "Ayua glances at Bella."
    scene sba926x with vpunch
    b "Not with me!"
    scene sba927x with dssa
    ay "Alright! Relax!"
    scene sba928x with dssr
    ay "It seems like you could use some training... So that this doesn't happen again."
    scene sba929x with dssa
    d "I know how to fight."
    scene sba928x with dssa
    ay "I can see that."
    scene sba929x with dssa
    d "I'm just a little rusty."
    scene sba930x with dssa
    ay "Then you wouldn't say no to a little sparring session with me, right?"
    scene sba931x with dssa
    d "Why not."
    $ AyuaSparring = True
    scene sba930x with dssa
    ay "Great!"
    ay "Drop by our studio when you got time. Preferably around 7pm after class."
    scene sba933x with dssa
    d "You work in a martial arts studio?"
    scene sba932x with dssa
    ay "I do indeed."
    scene sba933x with dssa
    d "I'll think about it."
    scene sba934x with dssr
    b "Let's go..."
    scene sba935x with dssa
    ay "Wait, wait. Don't you need to get your ID?"
    d "Oh fuck..."
    scene sba936x with dssa
    b "Just don't go."
    scene sba937x with dssa
    d "It's your fault!"
    scene sba938x with vpunch
    b "I was just joking!"
    d "Come with me."
    scene sba939x with dssr
    b "No? I will wait here!"
    scene sba940x with dssa
    d "No way. Come with me or I'll go home."
    scene sba939x with dssa
    b "Then go home."
    scene sba941x with dssa
    "You walk away."
    pause
    scene sba942x with vpunch
    b "FINE!"
    scene sba943x with dssa
    "Ayua lets out a laugh."
    scene sba944x with dssa
    b "You shut up!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene c407 with dssb
    d "Where is this room anyway?"
    b "Somewhere here judging by the numbers."
    d "Is she a teacher?"
    b "A teacher at the front desk? No."
    scene c408 with dissolve
    pause
    scene c409 with dissolve
    ka "Ah there you are."
    ka "And- you."
    scene c411 with dissolve
    b "Mh."
    scene c410 with dissolve
    ka "You have no business here, wait outside."
    scene c415 with dissolve
    b "I'd rather not."
    scene c412 with dissolve
    $ persistent.unlockedImageBella5 = True
    $ persistent.unlockedImageKaren2 = True
    ka "Wait."
    scene c413 with dissolve
    ka "What happened to your face?"
    ka "Did you get into a fight?"
    scene c414 with dissolve
    d "Yes."
    ka "*sigh* I will get the nurse."
    scene c413 with dissolve
    d "No thanks, it's just a little cut."
    scene c412 with dissolve
    ka "Come back when this cut is healed... I need to take pictures of you for your ID."
    d "...Okay."
    scene black with Dissolve(1.5)
    with Pause(.5)
    scene c416 with Dissolve(2)
    b "What is that whale even doing here?"
    scene c417 with dissolve
    d "She is somehow involved in the art classes."
    scene c416 with dissolve
    b "How do you know?"
    scene c417 with dissolve
    d "The room was full of model pictures of her."
    scene c418 with dissolve
    b "A model? A fatty like that?"
    menu:
        "Objectively, she has a very attractive body.":
            $ karen +=3
            $ Bjeal +=1
            $ KarenAttractive = True
            scene c419 with dissolve
            b "Ugh! You're one of those skinny dudes that always have a fat girlfriend?"
            b "And besides being fat she's old."
            scene c420 with dissolve
            d "Don't be jealous."
            b "I'm not jealous?!"
            d "Compared to her, you're flat-chested and cursed with an attitude."
            scene c421 with dissolve
            b "I- I'm not flat chested!"
            b "I have big, perky double D's! I am at the top of the game!"
            d "Sure."
            scene black with Dissolve(2)
        "Some people like curves.":
            scene c420 with dissolve
            b "There is a difference between having 'curves' and being an elephant."
            d "Jealous much?"
            scene c421 with dissolve
            b "Haha, as if I have to be jealous."
        "I have no type.":
            scene c420 with dissolve
            b "Of course not."
            b "Someone like you takes what he can get."
            scene c422 with dissolve
            b "Man! I'm on fire today!"
            d "Probably an STD."
    jump BHCH3
label BHCH3:
    stop music fadeout 3.0
    scene black with Dissolve(1.5)
    with Pause(.5)
    $ play_playlist(playlist_Amber)
    scene mm194 with Dissolve(2)
    pause
    scene mm195 with dissolve
    pause
    scene mm196 with dissolve
    bm "Honey? Is that you?"
    scene mm196 with dissolve
    b "Yes? Who else?"
    b "Don't you always complain that my car is too loud and you hear it through the entire house?"
    scene mm200 with vpunch
    bm "Oh my god, [name]!"
    scene m201 with dissolve
    bm "What happened to you?"
    scene m202 with vpunch
    bm "Bella?!"
    b "It wasn't me for fuck's sake!"
    scene m203 with Dissolve(1.3)
    bm "Sit down, [name]. Let me have a look at that."
    scene m205 with dissolve
    d "It's okay, Amber."
    scene m204 with dissolve
    bm "No! It's bleeding."
    bm "So let me just... here and... here."
    menu:
        "You should give Bella some slack.":
            $ bllamb +=1
            scene m205 with dissolve
            bm "What?"
            d "When you insinuated that she did this..."
            bm "Oh we-"
            scene m208 with dissolve
            d "No. I know exactly how she felt. And the last person who should make her feel like that is you."
            scene m209 with dissolve
            bm "Are you a psychologist now?"
            "You say nothing."
            scene m211 with dissolve
            bm "I know... That wasn't smart. The fact that you and her aren't friends and the way it ended last time made me overreact."
            bm "I'll talk to her later."
            menu:
                "Please apologize to her.":
                    $ bllamb +=2
                    $ AmberAP = True
                    $ amber +=3
                    scene m212  with dissolve
                    d "Mh?"
                    scene m213  with dissolve
                    bm "You are right, I will apologize to her."
                "I don't want to interfere.":
                    $ AmberAP = False
                    pass
        "She needs a firm hand.":
            $ bllamb -=1
            bm "*sigh* Maybe."
            d "Is it too personal to ask where her father is?"
            bm "It is."
            d "Okay."
    scene m214  with dissolve
    am "Mhm Mhhhm."
    scene m215  with dissolve
    am "Mhm, it's still very visible but... it looks less bloody now."
    scene m216  with dissolve
    d "Thank you, Amber."
    am "Of course."
    scene m217 with dssr
    d "And please no details to Nojiko."
    scene m218 with dssa
    d "Please. I don't want her to worry."
    scene m219 with dssr
    $ persistent.unlockedImageAmber1 = True
    am "I'll see what I can do."
    stop music fadeout 3.0
    scene black with Dissolve(2)
    with Pause(.5)
    play music "music/Vesky - Departure.ogg"
    scene m220 with Dissolve(2)
    $ persistent.unlockedImageBella6 = True
    pause
    scene m221 with dissolve
    d "Do-"
    scene m222 with dissolve
    b "Just go the fuck home!"
    scene m221 with dissolve
    d "I understand how you feel."
    scene m221 with dissolve
    "She ignores you."
    scene m223 with dissolve
    d "Back in high school I used to get into a lot of fights... Like- *sigh* I would be lying if I said that I was completely innocent."
    d "At first people used to pick on me because I was so quiet and always buried in my thoughts... and then I started to pick on them."
    d "Do you know why I did that?"
    scene m224 with dissolve
    b "I don't care."
    b "You have no idea how I feel."
    scene m223 with dissolve
    d "Do you think Nami and Nojiko never did what Amber just did?"
    scene m225 with dissolve
    b "You have no idea how it feels when people keep telling you from a very young age... day after day... how weird you are."
    b "How it is when every time something broke, the teachers scolded me. How every time someone got hurt, people glanced at me."
    b "When you hear as a child how adults are talking behind your back. Calling you a psycho... a- a weirdo!"
    b "When parents tell their children not to invite me to their birthday parties because of the way I supposedly am!"
    b "You get so fixated on trying to be not weird that you actually become weird.."
    d "...Then you gave them what they wanted?"
    scene m220 with dissolve
    b "No."
    b "I still tried to fit in- but you can't change a fool's mind."
    b "I just stopped at some point and- got bitter."
    scene m223 with dissolve
    d "I do know how that feels."
    d "They didn't call me a psycho but a cold hearted, mentally crippled kid."
    d "It stopped hurting someday but... I'll always remember that one specific incident... when I heard another parent tell their kids to keep their distance from me."
    d "This contemptuous look the parent gave me. It really hurt and- shook my self-worth quite a bit."
    pause
    scene m220 with dissolve
    menu:
        "You were right... We aren't so different.":
            scene m226 with dssr
            $ BTY = True
            $ bellalove +=1
            $ achievement.grant("NotSoDifferent")
            $ achievement.sync()
            pause
        "Don't say it":
            pass
    scene m227 with dissolve
    pause
    scene m228 with dissolve
    b "*sigh* Give me- 10 minutes."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    show text "You enter the room again after 10 minutes." with Dissolve(1.5)
    $ play_playlist(playlist_Chapter1d)
    scene m231 with dssb
    d "Should we start with work?"
    b "Soon."
    b "This took them forever."
    d "What's in there?"
    scene m232 with dssr
    b "That's none of your business."
    scene m233 with dssa
    d "Mh."
    d "What do you think about class 9oD?"
    if BTY is True:
        scene m234 with dssa
        b "I couldn't care less about them."
        scene m235 with dssa
        b "But it looked like you already found a friend."
        scene m237 with dssr
        d "Nia?"
        scene m236 with dssa
        b "The redhead with the piercings."
        scene m237 with dssa
        d "Yeah, that's Nia. She's kinda weird."
        scene m238 with dssa
        b "So you two match."
        scene m239 with dssr
        "Bella stares thoughtfully into the distance."
        scene m240 with dssa
        b "I know Robin from back in elementary school."
        scene m241 with dssa
        d "The melody of your voice changed."
        d "I assume your relationship was good?"
        scene m242 with dssa
        if BTY is True:
            b "Not good, but not bad either. She didn't judge me like all the others did."
            b "She treated me like a normal child."
        else:
            b "More like neutral."
    else:
        scene m234 with dssa
        b "I don't give a fuck about them."
    scene m243 with dssa
    "You both sit there in silence for a few seconds."
    scene m244 with dssa
    d "When we go shopping ca-"
    scene m245 with dssa
    "She starts laughing."
    scene m246 with dssa
    b "Shhh..."
    scene m247 with dssr
    pause
    scene m248 with dssa
    b "Listen..."
    b "It's not 'we'. I go shopping and you will wear what I choose for you."
    scene m246 with dssr
    d "I don't even get to decide on the clothes?"
    scene m249 with dssa
    b "Remember, I'm the one paying!"
    b "You can of course choose your own clothes... but this also means that you have to pay by yourself."
    scene m250 with dssa
    b "And where we are going, a nice suit often costs 12.000$."
    scene m251 with dssa
    d "What?! Where the fuck are we going?!"
    d "I will never be able to pay you back!"
    scene m252 with dssr
    b "You don't need to pay me back... in money."
    scene m251 with dssr
    "You give her a serious look"
    d "What do you want from me?"
    scene m253 with dssa
    b "Two favors."
    scene m254 with dssa
    d "Oh for fuck's sake..."
    if BTY is True:
        d "(Why's that cunt exactly like me.)"
    scene m255 with dssa
    b "It's either that or we scrap the whole thing."
    scene m254 with dssa
    d "And let him hit on your mom?"
    scene m256 with dssa
    if bellameet is True:
        b "No, I'll handle it myself then... and Mila will be in deep shit."
    else:
        b "No, I'll handle it myself then... And they will keep picking on Mila until someday... She'll get into some deep shit."
    scene m257 with dssr
    d "Bitch."
    d "Fine."
    scene m258 with vpunch
    cl "Belllllaaa!"
    scene m259 with dssr
    b "Oh, hey Claire."
    b "Have you ever heard about knocking?"
    if bellameet is False:
        scene m260 with dssr
        d "(It's the nurse.)"
        scene m261 with dssa
        cl "Oh! If it isn't... you never told me your name."
        scene m262 with dssa
        d "[name]."
        scene m269 with dssa
        cl "Oh! If it isn't [name], whose balls I had to inspect!"
        cl "Very photogenic balls."
        scene m270 with dssa
        b "Eww."
        scene m271 with dssa
        cl "Bella! Do I need to explain to you that there are body parts which are much better for handling a man's privates?"
        scene m272 with dssa
        b "Shut up. Even the sun can't take your bullshit."
        scene m268 with dssr
        cl "Is that a-"
        scene m267 with dssa
        b "Yes."
    else:
        scene m261 with dssr
        cl "Hi, I am Claire!"
        scene m262 with dssa
        d "Hi, [name]."
        scene m263 with dssa
        b "She's my aunt and also works as a nurse at our college."
        scene m264 with vpunch
        cl "Doctor!"
        scene m265 with dssa
        b "Even the sun doesn't believe you."
        scene m266 with dssa
        cl "Shut up! I have a medical degree."
        scene m267 with dssr
        b "I am still convinced you fabricated it."
    scene m274 with dssr
    b "Were you at a party? You smell like party."
    scene m275 with dssa
    cl "I was at a rave."
    scene m274 with dssa
    b "Oh god, an old woman like-"
    scene m276 with vpunch
    cl "Hey! I am not old!"
    cl "I look like 24!"
    scene m277 with dssa
    b "More like 42."
    scene m273 with vpunch
    cl "Shut it!"
    scene m278 with vpunch
    "Claire's push causes Bella to fall against her package."
    scene m279 with dssr
    pause
    scene m280 with vpunch
    pause
    $ persistent.unlockedImageClaire3 = True
    scene m281 with dssr
    "You hear the package rip open and its insides spill to the ground."
    scene m282 with dssa
    cl "Oops."
    scene m283 with dssa
    "Bella jumps from the bed."
    scene m284 with dssa
    b "God! You stupid moron!"
    scene m285 with dssa
    cl "Sorry."
    scene m286 with dssa
    pause
    scene m287 with dssa
    cl "Respect."
    scene m288 with dssa
    cl "By the way... You should try out the- "
    scene m289x with vpunch
    b "Get out!"
    scene m290x with dssa
    cl "I'll see you, sweety!"
    scene black with tleaf
    with Pause(.5)
    scene m291x with tleaf
    pause
    scene m292x with dssa
    d "Do we plan on finishing this today? This seems like a lot of work."
    "Bella keeps quiet for a few seconds."
    scene m293x with dssr
    b "Wow."
    b "You don't even comment on what you just saw."
    scene m294x with dssa
    d "Why would I?"
    scene m295x with dssa
    "She keeps quiet again."
    scene m296x with dssa
    b "Every other guy I know would have commented on the... items in that box."
    scene m297x with dssr
    d "Well, I won't."
    if bellameet or BTY is True:
        scene m298x with dssr
        b "I like that about you..."
    d "Your aunt is funny."
    scene m299x with dssa
    b "She is 12 years younger than my mother... She is in her early 30s but mentally she can't be older than 16."
    if BTY is True:
        scene m300x with dssa
        b "But when I was younger, she was always there for me."
        scene m301x with dssa
        d "Yeah, you two strike me more as friends than relatives."
    else:
        scene m301x with dssa
    d "Let's get to work."
    scene black with Dissolve(2)
    with Pause(.5)
    scene m302x with dssb
    b "There's an obligate type and a facultative type."
    scene m303x with dssa
    d "So it doesn't need a host cell to reproduce?"
    scene m304x with dssa
    b "Nope. It can do it inside and outside."
    b "And I think the fatty in our assignment has a facultative parasite!"
    scene m305x with dssa
    d "The assignment clearly states that it's a virus."
    scene m306x with dssa
    b "I call bullshit! It's a trap."
    b "I'm seventy percent sure it's Histoplasma capsulatum, a damn fungus."
    scene m307x with dssa
    d "Let's just... think about it for a while and we'll discuss it next time."
    scene m309x with dssr
    b "Next time?"
    scene m308x with dssa
    d "I have to leave now."
    scene m309x with dssa
    b "Therapy?"
    scene m308x with dssa
    d "Yes."
    scene m310x with dssa
    b "Okay."
    scene m311x with dssr
    b "I'll see you there later."
    d "Mhm."
    scene m312x with dssr
    pause
    scene m313x with dssa
    pause
    if BTY is True:
        scene m314x with dssr
        pause
        scene m315x with dssa
        pause
        scene m315x with dssa
    $ play_playlist(playlist_Chapter1c)
    scene black with Dissolve(2.5)
    with Pause(.5)
    scene ss202 with dssb
    pause
    scene ss203 with dssa
    m "Aww. This looks very nice."
    scene ss204 with dssr
    m "...I've heard only good things about Dr. von Halen."
    d "Amber von Halen?"
    m "Oh, do you know her?"
    d "Her daughter is my project partner."
    m "Oh, she is in for a treat then."
    scene ss205 with dssr
    d "No, she knows I am her patient... I just didn't know her surname."
    scene ss206 with dssr
    m "That's good! This means it won't be a total stranger."
    scene ss207 with dssa
    d "*You take a deep breath* Both have their advantages."
    scene ss209 with dssa
    m "I am here. Don't worry."
    m "The biggest and most important step is the first one."
    m "Actually looking for help."
    scene ss208 with dssa
    d "It's not like I went looking for it... You did."
    scene ss210 with dssr
    m "Thank me later."
    scene ss211 with dssr
    pause
    scene ss212 with dssr
    d "(Oh great.)"
    scene ss213 with dssr
    d "Miss Marla."
    scene ss214 with dssa
    ma "Oh- *an unusually long pause* [name]."
    scene ss215 with dssa
    d "Noji, this is my professor, Miss Marla."
    scene ss216 with dssa
    m "Oh! I beg your pardon."
    scene ss217 with dssa
    ma "Hello. You must be Miss Miyazaki?"
    m "I am, it's nice to meet you, Miss Marla."
    scene ss218 with dssr
    ma "It's nice to meet you too, Miss Miyazaki."
    scene ss219 with dssa
    am "Good evening, Miss Miyazaki."
    scene ss220 with dssa
    m "Good evening, Miss von Halen."
    scene ss222 with dssa
    am "Ah, [name]. It's so good to see you!"
    scene ss221 with dssa
    d "Hi."
    scene ss223 with dssa
    am "Very well. Please follow me into my office."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ss195 with dssb
    am "Nojiko, [name] and my daughter are college project partners, in case you didn't know."
    scene ss196 with dssa
    m "Yes, he told me on the way here."
    scene ss195 with dssa
    am "Good."
    scene ss198 with dssa
    am "We will discuss a few details, but then I have to ask you to wait outside, Nojiko."
    scene ss197 with dssa
    m "Of course."
    scene ss199 with dssr
    am "We will see how today goes, and then we'll create a plan for your next sessions, [name]."
    "You nod."
    scene ss200 with dssa
    am "If I may speak to you alone, Nojiko?"
    m "Sure."
    scene ss201 with dssa
    pause
    stop music fadeout 2.5
    scene black with Dissolve(2)
    with Pause(.5)
    scene ss190 with dssb
    d "*You exhale loudly.*"
    scene ss191 with dssr
    d "(Hmm... A teddy.)"
    scene ss192 with dssr
    "You grab the little, soft teddy."
    d "(He feels a little rough... You must have seen a lot.)"
    play music "music/VeskyBeyondTheWindow.ogg"
    scene ss193 with dssa
    pause
    scene ss194 with dssa
    d "(I feel watched.)"
    scene ss152 with dssb
    pause
    scene ss153 with dssr
    pause
    scene ss154 with dssa
    am "*Soft* Hello [name]."
    am "I was looking forward to this since we first met."
    scene ss155 with dssr
    am "Nojiko is going to wait outside."
    am "She did not tell me anything. I want to hear it all from you."
    scene ss157 with dssr
    d "What is 'all'?"
    scene ss156 with dssa
    am "Nothing you say here will leave this room."
    scene ss157 with dssa
    d "(If she only knew about Bella and her folder-peeking.)"
    d "(On the other hand I could use this to manipulate Bella... Say some things that mess with her head when she dares to peek into my folder... There's no way she wouldn't peek into it.)"
    d "That's good."
    scene ss158 with dssr
    am "And you found the teddy I got for you."
    scene ss159 with dssa
    d "For me?"
    scene ss158 with dssa
    am "Yes, it was my teddy from when I was younger."
    scene ss159 with dssa
    d "I don't understand?"
    scene ss160 with dssr
    am "The day and time will come when we have to be strong enough to let things we hold dear to us move on into the next life."
    am "The ability to let go is invaluable, and I can't expect you to let something go without me doing it first."
    scene ss161 with dssa
    am "Take good care of him and... when the time comes, let him move on."
    scene ss162 with dssa
    "You keep quiet."
    scene ss164 with dssr
    am "I sensed a certain aura around you when I first saw you in my kitchen."
    am "If I dare to presume... you lost someone?"
    scene ss163 with dssa
    d "You could say that, yes."
    scene ss164 with dssa
    am "Someone who was very close to you?"
    scene ss163 with dssa
    d "Someone I loved."
    d "More than my own life..."
    scene ss164 with dssa
    am "What was her name?"
    scene ss163 with dssa
    d "...Summer."
    scene ss165 with dssr
    am "I get the feeling that you are... Let's say in some way blaming yourself?"
    scene ss166 with dssa
    d "It... wasn't my fault. I had no other choice..."
    scene ss167 with dssa
    am "What happened to Summer?"
    scene ss168 with dssr
    "You feel it creep up... A sensation... First on your skin... your hair stands up. The air thickens around you and you're starting to sweat."
    scene ss169 with dssa
    am "Okay [name], calm down. It's okay..."
    am "Let me ask you something else..."
    am "What emotions emerge when you think about her?"
    scene ss170 with dssa
    d "Grief... Emptiness... As if a part of me died."
    scene ss171 with dssr
    d "(I'm sweating and I can't keep my hands from shaking... Confronting these thoughts I had buried so deep.)"
    scene ss172 with dssr
    am "I apologize for being so direct, [name]."
    am "I just wanted to stimulate your feelings."
    scene ss174 with dssr
    "Amber gets up and gently lowers herself on the couch."
    scene ss173 with dssa
    am "Tell me a little bit about her. What was she like?"
    scene ss175 with dssa
    d "Summer... she was nice. Not too nice but just the right balance of a jerk and nice."
    d "And she certainly wasn't a pushover."
    $ persistent.unlockedImageAmber3 = True
    scene ss176 with dssa
    am "How did you two meet?"
    scene black with Dissolve(1.5)
    with Pause(.8)
    scene m328 with dissolve
    d "These stupid bug bois! There are so many!"
    scene m329 with dissolve
    n "[name]!"
    scene m330 with vpunch
    d "Mh?"
    n "I made a new friend! A super duper friend!"
    d "Ah and now?"
    scene m331 with dissolve
    n "She is soooo funny! I invited her over!"
    scene m332 with dissolve
    d "I am playing here... so just don't bother me and keep her away from me."
    scene m333 with dissolve
    n "I wouldn't want you two to meet anyways! She is so much cooler than you!"
    n "Baaah!"
    scene m334 with vpunch
    d "Give me my controller back!"
    scene black with Dissolve(1.5)
    with Pause(.5)
    scene m335 with dissolve
    d "*Mumbles* Stupid bug bois."
    "You hear voices in the hallway."
    m "Hello! I am Nojiko."
    s "I am Summer!"
    m "That's a beautiful name!"
    pause
    n "No, that's [name]'s room... Come let's go to mine. He said we shouldn't bother him."
    scene black with Dissolve(1.5)
    with Pause(.5)
    scene ss173 with dssr
    am "So it didn't seem like you were going to like each other at first?"
    scene ss174 with dssa
    d "Yes... Her and Nami were very close at the beginning."
    scene ss173 with dssa
    am "I assume this changed over the course of your relationship?"
    scene ss174 with dssa
    d "*You pause for a second* Not just that... they started to dislike each other."
    scene black with Dissolve(1.5)
    scene m336 with vpunch
    s "Hey!"
    d "Get out!"
    s "Nami told me you killed her hamster!"
    s "How dare you!?"
    scene m337 with dissolve
    d "I- what?!"
    d "It died because of old age!"
    scene m339 with dissolve
    n "No! I gave him to you when I was at Girls Camp! You were supposed to take care of him!"
    n "And when I came back, he was dead!"
    d "I took good care of him!"
    scene m338 with dissolve
    s "Do you have proof?!"
    d "Do you have proof that I killed him?!"
    scene m340 with dissolve
    n "We do!"
    scene m342 with dissolve
    d "That was a joke!"
    scene m343 with dissolve
    n "I didn't find it funny!"
    scene m344 with dissolve
    s "Did you eat him?!"
    d "No!"
    d "Now get out!"
    scene m345 with dissolve
    n "Come Summer! Let's leave this hamster killer alone!"
    scene m346 with dissolve
    s "Not so fast!"
    s "What if we don't leave, mhhh?"
    s "Are you going to cry to mommy?"
    d "I punch you."
    scene m347 with vpunch
    pause
    scene m349 with dissolve
    pause
    scene m350 with dissolve
    d "Argh!"
    scene m351 with vpunch
    n "No, no! Stop!"
    scene m352 with dissolve
    s "Ahh my hair! My hair!"
    scene m353 with dissolve
    s "Get off my hair!"
    d "You're a girl! Why would you even fight me?"
    scene m354 with dissolve
    s "You think you're stronger than me just because you're a boy!?"
    d "Yes?"
    scene m355 with dissolve
    s "I fought against many boys and I won!"
    d "Liar!"
    scene m356 with vpunch
    s "ARhhh-ghhh"
    scene m357 with vpunch
    pause
    scene m358 with dissolve
    n "Noo! Enough!"
    scene m359 with vpunch
    n "I said enough!"
    d "Do you give up?"
    scene m360 with dissolve
    s "I do."
    scene m361 with Dissolve(2)
    d "When I come back from the bathroom, you two had better be gone!"
    scene m362 with dissolve
    n "*shy whisper* Okay."
    scene m363 with dissolve
    pause
    scene m364 with dissolve
    n "That was brutal!"
    scene m366 with dissolve
    s "It was just fun."
    n "It didn't look fun."
    s "It was fun. We both held back."
    scene m365 with dissolve
    n "[name] is stupid.."
    scene m367 with dissolve
    s "I like him."
    n "Whaaat?"
    s "I don't know... He is cute."
    n "Ewww!"
    scene m368 with dissolve
    pause
    scene black with Dissolve(1.5)
    with Pause(.5)
    scene ss176 with dssb
    am "And did Nami tell you that Summer liked you?"
    scene ss175 with dssa
    d "Yes."
    d "I guess she hoped it would gross me out."
    scene ss176 with dssa
    am "Did it?"
    scene ss177 with dssa
    d "I pretended that it did. Yet, she left an impression on me."
    scene ss178 with dssr
    am "Am I right to assume that Nami wasn't happy with it?"
    scene ss180 with dssa
    "A little clock rings. Signaling the end of the session."
    scene ss178 with dssa
    am "Please finish your sentence."
    scene ss179 with dssa
    d "No... She certainly wasn't happy with that. For her it must've felt like Summer was ditching her for me."
    scene ss181 with dssr
    "Amber keeps silent for a few seconds. Visibly thinking."
    scene ss182 with dssa
    am "This is it for today, [name]. Sadly we only had half a session."
    scene ss183 with dssa
    d "...Okay."
    scene ss182 with dssa
    am "But there is a free space for tomorrow and I'd like you to come."
    scene ss184 with dssr
    d "Uh- I need to talk about it with Nojiko... I don't know if we can afford that."
    scene ss185 with dssa
    am "Of course."
    if BTY is True:
        am "I'll give you and Nojiko a discount."
        scene ss186 with dssr
        d "I assume you don't do that for everyone."
        scene ss187 with dssr
        am "I treat all my patients the same. But it's in my own interest that your treatment is a success."
        scene ss188 with dssa
        d "I assume it's because of Bella."
        scene ss187 with dssa
        am "Yes."
        scene ss189 with dssa
    else:
        scene ss189 with dssr
    am "Don't forget your teddy."
    stop music fadeout 2.
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch1CollegeBella)
    scene ss224 with dssb
    pause
    scene ss225 with dssa
    pause
    scene ss226 with dssr
    pause
    scene ss227 with dssr
    m "Hey! Everything alright [name]?"
    d "Yeah."
    scene ss228 with dssr
    am "Bella? What are you doing here?"
    scene ss229 with dssr
    b "Hi."
    b "I'm waiting for him."
    scene ss230 with dssa
    with Pause(.6)
    scene ss231 with dssa
    pause
    scene ss234 with dssr
    m "Oh, you must be his project partner."
    scene ss232 with dssr
    b "Mhm. Hi."
    scene ss233 with dssa
    am "Bella could you wait outside, please?"
    b "Mh."
    scene ss235 with dssr
    "You all wait for Bella to leave the office."
    scene ss236 with dssa
    am "So Noj- Miss-"
    scene ss237 with dssa
    m "Nojiko please."
    scene ss238 with dssa
    am "Nojiko, I'd like to see him again tomorrow."
    scene ss237 with dssa
    m "Oh well, sure."
    scene ss239 with dssa
    d "...Don't just say yes. Can we even afford that?"
    scene ss237 with dssa
    m "Yes."
    "Amber nods."
    if bellameet is True:
        scene ss238 with dssa
        am "And please call me Amber."
        scene ss242 with dssr
        m "Amber... Don't take this the wrong way, but I think we have to be honest with each other."
        m "The final straw that made me look for a therapist was the night he vanished to do something with his project partner... Your daughter... It seems."
        scene ss240 with dssr
        am "Oh really?"
        d "(Oh shit.)"
        am "Thank you, Nojiko."
        am "I'll definitely have a talk with my daughter."
        scene ss243 with dssr
        m "I really don't want to cause trouble, but I think it's important that we are honest with each other."
        scene ss241 with dssr
        am "That's true, and thank you for telling me."
    scene ss244 with dssr
    "They both look at you."
    d "Till tomorrow then."
    scene ss245 with dssa
    am "Yes. Take care, [name]."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    $ play_playlist(playlist_Ch5_Nia)
    with Pause(.5)
    scene m396 with Dissolve(2.5)
    pause
    scene m399 with dissolve
    pause
    scene m397 with dissolve
    pause
    scene m399 with dissolve
    pause
    scene m398 with dissolve
    pause
    scene m395 with dissolve
    pause
    $ persistent.unlockedImageBella10 = True
    scene m402 with Dissolve(1.2)
    b "You're Asian?"
    scene m403 with dissolve
    d "Do I look Asian? She's not my mother."
    if bellameet is True:
        d "A little warning... Nojiko just told Amber that we met up the other night."
        scene m404 with dissolve
        b "What?!"
        d "Yes... Prepare yourself."
        b "Damn it!"
        b "Why would you tell her about it?!"
        d "I didn't... I made the mistake of telling Nami and... accidentally spilled the beans... And she put two and two together."
        scene m405 with dissolve
        b "*sigh* I'll deal with that later."
    scene m406 with dissolve
    b "Get in."
    d "The car gives me all sorts of cancer."
    b "And I hope it will kill you."
    scene black with Dissolve(1.5)
    with Pause(.5)
    scene m407 with Dissolve(1.5)
    pause
    scene m408 with dissolve
    d "Where is the boutique?"
    b "Further down the street."
    d "Then why do we park here?"
    scene m409 with dissolve
    pause
    scene m410 with dissolve
    d "Barber- No!"
    b "Yes."
    scene m411 with dissolve
    d "No! That's too much!"
    scene m412 with dissolve
    b "You will get a haircut!"
    d "No!"
    b "Have you looked in the mirror lately?"
    b "You look like some ugly ass hobo!"
    d "I don't give a fuck. I cut my hair myself!"
    scene m413 with dissolve
    b "Okay, if you don't go in there, I'll take you home and we cancel the whole plan."
    d "Okay."
    b "Alright."
    scene m414 with dissolve
    pause
    scene m415 with dissolve
    pause
    scene m416 with vpunch
    b "For fuck's sake! Get out of the car and get a fucking haircut!"
    "You stay silent"
    scene m417 with vpunch
    "Bella punches you on the shoulder."
    scene m418 with vpunch
    "You punch her back."
    scene m419 with vpunch
    b "Get the fuck out of this car and get a fucking haircut!"
    scene m420 with vpunch
    pause
    scene m421 with vpunch
    d "OKAY! GOD!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene m422 with Dissolve(2)
    pause
    scene m423 with dissolve
    b "Emilio."
    scene m424 with dissolve
    emi "Bellaah! Good to see you sweetheart!"
    scene m425 with dissolve
    emi "I knew you weren't dead!"
    b "What?"
    scene m426 with dissolve
    emi "Oh my... what do we have here?!"
    b "It's urgent."
    scene m427 with dissolve
    emi "Oh! What happened to you?"
    scene m428 with dissolve
    emi "Say no more! Desiree! We have an emergency! Get the good stuff!"
    d "*sigh*."
    scene m429 with dissolve
    emi "How should we do it?"
    d "TH-"
    scene m430 with dissolve
    emi "No, No. You stay quiet. I was asking the beautiful lady over there.."
    scene m431 with dissolve
    b "Hmm.."
    scene m432 with dissolve
    b "How about this?"
    scene m433 with dissolve
    emi "What about this?"
    b "Na."
    scene m434 with dissolve
    b "This here."
    scene m435 with dissolve
    emi "Yes. This could work."
    scene m436 with dissolve
    emi "Desiree! Bring our guests some wine."
    b "Not for me. I'm driving."
    scene m437 with dissolve
    d "A lot for me, please."
    desi "Of course, honey."
    scene m438 with dissolve
    d "Why am I not allowed to pick my own hair style?"
    scene m439 with dissolve
    pause
    scene m440 with vpunch
    b "Hahaha!"
    emi "Hahaha!"
    scene m441 with dissolve
    emi "No offense boy, but I am sure you've never even heard of fashion before."
    scene m442 with dissolve
    desi "Here you go, boy."
    d "Thanks."
    scene m443 with dissolve
    emi "*Whisper* He needs some real clothes."
    scene m445 with dissolve
    b "*whisper* That's our next stop."
    scene m443 with dissolve
    emi "*whisper* It warms my heart to see that you take care of the less fortunate... The ones born without any sense of fashion."
    d "I can hear you."
    emi "We know."
    scene m444 with dissolve
    d "*whisper* Cunts."
    emi "I heard that."
    d "I know."
    if BTY is True:
        scene m448 with dissolve
        emi "Uuuhh, you two are a perfect match!"
        scene m446 with dissolve
        b "What?"
        emi "You two are gorgeous together. I was always afraid you would end up alone, Bella."
        scene m447 with dissolve
        b "We aren't together!"
        emi "*whisper* Yet."
        b "I heard that!"
        emi "I know."
    scene m449 with Dissolve(1.5)
    pause
    scene m450 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene m452 with dssr
    emi "My, my... what a handsome young man!"
    desi "Definitely an improvement."
    scene m453 with dssr
    b "Still ugly, but at least I lost the urge to vomit."
    emi "Bella, you'd better put your flag into him before someone else does it."
    scene m454 with vpunch
    b "Go and die, Emilio."
    d "Please... kill me."
    scene m456 with Dissolve(2)
    emi "Don't be surprised if you attract the attention of the other sex from now on."
    if BTY is True:
        scene m458 with dissolve
        emi "*whisper* Or the attention of one particular woman.."
        scene m459 with vpunch
        b "Fuck off, Emilio!"
    emi "It was a pleasure to see you again Bella!"
    b "Yes..."
    if BTY is True:
        scene m458 with dissolve
        emi "Boy... what is your name?"
        d "[name]."
        emi "[name], take good care of her."
        scene m459 with vpunch
        b "I swear Emilio, I will set your fucking shop on fire!"
        emi "Take care you two!"
    scene m460 with Dissolve(2)
    pause
    scene m461 with dssr
    desi "It was lovely to see Bella again."
    emi "Yes... It's great to see that Bella is still well."
    scene m463 with dssr
    desi "What is it?"
    scene m462 with dssr
    emi "She reminds me of someone."
    scene m464 with dssr
    desi "Yes, they do indeed have similar character traits."
    emi "Also, do a little background check on the boy."
    desi "[name]? Do you suspect something?"
    emi "No, no. But you can never be too sure."
    desi "As good as done."
    stop music fadeout 3.0
    scene black with Dissolve(1.5)
    with Pause(.5)
    $ play_playlist(playlist_AmbientBellchen)
    scene m465 with Dissolve(2)
    pause
    d "I look disgusting."
    scene m467 with dissolve
    b "Less disgusting than an hour ago... but still disgusting."
    scene m466 with dissolve
    d "What a weird guy that was."
    scene m467 with dissolve
    b "Emilio is cool."
    scene m468 with dissolve
    b "He can get you all kinds of things."
    d "So he isn't just an incredibly gay barber?"
    b "Not many people know this but... He has some connections deep into the black market."
    b "Or do you think he has that Rolex because he owns a small barbershop?"
    d "Why would you tell me this? This is pretty sensitive information."
    scene m469 with dissolve
    b "We are on a risky mission... If something goes wrong and it hits me... You might need his help."
    b "He can also get you all sorts of information... if you got the money."
    d "(All sorts of... information.)"
    d "Next stop, clothes?"
    b "Yes."
    scene m466 with dissolve
    d "Mhhmm."
    d "This haircut-"
    scene m467 with dissolve
    b "It's similar to the one you had when you were younger... Just wilder."
    d "Did we know each other?"
    scene m468 with dissolve
    b "No, I looked you up and found some older pictures Nami posted."
    b "I didn't want to give you a totally fucked up hairstyle... so I went with something you might feel comfortable with."
    b "Because real beauty comes through confidence."
    scene m470 with dissolve
    b "Even tho you-"
    scene m472 with dissolve
    d "Bla bla bla... Shut up. I've heard it a million times already."
    scene m471 with dissolve
    b "Okay. This is important."
    b "It's best if you just do nothing..."
    b "Don't touch anything. Don't talk to anybody. Just be a ghost until I speak to you."
    b "And judging by your looks... You should be used to the 'ghost' role."
    b "Wait inside and don't move. I'll get you when I find something."
    stop music fadeout 3.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch4x53)
    scene ee82 with dssb
    pause
    scene ee83 with dssa
    b "Stay here and don't look poor."
    scene ee84 with dssa
    "She looks you up and down."
    scene ee83 with dssa
    b "...Just stay here."
    scene ee85 with dssa
    d "(I totally won't.)"
    scene ee86 with dssa
    ow "Oh... Not again."
    scene ee87 with dssa
    ow "*whispers* Security. It seems like the thieves are back."
    scene ee88 with dssa
    d "(That's so soft... I didn't know something that soft could exist.)"
    scene ee89 with dssa
    ow "Excuse me!"
    d "(...A zombie.)"
    scene ee90 with dssa
    ow "I think you're in the wrong shop."
    d "I-"
    play music "music/Suspense/Scott Buckley - Resonance.ogg"
    scene ee91 with vpunch
    ow "See if he has anything in his pockets."
    scene ee93 with vpunch
    d "What the-?!"
    scene ee94 with dssa
    sec "A phone."
    scene ee95 with dssa
    ow "Maybe in his pants."
    scene ee96 with vpunch
    d "If you dare to touch me below my belt, I'm going to beat the shit out of you!"
    scene ee97 with vpunch
    b "Hey!"
    scene ee98 with dssa
    ow "Miss von Halen, don't be worried we have it under control."
    scene ee99 with dssr
    b "He- *sigh*"
    scene ee100 with dssa
    b "-belongs to me."
    ow "Oh. Wh-."
    scene ee101 with vpunch
    "Bella shoves the clerk to the side."
    scene ee102 with dssa
    if BTY is True:
        b "Now get your hands off him!"
    else:
        b "Let him go!"
    scene ee103 with dssr
    ow "I beg your pardon, Sir."
    "You stare at him without moving a muscle."
    scene ee104 with dssa
    ow "I'll give you a discount. I apologize for my misjudgment."
    scene ee105 with dssa
    pause
    scene ee106 with dssa
    b "Didn't I tell you to wait?"
    scene ee107 with dssa
    d "Since when do I listen to you?"
    scene ee108 with vpunch
    b "Get in there."
    scene ee109 with dssr
    d "The-"
    scene ee110 with vpunch
    d "What are you doing?"
    scene ee111 with dssa
    b "What?"
    d "Wait outside!"
    if BTY is True:
        scene ee112 with vpunch
        b "No."
        scene ee113 with dssr
        d "What do you mean? No?"
        scene ee114 with dssa
        b "*whisper* Just... change."
        scene ee115 with dssr
        "You two stare at each other."
        d "You're a fucking creep."
        scene ee116 with dssa
        b "*Whispers* Sue me."
        scene ee117 with dssa
        "You push her against the door. Her flexible body allowing her leg to rest over your shoulder."
        menu:
            "Refuse to change while she's present.":
                scene ee118 with dssr
                d "No fucking way. Get out or I'll leave right now."
                scene ee119 with dssa
                b "*Sigh* Pussy."
                scene ee120 with dssa
                b "The clothes are in this bag."
                b "Be fast."
                scene sba780 with dssr
                scene black with Dissolve(2)
                with Pause(.5)
                $ play_playlist(playlist_AmbientBellchen)
                d "(Oh god.)"
                scene sba781 with dssa
                d "I look like a fucking donkey!"
                scene sba783 with dssr
                b "Then you can imagine how much worse you looked before."
                scene sba782 with dssa
                pause
                scene sba784 with dssa
                b "Besides that... You don't have to wear it every day."
                scene sba785 with dssa
                d "Right.."
                d "I'll change back."
                scene sba783 with dssa
                b "Mhm. I'll try on some outfits in the meantime. Just wait until I'm done."
                scene black with Dissolve(2)
                with Pause(.5)
                scene m544 with dssr
                b "And? How does it look?"
                d "Ugly."
                scene m543 with dssr
                b "Fuck you."
                b "I know you don't have a sense for fashion... But if I have to spend a whole evening in public with you... At the very least I want to look good."
                b "Wait at the counter."
            "Change with her being present":
                $ UmB = True
                $ persistent.unlockedImageBella12 = True
                scene ee121 with dssr
                pause
                scene ee171 with dssa
                b "Uhh-"
                scene ee172 with vpunch
                b "What are you doing?!"
                scene ee173 with dssa
                with Pause(.3)
                scene ee174 with dssa
                with Pause(.3)
                scene ee173 with dssa
                d "What? You said I should change."
                with Pause(.3)
                scene ee172 with dssa
                b "But no... But not the boxers!"
                scene ee173 with dssa
                with Pause(.3)
                scene ee174 with dssa
                with Pause(.3)
                scene ee173 with dssa
                b "I- didn't even get you a new pair!"
                d "Then get me a pair."
                scene ee175 with dssa
                b "Oh my god..."
                scene ee176 with vpunch
                pause
                scene ee178 with dssa
                b "I see what this is... You're trying to make me feel awkward."
                scene ee177 with dssa
                d "And it worked."
                scene ee178 with dssa
                b "I could ram my knee with an unbelievable amount of force into your balls."
                scene ee179 with dssa
                "You just stare at her."
                scene ee180 with dssa
                pause
                scene ee179 with dssa
                b "I'll get you some new underwear."
                stop music fadeout 2.5
                scene black with Dissolve(1.5)
                with Pause(.5)
                $ play_playlist(playlist_AmbientBellchen)
                scene ee182 with dssr
                b "Are you still nude?"
                d "Yes."
                scene ee183 with dssa
                b "Here... Costs only $90."
                scene ee184 with dssa
                d "Why would anyone in their right mind pay so much for a pair of underwear?"
                scene ee185 with dssr
                b "*Laughs* Haha... What kind of fabric is this supposed to be?"
                scene ee186 with dssa
                b "Wh-"
                scene ee187 with dssa
                b "W-Where did you buy them?"
                d "I didn't buy them."
                scene ee188 with dssa
                b "Nojiko did? Hahaha!"
                scene black with Dissolve(2)
                with Pause(.5)
                scene sba761 with dssr
                d "It's so soft."
                scene sba762 with dssa
                b "Like your balls are in a bed made out of clouds?"
                scene sba761 with dssa
                d "Yes."
                scene sba763 with dssa
                d "Is this a suit?"
                scene sba764 with dssa
                b "No, more like a casual jacket and shirt."
                scene sba763 with dssa
                d "I'll look like a fucking donkey."
                scene sba764 with dssa
                b "Clothes make people."
                scene black with Dissolve(2)
                with Pause(.2)
                scene sba765 with dssa
                d "Called it... I look like a donkey."
                scene sba766 with dssa
                b "*sensual whisper* No... for the first time in your life you look good."
                scene sba767 with vpunch
                "You furrow your brows and she realizes what she just said."
                scene sba768 with vpunch
                b "Decent! I mean- n-not like pure shit!"
                scene sba769 with dssr
                d "*sigh*"
                b "Everyone can suit up but not everyone knows how to wear a suit."
                scene sba770 with dssa
                b "Tsk, look at your collar."
                $ MCBL +=1
                scene sba771 with dssr
                pause
                d "(Her scent is... intoxicating.)"
                d "(It's a very clean fragrance... Amber... Iris... Neroli... Kinda like the ones Nojiko wears.)"
                scene sba772 with dssr
                b "I need to fix it on the back, too."
                d "(This feeling... She makes me... feel weird.)"
                scene sba773 with dssr
                "Multiple seconds go by without anyone moving."
                scene sba774 with dssa
                d "...Bella."
                scene sba775 with dssr
                "You two slowly separate."
                scene sba776 with dssa
                b "Done."
                scene sba777 with dssr
                d "I don't look like myself."
                scene sba778 with dssr
                b "You don't have to wear it every day."
                d "Mhm."
                scene sba779 with dssr
                b "I saw something for me."
                b "Just put it all in the bag and wait outside when you're done."
                scene black with Dissolve(2)
                with Pause(.5)
                if MCBL == 1:
                    scene m531 with dssr
                    d "(Oh my god. No.)"
                    d "(It can't be... I can't be possibly-)"
                    scene m532 with dssr
                    b "And? How is it?"
                    scene m544 with dssr
                    d "(-falling for her..)"
                    scene m543 with dissolve
                    d "...Ugly."
                    b "Fuck you."
                    b "I know you don't have a sense for fashion... But if I have to spend a whole evening in public with you... At the very least I want to look good."
                    menu:
                        "You look... decent.":
                            $ bellalove +=2
                            scene m545 with dissolve
                            b "Thanks."
                        "Don't compliment her.":
                            pass
                    scene m544 with dissolve
                    b "Wait at the counter."
                else:
                    scene m544 with dssr
                    b "And? How does it look?"
                    d "...Ugly."
                    scene m543 with dssr
                    b "Fuck you."
                    b "I know you don't have a sense for fashion... But if I have to spend a whole evening in public with you... At the very least I want to look good."
                    b "Wait at the counter."
    else:
        scene ee114 with vpunch
        b "The clothes are in this bag."
        scene ee116 with dssr
        b "Be quick."
        stop music fadeout 2.5
        scene black with Dissolve(2)
        with Pause(.5)
        $ play_playlist(playlist_AmbientBellchen)
        scene sba780 with dssr
        d "(Oh god.)"
        scene sba781 with dssa
        d "I look like a fucking donkey!"
        scene sba783 with dssr
        b "Then you can imagine how much worse you looked before."
        scene sba782 with dssa
        pause
        scene sba784 with dssa
        b "Besides that... You don't have to wear it every day."
        scene sba785 with dssa
        d "Right..."
        d "I'll change back."
        scene sba783 with dssa
        b "Mhm. I'll try on some outfits in the meantime. Just wait until I'm done."
        scene black with Dissolve(2)
        with Pause(.5)
        scene m543 with dssr
        b "And? How does it look?"
        d "...Ugly."
        scene m544 with dissolve
        b "Fuck you."
        b "I know you don't have a sense for fashion... But if I have to spend a whole evening in public with you... At the very least I want to look good."
        scene m545 with dissolve
        b "Wait at the counter."
    $ persistent.unlockedImageBella16 = True
    scene black with Dissolve(1.5)
    with Pause(.5)
    scene m546 with dssr
    b "This is about it."
    scene m547 with dissolve
    ow "That makes $24.580."
    b "The discount you mentioned earlier."
    scene m548 with dissolve
    pause
    ow "$22.500 then."
    scene m550 with dissolve
    b "Hmm... I wonder what would happen if word got out to all my friends how this boutique handled my friend here... And if you just knew who his father is... Oh boy."
    scene m549 with dissolve
    ow "$18.500."
    b "That's better."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    scene m551 with dissolve
    d "Will you drive me home?"
    b "Yes."
    scene m552 with dissolve
    b "Where exactly do you poor people live?"
    d "Fuck off... and you obviously know where I live."
    scene m553 with dissolve
    b "Hehe. I do."
    d "So... Now that you forcefully prepared me. When will we go to the restaurant?"
    b "He is there tomorrow evening."
    scene m554 with dissolve
    b "I will give you the details."
    d "Alright."
    scene black with Dissolve(2.0)
    with Pause(.5)
    scene m555 with Dissolve(1.5)
    n "No, as far as I know big Grey is now the one in charge!"
    scene m556 with dissolve
    m "I am pretty sure the little blue one defeated him."
    scene m557 with dissolve
    n "No, I have read the comics! And I'm active in the forums!"
    scene m558 with dissolve
    n "See- yo.."
    scene m559 with dissolve
    m "What?"
    scene m560 with dissolve
    d "...Don't say anything. Please."
    scene m561 with dissolve
    n "Oh... My... God..."
    scene m562 with dissolve
    n "I think there was something in these cookies.."
    m "You look amazing, [name]!"
    d "Please don't... I'm hideous.."
    scene m563 with dissolve
    m "Come sit with us."
    m "I am happy seeing you like this!"
    m "What's in the bag?"
    scene m564 with dissolve
    d "Clothes..."
    scene m565 with dissolve
    m "You and Bella went shopping?"
    scene m564 with dissolve
    d "Mh.."
    scene m565 with dissolve
    m "Honey, you should have asked me for some money."
    scene m566 with dissolve
    n "Can I see them?"
    d "Feel free to do so."
    scene m567 with dissolve
    m "How was it? Did you two have fun?"
    scene m568 with dissolve
    n "Ugh."
    m "Close your dirty mind."
    d "*sigh* I don't feel like myself.."
    scene m569 with dissolve
    m "Honey, she did in one day what we tried to do in years."
    m "She forced you out of your shell."
    scene m570 with dissolve
    n "[name]?"
    d "Nami?"
    n "These clothes cost about $13.500."
    scene m571 with vpunch
    m "WHAT?"
    scene m572 with dissolve
    m "[name]?! Where did you get that much money?"
    d "I didn't... Bella paid for me..."
    n "Why would she do- you got something on her?"
    scene m572 with vpunch
    m "[name]?! Are you blackmailing her?!"
    d "No! Of course not!"
    m "Then why would she spend so much money on you?"
    if BTY is True:
        scene m573 with dissolve
        m "[name]... Please tell me you're not exploiting her affection."
        d "No I-... Affection?"
        m "Let's call it female intuition..."
        scene m574 with dissolve
        n "I swear [name]... Marry Vic, Mila, Ayua or even Jeff but please not her."
        m "Nami. If he likes Bella then you have to accept it."
        m "And why are you so hostile again?"
        scene m575 with dissolve
        n "Because she is the bitch that made a fool of me on the first day of college and got me a detention?!"
        m "Oh... I didn't know that."
        m "Be careful... both of you."
    else:
        scene m573 with dissolve
        d "She's investing."
        m "Into you?"
        d "Yes."
        m "Why?"
        d "I'll tell you when the time is right."
        m "Oh god... [name]! Stop it!"
    scene m576 with dissolve
    n "Noji..."
    "Nami pauses for a few seconds."
    n "Now that [name] is here. I have to ask you something."
    n "Who's Nick?"
    scene m578 with dissolve
    m "Uh-h Nick?"
    n "Mhm."
    m "He and I are dating."
    scene m576 with dissolve
    n "I see."
    n "And you kept it from us, why?"
    m "Well, you see-"
    scene m577 with dissolve
    n "Wait a moment... [name]?"
    d "Mh?"
    n "Did you know that she was dating a guy named Nick?"
    n "Don't say anything, I can see it on your face."
    scene m580 with dissolve
    m "Nami!"
    scene m581 with dissolve
    "You let out a small but audible 'sigh'."
    scene m582 with dissolve
    d "I just hope you're not surprised that she reacted like this."
    scene m583 with dissolve
    m "I'll talk to her."
    d "No. Let me."
    scene m584 with dissolve
    d "Just... make sure to apologize later."
    scene black with Dissolve(1.4)
    with Pause(.5)
    scene sba859 with dssr
    pause
    scene sba860 with dssr
    pause
    scene sba861 with dssr
    d "She was about to tell you."
    scene sba862 with dssr
    $ persistent.unlockedImageNami_CH2_3 = True
    n "Do you think it's because of the way I am?"
    scene sba863 with dssa
    d "Huh?"
    scene sba862 with dssa
    n "The people I actually care about don't seem to see me the same way."
    n "I have this growing feeling of bitterness and this urge to just leave one night... Just to see if it would matter."
    scene sba863 with dssa
    d "Being a melodramatic fuck is my job, not yours."
    scene sba864 with dssa
    n "What if my happiness is just a facade?"
    scene sba865 with dssr
    d "It's not."
    d "You're a quirky, weird moron who takes everything way too personal."
    scene sba866 with dssa
    d "You care a lot."
    d "*sigh* I am sorry that Noji and I are not as lovable."
    scene sba867 with dssa
    n "How long did you know?"
    d "One or two days."
    scene sba868 with dssa
    n "Oh... So not that long."
    scene sba869 with dssr
    n "Sometimes, I feel like a parasite in this house... Maybe I should move out."
    n "Neither of you tell me anything... I'm always left out."
    $ persistent.unlockedImageNami10 = True
    n "It's exactly the same situation as with Summer. Suddenly, I was the third wheel."
    scene sba871 with dssa
    d "Cheeto... We've been through that and we both remember very different things."
    scene sba870 with dssa
    menu:
        "You'll always play a significant role in my life.":
            n "You keep telling me how important I am to you, and then you leave me in the rain again to run off with some blond bitch!"
            n "...You tell me nothing. We spend less and less time together."
            scene sba872 with dssa
            d "You play games all day."
            scene sba870 with dssa
            n "Tha-... True."
            scene sba873 with dssr
            d "I feel like a burden to you."
            d "Nami, I'm constantly quiet, I don't make many jokes... I don't want to drag you down."
            scene sba874 with dssa
            d "I love that you are quirky and full of life and I don't want you to lose that because of me."
            scene sba875 with dssa
            n "You bitch."
            scene sba874 with dssa
            d "What?"
            scene sba875 with dssa
            n "You act like I haven't known you for the majority of my life. I can keep up with your melodramatic phases."
            n "You're a selfish douche."
            scene sba877 with dssr
            d "I am?"
            scene sba876 with dssa
            n "Oh yes. You don't spend time with me because you don't want to burden me."
            n "You don't do it because it burdens you."
            n "It's the exact same principle as people who tell their significant others that they have cheated on them."
            n "They might say 'She/He deserves to know it' but in the end they only do it so that they themselves feel better."
            scene sba878 with dssa
            n "And it is the exact same thing you are doing."
            n "You little bitch."
            $ persistent.unlockedImageNami11 = True
            scene sba879 with dssa
            "You let out a laugh."
            scene sba878 with dssa
            n "Why are you laughing?"
            scene sba879 with dssa
            d "I think you've got a point."
            scene sba880 with dssr
            "She sighs."
            scene sba881 with dssa
            n "I just want to feel like I'm a part of it."
            n "What's the point in living life if you do it without the people you care about?"
            scene sba883 with dssr
            pause
            scene sba882 with dssa
            n "...Please start telling me things."
            scene sba883 with dssa
            d "I will."
            scene sba884 with dssa
            n "...Tell me how you got that cut.."
            scene sba885 with dssa
            d "This is the only thing I won't tell you right now."
            d "I will tell you... But not now."
            scene sba884 with dssa
            n "It wasn't Bella?"
            scene sba883 with dssa
            d "No."
            scene sba882 with dssa
            n "I feared this. That means you got even more enemies."
            scene sba886 with dssr
            n "How do you feel about Bella?"
            scene sba887 with dssa
            menu:
                "I'm starting to like her":
                    scene sba886 with dssa
                    n "How much?"
                    menu:
                        "I actually think I am falling for her" if MCBL == 1:
                            $ NEWB = True
                            scene sba888 with dssa
                            n "What?!"
                            scene sba889 with dssa
                            d "I don't know what it is about her... And I don't want it to happen but... I would be lying if I'd say that there's nothing."
                            d "And it totally hit me when she and I were in the changing room together... She was so close to me. Her scent was incredible."
                            scene sba890 with dssa
                            n "I don't like Bella. I would even go as far to say I hate her... But if she makes you feel these things... Then I'll encourage this."
                            scene sba891 with dssr
                            n "Thank you. And please keep telling me things."
                            scene sba892 with dssa
                            d "Even if it's Bella related?"
                            scene sba891 with dssa
                            n "Yes... Especially then."
                        "Just a normal amount, duh.":
                            scene sba886 with dssa
                            n "Okay."
                            n "But it can always turn into more."
                            scene sba891 with dssr
                            n "I'm just glad you're telling me stuff again."
                            scene sba892 with dssa
                            d "Ya."
                "I don't know. I haven't made up my mind yet":
                    pass
            scene sba897 with dssr
            d "Wanna play something together?"
            scene sba898 with vpunch
            n "Yo!? REALLY?!"
            scene sba899 with dssa
            d "Why not. Fire up something we can play together."
            scene sba898 with dssa
            n "Shit emo, that's all you had to say!"
        "It was a different situation back then":
            scene sba894 with vpunch
            n "No it wasn't!"
            scene sba893 with dssa
            d "Nami-"
            scene sba894 with dssa
            n "I am only good enough when no one else is around!"
            scene sba895 with vpunch
            n "Get out!"
            scene sba896 with dssa
            d "Nami for fuck's sake! We've been through this-"
            scene sba888 with dssr
            n "Please leave."
    stop music fadeout 3.0
    scene black with Dissolve(1.5)
    show text "The next morning" with Dissolve(1.5)
    with Pause(0.5)
    hide text with Dissolve(1.5)
    scene ax1 with Dissolve(2)
    $ play_playlist(playlist_Jaccuzi)
    d "Mmmmmm..."
    d "*sigh*."
    d "I could visit the gym... if I plan on going for the basketball tryouts."
    d "And I'd like some muscles, too."
    menu:
        "Invite Nami to the gym" if namix == 0:
            $ fitness +=1
            $ namigym = True
            show n_1 with dssr
            pause
            show n_2 with dssa
            pause
            stop music fadeout 2.0
            jump namigym
        "Invite Bella to the gym" if BTY is True:
            $ fitness +=1
            $ bellagym = True
            show b_1 with dssr
            pause
            show b_2 with dssa
            pause
            stop music fadeout 2.0
            jump bellagym
        "Invite Mila to the gym" if milatalk is True:
            $ fitness +=1
            $ milagym = True
            show m_1 with dssr
            pause
            show m_2 with dssa
            pause
            show m_3 with dssa
            pause
            show m_4 with dssa
            pause
            show m_5 with dssa
            pause
            show m_6 with dssa
            pause
            stop music fadeout 2.0
            jump milagym
        "Go on your own.":
            $ fitness +=1
            $ gymalone = True
            stop music fadeout 2.0
            scene black with Dissolve(2)
            jump gymalone
        "Don't go to the gym.":
            $ NoGymCh3 = True
            d "(Not gonna happen.)"
            jump schoolch3

label gymalone:
    $ play_playlist(playlist_Gymch3)
    scene m1401 with Dissolve(2)
    d "(I should probably start with some cardio.)"
    scene m1402 with Dissolve(1)
    "You warm yourself up for 10 minutes."
    scene m1403 with dissolve
    pause
    scene m1404 with dissolve
    pause
    scene m1403 with dissolve
    pause
    scene m1404 with vpunch
    d "*moans in pain*"
    scene m1405 with vpunch
    rob "Hi."
    scene m1406 with dissolve
    d "Hi."
    scene m1405 with dissolve
    rob "Aren't we in the same class?"
    scene m1406 with dissolve
    d "Uh- I think so."
    scene m1405 with dissolve
    rob "My name is Robin."
    scene m1406 with dissolve
    d "I'm [name]."
    if BTY is True:
        scene m1405 with dissolve
        rob "Would you like to train with us?"
        d "Why?"
        scene m1408 with dissolve
        rob "W-why?"
        scene m1409 with dissolve
        d "Why would you ask me that?"
        scene m1408 with dissolve
        rob "I'm a little confused now, haha."
        scene m1409 with dissolve
        d "Well- uh... I don't know you?"
        scene m1408 with dissolve
        rob "Yes- but you and Bella do understand each other, right?"
        scene m1409 with dissolve
        d "A little, yeah."
        d "(She is the Robin from Bella's elementary school.)"
        menu:
            "Train with them.":
                $ mobility +=1
                d "I'd like to train with you."
                scene m1410 with dissolve
                rob "Great!"
                d "(She mentioned Bella. I assume she wants to get to know me because of her.)"
                stop music fadeout 2.0
                scene black with Dissolve(2)
                with Pause(.5)
                $ play_playlist(playlist_BigTiddyMila)
                scene m1346 with Dissolve(2.5)
                pause
                scene m1347 with dissolve
                rob "So- where do you know Bella from?"
                d "I didn't until a few days ago."
                scene m1348 with dissolve
                rob "Oh?"
                rob "You two are acting quite close."
                scene m1349 with Dissolve(1.5)
                d "Oh? We are not doing weights?"
                rob "I should've probably mentioned it. Today we are doing some mobility workouts."
                d "I actually wanted to lift weights."
                scene m1350 with dissolve
                rob "If you have a high mobility, you will get better results in weightlifting."
                scene m1351 with dissolve
                d "Okay, let's give it a try."
                scene m1353 with dissolve
                rob "We will start with something easy."
                scene m1356 with dissolve
                rob "Try to do what Sasha does."
                d "Just reaching for my- toes?"
                scene m1357 with dissolve
                rob "Mhm."
                scene m1360 with dissolve
                pause
                d "..."
                scene m1359 with dissolve
                rob "Do it."
                scene m1361 with dissolve
                d "(I can't reach any further...)"
                scene m1362 with dissolve
                d "...About that."
                rob "Try to hold it at the furthest point for as long as you can."
                scene m1361 with dissolve
                d "Shit- that hurts!"
                scene m1363 with dissolve
                d "So... Robin. What is the real reason you asked me to train with you?"
                "Robin stays silent for a few seconds."
                scene m1364 with dissolve
                rob "I am just here to give you a pro-"
                scene m1363 with dissolve
                d "Robin. You are easier to read than a dog that pooped in the house."
                d "You asked me in hope of gaining some information about Bella."
                scene m1365 with dissolve
                rob "I am sorry. Don't take it the wrong way."
                scene m1366 with dissolve
                d "I don't."
                d "It's a win-win."
                d "I learn something about mobility, and you also might get something out of it."
                scene m1367 with dissolve
                rob "I didn't expect you to view it so... objectively."
                scene m1368 with Dissolve(1)
                rob "*She hastily changes the topic* Anyways, it is about time you start doing more mobility workouts."
                rob "So that someday- you could do something like this."
                scene m1369 with dissolve
                pause
                d "Most likely not."
                d "I have a different focus. But a certain level of mobility is something I wouldn't say no to."
                rob "That's good."
                scene m1370 with dissolve
                d "So what is the deal between you and Bella?"
                scene m1371 with dissolve
                rob "She's a friend."
                rob "Or was a friend. I just-... *she takes a long pause*."
                scene m1372 with dissolve
                "- and falls into a silence."
                d "(I wonder what really destroyed their friendship.)"
                d "(It's almost like Robin feels guilty and just really wants to make up with her.)"
                scene m1373 with dissolve
                d "(This Sasha is staring into my soul. She is probably making sure I am not going too far with the Bella topic.)"
                scene m1374 with Dissolve(2)
                rob "Try this one here."
                d "I will die."
                scene m1375 with dissolve
                rob "Try it out."
                rob "I'll 'stabilize' you."
                $ persistent.unlockedImageRobin1 = True
                scene m1377 with Dissolve(3)
                pause
                rob "Does it hurt?"
                d "A- lot."
                rob "You are shaking quite heavily."
                d "Nnrgh- No- shit!"
                scene m1378 with vpunch
                "Suddenly, Robin's hand loses its grip and you fall over!"
                rob "Oh no!"
                scene m1379 with vpunch
                pause
                scene m1380 with dissolve
                rob "Are you okay?"
                d "Yeah."
                rob "Sorry- my hand is a little sweaty."
                rob "But hey... It will get easier over time."
                scene m1381 with dissolve
                d "I don't mind a challenge... as long as the person who is supporting me is actually capable of doing so."
                rob "I am so sorry!"
                scene m1382 with dissolve
                rob "Give me one second, I will get you a kettle bell."
                scene m1383 with Dissolve(2)
                pause
                scene m1384 with dissolve
                pause
                scene m1385 with dissolve
                pause
                scene m1386 with vpunch
                pause
                scene m1387 with Dissolve(2)
                rob "Nrrgh! H-ere!"
                d "Thanks."
                $ persistent.unlockedImageSasha2 = True
                scene m1388 with dissolve
                d "You could have said something and I would have gotten it myself."
                rob "It's alright."
                scene m1389 with dissolve
                rob "Here- look."
                scene m1390 with dissolve
                pause
                scene m1389 with dissolve
                rob "Do it like this."
                scene m1391 with Dissolve(1)
                pause
                scene m1392 with dissolve
                pause
                scene m1393 with dissolve
                pause
                scene m1394 with dissolve
                d "Nrh-"
                scene m1393 with dissolve
                pause
                scene m1394 with dissolve
                pause
                scene m1395 with dissolve
                rob "That was good."
                rob "But you still lack core strength."
                scene m1396 with dissolve
                if fitness == 2:
                    d "This is my second time inside a gym."
                    rob "Which means you have no idea what you are doing?"
                    d "Jeff showed me some stuff."
                    scene m1398 with dissolve
                    rob "Some stuff?"
                    d "We didn't do much."
                else:
                    d "This is my first time in a gym."
                    scene m1398 with dissolve
                    rob "And you were on your way to do weightlifting without any sort of instruction?"
                    d "...Yeah?"
                    rob "You shouldn't do that. You can really hurt yourself."
                scene m1397 with dissolve
                rob "I will ask Coach Hill if she can give you some instructions."
                d "That's not-"
                scene m1398 with dissolve
                rob "It is. If you foolishly hurt yourself, you can say goodbye to your chances of joining the first team."
                d "There is a first team?"
                scene m1400 with dissolve
                rob "Of course?"
                d "(It seems like I am missing some information here.)"
                d "I think I will end the training with some slight cardio."
                rob "Sure, you should take it easy at first anyway."
                d "Alright. Thanks for the workout."
                scene m1399 with Dissolve(1)
                rob "Bye!"
                scene black with Dissolve(2.4)
                stop music fadeout 2.0
                $ achievement.grant("GymAloneA")
                $ achievement.sync()
                jump schoolch3
            "Thanks but I'd like to train on my own.":
                scene m1408 with dissolve
                rob "Okay sure."
                scene black with Dissolve(3)
                show text "You train for another 20 minutes and then make your way to an early class." with Dissolve(3)
                with Pause(1.5)
                stop music fadeout 2.0
                $ achievement.grant("GymAloneA")
                $ achievement.sync()
                jump schoolch3

    else:
        rob "We can talk later if you want- you also look pretty busy."
        "You give her a nod."
        d "(I have to be early for a course. I should hurry up.)"
        stop music fadeout 2.0
        scene black with Dissolve(2)
        jump schoolch3

label namigym:
    $ play_playlist(playlist_Gymch3)
    scene black with Dissolve(2)
    show text "You and Nami head to the gym together." with dissolve
    with Pause(2)
    $ RCNKED = True
    scene m894 with Dissolve(2)
    n "So... Let's pump some iron!"
    d "Should we train together or everyone does their own stuff?"
    scene m895 with dissolve
    n "What's the point of going together if we don't train together?"
    scene m896 with dissolve
    d "By the way, how was it with Jeff?"
    scene m897 with dissolve
    n "He..."
    n "Made me cry."
    d "What?"
    scene m898 with dissolve
    n "He always said 'just 2 more'... over and over again..."
    n "And after those two... two more!"
    if fitness == 2:
        d "Oh, I've been there.."
    scene m899 with dissolve
    n "But it made me stronger!"
    scene m900 with vpunch
    n "ARGH!"
    scene m901 with dissolve
    "Everyone currently in the gym directs their attention towards Nami."
    scene m902 with dissolve
    d "You done?"
    scene m903 with dissolve
    n "I am just getting started!"
    scene m904 with dissolve
    rob "Umm, Hi."
    scene m905 with dissolve
    d "Hi?"
    scene m906 with dissolve
    rob "We have the same course."
    rob "I didn't catch your name last time."
    d "[name]."
    rob "You look different."
    d "Long story."
    scene m907 with dissolve
    rob "Hello, I am Robin!"
    n "I am Nami! Nice to meet you!"
    scene m908 with dissolve
    rob "You two are a cute couple."
    scene m909 with dissolve
    d "We are just friends."
    rob "Oh, I am sorry."
    rob "I just wanted to say hi and welcome you two properly."
    scene m910 with Dissolve(2)
    n "Dude. how many of them are you banging?"
    d "I don't even know them.."
    d "Did you get some new classmates, too?"
    scene m912 with dissolve
    n "Yes."
    d "How are they?"
    n "Pretty cool."
    n "And... there is this one weird girl."
    n "Her name is Nia."
    scene m913 with dissolve
    d "Oh god."
    n "You know her?"
    d "We've met..."
    n "I hope you like her."
    scene m914 with dissolve
    d "Why?"
    n "Because I invited her to the gym."
    scene m915 with dissolve
    d "*sigh* Why!?"
    scene m916 with dissolve
    n "I- wanted you two to meet."
    scene m917 with dissolve
    d "Why?"
    scene m918 with dissolve
    n "She's weird... I like weird people."
    scene m919 with dissolve
    n "And... *whisper* Don't tell anybody... She's a camgirl."
    d "What is that?"
    scene m920 with dissolve
    n "Oh god..."
    n "She sits in front of her cam and makes sex shows."
    d "How do you know that?"
    scene m919 with dissolve
    n "I saw one of her videos once, and I instantly remembered her."
    scene m918 with dissolve
    d "You sure you aren't lesbian?"
    scene m919 with dissolve
    n "She did it with a dude in the video."
    scene m921 with dissolve
    n "But lately she's only streaming solo."
    d "Mh. There she is."
    scene m922 with dissolve
    nia "Hellllooo!"
    nia "Thanks for inviting me!"
    scene m923 with dissolve
    n "Sure!"
    scene m922 with dissolve
    nia "I was gaining a little weight here and there.."
    scene m924 with dissolve
    nia "*whisper* I can't have that if you know what I mean."
    scene m925 with vpunch
    nia "*gasp*!"
    nia "No! What happened to my sweet emo boy!? Who did this to you!?"
    "You ignore her."
    scene m927 with dissolve
    nia "You don't talk much, mh?"
    d "I prefer to only speak when necessary... or when I am in good company."
    scene m926 with dissolve
    nia "You are mean."
    scene m928 with dissolve
    n "Yes, [name] get it together."
    scene m929 with dissolve
    nia "What will you focus on, Nami?"
    n "My butt. It needs some work."
    nia "I see, I see!"
    scene m930 with dissolve
    nia "You have a great foundation."
    n "Aah-ha Thanks!"
    scene m931 with dissolve
    nia "And what will you focus on?"
    d "Something."
    scene m932 with dissolve
    nia "...Cool."
    nia "I will warm up with some squats."
    n "Sure!"
    scene m934 with vpunch
    "Nami drags you a few feet away."
    scene m933 with dissolve
    n "What's the matter with you?"
    scene m934 with dissolve
    d "Did you have to invite her?!"
    scene m935 with dissolve
    n "Yes!"
    n "Why are you so hostile to her?!"
    scene m936 with dissolve
    d "She is annoying... Her existence annoys me."
    scene m935 with dissolve
    n "She didn't even do anything to you!"
    scene m937 with dissolve
    d "Fuck off, Nami."
    d "You sometimes really piss me off!"
    n "What the hell is wrong with you?!"
    scene m938 with dissolve
    d "Sorry."
    d "I don't know what it is about her... Maybe the fact that she went to Tropic High school... I can't say."
    d "But whenever I see her I get mad for some reason."
    "Nami shakes her head."
    scene m939 with dissolve
    nia "Hey umm... I think I will skip the gym today... I don't feel like it."
    n "Nia? Because of [name]?"
    scene m940 with dissolve
    nia "I'll see you, okay?"
    scene m935 with vpunch
    n "Are you happy now?!"
    scene m936 with dissolve
    d "What?"
    scene m935 with dissolve
    n "She left!"
    scene m936 with dissolve
    d "Why would it bother her?"
    scene m935 with dissolve
    n "Sometimes I think you got the social intelligence of a fly!"
    n "I hate it when people treat others bad for no good reason!"
    scene m936 with dissolve
    d "Sorry."
    scene m933 with dissolve
    n "Sorry is not going to cut it."
    scene m934 with dissolve
    d "...*sigh* Where is she?"
    scene m933 with dissolve
    n "In the locker room, I guess."
    scene m934 with dissolve
    d "I will apologize."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Chapter1b)
    scene m976 with Dissolve(1.5)
    pause
    scene m977 with dissolve
    n "Nia?"
    scene m978 with dissolve
    nia "Yes?"
    scene m979 with dissolve
    n "Hey."
    n "You might want to wear something first."
    scene m980 with dissolve
    nia "Say what you got to say."
    scene m981 with dissolve
    d "I'm here to apologize to you."
    d "You didn't do anything to be treated like that."
    d "Even though your first impres-"
    scene m982 with dissolve
    nia "Yeah... It's okay."
    nia "I have been overthinking my first impression of you ever since we first met in the classroom."
    nia "And what I said and- well it made me cringe... Oh god... I choked myself."
    d "I remember."
    nia "I was super nervous, and when I am nervous, I tend to do weird stuff."
    scene m984 with dissolve
    nia "And thanks to this... I'm used to being avoided.."
    nia "But it doesn't hurt less when someone looks at me with contempt."
    scene m985 with dissolve
    n "Ohhh!"
    nia "Ohh- Nami, I am wet."
    scene m986 with dissolve
    n "I don't care!"
    d "Would you get out of the shower and train with us?"
    scene m987 with dissolve
    nia "...Yes."
    d "We will wait outside."
    nia "And... thanks for apologizing."
    $ persistent.unlockedImageNia1 = True
    scene m988 with dissolve
    pause
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(0.5)
    $ play_playlist(playlist_Ch1CollegeBella)
    scene m941 with Dissolve(2)
    pause
    scene m942 with dissolve
    pause
    scene m941 with dissolve
    pause
    scene m942 with dissolve
    pause
    scene m943 with dissolve
    nia "F-feels good!"
    scene m945 with Dissolve(2)
    pause
    scene m947 with dissolve
    pause
    scene m944 with dissolve
    pause
    scene m948 with dissolve
    pause
    scene m949 with dissolve
    pause
    scene m950 with dissolve
    pause
    scene m951 with dissolve
    nia "Hey... You won't skip leg day, will you?"
    scene m952 with dissolve
    d "I won't. It's an essential part of the body."
    scene m951 with dissolve
    nia "It's not so obvious. I know a lot of guys that only train chest and arms."
    scene m952 with dissolve
    d "I want to play in our tournaments. Everything needs to be in shape."
    scene m951 with dissolve
    nia "Oh right, I wonder if I should also play."
    scene m952 with dissolve
    d "That's up to you."
    scene m953 with dissolve
    nia "I don't want to get any bruises."
    scene m954 with dissolve
    d "Because of the cam show?"
    nia "Oh. You- umm saw my shows?"
    d "No, Nami told me about it."
    scene m955 with dissolve
    nia "Good- Puuuh, meeting someone who has watched me do certain things, would be pretty embarrassing."
    d "Nami saw them."
    scene m956 with dissolve
    nia "Yes but Nami is a girl."
    nia "I see guys a little differently."
    scene m951 with dissolve
    nia "I am going to add more weights."
    nia "Would you mind spotting me?"
    menu:
        "I will spot you.":
            $ niap +=1
            $ nami +=1
            scene m1018 with dissolve
            nia "You have to get a little closer and put your arms somewhat under mine."
            nia "And don't grab my boobs... or do."
            scene m1020 with dissolve
            "They giggle."
            d "Shut up, Cheeto-head."
            scene m1022 with dissolve
            nia "Hey! I'm a Cheeto-head, too!"
            d "Come on, we don't have that much time."
            scene m1021 with dissolve
            pause
            scene m1025 with dissolve
            nia "L-ast one!"
            d "Two more."
            scene m1023 with dissolve
            nia "Nghh!"
            scene m1025 with dissolve
            nia "Nghhhh-"
            scene m1024 with dissolve
            nia "Nnnnnhhi!"
            scene m1026 with dissolve
            nia "Ahhhh- my legs!"
            scene m1027 with dissolve
            n "Now spot me, [name]!"
            menu:
                "Fine.":
                    $ NamiSymlvl +=1
                    $ nami +=1
                    scene m1029 with dissolve
                    pause
                    scene m1030 with dissolve
                    pause
                    scene m1033 with dissolve
                    d "What?"
                    scene m1032 with dissolve
                    nia "You two have a sweet symbiosis."
                    nia "When you spotted me we were kinda out of rhythm."
                    nia "But you and Nami are in perfect balance with each other."
                    nia "As if you knew exactly how her body works."
                    scene m1034 with dissolve
                    d "Last one."
                    scene m957 with dissolve
                    n "Fuck."
                    n "I don't know if a good booty is worth this pain!"
                    nia "And you won't find out until you get one."
                "I think you will be fine.":
                    scene m1028 with dissolve
                    n "Tzz?"
        "I am not experienced enough.":
            nia "It's okay."
    scene black with Dissolve(2)
    with Pause(.5)
    scene m958 with Dissolve(2)
    nia "He has such a determined look."
    scene m959 with dissolve
    n "I was thinking the exact same thing."
    scene m960 with dissolve
    nia "Is he dating anyone at the moment?"
    if bellameet and BTY is True:
        n "This Bella."
        d "Arh- I- am not dating her!"
        scene m958 with dissolve
        nia "Who is that?"
        scene m960 with dissolve
        n "Blond-"
        scene m961 with dissolve
        nia "Oh! I think I saw her in class, yesterday."
        nia "When our eyes met it felt like she was staring into my soul."
        nia "My poor depraved and perverted little soul."
        scene m962 with dissolve
        nia "And now that you mention it. She did look a little jealous."
        n "She is a bitch. Don't worry about her."
        scene m961 with dissolve
        nia "I could tell."
        scene m963 with dissolve
        d "She is not that bad."
        scene m964 with dissolve
        nia "Yeaaaah, but we are not the ones trying to sleep with her."
        scene m965 with dissolve
        n "I am sure he is not trying to sleep with her."
        nia "Your voice suddenly turned a little hostile there."
        scene m966 with dissolve
        n "Sorry."
        nia "It's okay."
        nia "As his friend you're looking out for him."
        nia "And if I had a best friend, I wouldn't want them sleeping with people I don't like either."
        scene m969 with dissolve
        n "See? We understand each other."
    else:
        n "No, he isn't."
        scene m969 with dissolve
        n "Except his right hand... Ha-ha-ha."
        d "Argh- Can you fuck off?"
        scene m971 with dissolve
        n "Oh, right you don't do 'that'."
        scene m967 with dissolve
        nia "What?"
        scene m968 with dissolve
        n "Uhm- forget I said that... Damn! Me and my stupid mouth."
        scene m967 with dissolve
        nia "You really don't do it yourself?"
        "You ignore them and focus on the squats."
        scene m968 with dissolve
        n "It's complicated."
        scene m961 with dissolve
        nia "I see, I won't be digging anymore and I obviously won't tell anyone."
        scene m969 with dissolve
        nia "But it's pretty cute!"
        n "Right?!"
        "Nami and Nia start giggling."
    scene m970 with dissolve
    n "And you know, Nia.., [name] might act like a hard ass motherfucker... But he really is a gentle soul deep inside."
    n "But in private he massages me, cuddles with me and brings me my food."
    nia "Oh really?"
    scene m971 with dissolve
    n "Na, that's just wishful thinking."
    scene m972 with dissolve
    "They both start giggling again."
    scene m974 with dissolve
    d "*Fast breathing* Nami. We need to eat more... At least I do."
    d "I feel weak today."
    d "Let's buy a blender and make some mass shakes."
    scene m973 with dissolve
    n "Good idea."
    n "Damn it, we should have talked less and trained more.."
    scene m975 with dissolve
    n "I have to be in class in 20 minutes."
    stop music fadeout 2.0
    scene black with Dissolve(3)
    with Pause(.5)
    $ play_playlist(playlist_AmbientNamiLake)
    scene ss1 with dssb
    nia "[name], do you want to walk together to class?"
    scene ss2 with dssa
    d "Yeah, why not."
    scene ss1 with dssa
    nia "I wonder what adventures will await us in history class."
    scene ss3 with dssa
    d "History? I don't have history class."
    d "I have math."
    scene ss4 with dssa
    nia "Oh."
    nia "Then forget about going to class together."
    scene ss3 with dssa
    n "Who else is in the math class?"
    d "I have no idea."
    scene ss5 with dssr
    nia "Nami?"
    n "...Yes?"
    scene ss6 with dssa
    "Nia peeks outside to see if the air is clean."
    scene ss7 with dssr
    "She runs out of the shower."
    scene ss8 with vpunch
    n "Yo!?"
    scene ss9 with dssa
    pause
    scene ss10 with dssa
    nia "What do you think?"
    scene ss11 with dssa
    n "Man! That's awesome!"
    scene ss12 with dssa
    n "How did you trim it like that?"
    scene ss13 with dssa
    nia "Thanks!"
    nia "I got a precision hair trimmer, and it took me forever to make it look like this.."
    scene ss15 with dssa
    n "But damn! Worth it!"
    scene ss16 with dssa
    n "Well, as long as you have someoen to admire it."
    scene ss14 with dssa
    nia "You should trim your pubi."
    scene ss17 with dssa
    n "Someday... At the moment nobody is seeing me naked anyway..."
    scene ss18 with dssa
    n "...Except for you."
    scene ss19 with dssr
    n "All that creativity would go to waste."
    scene ss21 with dssa
    nia "What if you find a cute guy?"
    scene ss20 with dssa
    n "I have no interest in... anything too fast."
    scene ss21 with dssa
    nia "Understandable."
    nia "You're missing out on some potentially great stuff, though."
    scene ss22 with dssr
    n "I'm just waiting for someone that is worth trimming my pubis for."
    scene ss23 with dssa
    nia "Let me tell you something, Nami."
    nia "In the past, I was in a very dark place... I Pretty much lost myself."
    nia "Until I got proactive."
    scene ss24 with dssa
    nia "Real life is not a movie. There is no happy end waiting for us. No significant other that is certainly going to cross our way."
    nia "Do you think the people who die alone planned on doing so? No, every day they woke up, they expected that someday, their life would take a turn and they would end up happy."
    nia "And so years passed until they realized that time was up."
    scene ss25 with dssa
    nia "You either get proactive or you're about to miss out on a lot of stuff."
    nia "I wasted my childhood. I had no friends... because for some reason, I lack the ability to read a room and- I tend to behave inappropriately in a social setting."
    nia "Especially when I am nervous... I mean [name] saw it yesterday... I chocked myself in front of him... And I am sure I am going to lose sleep about it for years to come."
    scene ss26 with dssr
    nia "I always waited and waited for people to talk to me and then I turned seventeen and... I saw there was a reason no one ever came to my birthdays."
    scene ss28 with dssa
    nia "Becoming proactive was the best decision I ever made. The day I turned eighteen, I started a business on my strengths... My body."
    nia "I became more confident and that made it so much easier to form connection... If you accept yourself, other are more likely to do so, too."
    nia "I'm already blabbering too much."
    scene ss29 with dssr
    "Nami pauses for a brief moment."
    scene ss30 with dssa
    n "Make sure to invite [name] and me to your next birthday party."
    n "And don't blame yourself for just being yourself..."
    scene ss31 with dssr
    nia "Will do! And... Also yes to the other one. I don't blame myself anymore."
    nia "All I am saying is... Be proactive."
    scene ss32 with dssa
    nia "Or you might miss out on the one you are so desperately looking for."
    scene black with Dissolve(2)
    with Pause(.5)
    scene m1014 with dssb
    pause
    scene m1015 with dissolve
    nia "Nami?"
    n "Yes?"
    nia "I have a question."
    n "Sure, go ahead."
    scene m1016 with dissolve
    nia "It's about [name]-"
    scene m1017 with dissolve
    nia "-and Summer."
    $ NaNiProTalk = True
    $ NaNiSuTalk = True
    stop music fadeout 2.0
    $ achievement.grant("PumpingCheeto")
    $ achievement.sync()
    scene black with Dissolve(2)
    jump schoolch3






label bellagym:
    $ play_playlist(playlist_Gymch3)
    scene black with Dissolve(2)
    show text "You head to the gym to meet up with Bella." with dissolve
    with Pause(3)
    scene m641 with Dissolve(2)
    pause
    scene m642 with dissolve
    d "Hey."
    scene m643 with dissolve
    b "Hi."
    if bellasafe is True:
        $ bella +=1
        scene m644 with dissolve
        b "I hope I won't have to save your life again."
        d "That was one time..."
        scene m645 with dissolve
        b "Haha."
    scene m646 with dissolve
    d "So... you're pretty advanced, right?"
    scene m647 with dissolve
    b "Take a look at me."
    scene m648 with dissolve
    d "You look like a cripple."
    scene m649 with dissolve
    pause
    if fitness ==1:
        scene m650 with dissolve
        b "You trained with Jeffrey once?"
        d "Yes."
        scene m651 with dissolve
        b "Let me show you how a real workout looks like."
    else:
        scene m650 with dissolve
        b "It's about time you take some care of that thing you call your body."
        scene m651 with dissolve
    b "Let's do some cardio first."
    scene m652 with dissolve
    d "For how long?"
    b "15 minutes."
    scene m655 with dissolve
    pause
    scene m654 with dissolve
    b "How did they take your new hairstyle?"
    scene m653 with dissolve
    d "You mean Nami and Nojiko?"
    d "They liked it... At least Nojiko did."
    scene m657 with dissolve
    b "I bet the redhead just didn't like it because I was the one who made it happen."
    scene m656 with dissolve
    d "This is a stupid mindset in general. In today's world, it often only matters who said something and not what has been said."
    d "If the 'wrong' person says something important, the people won't listen."
    scene m658 with dissolve
    b "These are the kind of people that would sacrifice their own success just to hurt their rivals."
    b "Instead of just moving on and- focusing on themselves."
    scene m659 with dissolve
    d "And I am pretty sure you are like that."
    scene m655 with dissolve
    b "Hmm... A little maybe."
    scene m654 with dissolve
    b "But I am not the only one here who is like this."
    d "Why did you humiliate Nami on the first day?"
    scene m655 with dissolve
    b "I gave her a life lesson."
    d "An unnecessary one."
    scene m661 with dissolve
    b "Definitely, but I had fun."
    scene m662 with dissolve
    d "You will still pay for that."
    scene m663 with dissolve
    b "Will you help Nami with her revenge?"
    menu:
        "Yes.":
            $ bellalove +=1
            scene m667 with Dissolve(2)
            b "That's what I expected."
            b "They help each other, they stay by each other's side no matter what happens. They just... have each other's back."
            scene m668 with dissolve
            d "I assume you're not ready to tell me about your sibling."
            b "No."
            b "And I probably never will."
            d "We both know that the time will come when you'll tell me about her."
            scene m669 with dissolve
            b "You act like our lives are intertwined."
            "You say nothing."
            scene m658 with dissolve
            b "And I hate that I have the same feeling."
            b "I can't explain it otherwise."
            b "Why would I interact with you- on such a personal level... after just a few days?"
            if bellasummer is True:
                $ bellalove +=1
                scene m659 with dissolve
                d "It's the same reason why I told you about Summer."
                d "I never tell that to anyone."
                scene m657 with dissolve
                b "What is the reason?"
                d "It was a risk I was willing to take. A feeling that led me to it."
                scene m665 with dissolve
                b "How can you even trust me?"
                d "I don't trust you fully, obviously."
                scene m664 with dissolve
                d "But- you are a bitch. A really arrogant bitch."
                d "But you're not two-faced... You're not a liar."
                scene m663 with dissolve
                b "I lied to Nami."
                scene m670 with dissolve
                d "Yeah, but it was for a prank."
                d "What we are doing... What we are planning to do... You wouldn't do that with someone that might betray you."
                d "Even if we'll never acknowledge this. There is a bond of trust between us that formed naturally. It's a feeling."
                scene m672 with dissolve
                b "We have the same goal- and I think we kinda experienced the same tragedy."
                scene m671 with dissolve
                "You say nothing and stare out the window while you increase the bike speed."
                scene m669 with dissolve
                b "-We both got lost somehow."
                scene m673 with dissolve
                "You both proceed to do the cardio in silence."
        "I am not interfering in Nami's business.":
            $ bella -=1
            scene m667 with Dissolve(2)
            b "I wonder what she'll come up with."
            d "Prepare yourself."
            d "She has a very creative mind."
            scene m669 with Dissolve(2)
            b "I can't wait."
            scene m673 with dissolve
            "You both proceed to do the cardio in silence."
    with Pause(0.5)
    scene m674 with Dissolve(2)
    pause
    scene m676 with dissolve
    b "Come."
    scene m677 with dissolve
    b "Have you ever used this?"
    scene m678 with dissolve
    d "No, I haven't. I used to do squats only."
    scene m679 with dissolve
    b "It's called a leg press."
    b "And pay attention. You will see some nut bags do this."
    scene m680 with dissolve
    b "See how stretched my legs are?"
    b "I am currently resting the weight on my joints. Which as you can imagine, is not good."
    d "I think I saw some videos of the leg suddenly breaking and going sideways."
    scene m681 with dissolve
    b "Especially if you have such chicken legs."
    scene m682 with dissolve
    b "Never rest weight on your joints and always have some tension in your muscle."
    scene m684 with dissolve
    b "Don't stretch the leg out too much and if you do, make sure your muscles are under tension."
    b "Sit."
    d "Nhh-"
    scene m688 with dissolve
    b "You must feel it here.."
    d "I- Nrrrh-"
    b "Don't talk while you train."
    b "Just... concentrate on your body."
    scene m688 with dissolve
    b "Feel the pain from excessive muscle exertion."
    b "As it grows stronger and stronger... Your strength, slowly leaving you..."
    scene m689 with dissolve
    "Bella suddenly directs her attention towards the entrance."
    scene m690 with dissolve
    pause
    scene m691 with dissolve
    pause
    scene m693 with vpunch
    d "Nhh- What are you doing?!"
    b "Just keep going."
    scene m695 with dissolve
    d "Get of-"
    b "*whisper* I said keep going."
    scene m694 with dissolve
    pause
    scene m696 with dissolve
    b "Just a few more..."
    d "*Strong breathing* I can't d-o it like this!"
    scene m697 with dissolve
    d "Why *breathing* Why did you sit on me you cripple?!"
    scene m698 with dissolve
    b "Because I do what I want."
    scene m699 with vpunch
    rob "Hi."
    d "Hi? Do I know you?"
    scene m700 with dissolve
    rob "We're in the same course."
    rob "I didn't catch your name last time."
    d "[name]."
    rob "You look different."
    d "Long story."
    scene m701 with dissolve
    b "Hi Robin."
    rob "Hey Bella, long time no see."
    scene m702 with dissolve
    d "(For some reason I feel like... never mind.)"
    b "I've been busy."
    scene m704 with dissolve
    rob "Yeah, I thought as much."
    rob "I did try to contact you a few times."
    b "I didn't know that."
    scene m705 with dissolve
    rob "Well... Anyways, take care you two."
    if bellameet is True:
        scene m706 with dissolve
        d "The Robin from elementary school?"
        b "Mhm."
        d "I don't believe you didn't know that she tried to contact you."
        scene m707 with dissolve
        b "I lied."
        b "I am not interested in being her friend. But I also don't want to hurt her feelings."
        d "She seems nice."
        scene m708 with dissolve
        b "Am I nice?"
        d "No."
        b "Exactly. We have no common ground."
        d "Ayua seems to be nice and you're friends with her."
        scene m709 with dissolve
        b "Because we have common ground."
        d "What common ground?"
        $ Brace = True
        b "Racing."
        scene m710 with dissolve
        d "Racing. Wait... Now I know where I've seen those cars."
        d "You're one of those street racers?"
        b "Yup."
        d "Ayua, too?"
        b "Yes."
        scene m711 with dissolve
        d "You're reckless sons of bitches."
        scene m712 with dissolve
        b "Shut up. We make sure no one innocent gets hurt."
        d "...Are you at least good?"
        scene m713 with dissolve
        b "I'm in the top three when it comes to drag racing."
        b "And Ayua holds second place in drifting."
        b "Overall, I'm at place six in the Blacklist and Ayua is at 5th."
        scene m711 with dissolve
        d "I've heard of a few fatalities."
        scene m712 with dissolve
        b "Of course. If you hit a wall at 130 mph, then that's pretty much it."
        scene m713 with dissolve
        b "But the risk of dying makes it even more exciting. Every race can be the last."
        scene m711 with dissolve
        d "What do we train next?"
        b "Abs."
        scene m715 with Dissolve(2)
        b "If you want... I can take you with me sometime."
        scene m716 with dissolve
        d "To a race?"
        "She nods."
        d "...I'll think about it."
        scene m717 with dissolve
        d "(She invited me to an illegal street race.)"
        d "(There is no denying it anymore... She does like me.)"
        scene m718 with dissolve
        if MCBL ==1:
            d "(And I am afraid I'm starting to like her, too..)"
            pause
        else:
            pause
    scene m719 with dissolve
    b "I am going to do three sets first. Then you do three."
    d "Alright."
    d "(Mila is here- Should I say hi?)"
    menu:
        "Go and say hi to her.":
            $ milatalk = True
            $ TalkWithMilaGym = True
            d "Do your sets and I'll say hi to Mila."
            scene m720 with dissolve
            "Bella rolls her eyes."
            scene m721 with dissolve
            pause
            scene m722 with dissolve
            d "Hey."
            mi "Hey."
            d "Everything alright?"
            scene m723 with dissolve
            mi "Yes."
            if bellameet is True:
                scene m724 with dissolve
                mi "Except for the police stuff."
                d "Yeah."
                mi "But please let's not talk about it."
            scene m726 with dissolve
            "Mila takes a second."
            scene m725 with dissolve
            mi "It seems as if you and Bella are very close now."
            scene m726 with dissolve
            d "Not really."
            scene m726 with dissolve
            mi "Are you sure? She was sitting on your lap."
            scene m727 with dissolve
            d "(...That's why she sat on me. She must've seen Mila and wanted to mark her territory.)"
            d "(I should have expected internal clashes between some of the girls.)"
            d "(I need to be careful with what I do in the future. Especially when it involves an aggressive girl like Bella, who actively fights potential rivals.)"
            d "Don't read too much into that."
            if miladate is True:
                scene m728 with dissolve
                mi "Are you sure you want to go on a serious date with me?"
                d "Mila-"
                mi "I'm just saying [name]. I won't be mad. I just don't like being the third wheel."
                menu:
                    "Change the date into a friendly one.":
                        $ miladateF = True
                        scene m729 with dissolve
                        d "...I guess it's better to start off with a friendly date then."
                        scene m728 with dissolve
                        mi "As you wish."
                        mi "I think it's for the better."
                    "Keep it a serious date.":
                        scene m730 with dissolve
                        d "No, I want to keep it serious."
                        scene m731 with dissolve
                        mi "I'm glad to hear that."
                d "I need to keep training, I'll see you later."
                scene m732 with dissolve
                mi "Sure, take care!"
            else:
                scene m728 with dissolve
                mi "Well, you're free to do what you want."
                scene m729 with dissolve
                d "I know."
                d "Well, I should head back."
                mi "Yea, I'll see you later."
        "Don't.":
            scene black with Dissolve(2)
            with Pause(.5)
    scene m733 with dissolve
    d "So... Are you done?"
    b "Nrgh!"
    b "One more set."
    scene m734 with dissolve
    b "Ohh fuck yeah.."
    scene m735 with Dissolve(2)
    if TalkWithMilaGym is True:
        b "Did you two discuss your non-existent finances?"
        b "I might know a good bookie for you both..."
        scene m736 with dissolve
        d "Do you always have to make fun of her?"
        scene m735 with dissolve
        b "Yes, it's her own fault."
        menu:
            "Stop it.":
                scene m737 with dissolve
                b "Why?"
                d "Because I say so."
                scene m738 with dissolve
                b "*Sigh* Fucking poor people... I'll see what I can do."
                $ MBFAC = True
            "Don't tell her to stop it.":
                $ MBFAC = False
                pass
    scene m739 with dissolve
    b "Last set."
    scene m740 with dissolve
    b "Mhh-"
    scene m741 with dissolve
    if MCBL ==1:
        d "(Her moaning sounds kinda sweet.)"
    b "Mhhi-"
    scene m740 with dissolve
    with Pause(0.5)
    b "Ahh- Damn..."
    scene m743 with Dissolve(1.5)
    b "Now you."
    scene m744 with dissolve
    d "Mhh-"
    scene m745 with dissolve
    d "Nh-"
    scene m746 with dissolve
    b "Don't lift your whole body."
    scene m745 with dissolve
    pause
    scene m747 with dissolve
    b "I said not your whole body!"
    scene m745 with dissolve
    pause
    scene m747 with dissolve
    b "Keep the lower end on the floor you cripple!"
    d "I can't! It moves automatically."
    scene m748 with vpunch
    d "Nh- really?"
    scene m749 with dissolve
    b "Try it now."
    scene m761 with dissolve
    d "Nh-"
    d "...Now it's much harder."
    b "You're doing it without momentum now."
    scene m762 with dissolve
    d "Nhh-"
    if MCBL == 1:
        d "(That scent again...)"
        d "(Why does she affect me so much... Fucking pheromones.)"
        scene m750 with dissolve
        pause
    else:
        scene m750 with dissolve
        pause
    d "Ar-h"
    scene m751 with dissolve
    b "Come on."
    b "Always go a little beyond your limit."
    b "Feel the pain... Embrace it."
    b "The next time your muscles will be ready for it."
    scene m750 with dissolve
    b "Stay like this... Feel the contractions. The way your body is shaking... Your mind grasping for that sweet relief..."
    scene m751 with dissolve
    b "And back."
    d "Yo- *breathing* can go down now."
    scene m764 with dissolve
    b "I'm good."
    scene m765 with dissolve
    b "You got a boner?"
    d "No."
    scene m758 with dissolve
    b "...You got a medical condition?"
    scene m760 with dissolve
    d "No."
    d "Now stand up."
    scene m758 with dissolve
    b "You still need to do 2 sets."
    d "Then at least move down a little. Your breasts are literally in my face."
    scene m770 with dissolve
    b "I was testing you, you know."
    d "*Sigh* Why?"
    b "Yesterday I wore leggings that were way too tight."
    scene m770 with dissolve
    b "You didn't say anything about it."
    d "It shouldn't surprise you at this point."
    scene m772 with dissolve
    b "And that's why I grabbed this top."
    b "Just to see if it was an act that you were playing very well."
    b "But you really don't care, do you?"
    d "Why would I care about it? Do I like breasts? Of course I do. But-"
    scene m773 with dissolve
    b "Man, this Summer thing really fucked you up."
    b "I really hope that my mom will get to the core of your problem."
    scene m774 with dissolve
    d "Why would you hope that? Do you want me to acknowledge your- assets?"
    scene m775 with dissolve
    b "Dude, it's weird if you don't even take a little peek."
    b "Even the biggest gay would take a look and raise his brow while shaking his head."
    scene m776 with dissolve
    b "You come across like a machine. You're unpredictable and that's scary."
    b "I'm not even sure if you got a penis."
    b "It could be some sort of catheter tube."
    scene m777 with dissolve
    if UmB is True:
        d "You saw him yesterday."
        scene m778 with dissolve
        b "It could be some terminator-life-like infiltrator catheter."
    else:
        d "You are-"
        scene m778 with dissolve
        b "It's probably some terminator-life-like infiltrator catheter."
    scene m777 with dissolve
    "You just look at her with one brow raised."
    scene m779 with dissolve
    b "I talk too much."
    d "Way too much."
    scene m780 with dissolve
    b "Dude. You got your hand on my hip."
    d "You're one to complain."
    d "You're the one who is still sitting on me."
    scene m777 with dissolve
    d "God, when did you get so unbelievably touchy?"
    scene m776 with dissolve
    b "You always react very confused to physical contact."
    b "It's the only time you actually act human and show some sort of insecurity."
    if UmB is True:
        scene m778 with dissolve
        b "And do you think I didn't notice how your behavior changed?"
        b "From 'Uuuuh- I'm a little bitch! Don't touch me!' to nothing."
        b "You just let it happen."
        d "I told you multiple times to get off of me."
        b "You're the type of guy that would push me away if you really wanted me to go."
        scene m781 with dissolve
        b "*Whisper* But you know... you found a liking to it."
        d "You're such a pain in the ass."
    scene m782 with dissolve
    b "Next set."
    scene m750 with dissolve
    pause
    scene m751 with dissolve
    pause
    scene m752 with dissolve
    pause
    scene m753 with dissolve
    pause
    scene m754 with dissolve
    pause
    scene m756 with dissolve
    pause
    scene m757 with dissolve
    "You stop mid-set while your eyes are glaring at each other."
    scene m753 with dissolve
    d "Stop this before you do something else you will regret."
    scene m783 with dissolve
    b "*sensual whisper* I don't regret."
    scene m784 with dissolve
    b "But we should really get going. I need to be early for a course."
    stop music fadeout 2.0
    scene black with Dissolve(2.5)
    with Pause(0.5)
    hide text with Dissolve(1.5)
    $ play_playlist(playlist_AmbientBellchen)
    scene m785 with Dissolve(2)
    rob "I didn't like the acting."
    scene m786 with dissolve
    $ persistent.unlockedImageSasha1 = True
    u "It was indeed defiant."
    scene m787 with dissolve
    b "What course do you have now?"
    d "Math, you?"
    b "Art."
    d "With Karen?"#mc
    b "Oh no... I totally forgot she has something to do with the art class."
    scene m789 with dssb
    b "How did your first session with my mom go?"
    scene m790 with dssa
    d "I can't say..."
    scene m791 with dssa
    b "It takes a while but... She knows what she's doing."
    scene m790 with dssa
    d "Mhm."
    scene m792 with dssr
    b "Don't be surprised if she takes you out to some weird places... Or uses some weird methods."
    scene m794 with dssa
    d "She mentioned something like that."
    d "And she gave me a little teddy."
    scene m795 with dssr
    b "...A little brown one?"
    scene m795x with dssa
    d "Yeah."
    scene m796 with vpunch
    b "What the hell?! That's her teddy!"
    scene m797 with dssa
    d "I know. She said that."
    scene m796 with dssa
    b "Why would she give it to you?!"
    scene m797 with dssa
    d "You sound shocked?"
    scene m797x with dssa
    b "Yes!?"
    b "She loves that teddy! She's had it since she was a little girl!"
    scene m798 with dssa
    d "She just said that she cannot expect me to let something go if she doesn't do it herself."
    d "And that when the time comes, I need to let the teddy move on."
    scene m798x with vpunch
    "With one swift motion, she draws your curtain to the side."
    scene m798y with dssa
    b "Give it to me! I'll store it in my room."
    scene m798x with dssa
    d "No, I'll take care of the teddy."
    scene m798z with dssa
    b "It doesn't belong to you!"
    scene m799x with dssa
    d "It does now. Nothing bad will happen to the teddy. I promise."
    scene m799y with dssa
    b "I'll hold you to that."
    scene black with Dissolve(2)
    with Pause(.5)
    scene m799 with dssr
    b "It was a nice training session."
    d "Yeah."
    scene m800 with dissolve
    b "I need to get going... I'll see you, I guess."
    "You nod."
    scene black with Dissolve(2)
    $ persistent.unlockedImageBella17 = True
    stop music fadeout 3.0
    show text "You head straight to your first course." with dissolve
    with Pause(3)
    hide text with dissolve
    $ achievement.grant("BellaGymA")
    $ achievement.sync()
    jump schoolch3

label milagym:
    $ play_playlist(playlist_Gymch3)
    scene black with Dissolve(2)
    show text "You head to the gym to meet up with Mila." with dissolve
    with Pause(3)
    scene ee2 with dssb
    pause
    scene ee1 with dssb
    mi "Hey there."
    scene ee4 with dssr
    d "Hey."
    scene ee5 with dssa
    mi "Thanks for the invite."
    scene ee6 with dssa
    d "Sure."
    scene ee5 with dssa
    mi "So, what are we going to train today?"
    scene ee6 with dssa
    d "What do you usually train?"
    scene ee7 with dssa
    mi "I don't know if you noticed, but I have big boobs. So, naturally, I do a lot of back workouts."
    scene ee8 with dssr
    mi "I don't want to end up with chronic backpain."
    scene ee9 with dssa
    d "Makes sense."
    d "Let's start with legs and then do back?"
    scene ee10 with dssa
    mi "Sounds like a plan."
    scene ee11 with vpunch #sfx
    pause
    scene ee12 with dssa
    pause
    scene ee13 with dssa
    mi "Do you mind me asking why you have that wound?"
    scene ee14 with dssa
    d "I got into a little dispute."
    scene ee15 with dssa
    mi "With whom?"
    scene ee14 with dssa
    d "Is that important?"
    scene ee15 with dssa
    mi "It is."
    scene ee14 with dssa
    d "You will find out soon enough... but it is what it is."
    scene ee16 with dssa
    mi "You can talk-"
    scene ee17 with dssa
    d "Mila, please..."
    scene ee18 with dssa
    mi "Alright! Alright!"
    scene ee19 with dssr
    mi "But if you'll get hurt again..."
    scene ee20 with dssa
    d "Yeah, yeah..."
    scene ee21 with dssa
    mi "I'll start, okay?"
    scene ee20 with dssa
    d "Yeah, I still struggle with my squat mobility."
    scene ee22 with dssr
    with Pause(.5)
    scene ee23 with dssa
    with Pause(.5)
    scene ee22 with dssa
    with Pause(.5)
    scene ee23 with dssa
    with Pause(.5)
    scene ee31 with vpunch
    "She slaps on another 20KG plate on both sides."
    scene ee32 with dssa
    mi "Warm up is important."
    scene ee24 with dssr
    pause
    scene ee27 with dssa
    pause
    scene ee24 with dssa
    pause
    scene ee28 with dssa
    pause
    scene ee33 with vpunch
    "She adds another 10KG plate on both sides."
    scene ee25 with dssr
    mi "*Moans* Oh- damn it."
    scene ee29 with dssa
    pause
    scene ee25 with dssa
    pause
    scene ee29 with dssa
    pause
    scene ee26 with dssa
    mi "NGH!"
    scene ee30 with dssa
    pause
    scene ee34 with vpunch
    "She hangs the bar back in."
    scene ee35 with vpunch
    "She drops to the floor. Exhausted and breathing hard."
    scene ee37 with dssa
    d "You're in pretty good shape, and much stronger than I expected."
    scene ee39 with dssr
    mi "Thanks!"
    mi "Did you think my legs and butt were just for show?"
    scene ee38 with dssa
    d "Kinda."
    d "Now you only need to get over your fear of balls, and you will be a great asset to a sports team."
    scene ee40 with dssa
    mi "Yeah, I don't think that's going to happen anytime soon."
    mi "I black out when something gets thrown or shot my way. Kind of a... bad habit."
    scene ee36 with dssa
    d "And I guess you are not much of a fighter, either."
    scene ee40 with dssa
    mi "Not at all."
    mi "I think I'm useless when it comes to ball sports."
    scene ee41 with dssa
    mi "I just want to feel good... and that goes hand in hand with looking good."
    mi "I also kind of like the pain from a workout."
    scene ee42 with dssa
    mi "Your turn."
    scene ee43 with dssr
    pause
    scene ee44 with dssa
    pause
    scene ee45 with dssr
    mi "Don't go too far down if you still lack the mobility, though."
    scene ee46 with dssa
    d "Nrrh.."
    scene ee47 with dssa
    d "*breathing heavily* Do- you have to stare at me while I do this?"
    scene ee48 with dssa
    "Mila smiles and turns around."
    scene ee50 with dssa
    pause
    scene ee49 with dssa
    pause
    scene ee51 with dssa
    mi "That was good. If you keep this up, you'll get the mobility."
    mi "Can you spot me? I'm not sure if I can get the full five reps."
    d "Sure."
    scene ee52 with dssr
    mi "Ready?"
    d "Yes."
    scene ee53 with dssr
    pause
    scene ee54 with dssa
    pause
    scene ee56 with dssa
    pause
    scene ee55 with vpunch
    pause
    scene ee57 with dssa
    mi "*Breathy* L-last one!"
    scene ee55 with vpunch
    mi "NRGH!"
    scene ee58 with dssr
    mi "Was this your first time spotting someone?"
    scene ee59 with dssa
    d "It's my second time in the gym. What do you think?"
    scene ee58 with dssa
    mi "You got pretty close to me."
    scene ee59 with dssa
    d "I'm sorry."
    scene ee58 with dssa
    mi "Don't worry! I don't mind. But in case I really can't get the weight back up, you might run into problems getting me back up."
    scene ee60 with dssr
    if miladate is True:
        mi "I- wouldn't go out with you if I minded being close to you."
        scene ee62 with vpunch
        d "Less talking, more training."
        scene ee63 with dssr
        mi "Oh no! A second Jeff!"
    else:
        mi "I'll give you a step by step spotting guide if we should go again."
        scene ee61 with dssa
        d "Appreciate it."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ee64 with dssr
    mi "How is working with Bella?"
    if BTY is True:
        scene ee65 with dssa
        d "It's okay."
        scene ee64 with dssa
        mi "You two get along?"
        scene ee65 with dssa
        d "Yeah, kinda."
        scene ee64 with dssa
        mi "How's that?"
        scene ee65 with dssa
        d "She and I are- kinda similar and we have the same goal."
        scene ee66 with dssa
        mi "The project, right?"
        d "No, a goal outside of college."
        scene ee67 with dssr
        mi "What is it?"
        d "Sorry, I can't tell you."
        mi "Please don't turn into another Bella.."
    else:
        scene ee65 with dssa
        d "A little annoying."
        d "But- we are working on something."
        scene ee66 with dssa
        mi "On what?"
        d "Sorry, I cannot tell you."
    scene ee69 with dssr
    d "Your pants ripped."
    scene ee70 with vpunch
    mi "What?!"
    scene ee71 with dssr
    mi "*Mumbles* Damn... I should've worn underwear."
    mi "Three pairs of leggings have now fallen victim to my butt... Damn it!"
    scene ee72 with dssa
    d "I think they will hold until the end of our training."
    scene ee73 with dssr
    mi "Let's hope so. If someone else comes by, I'll head to the locker room."
    scene ee74 with dssa
    mi "My butt is too strong for its own good."
    menu:
        "Compliment her butt.":
            $ milalove +=1
            $ MGP03 = True
            scene ee75 with dssr
            d "You really got a big butt."
            scene ee76 with dssa
            mi "Thank you?"
            scene ee77 with dssa
            d "It was meant as a compliment."
            scene ee78 with dssa
            mi "It's very hard to read you."
            mi "I'm glad you like a big butt, haha."
            scene ee79 with dssa
            mi "Means... You're an ass guy?"
            scene ee80 with dssa
            d "Mh?"
            scene ee79 with dssa
            mi "I mean, if you prefer butts over breasts?"
            scene ee81 with dssr
            menu:
                "Yea, I do prefer butts.":
                    $ MMCPB03 = True
                    scene ee168 with dssa
                    mi "At least, I have that going for me, huh?"
                    scene ee169 with dssr
                    "You give her a subtle smile."
                    scene ee170 with dssr
                    d "I think you've got both going for you."
                "To be honest, I do prefer breasts.":
                    $ MMCBB03 = True
                    scene ee123 with dssa
                    mi "Oh, I am surprised."
                    scene ee81 with dssa
                    d "How so?"
                    scene ee124 with dssa
                    mi "You never even looked at my cleavage once. And let's be honest... There is a lot."
                    d "Well-"
                    scene ee125 with dssr
                    mi "So I guess it's just not mine you want to see."
                    scene ee126 with dssr
                    d "To be honest, I don't want to see anyone's boobs."
                    d "Mila... Things are complicated."
                    scene ee127 with dssr
                    mi "All good, don't feel weirded out by the stuff I say."
                    scene ee128 with dssa
                    d "But yeah. Objectively, I like boobs."
                    mi "Good to know, Mr. Robot."
                "I like both equally.":
                    $ MFEQ = True
                    scene ee123 with dssa
                    mi "I see, I see."
                    mi "Mister I want it all."
                    scene ee128 with dssr
                    d "You got it. Miss I have it all."
        "Ignore it and train back.":
            scene ee128 with dssr
            d "Let's do back."
    scene ee129 with dssa
    with Pause(.4)
    scene ee128 with dssa
    with Pause(.4)
    scene ee129 with dssa
    scene black with Dissolve(2)
    with Pause(.5)
    $ MiVicInvite03 = True
    scene ee130 with dssb
    with Pause(.4)
    scene ee131 with dssa
    with Pause(.4)
    scene ee130 with dssa
    pause
    scene ee132 with dssr
    mi "I heard you're going to the movies with Victoria and Maja?"
    scene ee133 with dssa
    d "Am I?"
    scene ee132 with dssa
    mi "Oh, I thought they had already asked you. At least they wanted to."
    if majalove == 1:
        mi "Maja respects you, so she said."
    scene ee133 with dssa
    d "What do you think of Maja? I assume you've met her?"
    scene ee134 with dssa
    mi "Of- nh- course."
    mi "I like her. She really takes care of Victoria."
    scene ee133 with dssa
    mi "But it also worries me."
    mi "She spends so much time taking care of Victoria that she's probably neglecting herself."
    scene ee135 with dssa
    mi "I- Nrrgh-"
    mi "-overheard a conversation between Maja and a friend of hers... Victoria can't be left alone for long periods of time, and I am sure it's taking quite a toll on Maja."
    scene ee136 with dssa
    d "Well, if Maja really needs some time off, I guess I can- jump in for a day."
    scene ee137 with dssa
    mi "I told her the same, and she said that she is leaving for the weekend to visit an old friend."
    mi "And I will take care of Victoria while she is away."
    mi "If you want, you can also come."
    mi "I bet Victoria would love to see you."
    scene ee138 with dssa
    d "Yeah, I might come over."
    scene ee139 with dssa
    mi "Bring some pajamas."
    scene ee140 with dssa
    d "Oh, you mean I have to stay overnight?"
    scene ee141 with dssa
    mi "No, of course not but if you want... I think Victoria would like that."
    mi "Us three could watch scary movies, eat pizza, and tell funny stories."
    scene ee142 with dssa
    d "I'll give you my answer later."
    scene ee141 with dssa
    mi "Sure."
    scene ee143 with dssr
    d "Judging by what you said yesterday, I assume you really want to move out?"
    scene ee144 with dssa
    mi "There is nothing I want more."
    mi "I really hate it at hom- there."
    scene ee145 with dssa
    mi "Don't you want to move out, too?"
    scene ee146 with dssa
    d "Well... I feel 'safe' at home, you know. It's a place where I can-... well- just be."
    scene ee147 with dssr
    mi "Even if you moved out, your home would still be there, and you could go there whenever you wanted to."
    scene ee148 with dssa
    d "Hmm, moving out would mean that I would probably have to get a job."
    scene ee147 with dssa
    mi "We all would need to get one."
    mi "But on the other hand, it would also give you the ability to become more independent."
    scene ee149 with dssa
    d "Hmm. That's definitely a big plus. At the moment, I rely too much on Noji."
    scene ee150 with dssr
    d "And she's just working herself to death."
    scene ee151 with dssa
    d "I think, I really have to speak with Nami about moving out at some point... Or at least help Noji out with the money aspect."
    if bellameet is True:
        d "(Sadly, I can't give Nojiko a part of Mario's money. She'd get suspicious.)"
    scene ee152 with dssa
    mi "Living together with you and Nami... Not gonna lie. It sounds fun."
    mi "But I think they only have four people apartments at the campus."
    scene ee153 with dssr
    rob "Umm, Hello Mila."
    scene ee154 with dssa
    mi "Hey Robin."
    scene ee155 with dssa
    rob "I overheard your conversation about the student house. I too started to look into them a while ago, but I haven't found any roommates yet."
    rob "At least no roommates, I'd actually want to live with."
    scene ee156 with dssa
    d "You look familiar, aren't you in our class?"
    scene ee157 with dssa
    mi "Yes. Her name is Robin."
    mi "And if we got to know each other better, perhaps we could work something out?"
    scene ee158 with dssa
    d "(She's staring into my soul.)"
    scene ee159 with dssr
    d "Chill with the plans, girl. First I'd have to speak to Nami."
    d "Or you know what, you speak to her."
    scene ee160 with dssa
    mi "Sure, I can do that."
    scene ee161 with dssa
    mi "And Robin, let's stay in contact. The four of us can meet after we talk to Nami."
    scene ee162 with dssa
    rob "Yes, I'd like that."
    scene ee164 with dssa
    rob "I have to go now, classes are about to start in half an hour."
    scene ee160 with dssr
    mi "Oh right... We should probably wrap up our training as well."
    scene ee159 with dssa
    d "Let's do two more sets and we'll be good to go."
    scene ee165 with dssr
    rob "Bye."
    scene ee163 with dssa
    mi "Bye, bye."
    scene ee166 with dssr
    d "Alright, let's finish up."
    scene ee167 with dssa
    mi "Show me what you've got."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_NamiSad)
    scene sba669 with dssb
    rob "I didn't like the acting."
    $ persistent.unlockedImageSasha1 = True
    u "It was indeed defiant."
    scene sba670 with dssr
    mi "I will never get over the fact that these showers are unisex."
    scene sba671 with dssa
    d "Are you suddenly shy?"
    scene sba670 with dssa
    mi "I don't like displaying my assets that openly to other people."
    scene sba672 with dssr
    d "Judging by your cle-"
    scene sba673 with dssa
    mi "Yeah, I know that I often have a very revealing cleavage."
    scene sba674 with dssr
    mi "I like to tease, you know... Not slap 'em in your face."
    mi "And usually, I'd never go to the gym with a cleavage-.."
    scene sba675 with dssa
    "She suddenly stops speaking."
    scene sba676 with dssa
    d "...Usually? So you picked that outfit for me?"
    "She says nothing for a few seconds and only the water of the showers can be heard."
    scene sba677 with dssr
    pause
    mi "*sigh*. Maybe... and the fact that you didn't even look at my cleavage once makes me kind of insecure."
    mi "It's like- well- what else do I have to offer?"
    scene sba678 with dssa
    d "You act like your only traits are your boobs."
    scene sba679 with dssa
    mi "Well no... But, I never ever experienced this before. Like you don't even have this reflex. You just stare into my eyes without flinching."
    mi "I need to get used to that."
    if miladate is True:
        scene sba680 with dssa
        pause
        scene sba681 with dssa
        mi "But it also makes you special."
        mi "I think this is one of the reasons why I agreed to go and have dinner with you."
        scene sba682 with dssr
        mi "You know, I get asked out a lot and it's usually guys that want to sleep with me."
        mi "I don't get that feeling from you. To me it appears that you really want to get to know me."
        scene sba683 with dssa
        mi "And maybe you can even tell me the reason why you are like this."
        mi "Because even though this makes you unique, it also worries me."
        scene sba684 with dssr
        mi "[name]? Are you still there?"
        scene sba685 with dssa
        d "Yes, I am."
        d "If we go out and have dinner... I'll tell you why I am the way I am."
        scene sba686 with dssa
        mi "Thanks. I appreciate it."
    elif miladateF is True:
        scene sba680 with dssa
        pause
        scene sba681 with dssa
        mi "But it also makes you special."
        mi "I think this is one of the reasons why I wanted to-... well, if you wouldn't be going out with Victoria."
        mi "Then I would have probably said yes to your more serious invitation."
        scene sba682 with dssr
        mi "You know, I get asked out a lot. But they usually just want to sleep with me."
        mi "I don't get that feeling from you. To me it appears that you really want to get to know me."
        scene sba682 with dssr
        mi "And maybe you can even tell me the reason why you are like this."
        mi "Because even though this makes you unique, it also worries me."
        scene sba684 with dssr
        mi "[name]? Are you still there?"
        scene sba685 with dssa
        d "Yes, I am."
        d "If- we go out and have dinner, I will tell you why I am the way I am."
        scene sba686 with dssa
        mi "Thanks. I appreciate it."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sba687 with dssb
    mi "It was a nice workout."
    scene sba688 with dssr
    mi "We should do it again, and maybe next time not right before class. I like to take my time."
    scene sba689 with dssr
    d "Sure. I'll let you know when we can train together again."
    $ persistent.unlockedImageMila2 = True
    scene sba690 with dssr
    mi "Awesome!"
    $ persistent.unlockedImageMilaCH2_1 = True
    scene sba691 with dssr
    pause
    stop music fadeout 2.0
    $ achievement.grant("MilaGymA")
    $ achievement.sync()
    scene black with Dissolve(2)
    with Pause(.5)
    jump schoolch3

label schoolch3:
    $ play_playlist(playlist_Ch4x5v)
    scene m1035 with Dissolve(2.5)
    with Pause(.5)
    d "(This should be the room.)"
    scene m1037 with Dissolve(2)
    d "(No one here I know..)"
    scene m1043 with vpunch
    na "Wait, [name]?"
    scene m1044 with dissolve
    d "Yes?"
    scene m1043 with dissolve
    na "Huh, I didn't recognize you."
    if BTY is True:
        scene m1044 with dissolve
        "Nadia stares at you."
        scene m1043 with dissolve
        na "*whisper* You are an anomaly."
        scene m1044 with dissolve
        d "Mh?"
        scene m1043 with dissolve
        na "Bella spoke about you."
        scene m1044 with dissolve
        d "And?"
        scene m1045 with dissolve
        na "She barely speaks about other people."
        d "I guess we connect somehow."
        scene m1046 with dissolve
        na "I can see that."
        na "She changed your whole appearance in less than a day."
        scene m1047 with dissolve
        d "More like forced me to change it."
    else:
        scene m1047 with dissolve
        d "I did go through some drastic changes."
    scene m1048 with dissolve
    nan "Hey Nadia."
    na "Hi Nancy."
    $ persistent.unlockedImageNadia1 = True
    if bellagym is True:
        scene m1049 with dissolve
        d "I was at the gym with Bella."
        scene m1050 with dissolve
        na "Did you really train together?"
        scene m1049 with dissolve
        d "Yea, you sound surprised?"
        scene m1050 with dissolve
        na "What are you doing to her? You know her for a few days, and it's like you two are best friends."
        na "It took me 2 years till she opened up to me."
        d "I'd call it common ground."
        scene m1051 with dissolve
        na "Oh. You're a racer."
        if Brace is True:
            d "Wha- ah no. I'm not a street racer."
            scene m1052 with dissolve
            na "That's good."
            na "I really hope Bella and Ayua will stop with these races."
            na "Someday it will go wrong... It's only a matter of time. And I really dread that day."
            scene m1053 with dissolve
            na "And not a word to anyone about this!"
            scene m1054 with dissolve
            d "Are you threatening me with your banana?"
            scene m1053 with dissolve
            na "And I am not afraid to use it."
        else:
            $ BraceNadia = True
            d "A what?"
            scene m1052 with dissolve
            na "Ahh- never mind."
            d "Racer?.."
            d "She's one of those street racers?"
            scene m1053 with dissolve
            na "You don't know that from me!"
            scene m1054 with dissolve
            d "Are you threatening me with your banana?"
            scene m1053 with dissolve
            na "And I am not afraid to use it."
    else:
        scene m1050 with dissolve
        na "What are you doing to her? You know her for a few days and it's like you two are best friends."
        na "It took me 2 years till she opened up to me."
        d "I'd call it common ground."
        scene m1051 with dissolve
        na "Oh. You're a racer."
        $ BraceNadia = True
        d "A what?"
        scene m1052 with dissolve
        na "Ahh- never mind."
        d "Racer?"
        d "She's one of those street racers?"
        scene m1053 with dissolve
        na "...You don't know that from me!"
        scene m1054 with dissolve
        d "Are you threatening me with your banana?"
        scene m1053 with dissolve
        na "And I'm not afraid to use it."
    scene m1055 with vpunch
    $ persistent.unlockedImageNadia2 = True
    "You grab the banana out of her hand."
    na "*Whisper* My banana.."
    scene m1056 with dissolve
    "Nadia jumps up and tries to grab the banana out of your hand."
    scene m1057 with dissolve
    pause
    scene m1058 with dissolve
    na "I talked a little with Victoria."
    na "She told me that you were there when she had the accident."
    scene m1059 with dissolve
    d "Correct."
    scene m1058 with dissolve
    na "Poor little girl."
    scene m1060 with dissolve
    na "It breaks my heart to see her in that wheelchair, and I don't even want to imagine how her family feels."
    d "You talk a lot."
    scene m1061 with dissolve
    na "I'll stop it then."
    scene m1062 with dissolve
    d "No, it wasn't meant in a bad way."
    d "I just thought you were more of the quiet type."
    scene m1061 with dissolve
    na "I guess I kinda am."
    na "I have phases where I am kinda talkative and some where I don't talk at all."
    scene m1062 with dissolve
    d "Mh."
    d "But, I still feel some resentment towards you."
    scene m1061 with dissolve
    na "How so?"
    d "What you did to Nami on the first day."
    scene m1063 with dissolve
    na "You don't really think it was me, do you?"
    d "No, but you still could've told Bella and Ayua to stop it."
    na "I am not their babysitter."
    scene m1064 with Dissolve(2)
    d "(Sonya was her name I think.)"
    scene m1065 with dissolve
    pause
    d "(She looks lost. Seems like she doesn't know where to sit.)"
    scene m1064 with dissolve
    d "Hey."
    d "You can sit here if you want."
    scene m1066 with dissolve
    so "Okay."
    scene m1067 with dissolve
    na "Hi Sonya!"
    scene m1068 with dissolve
    so "Hey Nadia."
    scene m1070 with dissolve
    na "Are you in our gym team, too?"
    so "Yes."
    scene m1071 with dissolve
    d "(She's seems a little nervous.)"
    so "I'll be there next time."
    na "I look forward to it."
    d "And scream at her like you used to do at me?"
    scene m1072 with dissolve
    pause
    show CindyAni with dissolve
    $ renpy.pause(2.5, hard=True)
    with Pause(4.0)
    scene m1073 with dissolve
    pause
    scene m1074 with dissolve
    pause #serious eye squint look
    scene m1075 with dissolve
    $ persistent.unlockedImageCindy1 = True
    ci "Good morning, class."
    ci "My name is Cindy Mueller."
    ci "Everyone just take a seat. We don't have a special seating order."
    scene m1076 with dissolve
    ci "Today, we start with the fundamental aspects of algebra."
    ci "I want you all to be on the same level."
    ci "Here, everyone please complete these tests to determine your current level of math knowledge."
    scene m1078 with dissolve
    d "(Doesn't look hard..)"
    scene m1080 with dissolve
    ci "And if anyone has a question or needs help, don't be afraid to ask."
    scene black with Dissolve(2)
    with Pause(.5)
    scene m1081 with Dissolve(2)
    ci "Thank you. I will now review your results. You can use this free time to get to know your classmates."
    scene m1082 with Dissolve(2)
    pause
    scene m1083 with Dissolve(1)
    na "Sonya, where are you from?"
    scene m1084 with dissolve
    so "Iran."
    scene m1083 with dissolve
    na "What made your family move here?"
    so "We had to leave."
    scene m1085 with dissolve
    na "I see."
    na "Do you have siblings?"
    scene m1086 with dissolve
    so "*She nods* Two brothers."
    scene m1087 with Dissolve(2)
    pause
    scene m1088 with vpunch
    "Brrr"
    scene m1089 with dssa
    with Pause(.5)
    scene m1089x with dssa
    show v1 with dssr
    pause
    show v2 with dssa
    pause
    show v3 with dssa
    pause
    show v4 with dssa
    pause
    show v5 with dssa
    pause
    $ VicChat_CH3 = True
    if fitness is 2 and bellagym is True:
        $ nadia +=1
        scene m1090 with dissolve
        na "Your workouts are starting to show."
        scene m1091 with dissolve
        d "I guess a little, yeah."
        scene m1090 with dissolve
        na "It looks good."
        scene m1092 with dissolve
        d "...Thanks, I guess."
        scene m1093 with dissolve
        na "And maybe someday you can make an actual contribution to the sports team."
    elif fitness == 2:
        $ nadia +=1
        scene m1090 with dissolve
        na "Did you work out?"
        scene m1091 with dissolve
        d "Huh? Oh yea."
        scene m1090 with dissolve
        na "It shows."
        scene m1092 with dissolve
        d "Thanks, I guess."
        scene m1093 with dissolve
        na "And maybe someday you will be an actual contribution to the sports team."
    scene m1095 with dissolve
    nan "Uh, Nadia?"
    na "Yes, Nancy?"
    nan "I haven't seen you at the meet up in quite some time."
    scene m1096 with dissolve
    na "Oh, I was just busy. I'll be there soon."
    scene m1097 with dissolve
    nan "Great... Romeo quit, too."
    nan "I- don't know if we're still enough to play it properly."
    scene m1099 with dissolve
    na "[name]. Are you interested in board games?"
    scene m1100 with dissolve
    d "Uh- like monopoly?"
    scene m1099 with dissolve
    na "Yea kinda, a lot more complex, and you look like someone who'd like that."
    scene m1100 with dissolve
    d "Because I look like a nerd?"
    scene m1099 with dissolve
    na "You did look like one. Bella changed that."
    na "So, if you know somebody who might like it, come to a meet up."
    scene m1102 with dissolve
    $ persistent.unlockedImageNancy1 = True
    d "I didn't take you for a gamer."
    scene m1101 with dissolve
    na "I live for fantasy."
    scene m1102 with dissolve
    d "Well Nami is a gamer too. She might like it."
    scene m1101 with dissolve
    na "What about you? You and Nami can take a look."
    scene m1102 with dissolve
    d "I am not really a gamer anymore but... I'll ask her and we'll take a look."
    scene m1099 with dissolve
    na "Great."
    na "By the way, this is Nancy."
    scene m1103 with dissolve
    d "Hi."
    nan "Hi."
    scene m1067 with dissolve
    na "You can come, too, Sonya."
    so "I- no."
    d "(I think she would like to, but can't.)"
    d "(Maybe it's possible to convince her parents that only girls are there.)"
    scene m1098 with dissolve
    nan "We play different kinds of games. Most are kinda in the RPG spectrum. And many of them feature a more dark approach."
    scene m1099 with dissolve
    na "True, but it's really good. It features more classes and even slightly more adult topics."
    na "It features two game modes. One Co-op mode where we all play in a team and one PvP mode."
    scene m1104 with dissolve
    nan "If you decide to come [name]- uhm- we would start a co-op match. So beginners can learn the basics."
    d "Mhm."
    scene m1105 with dissolve
    ci "Alright! It seems like everyone here is on the same level... Some small differences but nothing huge."
    ci "Let the lesson begin!"
    scene black with Dissolve(1.5)
    with Pause(1.5)
    scene m1107 with dissolve
    ci "Alright! That's it for your first lesson!"
    ci "And one important announcement!"
    ci "You now have 3 days to sign up for a Library ID if you plan on using the library."
    ci "The ID is for free. If you miss the three days, you will have to pay $20 for the ID."
    scene m1108 with dissolve
    nan "[name] and Sonya? Would you like to have lunch with us?"
    na "We can grab something in the cafeteria. It's just around the corner."
    scene m1109 with dissolve
    "You and Sonya give each other a look."
    d "(I still have some time before I have to go to Amber.)"
    d "Okay."
    scene m1110 with dissolve
    so "I- um- okay."
    na "Let's go."
    scene black with Dissolve(2.5)
    with Pause(.5)
    scene m1111 with Dissolve(2)
    har "I get where you are coming from."
    scene m1112 with dissolve
    mh "It will work out."
    scene m1111 with dissolve
    har "I hope so."
    scene m1113 with dissolve
    pause
    scene m1114 with dissolve
    na "Sonya, are you going to compete in the tournaments?"
    scene m1116 with dissolve
    so "What tournaments?"
    scene m1115 with dissolve
    na "Right. You weren't there."
    na "The sport tournaments we're training for."
    scene m1116 with dissolve
    so "I don't know. What tournaments exactly?"
    scene m1114 with dissolve
    na "Basketball, soccer, football, tennis, volleyball, boxing or fighting in general and swimming."
    na "We also have non-sport tournaments. Like chess and other board games."
    scene m1117 with dissolve
    "Her eyes go wide as she hears the word, swimming."
    so "No swimming."
    scene m1118 with dissolve
    d "Is it because of your religion?"
    "She nods."
    scene m1114 with dissolve
    na "That's okay. But you can attend the other ones, right?"
    so "I-guess."
    "Brrrr Brrrr Brrrr"
    scene m1125 with dissolve
    d "Yes.."
    n "Hi."
    d "What's up?"
    if namix ==1:
        n "I should ask you if you want to come with us to a bar."
        d "(She's still mad... I can hear it in her voice.)"
    else:
        n "You coming with us to a bar?"
        d "I can come later but... I need to... you know."
        n "Ah yeah, sure. Just catch up later."
    d "I will but I can't stay long. I have-"
    n "The date with Bella."
    d "Send me the address."
    if bellameet is True:
        n "Drinks on you, okay?"
        d "What?"
        n "*angry whisper* You have 10k! You can at least pay for my drinks tonight!"
        d "...Alright."
    d "(The food is actually pretty good.)"
    scene m1126 with dissolve
    nan "Have you thought about the new game?"
    scene m1128 with dissolve
    na "I don't know, Nancy."
    scene m1127 with dissolve
    nan "A little kinky?"
    scene m1129 with dissolve
    na "Let's just say that some options are very weird."
    na "And you know what it means when I say that..."
    na "Especially the stuff you know... when you get downed."
    na "But if the others are in, we can give it a try."
    scene m1119 with dissolve
    so "I-is Nami your friend?"
    d "Yeah, she is."
    so "She is a kind person."
    d "I would say she's a very social person. At least more social than me."
    so "Or me."
    scene m1121 with dissolve
    "You give each other a subtle smile."
    scene m1130 with dissolve
    na "I'll get some more food."
    nan "I'll come with you."
    if sonyatalk is True:
        scene m1122 with dissolve
        d "...Did you think about what I said on the bus?"
        scene m1124 with dissolve
        "She nods."
        d "What will you do?"
        scene m1123 with dissolve
        so "I- don't kn-ow."
        scene m1124 with dissolve
        d "We both know what you're going to do and when the day comes, talk to Nami or me."
    d "This board game thing that Nadia mentioned... You should come."
    scene m1123 with dissolve
    so "I don't know if I can."
    scene m1122 with dissolve
    d "Your parents will forbid it?"
    scene m1123 with dissolve
    so "Most likely."
    scene m1124 with dissolve
    d "Mhh. I might-"
    scene m1131 with dissolve
    na "You got the last pudding?"
    nan "Yes."
    na "*sigh* Maaan.."
    scene m1132 with dissolve
    na "What?"
    d "Do me a favor, Nadia."
    scene m1133 with dissolve
    "She gives you a questioning look."
    d "Sonya, give me your phone."
    scene m1140 with dissolve
    so "Why?"
    d "You want to play with us... Then dial a parent, and give me your phone."
    scene m1141 with dissolve
    "Sonya hesitates at first."
    scene m1142 with dissolve
    "But then decides to give you the phone."
    scene m1133 with dissolve
    so "W-what are you"
    scene m1134 with vpunch
    na "[name]?"
    d "Tell her parents that she has to attend an important seminar, only for females."
    "You push the phone into her hand while it's dialing."
    scene m1135 with dissolve
    na "Ah- H-hello?"
    na "Yes- ah- I- I am Sonya's professor, good morning."
    scene m1136 with dissolve
    d "(She caught herself.)"
    na "I wanted to inform you that your daughter has to attend a female only class on Wednesdays and Fridays. And sometimes also over the weekend."
    na "Mhhm."
    scene m1137 with dissolve
    na "Yes, exactly... No, no males will be there this is a female only event."
    na "Great."
    na "Of course I'll keep an eye on her... and the doors."
    na "Goodbye."
    scene m1138 with dissolve
    na "*Long exhale of relief.*"
    na "Never... do that again."
    d "But Sonya can come with us now."
    scene m1139 with vpunch
    so "Yes!"
    $ persistent.unlockedImageSonya4 = True
    "You are caught off guard by Sonya's strong, non-stuttering voice."
    d "(She must be really excited.)"
    scene m1143 with Dissolve(2)
    d "I have to leave now."
    nan "Take care."
    na "Bye."
    so "Goodbye [name]."
    scene m1144 with dissolve
    d "(I have to find Miss Marla, I have to skip the lesson to attend my therapy session.)"
    scene m1145 with dissolve
    d "(Coach Hill.)"
    scene m1146 with dissolve
    d "Coach?"
    "Coach Hill eyes you for a second."
    scene m1147 with dissolve
    $ persistent.unlockedImageHill1 = True
    mh "Oh-"
    mh "Spaghetti, I didn't recognize you. Looking good."
    d "I need to find Miss Marla. Do you know where I can find her?"
    scene m1148 with dissolve
    har "Stefanie often eats her lunch in her classroom."
    scene m1149 with dissolve
    d "Thanks."
    scene m1148 with dissolve
    har "[name]."
    har "Will you tell how you got that wound?"
    d "Would you believe me if I said I fell?"
    scene m1150 with dissolve
    har "No."
    scene m1151 with dissolve
    d "Bummer."
    stop music fadeout 3.0
    scene black with Dissolve(2)
    show text "You make your way through the college to Miss Marla's classroom." with Dissolve(3)
    $ play_playlist(playlist_AmbientCheeto)
    with Pause(.5)
    hide text with Dissolve(2)
    menu:
        "Knock at her door.":
            $ mmc = False
            d "Miss Marla?"
            ma "O-one moment, please!"
            ma "Come in."
            scene m1159 with dissolve
            d "Can I skip today's lesson? I have an appointment with Amber."
            scene m1158 with dissolve
            ma "Yes.."
            ma "Please choose your next appointments at a better time."
            "You nod."
        "Just go in.":
            $ mmc = True
            scene m1152 with dissolve
            d "Miss Ma-"
            scene m1154 with vpunch
            ma "*gasp*."
            $ persistent.unlockedImageMarla1 = True
            ma "Ah- [name]- can't you knock?! - she stutters while she wishes her tears away."
            menu:
                "What's wrong?":
                    $ marla +=1
                    scene m1155 with dissolve
                    ma "Nothing!"
                    d "I- of course knew that you wouldn't tell me..."
                    d "And I won't bother you anymore... I just have a quick question."
                    d "Can I skip today's lesson? I have an appointment with Amber."
                    scene m1156 with dissolve
                    ma "Of-f course."
                    d "Thank you."
                    d "(I am pretty sure it's because of the accident she caused. She isn't taking it well.)"
                "I don't care.":
                    scene m1155 with dissolve
                    d "(Ugh..)"
                    d "Can I skip today's lesson? I have an appointment with Amber."
                    ma "Yes.."
    scene m1160 with Dissolve(2)
    d "(The son of a bitch.)"
    scene m1161 with dissolve
    sai "What?! What are you looking at?"
    d "Your ugly face distracted me."
    play music "music/Suspense/Scott Buckley - Resonance.ogg"
    scene m1162 with vpunch
    u "You little bitch, who do you think you are?"
    u "Let's show him his place!"
    scene m1163 with dissolve
    pause
    scene m1164 with dissolve
    j "Are you sure about that?"
    sai "That's no-"
    scene m1165 with dissolve
    j "Listen to me you little shit... If I see you picking on him again... I'll pick on you."
    scene m1166 with dissolve
    sai "Consider yourself lucky.."
    scene m1167 with dissolve
    sai "For now."
    scene m1168 with dissolve
    j "Yo, what's going on?"
    d "Long story."
    scene m1170 with dissolve
    j "Where did you get the cut, bro? Was it one of them?!"
    d "Jeff, I can handle it."
    scene m1169 with dissolve
    j "I doubt that you can handle 3 people."
    menu:
        "Thank him":
            $ jeff +=1
            d "But thanks, Jeff."
            scene m1171 with dissolve
            j "No problem, buddy."
            j "Just give me a call when they stress you again."
            scene m1172 with dissolve
            d "Will do."
            d "I'll see you, Jeff."
        "I could've handled it.":
            $ jeff -=1
            j "If you say so."
            scene m1170 with dissolve
            j "I'll see you."
        "Don't say anything":
            d "Well, I am in a hurry."
            scene m1170 with dissolve
            j "Sure, I'll see you."
    stop music fadeout 2.5
    scene black with Dissolve(1.5)
    show text "You make your way to your next session with Amber." with Dissolve(2.5)
    with Pause(0.5)
    hide text
    jump AmberTherapy2

label AmberTherapy2:
    scene ss246 with dssb
    pause
    scene ss247 with dssr
    pause
    play music "music/VeskyBeyondTheWindow.ogg"
    scene ss248 with dssr
    pause
    scene ss249 with dssa
    am "Hello [name]."
    $ persistent.unlockedImageAmber4 = True
    scene ss250 with dssr
    d "I didn't hear you come in."
    scene ss251 with dssa
    am "What were you thinking about?"
    scene ss250 with dssa
    "You hold in for a few seconds."
    d "Memories... Memories I kept myself from thinking about."
    scene ss252 with dssr
    am "Facing our fears is one of the biggest challenges in life."
    scene ss253 with dssr
    am "How are you today?"
    scene ss254 with dssa
    d "Fine, I guess."
    scene ss253 with dssa
    am "That's good."
    am "The last time we were talking about Nami and the fact that she didn't like your fondness for Summer."
    scene ss254 with dssa
    d "Right..."
    scene ss253 with dssa
    am "We'll speak about Nami soon. But first tell me about the day you and Summer... found each other."
    scene ss255 with dssr
    d "...You mean when we fell in love?"
    scene ss256 with dssa
    am "Not necessarily. Tell me about the day you started to accept her."
    d "Hmm..."
    scene black with Dissolve(1.5)
    with Pause(.5)
    scene m1227 with dssb
    n "It's raining soooo much."
    scene m1228 with dissolve
    pause
    scene m1229 with dissolve
    s "What a bummer! I had hoped we could swim in the lake."
    n "Me too."
    scene m1230 with dissolve
    s "We could play some video games!"
    scene m1231 with dissolve
    n "My console isn't working anymore... I accidentally spilled juice over it."
    scene m1230 with dissolve
    s "What about [name]'s?"
    scene m1231 with dissolve
    n "Nooo. We're not allowed to use it."
    scene m1230 with dissolve
    s "Is he here?"
    n "No."
    scene m1232 with dissolve
    s "Then let's just do it! We play a few rounds and then leave and he will never know!"
    n "I don't know..."
    n "What if he suddenly comes back?"
    scene m1233 with dissolve
    s "Then I beat him up!"
    scene m1234 with dissolve
    s "Hihi, come on!"
    scene black with Dissolve(3)
    scene m1236 with Dissolve(2)
    s "So many bugs!"
    scene m1235 with dissolve
    s "See it's awesome!"
    scene m1237 with dissolve
    n "He even got some new games! He must've stolen them!"
    s "Does he steal?"
    scene m1238 with dissolve
    n "I saw him steal gum once."
    scene m1239 with dissolve
    s "He is such a meany."
    scene m1240 with dissolve
    s "Man, you're so good!"
    scene m1241 with dissolve
    pause
    scene m1242 with dissolve
    pause
    scene m1243 with vpunch
    d "I said you're not allowed to use my console!"
    scene m1244 with dissolve
    s "Why isn't she?!"
    d "Because she'll destroy it!"
    s "It wasn't her idea! It was mine!"
    d "You cow!"
    scene m1245 with dissolve
    s "Shut up!"
    d "Or what?! You cow!"
    scene m1246 with vpunch
    s "Aaahh!"
    scene m1247 with dissolve
    n "Not again! Noo!!"
    "You try to push her away from you."
    scene m1248 with vpunch
    s "MHhhmm!"
    scene m1249 with dissolve
    n "Ewww! Summer!"
    d "Wha- did you just do?!"
    scene m1250 with dissolve
    s "Seems like I won!"
    scene black with Dissolve(2.5)
    with Pause(.5)
    scene ss257 with dssb
    d "I just laid there... I was shocked."
    scene ss256 with dssa
    am "I understand that."
    am "For such a young boy, a kiss from a girl must've been quite the event."
    scene ss258 with dssa
    d "Even after they left... I didn't move for another five minutes."
    scene ss256 with dssa
    am "Did you find the kiss disgusting?"
    scene ss259 with dssr
    d "At first, yes."
    d "But... Ever since that happened, I slowly started to fall for her."
    d "And with every day Nami and Summer grew more and more apart."
    "Amber nods slowly."
    scene ss260 with dssa
    am "I see. Let's talk about the present."
    am "Can you tell me in your own words how you felt today?"
    scene ss261 with dssr
    d "Like the mood I had today?"
    scene ss262 with dssa
    am "Your thoughts... Your moods, everything."
    scene ss261 with dssa
    "You keep quiet for a moment."
    if bellagym is True:
        d "The day started good."
        scene ss262 with dssa
        am "You visited the gym with Bella, right?"
        scene ss261 with dssa
        d "Yes."
        scene ss262 with dssa
        am "How was it?"
        scene ss261 with dssa
        d "As I said... Good."
        if MCBL == 1:
            d "...Very good."
        scene ss262 with dssa
        am "I did notice some significant changes in yours and Bella's behaviors."
        am "The first time I saw you two together was forced. Neither you nor she wanted to be there."
        am "And I was sure that this wouldn't change."
        scene ss263 with dssa
        am "When she came home yesterday she vanished into the kitchen and I watched her from the living room."
        am "She was deeply in her thoughts and... She had a neutral expression for most of the time but I did catch a few subtle smiles."
        am "...Whatever you and her are doing [name]... She likes it."
        if bellameet is True:
            scene ss256 with dssa
            am "But... I sincerely hope that you two didn't break into the Holgersons house."
            "You stay silent."
            scene ss262 with dssa
            am "Back to the topic."
    elif namigym is True:
        d "I went to the gym with Nami."
        scene ss262 with dssa
        am "How was it?"
        scene ss261 with dssa
        d "Nami invited an unexpected guest."
        scene ss262 with dssa
        am "Male or female?"
        scene ss261 with dssa
        d "Female."
        d "Her name is Nia."
        scene ss263 with dssa
        am "How do you and Nia stand with each other?"
        scene ss264 with dssa
        d "It's difficult to say."
        d "There is something about her that makes me angry."
        d "She is annoying and socially awkward."
        scene ss263 with dssa
        am "Aren't you the same?"
        scene ss264 with dssa
        d "No."
        d "I know how to behave and I know what to say to get a certain reaction."
        d "It's just that I often don't care."
        scene ss261 with dssa
        am "I see."
    elif gymalone:
        d "I went to the gym alone."
        d "I had a good workout and that was about it."
    elif nogymch3:
        d "I thought about going to the gym but I didn't."
        d "I just went straight to college."
        scene ss263 with dssa
        am "How so?"
        d "I- just wasn't motivated, I guess."
    elif milagym is True:
        d "I went to the gym with a friend."
        scene ss263 with dssa
        am "I see."
    scene ss265 with dssr
    am "How did college go? And let me ask you about that wound in particular."
    scene ss266 with dssa
    d "I got into a fight."
    scene ss265 with dssa
    am "Why? What caused the fight?"
    scene ss266 with dssa
    d "He picked on me."
    scene ss268 with dssr
    am "And he just punched you?"
    scene ss267 with dssa
    d "No, after he refused to let me through I punched him in the face... which resulted in a fight."
    d "A friend of his came up from behind me, and before I could react... he hit me."
    scene ss268 with dssa
    am "You fought against two people?"
    scene ss267 with dssa
    d "At first... But it wasn't worth it. I ran away."
    scene ss268 with dssa
    am "That was a wise decision, and I advise you to speak to a professor about it."
    scene ss267 with dssa
    d "No."
    scene ss269 with dssa
    am "Why not?"
    scene ss270 with dssr
    d "*sigh* I will handle it myself."
    scene ss271 with dssa
    am "Do you often get into fights?"
    scene ss272 with dssa
    d "In high school... every day."
    scene ss271 with dssa
    am "How so?"
    scene ss272 with dssa
    d "After everything went down, I became the weird kid."
    d "I didn't talk. I never laughed. I was stone cold."
    scene ss275 with dssr
    am "Was?"
    scene ss276 with dssr
    d "I'm still repulsed by any sort of... emotion. But in high school it was on a different level."
    d "At first I was just silent. I didn't care what the others said, and I never paid attention to them."
    d "I was trapped in my thoughts. It were only words... They didn't attack me physically..."
    scene ss277 with dssa
    am "I assume that changed."
    scene ss278 with dssa
    d "As we grew older... Nami became popular. She was the cool redhead..."
    d "Almost everyone liked her. Especially guys."
    scene ss279 with dssr
    am "How was your relationship with Nami at that time?"
    scene ss280 with dssa
    d "We were very close."
    d "After the thing with Summ- *you inhale deeply.*"
    d "After Summer's disappearance, Nami and I got very close."
    d "She took pity on me and got very protective."
    scene ss281 with dssa
    am "How did this result in more fighting?"
    am "Her popularity must have discouraged people from antagonizing you."
    scene ss282 with dssa
    d "It did. People always acted... And I emphasize 'acted' nice towards me."
    d "I went from being 'trapped in my thoughts' to observing."
    d "I started to study the people around me. Not because I was interested in them but because I wanted to protect Nami at all costs."
    scene ss277 with dssr
    am "Did she need protection?"
    scene ss276 with dssa
    d "Yes and no. She always had guys at her feet, and they tried to date her and so on."
    scene ss275 with dssa
    am "Did this make you jealous?"
    scene ss276 with dssa
    d "No."
    scene ss277 with dssa
    am "And you prevented this by?"
    scene ss283 with dssr
    d "I did manipulate certain events, yes."
    scene ss284 with dssa
    am "Does Nami know that?"
    scene ss283 with dssa
    d "No, of course not. She still thinks I never gave a damn about her in high school."
    d "I was very distant to her... but I was pulling strings in the background."
    scene ss284 with dssa
    am "And the other guys found out about it?"
    scene ss285 with dssa
    d "No. I was just getting bored so instead of manipulating them from the shadows I turned to a more direct approach."
    d "I told them to fuck off and leave her alone."
    scene ss284 with dssa
    am "And this resulted in years of fighting?"
    scene ss285 with dssa
    d "Correct."
    scene ss284 with dssa
    am "You could have gone back to your old, quiet self."
    am "It would've probably stopped the fighting."
    scene ss273 with dssr
    d "It would have... But..."
    scene ss274 with dssa
    d "I liked it." #Mc smile
    d "I did lose many fights because of multiple opponents at once.."
    am "It made you feel something?"
    d "It made me feel alive."
    scene ss286 with dssr
    "You both don't say a word for almost 10 seconds. Only the ticking of an old clock can be heard."
    scene ss287 with dssr
    am "[name], is there someone you love?"
    d "What a weird question but- Right now?"
    d "Only Noji and Nami."
    scene ss288 with dssr
    am "Let's talk about your sexuality."
    scene ss289 with dssr
    d "Why?"
    scene ss288 with dssa
    am "Because you're a young man and in college."
    am "Have you had sex with an individual before?"
    scene ss289 with dssr
    d "No."
    scene ss290 with dssa
    d "There were quite a few girls that pursued me... I think they found me edgy or some shit like that... I think it was the fact that I didn't give a fuck."
    d "But I never acknowledged them."
    scene ss288 with dssa
    am "You weren't in the need of attention."
    scene ss289 with dssa
    d "No, I just wanted to be alone- and feel alive at the same time."
    scene ss288 with dssa
    am "But, I can see that you're trying to leave this shell."
    scene ss290 with dssa
    d "Yes, otherwise I wouldn't be here- well I would still be here just to make Nojiko happy."
    d "But yes, I- I want to fix myself."
    if bellalove >=2:
        scene ss291 with dssa
        am "How do you feel about Bella?"
        scene ss292 with dssa
        d "What?"
        scene ss291 with dssa
        am "It's a simple question."
        if MCBL >=1:
            menu:
                "I'm starting to like her.":
                    $ amber +=2
                    $ BYF = True
                    $ bellalove +=1
                    scene ss293 with dssa
                    d "She... She's the first person in a long time I kind of like."
                    scene ss294 with dssa
                    am "What does she make you feel?"
                    scene ss295 with dssa
                    d "*You shrug your shoulders* Alive, I guess."
                    scene ss296 with dssa
                    am "Do you think Bella feels the same?"
                    scene ss293 with dssa
                    d "Yes."
                    scene ss297 with dssa
                    am "You two are going out tonight... She called it 'business related'... but... we both know that this isn't the full truth."
                    am "It might have been that way at first... but the overall tone has changed."
                    scene ss298 with dssa
                    d "...You're saying it's a real date?"
                    scene ss297 with dssa
                    am "That depends on you. If you say the right things it will turn into one."
                    scene ss298 with dssa
                    d "I see."
                    scene ss297 with dssa
                    am "And... Bella likes yellow flowers. Bring her one but don't tell her I told you this."
                "Neutral.":
                    scene ss295 with dssa
                    d "I just feel neutral about her."
                    scene ss296 with dssa
                    am "I see."
        else:
            scene ss295 with dssa
            d "Neutral. I- yeah... Just neutral."
            scene ss296 with dssa
            am "I see."
    else:
        pass
    scene ss299 with dssr
    am "Thank you for your honesty and trust, [name]."
    scene ss300 with dssa
    d "There is something else."
    d "There is this dream."
    scene ss301 with dssa
    am "What kind of dream?"
    scene ss300 with dssa
    d "It's an event from the past that I'm reliving over and over again."
    scene ss301 with dssa
    am "How often does this dream appear?"
    scene ss300 with dssa
    d "Once or twice a week... It was almost every day a year ago."
    scene ss301 with dssa
    am "What happens in this dream?"
    scene ss300 with dssa
    d "Summer and I are in the woods and we were observing a white spider.."
    d "But that doesn't matter. *sigh* The dream ends in a cabin. Summer and I are kissing and I then either realize that it's a dream or Officer Larverne appears and the dream ends shortly after."
    scene ss302 with dssr
    am "This event was special to you?"
    scene ss303 with dssa
    d "It was-"
    d "It was the last time I touched her... The last time I kissed her."
    scene ss302 with dssa
    am "But not the last time you saw her?"
    scene ss304 with dssr
    d "*You slowly shake your head* I did see her one more time and-..."
    scene ss305 with dssa
    pause
    scene ss306 with dssa
    am "It's okay [name].."
    scene ss307 with dssa
    am "That's enough for today."
    if AmberAP is True:
        scene ss308 with dssr
        am "*Sensual whisper* It's going to be okay."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ss309 with dssb
    am "I'll give you a call about the next session and the next session will be a little different."
    scene ss310 with dssa
    d "How so?"
    scene ss312 with dssa
    am "We will take a more practical approach. We will visit this cabin you just told me about."
    if mmc == True:
        menu:
            "Tell her about Miss Marla.":
                $ marla +=3
                $ amberlove +=1
                $ AMMC = True
                $ achievement.grant("AmberMarla")
                $ achievement.sync()
                scene ss311 with dssa
                d "One more thing. I think you should look out for Miss Marla."
                scene ss311 with dssa
                d "I found her crying today. I don't think she's doing so well."
                scene ss314 with dssa
                am "Thank you, [name]."
                "You nod."
                am "[name]. Thank you... really."
            "Don't tell her about it":
                $ AMMC = False
                with Pause(.8)
    else:
        pass
    $ persistent.unlockedImageAmber7 = True
    scene ss315 with dssr
    "You leave Amber's office."
    with Pause(.8)
    stop music fadeout 2.0
    scene black with Dissolve(2.5)
    jump bar03

label bar03:
    $ play_playlist(playlist_Diner)
    scene ss33 with dssb
    pause
    scene ss34 with dssr
    "You arrive at the bar. Besides a handful of people. The bar is empty."
    scene ss36 with dssr
    t "Hey!"
    d "Hi."
    scene ss37 with dssa
    t "Glad you could make it."
    scene ss38 with dssa
    t "The others are over there."
    scene ss39 with dssr
    pause
    if mobility == 1:
        scene ss40 with dssa
        rob "Hey [name]!"
        scene ss41 with dssr
        d "Oh. Hi Robin."
    else:
        pass
    scene ss42 with dssr
    d "Hey."
    scene ss43 with dssa
    n "Yo."
    scene ss44 with dssa
    ay "Hi!"
    scene ss45 with dssa
    j "Hey [name]!"
    scene ss46 with dssr
    dam "Hey, I'm Damian."
    scene ss47 with dssa
    d "I'm [name]."
    d "I haven't seen you before. Are you at ZPR?"
    scene ss46 with dssa
    dam "Yeaaah, for some reason people tend to overlook me."
    scene ss48 with dssr
    pause
    scene ss49 with dssa
    d "*Sigh*"
    scene ss50 with dssa
    ay "What?"
    scene ss51 with dssa
    d "I'm tired."
    scene ss52 with dssa
    t "No dude! Let's get drunk!"
    d "Nah. I still have somewhere to be later."
    scene ss126 with dssr
    j "I hope you didn't run into any other problems."
    scene ss130 with dssr
    n "Mh? What problems?"
    j "Three dudes-"
    scene ss127 with dssr
    "You give him a serious look and shake your head."
    scene ss128 with dssa
    j "Uh- Ahh- I forgot something at the bar."
    scene ss129 with dssa
    j "[name], why don't you help me carry."
    scene ss131 with dssr
    j "Dude? What's going on?"
    scene ss132 with dssa
    d "Don't speak about it in front of Nami."
    scene ss131 with dssa
    j "Why not? I have seen them talking."
    scene ss133 with dssr
    d "I see."
    scene ss134 with dssa
    j "But he left when I came."
    scene ss133 with dssa
    d "I didn't tell her that it was him. Well it was his friend actually."
    scene ss135 with dssa
    j "Why not?"
    scene ss136 with dssa
    d "If I tell Nami what he did, I'll lose a valuable asset. She's capable of giving me inside information without being aware that she's giving me inside information."
    scene ss135 with dssa
    j "That's a dangerous game."
    scene ss138 with dssr
    lay "Hey, can I get you something?"
    d "One of those big beer mugs, please."
    scene ss140 with dssa
    lay "Sure."
    scene ss143 with dssa
    menu:
        "Can I count on you to have an eye on Nami?":
            $ JNS = True
            j "Of course!"
            j "Nami is my friend, too!"
            scene ss142 with dssa
            d "Thanks."
            d "But try not to make it obvious. I want him to feel safe."
            scene ss143 with dssa
            j "Yeah, I get it."
        "Don't ask him.":
            j "All I am saying is. Be careful."
            scene ss142 with dssa
            d "I'll have it under control, no worries."
    scene ss141 with dssr
    lay "Here you go."
    d "Thanks."
    scene ss145 with dssr
    pause
    scene ss144 with dssa
    "You notice Ayua staring at you intensely."
    scene ss146 with dssr
    d "(Did she hear us? Impossible.)"
    d "(Does she read lips?)"
    scene ss147 with dssr
    n "And where is the stuff you couldn't carry alone, Jeff?"
    scene ss148 with dssa
    j "You look amazing, Nami."
    scene ss149 with dssa
    n "What's going on?"
    scene ss150 with dssa
    d "Nothing."
    d "(She obviously doesn't believe it. But that's not so bad. It means she'll be more on alert.)"
    scene ss53 with dssr
    ay "I know what you said."
    scene ss54 with dssa
    d "You read lips?"
    scene ss55 with dssa
    "She just smiles."
    scene ss53 with dssa
    ay "These mind games you are playing can bring unforeseeable consequences."
    if Brace is True:
        scene ss56 with dssa
        d "So can being a street racer."
        scene ss57 with vpunch
        ay "How do you know that?!"
        scene ss151 with dssr
        pause
        scene ss58 with dssa
        ay "You guys mind your own business."
        scene ss59 with dssr
        ay "*whisper* How did you find out?"
        scene ss60 with dssa
        d "*whisper* Bella told me."
        scene ss59 with dssa
        ay "What?! Why-... Oh... I see."
        scene ss61 with dssa
        d "Don't draw any wrong conclusions."
        scene ss62 with dssa
        ay "I am so glad you two are getting so close."
        ay "*Whisper* Bella would never ever tell anyone that she does illegal street racing."
        scene ss63 with dssr
        ay "Only a few people know."
        scene ss64 with dssa
        d "Her car is very striking."
        scene ss63 with dssa
        ay "She doesn't use that car for the races."
        scene ss64 with dssa
        d "She has more cars?"
        scene ss63 with dssa
        ay "Yes, we people from the scene have our own workshop. We store the cars there."
        ay "You can't drive the cars you use for racing on the street. The police would be on your ass in the blink of an eye."
        scene ss65 with dssa
        ay "But damn, the fact that she told you this..."
        ay "After your first confrontation with her about her sister, I thought this was it."
        scene ss66 with dssr
        ay "How did you recover from that? Why does she like you so much?"
        scene ss67 with dssa
        if MCBL == 1:
            d "I can't really say. We connect on certain levels."
            d "As she once said to me... She and I aren't so different."
        else:
            d "We have the same goal... I think we kinda connect because of that."
        scene ss68 with dssr
        ay "I need to call her later! Haha, I'm so happy right now."
        scene ss69 with dssa
        d "You'd better wait. She and I are going... to a restaurant."
    else:
        d "I have it under control."
        ay "Famous last words."
        scene ss68 with dssr
        ay "*Long exhale* I'm glad you and Bella didn't kill each other yet."
        scene ss69 with dssa
        d "It can still happen."
        d "I mean, we're heading to a diner later."
    $ persistent.unlockedImageLayla1 = True
    scene ss70 with vpunch
    ay "YOU'RE GOING OUT!?"
    scene ss78 with dssr
    j "Who is going out?"
    scene ss79 with dssa
    d "Bella and me."
    scene ss80 with vpunch
    t "*cough* Arrh- *cough*!"
    scene ss81 with dssa
    t "You're going out with crazy Bella?!"
    scene ss71 with dssr
    ay "Hey, hey!"
    scene ss82 with dssr
    t "Don't stick your dick in crazy."
    scene ss72 with vpunch
    ay "She isn't crazy and if anybody here says one more bad word against her, I'll knock him the fuck out!"
    scene ss73 with dssr
    lay "Everything okay, guys?"
    scene ss74 with dssa
    ay "We're good... For now."
    scene ss75 with dssa
    lay "Please don't destroy the bar before it even opened, Ayua."
    menu:
        "I actually like Bella.":
            $ ayua +=2
            $ nadia +=2
            $ bellalove +=1
            $ AYTNA = True
            scene ss83 with dssr
            j "Bella's not bad... but she's got some stuff to work out."
            scene ss90 with dssr
            n "I don't get it."
            scene ss92 with dssr
            ay "I'm so happy about that!"
            scene ss91 with dssa
        "It's more of a business meeting.":
            $ bellalove -=2
            scene ss83 with dssr
            j "Be careful."
            scene ss91 with dssr
    d "Why are you so close to me?"
    scene ss93 with dssa
    j "She obviously can't hold her liquor."
    scene ss94 with dssa
    ay "...I got this from my mom. I get drunk very fast. *giggles*"
    scene ss101 with dssr
    u "Ayua, I'm cutting you off."
    ay "*Faint whisper* Noooooo... My beer!"
    if AyuaSparring is True:
        scene ss95 with dssr
        ay "And we're still doing our fighty fight, right?"
        scene ss96 with dssa
        d "Depends on how touchy you get..."
        "She giggles."
        scene ss94 with dssa
        ay "And don't make the mistake to think I'm weak."
        scene ss98 with dssa
        d "I'm not that stupid."
        scene ss97 with dssa
        ay "Bummer... I would loved to see your face."
        scene ss98 with dssa
        d "What kind of martial arts do you know?"
        scene ss97 with dssa
        ay "Brazilian Jiu-Jitsu, Muay Thai, Judo..."
        ay "But my family has their own fighting techniques... Maybe... Maaaaybe show you a little."
        scene ss98 with dssa
        d "You keep that knowledge inside the family?"
        scene ss99 with dssa
        ay "Mhm... and if you don't marry me, my sisters or one of my cousins, you'll never get to experience it."
        scene ss90 with dssr
        n "Who marries who?"
        scene ss99 with dssr
        ay "[name] said he'll marry me."
        scene ss100 with dssa
        d "Right..."
    scene ss103 with dssr
    d "What kind of bar is this anyways? Why's it so empty?"
    scene ss102 with dssa
    pause
    scene ss85 with dssr
    dam "It's a ZPR exclusive college bar and Layla was so nice to invite a few people for a little test run."
    dam "Besides other establishments like libraries, sport centers, and housing. Every college also has their own bar."
    scene ss86 with dssr
    dam "And this is ours. It's not opened yet, though."
    scene ss85 with dssr
    dam "If you're a player for one of the first teams, you do get 50 percent off."
    scene ss84 with dssr
    j "And it will open next week. If we manage to get some titles, our pictures will be in here until the end of time."
    ay "It's a tradition for the more serious colleges to have one."
    scene ss76 with dssr
    ay "AND LAYLA!"
    scene ss77 with dssa
    lay "I'll be right back."
    scene ss104 with dssr
    lay "Yes?"
    scene ss105 with dssa
    ay "And Layla's mommy owns the bar."
    scene ss106 with dssr
    lay "Correct."
    scene ss107 with dssa
    n "And you'll work here?"
    scene ss106 with dssr
    lay "Yes, I'll work here while I study."
    lay "We're still looking for staff. Only ZPR students of course."
    scene ss107 with dssa
    n "Hmm..."
    scene ss87 with dssr
    n "So the college wasn't good enough before?"
    scene ss88 with dssa
    j "It was but in the previous years it failed to meet some regulations. At least that's what Dex told me."
    j "We are now competing with the best of the best."
    scene ss89 with dssa
    j "Provided we don't fail in the playoffs."
    scene ss87 with dssa
    n "You wanna go pro, Jeff?"
    scene ss88 with dssa
    j "Yeah, at least I'll try."
    scene ss109 with dssr
    d "Well, I have to leave now... I need to get ready."
    scene ss110 with dssa
    n "I'll come with you."
    scene ss111 with dssa
    ay "So soon *hick*?"
    scene ss112 with dssr
    n "I need to help [name] before he does something stupid."
    scene ss113 with dssa
    d "Help with what?"
    scene ss114 with dssa
    n "Your date."
    scene ss115 with vpunch
    ay "More drinks for us!"
    scene ss116 with dssa
    j "I don't think you should drink anymore."
    scene ss117 with vpunch
    ay "Fight me, black man!"
    scene ss119 with dssr
    pause
    scene ss118 with dssa
    u "Mh?"
    scene ss120 with dssa
    "He sighs and gets up."
    scene ss122 with dssr
    u "Ayua. Let's go."
    scene ss123 with dssa
    ay "Nooo! I just started warming up!"
    scene ss124 with dssr
    u "I'm taking you home. No discussion."
    scene ss125 with dssa
    ay "That was *hick*- your doing, wasn't it?"
    scene ss121 with dssr
    pause
    stop music fadeout 2.0
    $ persistent.unlockedImageAyua1 = True
    scene black with Dissolve(2)
    with Pause(.5)
    $ persistent.unlockedImageAyua1 = True
    play music "music/Vesky - Departure.ogg"
    scene m1322 with Dissolve(2)
    window hide
    n "So... Why do we sit here?"
    d "What am I doing, Nami?"
    n "Sitting- on the ground?"
    pause
    scene m1323 with dissolve
    pause
    d "I have not been quite myself lately."
    d "I am mentally exhausted."
    scene m1324 with dissolve
    n "Well, you pretty much went from minus 20 percent social activity to 100 percent."
    n "You will get used to it."
    scene m1325 with dissolve
    d "I am thinking about calling my dinner with Bella off."
    scene m1326 with dissolve
    n "No, you should at least try."
    n "...But if you really want to call it off, do it."
    n "You and I can go out and eat something."
    d "That's nice but- *sigh*."
    d "There is no way around this."
    d "I am sick of running away. I have to face my demons."
    scene m1327 with dissolve
    n "Whatever happens, you are not alone."
    n "There are already so many people that found a liking to you."
    n "If there ever was a time to get back to your old self... It's now."
    d "Yeah."
    scene m1329 with dissolve
    n "Will you spend the night with her?"
    scene m1328 with dissolve
    d "No."
    scene m1329 with dissolve
    n "How are you so sure?"
    scene m1328 with dissolve
    d "It's like you don't know me at all."
    scene m1329 with dissolve
    n "What if she intends to?"
    scene m1328 with dissolve
    d "Then I have to tell her off."
    scene m1329 with dissolve
    n "Why?"
    d "Stop being annoying."
    scene m1330 with dissolve
    "You and Nami stare into the distance."
    d "Even if I... wanted to spend the night with her... I don't know if I could get it up."
    n "Your wormy?"
    d "Mhm."
    scene m1331 with dissolve
    n "Can't it get hard at all?"
    scene m1332 with dissolve
    d "I don't know. I'm not trying to spark something."
    scene m1334 with dissolve
    n "This is a real problem."
    n "What about Viagra?"
    d "No! What the fuck?!"
    n "Then just think about Summer... if it comes to it."
    scene m1335 with dissolve
    d "No, you moron!"
    d "*sigh*."
    d "I need to get this out of my head... I want to be normal again.."
    scene m1336 with dissolve
    d "I want to know what it's like to be nervous... That feeling you get when something matters to you."
    d "All I feel at the moment is the fear of losing you or Nojiko."
    d "I can't even remember what real excitement felt like..."
    scene m1337 with dissolve
    n "Maybe you just need to do it."
    n "Just do someone and see what happens!"
    scene m1338 with dissolve
    d "We talked about this... She has to be special."
    if namigym is True:
        n "Maybe Nia?"
        scene m1338 with dissolve
        d "I said special, and not someone with special needs."
        n "Dude..."
        n "She asked us to come over to her place."
        d "Let's not go."
        scene m1341 with dissolve
        n "We can always leave if she gets too weird."
    scene m1338 with dissolve
    d "That reminds me... Nadia asked if we would like to play a board game with them."
    scene m1341 with dissolve
    n "That sounds nice. I always wanted to play something like that!"
    d "There is a meet up soon. You and me can go there.."
    scene m1342 with dissolve
    n "Great, I wanted to get to know Nadia anyway."
    d "Mhm."
    scene m1343 with dissolve
    n "Are you nervous?"
    d "As I said... I want to feel nervous again... but I am not."
    n "It will happen. You just need to be a little more patient."
    d "I'm not in a rush, but it would be nice."
    n "I'll be there for you... Until the end."
    d "...Mhm."
    scene m1344 with dissolve
    pause
    scene m1345 with Dissolve(2)
    $ persistent.unlockedImageNami17 = True
    n "Let's get you ready for tonight."
    stop music fadeout 2.0
    scene black with Dissolve(1.5)
    scene End03 with dissolve
    $ renpy.pause(4.5, hard=True)
    with Pause(139.5)
    scene black with Dissolve(2)
    jump chapter3x5
    call screen EndScreen
    return
