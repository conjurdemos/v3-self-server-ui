import os
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests
import json

import config

class OnboardProject:

  def __init__(self, parent):
    mainframe = ttk.Frame(parent, padding="12 12 12 12")
    mainframe.grid(column=0, row=1, sticky=(N, W, E, S))

    baseFrame = ttk.Frame(mainframe, padding="10 10 10 10", style='Cybr.TFrame')
    baseFrame.grid(column=0, row=0, sticky=(N, W, E, S))

    self.projectFrame = ttk.LabelFrame(baseFrame, text='Project Info',padding="3 3 12 12")
    self.projectFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    self.projectFrame.columnconfigure(0, weight=1)
    self.projectFrame.rowconfigure(0, weight=1)
    self.projectFrame.dataValidated={'name':False,'admin':False}	# all must be True to save project info

    #############################################################
    # Project name entry
    ttk.Label(self.projectFrame, text="Project Name").grid(column=0, row=1, sticky=W)
    self.project = StringVar()
    self.project_entry = ttk.Entry(self.projectFrame, width=15, textvariable=self.project)
    self.project_entry.grid(column=2, row=1, sticky=(W, E))

    def projectExists(projectName):	# callback to validate non-blank unique project name 
      if projectName == "":
        messagebox.showinfo("Project Name Required", "Project name cannot be empty.")
        tk._default_root.grab_set()
        tk._default_root.grab_release()
        self.projectFrame.dataValidated['name']= False
        return True
      projectJson = json.loads(requests.get(config.cybr["apiEndpoint"]+"/project?projectName="+projectName).content)
      projectList = projectJson["projects"]	# get list of projects - will be empty or one
      if projectList:
        messagebox.showinfo("Project Exists", "There is an existing project named " + projectName + "\n\nName must be unique.")
        tk._default_root.grab_set()
        tk._default_root.grab_release()
        self.projectFrame.dataValidated['name']= False
        return True
      else:
        self.projectFrame.dataValidated['name']= True
        return True

    valPr = self.project_entry.register(projectExists)
    self.project_entry.config(validate='focusout', validatecommand=(valPr,'%P'))

    #############################################################
    # Admin user entry
    ttk.Label(self.projectFrame, text="Admin Name").grid(column=0, row=2, sticky=W)
    self.admin = StringVar()
    self.admin_entry = ttk.Entry(self.projectFrame, width=15, textvariable=self.admin)
    self.admin_entry.grid(column=2, row=2, sticky=(W, E))

    def adminIsEpvUser(adminName):	# callback for project admin user validation in PAS
      if adminName == "":
        messagebox.showinfo("Admin Name Required", "Project admin name cannot be empty.")
        tk._default_root.grab_set()
        tk._default_root.grab_release()
        self.projectFrame.dataValidated['admin']= False
        return True
      userJson = json.loads(requests.get(config.cybr["apiEndpoint"]+"/user?userName="+adminName).content)
      userList = userJson['users']
      if userList:
        self.projectFrame.dataValidated['admin']= True
        return True
      else:
        messagebox.showinfo("Invalid User", "There is no CyberArk vault user named " + adminName)
        tk._default_root.grab_set()
        tk._default_root.grab_release()
        self.projectFrame.dataValidated['admin']= False
        return True

    valAdmin = self.admin_entry.register(adminIsEpvUser)   # register admin validation callback
    self.admin_entry.config(validate='focusout', validatecommand=(valAdmin,'%P'))

    #############################################################
    # Billing code entry
    ttk.Label(self.projectFrame, text="Billing Code").grid(column=0, row=3, sticky=W)
    self.billing = StringVar()
    billing_entry = ttk.Entry(self.projectFrame, width=15, textvariable=self.billing)
    billing_entry.grid(column=2, row=3, sticky=(W, E))

    ttk.Button(parent, text="Save", command=self.save, style='Cybr.TButton').grid(column=3, row=3, sticky=E)

    self.project_entry.focus()

    for child in parent.winfo_children():
        child.grid_configure(padx=10, pady=10)

  ######################################
  def save(self, *args):
    if self.projectFrame.dataValidated['name'] and self.projectFrame.dataValidated['admin']:
      self.write_to_db()
      sys.exit(0)
    else:
      self.projectFrame.bell()
      messagebox.showinfo("Data Incorrect", "Please enter valid values for Project Name and Admin Name.")
      tk._default_root.grab_set()
      tk._default_root.grab_release()

  ##############################
  # Writes form input variables to MySQL database
  def write_to_db(self, *args):
    projectParms= "{" \
                + "\"projectName\": \"" + self.project.get() + "\"," \
                + "\"adminName\": \"" + self.admin.get() + "\"," \
                + "\"billingCode\": \"" + self.billing.get() + "\"" \
                + "}"

    r = requests.post(url = config.cybr["apiEndpoint"]+"/project", data = projectParms)
    messagebox.showinfo("Project Onboarded",
			"Project information SAVED\n\nProject: "
			+ self.project.get()
			+ "\nAdmin: " + self.admin.get()
			+ "\nBilling Code: " + self.billing.get())
