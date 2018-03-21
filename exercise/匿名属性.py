class Screen:
    #@property 下的属性必须是匿名属性
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,value):
        self.__width=value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,value):
        self.__height=value

    @property
    def resolution(self):
        return self.__width*self.__height
