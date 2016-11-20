## Installation

    PROJECT="$HOME/.ezpc" 
    USERNAME="taraval"
    REPO="pytodo"
    PATHX_USERNAME=$PROJECT/$USERNAME
    PATHX=$PATHX_USERNAME/$REPO
    mkdir -p $PATHX_USERNAME
    cd $PATHX_USERNAME
    git clone https://github.com/taraval/pytodo
    echo "alias t='python $PATHX/todo.py'" >> ~/.bashrc

## Remove me
