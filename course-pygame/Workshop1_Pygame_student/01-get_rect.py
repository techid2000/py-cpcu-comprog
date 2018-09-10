import pygame  # import library

pygame.init()  # initialize pygame modules

# initialize screen resolution and variable
width= 320
height = 240
FPS = 36

speed = [2, 2]
black = 0, 0, 0

# นำเอาค่าในตัวแปร size ใช้ในการสร้าง screen resolution
screen = pygame.display.set_mode((width,height))

# โหลดภาพจากภายนอกเข้ามาใช้
ball = pygame.image.load("source/intro_ball.gif")
clock = pygame.time.Clock()

# แปลง surface ให้เป็น object
ballrect = ball.get_rect()

running = True

# เข้า while loop เพื่อเริ่มวงวนการทำงาน
while running:

    # set ให้ตัวเกมส์แสดงผลด้วยความเร็วที่เหมาะสม
    clock.tick(FPS)

    # วน loop การรับ event จาก mouse หรือ keyboard
    for event in pygame.event.get():
        # ตรวจสอบว่า ถ้า event นั้นเป็นการคลิกปุ่มปิด x ให้ทำการปิดโปรแกรม
        if event.type == pygame.QUIT:
            running=False

    # เนื่องจากเราแปลง ballrect กลายเป็น object แล้วเราสามารถให้มันขยับได้ด้วย คำสั่ง .move(...)
    ballrect = ballrect.move(speed)

    # สร้าง condition ว่า ถ้า ball ทะลุกรอบซ้ายของจอ หรือ ทะลุกรอบขวาของจอให้กลับ
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    ###########################################################################
    # TO DO 1 : จงทำให้บอลชิ่งไปมาในกรอบสี่เหลี่ยม (ไม่ตกกรอบ บน-ล่าง) [ top , bottom ]
    # Hint [ทำคล้ายๆกับข้างบน speed[0] หมายถึงแกน x และ speed[1] หมายถึงแกน y]


    ###########################################################################

    # ล้างทุกอย่างในจอโดยการให้จอเป็นสีดำ (ลอง comment code ดูสิจะเกิดอะไรขึ้น)
    screen.fill(black)

    #เอาภาพ ball ใส่ใน object ballrect (ลอง comment code ดูสิว่าเกิดอะไรขึ้น)
    screen.blit(ball, ballrect)

    # อัพเดท content ลงใน screen -> ในที่นี้คือการ นำเอา screen และ ballrect ใส่ลงใน window
    # (ลอง comment code ดูสิว่าเกิดอะไรขึ้น)
    pygame.display.flip()

pygame.quit()