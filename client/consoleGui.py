
import npyscreen
class hurbim(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = npyscreen.Form(name = "hurbIM",)
        grid = F.add(npyscreen.SimpleGrid,columns = 2, column_width = 3,col_margin=1,row_height = 1)


        # This lets the user interact with the Form.
        F.edit()

        print(ms.get_selected_objects())
