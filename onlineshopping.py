#name=akash more 
#div=M batch=M2
#roll no=41 Gr  no=11810832
from easygui import *
import sys
sum=0
while 1:
    msgbox("ONLINE SHOPPING")
    msg ="CHOOSE YOUR WEBSITE?"
    title = "WEBSITES"
    choices = ["AMAZON", "FLIPKART"]
    choice = choicebox(msg, title, choices)
    if choice=="AMAZON" or choice=="FLIPKART":
        m1="CATEGORIES:"
        t1="CATEGORIES"
        c1=["ELECTRONICS","CLOTHING"]
        ch1=choicebox(m1,t1,c1)
        if ch1=="ELECTRONICS":
            m11="CATEGORIES"
            t11="CATEGORIES"
            c11=["MOBILES","TELEVISION","HEADPHONES"]
            ch11=choicebox(m11,t11,c11)
            if ch11=="MOBILES":
                m111="SELECT BRAND"
                t111="BRANDS"
                c111=["SAMSUNG","NOKIA","ONE PLUS","XIAOMI","OPPO","VIVO"]
                ch111=choicebox(m111,t111,c111)
                if ch111=="SAMSUNG":
                    m1111="SELECT YOUR CHOICE"
                    t1111="SAMSUNG MOBILES"
                    c1111=["SAMSUNG GALAXY NOTE 9(8GB RAM + 512GB \ 4000MAH \ ANDROID 8.1) : RS.84,900","SAMSUNG GALAXY S9 PLUS(6GB RAM + 256GB \ 3500MAH \ ANDROID 8.0) : RS.62,390.00","SAMSUNG GALAXY A7(4GB RAM + 64GB \ 3300MAH \ ANDROID 8.0) : RS.23,990.00"]
                    ch1111=choicebox(m1111,t1111,c1111)
                    x1=str(ch1111)
                    msgbox(x1)
                    if x1=="SAMSUNG GALAXY NOTE 9(8GB RAM + 512GB \ 4000MAH \ ANDROID 8.1) : RS.84,900":
                        sum+=84900
                    elif x1=="SAMSUNG GALAXY S9 PLUS(6GB RAM + 256GB \ 3500MAH \ ANDROID 8.0) : RS.62,390.00":
                        sum+=62390
                    else:
                        sum+=23990
                    msgbox("BILL : " +str(sum))    
                    m11111="DO YOU WANT TO SHOP MORE?"
                    t11111="FINISHED SHOPPING?"
                    if ccbox(m11111,t11111):
                        pass
                    else:
                        sys.exit(0)
                if ch111=="NOKIA":
                    m1112="SELECT YOUR CHOICE"
                    t1112="NOKIA MOBILES"
                    c1112=["NOKIA 6.1 PLUS(4GB RAM + 64GB \ 3060MAH \ ANDROID 8.1) : RS.15,999.00","NOKIA 9(8GB RAM + 256GB \ 3900MAH \ ANDROID 8.0) : RS.54,990.00","NOKIA P1(6GB RAM + 128GB \ 3500MAH \ ANDROID 7.0) : RS.40,990.00"]
                    ch1112=choicebox(m1112,t1112,c1112)
                    x2=str(ch1112)
                    msgbox(x2)
                    if x2=="NOKIA 6.1 PLUS(4GB RAM + 64GB \ 3060MAH \ ANDROID 8.1) : RS.15,999.00":
                        sum+=15999
                    elif x2=="NOKIA 9(8GB RAM + 256GB \ 3900MAH \ ANDROID 8.0) : RS.54,990.00":
                        sum+=54990
                    else:
                        sum+=40990
                    msgbox("BILL : " +str(sum))    
                    m11122="DO YOU WANT TO SHOP MORE?"
                    t11122="FINISHED SHOPPING?"
                    if ccbox(m11122,t11122):
                        pass
                    else:
                        sys.exit(0)
                if ch111=="OPPO":
                    m1113="SELECT YOUR CHOICE"
                    t1113="OPPO MOBILES"
                    c1113=["OPPO F9 PRO(6GB RAM + 64GB \ 3500MAH \ ANDROID 8.1) : RS.23,858.00","OPPO A5(4GB RAM + 32GB \ 4230MAH \ ANDROID 8.1) : RS.14,850.00","OPPO FIND X(LAMBORGHINI EDITION)(8GB RAM +512GB \ 3400MAH \ ANDROID 9.0) : RS.1,29,000.00"]
                    ch1113=choicebox(m1113,t1113,c1113)
                    x3=str(ch1113)
                    msgbox(x3)
                    if x3=="OPPO F9 PRO(6GB RAM + 64GB \ 3500MAH \ ANDROID 8.1) : RS.23,858.00":
                        sum+=23858
                    elif x3=="OPPO A5(4GB RAM + 32GB \ 4230MAH \ ANDROID 8.1) : RS.14,850.00":
                        sum+=14850
                    else:
                        sum+=129000
                    msgbox("BILL : " +str(sum))    
                    m11133="DO YOU WANT TO SHOP MORE?"
                    t11133="FINISHED SHOPPING?"
                    if ccbox(m11133,t11133):
                        pass
                    else:
                        sys.exit(0)
                if ch111=="VIVO":
                    m1114="SELECT YOUR CHOICE"
                    t1114="VIVO MOBILES"
                    c1114=["VIVO V11 PRO(6B RAM + 64 \ 3400MAH \ ANDROID 8.1) : RS.23,599","VIVO Y81(3GB RAM + 32GB \ 3260MAH \ ANDROID 8.1) : RS.11,199.00","VIVO NEX S(8GB RAM +256GB \ 4000MAH \ ANDROID 8.1) : RS.71,769.00"]
                    ch1114=choicebox(m1114,t1114,c1114)
                    x4=str(ch1114)
                    msgbox(x4)
                    if x4=="VIVO V11 PRO(6B RAM + 64 \ 3400MAH \ ANDROID 8.1) : RS.23,599":
                        sum+=23599
                    elif x4=="VIVO Y81(3GB RAM + 32GB \ 3260MAH \ ANDROID 8.1) : RS.11,199.00":
                        sum+=11199
                    else:
                        sum+=71769
                    msgbox("BILL : " +str(sum))    
                    m11144="DO YOU WANT TO SHOP MORE?"
                    t11144="FINISHED SHOPPING?"
                    if ccbox(m11144,t11144):
                        pass
                    else:
                        sys.exit(0)
                if ch111=="ONE PLUS":
                    m1115="SELECT YOUR CHOICE"
                    t1115="ONE PLUS MOBILES"
                    c1115=["ONE PLUS 6(8GB RAM + 512GB \ 3300MAH \ ANDROID 9.0) : RS.39,900.00","ONE PLUS 6T(8GB RAM + 512GB \ 4000MAH \ ANDROID 9.0) : RS.45,900.00"]
                    ch1115=choicebox(m1115,t1115,c1115)
                    x5=str(ch1115)
                    msgbox(x5)
                    if x5=="ONE PLUS 6(8GB RAM + 512GB \ 3300MAH \ ANDROID 9.0) : RS.39,900.00":
                        sum+=39900
                    else:
                        sum+=45900
                    msgbox("BILL : " +str(sum))
                    m11155="DO YOU WANT TO SHOP MORE?"
                    t11155="FINISHED SHOPPING?"
                    if ccbox(m11155,t11155):
                        pass
                    else:
                        sys.exit(0)
                if ch111=="XIAOMI":
                    m1116="SELECT YOUR CHOICE"
                    t1116="XIAOMI MOBILES"
                    c1116=["XIAOMI REDMI NOTE 5 PRO(4GB RAM + 64GB \ 4000MAH \ ANDROID 7.1.2) : RS.12,999.00","XIAOMI REDMI 6 PRO(3GB RAM + 32GB \ 4000MAH \ ANDROID 8.1) : RS.10,999.00","XIAOMI MI 8 EXPLORER EDITION(8GB RAM + 128GB \ 3000MAH \ ANDROID 8.1) : RS.55,657.00"]
                    ch1116=choicebox(m1116,t1116,c1116)
                    x6=str(ch1116)
                    msgbox(x6)
                    if x6=="XIAOMI REDMI NOTE 5 PRO(4GB RAM + 64GB \ 4000MAH \ ANDROID 7.1.2) : RS.12,999.00":
                        sum+=12999
                    elif x6=="XIAOMI REDMI 6 PRO(3GB RAM + 32GB \ 4000MAH \ ANDROID 8.1) : RS.10,999.00":
                        sum+=10999
                    else:
                        sum+=55657
                    msgbox("BILL : " +str(sum))
                    m11166="DO YOU WANT TO SHOP MORE?"
                    t11166="FINISHED SHOPPING?"
                    if ccbox(m11166,t11166):
                        pass
                    else:
                        sys.exit(0)
            if ch11=="TELEVISION":
                m112="SELECT BRAND"
                t112="BRANDS"
                c112=["SAMSUNG","SONY","LG"]
                ch112=choicebox(m112,t112,c112)
                if ch112=="SAMSUNG":
                    m1121="SELECT YOUR CHOICE"
                    t1121="SAMSUNG TELEVISIONS"
                    c1121=["SAMSUNG 75Q8C (75 INCH) ULTRA HD CURVED QLED SMART TV : RS.5,99,000.00","SAMSUNG 43NU7470 (43 INCH) ULTRA HD 4K SMART LED TV : RS.55,340.00","SAMSUNG 32M5570 (32 INCH) FULL HD LED SMART TV : RS.25,900.00"]
                    ch1121=choicebox(m1121,t1121,c1121)
                    y1=str(ch1121)
                    msgbox(y1)
                    if y1=="SAMSUNG 75Q8C (75 INCH) ULTRA HD CURVED QLED SMART TV : RS.5,99,000.00":
                        sum+=599000
                    elif y1=="SAMSUNG 43NU7470 (43 INCH) ULTRA HD 4K SMART LED TV : RS.55,340.00":
                        sum+=55340
                    else:
                        sum+=25900
                    msgbox("BILL : " +str(sum))
                    m11211="DO YOU WANT TO SHOP MORE?"
                    t11211="FINISHED SHOPPING?"
                    if ccbox(m11211,t11211):
                        pass
                    else:
                        sys.exit(0)
                if ch112=="SONY":
                    m1122="SELECT YOUR CHOICE"
                    t1122="SONY TELEVISIONS"
                    c1122=["SONY KLV-32W672F (32 INCH) FULL HD LED SMART TV : RS.33,320.00","SONY KD-55X8500F (55 INCH) ULTRA HD 4K LED SMART TV : RS.1,04,499.00","SONY KD-85X9000F (85 INCH) 4K LED SMART TV : RS.9,32,642.00"]
                    ch1122=choicebox(m1122,t1122,c1122)
                    y2=str(ch1122)
                    msgbox(y2)
                    if y2=="SONY KLV-32W672F (32 INCH) FULL HD LED SMART TV : RS.33,320.00":
                        sum+=33320
                    elif y2=="SONY KD-55X8500F (55 INCH) ULTRA HD 4K LED SMART TV : RS.1,04,499.00":
                        sum+=104499
                    else:
                        sum+=932642
                    msgbox("BILL : " +str(sum))
                    m11222="DO YOU WANT TO SHOP MORE?"
                    t11222="FINISHED SHOPPING?"
                    if ccbox(m11222,t11222):
                        pass
                    else:
                        sys.exit(0)
                if ch112=="LG":
                    m1123="SELECT YOUR CHOICE"
                    t1123="LG TELEVISIONS"
                    c1123=["LG 43UK6360PTE (43 INCH) 4K ULTRA HD SMART TV : RS.46,730.00","LG 32LJ573D (32 INCH) HD READY LED SMART TV : RS.20,990.00","LG OLED77W8PTA (77 INCH) ULTRA HD SIGNATURE SMART OLED TV : RS.32,99,990.00"]
                    ch1123=choicebox(m1123,t1123,c1123)
                    y3=str(ch1123)
                    msgbox(y3)
                    if y3=="LG 43UK6360PTE (43 INCH) 4K ULTRA HD SMART TV : RS.46,730.00":
                        sum+=47730
                    elif y3=="LG 32LJ573D (32 INCH) HD READY LED SMART TV : RS.20,990.00":
                        sum+=20990
                    else:
                        sum+=3299990
                    msgbox("BILL : " +str(sum))
                    m11233="DO YOU WANT TO SHOP MORE?"
                    t11233="FINISHED SHOPPING?"
                    if ccbox(m11233,t11233):
                        pass
                    else:
                        sys.exit(0)                        
            if ch11=="HEADPHONES":
                m113="SELECT BRAND"
                t113="BRANDS"
                c113=["JBL","BOAT","SENNHEISER"]
                ch113=choicebox(m113,t113,c113)
                if ch113=="JBL":
                    m1131="SELECT YOUR CHOICE"
                    t1131=" JBL HEADPHONES"
                    c1131=["JBL CS100SI (WIRED) : RS.749.00","JBL XX125 (WIRELESS) : RS.1,299.00"]
                    ch1131=choicebox(m1131,t1131,c1131)
                    z1=str(ch1131)
                    msgbox(z1)
                    if z1=="JBL CS100SI (WIRED) : RS.749.00":
                        sum+=749
                    else:
                        sum+=1299
                    msgbox("BILL : " +str(sum))
                    m11311="DO YOU WANT TO SHOP MORE?"
                    t11311="FINISHED SHOPPING?"
                    if ccbox(m11311,t11311):
                        pass
                    else:
                        sys.exit(0)
                if ch113=="BOAT":
                    m1132="SELECT YOUR CHOICE"
                    t1132="BOAT HEADPHONES"
                    c1132=["BOAT SL500 (WIRED) : RS.1,999.00","BOAT BL200 (WIRELESS) : RS.5,999.00"]
                    ch1132=choicebox(m1132,t1132,c1132)
                    z2=str(ch1132)
                    msgbox(z2)
                    if z2=="BOAT SL500 (WIRED) : RS.1,999.00":
                        sum+=1999
                    else:
                        sum+=5999
                    msgbox("BILL : " +str(sum))
                    m11322="DO YOU WANT TO SHOP MORE?"
                    t11322="FINISHED SHOPPING?"
                    if ccbox(m11322,t11322):
                        pass
                    else:
                        sys.exit(0)
                if ch113=="SENNHEISER":
                    m1133="SELECT YOUR CHOICE"
                    t1133="SENNHEISER HEADPHONES"
                    c1133=["SENNHEISER 220WT (WIRED) : RS.1,599.00","SENNHEISER 425XT (WIRELESS) : RS.6,729.00"]
                    ch1133=choicebox(m1133,t1133,c1133)
                    z3=str(ch1133)
                    msgbox(z3)
                    if z3=="SENNHEISER 220WT (WIRED) : RS.1,599.00":
                        sum+=1599
                    else:
                        sum+=6729
                    msgbox("BILL : " +str(sum))
                    m11333="DO YOU WANT TO SHOP MORE?"
                    t11333="FINISHED SHOPPING?"
                    if ccbox(m11333,t11333):
                        pass
                    else:
                        sys.exit(0)
        if ch1=="CLOTHING":
            m2="CHOOSE YOUR CATEGORY"
            t2="CATEGORIES"
            c2=["MEN","WOMEN"]
            ch2=choicebox(m2,t2,c2)
            if ch2=="MEN":
                m21="WHAT DO YOU WANNA BUY?"
                t21="MEN CLOTHING"
                c21=["SHIRTS","T-SHIRTS","JEANS"]
                ch21=choicebox(m21,t21,c21)
                if ch21=="SHIRTS":
                    m211="WHICH SHIRT?"
                    t211="MEN SHIRTS"
                    c211=["PRINTED","CASUAL","FORMALS"]
                    ch211=choicebox(m211,t211,c211)
                    if ch211=="PRINTED":
                        m2111="OPTIONS AVAILABLE :"
                        t2111="PRINTED MEN SHIRTS"
                        c2111=["ALLEN SOLLY(DOGGY PRINT)(PINK CLOUR / BROWN PRINT) : RS.2,999.00","VAN HEUSEN(SKETCHY PRINT)(LIGHT BLUE COLOUR / DARK BLUE PRINT) : RS.3,599.00"]
                        ch2111=choicebox(m2111,t2111,c2111)
                        xx1=str(ch2111)
                        msgbox(xx1)
                        if xx1=="ALLEN SOLLY(DOGGY PRINT)(PINK CLOUR / BROWN PRINT) : RS.2,999.00":
                            sum+=2999
                        else:
                            sum+=3599
                        msgbox("BILL : " +str(sum))
                        m21111="DO YOU WANT TO SHOP MORE?"
                        t21111="FINISHED SHOPPING?"
                        if ccbox(m21111,t21111):
                            pass
                        else:
                            sys.exit(0)
                    if ch211=="CASUAL":
                        m2112="OPTIONS AVAILABLE :"
                        t2112="CASUAL MEN SHIRTS"
                        c2112=["ALLEN SOLLY(BOX TYPE)(ORANGE / BLUE / WHITE) : RS.3,999.00","VAN HEUSEN(STRIPPED)(PINK / BLUE) : RS.2,999.00"]
                        ch2112=choicebox(m2111,t2111,c2111)
                        xx2=str(ch2112)
                        msgbox(xx2)
                        if xx2=="ALLEN SOLLY(BOX TYPE)(ORANGE / BLUE / WHITE) : RS.3,999.00":
                            sum+=3999
                        else:
                            sum+=2999
                        msgbox("BILL : " +str(sum))
                        m21112="DO YOU WANT TO SHOP MORE?"
                        t21112="FINISHED SHOPPING?"
                        if ccbox(m21112,t21112):
                            pass
                        else:
                            sys.exit(0)  
                    if ch211=="FORMALS":
                        m2113="OPTIONS AVAILABLE :"
                        t2113="FORMAL MEN SHIRTS"
                        c2113=["ALLEN SOLLY(FORMAL)(WHITE) : RS.2,999.00","VAN HEUSEN(FORMAL)(BLACK) : RS.3,799.00"]
                        ch2113=choicebox(m2113,t2113,c2113)
                        xx3=str(ch2113)
                        msg(xx3)
                        if xx3=="ALLEN SOLLY(FORMAL)(WHITE) : RS.2,999.00":
                            sum+=2999
                        else:
                            sum+=3799
                        msgbox("BILL : " +str(sum))    
                        m21113="DO YOU WANT TO SHOP MORE?"
                        t21113="FINISHED SHOPPING?"
                        if ccbox(m21113,t21113):
                            pass
                        else:
                            sys.exit(0)
                if ch21=="T-SHIRTS":
                    m212="WHICH T-SHIRT?"
                    t212="MEN T-SHIRTS"
                    c212=["MARVEL IRONMAN : RS.599.00","DC BATMAN : RS.999.00","SOLID T-SHIRT(ANY COLOUR) : RS.299.00"]
                    ch212=choicebox(m212,t212,c212)
                    xx4=str(ch212)
                    msgbox(xx4)
                    if xx4=="MARVEL IRONMAN : RS.599.00":
                        sum+=599
                    elif xx4=="DC BATMAN : RS.999.00":
                        sum+=999
                    else:
                        sum+=299
                    msgbox("BILL : " +str(sum))    
                    m2121="DO YOU WANT TO SHOP MORE?"
                    t2121="FINISHED SHOPPING?"
                    if ccbox(m2121,t2121):
                        pass
                    else:
                        sys.exit(0)
                if ch21=="JEANS":
                    m213="WHICH JEANS?"
                    t213="MEN JEANS"
                    c213=["OXEMBERG(BLUE) : RS.2,599.00","LEVI(BLACK) : RS.3,999.00"]
                    ch213=choicebox(m213,t213,c213)
                    xx5=str(ch213)
                    msgbox(xx5)
                    if xx5=="OXEMBERG(BLUE) : RS.2,599.00":
                        sum+=2599
                    else:
                        sum+=3999
                    msgbox("BILL : " +str(sum))    
                    m2131="DO YOU WANT TO SHOP MORE?"
                    t2131="FINISHED SHOPPING?"
                    if ccbox(m2131,t2131):
                        pass
                    else:
                        sys.exit(0)
            if ch2=="WOMEN":
                m22="WHAT DO YOU WANNA BUY?"
                t22="WOMEN CLOTHING"
                c22=["SHIRTS","T-SHIRTS","JEANS"]
                ch22=choicebox(m22,t22,c22)
                if ch22=="SHIRTS":
                    m221="WHICH SHIRT?"
                    t221="WOMEN SHIRTS"
                    c221=["PRINTED","CASUAL","FORMALS"]
                    ch221=choicebox(m221,t221,c221)
                    if ch221=="PRINTED":
                        m2211="OPTIONS AVAILABLE :"
                        t2211="PRINTED WOMEN SHIRTS"
                        c2211=["ALLEN SOLLY(DOGGY PRINT)(PINK CLOUR / BROWN PRINT) : RS.2,999.00","VAN HEUSEN(SKETCHY PRINT)(LIGHT BLUE COLOUR / DARK BLUE PRINT) : RS.3,599.00"]
                        ch2211=choicebox(m2211,t2211,c2211)
                        xx6=str(ch2211)
                        msgbox(xx6)
                        if xx6=="ALLEN SOLLY(DOGGY PRINT)(PINK CLOUR / BROWN PRINT) : RS.2,999.00":
                            sum+=2999
                        else:
                            sum+=3599
                        msgbox("BILL : " +str(sum))    
                        m22111="DO YOU WANT TO SHOP MORE?"
                        t22111="FINISHED SHOPPING?"
                        if ccbox(m22111,t22111):
                            pass
                        else:
                            sys.exit(0)
                    if ch221=="CASUAL":
                        m2212="OPTIONS AVAILABLE :"
                        t2212="CASUAL WOMEN SHIRTS"
                        c2212=["ALLEN SOLLY(BOX TYPE)(ORANGE / BLUE / WHITE) : RS.3,999.00","VAN HEUSEN(STRIPPED)(PINK / BLUE) : RS.2,999.00"]
                        ch2212=choicebox(m2212,t2212,c2212)
                        xx7=str(ch2212)
                        msgbox(xx7)
                        if xx7=="ALLEN SOLLY(BOX TYPE)(ORANGE / BLUE / WHITE) : RS.3,999.00":
                            sum+=3999
                        else:
                            sum+=2999
                        msgbox("BILL : " +str(sum))    
                        m22112="DO YOU WANT TO SHOP MORE?"
                        t22112="FINISHED SHOPPING?"
                        if ccbox(m22112,t22112):
                            pass
                        else:
                            sys.exit(0)  
                    if ch221=="FORMALS":
                        m2213="OPTIONS AVAILABLE :"
                        t2213="FORMAL WOMEN SHIRTS"
                        c2213=["ALLEN SOLLY(FORMAL)(WHITE) : RS.2,999.00","VAN HEUSEN(FORMAL)(BLACK) : RS.3,799.00"]
                        ch2213=choicebox(m2213,t2213,c2213)
                        xx8=str(ch2213)
                        msg(xx8)
                        if xx8=="ALLEN SOLLY(FORMAL)(WHITE) : RS.2,999.00":
                            sum+=2999
                        else:
                            sum+=3799
                        msgbox("BILL : " +str(sum))    
                        m22113="DO YOU WANT TO SHOP MORE?"
                        t22113="FINISHED SHOPPING?"
                        if ccbox(m22113,t22113):
                            pass
                        else:
                            sys.exit(0)
                if ch22=="T-SHIRTS":
                    m222="WHICH T-SHIRT?"
                    t222="MEN T-SHIRTS"
                    c222=["MARVEL IRONMAN(CROP TOP) : RS.599.00","DC BATMAN : RS.999.00","SOLID T-SHIRT(ANY COLOUR)(CROP TOP) : RS.299.00"]
                    ch222=choicebox(m222,t222,c222)
                    xx9=str(ch222)
                    msgbox(xx9)
                    if xx9=="MARVEL IRONMAN(CROP TOP) : RS.599.00":
                        sum+=599
                    elif xx9=="DC BATMAN : RS.999.00":
                        sum+=999
                    else:
                        sum+=299
                    msgbox("BILL : " +str(sum))    
                    m2221="DO YOU WANT TO SHOP MORE?"
                    t2221="FINISHED SHOPPING?"
                    if ccbox(m2221,t2221):
                        pass
                    else:
                        sys.exit(0)
                if ch22=="JEANS":
                    m223="WHICH JEANS?"
                    t223="WOMEN JEANS"
                    c223=["OXEMBERG(BLUE) : RS.2,599.00","LEVI(BLACK) : RS.3,999.00"]
                    ch223=choicebox(m223,t223,c223)
                    xx10=str(ch223)
                    msgbox(xx10)
                    if xx10=="OXEMBERG(BLUE) : RS.2,599.00":
                        sum+=2599
                    else:
                        sum+=3999
                    msgbox("BILL : " +str(sum))    
                    m2231="DO YOU WANT TO SHOP MORE?"
                    t2231="FINISHED SHOPPING?"
                    if ccbox(m2231,t2231):
                        pass
                    else:
                        sys.exit(0)

An exception has occurred, use %tb to see the full traceback.

SystemExit: 0


