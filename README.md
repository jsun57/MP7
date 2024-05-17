# MP7
https://download.jetbrains.com/python/pycharm-professional-2023.1.5-aarch64.dmg?_ga=2.7647991.491967528.1715789054-256653589.1715789054&_gl=1*wk6ajj*_ga*MjU2NjUzNTg5LjE3MTU3ODkwNTQ.*_ga_9J976DJZ68*MTcxNTc4OTA1NC4xLjEuMTcxNTc4OTMwNy42MC4wLjA.

alias cls='printf "\33c\e[3J"'


# Source the shared .bashrc for global aliases and functions
if [ -f /shared/config/.bashrc ]; then
    source /shared/config/.bashrc
fi

# Set global PIP configuration file
export PIP_CONFIG_FILE=/shared/config/pip.conf

# Conda configuration
if [ -f /shared/config/.condarc ]; then
    export CONDARC=/shared/config/.condarc
fi

# Node-specific settings (if any)
# For example, setting PATH for tools installed only on this node
export PATH="/usr/local/node-specific/bin:$PATH"
