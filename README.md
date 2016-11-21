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
    echo "### BEGIN: $USERNAME/$REPO ###" >> $BASHRC
    echo "alias t-upgrade='cd $PATHX; git pull; cd $HOME'" >> $BASHRC
    echo "alias t='python $PATHX/todo.py'" >> $BASHRC
    echo "### END: $USERNAME/$REPO ###" >> $BASHRC
    export $BASHRC

## Remove me
