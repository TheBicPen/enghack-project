# enghack-project

A collection of scripts to take pictures from a webcam, and use the Google Cloud Vision API to detect objects within the images.
Based on the content of the images, messages are posted to a Slack server. Also contains features for moderating the Slack channels, as well as filtering the images posted.

Possible uses:
- automatic announcements when there is activity near the camera
- announcements based on object detection, eg: posting 'Lunchtime!' when food is detected
- security: motion detection
