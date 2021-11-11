# Klip's Dotfiles
.dotfiles setup using chezmoi for mac or ubuntu(WIP).  

## Installation

1. Install [chezmoi](https://github.com/twpayne/chezmoi)
    - On Mac OS:
        - install [brew](https://brew.sh/) to install stuff on MacOS
        - install [chezmoi](https://github.com/twpayne/chezmoi) to manage dotfiles
        ```shell
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        brew install chezmoi
        ```

2. Init dotfiles
  - `chezmoi init --apply --verbose https://github.com/GitKlip/dotfiles.git`
3. If you want to set up your computer automatically
  - On Mac:
    - `~/.dotfiles/setup/osx.sh`
    - Open Terminal.app, then Preferences -> Profiles
      - Profile: Desert (click Default button to make it default one)
      - Font: Fira Code (should be already selected)
  - On Ubuntu
    - `~/.dotfiles/setup/ubuntu.sh`

Provide your user account password if BECOME password is asked.


## What it will do
- [ ] MacOS:
  - [ ] configure command/control keys to so control key works as expected in IDE
  - [ ] set bash as the shell default (bash is the least-common-denominator when it comes to shells) `chsh -s /bin/bash`
- [ ] shell config (choice of zsh or bash)
  - [ ] [zsh](https://ohmyz.sh/) - `bash` replacement. `.dotfiles` folder includes a lot of additional stuff for `zsh`.
  - [ ] bash - since it's the least common denominator on many systems, may want to go with bash.
- [ ] pyenv - lets you easily switch between multiple versions of Python. It’s simple, unobtrusive, and is a single-purpose tool
- [ ] pyenv-virtualenv - a pyenv plugin that provides features to manage virtualenvs and conda environments for Python on UNIX-like systems
- [ ] [VS Code](https://code.visualstudio.com/) - development IDE. `brew cask install visual-studio-code` Following settings will automatically applied:
        <!-- - font changed to Fira Code -->
        <!-- - ligatures enabled -->
        - rulers at width 80, 100, 120, 150 are added
        - autosave enabled
        - preview mode disabled (clicking the file opens it in a persistant editor)
        - extentions automatically installed:
            <!-- - Gitlens -->
            <!-- - Tslint -->
            <!-- - Eslint -->
            <!-- - Prettier -->
            - 'Dark+ (color blind)' by PedroFonsecaDEV
            - dbt Power User
            - Python
            - GitHub Pull Requests and Issues
- [ ] [Postman](https://www.getpostman.com/) - API development and testing tool.
- [ ] [Docker](https://www.docker.com/) - application containerization.
- [ ] `brew install wget`





## RESOURCES
- https://github.com/twpayne/dotfiles
- https://github.com/Amar1729/dotfiles
- https://github.com/jasonmorganson/dotfiles

- https://www.youtube.com/watch?v=L_Y3s0PS_Cg
- https://www.jacobbolda.com/chezmoi-dotfile-management
- https://github.com/ChristopherBiscardi/dotfiles
- https://github.com/benmezger/dotfiles

- https://www.moncefbelyamani.com/automating-the-setup-of-a-new-mac-with-all-your-apps-preferences-and-development-tools/
- https://github.com/monfresh/dotfiles

- https://dotfiles.github.io/
- https://dotfiles.github.io/inspiration/
- https://github.com/jtprince/dotfiles
- https://about.gitlab.com/blog/2020/04/17/dotfiles-document-and-automate-your-macbook-setup/
- https://github.com/twpayne/chezmoi
- https://github.com/twpayne/chezmoi/blob/master/docs/COMPARISON.md

- pyenv - lets you easily switch between multiple versions of Python. It’s simple, unobtrusive, and is a single-purpose tool
    * https://jordanthomasg.medium.com/python-development-on-macos-with-pyenv-2509c694a808
    * https://chamikakasun.medium.com/how-to-manage-multiple-python-versions-in-macos-2021-guide-f86ef81095a6
* pyenv-virtualenv - a pyenv plugin that provides features to manage virtualenvs and conda environments for Python on UNIX-like systems
    * https://jordanthomasg.medium.com/python-development-on-macos-with-pyenv-virtualenv-ec583b92934c





