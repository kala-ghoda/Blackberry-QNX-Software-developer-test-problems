tail -n +2 requirements.txt | xargs -I{} pip3 install {}
