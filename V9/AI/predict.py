# Need Bandicam to take a screenshot when Minecraft in full screen mode
import cv2
import numpy as np
from tensorflow.keras.models import load_model

class predict():
    Z = [(4, 4), (4, 76), (4, 148), (4, 220), (4, 292),
         (4, 364), (4, 436), (4, 508), (4, 580), (76, 4),
         (76, 76), (76, 148), (76, 220), (76, 292), (76, 364),
         (76, 436), (76, 508), (76, 580), (148, 4), (148, 76),
         (148, 148), (148, 220), (148, 292), (148, 364), (148, 436),
         (148, 508), (148, 580), (236, 4), (236, 76), (236, 148),
         (236, 220), (236, 292), (236, 364), (236, 436), (236, 508),
         (236, 580)]

    class_names = ['0', '1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26',
                   '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '4', '40', '5', '51', '6', '7', '8', '9']

    def __init__(self):
        self.model = load_model("AI/item_reader_seq.model")

    # 2.8 ms ± 135 µs
    def __call__(self, img):
        
        # img = cv2.imread("D:/Bi/Record/javaw 2021-11-06 15-39-52-677.jpg")
        # 367 ns ± 12.3 ns
        img = img[540:845, 636:1285]
        # img = img[480:845, 600:1285]
        # 25.4 µs ± 5.16 µs 
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        Slot = []
        for x, y in self.Z:
            Slot.append(img[x:x+64, y:y+32])
            # Slot.append(img)
    
        for n in range(36):
            # 10.2 µs ± 2.87 µs
            Slot[n] = cv2.resize(Slot[n], (32//4, 64//4),
                                interpolation=cv2.INTER_AREA)

        # model([Slot,])
        
        # 45.1 ms ± 1.91 ms
        # x = self.model.predict(np.array(Slot))
        
        x = self.model(np.array(Slot), training=False)
        
        x = np.argmax(x, axis=1)
        x = np.array([self.class_names[xi] for xi in x])
        x = np.reshape(x, (4, 9))
        return x

model = predict()