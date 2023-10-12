class Functions:
    def create_corners(self, cell_width:int=4, cell_number:int=3):
        connector = "#"
        middle = "-"
        line_corners = ""

        for i in range(cell_number):
            line_corners += connector
            line_corners += middle*cell_width
        line_corners += connector
        line_corners += "\n"
        return line_corners




    def create_central(self, cell_width:int=4, cell_number:int=3):
        connector = "|"
        middle = " "
        line_central = ""

        for i in range(cell_number):
            line_central += connector
            line_central += middle * cell_width
        line_central += connector

        line_central += "\n"
        return line_central


    def create_grid(self, width, height):
        head = self.create_corners(width)
        middle = self.create_central(width)
        picture = ""

        picture += head
        picture += middle * height
        picture += head
        picture += middle * height
        picture += head

        return picture




if __name__ == '__main__':
    function = Functions()
    print(function.create_grid(8, 10))