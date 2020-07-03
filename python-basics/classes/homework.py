class Line:
    def __init__(self,coor1,coor2):
       
        self.coor1 = coor1
        self.coor2 = coor2


    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2 - x1)**2 +(y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())


class Cylinder:
    def __init__(self,height=1,radius=1):
            self.height = height
            self.radius = radius

    def volume(self):
             return (self.radius**2)* 3.14 * self.height
    
    def surface_area(self):
        return 2*3.14*self.radius*self.height + 2*3.14*self.radius**2


c = Cylinder(2,3)
print(c.surface_area())


class Pets:
    def __init__(self, name, species, vacinated):
        self.name = name
        self.species = species
        self.vacinated = vacinated

    def intro(self):
        print(f'{self.name}')

    def species_type(self):
        print(f'{self.species}')

    def vac(self):
        print(f'{self.vacinated}')

pet1 = Pets('Korra', 'Species', True)
print(pet1.vacinated)



