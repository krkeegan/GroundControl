'''

Generates a grid which can be measured to calibrate the machine's dimensions

'''
from   kivy.uix.gridlayout                       import   GridLayout
from   kivy.properties                           import   ObjectProperty
from   kivy.properties                           import   StringProperty
from   UIElements.touchNumberInput               import   TouchNumberInput
from   kivy.uix.popup                            import   Popup

class CalibrationGrid(GridLayout):
    
    def runCalibrationPatternCut(self):
        '''
        
        Create a pattern of marks on the sheet which can be measured
        
        '''
        
        #coordinates of points to cut
        listOfPoints = [(-1080, 460),  (-540, 460), (0,  460), ( 540,  460), ( 1080,  460), 
                        ( 1080,   0),  ( 540,   0), (0,    0), (-540,    0), (-1080,    0),
                        (-1080, -460), (-540,-460), (0, -460), ( 540, -460), ( 1080, -460)]
        
        print "run calibration"
        self.data.units = "MM"
        self.data.gcode_queue.put("G21 ")
        self.data.gcode_queue.put("G90 ")
        self.data.gcode_queue.put("G40 ")
        
        #Move to the center 
        self.data.gcode_queue.put("G0 Z5 ")
        self.data.gcode_queue.put("G0 X0 Y0 ")
        self.data.gcode_queue.put("G17 ")
        
        for point in listOfPoints:
            self.markPoint(point)
        
        self.data.gcode_queue.put("G0 Z5 ")
        self.data.gcode_queue.put("G0 X0 Y0 ")
    
    def markPoint(self, point):
        '''
        
        Mark the passed coordinates on the wood
        
        '''
        print "mark point"
        print point[0]
        print point[1]
        
        self.data.gcode_queue.put("G0 Z5 ")
        moveString = "G0 X" + str(point[0]) + " Y" + str(point[1])
        self.data.gcode_queue.put(moveString)
        self.data.gcode_queue.put(moveString)
        self.data.gcode_queue.put("G0 Z-6 ")
        self.data.gcode_queue.put("G0 Z5 ")
    
    def stop(self):
        '''
        
        Stop the machine
        
        '''
        self.data.quick_queue.put("!") 
        with self.data.gcode_queue.mutex:
            self.data.gcode_queue.queue.clear()
    