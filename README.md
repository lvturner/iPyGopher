# iPyGopher
A basic Gopher client for iOS written entirely on an iPad using the following collection of tools:

 - *Pythonista 3* - Fantastic python based automation suite for iOS.
- *Dash* - Offline documentation sets
- *Working Copy* - Probably the best git client I've ever used, ever.

## Small story (you can skip over this)
I like gopher. I was on a plane to a holiday destination with limited WiFi, it dawned on me this would be a great use-case for gopher - unfortunately I did not have the IETF RFCs downloaded for Dash at this point, so I can't claim it was written on the plane.

It was however written whilst on holiday, mostly on New Year's Eve, happily sitting in a sunny resort drinking some cocktails, which I will blame for any of the particularly nasty parts in the code.

A lot of time was spent squinting myself with Python and Pythonista's iOS specific stuff - it seems in order to get things rendering in a WebView I had to work around a few limitations and quirks, the net result, realistically, is that while all this works, it is essentially one large hack.

## Requirements
Pythonista 3 is the only real requirement - I would also recommend the use of the App 'Working Copy', as you can use this to clone this repository directly in to your iOS device and then open it in Pythonista. Using this method will also alert you of any updates I ever make to it.

## Features and limitations
Most basic things work - binary file (image) downloads are not supported.

There is basic history function provided (i.e. a back-button) it's far from perfect, but it just about gets the job done.

There's support for search entries, but do be aware that the UI may appear to do nothing while as it currently does not stream the results direct into the web view.

There's an address bar too - however you currently have to press the 'go' button as I haven't hooked anything up to listen for pressing enter in the address bar.

It supports, to some degree, external (off-Gopher) links, in some instances (i.e. links to IRC) this will require you to have an app installed that registers an appropriate URL handler - for HTTP, it'll use Safari

It currently does not support some of the 'newer' Gopher formatting features (i.e. `!title`) and I'm sure there are plenty of formatting bugs and issues lurking.

There is also currently no support for any kind of customisation, colour schemes, or changing from the default font.

It also currently won't automatically fill in a default port for you, so you have to be a bit careful when entering addresses.

## Sign-off
For all four people that are likely to ever use this, I hope you enjoy it, please feel free to submit feature requests or code improvements - I only ask that you are gentle and kind with your criticisms :)

I also have my own little Gopherspace on SDF.org which can be found here: [gopher://sdf.org:70/users/lvturner/](gopher://sdf.org:70/users/lvturner/)