label Foursome4x5A:
    $ persistent.unlockedImageVicCh4x62 = True
    $ Foursome4x5 = True
    scene ae530 with dssb
    pause
    scene ae531 with dssb
    "Mila's eyes dilate and her breath quickens as you gently caress her thighs..."
    scene ae532 with dssb
    pause
    scene ae533 with dssa
    "Vic breaks the kiss and looks up to Mila..."
    scene ae534 with vpunch
    "And before you realize it, Vic pulls herself up and kisses her..."
    "Her heavy breasts rest right on your face."
    scene ae535 with dssb
    pause
    scene ae536 with dssb
    n "Uhhhh...?"
    scene ae538 with dssb
    "Mila gets on her knees, breaking the kiss with Vic..."
    scene ae539 with dssb
    pause
    scene ae540 with dssa
    if BellaKiss3x5 is True:
        "Mila bends over you and kisses you wildly... She puts a lot of passion into her kiss."
    else:
        "Mila bends over you and kisses you gently..."
    scene ae541 with dssb
    pause
    scene ae542 with dssb
    pause
    scene ae544 with dssa
    pause
    scene Foursomex4x5 with dssb
    call screen LewdContinue
label Foursome4x5B:
    scene ae567 with dssb
    pause
    scene ae568 with dssb
    mi "Okay- stop, stop... It was a damn dare for [name] and not- this."
    scene ae569 with dssr
    n "This did go... fun."
    scene ae570 with dssa
    n "*Giggles* Vic, why did you kiss Mila?"
    scene ae571 with dssr
    v "She looked at me like she wanted to be kissed."
    scene ae572 with dssr
    n "I think she wanted to be kissed by [name]."
    scene ae573 with dssa
    v "Oh."
    scene ae574 with dssb
    mi "All good, Vic."
    mi "At least I can now check 'Kissed a girl'."
    $ achievement.grant("Awkward4")
    $ achievement.sync()
    $ persistent.unlockedImageRLFoursome4x5 = True
    jump FourSomeAfterwards


#

label VicTease4x5A:
    $ persistent.unlockedImageVicCh4x66 = True
    $ McPa +=1
    $ VicTiddyTease4x5 = True
    scene VicTease4x5 with dssb
    call screen LewdContinue4x5_VicWalk



label VicTease4x5B:
    if vicdate is True:
        scene ae868 with dssb
        d "Tell me more about it on our date."
    jump VicWalkCon4x5



label MilaKiss4x5A:
    $ persistent.unlockedImageMilaCh4x516 = True
    $ McPa +=1
    if BellaKiss3x5 is True:
        $ McPa +=1
        $ MilaBellaAmour4x5 = True
    $ MilaKiss4x5x = True
    scene ae745 with dssa
    "Her soft lips gently touch yours... A little peek to test the waters."
    scene ae746 with dssa
    "You press your hands together, as you both carefully explore the other's lips."
    scene ae747 with dssa
    "Your hands slowly intertwine and Mila's breathing accelerates slightly."
    scene ae748 with dssa
    "Seemingly out of nowhere, Mila jumps up and you catch her mid air."
    scene ae749 with vpunch
    "You almost lose your footing on the uneven ground that is covered with twigs and stones."
    scene ae750 with dssa
    "The kiss has turned into a passionate dance."
    "Her heavy breasts are pressed against your body, her tongue dances with yours as you try to keep your balance."
    scene ae751 with dssa
    "You move your hands down to her big ass... Her pelvis tenses up as she gently pushes it against you."
    scene ae752 with dssa
    pause
    scene ae753 with dssa
    pause
    scene ae754 with dssa
    pause
    scene ae755 with dssa
    pause
    scene MilaKiss4x5 with dssb
    call screen LewdContinue4x5_MilaWalk

label MilaKiss4x5B:
    scene ae757 with dssb
    pause
    scene ae758 with dssb
    pause
    "You both gently disconnect the kiss..."
    "She's still breathing fast, and her warm breath gently strokes your cheek."
    scene ae760 with dssr
    d "*Whisper* That was nice."
    scene ae759 with dssa
    mi "*Whisper* More than just nice."
    scene ae761 with dssb
    "You both collect your thoughts after this steamy kiss... Taking in the view accompanied by the sound of the leaves and wind."
    scene ae762 with dssb
    pause
    jump MilaKiss4x5Con


label MilaKiss4x5C:
    $ McPa +=1
    $ MilaKiss4x5 = True
    scene ae741 with dssa
    pause
    scene ae742 with dssa
    "Mila gently moves in closer and puts your hand onto the side of her butt."
    scene ae743 with dssa
    pause
    scene ae744 with dssr
    "You can barely see Mila."
    scene ae745 with dssa
    "But you can certainly feel her."
    "Her soft lips gently touch yours... A little peek to test the waters."
    scene ae746 with dssa
    "You press your hands together, as you both carefully explore the other's lips."
    scene ae747 with dssa
    "Your hands slowly intertwine and Mila's breathing accelerates slightly."
    scene ae748 with dssa
    "Seemingly out of nowhere, Mila jumps up and you catch her mid air."
    scene ae749 with vpunch
    "You almost lose your footing on the uneven ground that is covered with twigs and stones."
    scene ae750 with dssa
    "The kiss has turned into a passionate dance."
    "Her heavy breasts are pressed against your body, her tongue dances with yours as you try to keep your balance."
    scene ae751 with dssa
    "You both collect your thoughts after this steamy kiss... Taking in the view accompanied by the sound of the leaves and wind."
    scene ae752 with dssa
    pause
    scene ae753 with dssa
    pause
    scene ae754 with dssa
    pause
    scene ae755 with dssa
    $ achievement.grant("KissMila")
    $ achievement.sync()
    $ KissedGirl = True
    $ persistent.unlockedImageMilaCh4x516 = True
    pause
    scene MilaKiss4x5 with dssb
    call screen LewdContinue4x5_MilaWalk2


label MilaKiss4x5D:
    scene ae757 with dssb
    pause
    scene ae758 with dssb
    "You both gently disconnect the kiss..."
    "She's still breathing fast, and her warm breath gently strokes your cheek."
    scene ae760 with dssr
    d "*Whisper* That was nice."
    scene ae759 with dssa
    mi "*Whisper* More than just nice."
    scene ae761 with dssb
    "You both collect your thoughts after this steamy kiss... Taking in the view accompanied by the sound of the leave and wind."
    scene ae762 with dssb
    pause
    jump MilaKiss4x5Con


label NamiKiss4x5A:
    scene NamiKiss4x5 with dssb
    call screen LewdContinue4x5_NamiKiss

label NamiKiss4x5B:
    $ persistent.unlockedNamiKiss4x5 = True
    scene ae1485 with dssb
    stop music fadeout 3.0
    "Nami starts shaking as you disconnect the kiss."
    scene ae1486 with dssr
    "You leave her room."
    scene ae1487 with dssr
    n "W-what was in that roll?"
    $ achievement.grant("Perception")
    $ achievement.sync()
    scene black with Dissolve(1)
    with Pause(.5)
    play music "music/Suspense/A.W - Darkness Inside.ogg"
    scene ae1488 with dssr
    d "(Calm down... Calm down...)"
    scene ae1489 with vpunch
    $ persistent.unlockedImageNamiCh4x550 = True
    "You're trying to fight off the incoming panic attack."
    if BellaKiss3x5 is True:
        "Until..."
    else:
        scene ae1490 with dssr
        d "I need to get out."
        scene black with Dissolve(2)
        with Pause(.5)
    stop music fadeout 3.0
    if BellaKiss3x5 is True:
        jump BellaEnd4x5
    else:
        jump EndScreen4x5
