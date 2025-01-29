import os
import sys
import time
import servicemanager
import win32event
import win32service
import win32serviceutil
import subprocess

class USBMonitorService(win32serviceutil.ServiceFramework):
    _svc_name_ = "windowsUsbDeviceSecurity"
    _svc_display_name_ = "Window Security device"
    _svc_description_ = "Check for window security"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.running = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        import finalsolution  
        finalsolution.run()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(USBMonitorService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(USBMonitorService)
    
    # Configure the service to restart on failure
    subprocess.run(['sc', 'failure', 'windowsUsbDeviceSecurity', 'reset=0', 'actions=restart/60000'])

    # Configure the service to start automatically after a reboot
    subprocess.run(['sc', 'config', 'windowsUsbDeviceSecurity', 'start=', 'auto'])
