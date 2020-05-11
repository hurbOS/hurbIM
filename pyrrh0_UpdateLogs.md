+ TO-DO:
    + GUI
        + [X] Complete Login Screen
        + [X] Complete Create Account
        + [ ] Complete Chat Screen
        + [ ] Complete Settings Screen 

    + Backend
        + [ ] Understand wtf is going on
        + [ ] Start implementing mySQL on a new branch. SQLite3 seems less secure (not verified)
        + [ ] Setup an account system in the database
        + [ ] Setup authentication system of people's information, email perhaps?
        + [ ] Research on chat app structures, how they work, how to implement them, etc.
        + [ ] Research security risks off the app... SQL injection, Buffer Overflow, Web attacks etc.

[Mon May 11, 17:46]

Notes: Started working on the "Create Account" screen, a few touches and it should be done. However, my main concern is the app's ability to scale correctly when resized/maximized. I've been thinking of also implementing some sort of user customzation settings, perhaps custom wallpapers for the chat screen, layout and color cutomizations and light mode for the poggers. I also need to do some research about this but I'm struggling to find time (*sigh*school). Anyways all major changes are below.

* Changes:
    * Created sepearte folders for source files - "fonts" and "images"
    * Added in new "Create Account" image and all Roboto fonts - do I need the lisence there?
    * Completed "Create Account" screen

[Tue May 5, 17:43]
- Minimal (TUI)
    - Working on login screen
    - Minor changes to client

**Note to fellow contributers:** <br>
        If you're seeing this, we need to consider using OOP for the minimal TUI. 
        Each Screen needs it's own class so that we can just import when we need it.
        Idk about you guys but labels are complete shit so if you need one, 
        just use d.add(x, y, "whatever text") and it will convert automatically. For example:

        d.add(mid_x-15, 12, "Username:")

[Sat May 2, 00:24]
- Kivy Application
    - Completed Login screen
    - Started on chat page
    - Added Kivy script to make the python script less bloated
    - Resolved Clock.max_iteration issue

[Thur Apr 23, 03:08]

- Kivy Application
    - Fixed Login screen, looks more sensible.
    - Getting a Criticial warning, Clock.max_iteration
    - Added Roboto Condensed Regular Font

[Wed Apr 22, 13:14]

- Created a kivy application
    - Designed Base Structure of the GUI
    - Designed Login screen. (Currently a clusterf**k but minor changes are required)
    - Created base classes for the main chat app and the create account sceen

- Created the hurbIM logo - black version and white version with border (Check gui/)

- Added vscode settings to .gitignore
