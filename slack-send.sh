
slack_key="$(cat credentials/slack-auth)"
labels="$(python vision.py)"
status=$?
echo "$labels"
keep=0
new_labels=""
for label in labels ; do
    if [ keep = 0 ] ; then
        new_labels += "$label"
    fi
done
echo "$new_labels"
if  [ status = 1 ] ; then
    echo "Vision failed to output file"
    exit 1
fi
curl -F "file=@out.jpg" -F "initial_comment=$labels" -F channels=CKT9VBX08 -H "Authorization: Bearer $slack_key" https://slack.com/api/files.upload