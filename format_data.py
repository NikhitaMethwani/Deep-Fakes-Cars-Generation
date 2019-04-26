# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:25:34 2019

@author: Nikhita Methwani
"""

car_dir = r"D:\MachineLearning-NickBrown\DeepFakes\DeepFakes_Dataset\Car_train"
save_dir = r"D:\MachineLearning-NickBrown\DeepFakes\DeepFakes_Dataset\Car_train_resize"

car_im_list = os.listdir(car_dir)
list_size = np.shape(car_im_list)

for j in range(0,list_size[0]):
    car_im = cv2.cvtColor(cv2.imread(os.path.join(car_dir, car_im_list[j])), cv2.COLOR_BGR2RGB)
    resized_car_im = cv2.resize(car_im, (128, 128))
    save_path = os.path.join(save_dir, car_im_list[j])
    cv2.imwrite(save_path,cv2.cvtColor(resized_car_im, cv2.COLOR_BGR2RGB))