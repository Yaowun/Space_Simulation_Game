'''太空系模擬器'''

import sys
import pygame
import pandas as pd

def creatmap():
    '''定義建立地圖的方法'''
    screen.blit(screen,(0,0))
    pygame.display.update()

def print_text(screen,size,text,x,y,fcolor): #字體大小30，一行30字
    font = pygame.font.Font('Xiufeng.ttc',size)
    imgtext = font.render(text,True,fcolor)
    screen.blit(imgtext,(x,y))

def image_set(folder,number,sizex,sizey,x,y): #image_set('資料夾名稱',檔名,x大小,y大小,x位置,y位置)
    name=pygame.image.load('./'+folder+'/'+str(number)+'.png')
    name=pygame.transform.scale(name,(sizex, sizey))
    name.convert
    screen.blit(name,(x,y))
    
def image_setgif(folder,number,sizex,sizey,x,y): #image_set('資料夾名稱',檔名,x大小,y大小,x位置,y位置)
    name=pygame.image.load('./'+folder+'/'+str(number)+'.gif').convert_alpha()
    name=pygame.transform.scale(name, (sizex, sizey))
    name.convert
    screen.blit(name,(x,y))
    
def mousedown(xsta,xend,ysta,yend):
    if xsta<pygame.mouse.get_pos()[0]<xend and ysta<pygame.mouse.get_pos()[1]<yend:
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True
     
def talk_image():
    image_set('txtimage',0,940,190,10,530)
    image_set('txtimage','next',30,40,880,650)
       
def gain():
    data = chooselist
    global thing
    global thingone
    number = 0
    thingone = [[0]*len(thingname[0]),[0]*len(thingname[1]),[0]*len(thingname[2]),[0]*len(thingname[3]),[0]*len(thingname[4])]
    for i in range(0,len(thingname)):
        for j in range(0,len(thingname[i])):
            planx=pd.value_counts(data) 
            if thingname[i][j] in data:
                number = planx[thingname[i][j]]
                thing[i][j] += number
                thingone[i][j] = number
                
def Fight_event():
    time = [1,7,15,25,40]
    time2 = [0,0,13,25,37]
    fightability = [[2,1,3],[1,3,2],[3,2,1]]
    global ability
    global thingone
    global fightabilitybonus
    global calendercount
    #while Fightstart:
    for whfight in range(0,3):
        Fightstart =False
        ability[0]+=fightability[whfight][0]*thingone[3][whfight]
        ability[1]+=fightability[whfight][1]*thingone[3][whfight]
        ability[3]+=fightability[whfight][2]*thingone[3][whfight]
        for whevent in range(0,5):
            if thing[3][whfight]>=time[whevent] and thingone[3][whfight]!=0 and thing[3][whfight]-thingone[3][whfight] <= time[whevent] and calendercount>=time2[whevent]:
                Fightstart = True
            while Fightstart:
                image_set('Fight',str(whfight)+str(whevent),960,720,0,0)
                talk_image()
                print_text(screen,30,'獲得成就：('+ work_achieve[whfight][whevent] +')',40,580,black)
                print_text(screen,30,work_story[whfight][whevent],40,640,black)
                creatmap()
                ability[0]+=fightabilitybonus[whfight][whevent][0]
                ability[1]+=fightabilitybonus[whfight][whevent][1]
                ability[3]+=fightabilitybonus[whfight][whevent][2]
                pygame.time.delay(1000)
                Fightstart = False

def social():
    global ability
    global thingone
    global calendercount
    ability[1] += sum(thingone[1])
    social = True
    while social:
        for g in range(0,len(social_name[calendercount-1])):
            if social_name[calendercount-1][g] in chooselist:
                for j in range(0,len(eval('social_story'+str((calendercount-1)//12+1)+'_'+str(thing[1][thingname[1].index(social_name[calendercount-1][g])]))[thingname[1].index(social_name[calendercount-1][g])])):
                    image_set('social/'+str((calendercount-1)//12+1)+'/'+str(thing[1][thingname[1].index(social_name[calendercount-1][g])]),str(thingname[1].index(social_name[calendercount-1][g]))+'-'+str(j),960,720,0,0)
                    talk_image()
                    print_text(screen,30,eval('social_story'+str((calendercount-1)//12+1)+'_'+str(thing[1][thingname[1].index(social_name[calendercount-1][g])]))[thingname[1].index(social_name[calendercount-1][g])][j],40,580,black)
                    creatmap()
                    pygame.time.delay(1000)
        social = False
                
            

#文字
story = [['今年暑假我成為了太空科學與工程學系的大一新生，','九月一號也是我進到中央大學的第一天。','進入大學第一天，該做什麼好呢?'],
         ['大學第一月過得好充實啊，','再來想想第二個月要做什麼吧！'],
         ['哇！！馬上就要期中考了，','該來好好安排這個月要做什麼了。'],
         [' 什麼！時間也過太快了吧！','大一生活馬上要結束了，','好好把握最後一個月吧。'],
         ['馬上就要期末考了！','第一次大學期末考，到底會不會all pass呢？'],
         ['大學第一個寒假欸，','竟然沒有寒假作業，太爽了吧！'],
         ['開學了，好想念大家喔！希望大家沒有忘記我，該來好好刷一波存在感了！'],
         ['風雲際馬上就要開始了！衝刺一波吧~~'],
         ['風雲際開始了，希望以前的努力，能有很好的成果！但課業也不要忘記嘍 ^_^'],
         ['風雲際結束了，好累喔。好不想讀書喔，不過再不讀書就要被當了，嗚嗚嗚嗚嗚嗚。'],
         ['哇，馬上又要放暑假了欸，期末考快結束RRRRR～'],
         ['地科營跑跑跑跑～好緊張喔，希望能有充實的暑假！'],
         ['耶～～大學第一個暑假，要來好好玩嘍。不過還有迎新要準備，希望大一小孩們可以更快容入大學生活！'],
         ['大二開學啦～變學長姐嘍，換我們好好帶領學弟妹融入大學生活了！'],
         ['哇啊啊啊啊啊啊啊！大二上的課好難啊，跟大一完全不一歐樣啊，而且馬上就要考試了。'],
         ['11月了，這學期終於過一半了！不過上課的作業和考試都好多啊，好難兼顧其。他東西啊。'],
         ['終於12月啦！聽說大二聖誕節前沒脫魯，就再也沒機會了。'],
         ['大二上最後一個月了！趕快考完期末考，趕快放假！'],
         ['大二上太累了，休息一下！'],
         ['大二下開始啦！好不就想上課喔，嗚嗚。'],
         ['3月到了欸！是打大地盃和大航盃的一個月！'],
         ['4月就是要放春假啊，但又要期中考了，好難兼顧啊！而且風雲際馬上就要開始了！'],
         ['暑假就快開始了，是不是應該要來規劃一下了。是要出國、實習、打工或是跟老師做研究呢？'],
         ['又是期末考！時間也過太快了吧。'],
         ['暑假開始了啊，來做一點事吧～'],
         ['暑假好無聊啊，不過該來規劃一下大三要來做什麼事吧，跟老師做實驗感覺不錯欸！'],
         ['大三開始了！必修課變好少！終於可以修自己想修的課了。'],
         ['忽然發現大三必修課好少啊，來想想可以做什麼其他的事吧！'],
         ['決定好要做哪些事了，那就來認真做事吧~~~'],
         ['12月了，一年又要過了，最後一個月該來做一些事了吧！'],
         ['大三上快結束了，撐過最後期末考啊！'],
         ['又是一個無所事事的寒假啊...'],
         ['']]

work_achieve = [['補習班抽成','做出口碑','1對1優質教學','教導乃學習','開班授課','補教界超新星'],
                ['第一次端盤子','得心應手','我不是菜鳥','老闆的最愛','老闆的衣缽','我要當老闆'],
                ['初出茅廬','記住名字','燃燒肝指數','專題大賽特優','出國深造','中央30年']]

work_story = [['補習班真討厭，我要努力做出口碑來。','家教也不過如此，也能從教導中了解更深。','多虧這些日子的努力，我才找到1對1的學生。','學生越來越多，要不要畢業去開班授課呢?','昔日討厭補習班的我，現在被找來開班授課，真不一樣。','幽默式教學竟讓我登上YT熱搜，真多人慕名而來'],
              ['客人好多，端菜、洗碗真累人。','洗碗、端菜都有自己的學問在。','經過了一年，店裡也有新成員。','老闆最近看到我，總是笑得詭異。','老闆把祖傳祕方通通跟我說，是在打甚麼主意啊?','反正我書也沒有讀好，也有一技之長，我要當老闆'],
              ['哇!太空電漿模擬艙!!','教授見到我那麼多次，總算不會叫錯名字了','沒想到實驗室要處理的東西很多，聽說有新學弟妹進來實驗室','拿實驗室研究成果去比賽，沒想到得獎了!獎金破萬，真香~~','混了這麼久，不小心就拿到出國交流的補助金','沒想到當上了教授，在中央待了30年阿...']]

social_name = [['期初系大','迎新宿營'],
              ['天空之城','星路壢乘'],
              [' 運動會',' 系出遊','天空之城','星路壢乘'],
              ['聖誕傳情','天空之城','星路壢乘',' 風雲祭',' 地科營'],
              ['星路壢乘',' 風雲祭',' 地科營'],
              ['星路壢乘',' 風雲祭',' 地科營'],
              [' 地科營','迎新宿營',' 風雲祭'],
              ['大氣卡K',' 風雲祭','迎新宿營',' 地科營'],
              [' 風雲祭',' 地科營','迎新宿營'],
              [' 小氣盃','大氣音樂',' 地科營','迎新宿營'],
              [' 地科營','迎新宿營'],
              ['迎新宿營']]

social_story1_1 = [['學長姐都好熱情的介紹各個部門，有學術部、廣器部、活動部...','啊啊...好猶豫要選哪一個...'],
                ['迎新ㄟ，真的是好玩又刺激，刺激是因為...','學姊很兇地對我們說:「再不來啊！」哈哈哈~'],
                ['運動會就是要熱血一波啊！還在等什麼！！！'],
                ['原本以為系出遊會好恐怖...','結果沒想到竟然能跟帥帥學長一起出遊！','還可以跟同學一起玩劈腿遊戲，真有趣！','更重要的是有好多好吃的食物可以吃~真的是來對了'],
                ['在這個寒冷的天，希望我的愛能夠溫暖你心~','愛你呦~~~啾咪 <3'],
                ['大氣系的各位真的是深藏不漏，尤其那個唱曹操的學姐也太...嗯'],
                ['雖然天氣沒有很好但是還是澆不熄大家打球的熱情~','來打系羽小氣盃的人也太多了吧！'],
                ['在繁忙的日子裡，似乎只有音樂能讓我清閒...休息之後繼續朝未來努力吧！'],
                ['相信天空之城的夥伴們都能夠齊心協力','把自己最好的一面展現出來讓小朋友看到我們的熱情！'],
                ['在星路壢乘中能夠與一群喜歡星星的人們一起努力，感覺真好~'],
                ['聽說大氣系下學期有一個大活動叫做...風雲祭','要報名哪一個組別呢？場宣、公關、活策還是學推呢？'],
                ['我誰~~~我瘋子~~~怎麼一個不小心又跑了地科營...']]

social_story1_2 = [['']]+[['回想起之前學長姐們帶給我的美好回憶，也希望我能繼續傳遞下去~']]+[['']]*6+[
                ['好期待可以看到那些可愛的小朋友~~~'],
                ['站在台上講課，好緊張...希望不會講錯。'],
                ['場器宣傳組到底是在幹嘛阿？'],
                ['閃電~~~','閃瞎你的眼哈哈哈~']]

social_story1_3 = [['']]+[['去年迎新的時候好像都會有學長在拍我們，原本以為是怪叔叔，原來是相手~']]+[['']]*6+[
                ['天空之城超棒der~謝謝大家給了我一個難忘的回憶。'],
                ['看到好多星星就好開心~'],
                ['哇~~~公關組看起來也好好玩的樣子'],
                ['奇怪勒...怎麼感覺心癢癢的(抓']]

social_story1_4 = [['']]+[['迎新跑到累了怎麼辦？當然是休息後再出發啊！']]+[['']]*7+[
                ['雖然是冷冷的天，但有星路壢乘陪伴我就不冷了喔~'],
                ['感覺活策組的組長好像GAYGAY的，是我的錯覺嗎?','看起來...真的是呢...'],
                ['我在做什麼?好想睡覺覺。']]

social_story1_5 = [['']]+[['休息完後精神飽滿~又可以繼續在小隊員們充滿活力啦','大家真的都超級棒的~']]+[['']]*7+[
                ['星路壢乘圓滿結束~~~'],
                ['學推組真的是知識的殿堂，每個人都好ㄎ一ㄤ 也好會講喔'],
                ['肝啊...對不起我沒有好好照顧你嗚嗚嗚...']]

social_story1_6 = [['']]+[['又要開始準備下一餐了，下一餐要吃什麼呢？','喔嗚~原來是水餃的部分啊。']]+[['']]*8+[
                ['宵夜街口有好多好玩又好吃的小點心~大家一定要來喔','台上演戲的大家超帥，每個都好會演~'],
                ['好愛地科營呦~希望我當美宣長時也能帶給大家快樂']]

social_story1_7 = [['']]+[['耶依~大氣系的學弟妹們都好乖好可愛哈哈哈','但是迎新即將要結束了...有點小難過嗚嗚嗚']]+[['']]*9+[
                ['不知不覺地科營也快要結束了，但我們明年...']]

social_story1_8 = [['']]*11+[
                ['地科營終於結束拉~~~我的肝真的要好好休養一下']]

#分數統計
thingname = [['普通物理','微積分'],
             ['期初系大','迎新宿營',' 運動會',' 系出遊','聖誕傳情','大氣卡K',' 小氣盃','大氣音樂','天空之城','星路壢乘',' 風雲祭',' 地科營'],
             ['愛情'],
             ['家教','校外餐廳','實驗室'],
             ['耍廢']]
thing = [[0]*len(thingname[0]),[0]*len(thingname[1]),[0]*len(thingname[2]),[0]*len(thingname[3]),[0]*len(thingname[4])]
thingone = [[0]*len(thingname[0]),[0]*len(thingname[1]),[0]*len(thingname[2]),[0]*len(thingname[3]),[0]*len(thingname[4])]
abilityname = [['課業'],['社交'],['愛情'],['打工'],['耍廢']]
ability = [0]*len(abilityname)
fightabilitybonus = [[[0,2,-1],[1,1,1],[2,1,2],[3,1,2],[3,2,3]],
                     [[0,1,0],[0,2,1],[0,3,2],[0,3,2],[0,3,3]],
                     [[1,0,0],[2,1,0],[2,1,2],[0,0,10],[3,2,3]]]

#定義顏色
black = (0,0,0)
white = (255,255,255)

if __name__ == '__main__':
    '''主程式'''
    #初始化
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    #介面設定
    screen = pygame.display.set_mode((960,720))
    pygame.display.set_caption('太空系模擬器')
    #聲音設定
    bgm = pygame.mixer.Sound('./musics/bgm.wav')
    bgm.play(-1)
    #時間設定
    clock = pygame.time.Clock()
    time_delta = clock.tick(60)/1000.0
    #參數設定
    calendercount = 1
    imagename = 1
    bg = 0

    #開始介面
    start = 0
    while start == 0:
        image_set('images',bg,960,720,0,0)
        print_text(screen,90,'太空系模擬器',30,30,white)
        print_text(screen,60,'開始遊戲',45,150,white)
        creatmap()
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if mousedown(45,285,150,210):
                bg += 1
                start = 1
    #行程規劃
    n = 0
    text = 0
    plan = 0
    chooselist=['','','','','']
    while start == 1:
        image_set('images',bg,960,720,0,0)
        #文字段落操控
        if 0 <= text < len(story[calendercount-1]):
            if mousedown(880,910,650,690):
                n += 1
                text += 1
        
        #敘述文字
        if text == n and text < len(story[calendercount-1]):
            talk_image()
            print_text(screen,30,story[calendercount-1][n],40,580,black)
        
        #安排行程
        elif text == len(story[calendercount-1]):
            image_set('txtimage',6,320,140,620,20)
            print_text(screen,100,'執行',685,40,white)
            
            #規劃行程控制
            if plan >= 0:
                image_set('calender',calendercount,180,210,20,0)
                image_set('txtimage',1,160,70,30,200)
                image_set('txtimage',5,160,70,780,200)
                image_set('txtimage',5,160,70,780,300)
                image_set('txtimage',5,160,70,780,400)
                image_set('txtimage',5,160,70,780,500)
                image_set('txtimage',5,160,70,780,600)
                image_set('txtimage',4,160,70,30,600)
                print_text(screen,30,'規劃行程',50,220,black)
                print_text(screen,30,'刪除行程',50,620,black)
                if mousedown(30,190,200,270):
                    image_set('txtimage',7,160,70,30,200)
                    plan = 10
            
            #if mousedown(30,190,600,670):
                #chooselist.pop()
            
            if 10 <= plan < 20:
                image_set('txtimage',2,160,70,210,200)
                image_set('txtimage',2,160,70,210,300)
                image_set('txtimage',2,160,70,210,400)
                image_set('txtimage',2,160,70,210,500)
                image_set('txtimage',2,160,70,210,600)
                if mousedown(210,370,200,270):
                    image_set('txtimage',7,160,70,210,200)
                    plan = 11
                elif mousedown(210,370,300,370):
                    image_set('txtimage',7,160,70,210,300)
                    plan = 12
                elif mousedown(210,370,400,470):
                    image_set('txtimage',7,160,70,210,400)
                    plan = 13
                elif mousedown(210,370,500,570):
                    image_set('txtimage',7,160,70,210,500)
                    plan = 14    
                elif  mousedown(210,370,600,670):
                    image_set('txtimage',7,160,70,210,600)
                    chooselist.insert(0,thingname[4][0])
                    chooselist.pop()
                    plan = 10
                #課業
                elif 11 <= plan < 12:
                    image_set('txtimage',3,160,70,390,200)
                    print_text(screen,30,thingname[0][0],410,220,black)
                    image_set('txtimage',3,160,70,390,300)
                    print_text(screen,30,thingname[0][1],425,320,black)
                    if mousedown(390,550,200,270): 
                        image_set('txtimage',7,160,70,390,200)
                        chooselist.insert(0,thingname[0][0])
                        chooselist.pop()
                    elif mousedown(390,550,300,370):
                        image_set('txtimage',7,160,70,390,300)
                        chooselist.insert(0,thingname[0][1])
                        chooselist.pop()
                #社交
                elif 12 <= plan < 13:
                    for g in range(0,len(social_name[calendercount-1])):
                        if social_name[calendercount-1][g] not in chooselist:
                            image_set('txtimage',3,160,70,390,200+100*g)
                            print_text(screen,30,social_name[calendercount-1][g],410,220+100*g,black)
                            if mousedown(390,550,200+100*g,270+100*g):
                                image_set('txtimage',7,160,70,390,200+100*g)
                                chooselist.insert(0,social_name[calendercount-1][g])
                                chooselist.pop()
                        elif social_name[calendercount-1][g] in chooselist:
                            image_set('txtimage',4,160,70,390,200+100*g)
                            print_text(screen,30,social_name[calendercount-1][g],410,220+100*g,black)
                #愛情
                elif 13 <= plan < 14:
                    image_set('txtimage',4,160,70,390,400)
                    print_text(screen,30,'無',455,420,black)
                #打工
                elif 14 <= plan < 15:
                    image_set('txtimage',3,160,70,390,300)
                    print_text(screen,30,thingname[3][0],440,320,black)
                    image_set('txtimage',3,160,70,390,400)
                    print_text(screen,30,thingname[3][1],410,420,black)
                    image_set('txtimage',3,160,70,390,500)
                    print_text(screen,30,thingname[3][2],425,520,black)
                    if mousedown(390,550,300,370):
                        image_set('txtimage',7,160,70,390,300)
                        chooselist.insert(0,thingname[3][0])
                        chooselist.pop()
                    elif mousedown(390,550,400,470):
                        image_set('txtimage',7,160,70,390,400)
                        chooselist.insert(0,thingname[3][1])
                        chooselist.pop()
                    elif mousedown(390,550,500,570):
                        image_set('txtimage',7,160,70,390,500)
                        chooselist.insert(0,thingname[3][2])
                        chooselist.pop()    
                        
                print_text(screen,30,abilityname[0][0],265,220,black)
                print_text(screen,30,abilityname[1][0],265,320,black)
                print_text(screen,30,abilityname[2][0],265,420,black)
                print_text(screen,30,abilityname[3][0],265,520,black)
                print_text(screen,30,abilityname[4][0],265,620,black)
                j = 0    
                for k in range(0,5):                         
                    print_text(screen,30,chooselist[k],860-len(chooselist[k])*15,220+j*100,black)                    
                    j+=1

            #執行按鈕
            if mousedown(620,940,20,160):
                gain()
                Fight_event()
                social()
                text += 1
                plan = 0
                calendercount += 1
                image_set('images','whi',960,720,0,0)
                image_setgif('images','Loading',300,300,330,210)
                creatmap()
                pygame.time.delay(1000)
                bg = 1
                n = 0
                text = 0
                chooselist=['','','','','']

        creatmap()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        

