package main

import (
	"github.com/rivo/tview"
)

func main() {
	app := tview.NewApplication()
	list := tview.NewList().
		AddItem("Footholds", "Foot in ze door.", 'a', nil).
		AddItem("Files Containing usernames", "Uzers galore!", 'b', nil).
		AddItem("Sensitive Directories", "Tasty Files", 'c', nil).
		AddItem("Web Server Detection", "Webz", 'd', nil).
		AddItem("Vulnerable Files", "Tasty Files", 'e', nil).
		AddItem("Vulnerable Servers", "Serverz", 'f', nil).
		AddItem("Error Messages", "Errors", 'g', nil).
		AddItem("Files Containing Juicy Info", "Juice", 'h', nil).
		AddItem("Files Containing Passwords", "Passwords galore!", 'i', nil).
		AddItem("Sensitive Online Shopping Info", "Consumerz", 'j', nil).
		AddItem("Network or Vulnerability Data", "Vulnz", 'k', nil).
		AddItem("Pages Containing Login Portals", "Portals", 'l', nil).
		AddItem("Various online Devices", "Cameras and Craziness", 'm', nil).
		AddItem("Advisories and Vulnerabilities", "More Vulnz!", 'n', nil).
		AddItem("Quit", "Press to exit", 'q', func() {
			app.Stop()
		})

	if err := app.SetRoot(list, true).SetFocus(list).Run(); err != nil {
		panic(err)
	}
}
