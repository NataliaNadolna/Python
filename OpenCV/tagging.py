import cv2
import glob
import os

class Coordinates():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        size = 416
        self.x1 = int(x*size - w*size/2)
        self.y1 = int(y*size - h*size/2)
        self.x2 = int(x*size + w*size/2)
        self.y2 = int(y*size + h*size/2)

    def __str__(self):
        return f"({self.x1}, {self.y1}), ({self.x2}, {self.y2})"

class CoordinatesList(list):
    def __init__(self):
        super().__init__()

    def load(self):
        coordinates_path = glob.glob('Python/OpenCV/coordinates/*.txt')
        print(coordinates_path)
        for f in coordinates_path:
            file = open(f, "r")
            for line in file.readlines():
                new_line = line.strip()
                new_line = new_line.split(" ")
                cords = Coordinates(float(new_line[1]), float(new_line[2]), float(new_line[3]), float(new_line[4]))
                self.append(cords)
            file.close()

    def print_list(self):
        for i in range(len(self)):
            print(f"{self[i]}")

class ImagesList(list):
    def __init__(self):
        super().__init__()

    def load(self):
        images_path = glob.glob('Python/OpenCV/pictures/*.jpg')
        for file in images_path:
            img = cv2.imread(file)
            images.append(img)

    def copy_names(self):
        images_path = glob.glob('Python/OpenCV/pictures/*.jpg')
        names = []
        for file in images_path:
            names.append(os.path.basename(file))
        return names

    def tag(self):
        for i, img in enumerate(self):
            img = cv2.rectangle(img, (coordinates[i].x1, coordinates[i].y1), 
                                     (coordinates[i].x2, coordinates[i].y2), (128, 128, 128), 5)
            cv2.imshow('frame', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def save(self):
        names = self.copy_names()
        for i, img in enumerate(self):
            img = cv2.rectangle(img, (coordinates[i].x1, coordinates[i].y1), 
                                     (coordinates[i].x2, coordinates[i].y2), (128, 128, 128), 5)
            file_name = f"Python/OpenCV/tagged/{names[i]}"
            cv2.imwrite(file_name, img)

images = ImagesList()
coordinates = CoordinatesList()

coordinates.load()
coordinates.print_list()
images.load()
images.tag()
images.save()







