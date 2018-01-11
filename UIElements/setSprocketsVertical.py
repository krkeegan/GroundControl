from kivy.uix.widget                      import   Widget
from kivy.properties                      import   ObjectProperty

class SetSprocketsVertical(Widget):
    '''

    Provides a standard interface for making both sprockets point vertically

    '''
    data = ObjectProperty(None) #set externally

    def LeftCW(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/360.0;
        self.data.gcode_queue.put("$MSLW6=" + str(degValue) + " ")

    def LeftCCW(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/360.0;
        self.data.gcode_queue.put("$MSLW6=" + str(degValue) + " ")

    def RightCW(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/360.0;
        self.data.gcode_queue.put("$MSLW7=" + str(degValue) + " ")

    def RightCCW(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/360.0;
        self.data.gcode_queue.put("$MSLW7=" + str(degValue) + " ")

    def LeftCW5(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/72.0;
        self.data.gcode_queue.put("$MSLW6=" + str(degValue) + " ")

    def LeftCCW5(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/72.0;
        self.data.gcode_queue.put("$MSLW6=" + str(degValue) + " ")

    def RightCW5(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/72.0;
        self.data.gcode_queue.put("$MSLW7=" + str(degValue) + " ")

    def RightCCW5(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/72.0;
        self.data.gcode_queue.put("$MSLW7=" + str(degValue) + " ")

    def LeftCWpoint1(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/3600.0;
        self.data.gcode_queue.put("$MSLW6=" + str(degValue) + " ")

    def LeftCCWpoint1(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/3600.0;
        self.data.gcode_queue.put("$MSLW6=" + str(degValue) + " ")

    def RightCWpoint1(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/3600.0;
        self.data.gcode_queue.put("$MSLW7=" + str(degValue) + " ")

    def RightCCWpoint1(self):
        degValue = float(self.data.config.get('Advanced Settings',"gearTeeth"))*float(self.data.config.get('Advanced Settings',"chainPitch"))/3600.0;
        self.data.gcode_queue.put("$MSLW7=" + str(degValue) + " ")

    def setZero(self):
        #mark that the sprockets are straight up
        self.data.gcode_queue.put("$MSLW4=0");
        self.data.gcode_queue.put("$MSLW5=0");
        self.carousel.load_next()
