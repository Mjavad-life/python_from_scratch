from random import choice

class RandomWalk :
    # کلاسی برای ساختن راه رفتن
    def __init__(self , num_point = 5000) :
        self.num_point = num_point

        # همه ی راه رفتن ها از نقطه 0 و 0 شروع میشود
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self) :
        #تمام نقاط در راه رفتن را محاسبه میکند
        # به گام برداشتن ادامه میدهد تا راه رفتن به انداره مشخص برشد
         while len(self.x_values) < self.num_point :
            # در محور افقی و عمودی گام برمیدارد
                x_step = self.get_step()
                y_step = self.get_step()   
                
                # اگر به هیچ سمتی نرفت
                if x_step == 0 and y_step == 0 :
                    continue
                
                # مکان جدید را مشخص میکند.
                x = self.x_values[-1] + x_step
                y = self.y_values[-1] + y_step

                self.x_values.append(x)
                self.y_values.append(y)

    def get_step(self):
        # تصمیم میگیرد به کدام جهت و تا چه مسافتی برود
        direction = choice([1 , -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

