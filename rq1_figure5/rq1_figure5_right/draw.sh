#!/bin/bash
curl https://api.ossinsight.io/q/analyze-pull-request-open-to-merged?repoId=207181317 > data/open-to-merged.json
curl https://api.ossinsight.io/q/analyze-pull-requests-size-per-month?repoId=207181317 > data/number_pr.json
cd code

# draw a vertical picture 
python3 draw.py

# draw a horizontal picture
python3 draw_horizontal.py
cd ..