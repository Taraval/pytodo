## Installation

	PROJECT="~/.ezpc"
	USERNAME="taraval"
	REPO="pytodo"
	PATHX_USERNAME=$PROJECT/$USERNAME
	PATHX=$PATHX_USERNAME/$REPO

    mkdir -p $PATHX_USERNAME
    cd $PATHX_USERNAME
    git clone https://github.com/taraval/pytodo
	echo "alias t='$PATHX/todo'" > ~/.bashrc

## Remove me
