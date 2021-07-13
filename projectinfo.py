from tkinter import *
from tkinter import ttk
import requests
from requests.auth import HTTPBasicAuth

class ProjectInfo:

  def __init__(self, parent):
    projectFrame = ttk.LabelFrame(parent, text='Project Info',padding="3 3 12 12")
    projectFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    projectFrame.columnconfigure(0, weight=1)
    projectFrame.rowconfigure(0, weight=1)

    ttk.Label(projectFrame, text="Project Name").grid(column=0, row=1, sticky=W)
    self.project = StringVar()
    self.project_entry = ttk.Entry(projectFrame, width=15, textvariable=self.project)
    self.project_entry.grid(column=2, row=1, sticky=(W, E))

    ttk.Label(projectFrame, text="Safe Name").grid(column=0, row=2, sticky=W)
    self.safe = StringVar()
    self.safe_entry = ttk.Entry(projectFrame, width=15, textvariable=self.safe)
    self.safe_entry.grid(column=2, row=2, sticky=(W, E))

    ttk.Label(projectFrame, text="Requestor").grid(column=0, row=3, sticky=W)
    self.requestor = StringVar()
    requestor_entry = ttk.Entry(projectFrame, width=15, textvariable=self.requestor)
    requestor_entry.grid(column=2, row=3, sticky=(W, E))

    ttk.Label(projectFrame, text="Environment").grid(column=0, row=4, sticky=W)
    self.env = StringVar()
    envDev = ttk.Radiobutton(projectFrame, text="Dev", variable=self.env, value="dev")
    envTest = ttk.Radiobutton(projectFrame, text="Test", variable=self.env, value="test")
    envProd = ttk.Radiobutton(projectFrame, text="Prod", variable=self.env, value="prod")
    envDev.grid(column=2, row=5, sticky=(W, E))
    envTest.grid(column=2, row=6, sticky=(W, E))
    envProd.grid(column=2, row=7, sticky=(W, E))
