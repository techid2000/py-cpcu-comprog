# Lab_BNK48 (SCORE 2%)
# TO DO 0 : นำเข้า library pygame


# TO DO 1 : กำหนด width : 1000 , height : 600 และ FPS : 60
width =
height =
FPS =

# TO DO 2 : กำหนดค่าสีดังนี้ pink : (197,142,195) , white : (255,255,255)
pink =
white =

# TO DO 3 : กำหนดความเร็วให้กับ member แต่ละคน [ 3 member ]
cherprang_speed = [2,2]
    # [-3,4]
    # [3,-2]

# TO DO 4 : initialize pygame variable and create clock
pygame.
clock =

# TO DO 5 : create screen [pygame.display.set_mode] and set caption [pygame.display.set_caption] ->("BNK48_BALL")
screen =


# Choose 3 members from BNK48 and create pygame object from  get_rect
# [ load , resize , get_rect ]

# Member 1 [size : (150 , 150) , center : (500 , 250) ]
cherprang_img = pygame.image.load("source/BNK48/cherprang.png").convert_alpha()
cherprang_img = pygame.transform.scale(cherprang_img, (150, 150))
cherprang_rect = cherprang_img.get_rect(center=(500,250))

# TO DO 6 : create object with attribute in each comment
# Member 2 [size : (100 , 100) , center : (250 , 120)]





# Member 3 [size : (120 , 120) , center : (800 , 400)]





running=True

while running:
    # TO DO 7 : set ให้ตัวเกมส์แสดงผลด้วยความเร็วที่เหมาะสม [clock.tick(...)]


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    # TO DO 8 :ใส่สี background สีชมพู (screen.fill(...))


    # TO DO 9 : ให้ member ทั้ง 3 คนเคลื่อนที่ตามทิศทางและความเร็วเป็นไปตาม speed ของแต่ละคน
    cherprang_rect = cherprang_rect.move(cherprang_speed)




    # TO DO 10 : วาด text คำว่า "BNK48" [size : 250 , center :(width/2 , height/4), สีขาว]






    # TO DO 11 : เขียนเงื่อนไขไม่ให้ตกกรอบทุกด้านให้กับ member ทั้ง 3 คน
    if cherprang_rect.left < 0 or cherprang_rect.right > width:
        cherprang_speed[0] = -cherprang_speed[0]







    # TO DO 12 : เอาภาพของ member แต่ละคนใส่ลงใน object ของตนเอง
    screen.blit(cherprang_img, cherprang_rect)



    pygame.display.flip()


pygame.quit()


#Extra Score (1%) : จงทำให้บอลเด้งกลับในทิศทางตรงกันข้ามเมื่อบอลแต่ละลูกกระทบกัน