## Installation

    PROJECT="$HOME/.ezpc" 
    USERNAME="taraval"
    REPO="pytodo"
    BASHRC="$HOME/.bashrc"
    PATHX_USERNAME=$PROJECT/$USERNAME
    PATHX=$PATHX_USERNAME/$REPO
    mkdir -p $PATHX_USERNAME
    cd $PATHX_USERNAME
    git clone https://github.com/taraval/pytodo
    echo "### BEGIN: $USERNAME/$REPO ###
    echo "alias t-upgrade='cd $PATHX; git pull; cd $HOME'" >> $BASHRC
    echo "alias t='python $PATHX/todo.py'" >> $BASHRC
    echo "### END: $USERNAME/$REPO ###
    export $BASHRC

## Remove me
