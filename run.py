# -*- coding: utf-8 -*-
"""
    run
    ~~~~~~~~~~~~

    Implements admin privilege escalation.

    :copyright: (c) 2017 by Arun John Kuruvilla.
"""
import ctypes
import sys
import os

import src.monitor as monitor
import src.admin as admin
import src.configg as configg
import src.report as report

def main():
    """Get the global configuration object
    """

    config_object = configg.configuration

    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            # If current user has administrator privileges
            # Initialize and start monitor object
            print("[+] Current priviledge level is Administrator.")
            print("[+] Initializing and starting monitor.")
            try:
                monitor_object = monitor.Monitor()
                monitor_status = monitor_object.initialize()
                if monitor_status:
                    report_object = report.Report()
                    report_object.generate_report()

            except Exception as e:
                print(e.message)
        else:
            print("[+] Current priviledge level is not Administrator.")
            print("[+] Initializing and starting privilege escalation.")

            # If current user does not have administrator privileges
            current_script = config_object['package_path'] + '\\' + __file__

            # Initialize admin object
            admin_object = admin.Admin()
            admin_object.bootstrap(current_script)
            sys.exit(0)
    except Exception as e:
        print(e.message)
        print("[-] A fatal system error has occurred. Exiting.")

if __name__ == '__main__':
    main()