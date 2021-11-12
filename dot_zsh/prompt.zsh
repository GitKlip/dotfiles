# https://scriptingosx.com/2019/07/moving-to-zsh-06-customizing-the-zsh-prompt/
# SPECIAL CODES
# %(?.√.?%?)	if return code ? is 0, show √, else show ?%?
# %?	        exit code of previous command
# %1~	        current working dir, shortening home to ~, show only last 1 element
# %#	        # with root privileges, % otherwise
# %B %b	        start/stop bold
# %F{...}	    text (foreground) color, see table
# %f	        reset to default textcolor
# %!          %h Current history event number
# %#          # if superuser, else %
# %%          A single %
# %)          A ) (use with %X(.tstr.fstr))
# %*          Time in 24­hour format with seconds
# %/          %d $PWD; n gives trailing parts, -n leading
# %c          %. %C Deprecated alternatives, differ by default n
# %?          Return status of last command
# %@          %t Time of day in am/pm format
# %B          (%b) Start (stop) bold face mode
# %D          %D{str} Date as YY-MM-DD, optional strftime spec
# %E          Clear to end of line
# %i          Script/function line number ($LINENO)
# %j          Number of jobs as listed by jobs
# %L          Shell depth ($SHLVL)
# %l          Login terminal without /dev or /dev/tty
# %M          Full host name
# %m          Host name to first dot or n dots
# %N          Name of script, function, sourced file
# %n          Name of user (same as $USERNAME)
# %S          %s Start (stop) standout mode
# %T          Time of day, 24­hour format
# %U          %u Start (stop) underline mode (patchy support)
# %v          nth component of $psvar array
# %W          Date as middle­endian MM/DD/YY
# %w          Date as DAY DD
# %y          Login terminal without /dev
# %_          Parser state (continuation lines, debug)
# %~          Like %/, %d but with tilde substitution
# %{esc%}     Escape sequence esc doesn’t move cursor
# %X(.tstr.fstr)  tstr if test X gives n, else fstr
# %<str<      Truncate to n on left, str on left if so
# %>str>      Truncate to n on right, str on right if so


PROMPT='%(?.%F{green}√.%F{red}?%?)%f

%F{blue}~~~ %n@%m ~~~%f
[%F{yellow}%~%f] $ '

PS1=$PROMPT

# SHOW GIT BRANCH/REPO
autoload -Uz vcs_info
precmd_vcs_info() { vcs_info }
precmd_functions+=( precmd_vcs_info )
setopt prompt_subst
RPROMPT=\$vcs_info_msg_0_
zstyle ':vcs_info:git:*' formats '%F{240}(%b)%r%f'
zstyle ':vcs_info:*' enable git