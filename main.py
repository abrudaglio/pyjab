import jab
import wx
# import pump


def test(e):
    jc = jab.JABContext(197362)
    print(dir(jc))
    print("vmId", jc.vmID)
    aci = jc.getAccessibleContextInfo()
    print("getAccessibleContextInfo", aci, dir(aci))
    print("getAccessibleContextInfo", aci.name, aci.role)
    # for field in ['name', 'description', 'role', 'role_en_US', 'states', 'states_en_US', 'indexInParent', 'childrenCount',
    #               'x', 'y', 'width', 'height', 'accessibleComponent', 'accessibleAction', 'accessibleSelection', 'accessibleText', 'accessibleValue']:
    #     print(field, aci.__getattr__(field))
    print(jc)


# Create a new app, don't redirect stdout/stderr to a window.
app = wx.App(False)
# A Frame is a top-level window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
pnl = wx.Panel(frame)
sizer = wx.BoxSizer(wx.VERTICAL)
btn = wx.Button(frame, id=wx.ID_ANY, label="click")
pnl.SetSizer(sizer)
sizer.Add(btn)

frame.Bind(wx.EVT_BUTTON, test, btn)
frame.Show(True)     # Show the frame.


# pump.createPump()
# pump.requestPump()
jab.initialize()

app.MainLoop()
