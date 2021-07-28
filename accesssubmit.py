import os
import sys
import time
import datetime
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests

from projectinfo import *
from identityinfo import *
from accountinfo import *
import config

class AccessRequest:

  def __init__(self, parent):
    mainframe = ttk.Frame(parent, padding="12 12 12 12")
    mainframe.grid(column=0, row=1, sticky=(N, W, E, S))

    self.projectFrame = ttk.Frame(mainframe, padding="10 10 10 10", style='Cybr.TFrame')
    self.projectFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    self.projectInfo = ProjectInfo(self.projectFrame)

    identityFrame = ttk.Frame(mainframe, padding="10 10 10 10", style='Cybr.TFrame')
    identityFrame.grid(column=0, row=1, sticky=(N, W, E, S))
    self.identityInfo = IdentityInfo(identityFrame)

#    accountFrame = ttk.Frame(mainframe, padding="10 10 10 10", style='Cybr.TFrame')
#    accountFrame.grid(column=0, row=2, sticky=(N, W, E, S))
#    self.accountInfo = AccountInfo(accountFrame)

    ttk.Button(parent, text="Submit", command=self.submit, style='Cybr.TButton').grid(column=3, row=3, sticky=E)

    self.projectInfo.project_entry.focus()

    for child in parent.winfo_children():
        child.grid_configure(padx=10, pady=10)

  ######################################
  def submit(self, *args):
    if self.projectInfo.dataValidated['name'] and self.projectInfo.dataValidated['safe']:
      self.write_to_db()
      sys.exit(0)
    else:
      self.projectFrame.bell()
      messagebox.showinfo("Data Incorrect", "Please enter valid values for Project Name and Safe Name.")
      tk._default_root.grab_set()
      tk._default_root.grab_release()

  ##############################
  # Writes form input variables to MySQL database
  def write_to_db(self, *args):
    approved = 0
    accReqParms= "{" \
                + "\"projectName\":\"" + self.projectInfo.project.get() + "\"," \
                + "\"requestor\":\"" + self.projectInfo.requestor.get() + "\"," \
                + "\"approved\":" + str(approved) + "," \
                + "\"environment\":\""  + self.projectInfo.env.get() + "\"," \
                + "\"pasVaultName\":\"" + config.cybr["pasVaultName"] + "\"," \
                + "\"pasSafeName\":\"" + self.projectInfo.safe.get() + "\"," \
                + "\"pasCpmName\":\"" + config.cybr["pasCpmName"] + "\"," \
                + "\"pasLobName\":\"" + config.cybr["pasLobName"] + "\"," \
                + "\"appIdName\":\"" + self.identityInfo.identity.get() + "\"," \
                + "\"appAuthnMethod\":\"authn-k8s\"" \
                + "}"
    r = requests.post(url = config.cybr["apiEndpoint"]+"/appgovdb", data = accReqParms)
    messagebox.showinfo("Access Request Submitted",
			"Access request SUBMITTED\n\nIdentity: "
			+ self.projectInfo.project.get() + "/" + self.identityInfo.identity.get()
			+ "\n\nSafe: " + self.projectInfo.safe.get())
