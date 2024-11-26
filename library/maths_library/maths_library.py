class my_maths():
    '''
    This maths library will evaluate and calculate the area and
    volume of a given variable(s)
    '''
    @staticmethod
    
    # ===========================================

    def area_square(size:float) -> float:
        '''
        Calculate the area of a square

        Parameters
        ----------
        size: float
            The size of the square
        
        Returns
        -------
        float:
            The area of the square    

        '''
        try:
            size = float(size)
            area = size * size
        except:
            print("area_square\nAn exception has occured, this may be because of an invalid data type")
            return 0
        return area
    
    # ===========================================

    def area_rectangle(width:float, height:float) -> float:
        '''
        Calculate the area of a rectangle

        Parameters
        ----------
        width: float
            The width of the rectangle
        height: float
            The height of the rectangle
        
        Returns
        -------
        float:
            The area of the rectangle    

        '''
        try:
            width = float(width)
            height = float(height)
        except:
            print("area_rectangle\nAn exception has occured, this may be because of an invalid data type")
            return 0
        return width * height
    
    # ===========================================

    def area_triangle(width:float, height:float) -> float:
        '''
        Calculate the area of a triangle

        Parameters
        ----------
        width: Float
            The width of the triangle
        height: Float
            The height of the triangle

        Returns
        -------
        float:
            Area of the triangle
        '''
        try:
            width = float(width)
            height = float(height)
            area = (width * height) / 2
        except:
            print("area_triangle\nAn exception has occured, this may be because of an invalid data type")
            return 0
        return area
    
    # ===========================================

    def area_circle(radius:float) -> float:
        '''
        Calculate the area of a circle

        Parameters
        ----------
        radius: float
            The size of the circle
        
        Returns
        -------
        float:
            The area of the circle    

        '''
        try:
            radius = float(radius)
            area = 3.14159 * (radius) * radius
        except:
            print("area_circle\nAn exception has occured, this may be because of an invalid data type")
            return 0
        return area
        
    # ===========================================
    
    def area_cuboid(x:float, y:float, z:float) -> float:
        '''
        Calculate the area of a cuboid

        Parameters
        ----------
        x: float
            X length of the cuboid
        y: float
            Y length of the cuboid
        z: float
            Z length of the cuboid
        
        Returns
        -------
        Float:
            Area of the cuboid
        '''
        try:
            x = float(x)
            y = float(y)
            z = float(z)
            volume = x * y * z
        except:
            print("area_cuboid\nAn exception has occured, this may be because of an invalid data type")
            return 0
        return volume
    
    # ===========================================
    
    def surface_area_cuboid(x:float, y:float, z:float) -> float:
        '''
        Calculate the surface area of a cube

        Parameters
        ----------
        x: float
            X length of the cuboid
        y: float
            Y length of the cuboid
        z: float
            Z length of the cuboid
        
        Returns
        -------
        Float:
            Surface area of the cube
        '''
        try:
            x = float(x)
            y = float(y)
            z = float(z)
            surface_area = 2 * (x*y + x*z + y*z)
        except:
            print("surface_area_cuboid\nAn exception has occured, this may be because of an invalid data type")
            return 0
        return surface_area

    # ===========================================

    def sphere_volume(radius:float) -> float:
        '''
        Calculate the volume of a sphere

        Parameters
        ----------
        radius: Float
            The radius of the sphere
        
        Returns
        -------
        Float:
            Volume of sphere
        '''
        try:
            radius = float(radius)
            volume = (4/3) * (3.14159) * radius * radius * radius
        except:
            print("surface_area_cuboid\nAn exception has occured, this may be because of an invalid data type")
            return 0
        return volume