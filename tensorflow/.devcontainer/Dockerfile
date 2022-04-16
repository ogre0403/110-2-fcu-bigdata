FROM ogre0403/latex:basic-collection

RUN apk update && apk --no-cache add perl wget && \
    tlmgr option repository http://mirror.ctan.org/systems/texlive/tlnet && \
    tlmgr -repository http://mirror.ctan.org/systems/texlive/tlnet install && \
    tlmgr install algpseudocodex algorithmicx algorithms && \
    tlmgr install minted && apk --no-cache add py3-pygments && \
    apk del perl wget