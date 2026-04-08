label Foursome4x5A:
    $ persistent.unlockedImageVicCh4x62 = True
    $ Foursome4x5 = True
    "Mila's eyes dilate and her breath quickens as you gently caress her thighs..."
    "Vic breaks the kiss and looks up to Mila..."
    "And before you realize it, Vic pulls herself up and kisses her..."
    "Her heavy breasts rest right on your face."
    n "Uhhhh...?"
    "Mila gets on her knees, breaking the kiss with Vic..."
    if BellaKiss3x5 is True:
        "Mila bends over you and kisses you wildly... She puts a lot of passion into her kiss."
    else:
        "Mila bends over you and kisses you gently..."
    call screen LewdContinue
label Foursome4x5B:
    mi "Okay- stop, stop... It was a damn dare for [name] and not- this."
    n "This did go... fun."
    n "*Giggles* Vic, why did you kiss Mila?"
    v "She looked at me like she wanted to be kissed."
    n "I think she wanted to be kissed by [name]."
    v "Oh."
    mi "All good, Vic."
    mi "At least I can now check 'Kissed a girl'."
    $ achievement.grant("Awkward4")
    $ persistent.unlockedImageRLFoursome4x5 = True
    jump FourSomeAfterwards


#

label VicTease4x5A:
    $ persistent.unlockedImageVicCh4x66 = True
    $ McPa +=1
    $ VicTiddyTease4x5 = True
    call screen LewdContinue4x5_VicWalk



label VicTease4x5B:
    if vicdate is True:
        d "Tell me more about it on our date."
    jump VicWalkCon4x5



label MilaKiss4x5A:
    $ persistent.unlockedImageMilaCh4x516 = True
    $ McPa +=1
    if BellaKiss3x5 is True:
        $ McPa +=1
        $ MilaBellaAmour4x5 = True
    $ MilaKiss4x5x = True
    "Her soft lips gently touch yours... A little peek to test the waters."
    "You press your hands together, as you both carefully explore the other's lips."
    "Your hands slowly intertwine and Mila's breathing accelerates slightly."
    "Seemingly out of nowhere, Mila jumps up and you catch her mid air."
    "You almost lose your footing on the uneven ground that is covered with twigs and stones."
    "The kiss has turned into a passionate dance."
    "Her heavy breasts are pressed against your body, her tongue dances with yours as you try to keep your balance."
    "You move your hands down to her big ass... Her pelvis tenses up as she gently pushes it against you."
    call screen LewdContinue4x5_MilaWalk

label MilaKiss4x5B:
    "You both gently disconnect the kiss..."
    "She's still breathing fast, and her warm breath gently strokes your cheek."
    d "*Whisper* That was nice."
    mi "*Whisper* More than just nice."
    "You both collect your thoughts after this steamy kiss... Taking in the view accompanied by the sound of the leaves and wind."
    jump MilaKiss4x5Con


label MilaKiss4x5C:
    $ McPa +=1
    $ MilaKiss4x5 = True
    "Mila gently moves in closer and puts your hand onto the side of her butt."
    "You can barely see Mila."
    "But you can certainly feel her."
    "Her soft lips gently touch yours... A little peek to test the waters."
    "You press your hands together, as you both carefully explore the other's lips."
    "Your hands slowly intertwine and Mila's breathing accelerates slightly."
    "Seemingly out of nowhere, Mila jumps up and you catch her mid air."
    "You almost lose your footing on the uneven ground that is covered with twigs and stones."
    "The kiss has turned into a passionate dance."
    "Her heavy breasts are pressed against your body, her tongue dances with yours as you try to keep your balance."
    "You both collect your thoughts after this steamy kiss... Taking in the view accompanied by the sound of the leaves and wind."
    $ achievement.grant("KissMila")
    $ achievement.sync()
    $ KissedGirl = True
    $ persistent.unlockedImageMilaCh4x516 = True
    call screen LewdContinue4x5_MilaWalk2


label MilaKiss4x5D:
    "You both gently disconnect the kiss..."
    "She's still breathing fast, and her warm breath gently strokes your cheek."
    d "*Whisper* That was nice."
    mi "*Whisper* More than just nice."
    "You both collect your thoughts after this steamy kiss... Taking in the view accompanied by the sound of the leave and wind."
    jump MilaKiss4x5Con


label NamiKiss4x5A:
    call screen LewdContinue4x5_NamiKiss

label NamiKiss4x5B:
    $ persistent.unlockedNamiKiss4x5 = True
    "Nami starts shaking as you disconnect the kiss."
    "You leave her room."
    n "W-what was in that roll?"
    $ achievement.grant("Perception")
    $ achievement.sync()
    d "(Calm down... Calm down...)"
    $ persistent.unlockedImageNamiCh4x550 = True
    "You're trying to fight off the incoming panic attack."
    if BellaKiss3x5 is True:
        "Until..."
    else:
        d "I need to get out."
    if BellaKiss3x5 is True:
        jump BellaEnd4x5
    else:
        jump EndScreen4x5
