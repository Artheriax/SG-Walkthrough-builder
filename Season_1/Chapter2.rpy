  ## Chapter 2
image cs = Movie (play="Cs.mkv")
image bxn = Movie (play="BxN.mkv")











label report2:
    $ achievement.grant("CH1Finished")
    $ achievement.sync()
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch2_New)
    scene ae1500 with dssb
    pause
    scene ae1501 with dssa
    maj "Is this it?"
    d "Yeah."
    scene ae1502 with dssb
    "As Maja parks the car, you feel a tingle in your throat..."
    scene ae1503 with dssa
    "A sensation runs over your body... Your hair stands up, little pearls of sweat form on your forehead."
    scene ae1504 with dssa
    "It feels as if someone cranked up the heat."
    scene ae1505 with dssb
    "Your heart starts beating faster and faster."
    scene ae1506 with dssr
    d "(Not now... Please... Keep it together, [name]!)"
    scene ae1507 with dssa
    "You close your eyes for a few seconds, you inhale twice... and exhale."
    scene ae1508 with dssa
    "You regain control over yourself."
    scene ae1509 with dssa
    pause
    scene ae1510 with dssb
    pause
    scene ae1511 with dssa
    may "I knew you were a weird dude... But..."
    may "Considering that you almost rocked a panic attack just now... I think there's some stuff you should deal with."
    scene ae1512 with dssa
    "You keep quiet."
    scene ae1513 with dssa
    may "Trust me. I speak from experience."
    scene ae1514 with dssa
    d "Thanks for driving me home."
    scene ae1513 with dssa
    may "You're welcome."
    scene ae1515 with vpunch
    "She stops you from getting out."
    scene ae1516 with dssa
    may "There's... something else."
    scene ae1517 with dssa
    may "*Sigh* And I hate to ask this... But..."
    scene ae1517 with dssa
    may "Could you keep an eye on Victoria?"
    scene ae1515 with dssa
    d "Why?"
    scene ae1516 with dssa
    may "I just want to make sure she's..."
    d "In good hands?"
    scene ae1518 with dssa
    may "Oh no, no... No."
    scene ae1519 with dssa
    may "I just want to make sure she's alright."
    may "So could you please keep an eye on her?"
    scene ae1520 with dssa
    menu:
        "For a favor.":
            $ achievement.grant("MajaFavor")
            $ achievement.sync()
            $ majafavour = True
            $ babysit = True
            d "I really don't like to play the babysitter... but I'll keep an eye on her... For a favor."
            scene ae1523 with dssa
            may "...What kind of favor?"
            scene ae1524 with dssa
            d "We'll get to that when the time comes."
            scene ae1525 with dssa
            may "You're creepy."
            scene ae1526 with dssa
            pause
            scene ae1527 with dssa
            may "Fine."
            d "Alright."
        "...I will.":
            $ babysit = True
            d "I really don't like to play the babysitter... but I'll keep an eye on her..."
            scene ae1522 with dssa
            may "Thank you."
        "Decline.":
            scene ae1521 with dssa
            d "I'm sorry, no."
    scene ae1528 with dssb
    "You open the slightly rusty door, it creeks, and you step outside into the summer breeze."
    scene ae1532 with dssb
    maj "Hey..."
    maj "Just because the camera stopped rolling... It doesn't mean it's not there anymore."
    scene ae1529 with dssb
    "You stand there, quiet... Listening... Thinking..."
    maj "The past... Just because we don't see it anymore, it doesn't mean it's not severely affecting our lives."
    scene ae1530 with dssr
    d "Trust me... My camera is still rolling."
    scene ae1531 with dssr
    maj "I hope you'll get through it."
    scene ae1533 with dssb
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae1534 with dssb
    pause
    scene ae1535 with dssb
    pause
    scene ae1536 with dssb
    d "Hi."
    scene ae1537 with dssa
    m "[name]! How was it?"
    scene ae1536 with dssa
    d "It was... normal?"
    scene ae1538 with dssb
    m "Did you meet some new people?"
    scene ae1541 with dssr
    d "It's a college..."
    scene ae1540 with dssb
    m "But did you interact with them?"
    scene ae1539 with dssa
    d "I talked to a few, yah."
    scene ae1540 with dssa
    m "Where's Nami?"
    scene ae1541 with dssr
    d "She stayed."
    scene ae1542 with dssb
    m "...You didn't just leave?"
    scene ae1543 with dssa
    d "It was completely optional. We didn't need to be there in the first place."
    d "The Cheeto got in trouble, though."
    scene ae1544 with dssa
    m "What did she do?"
    scene ae1545 with dssa
    d "The uniform she wore was from a different college... Some girl fooled Nami."
    m "Oh no..."
    d "And I met Maja."
    m "Who's Maja?"
    d "Victoria's sister."
    scene ae1546 with dssb
    m "Oh!"
    scene ae1547 with dssa
    d "She asked me if I could go with her to see Vic."
    d "Anyways, turns out she's also going to ZPR."
    scene ae1548 with dssb
    "Nojiko quietly looks into the room."
    scene ae1549 with dssa
    m "Victoria and Maja Frohn?"
    scene ae1550 with dssa
    d "I have no idea? I don't remember their last name."
    d "Do you know them?"
    scene ae1551 with dssa
    m "I... do remember a couple who had two girls named Victoria and Maja."
    m "It was the Frohns."
    scene ae1552 with dssa
    d "No idea."
    scene ae1553 with dssr
    d "Alright... I'll leave you to your book."
    scene ae1554 with dssa
    m "One more thing..."
    scene ae1555 with dssa
    m "I... haven't told you and Nami yet but... I have been seeing someone for the past couple of months."
    scene ae1556 with dssa
    d "The Cheeto already suspected something."
    scene ae1555 with dssa
    m "Did she?"
    scene ae1556 with dssa
    d "Yeah."
    scene ae1557 with dssb
    d "And you two are a couple?"
    scene ae1558 with dssa
    m "I guess? Maybe?"
    m "But... I needed to share it with someone."
    m "Please don't tell Nami yet."
    scene ae1557 with dssa
    d "Why?"
    scene ae1559 with dssa
    m "You know how she is."
    m "She'll bombard me with questions until there's nothing left standing."
    m "I'm just not ready to... go that far yet."
    scene ae1560 with dssa
    d "Alright. I won't tell her."
    m "Thanks."
    scene ae1562 with dssb
    pause
    scene ae1561 with dssa
    m "He does want to meet you two soon."
    scene ae1562 with dssa
    d "Does he have children?"
    scene ae1564 with dssa
    m "Yes. Two."
    scene ae1563 with dssa
    d "How are they?"
    scene ae1564 with dssa
    m "I've only seen one of them..."
    scene ae1565 with dssa
    m "She was special to say the least."
    scene ae1566 with dssb
    d "Alright... I'm gonna take a nap."
    scene ae1567 with dssr
    m "And please!"
    m "Keep me in the loop about the college, etc."
    scene ae1568 with dssa
    d "Will do."
    scene ae1569 with dssr
    m "And if you... like a girl, you can bring her over."
    scene ae1570 with dssr
    d "Let's not have 'The Talk'."
    scene ae1571 with dssb
    m "I'm sure you don't need it anymore."
    scene ae1572 with dssb
    pause
    scene ae1573 with dssr
    pause
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_RockPop)
    scene ae1574 with dssb
    pause
    d "(I think the Cheeto is back.)"
    scene ae1575 with vpunch
    n "YOOO!" #bangs into the door
    d "Knock! You cunt!"
    n "What? Afraid I might catch you playing with yourself?"
    scene ae1576 with vpunch
    "She kicks the door closed."
    scene ae1577 with dssb
    n "Why is it always so depressingly dark in your room?!"
    scene ae1578 with dssb
    d "You're so damn annoying."
    scene ae1579 with dssr
    n "How dare you speak the truth!"
    scene ae1580 with dssb
    n "Man, it was fun."
    scene ae1581 with dssr
    pause
    scene ae1582 with dssa
    n "Yo! Show some interest!"
    scene ae1583 with dssr
    d "I'm not interested."
    scene ae1584 with dssb
    d "Stop."
    scene ae1585 with dssb
    "Nami tries to fight you."
    scene ae1586 with dssa
    d "..."
    scene ae1587 with dssa
    n "Man, you're no fun."
    scene ae1588 with dssb
    d "It's boring to wrestle you."
    scene ae1589 with dssa
    d "It always ends the same way... You start it, we wrestle for a few seconds, I win."
    scene ae1590 with vpunch
    n "Oh yeah!? Try me! I've gotten better!"
    scene ae1591 with dssr
    d "Cheeto?"
    scene ae1592 with dssr
    d "Do you want to talk about anything? Otherwise I'm going to kick you out... and rough you up on the way out."
    scene ae1594 with dssb
    n "There's one thing..."
    scene ae1593 with dssb
    n "This Bella bitch..."
    n "I'll work on a plan to avenge myself."
    d "Your plans suck."
    scene ae1595 with vpunch
    n "They don't."
    scene ae1596 with dssa
    n "Remember when I pranked you and Summer?"
    scene ae1597 with dssr
    d "Oh right... yeah... about that...."
    d "It was such an obvious trap, that we just played along."
    d "It was pure pity."
    scene ae1598 with vpunch
    n "You- NO! Liar!"
    scene ae1599 with dssa
    n "I got you two good!"
    d "It was just embarrassing... I was embarrassed to know you."
    scene ae1601 with dssr
    pause
    scene ae1602 with dssa
    n "At first I thought it was going to be a terrible day... I get called out for wearing this uniform and already made an arch enemy."
    n "I'm so glad we met Jeff, Trey and Mila."
    scene ae1603 with dssr
    n "You should have stayed."
    n "You would've seen some tiddies."
    scene ae1604 with dssa
    d "I saw the three topless girls."
    scene ae1605 with dssa
    n "Three?"
    n "There were like twenty."
    scene ae1606 with dssb
    d "I was at Victoria's."
    n "What?!"
    scene ae1607 with dssr
    d "I met Maja at the college... and well, she asked me to see Vic."
    d "She drove me to their house, and we talked a little."
    d "She's also coming to ZPR."
    scene ae1608 with dssr
    n "Amazing! Cutie Vic!"
    scene ae1609 with dssa
    n "Wait, how's she doing?"
    d "I think she's in a wheelchair."
    scene ae1610 with dssa
    n "Oh fuck... Poor girl."
    if babysit is True:
        scene ae1611 with dssa
        d "*sigh* I agreed to keep an eye on her."
        scene ae1612 with dssr
        n "Aww! Sooo nice!"
        scene ae1613 with dssa
        n "You two are so going to marry each other!"
        n "I'll be the number one bride's maid!"
        scene ae1614 with dssr
        n "I'll be like: 'What up, bitches'."
        scene ae1615 with dssa
        n "And drink myself into a coma... cause I'll still be single."
        scene ae1616 with dssa
        d "I'll make sure to film you."
    else:
        scene ae1616 with dssr
        pause
    scene ae1617 with dssr
    n "Still, still, still... I was pleasantly surprised to hear that Trey and the others thought you're a social dude."
    n "How did you manage to do that?"
    scene ae1618 with dssa
    d "I initiated a conversation."
    scene ae1617 with dssa
    n "How so?"
    scene ae1618 with dssa
    d "When I first entered the college I... I felt some kind of drive... The drive to jump over my 'obstacles.'"
    d "I totally regret it now."
    scene ae1619 with dssa
    n "I'm proud of you."
    scene ae1620 with dssr
    d "Alright Cheeto, fuck off now... I need a nappy."
    scene ae1621 with vpunch
    n "Yo, naps are for weak people!"
    scene ae1622 with vpunch
    n "ARE YOU WEAK?!"
    d "Cheeto... Get out."
    scene ae1623 with dssb
    n "That's what I thought!"
    stop music fadeout 1.0
    scene ae1624 with dssb
    $ play_playlist(playlist_AmbientNamiLake)
    pause
    d "(Thanks for closing the curtains...)"
    scene ae1625 with dssr
    pause
    scene ae1628 with dssr
    pause
    d "(...I'm not ready.)"
    scene ae1625 with dssb
    pause
    scene ae1626 with vpunch
    pause
    scene ae1627 with dssr
    pause
    stop music fadeout 2.0
    scene ae2484 with dssb
    pause
    scene ae2485 with dssb
    "You open the curtains a little and sit there completely still for a few seconds... listening to your surroundings."
    scene ae2486 with dssr
    d "(Seems like the others are still asleep.)"
    scene ae2487 with dssa
    d "(I slept for 13 hours... I feel like shit.)"
    scene ae2488 with dssa
    d "(I need some air...)"
    scene black with Dissolve(2)
    $ play_playlist(playlist_WatchingStars)
    with Pause(.5)
    scene ae1629 with dssb
    pause
    scene ae1630 with dssr
    pause
    scene ae1631 with dssa
    pause
    "Distant sounds from the city... A weak, chilly breeze goes over your body."
    d "(It's been a day and the excitement has already faded.)"
    scene ae1632 with dssb
    pause
    scene ae1633 with dssa
    pause
    scene ae1634 with dssb
    pause
    scene ae1635 with dssr
    pause
    scene ae1636 with dssr
    pause
    scene ae1637 with dssr
    pause
    scene ae1638 with dssr
    pause
    scene ae1639 with dssr
    pause
    scene ae1641 with dssr
    pause
    scene ae1642 with dssa
    m "Do you want to talk about it?"
    d "I don't even know what it is."
    scene ae1643 with dssb
    m "You're transitioning into a new phase of your life."
    m "Many say that college is the best time of your life."
    scene ae1644 with dssa
    d "I don't even know why I'm going to college..."
    scene ae1643 with dssa
    m "So why did you say yes when I asked you?"
    scene ae1645 with dssr
    d "I had nothing else."
    scene ae1646 with dssr
    "Noji stays quiet."
    pause
    scene ae1647 with dssb
    m "You should-"
    scene ae1648 with dssa
    d "Please don't send me to the bakery again."
    scene ae1649 with dssa
    m "*Chuckles* I won't."
    scene ae1650 with dssb
    pause
    scene ae1652 with dssb
    m "You're tense."
    scene ae1651 with dssa
    d "I'm not looking forward to today."
    scene ae1652 with dssa
    m "Anything in particular?"
    scene ae1651 with dssa
    d "The people."
    d "I made a mistake."
    scene ae1653 with dssa
    m "Did you make enemies?"
    scene ae1654 with dssa
    d "Worse."
    d "I had a rare breeze of 'drive'... and talked to some people."
    d "I hope they don't think we're friends now."
    scene ae1655 with dssa
    m "I hope you are! That's great!"
    if majafavour or babysit is True:
        scene ae1658 with dssr
        d "But even worse... I told Maja I would keep an eye on Victoria."
        scene ae1657 with dssa
        m "That's amazing!"
        m "It'll teach you some valuable skills."
    else:
        scene ae1657 with dssr
    m "This must all be quite overwhelming for Victoria."
    scene ae1659 with dssa
    d "Not just for her."
    scene ae1660 with dssa
    m "Go inside and get yourself a coffee."
    m "I'll stop by the bakery during my run."
    scene ae1661 with dssb
    pause
    scene ae1662 with dssr
    pause
    scene ae1663 with dssr
    pause
    scene ae1664 with dssr
    pause
    scene ae1665 with vpunch
    "Nojiko squeeks and jumps up."
    stop music fadeout 2.5
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch2_Coffee)
    scene ae1667 with dssb
    d "Cheeto? Are you in there?"
    scene ae1668 with dssb
    pause
    n "Yes."
    d "I need to shower."
    n "*Mumbles* Come in!"
    scene ae1669 with dssb
    menu:
        "Go in and shower with Nami being present.":
            $ NojiVer +=1
            $ ShowerNami01 = True
            $ NamiWiggly1x0 = True
            scene ae1670 with dssb
            $ persistent.unlockedImageNami_CH2_1 = True
            pause
            scene ae1671 with dssr
            n "*Humming* Mhhhhh Mhhhhiiiii."
            scene ae1683 with dssr
            n "Your butt is small."
            d "Stop perving on me. Weirdo."
            scene ae1684 with dssr
            n "Bibi Butt!"
            scene ae1685 with dssb
            n "So, remember high school?"
            scene ae1686 with dssb
            n "Like... I was so shocked yesterday."
            n "In high school I was able to compete... but now?!"
            d "Cheeto, what're you talking about?"
            scene ae1687 with vpunch
            n "Tiddies! To me, it just seems like their boobs are so much bigger!"
            n "What's up with that?!"
            scene ae1688 with dssa
            d "Welcome to the big league."
            scene ae1689 with dssa
            n "I'm not gonna lie... I was a little bummed out by that."
            n "I was a NINE AND A HALF at our high school!"
            scene ae1690 with dssa
            n "Now I'm a funny seven."
            scene ae1691 with dssa
            d "You can indeed be funny."
            scene ae1692 with vpunch
            m "Nami?"
            scene ae1693 with dssr
            n "...Yes?"
            m "Where's [name]?"
            scene ae1694 with dssa
            n "In the shower."
            m "Are you in there together?!"
            scene ae1695 with dssa
            n "What?! No!"
            n "I'm just doing my morning routine!"
            m "Well- open the door."
            scene ae1696 with dssr
            pause
            scene ae1697 with dssr
            pause
            scene ae1698 with dssa
            m "Breakfast is done."
            scene ae1699 with dssa
            n "Great."
            n "Make sure it doesn't run away. I'm not done with my routine yet."
            scene ae1700 with vpunch
            pause
            scene ae1701 with dssb
            pause
            scene ae1702 with dssa
            n "Man... She and her stupid 'No funny business between roommates' rule."
            d "*Sarcastic* Yeah, I wonder where it came from..."
            scene ae1703 with dssa
            n "Hey! Was it unfortunate that I pushed my boob into your face that one time?"
            n "Yes!"
            scene ae1704 with dssa
            n "But was there any real intention behind it?! No!"
            scene ae1705 with dssa
            d "You said 'I'll make you eat them!'"
            scene ae1706 with dssr
            pause
            scene ae1707 with dssa
            n "Oh my... I did."
            scene ae1708 with dssr
            n "I'm a weirdo!"
            scene ae1709 with dssr
            "She starts doing some weird form of belly dance that reminds you of a worm that's trying to stand up, but keeps wiggling around."
            scene ae1710 with dssa
            n "*Chants* Weirdo! Weirdo! Weirdo!"
            scene ae1711 with dssb
            pause
            scene ae1712 with dssr
            pause
            scene ae1713 with dssb
            n "I call it 'The Wiggly!'"
            scene ae1714 with dssb
            "You leave the bathroom."
            scene TheWiggly with dssa
            pause
            $ achievement.grant("TheWiggly")
            $ achievement.sync()
        "Just pee and leave immediately":
            scene ae1670 with dssb
            pause
            scene ae1671 with dssr
            pause
            n "*Humming* Mhhhhh Mhhhhiiiii."
            scene ae1672 with dssr
            n "Your butt is small."
            scene ae1673 with dssr
            d "Stop perving on me. Weirdo."
            n "Bibi Butt!"
            scene ae1674 with dssr
            pause
            n "So, remember high school?"
            scene ae1675 with dssr
            n "Like... I was shocked yesterday."
            n "In High school I was able to compete... but now?!"
            d "Cheeto, what're you talking about?"
            scene ae1676 with vpunch
            n "Tiddies! To me, it just seems like their boobs are so much bigger!"
            n "What's up with that?!"
            d "Welcome to the big league."
            scene ae1677 with dssb
            n "I'm not gonna lie... I was a little bummed out by that."
            n "I was a NINE AND A HALF at our high school!"
            scene ae1679 with dssr
            n "Now I'm a funny seven."
            scene ae1678 with dssa
            d "You can indeed be funny."
            scene ae1680 with dssr
            d "Later Cheeto."
            scene ae1681 with dssa
            n "Didn't you wanna shower?"
            d "I'll do it later."
            scene ae1682 with dssb
            pause
    scene black with Dissolve(2)
    with Pause(0.5)
    scene ae1716 with dssb
    pause
    scene ae1717 with dssr
    pause
    scene ae1718 with dssa
    pause
    scene ae1719 with dssr
    n "Noji... I need new tampons."
    scene ae1720 with dssr
    d "Ugh! I'm eating!"
    scene ae1725 with dssr
    m "Be quiet [name]. It's something totally normal."
    scene ae1720 with dssr
    d "That doesn't make it less disgusting!"
    scene ae1721 with dssa
    n "Shut up or I'll give you a red slap!"
    scene ae1722 with dssa
    m "Nami..."
    scene ae1723 with dssa
    if jeff == 1:
        n "Are we-"
        scene ae1724 with dssr
        "The doorbell rings."
        $ fitness +=1
        scene ae1726 with dssr
        m "Is anyone expecting someone?"
        scene ae1740 with dssr
        n "No."
        scene ae1741 with dssr
        pause
        scene ae1742 with dssr
        pause
        scene ae1743 with dssr
        pause
        scene ae1744 with dssr
        j "Good morning."
        scene ae1744 with dssr
        n "Jeff?"
        scene ae1745 with dssr
        j "Hey Nami!"
        scene ae1746 with dssr
        j "[name]."
        d "Hi."
        scene ae1748 with dssr
        d "What brings you here?"
        scene ae1749 with dssa
        j "You bring me here! It's time to go to the gym."
        j "We need to surprise your non-existent muscles! They don't expect an ambush in the morning."
        scene ae1750 with dssr
        d "..."
        scene ae1751 with dssr
        pause
        scene ae1752 with dssr
        d "You're kidding?"
        scene ae1753 with dssr
        j "*Chuckles* Not at all."
        scene ae1754 with dssa
        pause
        scene ae1759 with dssr
        m "Can I get you something to drink?"
        scene ae1760 with dssa
        j "No, but thank you very much!"
        scene ae1758 with dssr
        n "I'll come with you guys!"
        scene ae1755 with dssr
        j "Sorry Nami."
        j "Today is [name]'s day. You'll be next."
        j "I can only really take care of one of you."
        n "Tzz."
        scene ae1756 with dssr
        d "Just so you know... I'm totally not into this right now."
        d "I'll get ready... But just so you know."
        scene ae1757 with dssr
        j "I'd be surprised if you were."
        scene black with Dissolve(2)
        with Pause(.5)
        jump Gym2x0
    else:
        n "So Noji... How's work?"
        scene ae1725 with dssr
        m "It's decent."
        d "That translates to 'It sucks.'"
        scene ae1727 with dssb
        m "Precisely."
        scene ae1728 with dssa
        d "Quit your job."
        scene ae1729 with dssr
        m "'Quit your job'."
        m "[name]... Why haven't I thought about that?"
        scene ae1730 with dssr
        d "Because you think you need to please society and what it expects of you?"
        scene ae1731 with dssa
        n "This coffee-"
        scene ae1732 with dssa
        m "What makes you think I'm being pressured into this?"
        scene ae1733 with dssa
        d "You're miserable. After your old boss left, your situation there took a turn for the worse."
        scene ae1734 with dssa
        m "I'm not going to deny that my situation has changed since Scarlet retired."
        m "However, I'm very much capable of analyzing my current situation and how it affects me."
        scene ae1735 with dssa
        m "The problem is, that you forgot to add an element to your equation."
        m "We have bills to pay."
        scene ae1739 with vpunch
        n "Stoooop ruining my morning!"
        "An awkward silence comes in."
        scene ae1736 with dssa
        d "Your well-being is more important than some comfort."
        scene ae1737 with dssa
        m "It's important to me that I can provide some comfort."
        scene ae1738 with dssr
        d "(Always trying to prove something to herself.)"
        scene black with Dissolve(2)
        with Pause(.5)
        jump bus02


label bus02:
    scene ae2456 with dssb
    pause
    scene ae2457 with dssa
    d "Tell me when it's our stop."
    n "We'll just get out when everyone else gets out."
    scene ae2458 with dssa
    d "Why did you change clothes again?"
    n "I felt ugly."
    scene ae2459 with dssa
    pause
    scene ae2460 with dssa
    n "So, I didn't take a close look yesterday, but I'm sure their selection of rolls was miserable to say the least..."
    scene ae2461 with dssa
    d "What?"
    scene ae2460 with dssa
    n "The Mensa. I only saw one decent type of roll. It's a disgrace for such a prestigious college."
    n "I'll talk to the person responsible."
    scene ae2462 with dssr
    d "You sound like a Karen."
    scene ae2463 with dssa
    n "How da-..."
    scene ae2466 with dssa
    n "Oh god... I do!"
    scene ae2465 with vpunch
    n "Pull it out of me! FAST!"
    scene ae2467 with dssa
    d "Sit down."
    scene ae2468 with dssa
    n "Hehe... Am I embarrassing you?"
    d "You're embarrassing yourself."
    scene ae2469 with dssa
    n "*Whisper* Is that why people laugh at me?"
    scene ae2470 with dssa
    d "Yeah."
    d "But it's also the reason people tend to like you."
    scene ae2468 with dssr
    n "I'll take that trade!"
    scene black with Dissolve(2)
    with Pause(.5)
    jump College2x0


label Gym2x0:
    scene ae1761 with dssb
    "You and Jeff arrive at the college gym."
    scene ae1762 with dssb
    d "Do you always train at this hour?"
    j "Usually."
    j "I hate it when these Aurora-athletes lock down the stations."
    scene ae1763 with dssr
    "You turn off the treadmill."
    scene ae1764 with dssr
    d "Alright, we'll start with legs?"
    scene ae1765 with dssr
    "Jeff stares at you."
    scene ae1766 with dssr
    j "You've worked out before, didn't you?"
    d "Yes."
    scene ae1767 with dssa
    j "I'm lowkey proud you mentioned legs... Many tend to skip them."
    d "It's stupid."
    d "Training legs releases a lot of growth hormones."
    scene ae1768 with dssr
    pause
    scene ae1770 with dssr
    j "What happened to you? Why are you so out of shape."
    scene ae1771 with dssr
    pause
    scene ae1772 with dssa
    pause
    scene ae1773 with dssa
    j "Sorry, I didn't want to dig."
    d "It's alright."
    scene ae1774 with dssb
    d "I'll need your help. I'm not sure how my technique is."
    scene ae1775 with dssa
    pause
    scene ae1776 with dssa
    j "Oh yeah... Yeah... That needs to be fixed."
    scene ae1777 with dssb
    pause
    scene ae1778 with dssa
    pause
    scene ae1779 with dssa
    pause
    scene ae1780 with dssa
    pause
    scene ae1781 with dssb
    j "Go."
    scene ae1782 with dssa
    pause
    scene ae1783 with dssa
    pause
    scene ae1782 with dssa
    pause
    scene ae1784 with vpunch
    pause
    scene ae1785 with dssa
    j "Two more."
    scene ae1784 with vpunch
    pause
    scene ae1785 with dssa
    j "Two more."
    scene ae1786 with vpunch
    d "F-fuck you."
    scene ae1787 with dssa
    j "Two more."
    scene ae1788 with vpunch
    d "Ngrrrrrrh..."
    scene ae1787 with dssa
    pause
    scene ae1786 with vpunch
    pause
    scene ae1789 with vpunch
    pause
    scene ae1790 with dssb
    j "Impressive."
    j "But that was too much, dude."
    scene ae1791 with dssa
    d "What? You kept saying 'Two more'!"
    scene ae1792 with dssr
    j "Yeah, but I never thought you'd actually keep going."
    j "That's some serious willpower... Considering the circumstances under which you're here."
    scene ae1793 with dssa
    d "What now?"
    scene ae1794 with dssa
    j "Let's get chest out of the way."
    d "Bench?"
    scene ae1795 with dssa
    j "Bench."
    scene ae1796 with vpunch #bella grace mesa musik
    pause
    scene ae1797 with dssr
    pause
    j "...I had hoped we'd be alone."
    scene ae1798 with dssr
    d "Who cares about her."
    scene ae1799 with dssa
    pause
    scene ae1800 with dssb
    j "I have to make a call. Wait for me."
    j "It won't take long."
    scene ae1801 with dssr
    pause
    scene ae1802 with dssr
    with Pause(.5)
    menu:
        "Wait for Jeff.":
            $ bellathreat = False
            $ bellasafe = False
            scene black with Dissolve(2)
            with Pause(.5)
        "Don't waste time and train without his supervision.":
            $ bellathreat = False
            $ bellasafe = True
            scene ae1803 with dssr
            pause
            scene ae1804 with dssr
            pause
            scene ae1805 with dssr
            pause
            play music "music/Suspense/Scott Buckley - Resonance.ogg"
            scene ae1806 with vpunch
            d "(Oh, I fucked up.)"
            scene ae1807 with dssa
            "The weight slams slightly on your chest..."
            scene ae1808 with vpunch
            d "(I can't get it up! Idiot me put on the safety clips!)"
            scene ae1809 with dssr
            pause
            scene ae1810 with dssr
            pause
            scene ae1811 with dssr
            "You both struggle with the weight."
            scene ae1812 with dssr
            "But together you manage to get the bar back up."
            scene ae1814 with dssr
            b "How stupid can a person be?!"
            scene ae1813 with dssa
            d "*Cough*"
            menu:
                "Thank her.":
                    scene ae1815 with dssa
                    b "Whatever, moron."
                    scene ae1818 with dssb
                    pause
                    scene ae1819 with dssr
                    b "At least keep the safety clips off, so you can slide the plates down in case of emergency."
                    scene ae1820 with dssa
                    d "I thought I could handle it."
                    scene ae1821 with dssa
                    b "Have you looked at yourself?"
                    scene ae1822 with dssr
                    b "Hey! I have no driver's license but let me drive the fastest car available! That'll go well."
                    b "Why should I slowly work myself up-"
                    scene ae1823 with dssr
                    d "Are you done?"
                    scene ae1824 with dssr
                    b "Oh, I have a few more."
                    d "Just fuck off."
                    scene ae1825 with dssa
                    b "Go fuck yourself."
                    stop music fadeout 2.0
                "I'd rather have died than getting saved by you.":
                    scene ae1817 with dssr
                    b "Oww..."
                    b "If I were you... I'd consider ending it... You wouldn't want to live with that shame, would you?"
                    scene ae1818 with dssb
                    pause
                    stop music fadeout 2.0
            scene black with Dissolve(2)
            with Pause(.5)
            scene ae1826 with dssb
            j "Ready."
            scene ae1827 with dssr
            d "Yeah."
            stop music fadeout 2.0
        "Threaten Bella.":
            $ bellathreat = True
            scene ae1828 with dssb
            pause
            scene ae1829 with dssr
            play music "music/Suspense/Scott Buckley - Resonance.ogg"
            pause
            scene ae1830 with vpunch
            b "Nghh!"
            scene ae1831 with dssa
            d "Listen..."
            d "You see... ahhh... what did I want to say again..."
            scene ae1833 with dssb
            d "Mhmmm mmmmm... No that wasn't it."
            scene ae1834 with dssr
            "Bella's struggling hard beneath the weight of the bar."
            scene ae1835 with dssa
            d "Oh! Right!"
            d "I remember..."
            scene ae1836 with dssr
            d "Don't you dare hurt Nami again..."
            scene ae1837 with dssa
            b "NGH!"
            scene ae1838 with dssa
            d "Oh! Girl! Lemme help you with that."
            scene ae1839 with dssa
            "You help lift the bar and she gasps for air."
            scene ae1840 with dssa
            d "You dummy, you shouldn't underestimate the weights."
            scene ae1841 with dssb
            d "*Serious* Stay on your level."
            scene ae1842 with dssa
            b "Y-you fucking asshole."
            b "I'll-"
            scene ae1843 with dssr
            d "Exactly, you'll now take more care not to get stuck in an unfortunate situation."
            scene ae1844 with dssr
            pause
            stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_BellaDate)
    scene ae1845 with vpunch
    pause
    scene ae1846 with dssr
    j "How did it feel?"
    scene ae1847 with dssa
    d "Good. I can already feel the muscle again."
    j "That's good."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae1849 with dssb
    pause
    scene ae1848 with dssr
    pause
    j "You did very well. I'm impressed."
    scene ae1850 with dssa
    d "Thanks."
    scene ae1851 with dssb
    pause
    scene ae1852 with dssa
    j "You almost fooled me yesterday."
    d "Mh?"
    scene ae1860 with dssr
    j "I thought you were an open dude, ya know?"
    scene ae1853 with dssr
    d "I assume the Cheeto spoiled it."
    scene ae1860 with dssr
    j "Not directly."
    j "Your eyes tell."
    j "You've got sad eyes."
    scene ae1862 with dssr
    d "I could say the same about you."
    scene ae1861 with dssa
    j "It takes one to know one."
    scene ae1854 with dssb
    pause
    scene ae1855 with dssr
    j "What do you think of Mila?"
    scene ae1856 with dssa
    d "I have no opinion of her."
    scene ae1857 with dssa
    j "She found you interesting."
    scene ae1856 with dssa
    d "A certain type of lost girl usually does."
    scene ae1857 with dssa
    j "Hey, she's not lost."
    scene ae1858 with dssr
    d "I don't know."
    d "She's nice, I guess."
    scene ae1859 with dssr
    d "How come these showers are unisex?"
    j "I have no idea."
    j "But don't worry, nobody's going to look at your dong."
    menu:
        "I wouldn't care.":
            $ JeffConfidence2x0 = True
            j "Confidence. I like it."
        "Good.":
            pass
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae1864 with dssb
    pause
    scene ae1863 with dssr
    j "You have a good body structure. Wide shoulders, small waist."
    scene ae1865 with dssa
    d "Thanks, I guess."
    scene ae1866 with dssb
    j "How do you feel?"
    d "Tired."
    j "That'll change as soon as your energy levels have increased their capacity."
    scene ae1867 with dssr
    pause
    scene ae1868 with dssa
    j "Another thing."
    j "Be careful with Bella."
    scene ae1869 with dssa
    d "Why?"
    scene ae1868 with dssa
    j "She's... unstable."
    j "I don't want anyone to get hurt."
    scene ae1870 with dssr
    menu:
        "I don't think she's that bad." if bellasafe is True:
            $ BellaNotBad2x0 = True
            scene ae1871 with dssa
            j "Really?"
            d "Yeah. She's a cunt, don't get me wrong."
            d "But a cunt that might not be as cunty as many people think she is."
        "I'll be careful.":
            scene ae1873 with dssa
            j "Good."
        "I'm not afraid of her.":
            scene ae1872 with dssr
            j "I'm not saying you are... I'm just saying that you should keep it cool."
            j "Enemies just distract you from what's really important."
            d "And what's that?"
            scene ae1873 with dssa
            j "Achieving your dreams."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae1874 with dssb
    pause
    scene ae1876 with dssr
    j "Next time I'll bring Nami to the gym."
    j "I'll see you later."
    scene ae1875 with dssr
    d "Yeah. Thanks for... this here."
    scene ae1877 with dssr
    j "No problem."
    j "If you need any help, don't hesitate to ask me."
    scene ae1878 with dssr
    j "...As long as you put in the work."
    scene ae1879 with dssa
    pause
    scene ae1880 with dssb
    pause
    scene ae1881 with dssr
    pause
    stop music fadeout 2.5
    scene black with Dissolve(2)
    with Pause(.5)
    $ achievement.grant("GymBros")
    $ achievement.sync()
    jump CollegeGymEntrance2x0



label CollegeGymEntrance2x0:
    $ play_playlist(playlist_Ch2_New)
    $ PunchPrefect2x0 = True
    scene ae1882 with dssb
    pause
    d "...Where the fuck am I?"
    scene ae1883 with dssr
    pause
    scene ae1884 with dssa
    pause
    scene ae1885 with dssa
    pause
    scene ae1886 with dssa
    d "(Something's not right.)"
    scene ae1887 with dssa
    "Your body heats up, sweat breaks out."
    "Loud noises clutter your mind."
    scene ae1888 with dssr
    "Your chest tightens, your heart pounds..."
    scene ae1889 with dssr
    d "(Fuck. Not here!)"
    scene ae1890 with dssa
    "Luckily, you spot a classroom... and hope that it's empty."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    $ play_playlist(playlist_Jaccuzi)
    with Pause(.5)
    scene ae1915 with dssb
    pause
    scene ae1916 with dssr
    "*Breathing heavily."
    scene ae1917 with dssr
    pause
    d "(Come on! This hasn't happened in forever!)"
    scene ae1919 with dssr
    "Your heart rate normalizes and the dizziness fades away."
    scene ae1920 with dssr
    u "Do I need to call someone?"
    scene ae1921 with dssr
    d "No."
    scene ae1922 with dssa
    "You get back up, straighten your clothes, and head back into the now much emptier corridor."
    scene ae1891 with dssb
    pause
    scene ae1892 with dssa
    pause
    scene ae1893 with dssr
    u "Hey! You!"
    scene ae1894 with dssa
    pause
    scene ae1896 with vpunch
    u "What were you doing in there?"
    scene ae1897 with dssa
    d "Nothing."
    scene ae1898 with dssa
    u "I'm a ZPR Prefect-"
    scene ae1899 with vpunch
    u "Ugh! You're sweaty. Oh god, did you masturbate in there?!"
    scene ae1900 with dssr
    "You shake your head and go your way."
    scene ae1901 with vpunch
    "But the guy stops you again."
    scene ae1902 with dssa
    u "Come with me! I'll have to report you and get that classroom clea-"
    scene ae1903 with vpunch
    pause
    scene ae1904 with vpunch
    "The guy immediately hits the ground."
    scene ae1905 with dssb
    pause
    scene ae1906 with dssa
    "You increase your pace and get out of there."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ achievement.grant("PunchPrefect")
    $ achievement.sync()
    $ play_playlist(playlist_Ch2_New)
    scene ae1941 with dssb
    pause
    scene ae1942 with dssr
    d "(...I can't let my temper get out of control again!)"
    scene ae1944 with dssr
    pause
    scene ae1945 with dssr
    "You spot someone familiar."
    scene ae1946 with dssa
    pause
    scene ae1947 with dssa
    d "H-hey Mila."
    mi "Hi [name]."
    scene ae1954 with dssr
    pause
    scene ae1955 with dssa
    d "Please no- no hug."
    mi "Oh- okay."
    mi "Are you okay?"
    d "Would you mind me lying and going with it?"
    "She takes a second to answer."
    mi "Just this once."
    scene ae1961 with dssb
    mi "I was heading to class."
    d "Let's go together."
    scene ae1962 with dssa
    mi "*Suspicious* Sure."
    scene ae1964 with dssr
    pause
    scene ae1965 with dssr
    mi "You don't know where it is, huh?"
    scene ae1966 with dssa
    "You give her a subtle smile."
    scene black with Dissolve(2)
    with Pause(.5)
    jump classroom2x0






label College2x0:
    scene ae1907 with dssb
    pause
    scene ae1908 with dssr
    d "Do you know where it is?"
    scene ae1909 with dssa
    n "Yeah, just follow my ass."
    scene ae1910 with dssr
    pause
    scene ae1911 with dssr
    pause
    scene ae1883 with dssr
    stop music fadeout 5.0
    d "Great..."
    scene ae1884 with dssr
    d "(I lost the Cheeto.)"
    scene ae1885 with dssr
    pause
    scene ae1886 with dssa
    d "(Something's not right.)"
    scene ae1887 with dssr
    "Your body heats up, sweat breaks out."
    scene ae1888 with dssr
    "Your chest tightens, your hearts pounds..."
    scene ae1889 with dssr
    pause
    scene ae1912 with vpunch
    n "Yo."
    n "I thought the crowd had swallowed you."
    scene ae1912 with dssa
    pause
    scene ae1914 with dssa
    pause
    scene ae1913 with dssa
    $ play_playlist(playlist_Jaccuzi)
    n "Yo, what's up?"
    scene ae1923 with dssb
    "Nami pushes you into an empty classroom."
    pause
    n "Yo?"
    scene ae1924 with dssa
    d "...I think I almost had a panic attack."
    n "Why?"
    d "I don't know!"
    scene ae1925 with dssb
    d "I almost had one yesterday too..."
    n "Do I need to get help?"
    d "No."
    d "Let's just stay here for a minute."
    pause
    scene ae1926 with dssr
    "Nami gently caresses your hair."
    scene ae1927 with dssr
    n "When was the last time this happened?"
    scene ae1928 with dssa
    d "Over two years ago."
    d "I don't know why it's happening again..."
    scene ae1929 with dssr
    pause
    scene ae1930 with dssa
    n "I could think of something... There's a barrage of sensory impressions out there."
    scene ae1931 with dssr
    d "...I was able to handle it yesterday..."
    scene ae1932 with dssr
    pause
    scene ae1933 with dssr
    pause
    scene ae1934 with dssa
    d "Alright... I'm alright."
    scene ae1935 with dssr
    n "You sure?"
    scene ae1936 with dssa
    d "Yeah."
    scene ae1937 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae1898 with vpunch
    u "Hey!? What did you do in there?"
    scene ae1897 with dssa
    d "Nothing."
    scene ae1899 with dssa
    u "You're sweaty. Did you masturbate in there?!"
    scene ae1900 with vpunch
    n "Hey!"
    scene ae1938 with dssr
    n "He didn't do anything!"
    scene ae1939 with dssa
    "He blushes as he spots Nami."
    u "Oh. I'm sorry... I- I thought... Nevermind."
    scene ae1940 with dssr
    pause
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch2_New)
    scene ae1941 with dssb
    pause
    scene ae1943 with dssr
    pause
    scene ae1944 with dssr
    pause
    scene ae1946 with dssr
    n "Yo Mila!"
    scene ae1947 with dssa
    mi "Hi!"
    scene ae1948 with dssa
    n "How's it going?"
    scene ae1950 with dssr
    mi "Good, good, you?"
    n "Good!"
    scene ae1949 with dssa
    mi "Hey [name]!"
    scene ae1953 with dssr
    pause
    scene ae1956 with dssa
    d "No hug... Please."
    scene ae1952 with dssa
    mi "Oh, sorry!"
    scene ae1957 with dssr
    n "*Whisper* He's allergic to bodies."
    scene ae1958 with dssa
    mi "*Whisper* Oh. Sounds serious."
    scene ae1959 with dssa
    "They chuckle."
    scene ae1960 with dssr
    mi "Wanna head to class?"
    n "Sure!"
    scene black with Dissolve(2)
    with Pause(.5)


label classroom2x0:
    if PunchPrefect2x0 is True:
        scene ae1967 with dssb
        "You and Mila sit down at the edge."
    else:
        scene ae1968 with dssb
        "You and Mila sit down at the edge, while Nami keeps walking."
    scene ae1969 with dssr
    pause
    if PunchPrefect2x0 is False:
        scene ae1970 with dssr
        "Nami suddenly realizes you and Mila didn't follow."
    else:
        "Nami spots you at the other side of the room."
    scene ae1972 with dssa
    pause
    scene ae1971 with dssa
    na "*Muffled* Pew."
    scene ae1973 with vpunch
    pause
    scene ae1974 with dssb
    ma "Good morning."
    ma "I hope everyone found their way here."
    scene ae1975 with dssr
    "She lets her gaze wander through the room."
    scene ae1976 with dssa
    "And it lasts unusually long on you."
    scene ae1978 with dssa
    d "(Wait... Is that the woman that caused Victoria's accident?)"
    scene ae1979 with dssr
    "Miss Marla tries to regain composure and nervously fiddles around with her blouse."
    scene ae1979 with dssa
    ma "I-  uh- well, we uh usually start the freshman year with a group project."
    scene ae1980 with dssa
    ma "I will..."
    scene ae1981 with dssa
    ma "One second, I need to drink something."
    scene ae1982 with dssa
    mi "She's acting weird?"
    scene ae1983 with dssa
    d "Mhm."
    scene ae1982 with dssa
    mi "She's probably just as nervous as we are."
    scene ae1984 with dssb
    ma "Okay..."
    scene ae1985 with dssb
    ma "I'll assemble the groups. They'll be made out of two students each. The groups will change throughout the year."
    ma "Giving you the opportunity to work with, and get to know the people in your class."
    scene ae1986 with dssa
    ma "Victoria, you'll get together with Mila."
    d "(Vic's here?)"
    scene ae1987 with dssb
    v "Sure!"
    scene ae1988 with dssb
    "Victoria looks over to you and Mila."
    scene ae1989 with dssa
    "Victoria smiles brightly as she spots you looking at her."
    scene ae1999 with dssr
    mi "*Whisper* Aww! Look at her... I think she likes you."
    scene ae1993 with dssb
    ma "Nami, I'll assign you to Ayua."
    scene ae1992 with dssa
    "Nami nods weirdly."
    ma "Sonya, I'll put you together with Nadia."
    scene ae1990 with dssb
    pause
    d "(I haven't seen her before.)"
    scene ae1991 with dssa
    mi "Oh."
    ma "Jeff, you and Trey."
    scene ae1994 with dssb
    ma "[name] you and-"
    scene ae1995 with vpunch
    ma "Bella."
    scene ae1996 with dssa
    pause
    scene ae1997 with dssa
    b "Ugh."
    b "Can I have a different partner?"
    scene ae1998 with dssa
    ma "No."
    scene ae2000 with dssr
    mi "Oh man, sorry [name]."
    scene ae2001 with dssa
    d "I'll be fine."
    scene ae2002 with dssb
    ma "Let's go through some fundamental aspects of this class."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch1CollegeEnd)
    scene ae2005 with dssb
    "While Miss Marla dictates something about biological procedures..."
    scene ae2011 with dssr
    "Yours and Bella's eyes meet occasionally."
    scene ae2012 with dssa
    pause
    d "(I'm not looking away.)"
    scene ae2008 with dssr
    pause
    scene ae2006 with dssa
    mi "*Whisper* Can you two stop that?"
    scene ae2007 with dssa
    mi "It's making me nervous."
    scene ae2009 with dssr
    "You keep staring into her yellow, green eyes."
    scene ae2010 with dssa
    na "Stooop. It's freaking me out."
    scene ae2004 with dssb
    ma "Alright, the first half of the class ends now."
    ma "Please take thirty minutes to refuel, let all this new information sink in, and we'll meet back here."
    ma "Please then sit with your previously assigned partner."
    scene BananaPokey with dssr
    pause
    scene ae2000 with dssb
    mi "[name], we're going to a cafe. Will you join?"
    d "Yeah, just give me a minute."
    mi "We'll wait outside."
    scene ae2014 with dssr
    na "Cooomeee!"
    scene ae2015 with dssa
    b "Go ahead."
    scene ae2016 with dssa
    pause
    scene ae2017 with dssa
    pause
    menu:
        "Break the eye contact and don't waste time anymore.":
            $ BellaEyeContactWin2x0 = False
            scene ae2013 with dssr
            b "*Smirks* Too easy."
            stop music fadeout 2.0
            scene black with Dissolve(2)
            with Pause(.5)
        "Keep staring at her.":
            $ BellaEyeContactWin2x0 = True
            scene ae2019 with dssr
            "She slowly walks over while maintaining eye contact."
            scene ae2020 with dssr
            pause
            scene ae2021 with vpunch
            "She almost stumbles down the stairs."
            scene ae2022 with dssr
            pause
            scene ae2023 with dssb
            pause
            scene ae2024 with dssr
            d "I can do this all day long."
            scene ae2025 with dssa
            b "You can't."
            scene ae2003 with dssr
            ma "Bella! May I talk to you for a second?"
            scene ae2026 with dssr
            pause
            scene ae2027 with dssa
            b "Consider yourself lucky."
            scene ae2028 with dssr
            d "You're just not in a position to win."
            scene ae2029 with dssa
            pause
            scene ae2030 with dssr
            pause
            stop music fadeout 2.0
            scene black with Dissolve(2)
            with Pause(.5)
    jump cafe2x0


label cafe2x0:
    $ play_playlist(playlist_Ch2_Coffee)
    scene ae2031 with dssb
    mi "Ahhh, it's been a while since I've last been here."
    scene ae2032 with dssa
    mi "It's one of my favorite coffee shops in the city."
    scene ae2033 with dssa
    d "I don't think I've ever been in one."
    scene ae2034 with dssr
    v "Coffee always makes me super jittery."
    scene ae2035 with dssr
    sil "Welcome to Muffin's Palace! My name is Silvie!"
    mi "Hi Silvie!"
    scene ae2036 with dssa
    sil "Oh Mila! Hey! Good to see you girl!"
    scene ae2037 with dssr
    mi "Yeah, it's been a while."
    mi "But I go to ZPR now, and it's right around the corner."
    scene ae2038 with dssr
    sil "Wow! Respect girl! You're killing it."
    sil "She's responsible for a quarter of our customers just by sitting near a window."
    scene ae2039 with dssa
    mi "*Chuckles* Oh stop it!"
    scene ae2038 with dssa
    sil "The usual?"
    mi "Yes."
    scene ae2040 with dssa
    v "Mmmmmhh, it's called Muffin's Palace."
    v "Do you have Muffins?"
    scene ae2041 with dssa
    sil "Oh lady... We've got all sorts of Muffins."
    scene ae2042 with dssa
    v "I'll take three!"
    scene ae2043 with dssr
    sil "Of course! Which ones?"
    v "Surprise me!"
    sil "Of course!"
    scene ae2044 with dssr
    d "I'll take the same as Mila."
    sil "Sure."
    scene ae2045 with dssa
    pause
    scene ae2046 with dssr
    mi "You poor thing..."
    mi "She assigned Bella to you."
    d "I'm gonna manage."
    scene ae2047 with dssr
    v "Is she nice?"
    scene ae2048 with dssa
    mi "Oh no, no... no, no... No."
    scene ae2049 with dssa
    v "Hmm."
    v "Are you and Mila friends?"
    scene ae2050 with dssa
    d "No."
    mi "At least not yet. We're acquaintances."
    scene ae2049 with dssa
    v "Oh! I'm sure you'll be friends in no time."
    scene ae2051 with dssa
    v "It's kinda sad that we didn't get teamed up!"
    scene ae2052 with dssa
    v "No offense to you, Mila!"
    scene ae2053 with dssa
    mi "None taken."
    scene ae2054 with dssr
    v "I saw Nami in the classroom. I hope she's gonna say hello."
    mi "Her partner is Ayua."
    v "How's Ayua?"
    scene ae2055 with dssa
    mi "She's cool."
    scene ae2056 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae2471 with dssr
    pause
    scene ae2473 with dssa
    s "I can feel my heart pounding."
    scene ae2474 with dssr
    n "S-same."
    n "Are we gonna die?"
    scene ae2475 with dssa
    d "We shouldn't have tasted all these espressos!"
    scene ae2476 with dssa
    n "I-t said super strong on some of the containers."
    scene ae2482 with dssr
    s "Am I shaking?"
    d "Yeah."
    scene ae2483 with dssa
    s "You're shaking too!"
    scene ae2477 with dssr
    n "I'm not!"
    scene ae2478 with dssa
    s "Yes you are!"
    scene ae2477 with vpunch
    n "PFF! I could drink ten more!"
    scene ae2479 with vpunch
    n "SEE!"
    s "Nami stop! You're gonna die!"
    scene ae2480 with vpunch
    n "I'm immune to caffeine!"
    scene ae2481 with dssa
    s "What's wrong with your left eye?"
    scene ae2480 with dssa
    n "Nothing! It's normal!"
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae2057 with dssb
    "You flop back into the present."
    scene ae2058 with dssb
    mi "And- will you run into any problems?"
    scene ae2059 with dssa
    v "I don't know..."
    scene ae2060 with dssa
    v "We'll see! Everything's gonna turn out fine!"
    scene ae2061 with dssa
    mi "You're such a positive person."
    scene ae2062 with dssr
    sil "Here you go."
    scene ae2063 with dssr
    mi "Thank you, Sylvie."
    scene ae2064 with dssr
    pause
    scene ae2065 with dssa
    mi "Are you okay?"
    scene ae2066 with dssa
    d "Yeah? Why wouldn't I be?"
    scene ae2065 with dssa
    mi "Just a feeling."
    v "[name] was there when I had the accident."
    scene ae2067 with vpunch
    mi "Really?!"
    d "Mhm."
    scene ae2068 with dssr
    v "He and I walked to the uhhh..."
    d "I was going to the bakery."
    scene ae2069 with dssa
    v "Right, me too."
    scene ae2070 with dssr
    pause
    scene ae2071 with dssa
    "Mila observes you and Victoria for a second."
    scene ae2072 with dssa
    mi "Call me weird but I think you two should go out... I don't believe in coincidences..."
    scene ae2073 with dssa
    v "I would like that!"
    menu:
        "Hesitantly agree and go out with her.":
            $ vicdate = True
            $ VicDate = True
            scene ae2075 with vpunch
            v "Great!"
            $ achievement.grant("VicDatePlan")
            $ achievement.sync()
        "I'm sorry but, I don't feel that way.":
            $ vicdate = False
            $ VicDate = False
            scene ae2076 with dssa
            v "Oh. No problem."
    scene ae2077 with dssr
    "You look around the cafe..."
    d "(I feel like I don't belong here.)"
    d "(I've got this unwell feeling in my stomach.)"
    scene ae2078 with dssr
    "Suddenly, something red enters your peripheral view."
    scene ae2079 with dssr
    n "Yo!"
    mi "Nami! Hi!"
    v "Hi Nami!"
    scene ae2080 with dssr
    n "Vic! Good to see you!"
    scene ae2081 with dssr
    pause
    v "I'm Victoria!"
    scene ae2082 with dssa
    ay "I'm Ayua. It's nice to meet you."
    scene ae2083 with dssa
    n "Ayua, this is [name]."
    scene ae2084 with dssa
    ay "Hi."
    "You give her a nod."
    scene ae2085 with dssr
    v "Sit with us!"
    scene ae2086 with dssr
    ay "Sorry, but Nami and I need to find someone."
    scene ae2087 with dssa
    n "Yeah, we're joining the art course for some extra credits."
    n "Wanna join too?"
    scene ae2088 with dssr
    d "No."
    scene ae2089 with dssr
    n "Your loss."
    n "Alright, we're gonna get a coffee to-go and be on our way."
    scene ae2090 with dssa
    mi "Bye!"
    scene ae2091 with dssr
    v "Nami is awesome!"
    d "Mhhh."
    scene ae2092 with dssr
    mi "I like her too."
    mi "Such a positive person."
    scene ae2093 with dssa
    pause
    scene ae2094 with dssr
    mi "And then there's you."
    "You raise a brow."
    scene ae2095 with dssa
    mi "Sorry, just kidding."
    scene ae2096 with vpunch
    v "Oh! It's almost 12!"
    v "I need to head back!"
    scene ae2097 with dssa
    mi "We can stay a little longer."
    scene ae2098 with dssa
    v "I need to talk to the dean."
    scene ae2100 with dssr
    v "Here's the money."
    scene ae2099 with dssr
    mi "Do you need any help?"
    v "No, no. I'm good."
    v "I'll see you two in class!"
    scene ae2101 with dssb
    pause
    scene ae2102 with dssa
    mi "Are you sure you don't need help?"
    scene ae2103 with dssa
    v "Nooo!"
    scene ae2104 with dssr
    pause
    scene ae2105 with dssa
    mi "She's such an inspiration."
    scene ae2106 with dssa
    d "Is she?"
    scene ae2105 with dssa
    mi "She loses the ability to walk and she seems as happy as a person can be."
    scene ae2106 with dssa
    d "I don't buy it."
    scene ae2107 with dssa
    pause
    scene ae2108 with dssa
    mi "Do you... do you think she's acting?"
    d "I don't know her well enough... but something about her freaks me out."
    scene ae2109 with dssr
    if VicDate is True:
        mi "And yet you agreed to go out with her."
        scene ae2110 with dssa
        d "Maybe that's exactly the reason why I said yes."
        d "I wanna know what's under the hood."
        scene ae2111 with dssa
        "Mila laughs."
        scene ae2112 with dssa
        mi "Y-you know how that sounded, right?"
        scene ae2113 with dssa
        d "Oh. Yeah... I see it now."
    else:
        scene ae2114 with dssa
        mi "I hope you're wrong."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae2115 with dssb
    mi "Wanna head back?"
    d "Yeah."
    scene ae2116 with dssa
    mi "Sylvie? Could we have the check, please?"
    sil "Sure!"
    scene ae2117 with dssb
    mi "Keep the change."
    sil "Thanks!"
    scene ae2118 with dssr
    mi "Thoughts about the coffee?"
    scene ae2119 with dssa
    d "Surprisingly good."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae2253 with dssb
    pause
    scene ae2254 with dssa
    mi "Shall we?"
    scene ae2255 with dssa
    d "They keep staring at you."
    mi "Who?"
    stop music fadeout 4.0
    scene ae2256 with dssa
    pause
    play music "music/Suspense/Scott Buckley - Resonance.ogg"
    scene ae2257 with dssr
    u "Look who it is, trash girl Mila."
    scene ae2258 with dssr
    u "Remember when she said she'd join Schwarz someday?"
    scene ae2259 with dssa
    u "It seems like she decided to work on the streets, huh?"
    u "Following your mother's footsteps. Inspirational."
    scene ae2260 with dssr
    d "Who are these clowns?"
    scene ae2261 with dssa
    u "Clowns?"
    scene ae2262 with dssa
    u "Trashy Mila got herself an even trashier boyfriend."
    scene ae2263 with dssa
    u "Have you ever heard of a barbershop, hobo?"
    scene ae2264 with dssr
    mi "Let's go."
    menu:
        "Stay, and confront them.":
            scene ae2265 with dssr
            mi "*Whisper* They're not worth it."
            scene ae2266 with dssa
            pause
            $ SchwartzStudentsConfront2x0 = True
            scene ae2268 with dssa
            "You take a few steps into the group's direction."
            scene ae2269 with dssr
            u "Oh, look at him."
            scene ae2270 with dssa
            pause
            scene ae2271 with dssa
            u "Touch me and see what happens... Do it."
            scene ae2272 with vpunch
            "As if Mila could read your thoughts, she grabs you by the arm and forcefully drags you away."
            scene ae2274 with dssr
            u "Disgusting trash."
            scene ae2273 with dssa
            u "Bye losers!"
            scene black with Dissolve(2)
            with Pause(.5)
            scene ae2275 with dssb
            d "Why did you do that?"
            scene ae2276 with dssa
            mi "They would sue you until there's nothing left!"
            mi "Just ignore them."
            scene ae2278 with dssa
            d "If you let people like that have their way, things are never going to change."
            scene ae2279 with dssa
            mi "You won't change anything by punching one of them."
            scene ae2278 with dssa
            d "But it would feel really good."
            scene ae2280 with dssa
            mi "That I believe."
            stop music fadeout 2.0
        "Go with Mila.":
            scene ae2265 with dssr
            mi "*Whisper* They're not worth it."
            scene ae2266 with dssa
            pause
            scene ae2267 with dssa
            d "A waste of energy."
            scene ae2265 with dssa
            mi "Yes."
            stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    jump College2x0_2

label College2x0_2:
    $ play_playlist(playlist_Ch2_Coffee)
    scene ae2281 with dssb
    pause
    scene ae2282 with dssr
    d "Who were they exactly?"
    scene ae2283 with dssa
    mi "From my old high school."
    d "Bad blood?"
    scene ae2286 with dssa
    pause
    scene ae2287 with dssa
    mi "I'm not from a very wealthy family."
    scene ae2288 with dssa
    d "So?"
    scene ae2289 with dssa
    mi "Well, not even from an average family."
    scene ae2290 with dssa
    d "So?!"
    scene ae2289 with dssa
    mi "We're as poor as it can get."
    scene ae2290 with vpunch
    d "SO?!"
    scene ae2291 with dssr
    mi "I've never really had clean clothing... And only two sets of clothes through most of elementary school."
    mi "People used to make fun of me... a lot."
    mi "And it didn't help when my parents showed up drunk the few times they bothered to pick me up."
    scene ae2292 with dssa
    mi "That's enough for them to pick on me..."
    scene ae2293 with dssr
    mi "Maybe also the fact that I rebuffed two of them in the past."
    mi "They probably thought I'd be impressed by a nice car."
    d "I see."
    scene ae2294 with dssa
    mi "I think they usually don't get rejected and took it reaaally bad."
    scene ae2295 with dssa
    d "I see some satisfaction on your face."
    scene ae2294 with dssa
    mi "That's why I don't take it personal."
    scene ae2296 with dssa
    mi "It still hurts because what they say is true... I'm poor and from a dysfunctional family."
    mi "But I also know that they're salty because I had no interest in them..."
    scene ae2297 with dssa
    d "It's good that you don't let them get into your head."
    d "Let's go inside."
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae2298 with dssb
    pause
    scene ae2299 with dssr
    mi "Good luck with Bella."
    scene ae2300 with dssa
    "You scan the room."
    scene ae2301 with dssb
    pause
    scene ae2302 with dssa
    pause
    scene ae2303 with dssa
    pause
    scene ae2304 with dssa
    "You both sit there in silence."
    scene ae2305 with dssa
    ma "Please open the book in front of you."
    scene ae2306 with dssa
    d "I have no book."
    ma "Yes, only one book per couple."
    scene ae2307 with dssa
    pause
    scene ae2345 with dssr
    mi "Miss Marla? I have a question."
    scene ae2346 with dssa
    ma "Yes, Mila?"
    scene ae2345 with dssa
    mi "Uhm- Chapter 1 looks pretty darn long... We're not supposed to finish it this quarter, right?"
    scene ae2350 with dssr
    ma "You totally are."
    scene ae2351 with dssa
    n "How?"
    scene ae2352 with dssa
    ma "You'll have to work on it outside of the school hours."
    scene ae2349 with dssr
    v "Yay! Sounds like fun."
    scene ae2308 with dssr
    b "Oh god..."
    scene ae2309 with dssa
    d "I really don't want to do that with you."
    scene ae2308 with dssa
    b "Neither do I."
    scene ae2309 with dssa
    d "You'll take it home one day... Me the next."
    scene ae2308 with dssa
    b "They designed the task in a way that forces you together... Otherwise we won't get it done on time."
    scene ae2310 with dssr
    b "Miss Marla?"
    b "Could I have a different partner?"
    scene ae2311 with dssa
    ma "No."
    scene ae2312 with dssa
    d "Could I have a different partner?"
    scene ae2314 with dssa
    ma "No."
    scene ae2311 with dssa
    d "Do I have to work with 'that' for the entire year?"
    scene ae2353 with dssr
    ma "No."
    ma "Partners will rotate every quarter."
    scene ae2308 with dssr
    b "No matter what, I won't come to your place."
    scene ae2309 with dssa
    d "I wouldn't want you there."
    scene ae2315 with dssb
    pause
    scene ae2316 with dssa
    d "Get off your phone and pay attention."
    scene ae2317 with dssa
    b "Suck it."
    scene ae2318 with dssr
    d "I don't want to explain all of this stuff to you later."
    scene ae2319 with dssr
    b "I'll give you five bucks if you just shut up."
    b "Maybe afterwards you can buy another twenty pack of shirts with that... Actually, put in some pants too."
    scene ae2320 with dssr
    b "...And give me back the change."
    scene ae2321 with dssa
    d "I'm pretty sure at the end of this quarter... One of us is going to be dead."
    scene ae2320 with dssa
    b "It's gonna be you."
    scene ae2322 with dssr
    d "Move your arm, I can't see."
    scene ae2323 with dssa
    pause
    scene ae2324 with dssr
    d "*sigh*"
    scene ae2325 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    if jeff == 1:
        scene ae2326 with dssb
        pause
        scene ae2328 with vpunch
        pause
        scene ae2329 with dssa
        pause
        scene ae2356 with dssr
        pause
        scene ae2330 with dssr
        d "(Remember to eat enough.)"
        scene ae2331 with dssa
        pause
        scene ae2332 with vpunch
        pause
        scene ae2333 with dssa
        pause
        scene ae2357 with dssr
        pause
        scene ae2334 with dssr
        d "(Suck it.)"
        scene ae2335 with dssa
        pause
        scene ae2358 with dssr
        d "(Fucking Cheeto...)"
    scene ae2355 with dssb
    ma "Alright, collect your thoughts and we'll see each other tomorrow."
    ma "I recommend getting together with your partner today. Get to know each other and figure out your part in the assignment."
    scene ae2336 with dssb
    pause
    scene ae2337 with dssb
    b "We'll go to my place."
    scene ae2338 with dssr
    pause
    scene ae2339 with dssa
    b "I've parked in the west parking space... Don't be late... I won't wait."
    scene ae2343 with dssa
    d "I'll go to the Mensa before... I'm hungry."
    scene ae2340 with dssa
    b "Fine. I wouldn't want to stop at a homeless shelter."
    scene ae2343 with dssa
    d "Are you always this annoying?"
    scene ae2341 with dssa
    pause
    scene ae2342 with dssa
    b "Pretty much, yeah."
    scene ae2344 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae2360 with dssb
    pause
    scene ae2361 with dssr
    d "Cheeto, I'm gonna go to the mensa."
    scene ae2362 with dssa
    n "Sure! See you then."
    scene ae2363 with vpunch
    n "WAIT!"
    scene ae2364 with dssr
    n "You're not bringing Bella home, right?"
    scene ae2365 with dssa
    d "No, I'm going to her place."
    scene ae2366 with dssa
    n "Please..."
    scene ae2367 with dssa
    n "Please use a condom."
    d "Shut up."
    scene ae2368 with dssa
    "She giggles."
    scene ae2369 with dssr
    v "Hey!"
    scene ae2370 with dssa
    d "Hey Victoria."
    scene ae2371 with dssa
    v "The only time I get called Victoria is when I messed up."
    scene ae2372 with dssa
    d "You didn't mess up... yet."
    scene ae2374 with dssa
    v "Mila looked a little sad. Did something happen when I left?"
    scene ae2373 with dssr
    d "Nah, nothing to worry about."
    d "Her coffee was a little strong."
    scene ae2375 with dssa
    "She smiles."
    scene ae2376 with dssa
    v "I don't believe you... But I'll still go with it."
    scene ae2377 with dssa
    v "See you later!"
    d "Yeah, I'll see you."
    scene ae2378 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    jump Mensa2x0

label Mensa2x0:
    scene ae2380 with dssb
    pause
    scene ae2381 with dssr
    pause
    scene ae2382 with dssr
    d "(I'm really not looking forward to working with Bella.)"
    scene ae2384 with dssa
    d "(She seems to be the worst kind of human being.)"
    scene ae2385 with vpunch
    u "Hi!"
    u "Do you want to sign up for the theater class?"
    scene ae2388 with dssr
    d "No."
    scene ae2389 with dssr
    u "Are you sure?"
    scene ae2390 with dssa
    d "*Stern* Yes."
    scene ae2391 with dssr
    u "Hi! Are you interested in joining our theater?" #zu sasha etc.
    scene ae2392 with dssa
    d "(If I just take long enough, Bella might just leave.)"
    scene ae2393 with dssr
    pause
    scene ae2394 with dssr
    pause
    scene black with Dissolve(2)
    stop music fadeout 2.5
    with Pause(.5)
    show text "You finish up your meal and slowly head towards the western parking space." with dissolve
    with Pause(2.5)
    $ play_playlist(playlist_Ch4x52)
    scene ae2395 with dssb
    pause
    scene ae2396 with dssr
    pause
    scene ae2397 with dssa
    b "I said be fast!"
    scene ae2398 with dssa
    d "You also said you'd leave."
    d "At least I was hoping for that."
    scene ae2399 with dssr
    u "Who's this?"
    scene ae2400 with dssa
    b "Some idiot I got grouped up with."
    scene ae2401 with dssa
    u "Show her some respect!"
    scene ae2402 with dssa
    d "Fuck off, beanpole."
    scene ae2401 with dssa
    u "Wow, he's got a mouth."
    scene ae2400 with dssa
    b "One that he should keep closed."
    scene ae2403 with dssr
    u "Who are you calling a beanpole?!"
    u "Look at you! You don't have a single gram of muscle."
    scene ae2404 with dssa
    d "Look, I'm really not interested in arguing with a living vegetable."
    scene ae2405 with dssa
    na "Eva... Can you two please stop."
    scene ae2406 with dssr
    ev "I'm gonna kick your ass."
    b "Please do..."
    scene ae2407 with dssa
    d "I'd rather not fight someone whose body hasn't entered puberty yet... Go over there and try to fight a blade of grass."
    scene ae2408 with vpunch
    ev "Nadia! Hold me back!"
    scene ae2409 with vpunch
    pause
    scene ae2410 with dssa
    ev "Be glad she's holding me back!"
    scene ae2411 with dssr
    pause
    scene ae2412 with dssa
    na "*Whispers* ...Don't make me do this."
    scene ae2413 with dssr
    d "Can we leave?"
    scene ae2414 with dssa
    b "I'd rather have you leave."
    scene ae2415 with dssa
    pause
    scene ae2416 with vpunch
    b "Come back! We have an assignment to complete!"
    scene ae2417 with dssr
    d "Do you have something to eat?"
    scene ae2418 with dssa
    b "No?"
    scene ae2419 with dssr
    pause
    scene ae2420 with dssa
    "You look at Nadia's banana."
    scene ae2421 with dssa
    pause
    scene ae2422 with dssa
    b "*sigh*"
    scene ae2423 with dssa
    b "I'll see you two later."
    scene ae2424 with dssb
    pause
    scene ae2429 with dssr
    d "That's your car?"
    scene ae2430 with dssa
    b "Duh?"
    scene ae2429 with dssa
    d "It looks like it's got all sorts of cancer."
    scene ae2431 with dssa
    b "Shut up. Get in. And be quiet."
    scene ae2432 with dssr
    pause
    scene ae2427 with dssr
    pause
    scene ae2425 with dssr
    ay "Did I miss Bella?"
    ev "By a second."
    scene ae2426 with dssa
    n "Hey, I'm Nami."
    ev "Hey, my name's Eva."
    scene black with Dissolve(2)
    with Pause(.5)
    jump BellaHome2x0

label BellaHome2x0:
    scene ae2433 with dssb
    pause
    scene ae2434 with vpunch
    "You get pressed into the seat whenever she launches from a traffic light."
    scene ae2435 with dssr
    d "Can you drive like a normal fucking person?"
    scene ae2436 with dssa
    b "My car, my rules."
    scene ae2435 with dssa
    d "I'm afraid this car might give me an STD."
    scene ae2436 with dssa
    b "You won't have to worry about that, stupid virgin."
    scene ae2437 with dssb
    pause
    scene ae2439 with dssr
    b "You're totally a virgin, aren't you?"
    scene ae2440 with dssa
    d "Keep driving and look at the road."
    scene ae2438 with dssa
    b "Bitch."
    scene ae2441 with dssr
    b "If you do all the work, and we get a good grade."
    scene ae2442 with dssa
    b "I'll buy you an escort."
    scene ae2443 with dssa
    b "I wonder if Mila's still in the biz..."
    d "She's an escort?"
    scene ae2445 with dssa
    b "*chuckles* No."
    b "I just like to make fun of her."
    scene ae2444 with dssa
    d "You're weak."
    scene ae2446 with dssb
    b "Am I?"
    scene ae2447 with dssa
    d "You pick on people below your social standing."
    d "Everyone can do that."
    d "You're embarrassing."
    d "And now look at the fucking street!"
    scene ae2448 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae2449 with dssb
    pause
    scene ae2450 with vpunch
    d "...Wait."
    b "We're here anyways."
    scene ae2454 with dssr
    d "Those guys..."
    b "What about them?"
    d "Your neighbors?"
    b "Mhm."
    d "(Those are the guys that insulted Mila and me.)"
    scene ae2451 with dssb
    d "I want to pick on them."
    $ bellaknowsmario = True
    $ bellavsmario = True
    scene ae2452 with dssa
    b "Why?"
    d "They have it coming."
    scene ae2453 with dssa
    pause
    scene ae2455 with dssa
    b "I agree."
    b "The guy who lives there is Mario Holgerson."
    b "The left one is Antony Reus."
    scene ae2451 with dssr
    d "I see."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    jump BellaHomeAmber2x0

label BellaHomeAmber2x0:
    $ play_playlist(playlist_Amber)
    scene ae2208 with dssb
    pause
    scene ae2209 with dssr
    b "Mama? I'm home."
    scene ae2210 with dssa
    u "I'm well aware. It's hard not to hear your car..."
    d "(I'll meet the person that gave birth to this demon.)"
    scene ae2211 with dssr
    b "I've got some unwanted baggage..."
    u "Mh?"
    scene ae2212 with dssr
    u "Oh! Hello!"
    d "Hello."
    scene ae2213 with dssr
    pause
    scene ae2214 with dssa
    b "That's the baggage I was talking about."
    "She looks confused."
    b "We got grouped up... For a group project."
    scene ae2215 with dssa
    u "How nice!"
    scene ae2216 with dssa
    "You and Bella say 'Not at all' at the same time."
    scene ae2217 with dssa
    u "Well, I think it can teach us some valuable lessons if we work together with others... Even if we aren't particularly fond of them."
    scene ae2218 with dssr
    u "If you need anything...?"
    scene ae2219 with dssr
    d "I'm [name]."
    scene ae2220 with dssa
    u "If you need anything [name], don't hesitate to ask."
    u "My name's Amber."
    scene ae2221 with dssa
    d "Thanks, Amber."
    scene ae2222 with dssa
    b "*Sigh* Let's get this over with."
    scene ae2223 with dssr
    pause
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    jump BellaHomeBreakdown2x0

label BellaHomeBreakdown2x0:
    $ play_playlist(playlist_Gymch3)
    scene ae2120 with dssb
    d "I'm surprised... Your Mom actually seems cool."
    scene ae2121 with dssa
    b "Don't you dare ever talk shit about her."
    scene ae2122 with dssa
    d "I just said she seems cool... Not like you, misguided bag of insecurities."
    d "But I don't blame the parent for their hopeless child."
    scene ae2123 with dssr
    b "How the fuck am I insecure?!"
    scene ae2124 with dssa
    d "You drool insecurity... Masked behind a tough exterior."
    scene ae2125 with dssr
    b "Wow, did you read that in today's horoscope?"
    b "Fucking hobo. I bet this is the closest you ever got to a girl's room."
    b "Not that I'm surprised."
    scene ae2126 with dssr
    "You ignore her and check out the room."
    scene ae2127 with dssr
    d "Hard to believe a girl lives here."
    scene ae2128 with dssa
    b "I didn't intend on bringing anyone over."
    scene ae2129 with dssr
    b "I'm going to change. Don't touch anything!"
    d "I don't wanna catch an STD."
    scene ae2130 with dssr
    b "*Chuckles* You'll never have to worry about that... Trust me."
    scene ae2131 with dssb
    pause
    scene ae2132 with dssr
    pause
    scene ae2133 with dssr
    d "(Hmm.)"
    scene ae2134 with dssr
    pause
    scene ae2135 with dssa
    pause
    scene ae2136 with dssr
    d "(Gummy bears...)"
    scene ae2137 with dssa
    pause
    scene ae2138 with dssr
    pause
    scene ae2139 with dssr
    "You touch some fabric with your elbow..."
    scene ae2140 with vpunch
    d "Ughhh..."
    scene ae2141 with dssa
    pause
    scene ae2142 with vpunch
    b "STOP EATING THEM!"
    scene ae2143 with dssr
    d "They're good."
    scene ae2144 with dssa
    "She starts laughing."
    b "I bet they are."
    d "(I don't like the look on her face.)"
    d "What's up with them?"
    scene ae2145 with dssa
    b "Those gummy bears have THC in them."
    scene ae2146 with dssr
    "You put the jar away."
    scene ae2147 with dssa
    b "How many did you eat?"
    d "Like four."
    scene ae2148 with dssa
    b "It won't be that bad then."
    scene ae2149 with dssa
    b "You now owe me some money, bitch."
    b "I told you not to touch anything!"
    scene ae2150 with dssa
    d "Let's make one thing very clear... I will never listen to you."
    scene ae2149 with dssa
    b "If you know what's good for you, you will."
    scene ae2151 with dssr
    d "Okay... Let's make this here as easy and comfortable as possible..."
    d "Let's not talk unless it's absolutely necessary for the project."
    scene ae2152 with dssr
    b "Sounds good."
    scene ae2153 with dssb
    pause
    d "Can I have something to drink? My mouth is getting dry."
    scene ae2154 with dssa
    b "No."
    scene ae2155 with dssa
    d "I'll get it myself."
    scene ae2156 with dssr
    pause
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Amber)
    scene ae2233 with dssb
    pause
    scene ae2234 with dssr
    am "That sounds like a long stretch."
    scene ae2235 with dssa
    u "Well Bam-"
    scene ae2236 with dssa
    d "Excuse me?"
    am "Yes?"
    scene ae2237 with dssr
    d "Could I have something to drink?"
    scene ae2238 with dssa
    am "But of course! What would you like?"
    scene ae2239 with dssa
    d "I'd take whatever umm... umm-"
    scene ae2240 with dssa
    am "Bella?"
    scene ae2241 with dssa
    d "Yes! Bella... That was her name... Whatever Bella likes."
    "Amber observes you weirdly."
    scene ae2242 with dssa
    d "She gave me some gummy bears that had some THC inside... It's her fault... Sorry."
    scene ae2243 with dssa
    am "*Sigh* Oh god... I'm sorry."
    d "It's alright. I'll survive it."
    scene ae2245 with dssr
    pause
    scene ae2244 with dssa
    pause
    scene ae2246 with dssr
    pause
    d "...Can I help you?"
    scene ae2247 with dssa
    u "Stop blinking for a sec."
    scene ae2248 with dssr
    am "Leave him alone."
    scene ae2249 with dssa
    am "Here."
    d "Thanks."
    scene ae2250 with dssr
    pause
    scene ae2251 with dssa
    pause
    scene ae2252 with dssa
    u "What?"
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_BellaDate)
    scene ae2157 with dssb
    d "Here."
    b "Why would you get me one?"
    scene ae2158 with dssr
    d "As an apology for telling your Mom that you drugged me."
    scene ae2159 with vpunch
    b "You fucking asshole! I didn't drug you!"
    d "I'm sure she'll believe you."
    scene ae2160 with dssa
    b "You don't want me as your enemy."
    d "Oh, why's that?"
    scene ae2161 with dssa
    b "I'll destroy you."
    scene ae2162 with dssa
    "Your nose touches hers."
    scene ae2163 with dssa
    d "You're right... I don't want you as my enemy... Right now."
    scene ae2164 with dssa
    d "I want to focus on your neighbor."
    scene ae2165 with dssa
    pause
    scene ae2166 with dssa
    b "You're too stupid to do anything."
    scene ae2167 with dssa
    "You ignore her."
    scene ae2168 with dssr
    pause
    scene ae2169 with dssa
    b "Let's destroy his car."
    scene ae2170 with dssa
    "You look at her visibly confused."
    scene ae2171 with dssa
    b "What? You said I only pick on weak people below my social standing."
    scene ae2172 with dssa
    d "You're a moron if you think you can fool me."
    scene ae2173 with dssa
    b "I'm not a two-faced bitch."
    b "I'll let people know where they stand."
    scene ae2174 with dssa
    "Everything inside of you is against the idea of teaming up with her... But a small part wishes to."
    scene ae2173 with dssa
    b "Come back here tonight around midnight, and we'll do it."
    scene ae2175 with dssr
    d "Why would you want to do that?"
    b "Because I hate them. Mario is a little bitch and his father lusts after my mother."
    d "Ohhh, now I get it... Your mother is holy."
    scene ae2176 with dssr
    pause
    "She says nothing but looks at you with a stern expression."
    scene ae2177 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ae2178 with dssb
    pause
    scene ae2133 with dssr
    d "Who's the other girl in the picture?"
    scene ae2179 with dssr
    "She doesn't react, but the lines on her face deepen."
    d "(It seems like a sensitive topic... Her body reacts to it.)"
    scene ae2180 with dssa
    d "Is it your sister?"
    scene ae2181 with dssa
    b "Shut the fuck up... and work."
    d "Sensitive top-"
    play music "music/Suspense/Scott Buckley - Resonance.ogg"
    scene ae2182 with vpunch
    b "Listen you little cunt!"
    b "Are you too stupid to read the room?!"
    scene ae2183 with dssa
    d "I'm well aware of the tension."
    d "I just like to know things."
    "She stares at you."
    d "...So, who's she?"
    scene ae2184 with dssr
    b "Don't."
    scene ae2185 with dssa
    "Her voice gained a cold and uneasy layer."
    scene ae2186 with dssr
    d "(I'm at the crossroads here... I know that when I say another word, she'll flip.)"
    scene ae2187 with dssa
    d "(My curiosity is... I need to see what happens.)"
    scene ae2188 with dssa
    d "I'd like to know her name."
    scene ae2189 with vpunch
    "You predict her punch."
    "But she follows up with something you didn't see coming..."
    scene ae2190 with vpunch
    pause
    scene ae2191 with vpunch
    "She lands a rather weak punch, but her grappling technique overwhelms you."
    scene ae2192 with vpunch
    d "(Shit! I forgot her connection to Ayua.)"
    d "(I should've predicted something like this!)"
    scene ae2193 with vpunch
    "You struggle to get out of her grip."
    scene ae2194 with vpunch
    "You block as many attacks as you can, but you also don't retaliate in any form."
    scene ae2195 with vpunch
    "As her already weak punches become even weaker and slower... You start pushing her away from you."
    stop music fadeout 4.0
    scene ae2196 with vpunch
    "She doesn't fight it and lets herself fall back."
    scene ae2197 with dssb
    play music "music/Ambience/Repeating History - Kevin Maison.ogg"
    "You collect your thoughts."
    scene ae2198 with dssa
    "You make out a faint cry."
    scene ae2200 with dssr
    "You watch her for a few seconds."
    scene ae2201 with dssr
    pause
    "She sniffles quietly."
    scene ae2202 with dssa
    d "I should-"
    scene ae2203 with dssr
    b "Leave. Now."
    scene ae2204 with dssr
    d "(For some reason I actually feel bad... I went into her past and touched holy ground... and acted like a tool.)"
    d "(I miscalculated, but I have a deeper understanding of her now.)"
    scene ae2205 with dssr
    d "The thing at midnight-"
    scene ae2206 with dssa
    b "*Cold* Be there or not. I don't care."
    scene ae2207 with dssa
    pause
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Amber)
    scene ae2224 with dssb
    d "Amber?"
    scene ae2225 with dssa
    am "What can I do for you, [name]?"
    scene ae2224 with dssa
    d "Could you show me how I get home? Bella and I had a little falling out and we'll continue with our project another time."
    scene ae2226 with dssa
    am "Oh, what happened?"
    d "I made the mistake of asking about the other girl on the picture."
    scene ae2227 with dssr
    am "...Oh."
    scene ae2228 with dssr
    pause
    scene ae2229 with dssa
    am "Did she... Did she attack you?"
    scene ae2230 with dssa
    d "It's not her fault, I pushed a little too hard."
    scene ae2231 with dssr
    pause
    scene ae2232 with dssr
    am "I'll drive you home."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch5_ViceCity)
    scene sba1 with dssb
    pause
    scene sba2 with dssa
    am "I'll talk to Bella."
    scene sba3 with dssa
    d "No."
    d "It would do no good if a third party got involved."
    scene sba4 with dssa
    d "This is between me and her."
    "Amber nods slightly even though she doesn't seem to fully agree."
    scene sba5 with dssa
    d "Thanks."
    scene sba7 with dssr
    am "I think... you as her project partner should know that Bella is very sensitive."
    am "She has seen some things and- I don't want this to happen again."
    scene sba6 with dssa
    d "It was my fault. Not hers."
    d "I touched holy ground."
    scene sba9 with dssa
    d "Thank you for taking me home."
    scene sba8 with dssa
    am "No problem."
    scene sba10 with dssr
    pause
    scene sba11 with dssa
    pause
    scene sba12 with dssr
    pause
    scene sba13 with dssa
    am "*Sigh*"
    scene black with Dissolve(2)
    with Pause(.5)
    scene sba14 with dssb
    pause
    scene sba15 with dssa
    ay "No. More to the right."
    scene sba16 with dssa
    ay "The other right."
    ay "No! The other right!"
    scene sba17 with vpunch
    n "How many rights are there for you?!"
    ay "That is good! Don't move!"
    scene sba18 with dssr
    n "Yo!"
    scene sba19 with dssa
    d "Yo."
    scene sba20 with dssr
    ay "Hi."
    d "Hi."
    scene sba21 with dssr
    pause
    scene sba23 with dssr
    d "Do I even need to ask?"
    scene sba24 with dssa
    pause
    scene sba25 with dssa
    n "I'm getting painted for class."
    scene sba26 with dssa
    ay "It's not for class. We're supposed to train and paint fruit baskets."
    scene sba27 with dssa
    n "And I'm one hell of a fruit basket! AM I RIGHT?!"
    scene sba28 with dssr
    "Ayua chuckles."
    n "Why are you already here?"
    scene sba29 with dssa
    d "We canceled studies for today. She and I had a falling out."
    scene sba31 with dssa
    ay "...What happened?"
    scene sba32 with dssa
    d "I asked her about the picture in her room. Specifically, the little kid next to her."
    scene sba33 with dssa
    ay "Oh."
    n "So? What's the issue?"
    ay "Don't move!"
    scene sba17 with vpunch
    n "My limbs are sleeping in! DRAW FASTER!"
    scene sba34 with dssa
    ay "What happened exactly?"
    scene sba35 with dssa
    d "I just asked her about the kid."
    scene sba34 with dssa
    ay "And?"
    scene sba35 with dssa
    d "Might've asked a few times more."
    scene sba36 with dssa
    ay "Why?"
    scene sba37 with dssa
    ay "I'm sure she made clear that she didn't want to talk about it!"
    scene sba39 with dssa
    d "...She might've mentioned it."
    n "Yo? What's going on."
    scene sba38 with dssa
    ay "What was she like when you left?"
    scene sba39 with dssa
    d "Demons wouldn't like to be in a room with her."
    scene sba40 with vpunch
    ay "You stupid, insensitive ass!"
    scene sba41 with dssr
    "She returns to the easel."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sbc1 with dssr
    pause
    scene sbc2 with dssr
    pause
    scene sbc3 with vpunch
    "You twitch."
    d "How did you get in here? I didn't even hear the door."
    scene sbc4 with vpunch
    "Before you can react, she kicks your legs away and throws you on the bed at the same time."
    scene sbc5 with vpunch
    ay "Listen! What is your problem with her?!"
    scene sbc7 with dssr
    d "(She fixed my arm in a way that I can't move it at all.)"
    scene sbc6 with dssr
    d "She likes to deal blows but can't take them herself."
    scene sbc5 with dssa
    ay "It doesn't give you the right to go that deep and think it won't have consequences!"
    scene sbc8 with dssr
    d "I knew it would have consequences. I mean she hit me."
    ay "Did you hit her back?"
    scene sbc9 with dssr
    "She loses her grip and slowly let's you get up."
    d "No."
    d "While she did attack me out of anger... It was quite hollow. There wasn't much behind it."
    scene sbc10 with dssr
    pause
    scene sbc11 with dssr
    ay "You'd better pray that she's okay or I'll hurt you really, really bad."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sba42 with dssb
    ay "Naaami, I'm so sorry! I have to leave."
    ay "It's urgent."
    scene sba46 with dssr
    n "What? Why?"
    scene sba47 with dssa
    n "I just got my butt to pop!"
    scene sba43 with dssr
    ay "Aww damn..."
    scene sba44 with dssa
    ay "You really did."
    scene sba45 with dssr
    ay "So sorry! We make up for the lost time!"
    scene sba48 with dssa
    pause
    scene sba49 with dssa
    n "W-what did you do?"
    scene sba50 with dssa
    d "Nothing really."
    scene sba51 with dssa
    stop music fadeout 2.0
    d "I just pushed her on a sensitive topic."
    scene sba52 with dssr
    play music "music/Suspense/Scott Buckley - Resonance.ogg"
    "The Cheeto just stares at you in an uncomfortable way."
    d "What's the harm?"
    scene sba53 with dssa
    "She takes a few slow steps towards you."
    scene sba54 with dssa
    n "*Whispers* What's the harm?"
    scene sba56 with vpunch
    n "WHAT'S THE FUCKING HARM!?" #grabs
    scene sba57 with vpunch
    n "WHAT WOULD YOU'VE DONE IF SOMEONE PUSHED YOU ON THE SUMMER TOPIC!"
    d "Che-"
    scene sba59 with vpunch
    n "NO!"
    n "You took it too far! What's the harm?! You fucking bitch ass retard!"
    scene sba60 with vpunch
    n "Y-YOU would go berserk if someone talked shit about Summer!"
    n "And now you did the same to her?!"
    scene sba61 with dssr
    d "I didn't say anything bad!"
    scene sba62 with vpunch
    n "It doesn't have to be bad! Oh my god!"
    scene sba63 with vpunch
    n "You- It's you! Why would you push her on such a sensitive topic?! It doesn't even matter what you said!"
    scene sba64 with dssa
    n "Just that you did it at all!"
    d "I-"
    n "Seriously [name]! What is wrong with you?!"
    scene sba65 with vpunch
    stop music fadeout 3.0
    d "Cheeto! Shut up!"
    scene sba67 with dssa
    $ play_playlist(playlist_AmbientNamiLake)
    d "...You're right."
    scene sba68 with dssa
    d "Shit... How could I not see that..."
    scene sba69 with dssr
    pause
    scene sba70 with dssr
    n "At least you realize it now... After all the damage has been done."
    n "And I guess it's too late to make it up to her..."
    scene sba71 with dssa
    d "...It's not."
    d "I'll meet up with her tonight."
    scene sba72 with dssa
    n "What? Why?"
    scene sba73 with dssa
    "You shake your head."
    scene sba74 with vpunch
    n "Tell me!"
    scene sba75 with dssr
    d "No. You're going to preach a fucking sermon. I don't need that right now."
    scene sba76 with dssa
    n "So it's something bad?"
    scene sba75 with dssa
    d "Depends on your point of view."
    scene sba76 with dssa
    n "I'll tell Noji."
    scene sba77 with dssa
    d "You will not."
    scene sba78 with dssa
    n "Oh. I will."
    n "If you leave the house tonight. I'll tell her!"
    scene sba79 with dssa
    d "Nami... please."
    scene sba80 with dssr
    n "No. You'll only get in trouble!"
    n "I don't want that..."
    scene sba81 with dssa
    d "First you make me feel bad about Bella. Then you get in my way of making it up to her."
    scene sba82 with dssa
    n "Not like that."
    scene sba83 with dssr
    pause
    n "I'm sorry... I can't stand the thought of you getting hurt... Leave the house and I'll tell her."
    scene sba84 with dssa
    d "By telling Noji you'll hurt me."
    scene sba85 with dssa
    n "No. I'm protecting you."
    scene sba86 with dssa
    pause
    scene sba87 with dssa
    d "*Sigh*"
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    jump NightBellchen2x0


label NightBellchen2x0:
    $ bellameet = True
    $ Bellameet = True
    $ play_playlist(playlist_Crossroads2)
    scene sba852 with dssb
    pause
    scene sba853 with dssr
    pause
    d "(Midnight.)"
    scene sba854 with dssa
    d "(Do I meet up with Bella?)"
    menu:
        "Go and meet up with Bella.":
            $ bellameet = True
            scene sba855 with dssa
            d "(Sorry Cheeto.)"
        "Don't meet up with Bella.":
            $ bellameet = False
            scene sba855 with dssa
            d "(The Cheeto might be right... I should try not to get in trouble... But...)"
            d "(I still feel somewhat bad for how I pushed Bella...)"
            scene sba856 with dssa
            d "(I don't have her number... Shit.)"
            d "(Ayua will kill me if Bella does something stupid and I didn't even show up.)"
    scene black with Dissolve(2)
    with Pause(.5)
    scene sba857 with dssb
    pause
    scene sba858 with dssr
    "You jump on your old bike and make your way to Bella's house."
    scene black with Dissolve(1.3)
    with Pause(.5)
    scene sba88 with dssr
    pause
    scene sba89 with dssa
    if bellameet is False:
        d "Hi."
        scene sba90 with dssr
        d "I'm just here to tell you that we're not gonna do it."
        scene sba92 with dssa
        b "What? Then why the fuck did you show up?"
        scene sba91 with dssa
        d "I didn't have your number, I had no way of contacting you."
        scene sba94 with dssa
        b "Well? Then fuck off."
        scene sba93 with dssa
        d "...You're not gonna do it alone?"
        scene sba94 with dssa
        b "Why are you still here? We're done."
        scene sba95 with dssa
        d "(Whatever she does now is on her.)"
        scene sba96 with dssa
        pause
        scene sba97 with dssa
        pause
        stop music fadeout 2.0
        scene black with Dissolve(2)
        with Pause(.5)
        jump NoBellaMidnight2x0
    else:
        d "Hi."
        scene sba90 with dssr
        d "What's the plan?"
        scene sba98 with dssa
        "She fumbles around in her backpack."
        scene sba99 with dssa
        "She hands you a spray can."
        d "And what are we going to write?"
        scene sba101 with dssa
        b "The truth."
        scene sba102 with dssr
        "Bella jogs forward."
        scene sba103 with dssr
        pause
        scene sba104 with vpunch
        with Pause(.5)
        "You grab her by the shoulder and drag her back."
        scene sba105 with vpunch
        b "*Angry whisper* What the fuck?!"
        scene sba106 with dssa
        d "You see these cameras right?!"
        scene sba107 with dssr
        b "They haven't been turned on in years!"
        b "They just serve the prospect of deterrence."
        scene sba108 with dssa
        d "How would you know that?"
        scene sba109 with dssa
        b "We've had dinner with them quite often and they mentioned it."
        scene sba111 with dssr
        d "I have a bad feeling."
        scene sba110 with dssa
        b "Then go home, pussy."
        scene sba112 with dssa
        d "Fuck off."
        scene sba113 with dssr
        pause #sie schreibt etwas
        scene sba114 with dssr
        pause
        scene sba115 with dssa
        pause
        scene sba116 with dssa
        d "What kind of moon man writing is that?"
        scene sba117 with dssa
        b "Idiot."
        scene sba118 with dssr
        d "Pedophile?"
        scene sba119 with dssa
        b "Write it on the other side."
        d "Nah, I don't trust you enough to take your word for it."
        scene sba120 with dssa
        d "I'll write something more sophisticated."
        scene sba121 with dssr
        pause
        scene sba122 with dssa
        d "Perfect."
        scene sba123 with dssr
        d "*Whisper* What now?"
        scene sba124 with dssa
        b "We'll go in."
        d "...You're kidding me, right?"
        scene sba125 with dssr
        b "A door at the back is open. I checked out the place before you came."
        scene sba126 with dssa
        d "I'm not going in there."
        scene sba125 with dssa
        b "You do you."
        scene sba126 with dssa
        d "You know it's one thing to spray can a car... But another to break into a house?"
        scene sba127 with dssa
        b "I don't really care."
        scene sba128 with dssr
        pause
        scene sba129 with dssa
        d "(I've got nothing to lose...)"
        scene black with Dissolve(2)
        with Pause(.5)
        scene sba130 with dssr
        pause
        scene sda132 with dssr
        pause
        scene sda133 with dssa
        pause
        scene sda134 with dssr
        d "What do you want in here?"
        b "There's something I wanna steal. An heirloom."
        scene sda143 with dssr
        pause
        scene sda144 with dssa
        d "You had something with the guy?"
        b "Of course not you idiot!"
        scene sda145 with dssr
        d "Don't you wanna be any louder? Stupid twat."
        scene sda146 with dssr
        pause
        scene sda147 with dssa
        pause
        scene sba140 with vpunch
        "She suddenly stops and your head bumps into her rear."
        scene sba141 with dssa
        b "*Whisper* Seriously?"
        stop music fadeout 2.0
        d "Why did you suddenly stop?"
        scene sba142 with dssa
        "She crawls a little further up, then stops again..."
        scene sba143 with dssr
        b "*Whisper* I heard something..."
        scene sba144 with dssr
        pause
        scene sba145 with dssr
        pause
        scene sba146 with dssr
        pause
        d "(The house is gigantic and we can barely see shit.)"
        scene sba147 with dssa
        d "How many people live here?"
        b "Three, including some staff."
        play sound "music/SFX/SFX_BumpEcho.mp3"
        scene sba147 with vpunch
        "You and Bella twitch as you hear a loud bump echoing from the upper levels."
        scene sba148 with dssr
        $ play_playlist(playlist_DarkAmbientDnD)
        d "...What was that?"
        scene sba149 with dssr
        "Bella stays quiet and tries to listen for sound cues."
        scene sba151 with dssr
        b "Just follow me."
        b "We need to crawl up the stairs and then left... I think."
        scene sba150 with dssa
        pause
        scene sba152 with dssr
        pause
        scene sba153 with dssr
        b "No wait... In here. That was the way."
        scene sba154 with dssa
        b "No. Wrong. Upstairs."
        scene sba155 with dssa
        pause
        scene sba156 with dssr
        pause
        scene sba157 with dssa
        b "Yes, that's it."
        scene sba158 with dssa
        b "This way."
        scene sba159 with dssa
        pause
        scene sba160 with dssr
        pause
        scene sba161 with vpunch
        "Suddenly, Bella rams her nails into your calves."
        d "Ngh!"
        scene sba162 with vpunch
        d "You stupid- Why would you do that?!"
        scene sba163 with vpunch
        b "What is wrong with you?!"
        scene sba164 with dssa
        b "I didn't do anything you schizo-idiot!"
        scene sba165 with dssr
        pause
        $ play_playlist(playlist_Ch2_ScaryMary2)
        scene sba166 with vpunch
        "Suddenly, the light turns on!"
        scene sba167 with dssa
        "You and Bella freeze for a few seconds."
        scene sba168 with dssa
        b "*Whisper* Go go go! To the left!"
        "You two crawl as fast and quiet as you can."
        scene sba169 with dssr
        "You hear steps coming up the stairs."
        scene sba170 with dssa
        pause
        scene sba171 with dssa
        pause
        scene sba172 with dssa
        pause
        "You both stand there completely motionless for a few minutes..."
        scene sba173 with dssa
        b "*Whisper* He left his room. This is our chance to take a look inside."
        scene sba174 with dssr
        pause
        scene sba245 with dssr
        pause
        scene sba246 with vpunch
        "But then you both hear him return!"
        scene sba247 with dssa
        "Bella freezes and is unable to speak... Meanwhile you scan the room for a place to hide."
        scene sba248 with dssa
        stop music fadeout 2.0
        "You drag her towards the closet."
        $ play_playlist(playlist_Ch2_ScaryMary3)
        scene sba249 with dssa
        "Mario enters the room laser focused on his phone... So focused in fact that he doesn't hear you and Bella rearranging your bodies in the closet."
        scene sba250 with dssr
        pause
        scene sba251 with dssa
        "Her elbow, knee and hip bone pierce your body in a lot of uncomfortable places."
        scene sba252 with dssa
        pause
        scene sba253 with dssa
        "Suddenly Mario pulls down his shorts and turns on some 'late night entertainment.'"
        scene sba254 with dssa
        b "Ugh..."
        d "What's he doing?"
        scene sba255 with dssr
        "Bella slowly opens the door a little wider."
        scene sba256 with dssa
        d "..."
        scene sba257 with dssa
        "His chair rotates just far enough to give you and Bella a short glimpse of his mini-schlong."
        scene sba258 with dssa
        $ persistent.unlockedImageBellaCh2_2 = True
        b "*Whisper* It's so small."
        d "*Whisper* Mh."
        scene sba259 with dssa
        pause
        scene sba260 with dssa
        pause
        scene sba261 with dssa
        b "*Whisper*...What's poking my butt?"
        scene sba262 with dssa
        d "*Whisper* A flashlight."
        scene sba263 with dssa
        b "*Whisper* Ugh..."
        scene sba264 with dssa
        d "*Whisper* No. Like an actual flashlight."
        scene sba266 with dssa
        b "*Whisper* Oh."
        scene sba267 with dssa
        d "*Whisper* What's that thing by his butt though?"
        scene sba263 with dssa
        b "*Whisper* A buttplug."
        scene sba267 with dssa
        d "*Whisper* I have no idea what that is."
        scene sba263 with dssa
        b "*Whisper* Virgin."
        scene sba268 with dssr
        d "There's cash on the cupboard."
        b "So?"
        d "I want it."
        b "Why?"
        scene sba267 with dssa
        d "Not everyone was born rich, you privileged baboon..."
        scene sba263 with dssa
        b "Poor-people-talk bores me."
        scene sba269 with dssr
        "Bella opens the closet door and slowly crawls out of it."
        d "(She's gonna get us caught and we'll have to kill the guy...)"
        scene sba270 with dssa
        pause
        scene sba271 with dssa
        pause
        scene sba272 with dssa
        "She grabs the bundle of cash."
        scene sba273 with dssr
        "She shoots you a look."
        scene sba274 with dssr
        pause
        scene sba275 with dssr
        pause
        scene sba276 with dssa
        pause
        scene sba277 with dssa
        "You and Bella crawl back into the darkness."
        stop music fadeout 2.0
        scene black with Dissolve(2)
        with Pause(.5)
        $ play_playlist(playlist_Ch2_ScaryMary)
        scene sba175 with dssb
        d "Where's that heirloom?"
        b "There's a trophy room."
        scene sba176 with dssr
        "Bella turns on her phone for some light."
        scene sba177 with vpunch
        "Suddenly, a noise from the right."
        d "(Again that weird noise.)"
        scene sba178 with dssa
        b "...What is that?"
        scene sba179 with dssr
        d "(She actually sounds a little scared.)"
        scene sba180 with dssr
        d "Careful, remember the stairs."
        scene sba181 with dssa
        pause
        scene sba182 with dssa
        d "And turn off the flashlight!"
        scene sba183 with dssa
        d "Do you know where the room is?"
        scene sba184 with dssa
        b "Somewhat."
        scene sba183 with dssa
        d "Let's just get out."
        scene sba184 with dssa
        b "Fuck off. We're going to get it!"
        scene sba185 with dssa
        "Bella's phone switches to the lock screen and turns dark."
        scene sba186 with dssr
        pause
        play music "music/Suspense/Scott Buckley - Resonance.ogg"
        scene sba187 with dssa
        with Pause(.4)
        scene sba188 with vpunch
        "The cat jumps into Bella's face..."
        scene sba189 with dssr
        "Bella's phone slips out of her hand and flies down the stairs."
        scene sba190 with dssa
        pause
        scene sba191 with dssa
        "You can't see it but hear Bella and the cat fighting."
        scene sba192 with dssa
        "The cat makes some otherworldly noises while it massacres her."
        scene sba193 with vpunch
        "It gives her a feisty left claw right through her face."
        b "*Sharp whisper* GET IT AWAY FROM ME!"
        scene sba194 with dssr
        "You start feeling into the dark..."
        scene sba195 with dssa
        "And you find Bella's leg."
        scene sba196 with dssa
        "You slide your hand along her leg, grab the cat by it's tail and somewhat gently pull it off Bella."
        scene sba197 with dssa
        "Causing it to attack you."
        scene sba198 with vpunch
        "You try to keep it at bay, but its claws keep scratching your arm."
        scene sba199 with dssr
        "All of a sudden, the cat gets pulled away from you-"
        scene sba200 with dssa
        "And it flies down a few steps."
        scene sba201 with vpunch
        d "Where is it?!"
        scene sba202 with dssa
        b "I don't know! I threw it down the stairs!"
        scene sba203 with dssa
        d "(It wasn't Bella who put her nails into my calves. It was the damn cat!)"
        scene sba204 with vpunch
        d "I hear it coming back up!"
        scene sba205 with dssr
        "You and Bella crawl at maximum speed towards a different room."
        scene sba206 with dssa
        b "Shit! My phone!"
        d "You fucking idiot!"
        scene sba208 with dssa
        "Bella crawls back into the direction of the cat."
        scene sba209 with dssa
        "You try to follow Bella into the darkness."
        scene sba210 with dssr
        d "Shit, I'm totally lost. I don't know what direction I just came from."
        scene sba211 with vpunch
        pause
        scene sba212 with dssa
        "The cat jumps you again, pushing its claws into your shirt."
        "You manage to push it away, but it comes right back at you."
        scene sba213 with dssa
        "Bella appears out of the dark and grabs the cat, and again throws it away from you."
        scene sba214 with dssr
        "The cat slides around on the floor..."
        scene sba215 with vpunch
        "And bops against Mario's door."
        stop music fadeout 2.0
        scene sba216 with vpunch
        pause
        scene sba217 with dssa
        mar "What the fuck are you doing, Siegbert?"
        "Meow!"
        scene sba218 with dssa
        mar "I want to go to bed... It's no play-time now."
        mar "Come, you can sleep in my room."
        scene sba219 with dssa
        "Siegbert protests but Mario gently grabs him and carries him into his room."
        scene sba220 with dssa
        pause
        scene sba221 with dssr
        $ play_playlist(playlist_Ch2_ScaryMary)
        "You and Bella exhale in relief."
        d "Let's never talk about the fact that a vicious cat absolutely destroyed us... ever."
        b "...Deal."
        "You two sit there for two minutes until you calmed down, and the air's clean."
        scene sba222 with dssr
        "As you crawl past Mario's room, you can hear the cat on the other side of the door... Viciously meowing."
        d "Fast, before he lets it out again."
        scene sba223 with dssr
        "Carefully, you two crawl down the stairs."
        scene black with Dissolve(2)
        with Pause(.5)
        "After a minute of crawling, you arrive at a big, wooden door. At the same time, you hear a door on an upper level open and close."
        "Little foot steps can be heard in the far distance. Something's running down the stairs!"
        stop music fadeout 3.0
        d "The cat's coming!"
        $ play_playlist(playlist_Crossroads2)
        scene black with Dissolve(2)
        with Pause(.5)
        scene sba278 with dssb
        pause
        scene sba279 with dssr
        d "Is that what we're here for?"
        b "Yes."
        scene sba280 with dssr
        pause
        d "Which one of them?"
        scene sba281 with dssa
        pause
        scene sba282 with dssa
        b "This one."
        scene sba283 with dssr
        b "It's small enough to carry around comfortably."
        scene sba284 with dssa
        b "Let's get out of here."
        scene sba285 with dssr
        d "Is that a golden panty?"
        b "I don't want to know dude."
        scene sba286 with dssa
        d "The cat is somewhere around here. It's looking for us."
        scene sba287 with dssr
        b "You go first."
        scene sba288 with dssa
        d "No fucking way. I have no interest in getting mauled out of nowhere."
        scene sba289 with vpunch
        b "But I do?!"
        scene sba290 with dssa
        d "This was your stupid idea!"
        d "And I don't know the way out!"
        scene sba291 with dssa
        "Bella gives herself an internal pep talk... Preparing for the monster awaiting her in the dark halls."
        scene black with Dissolve(2)
        with Pause(.5)
        scene sba224 with dssr
        pause
        b "We're almost out."
        scene sba225 with dssa
        d "I hear the cat! It's coming!"
        scene sba226 with vpunch
        "You and Bella lose all inhibitions in the face of the never resting predator and start running."
        scene sba227 with vpunch
        pause
        "You run outside the backdoor, and close it hastily."
        scene sba228 with vpunch
        "Siegbert plops against the glass."
        scene sba229 with dssa
        pause
        scene sba230 with dssr
        d "Murmurs* Fuck you, Siegbert."
        scene sba231 with dssa
        "Bella starts giggling."
        scene sba232 with dssa
        "You can't help but also let out a little laugh."
        b "The fucking cat made us look like absolute fools."
        b "I respect the little thing."
        scene sba233 with dssa
        "She hands you the cash."
        scene sba234 with dssa
        d "$9000."
        d "(I never before had this much money in my hands.)"
        scene sba235 with dssa
        pause
        d "I... *sigh*"
        d "I wanted to apologize for earlier."
        d "It was-"
        scene sba236 with dssr
        b "I don't need your apology."
        scene sba237 with dssa
        d "I'm just-"
        scene sba238 with dssa
        b "Fuck off."
        scene sba235 with dssr
        d "Alright, I tried to apologize to you. Now Nami can't be mad at me anymore."
        d "(The Cheeto will totally hate me for coming here, though... For like two days.)"
        d "(I'm more worried about Noji, though.)"
        b "Why would she even care?"
        scene sba239 with dssr
        "You ignore her question and you both slowly sneak away."
        scene sba240 with dssr
        d "I'm not going to lie... It was exciting."
        scene sba241 with dssa
        "You climb the fence."
        scene sba242 with dssr
        pause
        b "You're bleeding."
        d "So are you."
        scene sba243 with dssr
        b "...Come."
        d "...Where to?"
        pause
        stop music fadeout 2.0
        scene black with Dissolve(2)
        with Pause(.5)
        $ play_playlist(playlist_Jaccuzi)
        scene sd138 with dssb
        pause
        scene sd139 with dssr
        b "Hold still or I'll spray it into your eyes."
        scene sd140 with dssa
        pause
        scene sd141 with dssr
        "She starts disinfecting multiple little scratch wounds."
        scene sd142 with dssa
        pause
        scene sd143 with dssr
        pause
        scene sd144 with dssa
        b "Don't look at me."
        scene sd145 with dssa
        d "I look where I want."
        scene sd146 with dssa
        pause
        scene sd147 with dssa
        d "This burns like hell."
        scene sd148 with dssr
        b "Mhm."
        scene sd149 with dssr
        b "This over here wouldn't have burned so bad."
        scene sd150 with dssa
        d "Then why did you use this one?"
        scene sd151 with dssa
        pause
        d "Cunt."
        scene sd152 with dssr
        pause
        scene sd153 with dssa
        d "Were those all?"
        b "Yeah, I think so."
        scene sd154 with dssr
        d "Oh... You want me to..."
        scene sd155 with dssa
        b "The ones on my back, I can't reach them."
        scene sd156 with dssa
        "You open her chest strap."
        scene sd157 with dssa
        pause
        scene sd158 with dssa
        d "This is actually worse than anything we've done today."
        b "It's the first and last time you ever get to touch an attractive girl."
        scene sd159 with dssa
        "You scoff."
        scene sd160 with dssa
        d "You're like a three."
        b "A three out of three? True."
        scene sd161 with dssa
        pause
        scene sd162 with dssa
        d "Siegbert got you good."
        scene sd163 with dssa
        b "I didn't want to hurt him and hesitated throwing him away."
        scene sd164 with dssa
        pause
        scene sd165 with dssa
        b "Still, I didn't think you had the balls to go through with it."
        scene sd166 with dssr
        d "I don't just talk."
        scene sd167 with dssa
        pause
        scene sd168 with dssr
        d "You also got some scratches on your face."
        scene sd169 with dssa
        b "I'll use makeup to cover them."
        scene sd170 with dssa
        d "Well, it's done."
        scene sd171 with dssa
        b "Great. Now get the fuck out."
        scene sd172 with vpunch
        play music "music/Suspense/Scott Buckley - Resonance.ogg"
        "You spray it in her face."
        scene sd173 with vpunch
        b "ARGH!"
        scene sd174 with vpunch
        "You turn off the light and quickly make your way out of the house."
        b "You cunt!"
        scene sd175 with dssa
        "She grabs the air trying to find you."
        scene sd176 with dssa
        b "I SWEAR IF I-"
        scene sd177 with vpunch
        "She stumbles over the table and drags down a plant with her."
        scene sd178 with vpunch
        pause
        b "...You're so dead, [name]."
        stop music fadeout 3.0
        scene black with Dissolve(2)
        with Pause(.5)
        show text "The next morning." with dissolve
        with Pause(2)
        $ achievement.grant("BellaHeist")
        $ achievement.sync()
        jump MorningAfterBella2x0


label MorningAfterBella2x0:
    $ play_playlist(playlist_Ch2_ScaryMary3)
    hide text with dissolve
    scene sd179 with dssb
    pause
    scene sd180 with dssr
    pause
    scene sd181 with dssa
    pause
    scene sd182 with dssr
    pause
    scene sd183 with dssr
    m "Good morning."
    scene sd184 with dssr
    d "Morning."
    scene sd185 with dssa
    pause
    scene sd186 with dssa
    d "...How fucked am I?"
    scene sd187 with dssr
    m "Oh..."
    scene sd188 with dssa
    m "You have no idea."
    scene sd189 with vpunch
    n "Yeah, make him suffer!"
    scene sd190 with dssr
    pause
    scene sd191 with dssa
    n "That's not how you make people suffer!"
    scene sd192 with dssa
    m "He'll need it for what's to come."
    scene sd193 with dssr
    d "Cheeto, you and I are done."
    scene sd194 with dssr
    n "Fuck. You."
    scene sd195 with vpunch
    m "Hey! You both stop with these words!"
    scene sd196 with dssr
    d "Oh please. You say 'fuck' all the time."
    scene sd197 with dssa
    m "I don't!"
    scene sd198 with dssr
    n "You always use a lot of profanities after a call from work."
    scene sd199 with dssa
    d "Or whenever you're on the phone with that friend of yours, you swear a lot, too."
    scene sd198 with dssa
    n "Or when someone mentions homeopathy."
    scene sd200 with dssa
    m "Speaking of my friends..."
    m "...A friend gave me a number of a well known therapist."
    scene sd199 with vpunch
    d "No fucking way! I'm not-"
    scene sd201 with vpunch
    m "YOU WILL!"
    m "No discussion!"
    scene sd202 with dssa
    d "I don-"
    scene sd204 with dssr
    "Noji walks around the table and sits on the edge of it..."
    scene sd205 with dssr
    "One leg dangling to the side... The other on the table."
    scene sd203 with dssr
    m "*Soft* Please do it for me."
    scene sd207 with dssa
    d "Just because I went to meet up with Bella at midnight?"
    scene sd208 with vpunch
    m "You what?"
    d "...What?"
    scene sd209 with dssr
    "You look at the Cheeto."
    d "(She didn't snitch on me...)"
    scene sd211 with dssr
    d "Then what did I do?"
    scene sd212 with dssa
    m "Nami told me about your incident with Bella."
    m "Yesterday, while you were at her place."
    scene sd214 with dssr
    pause
    scene sd213 with dssa
    m "I know how... how hard it is."
    m "Everything... From your isolation, the depression and... just the stress in general."
    m "Please, please do it for me and have at least one session."
    scene sd214 with dssa
    d "*Sigh* Okay."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    jump Bus2x0



label NoBellaMidnight2x0:
    $ play_playlist(playlist_Crossroads)
    scene sba292 with dssb
    pause
    scene sba293 with dssr
    pause
    scene sba294 with dssr
    pause
    n "You didn't go..."
    scene sba295 with dssr
    d "I didn't feel like it."
    d "And just to be clear. I didn't do it because of you."
    n "Whatever you tell yourself is your business."
    scene sba296 with dssr
    n "I know I'm a noisy bibi, but the last thing you need is another charge."
    scene sba297 with dssr
    pause
    scene sba298 with dssa
    n "Does the bike still run?"
    $ persistent.unlockedImageNami_CH2_2 = True
    d "The battery works but everything else is long gone."
    scene sba299 with dssr
    n "I remember when you got it... A last resort to get you out of your isolation."
    n "You begged for years to get a bike..."
    scene sba300 with dssr
    n "I never saw you ride it."
    scene sba301 with dssa
    d "I rode it at night..."
    d "And I thought I'd do it again tonight but... It's not working."
    scene sba302 with dssr
    n "Aren't you cold?"
    d "No."
    scene sba303 with dssr
    "She moves her legs over the bike, and cuddles closer to you."
    scene sba304 with dssr
    "The warmth her body radiates sends a shiver down your spine."
    scene sba305 with dssa
    d "I went to see Bella to tell her we wouldn't do it."
    scene sba306 with dssr
    n "Oh."
    n "How did she take it?"
    scene sba307 with dssa
    d "There was disappointment in her voice."
    scene sba306 with dssa
    n "You did the right thing."
    scene sba308 with dssr
    pause
    d "It depends on your point of view."
    scene sba309 with dssr
    "She rests her head on your shoulder... Little strands of her hair, blown up by the wind tickle the side of your face."
    pause
    scene sba310 with dssr
    "The Cheeto's head weighs heavier and heavier as she starts to fall asleep."
    pause
    scene sba312 with dssa
    d "Go to bed."
    scene sba311 with dssa
    n "*Whispers* Nhmmmm... Come with me."
    scene sba312 with dssa
    d "I just want to sit here for a while longer."
    scene sba311 with dssa
    n "So do I then."
    n "I can't leave you alone with all those monsters out here in the dark."
    scene sba313 with dssr
    d "There's something else out here... Something I yearn for, yet I can't grasp."
    scene sba314 with dssa
    pause
    scene sba315 with dssr
    pause
    d "Homesickness for a place I've never been."
    stop music fadeout 4.0
    scene black with Dissolve(2)
    with Pause(.5)
    show text "The next morning." with dssr
    with Pause(2)
    $ play_playlist(playlist_Ch2_ScaryMary3)
    hide text with dssb
    with Pause(.5)
    $ achievement.grant("Homesickness")
    $ achievement.sync()
    jump MorningNoBella2x0


label MorningNoBella2x0:
    scene sba317x with dssb
    pause
    scene sba318x with dssa
    d "Morning."
    scene sba319x with dssa
    n "Yo."
    scene sba320x with dssa
    m "Morning."
    m "Tea?"
    scene sba321x with dssa
    d "Coffee, please."
    scene sba322x with dssa
    pause
    scene sd182 with dssr
    d "You look like shit."
    scene sd194 with dssr
    n "Fuck. You. I had a hard night!"
    scene sd195 with vpunch
    m "Hey! You both stop with these words!"
    scene sd196 with dssr
    d "Oh please. You say 'fuck' all the time."
    scene sd197 with dssa
    m "I don't!"
    scene sd198 with dssr
    n "You always use a lot of profanities after a call from work."
    scene sd199 with dssa
    d "Or whenever you're on the phone with that friend of yours, you swear a lot, too."
    scene sd198 with dssa
    n "Or when someone mentions homeopathy."
    scene sd200 with dssa
    m "Speaking of my friends..."
    m "...A friend gave me a number of a well known therapist."
    scene sd199 with vpunch
    d "No fucking way! I'm not-"
    scene sd201 with vpunch
    m "YOU WILL!"
    m "No discussion!"
    scene sd202 with dssa
    d "I'm eighteen. I don't need-"
    scene sd204 with dssr
    "Noji walks around the table and sits on the edge of the table..."
    scene sd205 with dssr
    "One leg dangling to the side... The other on the table. "
    scene sd203 with dssr
    m "*Soft* Please do it for me."
    d "I... *Sigh* But why? Why now? Maybe all this college bullshit fixes me..."
    scene sd212 with dssa
    m "Nami told me about your incident with Bella yesterday."
    scene sd214 with dssr
    pause
    scene sd213 with dssa
    m "I know how... how hard it is."
    m "Everything... From your isolation, the depression and... just the stress in general."
    m "Please, please do it for me and have at least one session."
    scene sd213 with dssa
    d "*Sigh* Okay."
    scene sba304x with dssr
    "Noji finishes her good-morning jasmine tea."
    scene sba305x with dssa
    m "I'll go after my routine and I'll see you two later."
    scene sba306x with dssr
    n "You'll survive one session."
    scene sba307x with dssa
    d "Funny to hear that from you."
    scene sba308x with dssa
    pause
    scene sba309x with dssr
    d "*Sigh*"
    d "Wanna go?"
    scene sba310x with dssa
    n "In a minute."
    scene sba309x with dssa
    pause
    scene sba311x with dssa
    n "Yo, do you have some sunscreen?"
    scene sba312x with dssa
    d "I never leave the house. Why would I have sunscreen?"
    scene sba313x with dssa
    n "Man! I'm a pale lady!"
    scene sba314x with dssa
    d "A typical Cheeto."
    scene sba315x with dssr
    n "Sometimes I wish I had black hair."
    d "You do?"
    scene sba316x with dssr
    n "No."
    n "I look too good with red hair."
    scene black with Dissolve(2)
    with Pause(.5)
    show t1 with dssr
    jump UniCor2x0





label Bus2x0:
    $ play_playlist(playlist_Ch2_Coffee)
    scene sba349 with dssb
    pause
    scene sba350 with dssr
    d "Why didn't-"
    scene sba351 with dssa
    n "Did you really think I'd snitch on you, you goofy ass bitch?!"
    scene sba352 with dssa
    d "I did."
    scene sba353 with dssa
    n "I'll totally snitch on you if you don't go to therapy."
    scene sba354 with dssa
    pause
    scene sba355 with dssr
    n "What is it that you and Bella did?"
    scene sba356 with dssa
    d "Nothing really."
    scene sba357 with vpunch
    n "Bullshit."
    n "You were gone for almost two hours."
    n "I heard you leave and come back."
    scene sba358 with dssr
    pause
    scene sba359 with dssa
    n "I'm listening."
    scene sba360 with dssa
    d "Cheeto. Let it be."
    scene sba361 with dssa
    n "Asshole."
    n "First I don't snitch on you, and then you won't even tell me shit!"
    scene sba363 with dssa
    pause
    scene sba362 with dssa
    n "I should've snitched... Made Nojiko aware of your shenanigans."
    n "But I think even if I told her, she'd not do shit."
    scene sba364 with dssa
    n "Poor [name] is always a victim of his circumstances."
    n "She loves to play favorites."
    scene sba366 with dssa
    d "You're my favorite."
    scene sba367 with dssa
    n "Bullshit."
    scene sba368 with dssr
    d "She gives me enough shit behind closed doors."
    d "Just not in front of you."
    d "Because you're known for weaponizing this shit."
    scene sba369 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    jump UniCor2x0

label UniCor2x0:
    scene sba370 with dssb
    pause
    scene sba371 with dssr
    pause
    scene sba373 with dssr
    pause
    scene sba374 with dssa
    pause
    scene sba375 with dssr
    v "Hi!"
    scene sba376 with dssa
    d "Hey Vic."
    scene sba377 with dssa
    v "Are you heading to the gym?"
    scene sba378 with dssa
    d "Soon."
    scene sba379 with dssa
    v "*Sigh* I was asked to join another course..."
    d "Don't worry. Someday you'll join us."
    v "...Yeah. Right."
    scene sba382 with dssa
    d "How do you feel?"
    scene sba383 with dssa
    v "A little hot... Which reminds me!"
    v "We should head to the beach someday."
    scene sba384 with dssa
    d "Why not."
    scene sba383 with dssa
    v "Maja can drive us!"
    scene sba384 with dssa
    d "You made her your personal chauffeur, huh?"
    scene sba385 with vpunch
    v "Yes!"
    d "I like it."
    scene sba386 with dssa
    v "Well, I've gotta roll..."
    v "I'll see you later!"
    scene sba387 with dssa
    d "Sure. Later then."
    stop music fadeout 5.0
    scene sba388 with dssr
    pause
    scene sba389 with dssr
    "The corridor, which seconds ago was sprawling with students and teachers..."
    scene sba390 with dssr
    "Now has an eerie silence to it."
    scene sba391 with dssa
    pause
    scene sba392 with dssr
    pause
    scene sba393 with dssr
    pause
    scene sba394 with dssr
    d "(It's time to find the gym and see what the mandatory training looks like...)"
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch2BB)
    scene sba395 with dssb
    pause
    scene sba396 with dssa
    pause
    scene sba397 with dssr
    j "Hey."
    d "Hi."
    scene sba398 with dssr
    t "Look."
    t "I told you! I got shredded!"
    j "I'll give you that."
    scene sba399 with dssa
    t "Hey [name]."
    scene sba400 with dssa
    d "Trey."
    scene sba402 with dssr
    t "You haven't been going to the gym, right?"
    scene sba401 with dssa
    d "No."
    scene sba402 with dssa
    t "You've got good body composition."
    scene sba403 with dssa
    j "He's got a small waist and broad shoulders."
    j "Lots of potential there..."
    scene sba404 with dssr
    j "What're you signing up for?"
    scene sba405 with dssa
    d "Huh?"
    scene sba406 with dssa
    j "Oh? You're just going to do the mandatory training?"
    scene sba407 with dssa
    d "I didn't think that far yet."
    scene sba408 with dssa
    j "Any sports you're good at?"
    scene sba407 with dssa
    d "I was decent at basketball."
    scene sba408 with dssa
    j "Oh, right! Nami mentioned it."
    j "I'm gonna go for the basketball tryouts."
    scene sba409 with dssa
    t "Same here."
    scene sba410 with dssr
    j "Get over your phobia bro, and get back to American Football."
    scene sba411 with dssa
    "Trey says nothing and averts his gaze."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sba412 with dssb
    pause
    scene sba413 with dssa
    n "Yo!"
    scene sba414 with dssa
    d "Cheeto."
    scene sba415 with dssa
    d "Mila."
    scene sba416 with dssr
    mi "Hey [name]."
    if bellameet is True:
        scene sba417 with dssr
        pause
    else:
        scene sba418 with dssr
        pause
    scene sba419 with dssr
    ms "I'm Coach Stahl."
    scene sba420 with dssa
    mh "And I'm Coach Hill."
    scene sba421 with dssa
    mh "Welcome to the mandatory training sessions."
    mh "They'll be once a week, except for those that intend to join a sports team."
    scene sba422 with dssr
    pause
    scene sba423 with dssa
    ms "I don't like the look on your face."
    scene sba424 with dssr
    pause
    scene sba425 with dssa
    mi "What?"
    scene sba426 with dssa
    ms "Ten pushups."
    scene sba427 with dssa
    "Confused, Mila's eyes search for Nami's."
    scene sba428 with vpunch
    ms "TEN PUSHUPS!"
    mi "Okay!"
    scene sba429 with vpunch
    pause
    scene sba431 with dssr
    ms "You punks better not make the mistake to think this is some little kids sports class where we all jump happily in a circle."
    scene sba432 with dssr
    ms "What's your name, Spaghetti arm?"
    d "[name]."
    scene sba433 with dssa
    mh "[name]. What do you like?"
    menu:
        "Winning":
            scene sba435 with dssa
            mh "Yes! Exactly!"
        "Food":
            scene sba435 with dssa
            mh "You sure? Then why do you have two spaghetti arms?"
        "Spongebob squarepants":
            scene sba434 with dssa
            ms "...Can't argue with that."
        "Crushing enemies.":
            scene sba435 with dssa
            mh "That's the spirit!"
    scene sba436 with dssa
    ms "Listen up, punks."
    scene sba437 with dssa
    mh "We've created several different teams with the other coaches."
    mh "Please pick your preferred sports."
    ms "Coach Hill and I are responsible for the freshman basketball team."
    scene sba438 with dssr
    mh "Y'all will play Basketball today, but the next time everyone who's not interested in the big orange ball, go and fuck off."
    scene sba439 with dssa
    ms "Football and various other sports are going to start in the next few weeks."
    scene sba440 with dssa
    mh "Everyone who's got an interest in making it further, tryouts are in six weeks."
    scene sba441 with vpunch
    "He fakes a throw at Bella's face."
    scene sba442 with dssa
    ms "Everyone get some blood pumping and warm up!"
    scene sba443 with dssa
    mi "They seem mean."
    scene sba444 with dssa
    d "The last coach you'd want is someone that resembles a wet noodle."
    scene sba445 with vpunch
    n "Yo! Are ya talking about yourself?"
    scene sba446 with dssa
    n "I'ma slurp your noodle!"
    scene sba447 with dssa
    n "...That came out wrong."
    scene sba448 with dssa
    "Mila laughs."
    scene sba446 with vpunch
    n "I meant your noodle arms! Spaghetti!"
    scene sba449 with dssr
    ms "We'll start easy. A simple match."
    scene sba450 with dssa
    ms "Let's see whose parents can be proud... And who's just another disappointment."
    scene sba451 with dssa
    ms "Malcom."
    scene sba452 with dssa
    j "...What?"
    scene sba453 with dssa
    ms "Redhead."
    scene sba454 with dssa
    ms "Ashley."
    scene sba455 with dssa
    mi "My name's not Ashley."
    scene sba456 with dssa
    ms "You look like one."
    scene sba457 with dssr
    ms "Bushy brows."
    scene sba459 with dssr
    ms "Crooked teeth."
    scene sba460 with dssr
    ms "Versus."
    scene sba461 with dssa
    ms "Juice box."
    scene sba462 with dssa
    ms "Spaghetti."
    scene sba463 with dssa
    ms "Ali."
    scene sba458 with dssr
    ms "Girl in the inappropriately tight bodysuit."
    scene sba464 with dssr
    ms "And at last... I'd give you a funny and racist nickname, but I'm afraid of your Mother- Ayua."
    scene sba465 with dssa
    ay "Smart."
    scene sba466 with dssr
    pause
    scene sba467 with vpunch
    "Bella checks your shoulder."
    scene sba469 with dssr
    "But you don't pay her any attention."
    scene sba468 with dssr
    d "(The cripple is on my side.)"
    scene sba471 with dssr
    j "Yes, I played in the high school."
    ms "We've heard of you."
    scene sba472 with dssa
    d "(Mila's body language is 'wet noodle'.)"
    d "(She won't be an issue.)"
    scene sba470 with dssr
    d "(Bella seems fixated on me. I doubt she's going to play fair.)"
    scene sba474 with dssa
    na "Alright. [name]!"
    na "Come over here."
    scene sba475 with dssa
    pause
    scene sba476 with dssr
    na "Have you played before?"
    scene sba477 with dssa
    d "Once or twice."
    scene sba478 with dssa
    na "Then you can face off Bella."
    na "She's not thaaaat good."
    scene sba479 with dssa
    na "I'll take the center, Trey and Ayua defense."
    na "Sai, you take the right side?"
    scene sba480 with dssa
    sai "Yeah."
    scene sba482 with dssr
    mh "Nami, Nadia."
    scene sba483 with dssa
    mh "Come forward."
    stop music fadeout 2.0
    scene sba481 with dssa
    pause
    scene sba484 with dssa
    $ play_playlist(playlist_Ch1CollegeEnd)
    n "Are you ready to meet your creator?"
    scene sba485 with dssa
    na "Red meat seems to be back on the menu."
    scene sba486 with dssr
    "They giggle."
    scene sba487 with dssa
    mh "Ready?"
    scene sba488 with vpunch
    pause
    scene sba489 with vpunch
    "Nadia beats Nami and secures the ball!"
    scene sba490 with dssr
    "You study the movement of each player to determine who's up to the task."
    scene sba491 with dssa
    "Ayua catches your attention... She appears calm and chilled but there's something in her eyes that reminds you of a crouching tiger."
    scene sba492 with vpunch
    b "Watch it."
    scene sba493 with vpunch
    "As Bella is occupied with spitting hot bars, you see an opening and go into a full sprint."
    scene sba494 with dssa
    "Nadia spots you-"
    scene sba495 with vpunch
    pause
    scene sba496 with dssa
    pause
    scene sba497 with dssr
    pause
    scene sba498 with dssa
    "You take an abrupt stop to pass back to Nadia-"
    scene sba499 with vpunch
    "Causing Bella to fly against you with more force than she would've liked."
    scene sba500 with dssr
    mh "Bella! This isn't rugby!"
    scene sba501 with dssa
    b "I barely touched him."
    scene sba502 with vpunch
    "Nadia's in full sprint and closing in fast towards a scared Mila."
    scene sba503 with vpunch
    "Mila raises her slightly shaky arm, her eyes closed, and just hopes for the best."
    scene sba504 with dssr
    pause
    scene sba505 with dssr
    ms "Ashley! That was pathetic!"
    scene sba506 with dssr
    pause
    if bellameet is True:
        scene sba507 with vpunch
        pause
        scene sba508 with dssr
        d "I know you've got a thing for me bu-"
        scene sba509 with dssa
        b "Eww!"
        scene sba510 with dssr
        b "Say that again and I'll make sure you won't stand up again!"
        scene sba511 with vpunch
        pause
        scene sba512 with dssa
        "You hit her with your shoulder, causing her to lose her balance."
        scene sba513 with vpunch
        "She storms after you with flaring nostrils and an angry growl."
        scene sba514 with vpunch
        pause
        scene sba515 with vpunch
        d "Weak ass cunt!"
        scene sba516 with vpunch
        "She materializes additional strength and manages to push you away."
        d "(How can she be stronger than me?!)"
        scene sba517 with dssr
        b "You fucking bitch!"
        scene sba518 with vpunch
        n "Pay attention to the game you stupid bimbo!"
        scene sba519 with dssa
        mh "Last chance Bella or you're on the bench."
    else:
        d "(As long as Bella keeps her focus on me, we'll win.)"
        scene sba507 with vpunch
        pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene sba520 with dssb
    mh "Last point!"
    scene sba521 with dssr
    pause
    scene sba522 with dssa
    na "[name]."
    scene sba523 with dssr
    $ persistent.unlockedImageBellaCh2_3 = True
    na "Bella's right leg is injured. I accidentally drove over her foot a few weeks ago."
    na "Use it to your advantage."
    scene sba524 with dssa
    d "Got it."
    scene sba525 with dssr
    pause
    scene sba526 with dssa
    "The Cheeto passes to Jeff."
    scene sba527 with dssa
    "They outplay Sai."
    scene sba528 with dssr
    "Nami makes a run for the basket."
    scene sba529 with vpunch
    "Ayua flies in, takes a spin and the ball from Nami!"
    "And the Cheeto, utterly confused..."
    scene sba530 with vpunch
    "Kisses the ground."
    scene sba531 with dssr
    $ persistent.unlockedImageNami_CH2_4 = True
    n "What the fuck...?"
    scene sba532 with dssr
    ms "That was impressive."
    scene sba533 with dssa
    mh "I heard about her."
    scene sba532 with dssa
    ms "Everyone has heard about Ayua."
    scene sba534 with dssr
    pause
    scene sba535 with vpunch
    "Ayua passes to you-"
    scene sba536 with dssa
    pause
    scene sba537 with dssa
    d "(If I'll make it past her, we'll win.)"
    scene sba538 with dssr
    "(Nadia mentioned her right leg.)"
    scene sba539 with dssr
    d "(It doesn't matter. The adrenaline is too strong... and even stronger than that... Her will to punish me.)"
    d "(But I know her weakness.)"
    scene sba540 with dssr
    "You and Bella face off-"
    scene sba541 with dssr
    d "Since I first saw you... I can't stop thinking about your beautiful, yellow-green eyes."
    if bellameet is True:
        scene sba541 with vpunch
        "Bella stops dead in her tracks."
        scene sba542 with vpunch
        "And with a fast move to the left, you manage to overtake before she recovers."
        scene sba543 with dssr
        b "*Mumbles* Fucking bitch!"
        scene sba544 with vpunch
        "She sprints after you in full speed, destined to ground you."
        scene sba545 with dssr
        d "(I won't make it alone. I'm too out of shape.)"
        scene sba546 with dssr
        "Your eyes search for someone-"
        scene sba547 with dssr
        "Ayua appears behind Jeff, leaving him in the dust-"
        scene sba548 with dssa
        pause
        scene sba549 with dssr
        pause
        scene sba550 with vpunch
        pause
        scene sba551 with dssr
        pause
        "Even though the ball has left your hand three seconds ago-"
        scene sba552 with vpunch
        "Bella crashes into you hard enough for you both to crash to the ground-"
        scene sba553 with vpunch
        "-and slide against a mat."
        scene sba554 with vpunch
        pause
        d "You suck."
        scene sba555 with vpunch
        b "Fuck you."
        scene sba556 with dssr
        b "What a cheap trick."
        scene sba557 with dssr
        d "Loser."
        d "You're just not on my level."
        scene sba558 with dssa
        n "Get off him!"
        scene sba559 with dssa
        b "I'll get off him when I want to!"
        scene sba560 with vpunch
        "Nami grabs her ponytail-"
        scene sba561 with dssa
        "But before she can pull it, you grab her hand."
        scene sba562 with dssa
        "You look into Nami's eyes and shake your head."
        scene sba563 with dssa
        "The Cheeto releases Bella's hair reluctantly."
        scene sba557 with dssr
        d "Now get off me."
        scene sba565 with dssr
        pause
        scene sba564 with dssr
        mh "Alright."
        mh "Everyone who hasn't signed in to a sport program will meet in the small gym next week."
        mh "Gym A4-B to be exact."
        scene sba567 with dssr
        stop music fadeout 3.0
        ms "You all can fuck off now."
        scene sba569 with dssr
        $ play_playlist(playlist_AmbientBella)
        pause
        scene sba570 with dssa
        pause
        scene sba568 with dssr
        pause
        scene sba571 with dssr
        na "Good game."
        scene sba572 with dssa
        pause
        scene sba573 with dssr
        d "Thanks."
        scene sba575 with dssr
        na "Your passes and throws were very precise. Will you play for a team?"
        scene sba574 with dssr
        d "I haven't decided yet. Maybe."
        scene sba576 with dssr
        d "Do you?"
        scene sba577 with dssr
        $ persistent.unlockedImageNadiaCH2 = True
        na "No, I mostly just play for fun."
        d "I see."
        scene black with Dissolve(2)
        stop music fadeout 2.0
        with Pause(.5)
        jump ClassEnd2x0
    else:
        scene sba578 with dssa
        "You make a fast left step-"
        scene sba579 with dssr
        "But she recovers fast enough and in her attempt to block you with her right leg-"
        scene sba580 with vpunch #sfx
        "She miscalculates and rams her knee into your crotch."
        scene sba581 with vpunch
        "You let out a cough followed by a deep, painful inhale."
        j "Ouch- no..."
        ms "...Not cool."
        scene sba582 with dssr
        b "I found him like this."
        scene sba583 with dssa
        mh "What the hell, Bella?"
        scene sba584 with dssa
        b "I didn't intend to do that. He ran into it."
        scene sba585 with vpunch
        n "Bullshit!"
        "Nami grabs her ponytail and pulls her head down."
        scene sba586 with vpunch
        "Bella retaliates by grabbing hers."
        n "Bitch! I'll whoop your bimbo ass!"
        b "TRY IT!"
        n "I'm doin' it!"
        scene sba587 with dssa
        mh "Stop it you two!"
        scene sba588 with dssr
        j "Are you okay?"
        d "...I feel like I'm... I'm gonna puke."
        scene sba589 with dssr
        n "Yo! Come up!"
        scene sba590 with dssa
        d "Don't touch me!"
        d "Let me just be here for a while..."
        scene sba591 with dssr
        n "Your nuts shall be avenged!"
        scene sba592 with dssr
        mh "Bella! Apologize!"
        scene sba593 with dssa
        b "Nope."
        scene sba592 with dssa
        mh "You don't want to get on the wrong side here."
        scene sba594 with dssa
        b "Try me."
        "Miss Hill shakes her head."
        scene sba595 with dssa
        mh "I'll take him to the nurse."
        scene sba596 with dssa
        pause
        scene black with Dissolve(2)
        with Pause(.5)
        stop music fadeout 2.0
        jump Claire2x0


label Claire2x0:
    $ play_playlist(playlist_Ch5_Nia)
    scene sba597 with dssb
    pause
    scene sba598 with dssr
    pause
    scene sba599 with dssa
    mh "What happened?"
    d "She's just an annoyance..."
    scene sba600 with dssr
    mh "That's not what I meant."
    mh "Why did you quit playing in high school?"
    "Your eyes meet hers."
    scene sba601 with dssr
    mh "I know you were playing for Tropics. We monitor promising athletes."
    mh "But one day you vanished from the team."
    scene sba602 with dssr
    nur "Can't you kids wait with injuring yourself a few weeks into the year?"
    scene sba603 with dssr
    nur "Ah, Demi... Who did you bring me?"
    scene sba604 with dssa
    mh "[name]."
    scene sba605 with dssa
    $ persistent.unlockedImageClaire1 = True
    d "I can smell the booze from here."
    scene sba606 with dssa
    nur "I'm still sobering up."
    scene sba607 with dssa
    mh "Don't let certain people hear that."
    scene sba608 with dssa
    mh "Take care, [name]."
    scene sba609 with dssr
    pause
    scene sba610 with dssr
    mh "And..."
    scene sba611 with dssa
    mh "If I don't see your name on the list for the basketball tryouts. I'll take the liberty to put it on there myself."
    scene sba612 with dssr
    cl "My name is Claire. What can I do for you, [name]?"
    scene sba613 with dssr
    d "Some blonde bitch rammed her knee into my crotch."
    scene sba614 with dssa
    cl "*Laughs* Ahh... Classic."
    scene sba615 with dssr
    cl "One second please."
    scene sba616 with dssr
    pause
    scene sba618 with dssa
    pause
    scene sba617 with dssa
    cl "*Mumbles* Off too a good start."
    scene sba619 with dssr
    cl "Let me take a look."
    scene sba620 with dssr
    pause
    scene sba621 with vpunch
    d "*Gasps* Don't put pressure on it!"
    scene sba622 with vpunch
    pause #sfx
    cl "I have to know if everything's alright."
    scene sba620 with dssa
    pause
    scene sba623 with dssr
    cl "Yeah, yeah. You're fine."
    cl "Put some cool pads in a towel and put them on your jewels when you're back home."
    scene sba624 with dssa
    d "Okay."
    scene sba623 with dssa
    cl "What caused the girl to do this to you?"
    scene sba624 with dssa
    "You raise a brow."
    scene sba625 with dssa
    cl "Oh come on! I want to know! I love college gossip."
    scene sba626 with dssr
    d "This Bella just dislikes me... And I dislike her too."
    scene sba627 with dssa
    cl "Bella..."
    scene sba628 with dssa
    cl "Blonde, ponytail... Yellow-green eyes, often sports a look on her face as if she's about to drown some puppies?"
    scene sba629 with dssa
    d "...Pretty accurate."
    scene sba628 with dssa
    cl "Did she do it on purpose?"
    scene sba629 with dssa
    d "(That's a weird question... They must know each other.)"
    menu:
        "*Lie* She didn't.":
            scene sba630 with dssa
            $ BNOP = False
            cl "I see."
        "Yeah, she did it on purpose.":
            scene sba630 with dssa
            $ BNOP = True
            cl "I see."
    scene sba631 with dssa
    cl "All good then."
    scene sba632 with dssr
    d "Thanks."
    scene sba633 with dssr
    pause
    scene sba634 with dssr
    pause
    scene sba635 with dssr
    cl "*Moans* Mhmmm... Good night."
    $ achievement.grant("MeetClaire")
    $ achievement.sync()
    scene black with Dissolve(2)
    with Pause(.5)
    jump ClassEnd2x0


label ClassEnd2x0:
    $ play_playlist(playlist_Ch1Bus)
    scene sba316 with dssb
    pause
    scene sba318 with dssr
    u "They did offer us free entrance to the event afterwards."
    na "At least you got something out of it."
    scene sba317 with dssa
    u "The event was amazing."
    scene sba320 with dssr
    pause
    scene sba637 with dssr
    b "I wanted to apologize."
    scene sba638 with dssr
    b "I know that life as an eunuch is hard enough. I shouldn't have added to it."
    scene sba639 with dssa
    d "You've got a really slapable face."
    scene sba638 with dssa
    b "And you look like you've been slapped for the better part of your life."
    scene sba640 with dssa
    d "I'm glad you'll end up in prison one day."
    scene sba641 with dssa
    b "Still better than what's awaiting you on that loooong lonely corridor you call your excuse of a life."
    scene sba642 with dssr
    ma "Please note down what we discuss today."
    scene sba643 with dssa
    b "Note it down."
    scene sba644 with dssa
    d "You do it."
    scene sba645 with dssa
    b "No."
    scene sba646 with dssa
    d "Rock, paper, worm."
    scene sba647 with dssa
    pause
    scene sba648 with dssr
    b "Best out of three?"
    d "No. You only got one shot."
    b "I won't need more."
    scene sba649
    with Pause(.2)
    scene sba650
    with Pause(.2)
    scene sba649
    with Pause(.2)
    scene sba650
    with Pause(.2)
    scene sba649
    with Pause(.2)
    scene sba650
    with Pause(.2)
    scene sba652 with vpunch
    pause
    scene sba651 with vpunch
    b "Fuck!"
    scene sba653 with dssr
    pause
    scene sba654 with dssa
    d "Your handwriting looks like some troll trying to write a love letter."
    scene sba655 with dssa
    b "Don't worry. I'll put more effort into writing your obituary."
    scene sba656 with dssr
    "You take on a comfy position."
    scene sba657 with dssa
    pause
    scene sba658 with dssa
    pause
    scene sba659 with vpunch
    pause
    scene sba660 with dssr
    pause
    scene sba661 with vpunch
    "She deflects your incoming pen attack-"
    scene sba662 with vpunch
    "You wrestle a little until-"
    scene sba663 with vpunch
    "-you both drop of your chairs onto the floor, where you manage to pin her."
    scene sba664 with vpunch
    b "Nooo!"
    scene sba665 with vpunch
    u "Miss Marla! These two are fighting!"
    scene sba666 with vpunch
    ev "Kick his ass, Bella!"
    scene sba667 with dssa
    ma "*Confused* What?"
    scene black with Dissolve(2)
    with Pause(.5)
    scene sba321 with vpunch
    ma "I don't care!"
    scene sba322 with vpunch
    ma "You both got five minutes to clean yourself up!"
    scene sba323 with dssr
    ma "What is this here?! A Kindergarten?!"
    d "She belongs to a place that treats people with special needs."
    ma "Five minutes and you're both back in class or God may have mercy on you."
    scene sba324 with dssr
    pause
    scene sba325 with dssa
    d "You're the most annoying shit I've ever met."
    scene sba326 with dssa
    b "You're the biggest excuse of a guy I've ever met."
    scene sba325 with dssa
    d "What is it? Why do you keep interacting with me?"
    scene sba327 with dssr
    d "Jesus! Just shut the fuck up and don't speak to me!"
    scene sba328 with dssa
    b "Yeah."
    b "That would totally bore me. I'd rather see you lose your marbles."
    scene sba329 with dssr
    b "If I'm forced to work with you emo cunt, I'll at least amuse myself."
    scene sba330 with dssa
    pause
    scene sba331 with dssa
    pause
    scene sba332 with dssr
    b "You fucking creep."
    b "Why did you write on my boobs?"
    scene sba333 with dssa
    d "I didn't. It's your upper chest."
    scene sba334 with dssr
    b "The boob begins here."
    d "I don't give a damn where your floppy pancakes begin."
    b "I have perfect boobs, you damn incel."
    scene sba335 with dssa
    d "What you just don't seem to understand is that I don't care about you."
    scene sba336 with dssa
    d "You could die today and I wouldn't remember you in a week."
    scene sba337 with dssa
    b "Wow."
    scene sba339 with dssa
    b "We found some common ground." #smiles
    scene sba340 with dssr
    pause
    scene sba341 with dssa
    pause
    scene sba342 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.4)
    scene sba343 with dssr
    pause
    scene sba344 with dssr
    d "Are you done?"
    scene sba345 with dssa
    pause
    scene sba346 with dssa
    pause
    scene sba348 with dssa
    d "I'll take that as a yes."
    jump ClassContinue2x0


label ClassContinue2x0:
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_GirlyPop)
    scene sba695 with dssb
    "Miss Marla shoots you and Bella an annoyed look as you enter the lecture hall."
    scene sba668 with dssr
    d "Note down what she has to say while I'll take a nap."
    scene sba694 with dssa
    pause
    scene sba696 with dssr
    ma "At the end of next week I'll review the first part of your work. You can earn bonus points if you've already figured out the type of disease."
    ma "Every team who earns 90 percent or higher, won't have to attend the extra classes."
    scene sba692 with dssr
    d "Please note that shit down before we have to spend even more time together."
    scene sba693 with dssr
    "Your words and the threat of having to spend even more time together must've had a vigorous effect on her, as she starts to note down stuff in a serious manner."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    with Pause(.5)
    $ play_playlist(playlist_Ch5_ViceCity2)
    scene sba697 with dssb
    pause
    scene sba698 with dssr
    v "Hey!"
    d "Hey."
    scene sba699 with dssr
    if VicDate is True:
        v "What are you up to today? I thought we could go on a date."
    else:
        v "What are you up to today? I thought we could meet up?"
    scene sba700 with dssa
    "Bella starts laughing."
    scene sba701 with dssa
    v "What's so funny?"
    scene sba704 with dssr
    b "Oh nothing."
    scene sba702 with dssr
    v "You must be Bella. We haven't spoken yet."
    scene sba705 with dssr
    b "Mhm."
    scene sba706 with dssa
    v "You've got striking eyes."
    scene sba707 with dssa
    b "Umm- uh- thanks?"
    scene sba702 with dssr
    v "But they're sad. I'm sorry for whatever happened to you."
    scene sba703 with dssr
    v "Coming back to our date."
    scene sba708 with dssr
    d "I'm sorry, I can't today."
    scene sba709 with dssa
    d "Bella and I didn't get to work yesterday due to an infant having an emotional outburst-"
    scene sba710 with dssa
    b "Fuck you."
    scene sba709 with dssa
    d "-and we have to put in some hours today."
    scene sba711 with dssa
    v "Hmm, sad. But okay!"
    scene sba713 with dssa
    v "If you and Bella need some help or a different pair of eyes, just ask me and Mila! We're happy to help."
    d "Thanks, but no."
    scene sba714 with dssr
    v "Alrighty. I'll see you!"
    scene sba715 with dssa
    d "I'll see you tomorrow, Vic."
    scene sba716 with dssa
    pause
    scene sba717 with dssa
    "Mila gives you a subtle smile as she follows Victoria outside."
    scene sba718 with dssr
    d "(Miss Marla keeps peeking at me. I think she needs to get something of her chest.)"
    scene sba719 with dssa
    d "Wait outside."
    scene sba720 with dssa
    b "Why?"
    scene sba721 with dssa
    d "I've got to talk to Miss Marla."
    scene sba720 with dssa
    b "She's not going to give us new partners."
    scene sba721 with dssa
    pause
    scene sba722 with dssr
    ma "Ah [name]? Do you have a minute?"
    scene sba723 with dssa
    d "Yeah."
    scene sba724 with dssa
    ma "I think it's... I think it's important that we talk about the incident."
    scene sba726 with dssa
    d "The incident where you hit Vic?"
    scene sba725 with dssa
    ma "...Yes. That one."
    scene sba732 with dssr
    "She nervously fiddles around with a pen."
    scene sba727 with dssr
    ma "I just want to say that there's no bad blood between us."
    ma "I won't treat you or your grades any different."
    scene sba728 with dssa
    d "I know. You don't give me that vibe."
    d "But I still don't like you as you put an innocent girl into-"
    scene sba727 with dssa
    ma "*Firm* I'm well aware."
    scene sba728 with dssa
    d "But that doesn't mean I'll behave, in some way, rude."
    d "There's nothing between us personally."
    scene sba727 with dssa
    ma "I'm glad to hear that."
    scene sba731 with dssa
    pause
    scene sba730 with dssa
    d "Just... One question."
    d "Why did the police never knock on my door?"
    scene sba729 with dssa
    ma "...We settled in private. There was no need to involve you."
    scene sba730 with dssa

    d "I see."
    scene sba733 with dssb
    pause
    scene sba734 with dssr
    pause
    scene sba735 with dssr
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene sba736 with dssb
    pause
    scene sba737 with dssr
    pause
    scene sba738 with dssr
    b "Where do you think you're going?"
    scene sba739 with dssa
    d "I'm looking for Nami."
    scene sba740 with dssa
    b "No. Come. We'll leave."
    scene sba741 with dssa
    d "Alright. Bye."
    scene sba742 with dssr
    pause
    scene sba743 with vpunch
    b "*Furious* You fucking ugly ass- noodle head!"
    scene sba744 with dssr
    "Furiously, she walks after you."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sba745 with dssb
    pause
    scene sba746 with dssr
    pause
    scene sba747 with dssa
    d "Cheeto!"
    scene sba748 with dssa
    n "YO!"
    scene sba749 with dssa
    d "Just wanted to catch you before we left."
    scene sba751 with dssr
    n "Do you want a hug?"
    scene sba750 with dssa
    n "A hug that protects you from blonde bimbos?"
    scene sba752 with dssa
    d "Nah, I'm good."
    scene sba753 with vpunch
    pause
    scene sba754 with dssr
    n "Bimbo protection granted."
    scene sba755 with dssa
    $ persistent.unlockedImageSonya1 = True
    n "Huh... Bimbo protection charms... I should sell that on Etsie."
    scene sba756 with dssa
    pause
    scene sba758 with dssr
    d "Hey."
    scene sba757 with dssa
    so "Hi."
    scene sba759 with dssa
    pause
    scene sba760 with dssr
    d "Let's go, fucker."
    scene black with Dissolve(2)
    with Pause(.5)
    show t2 with dssb
    jump BellaHouse2x0

label BellaHouse2x0:
    scene sd1 with dssb
    pause
    scene sd2 with dssa
    d "You found it?"
    b "Mh?"
    d "Did you look up the word?"
    scene sd3 with dssr
    b "Nah, but I just saw that the Wormy Girls concert is soon coming back to Wollust."
    scene sd4 with dssa
    d "Stop wasting time and get to work!"
    scene sd5 with dssa
    if bellameet is True:
        b "Did I tell you that the police was at the Holgerson's?"
        scene sd6 with dssa
        d "No."
        scene sd5 with dssa
        b "It seems like there's a full blown investigation."
        scene sd6 with dssa
        d "...Do they suspect anything?"
        scene sd7 with dssr
        b "If they did we'd already be in custody."
        d "*Sigh*"
        scene sd9 with dssa
        b "Don't piss yourself."
        d "We both know the justice system would fuck me much harder than you."
        scene sd10 with dssa
        b "Yeah." #content
    else:
        b "By the way, did I mention that I went on with the plan?"
        scene sd6 with dssa
        d "What plan?"
        scene sd5 with dssa
        b "Midnight."
        scene sd6 with dssa
        d "No? What did you do?"
        scene sd5 with dssa
        b "I sprayed some profanities on his car and went in through the backdoor."
        scene sd6 with dssa
        d "You broke in?"
        scene sd5 with dssa
        b "The door was open."
        scene sd8 with dssa
        d "Well, whatever you did... That's not my problem."
        scene sd9 with dssa
        b "Yeaaaah, about that..."
        b "You umm... Went into all of this because someone said some mean things to Mila, right?"
        scene sd10 with dssa
        b "Anyways, as far as I have heard, they think it was her and some of her low status friends."
        scene sd11 with dssa
        d "What? How do you know that?"
        scene sd9 with dssa
        b "My mama talked to them this morning and she told me."
    scene sd11 with dssa
    d "Alright let's-"
    scene sd12 with dssa
    b "Shut up."
    scene sd13 with dssa
    b "I hear voices... The voice of Stefan Holgerson."
    scene sd14 with dssr
    pause
    scene sd15 with dssa
    "She slides over her bed and runs out of the room."
    scene black with Dissolve(1)
    with Pause(.5)
    scene sd131 with dssr
    mf "And we thought you'd like to come."
    mf "I remember that Zoey always liked to chat with Bella."
    scene sd132 with dssa
    am "Yes. Bella and Zoey always got along well."
    scene sd133 with dssa
    mf "Well, great."
    scene sd134 with dssr
    mf "You'll get a formal invitation soon."
    scene sd135 with dssa
    am "Thank you very much, Stefan."
    scene sd136 with dssr
    pause
    scene sd137 with dssa
    "You and Bella sneak back to her room."
    scene black with Dissolve(2)
    with Pause(.5)
    scene sd16 with dssb
    b "I hate them!"
    scene sd17 with dssr
    pause
    scene sd18 with dssa
    b "My Mama's gonna come up soon... So shut up."
    scene sd19 with dssr
    pause
    scene sd20 with dssa
    am "Hello."
    scene sd22 with dssr
    d "Hello Amber."
    scene sd21 with dssa
    am "[name] it-... [name] Cyrus?"
    d "(She's my therapist?)"
    scene sd23 with dssa
    d "Oh, I know what you're getting at."
    scene sd24 with dssa
    am "Yes. Uh- Bella."
    scene sd25 with dssr
    b "Mh?"
    scene sd26 with dssa
    am "Somebody broke into the Holgerson's house last night."
    scene sd27 with dssa
    b "Okay? And?"
    scene sd32 with dssa
    am "What do you mean 'and'?"
    am "We could be the next."
    am "But... It appears as if they have a subject who might've been involved in the burglary."
    scene sd28 with dssr
    am "She's at ZPR. Mila Steiner."
    if bellameet is True:
        d "(What the fuck?)"
    else:
        d "(What did you do, Bella...)"
    scene sd27 with dssa
    b "Oh."
    scene sd26 with dssa
    am "So please make sure to lock the door."
    scene sd27 with dssa
    b "I will."
    scene sd26 with dssa
    am "You and I got invited to a Gala, where I want you to be."
    scene sd27 with dssa
    b "Since when? You said I could choose not to go."
    scene sd28 with dssa
    am "Not this time."
    "Bella sighs."
    scene sd29 with dssr
    am "Mister Holgerson told me that someone broke in their house."
    am "Please make sure to always double lock the doors."
    scene sd30 with dssa
    b "I will."
    scene sd31 with dssa
    b "But why on gods green earth would you say yes?"
    b "It's obvious that he's just after you!"
    scene sd32 with vpunch
    am "Bella! Mister Holgerson is married!"
    scene sd33 with dssa
    b "Right?! Because people don't cheat and this bitch Mario-"
    scene sd32 with vpunch
    am "Bella! Don't overdo it!"
    scene sd34 with dssr
    b "Why can't you see it..."
    scene sd35 with dssa
    pause
    scene sd36 with dssr
    am "I'm sorry [name]."
    scene sd37 with dssa
    d "Don't mind me."
    scene sd38 with dssr
    am "I'll leave you two alone."
    scene sd39 with dssr
    am "If you get hungry or need something to drink, just tell me."
    d "Sure. Thanks."
    scene sd40 with dssr
    d "(Her mother seems to be a very decent person.)"
    scene sd41 with dssa
    d "(I wonder what happened to you Bella. Nobody is born this retarded. I'm speaking from experience.)"
    scene sd42 with dssa
    if bellameet is False:
        d "What did you do last night? Why's Mila a subject?"
        b "I might've gone in and took a little heirloom with me."
        d "And blamed it on Mila?"
        scene sd43 with dssa
        b "Of course not!"
        scene sd41 with dssa
        d "You'll fix this."
        "She stays quiet."
    else:
        d "Why Mila? That makes no sense."
        scene sd43 with dssa
        b "I know."
        b "And this scares me more than if they had just come to me."
        scene sd41 with dssa
        d "We'll need to fix this."
        "She stays quiet."
    d "Do you think they're going to hit on your Mom at that gala?"
    scene sd43 with vpunch
    b "Shut the fuck up!"
    scene sd44 with dssr
    d "They must be... Damn... She better brings a spare change of clothes."
    scene sd45 with vpunch
    b "SHUT UP!"
    scene sd46 with dssr
    "You crawl towards the angry muppet."
    d "(She's so emotional... she can't think straight.)"
    d "(I could let her dance so easily...)"  #Doll
    scene sd47 with dssa
    "You take her hand."
    d "You can't protect her... You know that, right?"
    scene sd48 with dssa
    b "Of course I can!"
    scene sd49 with vpunch
    $ persistent.unlockedImageBellaCh2_1 = True
    b "Don't touch me!"
    scene sd50 with dssr
    d "I have an idea how to 'save' your mom."
    scene sd51 with dssa
    b "I don't care about your stupid ideas!"
    b "And I certainly don't need help from some third class villain."
    scene sd52 with dssa
    "You smile at her."
    scene sd54 with dssr
    pause
    scene sd53 with dssa
    d "Tell me about your plan."
    scene sd55 with dssa
    b "The second they do something, I'll act accordingly."
    scene sd56 with dssa
    d "Why would you even let it go that far?"
    scene sd57 with dssr
    pause
    scene sd58 with dssr
    d "Mario has a girlfriend, no?"
    b "He does."
    scene sd59 with dssr
    d "You say his father is a lusty guy... Can he resist her?"
    scene sd60 with dssa
    pause
    scene sd61 with dssa
    b "I think he would go for her."
    b "Let me repeat this... You're trying to tell me that we should set up a chain of events that lead to him hitting on his son's girlfriend? Which could destroy their whole family and bring unforeseeable consequences?"
    scene sd63 with dssa
    d "Yes."
    d "I'll have some fun and get a bit of revenge, and you can force them to leave your mother alone... unless he wants to lose his marriage and his son."
    scene sd62 with dssa
    b "I'm in."
    scene sd64 with dssr
    d "Good."
    b "You didn't make this up right now, did you?"
    d "I did. But I had been preparing some ideas in the back of my mind since they insulted Mila."
    scene sd65 with dssr
    b "Mila? Is that what this was all about?"
    scene sd66 with dssa
    d "No. I don't know her well enough to put this much effort into avenging someone I don't even really know."
    d "But I find it amusing to fuck with them, and it just so happens to align with the Mila situation."
    scene sd67 with dssa
    b "I mean you're both poor so I guess you've got a natural attraction to each other... When the heater stops working, you can cuddle to keep warm during a raging blizzard."
    scene sd68 with dssa
    d "Someday you'll get into my crosshair."
    scene sd69 with dssa
    b "I thought I already was."
    scene sd70 with dssr
    b "Who says all this here isn't to get back at me for making fun of Nami?"
    d "Time will tell."
    scene sd71 with dssa
    "She eyes you and smiles devilishly."
    scene sd72 with dssa
    b "When do we start? Today?"
    scene sd73 with dssa
    d "No? We can't do shit today."
    d "First we need to find his girlfriend."
    scene sd74 with dssr
    d "Do you know her?"
    scene sd75 with dssa
    b "No, we never really talked... Just by looking at her, I knew she's not my type of girl."
    scene sd74 with dssa
    d "Find her and befriend her."
    scene sd76 with dssa
    b "Done."
    scene sd77 with dssa
    d "We need to gain her trust, and then we need a spare key to the Holgersons house."
    scene sd78 with dssa
    b "I know how I could get a key..."
    scene sd79 with dssr
    b "Ugh... I'm so close to vomiting."
    b "Just leave this to me."
    scene sd80 with dssa
    d "I'm surprised to see how much you're into this."
    scene sd81 with dssa
    b "You have no idea how much I hate these people."
    b "But if you only want revenge for Mila... Why don't you set up something for Mario? Beat the shit out of him?"
    scene sd80 with dssa
    d "Again. It's not just about Mila. But we will get her out of there."
    scene sd83 with dssr
    d "I don't enjoy this simple shit anymore... I'd like to put some thought into it."
    d "I changed the plan to his father because it would help us both and would result in much more devastation."
    if majafavour is True:
        d "And I have someone who owes me a favor."
        d "She'll be useful."
        scene sd82 with dssa
        b "Who is it?"
        d "Victoria's sister, Maja."
        b "Okay."
    else:
        d "But we might need Nami anyways."
        scene sd82 with dssa
        b "For what?"
        d "Let's talk about it when the time comes."
    scene sd84 with dssr
    d "Besides that... We need someone who knows how to handle tech."
    d "It doesn't give us any leverage if he does cheat but we can't prove it."
    scene sd85 with dssa
    b "Ask one of your nerd friends."
    d "I don't have frie-."
    scene sd86 with dssa
    b "Why am I not surprised?"
    scene sd87 with dssa
    b "Fine. I'll befriend his girlfriend and we have to find someone with technical skills. But what will you do? It seems like I have all the work."
    d "I'll keep an eye on his father. I need to know where he goes to lunch, study his schedule, his friends, his behavior in general."
    scene sd88 with dssr
    b "He always has lunch at the same place. Relucia Dinner. Where all those rich idiots go to have dinner."
    scene sd89 with dssa
    d "Great. I'll visit this place a few times."
    scene sd88 with dssa
    b "*Giggles* You won't."
    scene sd89 with dssa
    d "Is it exclusive?"
    b "Mhm."
    d "Can you get in there?"
    scene sd90 with dssr
    b "*Giggles* Look at me. Of course I can."
    d "Then you have to do it, too."
    scene sd91 with vpunch
    b "No! I won't do everything!"
    scene sd92 with dssa
    d "*sigh* Then let's do this part together."
    d "You can get us in there."
    scene sd93 with vpunch
    b "No! I don't want to be seen with you!"
    scene sd94 with dssa
    d "Oh well, then please remember to send me the sex tape of your Mom and him."
    scene sd93 with vpunch
    b "You son of a bitch! Fine! But you can't wear these clothes!"
    scene sd95 with dssa
    b "You'll need fine dining clothes!"
    scene sd96 with dssa
    d "I can't afford them."
    scene sd97 with dssa
    b "I can't believe I am going to do this... I'll pay for it."
    scene sd98 with dssr
    d "Wow. You must really hate them."
    scene sd99 with dssa
    b "If you keep going like this you'll share their fate."
    scene sd100 with dssa
    d "That's cute."
    scene sd101 with dssa
    d "I'll leave now."
    scene sd102 with vpunch
    b "What? We're not done yet!"
    scene sd103 with dssa
    d "Yeah, but I've seen enough of you today."
    scene sd104 with dssr
    pause
    scene sd105 with vpunch
    "You hear her run up at you and turn around before she jumps you with full force."
    scene sd106 with vpunch
    d "What is wrong with you?!"
    pause
    scene sd107 with dssr
    b "We aren't so different, are we?"
    scene sd108 with vpunch
    d "Ugh... Do you have to come so fucking close?"
    d "Get off me!"
    scene sd109 with dssa
    b "Are you afraid of me?"
    scene sd110 with dssa
    d "Fuck you... And I'm not like you."
    scene sd109 with dssa
    b "Didn't you tell me that you know how complicated things can be?"
    scene sd110 with dssa
    "You say nothing."
    scene sd111 with dssr
    b "I listened."
    b "Tell me what happened."
    scene sd112 with dssa
    d "Only in exchange for your sister's story."
    scene sd113 with dssa
    b "No."
    scene sd114 with vpunch
    d "Then leave it... Now get off me!"
    scene sd115 with vpunch
    pause
    scene sd116 with dssr
    d "(I think I know what this is... She is agreeing with me more than she wants to and is now trying to re-establish dominance.)"
    d "(She knows too well that I don't feel comfortable when she comes too close to me. I can't let her get the upper hand though.)"
    scene sd117 with dssa
    d "I know the pain."
    scene sd118 with dssa
    b "Then tell me your story and I might tell you a little bit of mine."
    menu:
        "Tell her the story about Summer.":
            $ bella +=2
            $ bellasummer = True
            scene black with dssb
            with Pause(.5)
            scene sd119 with dssa
            "You tell her everything about the day at the cabin, but you keep it superficial."
            d "Then Jane drove us home.."
            d "And I can't remember more."
            scene sd122 with dssr
            b "Mhm.."
            b "Interesting, but not good enough for my story."
            d "Fuck you! Seriously!"
        "Don't tell her.":
            $ bellasummer = False
            scene sd120 with dssa
            d "No. I won't."
            scene sd121 with dssa
            b "It would've bored me anyways."
    scene sd124 with dssr
    d "I'm going home."
    scene sd125 with dssa
    b "Finally."
    scene sd126 with dssa
    pause
    if bellasummer is True:
        scene sd127 with dssa
        "An eerie silence falls over the room."
        scene sd128 with dssr
        pause
        scene sd129 with dssa
        pause
        scene sd130 with dssr
        pause
    scene black with Dissolve(1.5)
    with Pause(.5)
    scene sba909 with dssb
    pause
    scene sba910 with dssr
    pause
    scene sba911 with dssa
    with Pause(.3)
    scene sba911x with dssa
    with Pause(.5)
    show b_c_3 with dssr
    pause
    scene z402x with dssr
    pause
    scene sba911x with dssa
    show b_c_4 with dssa
    pause
    show b_c_5 with dssa
    pause
    show b_c_6 with dssa
    pause
    show b_c_7 with dssa
    pause
    show b_c_8 with dssa
    pause
    show b_c_9 with dssa
    pause
    show b_c_10 with dssa
    pause
    scene sba911x with dssa
    show b_c_13 with dssa
    pause
    show b_c_14 with dssa
    pause
    if bellameet is False and BNOP is False:
        show b_c_15 with dssa
        pause
        show b_c_16 with dssa
        pause
    else:
        pass
    scene sba911 with dssa
    "Your phone starts ringing. Displaying an unknown number."
    scene sba912 with dssa
    d "Yes?"
    scene sba913 with dssa
    maj "[name]? It's Maja."
    scene sba912 with dssa
    d "...What's up?"
    scene sba914 with dssr
    maj "Could you please come to Evangelina Street 11?"
    maj "It's at the eastern side of Wollust."
    scene sba915 with dssr
    d "Why?"
    scene sba916 with dssa
    maj "I have a situation with Victoria... And I can't-... I can't get her to stay..."
    scene sba915 with dssa
    d "...I'm on my way."
    scene sba917 with dssr
    "You let out a sigh."
    $ persistent.unlockedImageMaja1 = True
    $ play_playlist(playlist_AmbientCheeto)
    scene black with Dissolve(2)
    with Pause(.5)
    scene cba17 with dssb
    pause
    scene cba18 with dssr
    pause
    scene cba19 with dssr
    d "Hey."
    scene cba20 with vpunch
    pause
    d "..."
    scene cba21 with dssa
    maj "Thank you so much for coming."
    scene cba22 with dssr
    d "So... What's the situation?"
    scene cba23 with dssa
    maj "She totally came crashing down the moment we entered this place."
    scene cba24 with dssa
    maj "Victoria has always been a very positive person, but her reaction to this accident has been really weird!"
    maj "She acted even happier, as if the accident never happened and nothing was wrong..."
    scene cba25 with dssa
    d "She's in denial."
    scene cba26 with dssr
    maj "I think she must've realized that if this fails... She might be bound to this chair for the rest of her life. That all this isn't just a bad dream."
    scene cba27 with dssa
    d "And what should I do?"
    scene cba28 with dssa
    maj "She cried and begged me to take her home..."
    maj "I tried everything to keep her here... she wouldn't listen."
    d "Where is she now?"
    scene cba29 with dssr
    maj "In the waiting room."
    scene cba30 with dssa
    maj "I told her that I have to talk to someone, and after that, we'll leave."
    scene cba31 with dssr
    d "You want me to speak to her?"
    scene cba32 with dssa
    maj "Yes, please!"
    scene cba33 with dssa
    d "Alright."
    d "You wait here... I need to be alone with her."
    scene cba34 with dssa
    d "(I know what I have to do... I know how to get Victoria to stay...)"
    scene cba36 with dssa
    d "(I care about her... I can't deny it anymore.)"
    if vicdate is True:
        d "(But I still feel too weird to do more.)"
    scene cba35 with dssa
    pause
    scene black with Dissolve(2)
    with Pause(.5)
    scene ee264 with dssb
    pause
    scene ee265 with dssr
    v "*Sobbing*."
    scene ee266 with dssr
    "You gently place your hand on her shoulder."
    scene cba2 with dssa
    v "Maj-ja can we g-go now?"
    scene cba3 with dssa
    d "I'd rather have you stay."
    scene cba4 with vpunch
    v "*Gasp*! [name]!"
    scene cbba52 with vpunch
    v "No! No! Y-You're not supposed to see me like this!"
    v "Please no!"
    scene cba5 with dssr
    d "Victoria..."
    scene cba6 with dssr
    "You gently turn her around."
    d "This might be the hardest thing you'll ever have to do... I- I'm in desperate need to let go of my past, and the worst thing you could do is to live in denial... to not face your fears... and to end up like me..."
    d "Every time I... try to let go, I feel like I'm suffocating. My heart races, and I'm on the threshold of a panic attack..."
    if vicdate is True:
        d "It took a lot of courage for me to ask you on a date... But it was a first, and a very important step for me. I might not show affection the way other people do... but it's there."
        d "I still feel *deep breath* vulnerable, scared, and alone..."
    scene cba8 with dssr
    v "I-"
    d "I'm not done."
    scene cba9 with dssr
    if vicdate is True:
        d "Let me be your companion on this journey. Let me lend you my hand on all those difficult days to come... and no matter which direction you're headed... I'll be by your side... 'til the very end."
        d "...And I'll need your hand as well... more than you might think..."
    else:
        d "Let's not let our fear guide us... We both have nothing to lose but a lot to win."
    scene cba10 with dssr
    menu:
        "I promise you.":
            $ achievement.grant("ThePromise")
            $ achievement.sync()
            $ vici +=5
            $ vicpromise = True
        "End it there.":
            pause
    scene cba11 with dssa
    v "[name] I.."
    $ persistent.unlockedImageVic1 = True
    v "Thank... Thank you so m-much for being here..."
    scene cba12 with dssr
    d "Come here... come up."
    v "What?"
    scene cba13 with dssr
    "You grab her under her arms and lift her up."
    v "Aah-h"
    scene cba14 with dssr
    "Her body is shaking. She desperately grabs onto you... pulling herself closer..."
    scene cba15 with dssa
    d "*whisper* ...You're not alone."
    scene cba16 with dssr
    pause
    scene black with Dissolve(3.5)
    show text "End of Chapter 2." with Dissolve(1.5)
    with Pause(1.5)
    jump startch3
