#!/bin/bash


slack_key="$(cat credentials/slack-auth)"
# labels="$(python vision.py)"
python3 vision.py | grep -v Corrupt
status=$?
# echo "labels =asdas $labels end labels"
# keep=0
# new_labels=""
# while read -r line; do
#     if [ keep = 1 ] ; then
#         echo "label= $line"
#         new_labels += "$line"
#     fi
#     if [ "$line" = "Labels:" ] ; then
#         keep=1
#     fi
# done <<< "$labels"
# echo "new_labels = $new_labels"
if  [ status = 1 ] || [ ! -f "labels.txt" ] || [ ! -f "out.jpg" ] ; then
    echo "Vision failed to output files"
    exit 1
fi
labels="$(cat labels_ez.txt)"
curl -F "file=@out.jpg" -F "initial_comment=This is an image of: $labels" -F channels=CKT9VBX08 -H "Authorization: Bearer $slack_key" https://slack.com/api/files.upload