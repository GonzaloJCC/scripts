import cv2
import numpy as np
import os

img = cv2.imread('./reverse_card.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output_folder = 'cartas_output'
os.makedirs(output_folder, exist_ok=True)

desired_size = (160, 230)
count = 0
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w > 50 and h > 50:
        card = img[y:y+h, x:x+w]
        card_gray = cv2.cvtColor(card, cv2.COLOR_BGR2GRAY)
        _, alpha = cv2.threshold(card_gray, 254, 255, cv2.THRESH_BINARY_INV)
        b, g, r = cv2.split(card)
        rgba = [b, g, r, alpha]
        card_trans = cv2.merge(rgba)
        card_trans = cv2.resize(card_trans, desired_size, interpolation=cv2.INTER_AREA)
        cv2.imwrite(f'{output_folder}/card_{count}.png', card_trans)
        count += 1

print(f'Se guardaron {count} cartas')
